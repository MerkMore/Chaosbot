# Placer.py
# Makes text for building placement
# put the output   starting from "#####"   in a file "placement.txt"
# author: MerkMore
# version 5 july 2020
import layout_if
import random



class prog:
#   
    filterresult = set()
    startsquare = (0,0)
    rampcenter = (0,0)
    center = (0,0)
    logging = False

    def main(self):
        layout_if.load_layout()
#       write placement.png
#       
        print('put next lines in a file   placement.txt')
        print('#####')
        mapplace = 'map: '+layout_if.mapname+' '+str(layout_if.startx)+' '+str(layout_if.starty)
        print(mapplace)
#
#       startx,y can be 36.5,112.5 but we identify that square with the tuple (36,112)
        self.startsquare = (round(layout_if.startx-0.5),round(layout_if.starty-0.5))          
#       We will work with sets of squares.
        startcc = set([self.startsquare])
        self.extend(startcc)
        self.logg('startcc '+str(len(startcc)))
        self.get_edge(startcc)
        aroundcc = self.edge.copy()
        self.logg('aroundcc '+str(len(aroundcc)))
        basearea = aroundcc.copy()
        self.extend(basearea)
        self.logg('basearea '+str(len(basearea)))
        self.get_edge(basearea)
        ramp = self.edge.copy()
        self.filter_color(ramp,2)
        ramp = self.filterresult.copy()
        self.logg('ramp '+str(len(ramp)))
        self.get_edge(ramp)
        aroundramp = self.edge.copy()
        self.filter_color(aroundramp,0)
        aroundramp = self.filterresult.copy()
        self.logg('aroundramp '+str(len(aroundramp)))
        if self.has_path(aroundramp,aroundcc):
            self.logg('path found')
        else:
            self.logg('no path found')
#       now we try to close the path with the 3 blocks
#       make totry. That is possible positions for blocks to be put 
        self.get_center(aroundramp)
        self.rampcenter = self.center
#       for blocks, the position is described by the leftunder corner
        totry = set()
        for dx in range(-6,6):
            for dy in range(-6,6):
                square = (self.rampcenter[0]+dx,self.rampcenter[1]+dy)
                if self.get_color(square) == 0:
                    totry.add(square)
        self.logg('per block '+str(len(totry))+' positions')
        solutions = []
        for b0 in totry:
            if self.tryplace(2,b0):
                self.logg('trying block 0 at '+str(b0[0])+' '+str(b0[1]))
                for b1 in totry:
                    if (b1[0]>b0[0]) or ((b1[0]==b0[0]) and (b1[1]>b0[1])):
                        if self.tryplace(2,b1):
                            self.logg('   trying block 1 at '+str(b1[0])+' '+str(b1[1]))
                            for b2 in totry:
                                if self.tryplace(3,b2):
                                    if not self.has_path(aroundramp,aroundcc):
                                        solutions.append((b0,b1,b2))
                                        self.logg('      a solution')
                                    self.colorplace(3,b2,0)
                            self.colorplace(2,b1,0)
                self.colorplace(2,b0,0)
        self.logg('found '+str(len(solutions))+' 3-block ramp blocking solutions')
        if len(solutions)>0:
            asol = solutions[0]
            for (b0,b1,b2) in solutions:
                self.colorplace(2,b0,4)
                self.colorplace(2,b1,4)
                if self.can_place_shape(1,b2):
                    asol = (b0,b1,b2)
                self.colorplace(2,b0,0)
                self.colorplace(2,b1,0)
            print('position SUPPLYDEPOT '+str(asol[0][0]+1)+' '+str(asol[0][1]+1))
            print('position SUPPLYDEPOT '+str(asol[1][0]+1)+' '+str(asol[1][1]+1))
            print('position BARRACKS '+str(asol[2][0]+1.5)+' '+str(asol[2][1]+1.5))
#       now, find some hidden fusioncore positions
        for shape in (0,2):
            alters = []
            while len(alters)<10000:
                alt = (random.randrange(0,200),random.randrange(0,200))
                dis = self.sdist(alt,self.startsquare)
                if (dis>25*25) and (dis<70*70):
                    dis = self.sdist(alt,self.rampcenter)
                    if (dis>25*25):
                        if self.can_place_shape(shape,alt):
                            alters.append(alt)
            choices = []
            middle = (100,100)
            while len(choices)<7:
                bestdist = 0
                for alt in alters:
                    allowed = True
                    for have in choices:
                        dis = self.sdist(alt,have)
                        allowed = allowed and (dis>12*12)
                    if allowed:
                        dis = self.sdist(alt,middle)
                        if dis>bestdist:
                            best = alt
                            bestdist = dis
                choices.append(best)
            for alt in choices:
                self.do_place_shape(shape,alt)
                if shape == 0:
                    print('position FUSIONCORE * '+str(alt[0]+1.5)+' '+str(alt[1]+1.5))
                else:
                    print('position STARPORT * '+str(alt[0]+1.5)+' '+str(alt[1]+1.5))
        layout_if.photo_layout()
        print('#####')






    def do_place_shape(self,shape,alt):
#       leftunder definition
        if shape == 0:
#           fusioncore
            layout_if.layout[alt[0]+0][alt[1]+0] = 4
            layout_if.layout[alt[0]+0][alt[1]+1] = 4
            layout_if.layout[alt[0]+0][alt[1]+2] = 4
            layout_if.layout[alt[0]+1][alt[1]+0] = 4
            layout_if.layout[alt[0]+1][alt[1]+1] = 4
            layout_if.layout[alt[0]+1][alt[1]+2] = 4
            layout_if.layout[alt[0]+2][alt[1]+0] = 4
            layout_if.layout[alt[0]+2][alt[1]+1] = 4
            layout_if.layout[alt[0]+2][alt[1]+2] = 4
        else:
#           starport                                 
            layout_if.layout[alt[0]+0][alt[1]+0] = 4
            layout_if.layout[alt[0]+0][alt[1]+1] = 4
            layout_if.layout[alt[0]+0][alt[1]+2] = 4
            layout_if.layout[alt[0]+1][alt[1]+0] = 4
            layout_if.layout[alt[0]+1][alt[1]+1] = 4
            layout_if.layout[alt[0]+1][alt[1]+2] = 4
            layout_if.layout[alt[0]+2][alt[1]+0] = 4
            layout_if.layout[alt[0]+2][alt[1]+1] = 4
            layout_if.layout[alt[0]+2][alt[1]+2] = 4
            layout_if.layout[alt[0]+3][alt[1]+0] = 4
            layout_if.layout[alt[0]+3][alt[1]+1] = 4
            layout_if.layout[alt[0]+4][alt[1]+0] = 4
            layout_if.layout[alt[0]+4][alt[1]+1] = 4


    def can_place_shape(self,shape,alt) -> bool:
#       leftunder definition
        can = True
        if shape == 0:
#           fusioncore
            can = can and (layout_if.layout[alt[0]+0][alt[1]+0] == 0)
            can = can and (layout_if.layout[alt[0]+0][alt[1]+1] == 0)
            can = can and (layout_if.layout[alt[0]+0][alt[1]+2] == 0)
            can = can and (layout_if.layout[alt[0]+1][alt[1]+0] == 0)
            can = can and (layout_if.layout[alt[0]+1][alt[1]+1] == 0)
            can = can and (layout_if.layout[alt[0]+1][alt[1]+2] == 0)
            can = can and (layout_if.layout[alt[0]+2][alt[1]+0] == 0)
            can = can and (layout_if.layout[alt[0]+2][alt[1]+1] == 0)
            can = can and (layout_if.layout[alt[0]+2][alt[1]+2] == 0)
        else:
#           starport                                 
            can = can and (layout_if.layout[alt[0]+0][alt[1]+0] == 0)
            can = can and (layout_if.layout[alt[0]+0][alt[1]+1] == 0)
            can = can and (layout_if.layout[alt[0]+0][alt[1]+2] == 0)
            can = can and (layout_if.layout[alt[0]+1][alt[1]+0] == 0)
            can = can and (layout_if.layout[alt[0]+1][alt[1]+1] == 0)
            can = can and (layout_if.layout[alt[0]+1][alt[1]+2] == 0)
            can = can and (layout_if.layout[alt[0]+2][alt[1]+0] == 0)
            can = can and (layout_if.layout[alt[0]+2][alt[1]+1] == 0)
            can = can and (layout_if.layout[alt[0]+2][alt[1]+2] == 0)
            can = can and (layout_if.layout[alt[0]+3][alt[1]+0] == 0)
            can = can and (layout_if.layout[alt[0]+3][alt[1]+1] == 0)
            can = can and (layout_if.layout[alt[0]+4][alt[1]+0] == 0)
            can = can and (layout_if.layout[alt[0]+4][alt[1]+1] == 0)
        return can






    def logg(self,stri):
        if self.logging:
            print(stri)
    
    def colorplace(self,am,square,color):
        if am==2:
            layout_if.layout[square[0]+0][square[1]+0] = color
            layout_if.layout[square[0]+0][square[1]+1] = color
            layout_if.layout[square[0]+1][square[1]+0] = color
            layout_if.layout[square[0]+1][square[1]+1] = color
        if am==3:
            layout_if.layout[square[0]+0][square[1]+0] = color
            layout_if.layout[square[0]+0][square[1]+1] = color
            layout_if.layout[square[0]+0][square[1]+2] = color
            layout_if.layout[square[0]+1][square[1]+0] = color
            layout_if.layout[square[0]+1][square[1]+1] = color
            layout_if.layout[square[0]+1][square[1]+2] = color
            layout_if.layout[square[0]+2][square[1]+0] = color
            layout_if.layout[square[0]+2][square[1]+1] = color
            layout_if.layout[square[0]+2][square[1]+2] = color


    def tryplace(self,am,square):
        can = True
        if am==2:
            can = can and (layout_if.layout[square[0]+0][square[1]+0] == 0)
            can = can and (layout_if.layout[square[0]+0][square[1]+1] == 0)
            can = can and (layout_if.layout[square[0]+1][square[1]+0] == 0)
            can = can and (layout_if.layout[square[0]+1][square[1]+1] == 0)
            touching = False
            touching = touching or (layout_if.layout[square[0]-1][square[1]+0] != 0)
            touching = touching or (layout_if.layout[square[0]-1][square[1]+1] != 0)
            touching = touching or (layout_if.layout[square[0]+0][square[1]+2] != 0)
            touching = touching or (layout_if.layout[square[0]+1][square[1]+2] != 0)
            touching = touching or (layout_if.layout[square[0]+2][square[1]+0] != 0)
            touching = touching or (layout_if.layout[square[0]+2][square[1]+1] != 0)
            touching = touching or (layout_if.layout[square[0]+0][square[1]-1] != 0)
            touching = touching or (layout_if.layout[square[0]+1][square[1]-1] != 0)
            can = can and touching
        if am==3:
            can = can and (layout_if.layout[square[0]+0][square[1]+0] == 0)
            can = can and (layout_if.layout[square[0]+0][square[1]+1] == 0)
            can = can and (layout_if.layout[square[0]+0][square[1]+2] == 0)
            can = can and (layout_if.layout[square[0]+1][square[1]+0] == 0)
            can = can and (layout_if.layout[square[0]+1][square[1]+1] == 0)
            can = can and (layout_if.layout[square[0]+1][square[1]+2] == 0)
            can = can and (layout_if.layout[square[0]+2][square[1]+0] == 0)
            can = can and (layout_if.layout[square[0]+2][square[1]+1] == 0)
            can = can and (layout_if.layout[square[0]+2][square[1]+2] == 0)
            touching = False
            touching = touching or (layout_if.layout[square[0]-1][square[1]+0] != 0)
            touching = touching or (layout_if.layout[square[0]-1][square[1]+1] != 0)
            touching = touching or (layout_if.layout[square[0]-1][square[1]+2] != 0)
            touching = touching or (layout_if.layout[square[0]+3][square[1]+0] != 0)
            touching = touching or (layout_if.layout[square[0]+3][square[1]+1] != 0)
            touching = touching or (layout_if.layout[square[0]+3][square[1]+2] != 0)
            touching = touching or (layout_if.layout[square[0]+0][square[1]-1] != 0)
            touching = touching or (layout_if.layout[square[0]+1][square[1]-1] != 0)
            touching = touching or (layout_if.layout[square[0]+2][square[1]-1] != 0)
            touching = touching or (layout_if.layout[square[0]+0][square[1]+3] != 0)
            touching = touching or (layout_if.layout[square[0]+1][square[1]+3] != 0)
            touching = touching or (layout_if.layout[square[0]+2][square[1]+3] != 0)
            can = can and touching
        if can:
            self.colorplace(am,square,4)
        return can


    def get_color(self,square) -> int:
        return layout_if.layout[square[0]][square[1]]

    def get_neighbours(self,square):
        self.neighbours = set()
        self.neighbours.add((square[0]-1,square[1]))
        self.neighbours.add((square[0],square[1]-1))
        self.neighbours.add((square[0]+1,square[1]))
        self.neighbours.add((square[0],square[1]+1))
        self.neighbours.add((square[0]-1,square[1]-1))
        self.neighbours.add((square[0]+1,square[1]-1))
        self.neighbours.add((square[0]+1,square[1]+1))
        self.neighbours.add((square[0]-1,square[1]+1))
        
    def extend(self,aset):
#       aset is enlarged with same-colored squares
        square = aset.pop()
        aset.add(square)
        mycolor = self.get_color(square)
        smallset = set()
        bigset = aset
        while len(smallset)<len(bigset):
            smallset = bigset.copy()
            for square in smallset:
                self.get_neighbours(square)
                for nsquare in self.neighbours:
                    if self.get_color(nsquare) == mycolor:
                        bigset.add(nsquare)
        aset = bigset.copy()

    def get_edge(self,aset):
#       self.edge is the squares around aset
        square = aset.pop()
        aset.add(square)
        mycolor = self.get_color(square)
        self.edge = set()
        for square in aset:
            self.get_neighbours(square)
            for nsquare in self.neighbours:
                if self.get_color(nsquare) != mycolor:
                    self.edge.add(nsquare)

    def filter_color(self,aset,mustcolor):
        wrong = set()        
        for square in aset:
            if self.get_color(square) != mustcolor:
                wrong.add(square)
        self.filterresult = aset - wrong

    def get_center(self,aset):
#       self.center is a square near the middle of aset
        n = len(aset)
        sumx = 0
        sumy = 0
        for square in aset:
            sumx = sumx + square[0] 
            sumy = sumy + square[1]
        avgx = round(sumx/n)
        avgy = round(sumy/n) 
        self.center = (avgx,avgy)

    def make_spo(self,aset):
#       list self.spo with (x,y,sd) from aset
        self.spo = []
        for square in aset:
            sd = self.sdist(square,self.startsquare)
            self.spo.append((square[0],square[1],sd))
            thigh = len(self.spo)-1
            while thigh>0:
                tlow = (thigh-1)//2
                if self.spo[thigh][2]<self.spo[tlow][2]:
                    hold = self.spo[thigh]
                    self.spo[thigh] = self.spo[tlow]
                    self.spo[tlow] = hold
                thigh = tlow
                
    def pop_spo(self):
        square = (self.spo[0][0],self.spo[0][1])
        thigh = len(self.spo)-1
        self.spo[0] = self.spo[thigh]
        del self.spo[thigh]
        n = len(self.spo)
        tlow = 0
        while tlow<n:
            tleft = 2*tlow+1
            tright = 2*tlow+2
            thigh = tleft
            if tright<n:
                if self.spo[tright][2]<self.spo[tleft][2]:
                    thigh = tright
            if thigh<n:
                if self.spo[thigh][2]<self.spo[tlow][2]:
                    hold = self.spo[thigh]
                    self.spo[thigh] = self.spo[tlow]
                    self.spo[tlow] = hold
            tlow = thigh


    def add_spo(self,square):
#       square should not be in spo yet
        sd = self.sdist(square,self.startsquare)
        self.spo.append((square[0],square[1],sd))
        thigh = len(self.spo)-1
        while thigh>0:
            tlow = (thigh-1)//2
            if self.spo[thigh][2]<self.spo[tlow][2]:
                hold = self.spo[thigh]
                self.spo[thigh] = self.spo[tlow]
                self.spo[tlow] = hold
            thigh = tlow


    def has_path(self,in_aset,bset) -> bool:
#       bset should be near self.startsquare
        aset = in_aset.copy()
        self.filter_color(aset,0)
        aset = self.filterresult.copy()
        if len(aset) == 0:
            hp = False
        else:
            if len(aset & bset) > 0:
                hp = True
            else:
                hp = False
                self.make_spo(aset)
                seen = aset.copy()
                while (len(self.spo)>0) and (not hp):
                    square = self.spo[0]
                    self.pop_spo()
                    self.get_neighbours(square)
                    for nsquare in self.neighbours:
                        if self.get_color(nsquare) == 0:
                            if nsquare not in seen:
                                seen.add(nsquare)
                                hp = hp or (nsquare in bset)
                                self.add_spo(nsquare)
        return hp        


#   distance
    def sdist(self,p,q) -> int:
        return (p[0]-q[0])**2 + (p[1]-q[1])**2
 

solo = prog()
solo.main()

            
