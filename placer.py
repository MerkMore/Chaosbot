# Placer.py
# Makes text for building placement
# appends the output to file "placement.txt"
# author: MerkMore
# version 11 aug 2020
from layout_if_py import layout_if
import random
from math import sqrt, sin, cos, acos, pi



class prog:
#
    mapplace = ''
    filterresult = set()
    startsquare = (0,0)
    enemystartsquare = (0,0)
    rampcenter = (0,0)
    center = (0,0)
    logging = False
#   the map with walk-distances to enemystartsquare
    walking = []

    def main(self):
        layout_if.load_layout()
        print('I can append to placement.txt')
        self.mapplace = 'map: '+layout_if.mapname+' '+str(layout_if.startx)+' '+str(layout_if.starty)
        print('looking for:   '+self.mapplace)
        text = open('placement.txt','r')
        content = text.read().splitlines()
        for line in content:
            if (line[0] == 'm') and (line[1] == 'a') and (line[2] == 'p'):
                print(line)
        text.close()
        if self.mapplace in content:
            print('No action, the map is already in placement.txt')
        else:
            print('Not found, so I will append to placement.txt')
            self.appendthemap()


    def appendthemap(self):
        text = open('placement.txt','a')
        text.write('#####'+'\n')
        text.write(self.mapplace+'\n')
#
#       startx,y can be 36.5,112.5 but we identify that square with the tuple (36,112)
        self.startsquare = (round(layout_if.startx-0.5),round(layout_if.starty-0.5))
        self.enemystartsquare = (round(layout_if.enemyx - 0.5), round(layout_if.enemyy - 0.5))
        self.logg('enemy start '+str(self.enemystartsquare[0])+' '+str(self.enemystartsquare[1]))
#       We will work with sets of squares.
        enemybasearea = set([self.enemystartsquare])
        self.extend(enemybasearea)
        self.logg('enemybasearea '+str(len(enemybasearea)))
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
            text.write('position SUPPLYDEPOT '+str(asol[0][0]+1)+' '+str(asol[0][1]+1)+'\n')
            text.write('position SUPPLYDEPOT '+str(asol[1][0]+1)+' '+str(asol[1][1]+1)+'\n')
            text.write('position BARRACKS '+str(asol[2][0]+1.5)+' '+str(asol[2][1]+1.5)+'\n')
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
                    text.write('position FUSIONCORE * '+str(alt[0]+1.5)+' '+str(alt[1]+1.5)+'\n')
                else:
                    text.write('position STARPORT * '+str(alt[0]+1.5)+' '+str(alt[1]+1.5)+'\n')
#       walking
        self.walking = []
        for col in range(0, 200):
            collist = []
            for row in range(0, 200):
                collist.append(-1)
            self.walking.append(collist)
        self.walking[self.enemystartsquare[0]][self.enemystartsquare[1]] = 0
        dist = 0
#       edge will contain all squares with dist
        edge = [self.enemystartsquare]
        while len(edge)>0:
            self.logg('edge ' + str(len(edge)))
            dist = dist+1
            new_edge = []
            for square in edge:
                self.get_neighbours(square)
                for nsquare in self.neighbours:
                    if self.walking[nsquare[0]][nsquare[1]] == -1:
                        if layout_if.layout[nsquare[0]][nsquare[1]] in (0,2,5):
                            self.walking[nsquare[0]][nsquare[1]] = dist
                            new_edge.append(nsquare)
            edge = new_edge.copy()
#       now we will estimate a high value of walking-flying
#       also slightly negative weigh in the flydistance to home
        best = -999
        for pog in range(0,1000):
            square = (random.randrange(0,200),random.randrange(0,200))
            walk = self.walking[square[0]][square[1]]
            if walk >= 0:
                wafy = (walk - self.fly(square,self.enemystartsquare))-0.1*self.fly(square,self.startsquare)
                if wafy>best:
                    best = wafy
                    bestsquare = square
#       now we hope to place a single barracks there
        leftunder = (bestsquare[0]-1,bestsquare[1]-1)
        placed = self.can_place_shape(0,leftunder)
        barracksresult = leftunder
        dist = 0
        while not placed:
            dist = dist+1
            for dx in range(-dist,dist):
                for dy in range(-dist,dist):
                    maybe = (leftunder[0]+dx,leftunder[1]+dy)
                    if self.can_place_shape(0,maybe):
                        barracksresult = maybe
                        placed = True
#       if not unlucky, this result is a good cheese building place
        text.write('position CHEESEBARRACKS '+str(barracksresult[0]+1.5)+' '+str(barracksresult[1]+1.5)+'\n')
        # do not draw the barracks, as later we want to place a tank here
        # self.do_place_shape(0,barracksresult)
#       get infested_factory place, about 8 from the infestedbarracks, away from the enemy
        vector = (barracksresult[0]-self.enemystartsquare[0],barracksresult[1]-self.enemystartsquare[1])
        factor = 8/sqrt(self.sdist(barracksresult,self.enemystartsquare))
        factorysuggestion = (round(barracksresult[0]+factor*vector[0]),round(barracksresult[1]+factor*vector[1]))
#       now we hope to place a factory there
        leftunder = (factorysuggestion[0]-1,factorysuggestion[1]-1)
        placed = self.can_place_shape(1,leftunder)
        factoryresult = leftunder
        dist = 0
        while not placed:
            dist = dist+1
            for dx in range(-dist,dist):
                for dy in range(-dist,dist):
                    maybe = (leftunder[0]+dx,leftunder[1]+dy)
                    if self.can_place_shape(1,maybe):
                        factoryresult = maybe
                        placed = True
#       if not unlucky, this result is a good cheese building place
        text.write('position CHEESEFACTORY '+str(factoryresult[0]+1.5)+' '+str(factoryresult[1]+1.5)+'\n')
        self.do_place_shape(1,factoryresult)
#       go find a corner in the enemy base
        corners = set()
        for square in enemybasearea:
            ownneighs = 0
            self.get_neighbours(square)
            for nsquare in self.neighbours:
                if self.get_color(nsquare) == 0:
                    ownneighs = ownneighs+1
            if ownneighs <= 4:
                corners.add(square)
        best = None
        bestdist = 80000
        for cornersquare in corners:
            dist = self.sdist(cornersquare,barracksresult)
            if dist < bestdist:
                bestdist = dist
                best = cornersquare
        cornersquare = best
        self.logg('cornersquare '+str(cornersquare[0])+' '+str(cornersquare[1]))
#       now try to lock this square in with 2 3x3 blocks
        cornersquares = set([cornersquare])
        aroundcc = set([self.enemystartsquare])
        totry = set()
        for dx in range(-6,6):
            for dy in range(-6,6):
                square = (cornersquare[0]+dx,cornersquare[1]+dy)
                if self.get_color(square) == 0:
                    totry.add(square)
        self.logg('per block '+str(len(totry))+' positions')
        solutions = []
        for b0 in totry:
            if self.tryplace(3,b0):
                self.logg('trying block 0 at '+str(b0[0])+' '+str(b0[1]))
                for b1 in totry:
                    if (b1[0]>b0[0]) or ((b1[0]==b0[0]) and (b1[1]>b0[1])):
                        if self.tryplace(3,b1):
                            if self.get_color(cornersquare) == 0:
                                if not self.has_path(cornersquares,aroundcc):
                                    solutions.append((b0,b1))
                                    self.logg('      a solution')
                            self.colorplace(3,b1,0)
                self.colorplace(3,b0,0)
        self.logg('found '+str(len(solutions))+' 2-block corner  solutions')
        if len(solutions)>0:
            asol = solutions[0]
            for (b0,b1) in solutions:
                self.colorplace(3,b0,4)
                self.colorplace(3,b1,4)
                prison = cornersquares.copy()
                self.extend(prison)
                if len(prison)>=3:
                    asol = (b0,b1)
                self.colorplace(3,b0,0)
                self.colorplace(3,b1,0)
            text.write('position CHEESELANDING '+str(asol[0][0]+1.5)+' '+str(asol[0][1]+1.5)+'\n')
            text.write('position CHEESEBUNKER '+str(asol[1][0]+1.5)+' '+str(asol[1][1]+1.5)+'\n')
            self.do_place_shape(0,asol[0])
            self.do_place_shape(0,asol[1])
            # write average prison
            summ0 = 0
            summ1 = 0
            n = 0
            for (x,y) in prison:
                summ0 = summ0+x
                summ1 = summ1+y
                n = n+1
            avera0 = summ0/n
            avera1 = summ1/n
            # use the middle of the squares
            avera0 = avera0+0.5
            avera1 = avera1+0.5
            # round a bit
            avera0 = 0.001*round(1000*avera0)
            avera1 = 0.001*round(1000*avera1)
            text.write('position CHEESEPRISON '+str(avera0)+' '+str(avera1)+'\n')
            # get a 2x2 place for a tank near cheeseprison but outside enemybasearea
            around = (round(avera0),round(avera1))
            bestsd = 9999
            for x in range(around[0]-9,around[0]+9):
                for y in range(around[1]-9,around[1]+9):
                    square = (x,y)
                    if square not in enemybasearea:
                        can = True
                        can = can and (layout_if.layout[square[0]-1][square[1]+-1] == 0)
                        can = can and (layout_if.layout[square[0]-1][square[1]+0] == 0)
                        can = can and (layout_if.layout[square[0]+0][square[1]-1] == 0)
                        can = can and (layout_if.layout[square[0]+0][square[1]+0] == 0)
                        if can:
                            sd = self.sdist(square,around)
                            if sd < bestsd:
                                bestsquare = square
                                bestsd = sd
            text.write('position CHEESETANK '+str(bestsquare[0])+' '+str(bestsquare[1])+'\n')
            # now we can draw the barracks, even if it is on the tankspot
            self.do_place_shape(0,barracksresult)
        # make scout positions just inside the enemy base
        self.get_edge(enemybasearea)
        outside = self.edge.copy()
        self.logg('outside '+str(len(outside)))
        green = set()
        for square in outside:
            if self.get_color(square) == 1:
                green.add(square)
        outeroutside = outside - green
        self.logg('outeroutside '+str(len(outeroutside)))
        self.get_edge(outeroutside)
        inside = self.edge.copy()
        inside = inside & enemybasearea
        self.logg('inside '+str(len(inside)))
        for square in outside:
            if self.get_color(square) == 2:
                rampsquare = square
        radius = sqrt(self.sdist(rampsquare,self.enemystartsquare))
        thecos = (rampsquare[0]-self.enemystartsquare[0])/radius
        thesin = (rampsquare[1]-self.enemystartsquare[1])/radius
        if thesin > 0:
            alfa = acos(thecos)
        else:
            alfa = 2*pi - acos(thecos)
        # make 15 points around enemystartsquare
        for nr in range(0,15):
            beta = alfa + nr * 2*pi/15
            circlepoint = (self.enemystartsquare[0] + cos(beta)*radius*1.3 , self.enemystartsquare[1] + sin(beta)*radius*1.3)
            bestsdist = 9999
            for square in inside:
                sd = self.sdist(square,circlepoint)
                if sd < bestsdist:
                    bestsquare = square
                    bestsdist = sd
            text.write('position SCOUT '+str(bestsquare[0]+0.5)+' '+str(bestsquare[1]+0.5)+'\n')
#
#       that is all
        layout_if.photo_layout()
        text.write('#####'+'\n')
        text.close()







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
 
    def fly(self,p,q) -> float:
        return sqrt(self.sdist(p,q))

solo = prog()
solo.main()

            
