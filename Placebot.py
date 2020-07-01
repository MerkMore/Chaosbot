# Placebot.py
# Uses a human to suggest building placement
# put the output   starting from "#####"   in a file "placement.txt"
# author: MerkMore
# version 18 june 2020
# Burny style
# python -m pip install Pillow
import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer
from sc2.constants import *
from sc2.position import Point2
import random
from sc2.game_info import GameInfo
from PIL import Image, ImageDraw



class Placebot(sc2.BotAI):
#   constants
    pointtoures = []
    all_structures = []
    index = 0
    bobtag = 0
    johntag = 0
    miketag = 0
    asked = False
    home = None
    gasbuilt = False
    gasmining = False
    layout = []
    img = None
#   rgb
    grey = (125,125,125)
    white = (255,255,255)
    green = (0,125,0)
    blue = (0,0,125)
    red = (125,0,0)
    black = (0,0,0)

    async def on_step(self, iteration: int):
#       init stuff
        if iteration == 0:
            print('put next lines in a file   placement.txt')
            print('#####')
            mapplace = 'map: '+self.game_info.map_name+' '+str(self.start_location.position.x)+' '+str(self.start_location.position.y)
            print(mapplace)
#           list of most structures
            self.pointto(SUPPLYDEPOT)
            self.pointto(SUPPLYDEPOT)
            self.pointto(BARRACKS)
            self.pointto(FACTORY)
            self.pointto(SUPPLYDEPOT)
            self.pointto(ENGINEERINGBAY)
            self.pointto(STARPORT)
            self.pointto(FUSIONCORE)
            self.pointto(MISSILETURRET)
            self.pointto(MISSILETURRET)
            self.pointto(MISSILETURRET)
            self.pointto(BARRACKS)
            self.pointto(FACTORY)
            self.pointto(STARPORT)
            self.pointto(FUSIONCORE)
            self.pointto(ARMORY)
            cc = self.townhalls.ready[0]
            self.home = cc.position.towards(self.game_info.map_center, 5)
#           1 bob, 1 john, 1 mike
            for scv in self.units(SCV).ready:
                self.miketag = self.johntag
                self.johntag = self.bobtag                
                self.bobtag = scv.tag                
            for scv in self.units(SCV).ready:
                if scv.tag == self.bobtag:
                    scv(MOVE_MOVE,self.home)
            self.get_layout()
            self.all_structures.append((COMMANDCENTER,5))
            self.all_structures.append((SUPPLYDEPOT,2))
            self.all_structures.append((BARRACKS,3))
            self.all_structures.append((FACTORY,3))
            self.all_structures.append((ENGINEERINGBAY,3))
            self.all_structures.append((STARPORT,3))
            self.all_structures.append((FUSIONCORE,3))
            self.all_structures.append((MISSILETURRET,2))
            self.all_structures.append((ARMORY,3))
#       main iteree
#       
        await self.refine()
        if self.gasmining:
            building = self.pointtoures[self.index]
            await self.build_building(building)
        await self.build_techlabs()
        await self.lower_depots()

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
                        self.layout[vakx][vaky] = 4


#   distance
    def sdist(self,p,q) -> int:
        return (p[0]-q[0])**2 + (p[1]-q[1])**2
 
    def near(self,p,q,supdist) -> bool:
        return (self.sdist(p,q) < supdist**2)

    def pointto(self,barra):
        self.pointtoures.append(barra)

    def get_layout(self):
        self.layout = []
#       layout is in a col=right,row=up notation
        for col in range(0,200):
            collist = []
            for row in range(0,200):
                info = 0
                point = Point2((col,row))
#               point2 is a (x=right,y=up notation)
                if (col<self.game_info.playable_area.width+self.game_info.playable_area.x) \
                and (col>=self.game_info.playable_area.x) \
                and (row<self.game_info.playable_area.height+self.game_info.playable_area.y) \
                and (row>=self.game_info.playable_area.y):
                    if self.game_info.pathing_grid[point] == 0:
                        info = info+1
                    if self.game_info.placement_grid[point] == 0:
                        info = info+2
                else:
                    info = 3
                collist.append(info)
            self.layout.append(collist)

    def photo(self):
        self.img = Image.new('RGB', (450, 450),self.grey)
        for col in range(0,200):
#           Draw uses a (right,down) notation
            for row in range(0,200):
                swaprow = 200-row
                info = self.layout[col][row]
                if info == 0:
#                   buildable
                    rgb = self.white
                elif info == 1:
                    rgb = self.green
                elif info == 2:
                    rgb = self.blue
                elif info == 3:
                    rgb = self.red
                else:
                    rgb = self.black
                ImageDraw.Draw(self.img).rectangle([25+col*2,25+swaprow*2,27+col*2,27+swaprow*2],fill=rgb,outline=None)
        self.img.save('layout.png')




    async def build_building(self,building):
        if not self.asked:
            self.asked = True
            await self.chat_send('Were to build '+building.name)
            self.realized()
            self.photo()
        for scv in self.units(SCV).ready.idle:
            if scv.tag == self.bobtag:
                place = scv.position
                dist = (self.home.x-place.x)**2 + (self.home.y-place.y)**2
                if dist > 1:
                    await self.chat_send('ah')
                    if await self.build(building,place):
                        pass
                    self.index = self.index+1
                    if self.index == len(self.pointtoures):
                        self.index = 0
                    scv(MOVE_MOVE,self.home)
                    self.asked = False


    async def lower_depots(self):
        for sd in self.structures(SUPPLYDEPOT):
            sd(MORPH_SUPPLYDEPOT_LOWER)



    async def build_techlabs(self):
        thing = BARRACKSTECHLAB
        for ba in self.structures(BARRACKS).ready.idle:
            if not ba.has_add_on:
                if self.can_afford(thing):
                    ba.build(thing)
        thing = FACTORYTECHLAB
        for ba in self.structures(FACTORY).ready.idle:
            if not ba.has_add_on:
                if self.can_afford(thing):
                    ba.build(thing)
        thing = STARPORTTECHLAB
        for ba in self.structures(STARPORT).ready.idle:
            if not ba.has_add_on:
                if self.can_afford(thing):
                    ba.build(thing)
 


    async def refine(self):
        if not self.gasbuilt:
            if self.minerals>75:
                self.gasbuilt = True
                vg = self.vespene_geyser.closest_to(self.start_location.position)
                for scv in self.units(SCV).ready:
                    if scv.tag == self.johntag:
                        scv.build(REFINERY,vg)
        if (not self.gasmining) and (self.vespene>0):
            self.gasmining = True
            vg = self.structures(REFINERY).ready.random        
            for scv in self.units(SCV).ready:
                if scv.tag == self.miketag:
                    scv.gather(vg)


            
run_game(maps.get("ThunderbirdLE"), [
    Bot(Race.Terran, Placebot()),
    Computer(Race.Protoss, Difficulty.Easy)
    ], realtime=True)
