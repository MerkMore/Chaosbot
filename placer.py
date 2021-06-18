# Placer.py
# Makes text for building placement
# appends the output to file "data\placement.txt"
# author: MerkMore
# version 16 jun 2021
from layout_if_py import layout_if
import random
from math import sqrt, sin, cos, acos, pi

#
# 0 = free
# 1 = minerals,gas, rocks
# 2 = ramp, unbuildable
# 3 = nogo
# 4 = building
# 5 = nobuild
#

class prog:
    #
    testing = False
    mapplace = ''
    mapleft = 0
    mapright = 0
    mapbot = 0
    maptop = 0
    mapcenter = (0,0)
    filterresult = set()
    enemybasearea = set()
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
        didsomething = False
        for self.mapplace in self.maps:
            old = False
            for line in content:
                if line == self.mapplace:
                    old = True
            if old:
                print(self.mapplace+' is already in data\placement.txt')
            else:
                print('analyzing '+self.mapplace)
                didsomething = True
                layout_if.load_layout(self.mapplace)
                #layout_if.photo_layout() # debug
                #layout_if.photo_height() # debug
                self.appendthemap()
                #layout_if.photo_layout() # debug
                #layout_if.photo_height() # debug
        if not didsomething:
            self.testing = True
            # using the last self.mapplace
            print('test analyzing ' + self.mapplace)
            layout_if.load_layout(self.mapplace)
            self.appendthemap()
            layout_if.photo_layout() # debug

    def appendthemap(self):
        if self.testing:
            text = open('data\pest.txt','w')
        else:
            text = open('data\placement.txt','a')
        text.write('#####'+'\n')
        text.write(self.mapplace+'\n')
        #
        # MAPINFO
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
        toskip = (self.enemystartsquare[0]-2,self.enemystartsquare[1]-2)
        for x in range(0,200):
            for y in range(0,200):
                lo = (x,y)
                if self.has_cc(lo):
                    if lo != toskip:
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
        self.enemybasearea = aroundcc.copy()
        self.extend(self.enemybasearea) # the whole enemy top area
        self.logg('self.enemybasearea '+str(len(self.enemybasearea)))
        self.get_edge(self.enemybasearea)
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
                enemyramptop_tobeusedlater = square
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
        # enemynatural
        closest = 99999
        for lo in self.expansions:
            sd = self.sdist(lo,self.enemystartsquare)
            if sd > 3*3:
                sd = self.sdist(lo,enemyramp)
                if sd < closest:
                    closest = sd
                    self.enemynatural = (lo[0]+2,lo[1]+2)
        x = self.enemynatural[0]+0.5
        y = self.enemynatural[1]+0.5
        text.write('position ENEMYNATURAL ' + str(x) + ' ' + str(y) + '\n')
        # enemythird
        closest = 99999
        for lo in self.expansions:
            sd = self.sdist(lo,self.enemystartsquare)
            if sd > 3*3:
                sd = self.sdist(lo, self.enemynatural)
                if sd > 3 * 3:
                    sd = self.sdist(lo,enemyramp)
                    if sd < closest:
                        closest = sd
                        self.enemythird = (lo[0]+2,lo[1]+2)
        x = self.enemythird[0]+0.5
        y = self.enemythird[1]+0.5
        text.write('position ENEMYTHIRD ' + str(x) + ' ' + str(y) + '\n')
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
        #
        # ENEMY NATURAL CHOKE
        # centertile
        around = self.mapcenter
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
        # estimate a choke as enemynatural in the direction of mapcenter dist 0.5*dist(enemystart,enemynatural)
        wantsize = 0.5 * self.circledist(self.enemynatural,self.enemystartsquare)
        hassize = self.circledist(self.enemynatural,self.mapcenter)
        vec = (self.mapcenter[0] - self.enemynatural[0], self.mapcenter[1] - self.enemynatural[1])
        vec = (vec[0] * wantsize / hassize, vec[1] * wantsize / hassize)
        estimate = (round(self.enemynatural[0] + vec[0]),round(self.enemynatural[1] + vec[1]))
        self.logg('estimate en. nat. choke '+str(estimate[0])+','+str(estimate[1]))
        enemynaturalchoke = estimate
        # check that a tankpath can be found without choking
        ennattile = (round(self.enemynatural[0]),round(self.enemynatural[1]))
        while not self.istile(ennattile): # can place a tank
            ennattile = (ennattile[0],ennattile[1]+1)
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
            enemynaturalchoke = (round(x),round(y))
        #
        # WALKING dist to enemy
        # enemy starts being colored 4, temporally erase it
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
        # put back the enemy base
        self.colorplace(5, cccorner, 4)
        #
        # FLEE CIRCLE
        # find a big circle
        away = (200 - self.enemystartsquare[0], 200 - self.startsquare[1]) # not his main, not my main
        found = False
        while not found:
            middle = (random.randrange(0, 200), random.randrange(0, 200))
            if self.sdist(middle,away) < 80*80:
                radius = 8
                apoint = (round(middle[0]+radius),round(middle[1]))
                if self.inmap(apoint):
                    myheight = layout_if.height[apoint[0]][apoint[1]]
                    ok = True
                    for nr in range(0, 15):
                        beta = nr * 2 * pi / 15
                        apoint = (round(middle[0] + cos(beta) * radius),round(middle[1] + sin(beta) * radius))
                        if self.inmap(apoint):
                            itsheight = layout_if.height[apoint[0]][apoint[1]]
                            ok = ok and (myheight == itsheight)
                            ok = ok and (layout_if.layout[apoint[0]][apoint[1]] == 0)
                        else:
                            ok = False
                    if ok:
                        found = True
                        text.write('position FOLLOWERS ' + str(middle[0] + 0.5) + ' ' + str(middle[1] + 0.5) + '\n')
                        self.logg('position FOLLOWERS ' + str(middle[0] + 0.5) + ' ' + str(middle[1] + 0.5))
        #
        # RAMP WALL
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
        #
        # NOBUILD PATH
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
        # COCOON
        # Find a 8*8 cocoon spot near the enemy choke.
        # Do not draw/reserve it as this spot can have other uses.
        anchor = enemynaturalchoke
        idealsd = 35
        besttry = 99999
        found_spot = (0, 0)
        estimate = self.fromto(anchor, self.mapcenter, sqrt(idealsd))
        for dx in range(-20, 20):
            for dy in range(-20, 20):
                maypos = (estimate[0] + dx, estimate[1] + dy)
                if self.can_place_shape(8, maypos):
                    sd = self.sdist(anchor, maypos)
                    try0 = (sd - idealsd) * (sd - idealsd) + self.circledist(maypos, self.mapcenter)
                    if try0 < besttry:
                        found_spot = maypos
                        besttry = try0
        if besttry != 99999:
            place = found_spot
            text.write('position INFESTEDCOCOON ' + str(place[0] + 4) + ' ' + str(place[1] + 4) + '\n')
            self.logg('position INFESTEDCOCOON ' + str(place[0] + 4) + ' ' + str(place[1] + 4))
        #
        # PF POSITIONS
        # find a close hallposition for each old hallposition
        for anchor in self.expansions:
            idealsd = 115
            besttry = 99999
            found_spot = (0,0)
            estimate = self.fromto(anchor,self.mapcenter,sqrt(idealsd))
            for dx in range(-20, 20):
                for dy in range(-20, 20):
                    maypos = (estimate[0] + dx, estimate[1] + dy)
                    if self.can_place_shape(5, maypos):
                        if self.not_near_minerals(maypos):
                            sd = self.sdist(anchor, maypos)
                            try0 = (sd - idealsd)*(sd-idealsd) + self.circledist(maypos,self.mapcenter)
                            if try0 < besttry:
                                found_spot = maypos
                                besttry = try0
            if besttry != 99999:
                place = found_spot
                self.do_place_shape(5, place)
                text.write('position EXTRACC ' + str(place[0] + 2.5) + ' ' + str(place[1] + 2.5) + '\n')
                self.logg('position EXTRACC ' + str(place[0] + 2.5) + ' ' + str(place[1] + 2.5))
        #
        # find some highground pf positions
        extras = 0
        while extras < 10:
            place = (random.randrange(0,200),random.randrange(0,200))
            if place not in self.enemybasearea:
                if self.can_place_shape(5, place):
                    if self.not_near_minerals(place):
                        myheight = layout_if.height[place[0]][place[1]]
                        itishigh = False
                        for dx in [-5, 0, 5]:
                            for dy in [-5, 0, 5]:
                                alt = (place[0]+2+dx,place[1]+2+dy)
                                if (alt[0] >= 0) and (alt[0] < 200) and (alt[1] >= 0) and (alt[1] < 200):
                                    if layout_if.layout[alt[0]][alt[1]] in {0,2}:
                                        itsheight = layout_if.height[alt[0]][alt[1]]
                                        if myheight > itsheight:
                                            itishigh = True
                        if itishigh:
                            self.do_place_shape(5, place)
                            text.write('position EXTRACC ' + str(place[0] + 2.5) + ' ' + str(place[1] + 2.5) + '\n')
                            self.logg('position EXTRACC ' + str(place[0] + 2.5) + ' ' + str(place[1] + 2.5))
                            extras += 1
        #
        # STARPORT POSITIONS
        # now, find some hidden fusioncore positions
        for shape in (3,3.5):
            alters = []
            while len(alters)<10000:
                alt = (random.randrange(0,200),random.randrange(0,200))
                dis = self.sdist(alt,self.startsquare)
                if (dis>17*17) and (dis<90*90):
                    dis = self.sdist(alt,self.ramptopcenter)
                    if (dis>25*25):
                        dis = self.sdist(alt,self.enemystartsquare)
                        if (dis>25*25):
                            if self.can_place_shape(shape,alt):
                                if self.walking[alt[0]][alt[1]] > 0:
                                    alters.append(alt)
            choices = []
            while len(choices)<7:
                bestdist = 0
                for alt in alters:
                    allowed = True
                    for have in choices:
                        dis = self.sdist(alt,have)
                        allowed = allowed and (dis>10*10)
                    if allowed:
                        dis = self.sdist(alt,self.mapcenter)
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
        # scout
        # make scout positions just inside the enemy base
        self.logg('enemybasearea '+str(len(self.enemybasearea)))
        self.get_edge(self.enemybasearea)
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
        inside = inside & self.enemybasearea
        self.logg('inside '+str(len(inside)))
        ramptopsquare = enemyramptop_tobeusedlater
        radius = self.circledist(ramptopsquare,self.enemystartsquare)
        self.logg('radius '+str(radius))
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
            bestsdist = 99999
            for square in inside:
                sd = self.sdist(square,circlepoint)
                if sd < bestsdist:
                    bestsquare = square
                    bestsdist = sd
            text.write('position SCOUT '+str(bestsquare[0]+0.5)+' '+str(bestsquare[1]+0.5)+'\n')
        # reapers
        # find reaperjumpspots near the self.enemybasearea
        reaperbunker1 = (0,0)
        reaperbunker2 = (0,0)
        square = tuple(self.enemybasearea)[0]
        dsquare = (square[0]*2,square[1]*2)
        (baselayout, baseheight) = self.get_terrain(dsquare)
        darea = {dsquare}
        self.terrain_extend(darea)
        self.terrain_get_edge(darea)
        possi = self.edgeresult.copy()
        self.terrain_get_edge(possi)
        possi = self.edgeresult
        reaperall = set()
        for dsquare in possi:
            (layout,height) = self.get_terrain(dsquare)
            if (height == baseheight - 16) and (layout == 0):
                self.logg('reaperjumppoint '+str(layout)+' '+str(height)+' '+str(dsquare[0]/2)+','+str(dsquare[1]/2))
                reaperall.add(dsquare)
        for dsquare in reaperall:
            x = dsquare[0] / 2
            y = dsquare[1] / 2
            self.logg('position REAPERJUMP ' + str(x) + ' ' + str(y))
            text.write('position REAPERJUMP ' + str(x) + ' ' + str(y) + '\n')
            # color it to debug
            #square = (dsquare[0] // 2,dsquare[1] // 2)
            #self.colorplace(1,square,5)
        # make reaperbasespots, real squares inside the enemy base
        reaperbasespots = set()
        for dsquare in reaperall:
            jumpsquare = (dsquare[0] / 2,dsquare[1] / 2) # can have halves
            bestsd = 99999
            for square in self.enemybasearea:
                sd = self.sdist(square, jumpsquare)
                if sd < bestsd:
                    bestsquare = square
                    bestsd = sd
            reaperbasespots.add(bestsquare)
        self.logg('reaperbasespots '+str(len(reaperbasespots)))
        # reaperjumpspot: get the reaperbasespot away from enemyramp and near mapcenter
        bestqual = -99999
        for square in reaperbasespots:
            qual = 2 * self.octagondist(square, enemyramp) - self.octagondist(square, self.mapcenter)
            if qual > bestqual:
                bestqual = qual
                reaperjumpspot = square
        # restrict to blockable with two bunkers
        goodspots = set()
        for square in reaperbasespots:
            if self.twoblock(square):
                goodspots.add(square)
        self.logg('goodspots ' + str(len(goodspots)))
        if len(goodspots) > 0:
            # reaperjumpspot: get the goodspot away from enemyramp and near mapcenter
            bestqual = -99999
            for square in goodspots:
                qual = 2 * self.octagondist(square,enemyramp) - self.octagondist(square,self.mapcenter)
                if qual > bestqual:
                    bestqual = qual
                    reaperjumpspot = square
            self.logg('reaperjumpspot '+str(reaperjumpspot[0])+' '+str(reaperjumpspot[1]))
        if len(goodspots) > 0:
            # block reaperbasejump with two bunkers
            if self.twoblock(reaperjumpspot):
                text.write('position REAPERBUNKER1 '+str(self.asol[0][0]+1.5)+' '+str(self.asol[0][1]+1.5)+'\n')
                text.write('position REAPERBUNKER2 '+str(self.asol[1][0]+1.5)+' '+str(self.asol[1][1]+1.5)+'\n')
                reaperbunker1 = self.asol[0]
                reaperbunker2 = self.asol[1]
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
        # get the reaperbarracksspot
        if len(reaperbasespots) > 0:
            around = self.fromto(reaperjumpspot,self.mapcenter,12)
            self.logg('reaperbarracks around '+str(around[0])+','+str(around[1]))
            bestsd = 99999
            for x in range(around[0]-15,around[0]+15):
                for y in range(around[1]-15,around[1]+15):
                    square = (x,y)
                    if self.can_place_shape(3.5,square): # can place barracks
                        acceptable = True
                        for ba in self.enemybasearea:
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
                # do not place, it interferes with next code
                # self.do_place_shape(3.5, bestsquare)
            else:
                self.logg('no reaperbarracks')
        else:
            self.logg('no reaperbasespots')
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
        # now we hope to place a single barracks there
        leftunder = (bestsquare[0]-1,bestsquare[1]-1)
        placed = self.can_place_shape(3,leftunder)
        barracksproposal = leftunder
        dist = 0
        while not placed:
            dist = dist+1
            for dx in range(-dist,dist):
                for dy in range(-dist,dist):
                    maybe = (leftunder[0]+dx,leftunder[1]+dy)
                    if maybe not in self.enemybasearea:
                        if self.can_place_shape(3,maybe):
                            barracksproposal = maybe
                            placed = True
        # if not unlucky, this result is a good cheese barracks building place
        # go find a corner in the enemy base
        corners = set()
        for square in self.enemybasearea:
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
        self.logg('two-block prisons '+str(len(corners)))
        # get one close to barracksproposal
        bestsd = 99999
        for cornersquare in corners:
            sd = self.sdist(cornersquare,barracksproposal)
            if sd < bestsd:
                bestcornersquare = cornersquare
                bestsd = sd
        cornersquare = bestcornersquare
        if self.twoblock(cornersquare):
            self.logg('prison size '+str(len(self.asolprison)))
        # of those, the closest to the enemy should be the bunker
        sd0 = self.sdist(self.asol[0],self.enemystartsquare)
        sd1 = self.sdist(self.asol[1],self.enemystartsquare)
        if sd0 < sd1:
            text.write('position INFESTEDBUNKER '+str(self.asol[0][0]+1.5)+' '+str(self.asol[0][1]+1.5)+'\n')
            self.logg('position INFESTEDBUNKER '+str(self.asol[0][0]+1.5)+' '+str(self.asol[0][1]+1.5))
            text.write('position INFESTEDLANDING '+str(self.asol[1][0]+1.5)+' '+str(self.asol[1][1]+1.5)+'\n')
            self.logg('position INFESTEDLANDING '+str(self.asol[1][0]+1.5)+' '+str(self.asol[1][1]+1.5))
        else:
            text.write('position INFESTEDLANDING ' + str(self.asol[0][0] + 1.5) + ' ' + str(self.asol[0][1] + 1.5) + '\n')
            self.logg('position INFESTEDLANDING ' + str(self.asol[0][0] + 1.5) + ' ' + str(self.asol[0][1] + 1.5))
            text.write('position INFESTEDBUNKER ' + str(self.asol[1][0] + 1.5) + ' ' + str(self.asol[1][1] + 1.5) + '\n')
            self.logg('position INFESTEDBUNKER ' + str(self.asol[1][0] + 1.5) + ' ' + str(self.asol[1][1] + 1.5))
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
        # get a 5x5 freespace outside self.enemybasearea, as a tankmove point
        # this freespace must have a tankpath to enemybasearea.
        enemytile = self.enemystartsquare
        while not self.istile(enemytile):
            enemytile = (enemytile[0],enemytile[1]+1)
        haspath = False
        while not haspath:
            self.logg('searching freespace')
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
            haspath = self.has_tankpath(enemytile, freespace)
        self.logg('freespace '+str(freespace[0])+','+str(freespace[1]))
        # get a 2x2 place for a tank near cheeseprison but outside self.enemybasearea
        self.logg('B')
        around = (round(avera0),round(avera1))
        bestsd = 9999
        for x in range(around[0]-10,around[0]+10):
            for y in range(around[1]-10,around[1]+10):
                square = (x,y)
                if square not in self.enemybasearea:
                    if self.istile(square): # can place a tank
                        sd = self.sdist(square,self.centerresult)
                        if sd < bestsd:
                            if self.has_tankpath(square, freespace):
                                bestsquare = square
                                bestsd = sd
        tanksquare = bestsquare
        text.write('position INFESTEDTANK '+str(tanksquare[0])+' '+str(tanksquare[1])+'\n')
        self.logg('position INFESTEDTANK '+str(tanksquare[0])+' '+str(tanksquare[1]))
        # get barracksposition around barracksproposal, close to centerresult prison, it may cross the tankspot
        self.logg('C')
        around = barracksproposal
        bestsd = 9999
        for x in range(around[0]-10,around[0]+10):
            for y in range(around[1]-10,around[1]+10):
                square = (x,y)
                if square not in self.enemybasearea:
                    if self.can_place_shape(3, square):
                        sd = self.sdist(square,self.centerresult)
                        if sd < bestsd:
                            bestsquare = square
                            bestsd = sd
        barracksposition = bestsquare
        text.write('position INFESTEDBARRACKS '+str(barracksposition[0]+1.5)+' '+str(barracksposition[1]+1.5)+'\n')
        self.do_place_shape(3,barracksposition)
        # factory
        # get infested_factory place, about 14 from the infestedbarracks, away from the enemy
        vector = (barracksposition[0] - self.enemystartsquare[0], barracksposition[1] - self.enemystartsquare[1])
        factor = 14 / self.circledist(barracksposition, self.enemystartsquare)
        factorysuggestion = (round(barracksposition[0] + factor * vector[0]), \
                             round(barracksposition[1] + factor * vector[1]))
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
        self.do_place_shape(3.5, factoryresult)
        #
        # delayed show
        if reaperbunker1 != (0,0):
            self.do_place_shape(3, reaperbunker1)
        if reaperbunker2 != (0, 0):
            self.do_place_shape(3, reaperbunker2)
        #
        #  that is all
        text.write('#####'+'\n')
        text.close()


    def inmap(self, alt) -> bool:
        return (alt[0] >= 0) and (alt[0] < 200) and (alt[1] >= 0) and (alt[1] < 200)

    def twoblock(self, cornersquare) -> bool:
        # try to lock this self.enemybasearea square in with 2 3x3 blocks
        # return self.asol ([0] and [1] leftunderpoints of 3x3 blocks)
        # return self.asolprison (the enclosed squares)
        cornersquares = set([cornersquare])
        opensquare = self.enemystartsquare
        while self.get_color(opensquare) != 0:
            opensquare = (opensquare[0],opensquare[1]+1)
        aroundcc = set([opensquare])
        self.path_direction = opensquare
        totry = set()
        for dx in range(-6, 6):
            for dy in range(-6, 6):
                square = (cornersquare[0] + dx, cornersquare[1] + dy)
                if self.get_color(square) == 0:
                    if square in self.enemybasearea:
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
                                    # next check is needed as the ramp is accessible
                                    if not self.has_path(cornersquares, aroundcc):
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
        # leftunder definition
        if shape == 3.5:
            # starport
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
        else:
            for dx in range(0, shape):
                for dy in range(0, shape):
                    layout_if.layout[alt[0] + dx][alt[1] + dy] = 4


    def can_place_shape(self,shape,alt) -> bool:
        # leftunder definition
        can = (alt[0] >= 0) and (alt[0]+shape < 200) and (alt[1] >= 0) and (alt[1]+shape < 200)
        if can:
            if shape == 3.5:
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
                for dx in range(0, shape):
                    for dy in range(0, shape):
                        can = can and (layout_if.layout[alt[0] + dx][alt[1] + dy] == 0)
        return can

    def not_near_minerals(self, place) -> bool:
        # hall placement
        # a bit too restrictive, the standard expansions would fail.
        can = (place[0] >= 3) and (place[0] + 7 < 200) and (place[1] >= 3) and (place[1] + 7 < 200)
        if can:
            for dx in range(-3,8):
                for dy in range(-3,8):
                    can = can and (layout_if.layout[place[0] + dx][place[1] + dy] != 1)
        return can

    def has_cc(self, alt) -> bool:
        # Is alt the leftunder point of a cc?
        has = (alt[0] >= 0) and (alt[0] + 4 < 200) and (alt[1] >= 0) and (alt[1] + 4 < 200)
        if has:
            has = has and (layout_if.layout[alt[0] + 0][alt[1] + 0] == 4)
            if has:
                for dx in range(0,5):
                    for dy in range(0,5):
                        has = has and (layout_if.layout[alt[0] + dx][alt[1] + dy] == 4)
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

    def fromto(self, fra, ta, dist): # -> point
        direction = (ta[0] - fra[0], ta[1] - fra[1])
        norm = sqrt(direction[0]*direction[0] + direction[1]*direction[1])
        factor = dist / norm
        vector = (round(direction[0]*factor), round(direction[1]*factor))
        res = (fra[0] + vector[0], fra[1] + vector[1])
        return res
    
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

            
