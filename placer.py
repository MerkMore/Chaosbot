# Placer.py
# Makes text for building placement
# appends the output to file "data\placement.txt"
# author: MerkMore
# version 6 dec 2020
from layout_if_py import layout_if
import random
from math import sqrt, sin, cos, acos, pi

#
# 0 = free
# 1 = minerals,gas
# 2 = ramp
# 3 = nogo
# 4 = building
# 5 = nobuild
#

class prog:
    #
    mapplace = ''
    mapleft = 0
    mapright = 0
    mapbot = 0
    maptop = 0
    mapcenter = (0,0)
    filterresult = set()
    startsquare = (0,0)
    enemystartsquare = (0,0)
    enemynatural = (0,0)
    ramptopcenter = (0,0)
    centerresult = (0,0)
    edgeresult = set()
    logging = True
    walking = []    # the map with walk-distances to enemystartsquare
    tankpath = []
    diskpath = []
    maps = []
    expansions = set()
    path_direction = (0,0)
    asol = []
    asolprison = set()

    def main(self):
        # get maps
        self.maps = []
        print('data\layout.txt:')
        with open('data\layout.txt','r') as open_file:
            for linen in open_file:
                line = linen.rstrip('\n')
                if (line[0] == 'm') and (line[1] == 'a') and (line[2] == 'p'):
                    print(line)
                    self.maps.append(line)
        # get placement.txt (there may be some output already)
        text = open('data\placement.txt', 'r')
        content = text.read().splitlines()
        text.close()
        for self.mapplace in self.maps:
            old = False
            for line in content:
                if line == self.mapplace:
                    old = True
            if old:
                print(self.mapplace+' is already in data\placement.txt')
            else:
                print('analyzing '+self.mapplace)
                layout_if.load_layout(self.mapplace)
                self.appendthemap()
                layout_if.photo_layout()
                layout_if.photo_height()

    def appendthemap(self):
        text = open('data\placement.txt','a')
        text.write('#####'+'\n')
        text.write(self.mapplace+'\n')
        #
        # mapleft,mapright,mapbot,maptop
        self.mapleft = 99999
        self.mapright = 0
        self.mapbot = 99999
        self.maptop = 0
        for x in range(0,200):
            for y in range(0,200):
                if layout_if.layout[x][y] != 3:
                    self.mapleft = min(self.mapleft,x)
                    self.mapright = max(self.mapright,x+1)
                    self.mapbot = min(self.mapbot,y)
                    self.maptop = max(self.maptop,y+1)
        self.mapcenter = (round((self.mapleft+self.mapright)/2),round((self.mapbot+self.maptop)/2))
        self.logg('mapcenter '+str(self.mapcenter[0])+','+str(self.mapcenter[1]))
        #
        #       startx,y can be 36.5,112.5 but we identify that square with the tuple (36,112)
        self.startsquare = (round(layout_if.startx-0.5),round(layout_if.starty-0.5))
        self.enemystartsquare = (round(layout_if.enemyx - 0.5), round(layout_if.enemyy - 0.5))
        self.logg('enemy start '+str(self.enemystartsquare[0])+','+str(self.enemystartsquare[1]))
        self.expansions = set()
        for x in range(0,200):
            for y in range(0,200):
                lo = (x,y)
                if self.has_cc(lo):
                    self.expansions.add(lo)
        self.logg('expansions '+str(len(self.expansions)))
        #
        #       We will work with sets of squares.
        startcc = set([self.enemystartsquare]) # there is a building
        self.extend(startcc)
        self.logg('enemystartcc '+str(len(startcc)))
        self.get_edge(startcc) # empty boundery around the cc
        aroundcc = self.edgeresult.copy()
        self.logg('aroundcc '+str(len(aroundcc)))
        enemybasearea = aroundcc.copy()
        self.extend(enemybasearea) # the whole enemy top area
        self.logg('enemybasearea '+str(len(enemybasearea)))
        self.get_edge(enemybasearea)
        ramptop = self.edgeresult.copy()
        self.filter_color(ramptop,2)
        ramptop = self.filterresult.copy() # the parts of ramp touching the top area
        self.logg('enemyramptop '+str(len(ramptop)))
        # for a multi-ramp map, the central ramp is chosen
        alsoramptop = set()
        bestsd = 99999
        for square in ramptop:
            sd = self.sdist(square,self.mapcenter)
            if sd < bestsd:
                bestsd = sd
                alsoramptop = set([square])
        self.extend(alsoramptop)
        ramptop = ramptop & alsoramptop
        self.logg('restricted to 1 ramptop, ramptop '+str(len(ramptop)))
        ramp = ramptop.copy()
        self.extend(ramp)
        self.get_center(ramp)
        enemyramp = self.centerresult
        x = 0.001*round(1000*(self.centerresult[0]+0.5))
        y = 0.001*round(1000*(self.centerresult[1]+0.5))
        text.write('position ENEMYRAMP ' + str(x) + ' ' + str(y) + '\n')
        closest = 99999
        for lo in self.expansions:
            sd = self.sdist(lo,self.enemystartsquare)
            if sd > 8: # lo is leftunder, startsquare is middle
                sd = self.sdist(lo,self.centerresult)
                if sd < closest:
                    closest = sd
                    self.enemynatural = (lo[0]+2,lo[1]+2)
        x = self.enemynatural[0]+0.5
        y = self.enemynatural[1]+0.5
        text.write('position ENEMYNATURAL ' + str(x) + ' ' + str(y) + '\n')
        #
        startcc = set([self.startsquare]) # cc
        self.extend(startcc)
        self.logg('startcc '+str(len(startcc)))
        self.get_edge(startcc)
        aroundcc = self.edgeresult.copy()
        self.logg('aroundcc '+str(len(aroundcc)))
        basearea = aroundcc.copy()
        self.extend(basearea)
        self.logg('basearea '+str(len(basearea)))
        self.get_edge(basearea)
        ramptop = self.edgeresult.copy()
        self.filter_color(ramptop,2)
        ramptop = self.filterresult.copy()
        self.logg('ramptop '+str(len(ramptop)))
        # for a multi-ramp map, the central ramp is chosen
        alsoramptop = set()
        bestsd = 99999
        for square in ramptop:
            sd = self.sdist(square,self.mapcenter)
            if sd < bestsd:
                bestsd = sd
                alsoramptop = set([square])
        self.extend(alsoramptop)
        ramptop = ramptop & alsoramptop
        self.logg('restricted to 1 ramptop, ramptop '+str(len(ramptop)))
        ramp = ramptop.copy()
        self.extend(ramp)
        self.get_center(ramp)
        x = 0.001*round(1000*(self.centerresult[0]+0.5))
        y = 0.001*round(1000*(self.centerresult[1]+0.5))
        text.write('position HOMERAMP ' + str(x) + ' ' + str(y) + '\n')
        self.get_edge(ramptop)
        aroundramptop = self.edgeresult.copy()
        self.filter_color(aroundramptop,0)
        aroundramptop = self.filterresult.copy()
        self.logg('aroundramptop '+str(len(aroundramptop)))
        self.path_direction = self.startsquare
        if self.has_zeropath(aroundramptop,aroundcc):
            self.logg('path found')
        else:
            self.logg('no path found')
        #       now we try to close the path with the 3 blocks
        #       make totry. That is possible positions for blocks to be put
        self.get_center(aroundramptop)
        self.ramptopcenter = self.centerresult
        #       for blocks, the position is described by the leftunder corner
        totry = set()
        for dx in range(-6,6):
            for dy in range(-6,6):
                square = (self.ramptopcenter[0]+dx,self.ramptopcenter[1]+dy)
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
                            # self.logg('   trying block 1 at '+str(b1[0])+' '+str(b1[1]))
                            for b2 in totry:
                                if self.tryplace(3,b2):
                                    self.filter_color(aroundramptop,0)
                                    if not self.has_zeropath(self.filterresult,aroundcc):
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
                if self.can_place_shape(3.5,b2):
                    asol = (b0,b1,b2)
                self.colorplace(2,b0,0)
                self.colorplace(2,b1,0)
            text.write('position SUPPLYDEPOT '+str(asol[0][0]+1)+' '+str(asol[0][1]+1)+'\n')
            text.write('position SUPPLYDEPOT '+str(asol[1][0]+1)+' '+str(asol[1][1]+1)+'\n')
            text.write('position BARRACKS '+str(asol[2][0]+1.5)+' '+str(asol[2][1]+1.5)+'\n')
        # against building clutter, color a tankpath from start to center
        starttile = self.startsquare
        # it starts being colored 4
        cccorner = (self.startsquare[0] - 2, self.startsquare[1] - 2)
        self.colorplace(5, cccorner, 0)
        # centertile
        around = self.mapcenter
        bestsd = 99999
        for x in range(around[0]-10,around[0]+10):
            for y in range(around[1]-10,around[1]+10):
                square = (x,y)
                if self.istile(square): # can place a tank
                    sd = self.sdist(square,around)
                    if sd < bestsd:
                        bestsquare = square
                        bestsd = sd
        centertile = bestsquare
        # place the wallbarracks but not the walldepots
        (b0, b1, b2) = asol
        self.colorplace(3, b2, 4)
        if self.has_tankpath(starttile,centertile):
            self.color_tankpath(5)
            # give the info to Merkbot
            lineel = 0
            stri = 'path '
            for tile in self.tankpath:
                stri = stri + str(tile[0]) + ' ' + str(tile[1])+'  '
                lineel += 1
                if lineel == 10:
                    text.write(stri + '\n')
                    lineel = 0
                    stri = 'path '
            if lineel != 0:
                text.write(stri + '\n')
        self.colorplace(3, b2, 0)
        # draw back the startcc
        self.colorplace(5, cccorner, 4)
        #
        # enemy starts being colored 4
        cccorner = (self.enemystartsquare[0] - 2, self.enemystartsquare[1] - 2)
        self.colorplace(5, cccorner, 0)
        # walking enemy
        self.walking = []
        for col in range(0, 200):
            collist = []
            for row in range(0, 200):
                collist.append(-1)
            self.walking.append(collist)
        self.walking[self.enemystartsquare[0]][self.enemystartsquare[1]] = 0
        dist = 0
        # edge will contain all squares with dist
        edge = [self.enemystartsquare]
        while len(edge)>0:
            dist = dist+1
            new_edge = []
            for square in edge:
                self.get_neighbours(square)
                for nsquare in self.neighbours:
                    if self.walking[nsquare[0]][nsquare[1]] == -1:
                        if layout_if.layout[nsquare[0]][nsquare[1]] in (0,2):
                            self.walking[nsquare[0]][nsquare[1]] = dist
                            new_edge.append(nsquare)
            edge = new_edge.copy()
        #       now, find some hidden fusioncore positions
        for shape in (3,3.5):
            alters = []
            while len(alters)<10000:
                alt = (random.randrange(0,200),random.randrange(0,200))
                dis = self.sdist(alt,self.startsquare)
                if (dis>20*20) and (dis<70*70):
                    dis = self.sdist(alt,self.ramptopcenter)
                    if (dis>30*30):
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
                if shape == 3:
                    text.write('position FUSIONCORE * '+str(alt[0]+1.5)+' '+str(alt[1]+1.5)+'\n')
                else:
                    text.write('position STARPORT * '+str(alt[0]+1.5)+' '+str(alt[1]+1.5)+'\n')
        #
        # erase all buildings for the rest of the program
        #
        for x in range(0,200):
            for y in range(0,200):
                if layout_if.layout[x][y] == 4:
                    layout_if.layout[x][y] = 0
        #
        # find reaperjumpspots near the enemybasearea
        square = tuple(enemybasearea)[0]
        dsquare = (square[0]*2,square[1]*2)
        (baselayout, baseheight) = self.get_terrain(dsquare)
        darea = {dsquare}
        self.terrain_extend(darea)
        self.terrain_get_edge(darea)
        possi = self.edgeresult.copy()
        self.terrain_get_edge(possi)
        possi = possi | self.edgeresult
        reaperall = set()
        for dsquare in possi:
            (layout,height) = self.get_terrain(dsquare)
            if height == baseheight - 16:
                self.logg('reaperjumppoint '+str(layout)+' '+str(height)+' '+str(dsquare[0]/2)+','+str(dsquare[1]/2))
                reaperall.add(dsquare)
        # get one representant per cluster
        reaperspots = set()
        while len(reaperall) > 0:
            one = tuple(reaperall)[0]
            reaperspots.add(one)
            todel = {one}
            stable = False
            while not stable:
                curlen = len(todel)
                toadd = set()
                for aone in todel:
                    self.terrain_get_neighbours(aone)
                    for aneigh in self.neighbours:
                        if aneigh in reaperall:
                            toadd.add(aneigh)
                todel = todel | toadd
                stable = (len(todel) == curlen)
            reaperall -= todel
        for dsquare in reaperspots:
            x = dsquare[0] / 2
            y = dsquare[1] / 2
            self.logg('position REAPERJUMP ' + str(x) + ' ' + str(y))
            text.write('position REAPERJUMP ' + str(x) + ' ' + str(y) + '\n')
        # get the reaperjumpspot away from enemyramp and near mapcenter
        bestqual = -99999
        for dsquare in reaperspots:
            square = (dsquare[0] / 2,dsquare[1] / 2)
            qual = 2 * self.octagondist(square,enemyramp) - self.octagondist(square,self.mapcenter)
            if qual > bestqual:
                bestqual = qual
                reaperjumpspot = square
        # get the enemybasearea point near the reaperjumpspot
        bestsd = 99999
        for square in enemybasearea:
            sd = self.sdist(square, reaperjumpspot)
            if sd < bestsd:
                bestsquare = square
                bestsd = sd
        if bestsd != 99999:
            reaperbasejump = bestsquare
        # get the reaperbarracksspot
        wantsize = 8 # try to get it unscoutable from the top
        hassize = self.circledist(reaperjumpspot,self.mapcenter)
        vec = (self.mapcenter[0] - reaperjumpspot[0], self.mapcenter[1] - reaperjumpspot[1])
        vec = (vec[0] * wantsize / hassize, vec[1] * wantsize / hassize)
        around = (round(reaperjumpspot[0] + vec[0]),round(reaperjumpspot[1] + vec[1]))
        self.logg('reaperbarracks around '+str(around[0])+','+str(around[1]))
        bestsd = 99999
        for x in range(around[0]-15,around[0]+15):
            for y in range(around[1]-15,around[1]+15):
                square = (x,y)
                if self.can_place_shape(3.5,square): # can place barracks
                    acceptable = True
                    for ba in enemybasearea:
                        if self.sdist(square,ba) < wantsize*wantsize:
                            acceptable = False
                    if acceptable:
                        sd = self.sdist(square,reaperjumpspot)
                        if sd < bestsd:
                            bestsquare = square
                            bestsd = sd
        if bestsd != 99999:
            x = bestsquare[0] + 1.5
            y = bestsquare[1] + 1.5
            text.write('position REAPERBARRACKS ' + str(x) + ' ' + str(y) + '\n')
            self.logg('position REAPERBARRACKS ' + str(x) + ' ' + str(y))
        else:
            self.logg('no reaperbarracks')
        # block reaperbasejump with two bunkers
        if self.twoblock(reaperbasejump):
            text.write('position REAPERBUNKER '+str(self.asol[0][0]+1.5)+' '+str(self.asol[0][1]+1.5)+'\n')
            text.write('position REAPERBUNKER '+str(self.asol[1][0]+1.5)+' '+str(self.asol[1][1]+1.5)+'\n')
            self.get_center(self.asolprison)
            # use the middle of the squares
            avera0 = self.centerresult[0] + 0.5
            avera1 = self.centerresult[1] + 0.5
            # round a bit
            avera0 = 0.001 * round(1000 * avera0)
            avera1 = 0.001 * round(1000 * avera1)
            text.write('position REAPERPRISON ' + str(avera0) + ' ' + str(avera1) + '\n')
            self.logg('position REAPERPRISON ' + str(avera0) + ' ' + str(avera1))
        else:
            self.logg('no reaperprison')
        #
        # estimate a choke as enemynatural in the direction of mapcenter dist 0.5*dist(enemystart,enemynatural)
        wantsize = 0.5 * self.circledist(self.enemynatural,self.enemystartsquare)
        hassize = self.circledist(self.enemynatural,self.mapcenter)
        vec = (self.mapcenter[0] - self.enemynatural[0], self.mapcenter[1] - self.enemynatural[1])
        vec = (vec[0] * wantsize / hassize, vec[1] * wantsize / hassize)
        estimate = (round(self.enemynatural[0] + vec[0]),round(self.enemynatural[1] + vec[1]))
        self.logg('estimate en. nat. choke '+str(estimate[0])+','+str(estimate[1]))
        # centertile
        around = (round(0.33*(self.startsquare[0]+2*self.enemystartsquare[0])),
                  round(0.33*(self.startsquare[1]+2*self.enemystartsquare[1])))
        bestsd = 99999
        for x in range(around[0]-20,around[0]+20):
            for y in range(around[1]-20,around[1]+20):
                square = (x,y)
                if self.istile(square): # can place a tank
                    sd = self.sdist(square,around)
                    if sd < bestsd:
                        bestsquare = square
                        bestsd = sd
        centertile = bestsquare
        ennattile = (round(self.enemynatural[0]),round(self.enemynatural[1]))
        pathstart = {ennattile}
        pathend = {centertile}
        self.path_direction = centertile
        if not self.has_path(pathstart, pathend):
            self.logg('no path from enemynatural to centertile?!')
        # now get good chokes around estimate
        chokes = set()
        for dx in range(-19,20):
            for dy in range(-19,20):
                choke = (estimate[0]+dx,estimate[1]+dy)
                self.mask_disk(choke,10)
                if self.istile(ennattile) and self.istile(centertile):
                    if not self.has_path(pathstart,pathend):
                        chokes.add(choke)
                self.mask_disk(choke, 10) # unmask
            #
        self.logg('found chokes: '+str(len(chokes)))
        if len(chokes) > 0:
            self.get_center(chokes)
            x = 0.001*round(1000*(self.centerresult[0])) # do not add 0.5 as these are real centers
            y = 0.001*round(1000*(self.centerresult[1]))
            text.write('position ENEMYNATURALCHOKE ' + str(x) + ' ' + str(y) + '\n')
        #
        #
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
        placed = self.can_place_shape(3,leftunder)
        barracksresult = leftunder
        dist = 0
        while not placed:
            dist = dist+1
            for dx in range(-dist,dist):
                for dy in range(-dist,dist):
                    maybe = (leftunder[0]+dx,leftunder[1]+dy)
                    if maybe not in enemybasearea:
                        if self.can_place_shape(3,maybe):
                            barracksresult = maybe
                            placed = True
        #       if not unlucky, this result is a good cheese building place
        text.write('position INFESTEDBARRACKS '+str(barracksresult[0]+1.5)+' '+str(barracksresult[1]+1.5)+'\n')
        # do not draw the barracks, as later we want to place a tank here
        # self.do_place_shape(3,barracksresult)
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
        todel = set()
        for cornersquare in corners:
            if self.twoblock(cornersquare):
                if len(self.asolprison) < 3:
                    todel.add(cornersquare)
            else:
                todel.add(cornersquare)
        corners -= todel
        # of those, the closest to the enemy should be the bunker
        sd0 = self.sdist(self.asol[0],self.enemystartsquare)
        sd1 = self.sdist(self.asol[1],self.enemystartsquare)
        if sd0 < sd1:
            text.write('position INFESTEDBUNKER '+str(self.asol[0][0]+1.5)+' '+str(self.asol[0][1]+1.5)+'\n')
            text.write('position INFESTEDLANDING '+str(self.asol[1][0]+1.5)+' '+str(self.asol[1][1]+1.5)+'\n')
        else:
            text.write('position INFESTEDLANDING ' + str(self.asol[0][0] + 1.5) + ' ' + str(self.asol[0][1] + 1.5) + '\n')
            text.write('position INFESTEDBUNKER ' + str(self.asol[1][0] + 1.5) + ' ' + str(self.asol[1][1] + 1.5) + '\n')
        self.do_place_shape(3,self.asol[0])
        self.do_place_shape(3,self.asol[1])
        # write average asolprison
        self.get_center(self.asolprison)
        # use the middle of the squares
        avera0 = self.centerresult[0]+0.5
        avera1 = self.centerresult[1]+0.5
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
                    if self.can_place_shape(5,square):
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
        self.color_tankpath(5)
        stored_tankpath = self.tankpath.copy()
        self.logg('tankpath ' + str(len(self.tankpath)))
        # now we can draw the barracks, even if it is on the tankspot
        self.do_place_shape(3,barracksresult)
        # make freespace reachable
        self.colortile(freespace,0)
        # for debugging, a photo
        #layout_if.photo_layout()
        # factory
        # get infested_factory place, about 14 from the infestedbarracks, away from the enemy
        vector = (barracksresult[0] - self.enemystartsquare[0], barracksresult[1] - self.enemystartsquare[1])
        factor = 14 / self.circledist(barracksresult, self.enemystartsquare)
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
                        if self.can_place_shape(3.5, maybe):
                            if self.has_tankpath(tile,freespace):
                                factoryresult = maybe
                                placed = True
        # Usually this result is a good cheese building place
        text.write('position INFESTEDFACTORY ' + str(factoryresult[0] + 1.5) + ' ' + str(factoryresult[1] + 1.5) + '\n')
        self.logg('position INFESTEDFACTORY ' + str(factoryresult[0] + 1.5) + ' ' + str(factoryresult[1] + 1.5))
        self.do_place_shape(3.5,factoryresult)
        # erase the stored tankpath roughly
        self.tankpath = stored_tankpath
        self.color_tankpath(0)
        self.do_place_shape(3,barracksresult)
        self.do_place_shape(3.5,factoryresult)
        # make scout positions just inside the enemy base
        self.get_edge(enemybasearea)
        outside = self.edgeresult.copy()
        self.logg('outside '+str(len(outside)))
        green = set()
        for square in outside:
            if self.get_color(square) == 1:
                green.add(square)
        outeroutside = outside - green
        self.logg('outeroutside '+str(len(outeroutside)))
        self.get_edge(outeroutside)
        inside = self.edgeresult.copy()
        inside = inside & enemybasearea
        self.logg('inside '+str(len(inside)))
        for square in outside:
            if self.get_color(square) == 2:
                ramptopsquare = square
        radius = self.circledist(ramptopsquare,self.enemystartsquare)
        thecos = (ramptopsquare[0]-self.enemystartsquare[0])/radius
        thesin = (ramptopsquare[1]-self.enemystartsquare[1])/radius
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
        text.write('#####'+'\n')
        text.close()



    def twoblock(self, cornersquare) -> bool:
        # try to lock this enemybasearea square in with 2 3x3 blocks
        # return self.asol ([0] and [1] leftunderpoints of 3x3 blocks)
        # return self.asolprison (the enclosed squares)
        cornersquares = set([cornersquare])
        aroundcc = set([self.enemystartsquare])
        self.path_direction = self.enemystartsquare
        totry = set()
        for dx in range(-6, 6):
            for dy in range(-6, 6):
                square = (cornersquare[0] + dx, cornersquare[1] + dy)
                if self.get_color(square) == 0:
                    totry.add(square)
        self.logg('per block ' + str(len(totry)) + ' positions')
        solutions = []
        for b0 in totry:
            if self.tryplace(3, b0):
                self.logg('trying block 0 at ' + str(b0[0]) + ' ' + str(b0[1]))
                for b1 in totry:
                    if (b1[0] > b0[0]) or ((b1[0] == b0[0]) and (b1[1] > b0[1])):
                        if self.tryplace(3, b1):
                            if self.get_color(cornersquare) == 0:
                                if not self.has_zeropath(cornersquares, aroundcc):
                                    solutions.append((b0, b1))
                                    self.logg('      a solution')
                            self.colorplace(3, b1, 0)
                self.colorplace(3, b0, 0)
        self.logg('found ' + str(len(solutions)) + ' 2-block corner  solutions')
        bestlen = 0
        if len(solutions) > 0:
            for (b0, b1) in solutions:
                self.colorplace(3, b0, 4)
                self.colorplace(3, b1, 4)
                prison = cornersquares.copy()
                self.extend(prison)
                if len(prison) >= bestlen:
                    self.asol = (b0, b1)
                    self.asolprison = prison.copy()
                self.colorplace(3, b0, 0)
                self.colorplace(3, b1, 0)
        return (len(solutions) > 0)



    def do_place_shape(self,shape,alt):
        #       leftunder definition
        if shape == 3:
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
        elif shape == 3.5:
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
            if shape == 3:
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
            elif shape == 3.5:
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
            elif shape == 5:
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


    def has_cc(self, alt) -> bool:
        has = (alt[0] >= 0) and (alt[0] + 4 < 200) and (alt[1] >= 0) and (alt[1] + 4 < 200)
        if has:
            has = has and (layout_if.layout[alt[0] + 0][alt[1] + 0] == 4)
            if has:
                has = has and (layout_if.layout[alt[0] + 0][alt[1] + 1] == 4)
                has = has and (layout_if.layout[alt[0] + 0][alt[1] + 2] == 4)
                has = has and (layout_if.layout[alt[0] + 0][alt[1] + 3] == 4)
                has = has and (layout_if.layout[alt[0] + 0][alt[1] + 4] == 4)
                has = has and (layout_if.layout[alt[0] + 1][alt[1] + 0] == 4)
                has = has and (layout_if.layout[alt[0] + 1][alt[1] + 1] == 4)
                has = has and (layout_if.layout[alt[0] + 1][alt[1] + 2] == 4)
                has = has and (layout_if.layout[alt[0] + 1][alt[1] + 3] == 4)
                has = has and (layout_if.layout[alt[0] + 1][alt[1] + 4] == 4)
                has = has and (layout_if.layout[alt[0] + 2][alt[1] + 0] == 4)
                has = has and (layout_if.layout[alt[0] + 2][alt[1] + 1] == 4)
                has = has and (layout_if.layout[alt[0] + 2][alt[1] + 2] == 4)
                has = has and (layout_if.layout[alt[0] + 2][alt[1] + 3] == 4)
                has = has and (layout_if.layout[alt[0] + 2][alt[1] + 4] == 4)
                has = has and (layout_if.layout[alt[0] + 3][alt[1] + 0] == 4)
                has = has and (layout_if.layout[alt[0] + 3][alt[1] + 1] == 4)
                has = has and (layout_if.layout[alt[0] + 3][alt[1] + 2] == 4)
                has = has and (layout_if.layout[alt[0] + 3][alt[1] + 3] == 4)
                has = has and (layout_if.layout[alt[0] + 3][alt[1] + 4] == 4)
                has = has and (layout_if.layout[alt[0] + 4][alt[1] + 0] == 4)
                has = has and (layout_if.layout[alt[0] + 4][alt[1] + 1] == 4)
                has = has and (layout_if.layout[alt[0] + 4][alt[1] + 2] == 4)
                has = has and (layout_if.layout[alt[0] + 4][alt[1] + 3] == 4)
                has = has and (layout_if.layout[alt[0] + 4][alt[1] + 4] == 4)
        return has

    def logg(self,stri):
        if self.logging:
            print(stri)
    
    def colorplace(self, am,square,color):
        # grab the building by its leftunder point
        for dx in range(0,am):
            for dy in range(0,am):
                layout_if.layout[square[0] + dx][square[1] + dy] = color

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
        # self.edgeresult is the squares around aset
        square = aset.pop()
        aset.add(square)
        mycolor = self.get_color(square)
        self.edgeresult = set()
        for square in aset:
            self.get_neighbours(square)
            for nsquare in self.neighbours:
                if self.get_color(nsquare) != mycolor:
                    self.edgeresult.add(nsquare)

    def filter_color(self,aset,mustcolor):
        wrong = set()        
        for square in aset:
            if self.get_color(square) != mustcolor:
                wrong.add(square)
        self.filterresult = aset - wrong

    def get_center(self,aset):
        # self.centerresult is a square near the middle of aset
        n = len(aset)
        sumx = 0
        sumy = 0
        for square in aset:
            sumx = sumx + square[0] 
            sumy = sumy + square[1]
        avgx = round(sumx/n)
        avgy = round(sumy/n) 
        self.centerresult = (avgx,avgy)

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
        sd = self.sdist(square,self.path_direction)
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
        # bset should be near self.path_direction
        aset = in_aset.copy()
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
                        if self.get_color(nsquare) in [0,2]:
                            if nsquare not in seen:
                                seen.add(nsquare)
                                hp = hp or (nsquare in bset)
                                self.add_spo(nsquare)
        return hp

    def has_zeropath(self,in_aset,bset) -> bool:
        # bset should be near self.path_direction
        aset = in_aset.copy()
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


    # disk routines
    def mask_disk(self,mid,diskdiameter):
        # mask (or unmask) a circle on the layout
        # diskdiameter > 0, diskdiameter whole number
        # if diskdiameter odd, mid must contain halves
        r = diskdiameter / 2
        left = round(mid[0]-r)
        right = round(mid[0]+r)
        bot = round(mid[1]-r)
        top = round(mid[1]+r)
        can = (left >= 0) and (right < 200) and (bot >= 0) and (top < 200)
        if can:
            for x in range(left, right):
                for y in range(bot, top):
                    squaremid = (x+0.5,y+0.5)
                    if self.sdist(squaremid,mid) <= r * r:
                        was = layout_if.layout[x][y]
                        if was < 10:
                            layout_if.layout[x][y] = was + 10
                        else:
                            layout_if.layout[x][y] = was - 10

    #   distance
    def sdist(self,p,q) -> int:
        # circle-distance (quadrat)
        return (p[0]-q[0])**2 + (p[1]-q[1])**2
 
    def fly(self,p,q) -> int:
        # the square-distance, fitting to the neighbours-function.
        return max(abs(p[0]-q[0]),abs(p[1]-q[1]))

    def octagondist(self, p, q) -> int:
        dx = abs(p[0] - q[0])
        dy = abs(p[1] - q[1])
        return dx + dy + max(dx, dy)

    def circledist(self, p,q) -> float:
        return sqrt(self.sdist(p,q))

    ############## terrain routines ###################################

    def get_terrain(self, dpoint):
        # for a dpoint of the 399x399 grid, return (layout,height)
        if (dpoint[0] < 0) or (dpoint[0] >= 399) or (dpoint[1] < 0) or (dpoint[1] >= 399):
            print('dpoint ERROR')
        else:
            return (layout_if.layout[dpoint[0] // 2][dpoint[1] // 2], layout_if.height[(dpoint[0]+1) // 2][(dpoint[1]+1) // 2])

    def terrain_get_neighbours(self,square):
        self.neighbours = set()
        self.neighbours.add((square[0] - 1, square[1] + 0))
        self.neighbours.add((square[0] + 0, square[1] - 1))
        self.neighbours.add((square[0] + 1, square[1] + 0))
        self.neighbours.add((square[0] + 0, square[1] + 1))
        self.neighbours.add((square[0] - 1, square[1] - 1))
        self.neighbours.add((square[0] + 1, square[1] - 1))
        self.neighbours.add((square[0] + 1, square[1] + 1))
        self.neighbours.add((square[0] - 1, square[1] + 1))

    def terrain_extend(self,aset):
        # aset is enlarged with same terrain
        square = aset.pop()
        aset.add(square)
        myterrain = self.get_terrain(square)
        smallset = set()
        bigset = aset
        while len(smallset)<len(bigset):
            smallset = bigset.copy()
            for square in smallset:
                self.terrain_get_neighbours(square)
                for nsquare in self.neighbours:
                    if self.get_terrain(nsquare) == myterrain:
                        bigset.add(nsquare)
        aset = bigset.copy()

    def terrain_get_edge(self,aset):
        # self.edgeresult is the squares around aset
        square = aset.pop()
        aset.add(square)
        myterrain = self.get_terrain(square)
        self.edgeresult = set()
        for square in aset:
            self.terrain_get_neighbours(square)
            for nsquare in self.neighbours:
                if self.get_terrain(nsquare) != myterrain:
                    self.edgeresult.add(nsquare)



solo = prog()
solo.main()

            
