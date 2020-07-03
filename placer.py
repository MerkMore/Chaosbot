# Placer.py
# Makes text for building placement
# put the output   starting from "#####"   in a file "placement.txt"
# author: MerkMore
# version 2 july 2020
import layout_if
import random



class prog:
#   
    filterresult = set()
    center = None


    def main(self):
        layout_if.load_layout()
#       write placement.png
#       
        print('put next lines in a file   placement.txt')
        print('#####')
        mapplace = 'map: '+layout_if.mapname+' '+str(layout_if.startx)+' '+str(layout_if.starty)
        print(mapplace)
#
        layout_if.photo_layout()
#
#       startx,y can be 36.5,112.5 but we identify that square with the tuple (36,112)
        self.center = (round(layout_if.startx-0.5),round(layout_if.starty-0.5))          
#       We will work with sets of squares.
        startpos = set([self.center])
        startcc = startpos.copy()
        self.extend(startcc)
        print('startcc '+str(len(startcc)))
        self.get_edge(startcc)
        aroundcc = self.edge.copy()
        print('aroundcc '+str(len(aroundcc)))
        basearea = aroundcc.copy()
        self.extend(basearea)
        print('basearea '+str(len(basearea)))
        self.get_edge(basearea)
        ramp = self.edge.copy()
        self.filter_color(ramp,2)
        ramp = self.filterresult.copy()
        print('ramp '+str(len(ramp)))
        self.get_edge(ramp)
        aroundramp = self.edge.copy()
        self.filter_color(aroundramp,0)
        aroundramp = self.filterresult.copy()
        print('aroundramp '+str(len(aroundramp)))
        if self.has_path(aroundramp,aroundcc):
            print('path found')
        else:
            print('no path found')


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
            sd = self.sdist(square,self.center)
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
        tlow = 0
        while tlow<len(self.spo):
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
        sd = self.sdist(square,self.center)
        self.spo.append((square[0],square[1],sd))
        thigh = len(self.spo)-1
        while thigh>0:
            tlow = (thigh-1)//2
            if self.spo[thigh][2]<self.spo[tlow][2]:
                hold = self.spo[thigh]
                self.spo[thigh] = self.spo[tlow]
                self.spo[tlow] = hold
            thigh = tlow


    def has_path(self,aset,bset) -> bool:
        self.filter_color(aset,0)
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
                    self.pop_spo
                    self.get_neighbours(square)
                    for nsquare in self.neighbours:
                        if self.get_color(nsquare) == 0:
                            if nsquare not in seen:
                                seen.add(nsquare)
                                hp = hp or (nsquare in bset)
                                self.add_spo(nsquare)
        print('work '+str(len(seen)))
        return hp        






    def realized(self):
        print('----------------')
        for (srt,siz) in self.all_structures:
            for bui in self.structures(srt):
                place = bui.position
                x = round(place.x*2)/2
                y = round(place.y*2)/2
                print('position '+srt.name+' '+str(x)+' '+str(y))
                for vakx in range(round(x-siz/2),round(x+siz/2)):
                    for vaky in range(round(y-siz/2),round(y+siz/2)):
                        layout_if.layout[vakx][vaky] = 4


#   distance
    def sdist(self,p,q) -> int:
        return (p[0]-q[0])**2 + (p[1]-q[1])**2
 

solo = prog()
solo.main()

            
