# Placer.py
# Makes text for building placement
# appends the output to file "data/placement.txt"
# author: MerkMore
# version 21 oct 2020
from layout_if_py import layout_if
import random
from math import sqrt, sin, cos, acos, pi

#
# 0 = free
# 1 = minerals,gas
# 2 = ramp
# 3 = nogo
# 4 = building
#

class prog:
#
    mapplace = ''
    filterresult = set()
    startsquare = (0,0)
    enemystartsquare = (0,0)
    rampcenter = (0,0)
    center = (0,0)
    logging = True
#   the map with walk-distances to enemystartsquare
    walking = []
    tankpath = []
    maps = []

    def main(self):
        # get maps
        self.maps = []
        print('data/layout.txt:')
        with open('data/layout.txt','r') as open_file:
            for linen in open_file:
                line = linen.rstrip('\n')
                if (line[0] == 'm') and (line[1] == 'a') and (line[2] == 'p'):
                    print(line)
                    self.maps.append(line)
        # get placement.txt (there may be some output already)
        text = open('data/placement.txt', 'r')
        content = text.read().splitlines()
        text.close()
        for self.mapplace in self.maps:
            old = False
            for line in content:
                if line == self.mapplace:
                    old = True
            if old:
                print(self.mapplace+' is already in data/placement.txt')
            else:
                print('analyzing '+self.mapplace)
                layout_if.load_layout(self.mapplace)
                self.appendthemap()


    def appendthemap(self):
        text = open('data/placement.txt','a')
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
        self.get_edge(enemybasearea)
        ramp = self.edge.copy()
        self.filter_color(ramp,2)
        ramp = self.filterresult.copy()
        self.logg('enemyramp '+str(len(ramp)))
        # for a multi-ramp map, the central ramp is chosen
        mapcenter = (100,100)
        alsoramp = set()
        bestsd = 99999
        for square in ramp:
            sd = self.sdist(square,mapcenter)
            if sd < bestsd:
                bestsd = sd
                alsoramp = set([square])
        self.extend(alsoramp)
        ramp = ramp & alsoramp
        self.logg('restricted to 1 ramp, ramp '+str(len(ramp)))
        self.get_center(ramp)
        x = 0.001*round(1000*(self.center[0]+0.5))
        y = 0.001*round(1000*(self.center[1]+0.5))
        text.write('position ENEMYRAMP ' + str(x) + ' ' + str(y) + '\n')
        #
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
        # for a multi-ramp map, the central ramp is chosen
        mapcenter = (100,100)
        alsoramp = set()
        bestsd = 99999
        for square in ramp:
            sd = self.sdist(square,mapcenter)
            if sd < bestsd:
                bestsd = sd
                alsoramp = set([square])
        self.extend(alsoramp)
        ramp = ramp & alsoramp
        self.logg('restricted to 1 ramp, ramp '+str(len(ramp)))
        self.get_center(ramp)
        x = 0.001*round(1000*(self.center[0]+0.5))
        y = 0.001*round(1000*(self.center[1]+0.5))
        text.write('position HOMERAMP ' + str(x) + ' ' + str(y) + '\n')
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
                            if self.walking[alt[0]][alt[1]] > 0:
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
#       now we will estimate a high value of walking-flying
#       also slightly negative weigh in the flydistance to enemy
#       also slightly negative weigh in the flydistance to home
        best = -999
        for pog in range(0,10000):
            square = (random.randrange(0,200),random.randrange(0,200))
            walk = self.walking[square[0]][square[1]]
            fly = self.fly(square,self.enemystartsquare)
            homefly = self.fly(square,self.startsquare)
            if (walk >= 0) and (fly>10) and (fly<40):
                wafy = (walk - fly)
                wafy = wafy - 0.5*fly
                wafy = wafy - 0.03*homefly
                if wafy>best:
                    best = wafy
                    bestsquare = square
                    self.logg('pos '+str(square[0])+','+str(square[1])+' wafy '+str(wafy)+'   walk '+str(walk)+'  fly '+str(fly))
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
                    if maybe not in enemybasearea:
                        if self.can_place_shape(0,maybe):
                            barracksresult = maybe
                            placed = True
#       if not unlucky, this result is a good cheese building place
        text.write('position INFESTEDBARRACKS '+str(barracksresult[0]+1.5)+' '+str(barracksresult[1]+1.5)+'\n')
        # do not draw the barracks, as later we want to place a tank here
        # self.do_place_shape(0,barracksresult)
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
        self.logg('corners '+str(len(corners)))
        maycorners = corners.copy()
        corners = set()
        for cornersquare in maycorners:
            sd = self.sdist(cornersquare,self.enemystartsquare)
            if sd >= 16*16:
                corners.add(cornersquare)
        self.logg('corners far from creep '+str(len(corners)))
        # happy if we can find 2 2block prisoning at least 3 squares
        happy = False
        while not happy:
            best = None
            bestdist = 80000
            for cornersquare in corners:
                dist = self.sdist(cornersquare,barracksresult)
                if dist < bestdist:
                    bestdist = dist
                    best = cornersquare
            cornersquare = best
            self.logg('cornersquare '+str(cornersquare[0])+' '+str(cornersquare[1]))
            # now try to lock this square in with 2 3x3 blocks
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
            happy = False
            if len(solutions)>0:
                asol = solutions[0]
                for (b0,b1) in solutions:
                    self.colorplace(3,b0,4)
                    self.colorplace(3,b1,4)
                    prison = cornersquares.copy()
                    self.extend(prison)
                    if len(prison)>=3:
                        asol = (b0,b1)
                        asolprison = prison.copy()
                        happy = True
                    self.colorplace(3,b0,0)
                    self.colorplace(3,b1,0)
            # if not happy, delete that one from corners
            if not happy:
                corners.remove(cornersquare)
        # happy
        # of those, the closest to the enemy should be the bunker
        sd0 = self.sdist(asol[0],self.enemystartsquare)
        sd1 = self.sdist(asol[1],self.enemystartsquare)
        if sd0 < sd1:
            text.write('position INFESTEDBUNKER '+str(asol[0][0]+1.5)+' '+str(asol[0][1]+1.5)+'\n')
            text.write('position INFESTEDLANDING '+str(asol[1][0]+1.5)+' '+str(asol[1][1]+1.5)+'\n')
        else:
            text.write('position INFESTEDLANDING ' + str(asol[0][0] + 1.5) + ' ' + str(asol[0][1] + 1.5) + '\n')
            text.write('position INFESTEDBUNKER ' + str(asol[1][0] + 1.5) + ' ' + str(asol[1][1] + 1.5) + '\n')
        self.do_place_shape(0,asol[0])
        self.do_place_shape(0,asol[1])
        # write average asolprison
        summ0 = 0
        summ1 = 0
        n = 0
        for (x,y) in asolprison:
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
        text.write('position INFESTEDPRISON '+str(avera0)+' '+str(avera1)+'\n')
        self.logg('position INFESTEDPRISON '+str(avera0)+' '+str(avera1))
        # get a 5x5 freespace outside enemybasearea, as a tankmove point
        rough = (round(2*avera0 - self.enemystartsquare[0]), round(2*avera1 - self.enemystartsquare[1]))
        if (rough[0]<0) or (rough[0]>=200) or (rough[1]<0) or (rough[1]>=200):
            rough = (random.randrange(0, 200), random.randrange(0, 200))
        sd = self.sdist(rough,self.enemystartsquare)
        while (sd<10*10) or (sd>50*50):
            rough = (random.randrange(0, 200), random.randrange(0, 200))
            sd = self.sdist(rough,self.enemystartsquare)
        self.logg('rough '+str(rough[0])+','+str(rough[1]))
        placed = False
        dist = 0
        while not placed:
            dist = dist + 1
            for dx in range(-dist, dist):
                for dy in range(-dist, dist):
                    square = (rough[0] + dx, rough[1] + dy)
                    if self.can_place_shape(2,square):
                        freespace = (square[0]+2,square[1]+2)
                        placed = True
        self.logg('freespace '+str(freespace[0])+','+str(freespace[1]))
        # get a 2x2 place for a tank near cheeseprison but outside enemybasearea
        self.logg('B')
        around = (round(avera0),round(avera1))
        bestsd = 9999
        for x in range(around[0]-10,around[0]+10):
            for y in range(around[1]-10,around[1]+10):
                square = (x,y)
                if square not in enemybasearea:
                    if self.istile(square): # can place a tank
                        sd = self.sdist(square,around)
                        if sd < bestsd:
                            if self.has_tankpath(square, freespace):
                                bestsquare = square
                                bestsd = sd
        tanksquare = bestsquare
        text.write('position INFESTEDTANK '+str(tanksquare[0])+' '+str(tanksquare[1])+'\n')
        self.logg('position INFESTEDTANK '+str(tanksquare[0])+' '+str(tanksquare[1]))
        # Color the tankpath until we found a factory place.
        surely = self.has_tankpath(tanksquare, freespace) # to get the right tankpath
        self.color_tankpath(4)
        stored_tankpath = self.tankpath.copy()
        self.logg('tankpath ' + str(len(self.tankpath)))
        # now we can draw the barracks, even if it is on the tankspot
        self.do_place_shape(0,barracksresult)
        # make freespace reachable
        self.colortile(freespace,0)
        # for debugging, a photo
        #layout_if.photo_layout()
        # factory
        # get infested_factory place, about 14 from the infestedbarracks, away from the enemy
        vector = (barracksresult[0] - self.enemystartsquare[0], barracksresult[1] - self.enemystartsquare[1])
        factor = 14 / sqrt(self.sdist(barracksresult, self.enemystartsquare))
        factorysuggestion = (round(barracksresult[0] + factor * vector[0]), \
                             round(barracksresult[1] + factor * vector[1]))
        # now we hope to place a factory there
        leftunder = (factorysuggestion[0] - 1, factorysuggestion[1] - 1)
        placed = False
        dist = 0
        while not placed:
            dist = dist + 1
            for dx in range(-dist, dist):
                for dy in range(-dist, dist):
                    if abs(dx)+abs(dy)+max(abs(dx),abs(dy)) == dist:
                        maybe = (leftunder[0] + dx, leftunder[1] + dy)
                        tile = (maybe[0]+1,maybe[1]+1)
                        if self.can_place_shape(1, maybe):
                            if self.has_tankpath(tile,freespace):
                                factoryresult = maybe
                                placed = True
        # Usually this result is a good cheese building place
        text.write('position INFESTEDFACTORY ' + str(factoryresult[0] + 1.5) + ' ' + str(factoryresult[1] + 1.5) + '\n')
        self.logg('position INFESTEDFACTORY ' + str(factoryresult[0] + 1.5) + ' ' + str(factoryresult[1] + 1.5))
        self.do_place_shape(1,factoryresult)
        # erase the stored tankpath roughly
        self.tankpath = stored_tankpath
        self.color_tankpath(0)
        self.do_place_shape(0,barracksresult)
        self.do_place_shape(1,factoryresult)
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
        # leftunder definition
        can = (alt[0] >= 0) and (alt[0]+4 < 200) and (alt[1] >= 0) and (alt[1]+4 < 200)
        if can:
            if shape == 0:
                # fusioncore
                can = can and (layout_if.layout[alt[0]+0][alt[1]+0] == 0)
                can = can and (layout_if.layout[alt[0]+0][alt[1]+1] == 0)
                can = can and (layout_if.layout[alt[0]+0][alt[1]+2] == 0)
                can = can and (layout_if.layout[alt[0]+1][alt[1]+0] == 0)
                can = can and (layout_if.layout[alt[0]+1][alt[1]+1] == 0)
                can = can and (layout_if.layout[alt[0]+1][alt[1]+2] == 0)
                can = can and (layout_if.layout[alt[0]+2][alt[1]+0] == 0)
                can = can and (layout_if.layout[alt[0]+2][alt[1]+1] == 0)
                can = can and (layout_if.layout[alt[0]+2][alt[1]+2] == 0)
            elif shape == 1:
                # starport
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
            else:
                # 5x5 space
                can = can and (layout_if.layout[alt[0] + 0][alt[1] + 0] == 0)
                can = can and (layout_if.layout[alt[0] + 0][alt[1] + 1] == 0)
                can = can and (layout_if.layout[alt[0] + 0][alt[1] + 2] == 0)
                can = can and (layout_if.layout[alt[0] + 0][alt[1] + 3] == 0)
                can = can and (layout_if.layout[alt[0] + 0][alt[1] + 4] == 0)
                can = can and (layout_if.layout[alt[0] + 1][alt[1] + 0] == 0)
                can = can and (layout_if.layout[alt[0] + 1][alt[1] + 1] == 0)
                can = can and (layout_if.layout[alt[0] + 1][alt[1] + 2] == 0)
                can = can and (layout_if.layout[alt[0] + 1][alt[1] + 3] == 0)
                can = can and (layout_if.layout[alt[0] + 1][alt[1] + 4] == 0)
                can = can and (layout_if.layout[alt[0] + 2][alt[1] + 0] == 0)
                can = can and (layout_if.layout[alt[0] + 2][alt[1] + 1] == 0)
                can = can and (layout_if.layout[alt[0] + 2][alt[1] + 2] == 0)
                can = can and (layout_if.layout[alt[0] + 2][alt[1] + 3] == 0)
                can = can and (layout_if.layout[alt[0] + 2][alt[1] + 4] == 0)
                can = can and (layout_if.layout[alt[0] + 3][alt[1] + 0] == 0)
                can = can and (layout_if.layout[alt[0] + 3][alt[1] + 1] == 0)
                can = can and (layout_if.layout[alt[0] + 3][alt[1] + 2] == 0)
                can = can and (layout_if.layout[alt[0] + 3][alt[1] + 3] == 0)
                can = can and (layout_if.layout[alt[0] + 3][alt[1] + 4] == 0)
                can = can and (layout_if.layout[alt[0] + 4][alt[1] + 0] == 0)
                can = can and (layout_if.layout[alt[0] + 4][alt[1] + 1] == 0)
                can = can and (layout_if.layout[alt[0] + 4][alt[1] + 2] == 0)
                can = can and (layout_if.layout[alt[0] + 4][alt[1] + 3] == 0)
                can = can and (layout_if.layout[alt[0] + 4][alt[1] + 4] == 0)
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
        if self.get_color(square) == 0:
            # usually 8, but you cannot walk diagonal through minerals
            self.neighbours = set()
            self.neighbours.add((square[0] - 1, square[1] + 0))
            self.neighbours.add((square[0] + 0, square[1] - 1))
            self.neighbours.add((square[0] + 1, square[1] + 0))
            self.neighbours.add((square[0] + 0, square[1] + 1))
            if layout_if.layout[square[0] + 1][square[1] + 0] != 1:
                self.neighbours.add((square[0] + 1, square[1] - 1))
                self.neighbours.add((square[0] + 1, square[1] + 1))
            if layout_if.layout[square[0] - 1][square[1] + 0] != 1:
                self.neighbours.add((square[0] - 1, square[1] - 1))
                self.neighbours.add((square[0] - 1, square[1] + 1))
            if layout_if.layout[square[0] + 0][square[1] + 1] != 1:
                self.neighbours.add((square[0] - 1, square[1] + 1))
                self.neighbours.add((square[0] + 1, square[1] + 1))
            if layout_if.layout[square[0] + 0][square[1] - 1] != 1:
                self.neighbours.add((square[0] - 1, square[1] - 1))
                self.neighbours.add((square[0] + 1, square[1] - 1))
        else:
            self.neighbours = set()
            self.neighbours.add((square[0] - 1, square[1] + 0))
            self.neighbours.add((square[0] + 0, square[1] - 1))
            self.neighbours.add((square[0] + 1, square[1] + 0))
            self.neighbours.add((square[0] + 0, square[1] + 1))
            self.neighbours.add((square[0] - 1, square[1] - 1))
            self.neighbours.add((square[0] + 1, square[1] - 1))
            self.neighbours.add((square[0] + 1, square[1] + 1))
            self.neighbours.add((square[0] - 1, square[1] + 1))

    def extend(self,aset):
        # aset is enlarged with same-colored squares
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
        # self.edge is the squares around aset
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


    # tank routines
    def istile(self,sq) -> bool:
        # a tanktile is the middle of 4 squares
        ist = True
        ist = ist and (layout_if.layout[sq[0] + 0][sq[1] + 0] in (0,2))
        ist = ist and (layout_if.layout[sq[0] - 1][sq[1] + 0] in (0,2))
        ist = ist and (layout_if.layout[sq[0] + 0][sq[1] - 1] in (0,2))
        ist = ist and (layout_if.layout[sq[0] - 1][sq[1] - 1] in (0,2))
        return ist

    def colortile(self,sq,color):
        layout_if.layout[sq[0] + 0][sq[1] + 0] = color
        layout_if.layout[sq[0] - 1][sq[1] + 0] = color
        layout_if.layout[sq[0] + 0][sq[1] - 1] = color
        layout_if.layout[sq[0] - 1][sq[1] - 1] = color

    def color_tankpath(self,color):
        for tile in self.tankpath:
            self.colortile(tile,color)

    def has_tankpath(self,starttile,stoptile) -> bool:
        # a tanktile is the middle of 4 squares
        hp = self.istile(starttile) and self.istile(stoptile)
        steptostart = {} # for the inside, the dist to starttile is administrated
        n = 0
        steptostart[starttile] = n
        inside = set([starttile])
        edge = set([starttile])
        while hp and (stoptile not in edge) and (len(edge) > 0):
            n = n + 1
            newedge = set()
            for tile in edge:
                self.get_neighbours(tile)
                for nsquare in self.neighbours:
                    if nsquare not in inside:
                        if self.istile(nsquare):
                            newedge.add(nsquare)
            inside = inside | newedge
            for square in newedge:
                steptostart[square] = n
            edge = newedge.copy()
        hp = hp and (stoptile in edge)
        self.tankpath = []
        if hp:
            tile = stoptile
            self.tankpath.append(tile)
            while n > 0:
                n = n - 1
                self.get_neighbours(tile)
                for nsquare in self.neighbours:
                    if nsquare in inside:
                        if steptostart[nsquare] == n:
                            tile = nsquare
                self.tankpath.append(tile)
        return hp



#   distance
    def sdist(self,p,q) -> int:
        return (p[0]-q[0])**2 + (p[1]-q[1])**2
 
    def fly(self,p,q) -> int:
        return max(abs(p[0]-q[0]),abs(p[1]-q[1]))

solo = prog()
solo.main()

            
