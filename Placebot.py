# Placebot.py
# Uses a human to suggest building placement
# put the output   starting from "#####"   in a file "placement.txt"
# author: MerkMore
# version 18 june 2020
# Burny style
import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer
from sc2.constants import *
from sc2.position import Point2
import random



class Placebot(sc2.BotAI):
#   constants
    most_structures = []
    index = 0
    bobtag = 0
    johntag = 0
    miketag = 0
    asked = False
    home = None
    gasbuilt = False
    gasmining = False

    async def on_step(self, iteration: int):
#       init stuff
        if iteration == 0:
            print('put next lines in a file   placement.txt')
            print('#####')
            mapplace = 'map: '+self.game_info.map_name+' '+str(self.start_location.position.x)+' '+str(self.start_location.position.y)
            print(mapplace)
#           list of most structures
            self.most_struct(SUPPLYDEPOT)
            self.most_struct(SUPPLYDEPOT)
            self.most_struct(BARRACKS)
            self.most_struct(FACTORY)
            self.most_struct(SUPPLYDEPOT)
            self.most_struct(BARRACKS)
            self.most_struct(STARPORT)
            self.most_struct(SUPPLYDEPOT)
            self.most_struct(FACTORY)
            self.most_struct(MISSILETURRET)
            self.most_struct(MISSILETURRET)
            self.most_struct(MISSILETURRET)
            self.most_struct(BARRACKS)
            self.most_struct(FUSIONCORE)
            self.most_struct(STARPORT)
            self.most_struct(ENGINEERINGBAY)
            self.most_struct(ARMORY)
            self.most_struct(ARMORY)
            self.most_struct(FUSIONCORE)
            self.most_struct(FUSIONCORE)
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
#       main iteree
#       
        await self.refine()
        if self.gasmining:
            building = self.most_structures[self.index]
            await self.build_building(building)
        await self.build_techlabs()
        await self.lower_depots()

    def realized(self,building,place):
        x = round(place.x)
        y = round(place.y)
        print('position '+building.name+' '+str(x)+' '+str(y))


    def most_struct(self,barra):
        self.most_structures.append(barra)



    async def build_building(self,building):
        if not self.asked:
            self.asked = True
            await self.chat_send('Were to build '+building.name)
        for scv in self.units(SCV).ready.idle:
            if scv.tag == self.bobtag:
                place = scv.position
                dist = (self.home.x-place.x)**2 + (self.home.y-place.y)**2
                if dist > 1:
                    await self.chat_send('ah')
                    if await self.build(building,place):
                        self.realized(building,place)
                    self.index = self.index+1
                    if self.index == len(self.most_structures):
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
