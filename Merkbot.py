# Merkbot.py containing Chaosbot
# author: MerkMore
# version 4 july 2020
# Burny style
import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer
from sc2.constants import *
from sc2.position import Point2
import random
from math import sqrt
from sc2.game_info import GameInfo
import layout_if



class Chaosbot(sc2.BotAI):
#   ############### CHANGE VALUE AD LIB
    do_log_success = True
    do_log_workers = True
    do_log_population = False
    do_log_armysize = False
    do_log_army = False
    do_log_attacktype = True
    do_log_gasminer = False
    do_log_resource = False
    do_log_limbo = False
    do_log_wish = True
    do_log_workstock = True
    do_log_placing = True
    do_log_time = False
    do_log_layout = False
#   ############### CONSTANT
#   constant over the iterations after iteration 0:
#   other
    nowhere = Point2((1,1))
    all_structures = []
    all_structures_tobuildwalk = []
    all_army = []
    buildtime_of_structure = {}
    size_of_structure = {}
    liftable = []
    techtree = []
    anything = []
    cradle = []
    shipyard = None
#   squareroots of integers from 0 to 200*200*2, 0<=x<400
    stored_root = []
#   timing constants
    gas_speed = 1.0
    mim_speed = 1.0
    walk_speed = 4.0
    stocksize = 4
    miner_bound = 10
    enemyloc = None
    map_left = 0
    map_right = 0
    map_bottom = 0
    map_top = 0
#   ############### GAMESTATE
#   gamestate values constant in this iteration after gamestate:  
    itera = -1
    all_bases = []
    all_refineries = []
#   ############### REST
    routine = 'start'
#   stored tips
    tips = []
    tips_used = []
#   coding problem
    function_result_Point2 = None
    idle_structure_tags = []
    last_log_workstock_string = ''
#   ############### ARMY AND STRUCTURE MANAGEMENT
#   the supplydepot used as a gate:
    updown = -1
#   army coodination
    frozenbctags = set()
    attack_type = 'chaos'
    cruisercount = 0
    lastcruisercount = 0
    never_had_a_bc = True
    home_of_flying_struct = {}
    bct_in_repair = []
    bestbctag = -1
    bc_fear = 250
#   ambition contains commandcenters becoming a planetaryfortress, factories getting a techlab, etc.
    ambition_of_strt = {}
#   the barracks in the wall could be placed such as not to be able to get a techlab
    add_on_denied = []
    towt_of_tnkt = {}
    army_center_point = None 
#   ############### SCV MANAGEMENT
#   traveller and builder scvs have a goal
#   traveller and builder scvs have a structure to build
#   for a traveller, the cost of its building is reserved
    goal_of_trabu_scvt = {}
    structure_of_trabu_scvt = {}
#   scv management:
#   The tag of existing own scvs, in this iteration
    all_scvt = []
#   The tag of existing refineries where we want to mine from, in this iteration
    all_gast = []
#   The tag of existing minerals where we want to mine from, in this iteration
    all_mimt = []
#   job_of_scvt dictionary 
    all_job = ('gasminer','mimminer','applicant','traveller','escorter','builder','shiprepairer','arearepairer','idler','suicider','fleeer')
    job_of_scvt = {}
    count_of_job = {}
#   arearepairers have a cottage
    cottage_of_scvt = {}
#   applicants have a vision, a tag of a base to walk to
    vision_of_scvt = {}
#   recalculated each iteration:
    wanted_of_cct = {}
#   gas harvesting assignments
    gast_of_scvt = {}
    count_of_gast = {}
#   mineral harvesting assignments
    mimt_of_scvt = {}
    count_of_mimt = {}
#   When promoted, fire if idle, but not when not moved yet.
    promotionsite_of_scvt = {}
#   is_repairing
    busy_arearepairer = []
#   for missing scvs (fallen or in gaslimbo), the iteration is stored
    itera_of_missing_scvt = {}
#   fun translate output scvt to names
    all_names = []
    name_of_scvt = {}
#   ############### PLAY CHOICES
#   wish for rush
    rushing = True
    enddemand_am_of_th = {}
    endwish_am_of_th = {}
    wish_am_of_th = {}
    wish_pri_of_th = {}
    wish_now = []
    also_wish_now = []
    log_wish_history = ''
#   money handling with reservations
    reserved_minerals = 0
    reserved_vespene = 0
#   workstock of a few (building,place) combinations.
#   workstock can also contain things that don't need a place. Then place = nowhere.
#   workstock is 0, 1, 2 or 3  (see the constant stocksize)
#   work to be removed from the workstock when the order is started
#   workstock contains work we will do, it just is not clear when to start it, money is not reserved yet
    thing_of_workstock = {}
    place_of_workstock = {}


    async def on_step(self, iteration: int):
#       make iteration available for logging
        self.itera = iteration
#       init stuff
        if len(self.techtree) == 0:
            await self.my_init()
#       
#       main iteree:
#       
        await self.gamestate()
        self.log_resource()
        self.log_armysize()
        await self.build_worker(100-self.minerals//100)
        self.fill_workstock()
        await self.use_workstock()
        await self.start_construction()
        await self.siege_tank()
        await self.fire_yamato()
        await self.battle_jump_home()
        await self.ruin()
        await self.repair_it()
        await self.lift()
        await self.do_updown()
        await self.attack()
        await self.manage_workers()
        if self.minerals < self.vespene:
            await self.manage_minerals()
            await self.manage_gas()
        else:
            await self.manage_gas()
            await self.manage_minerals()
        await self.manage_rest() 



    async def my_init(self):
        self.routine = 'my_init'
        self.log_success('##############################################################################')
        random.seed()
#       liftable
        self.liftable = [BARRACKS,FACTORY,STARPORT,COMMANDCENTER]
        self.landable = [BARRACKSFLYING,FACTORYFLYING,STARPORTFLYING,COMMANDCENTERFLYING]
        self.all_army = [RAVEN,VIKINGFIGHTER,MARINE,MARAUDER,SIEGETANK,BATTLECRUISER,SIEGETANKSIEGED]
#       list of most structures, with buildtime, size
        self.init_structures(SUPPLYDEPOT, 50, 2)
        self.init_structures(BARRACKS, 60, 3)
        self.init_structures(REFINERY, 60, 3)
        self.init_structures(BARRACKSTECHLAB, 40, 2)
        self.init_structures(FACTORY, 60, 3)
        self.init_structures(FACTORYTECHLAB, 40, 2)
        self.init_structures(STARPORT, 60, 3)
        self.init_structures(STARPORTTECHLAB, 40, 2)
        self.init_structures(FUSIONCORE, 80, 3)
        self.init_structures(COMMANDCENTER, 90, 5)
        self.init_structures(PLANETARYFORTRESS, 30, 5)
        self.init_structures(ENGINEERINGBAY, 40, 3)
        self.init_structures(MISSILETURRET,30, 2)
        self.init_structures(ARMORY, 40, 3)
#       things that, to be built, need a cradle (a free building)
        self.init_cradle(RAVEN,STARPORT)
        self.init_cradle(VIKINGFIGHTER,STARPORT)
        self.init_cradle(MARINE,BARRACKS)
        self.init_cradle(MARAUDER,BARRACKS)
        self.init_cradle(SIEGETANK,FACTORY)
        self.init_cradle(BATTLECRUISER,STARPORT)
        self.init_cradle(BARRACKSTECHLAB,BARRACKS)
        self.init_cradle(FACTORYTECHLAB,FACTORY)
        self.init_cradle(STARPORTTECHLAB,STARPORT)
        self.init_cradle(PUNISHERGRENADES,BARRACKSTECHLAB)
        self.init_cradle(TERRANSHIPWEAPONSLEVEL1,ARMORY)
        self.init_cradle(TERRANSHIPWEAPONSLEVEL2,ARMORY)
        self.init_cradle(TERRANSHIPWEAPONSLEVEL3,ARMORY)
        self.init_cradle(TERRANVEHICLEANDSHIPARMORSLEVEL1,ARMORY)
        self.init_cradle(TERRANVEHICLEANDSHIPARMORSLEVEL2,ARMORY)
        self.init_cradle(TERRANVEHICLEANDSHIPARMORSLEVEL3,ARMORY)
        self.init_cradle(TERRANBUILDINGARMOR,ENGINEERINGBAY)
        self.init_cradle(TERRANINFANTRYWEAPONSLEVEL1,ENGINEERINGBAY)
        self.init_cradle(TERRANINFANTRYWEAPONSLEVEL2,ENGINEERINGBAY)
        self.init_cradle(TERRANINFANTRYWEAPONSLEVEL3,ENGINEERINGBAY)
        self.init_cradle(PLANETARYFORTRESS,COMMANDCENTER)
        self.init_cradle(BATTLECRUISERENABLESPECIALIZATIONS,FUSIONCORE)
#       Some preconditions.
#       Each element is a unit, upgrade, or structure. First can not be produced without second. 
#       In the init, those mentioned in init_cradle are not repeated.
#       The techtree does not contain multistep dependencies.
#       First is structure
        self.init_techtree(BARRACKS,SUPPLYDEPOT)
        self.init_techtree(BARRACKSTECHLAB,REFINERY)
        self.init_techtree(FACTORY,REFINERY)
        self.init_techtree(FACTORY,BARRACKS)
        self.init_techtree(FACTORYTECHLAB,REFINERY)
        self.init_techtree(STARPORT,FACTORY)
        self.init_techtree(STARPORTTECHLAB,REFINERY)
        self.init_techtree(PLANETARYFORTRESS,ENGINEERINGBAY)
        self.init_techtree(PLANETARYFORTRESS,REFINERY)
        self.init_techtree(MISSILETURRET,ENGINEERINGBAY)
        self.init_techtree(FUSIONCORE,STARPORT)
        self.init_techtree(ARMORY,FACTORY)
#       First is unit
        self.init_techtree(BATTLECRUISER,STARPORTTECHLAB)
        self.init_techtree(BATTLECRUISER,FUSIONCORE)
        self.init_techtree(SIEGETANK,FACTORYTECHLAB)
        self.init_techtree(MARAUDER,BARRACKSTECHLAB)
        self.init_techtree(RAVEN,STARPORTTECHLAB)
#       First is upgrade
        self.init_techtree(TERRANSHIPWEAPONSLEVEL2,TERRANSHIPWEAPONSLEVEL1)
        self.init_techtree(TERRANSHIPWEAPONSLEVEL3,TERRANSHIPWEAPONSLEVEL2)
        self.init_techtree(TERRANVEHICLEANDSHIPARMORSLEVEL2,TERRANVEHICLEANDSHIPARMORSLEVEL1)
        self.init_techtree(TERRANVEHICLEANDSHIPARMORSLEVEL3,TERRANVEHICLEANDSHIPARMORSLEVEL2)
        self.init_techtree(TERRANINFANTRYWEAPONSLEVEL2,TERRANINFANTRYWEAPONSLEVEL1)
        self.init_techtree(TERRANINFANTRYWEAPONSLEVEL3,TERRANINFANTRYWEAPONSLEVEL2)
        self.compute_anything()
#       shipyard
        self.shipyard = self.start_location.position.towards(self.game_info.map_center,4)
        self.enemyloc = self.enemy_start_locations[0].position
        self.fix_count_of_job()
#       priority strategy
        await self.rush(BATTLECRUISER,1)
        await self.rush(SIEGETANK,1)
        await self.rush(MARINE,7)
        await self.rush(COMMANDCENTER,2)
        await self.rush(REFINERY,4)
        await self.rush(SUPPLYDEPOT,2)
        await self.rush_stop(BATTLECRUISER,1)
#       layout
        self.map_left = self.game_info.playable_area.x
        self.map_right = self.game_info.playable_area.width+self.game_info.playable_area.x
        self.map_bottom = self.game_info.playable_area.y
        self.map_top = self.game_info.playable_area.height+self.game_info.playable_area.y
        self.get_layout()
        self.write_layout(COMMANDCENTER,self.start_location.position)
#       make layout.txt for placer.py to compute placement tips
        layout_if.mapname = self.game_info.map_name
        layout_if.startx = self.start_location.position.x
        layout_if.starty = self.start_location.position.y
        layout_if.save_layout()
#       use stored placement tips
        mapplace = 'map: '+layout_if.mapname+' '+str(layout_if.startx)+' '+str(layout_if.starty)
        self.log_success(mapplace)
        pl = open('placement.txt','r')
        all_tips = pl.read().splitlines()
        pl.close()
        self.tips = []
        cop = False
        for nr in range(0,len(all_tips)):
            if all_tips[nr] == mapplace:
                cop = True
            elif all_tips[nr] == '#####':
                cop = False
            if cop:
                self.tips.append(all_tips[nr])
#       feedback the tips
        for nr in range(0,len(self.tips)):
            ti = self.tips[nr]
            print(ti)
#       name_of_scvt: fun translation of scvt to english boy name
        pl = open('names.txt','r')
        self.all_names = pl.read().splitlines()
        pl.close()


#   a lot of the strategy is in this maximumamount function
    def maxam(self,thing) -> int:
        bases = len(self.all_bases)
        battlecruisers = self.units(BATTLECRUISER).ready.amount
        onetwo = min(2,battlecruisers+1)
        if thing == ENGINEERINGBAY:
            return onetwo
        elif thing == BARRACKS:
            return onetwo
        elif thing == FACTORY:
            return onetwo
        elif thing == FUSIONCORE:
            return onetwo
        elif thing == ARMORY:
            return min(2,battlecruisers)
        elif thing == RAVEN:
            return min(1,battlecruisers-1)
        elif thing == VIKINGFIGHTER:
            return 1
        elif thing == REFINERY:
            return 2*bases
        elif thing == SUPPLYDEPOT:
            return battlecruisers+3*bases-1
        elif thing == MISSILETURRET:
            if self.supply_used < 190:
                return 3*bases-2
            else:
                return 5*bases
        elif thing == COMMANDCENTER:
            return 5+(self.minerals-500)//500
        elif thing == MARINE:
            return 10-battlecruisers
        elif thing == MARAUDER:
            return 5-battlecruisers
        elif thing == SIEGETANK:
            return (2*bases)//3
        elif thing == BATTLECRUISER:
            return 32
        elif thing == STARPORT:
            return bases
        elif thing == PLANETARYFORTRESS:
            return 10
        elif thing in (BARRACKSTECHLAB,FACTORYTECHLAB,STARPORTTECHLAB):
            return 10
        else:
#           e.g. upgrades
            return min(1,bases-3)


#   logging
    def log_fail(self,bol,stri):
        if not bol:
            print(f' On {self.itera} fail {self.routine} '+stri) 

    def log_success(self,stri):
        if self.do_log_success:
            print(f' On {self.itera} success {self.routine} '+stri) 

    def log_army(self,stri):
        if self.do_log_army:
            print(f' On {self.itera} army {self.routine} '+stri)

    async def log_attacktype(self,stri):
        if self.do_log_attacktype:
            print(f' On {self.itera} attacktype {self.routine} '+stri)
            await self._client.chat_send(stri, team_only=False) 

    def log_workers(self,stri):
        if self.do_log_workers:
            print(f' On {self.itera} workers {self.routine} '+stri) 

    def log_layout(self,stri):
        if self.do_log_layout:
            print(f' On {self.itera} layout {self.routine} '+stri) 

    def log_placing(self,stri):
        if self.do_log_placing:
            print(f' On {self.itera} placing {self.routine} '+stri) 

    def log_armysize(self):
        if self.do_log_armysize:
            stri = ''
            for ut in self.all_army:
                am = self.units(ut).amount
                if am>0:
                    stri = stri+'   '+ut.name+' '+str(am)
            print(f' On {self.itera} army'+stri)

    def name(self,scvt) -> str:
        if scvt in self.name_of_scvt:
            return self.name_of_scvt[scvt]
        else:
            return str(scvt)

    def log_gasminer(self):
        if self.do_log_gasminer:
            print(f' On {self.itera} gasminer: ')
            for scvt in self.all_scvt:
                if self.job_of_scvt[scvt] == 'gasminer':
                    print(str(scvt)+',')
            for gast in self.all_gast:
                print('gas '+str(gast)+': ')
                for scvt in self.gast_of_scvt: 
                    if self.gast_of_scvt[scvt] == gast:
                        print(str(scvt))
            for scvt in self.all_scvt:
                if self.job_of_scvt[scvt] == 'gasminer':
                    if scvt not in self.gast_of_scvt:
                        print('gasminer without assignment '+self.name(scvt)) 
            for scvt in self.gast_of_scvt:
                if scvt not in self.all_scvt:
                    print('assignment but not existing?! scv '+self.name(scvt))
                if scvt not in self.job_of_scvt:
                    print('assignment but scv without job?! '+self.name(scvt))
                if scvt in self.job_of_scvt:
                    job = self.job_of_scvt[scvt]
                    if job != 'gasminer':
                        print(job+' with gasminer assignment '+self.name(scvt))

    def log_population(self):
        if self.do_log_population:
            lin = ''
            for jo in self.count_of_job:
                co = self.count_of_job[jo]
                lin = lin + jo[0]+jo[1]+jo[2]+' '+str(co)+'   '
            print(f' On {self.itera} population: '+lin)

    def log_limbo(self,stri):
        if self.do_log_limbo:
            print(f' On {self.itera} limbo: '+stri) 

    def log_wish(self,stri):
        if self.do_log_wish:
            if stri != self.log_wish_history:
                self.log_wish_history = stri
                print(f' On {self.itera} wish: '+stri) 

    def log_resource(self):
        if self.do_log_resource:
            print(f' On {self.itera} minerals '+str(self.minerals)+'   gas '+str(self.vespene)\
            +'   reserved '+str(self.reserved_minerals)+'   reserved gas '+str(self.reserved_vespene))

    def log_workstock(self,stri): 
        if self.do_log_workstock:
            if stri != self.last_log_workstock_string:
                print(f' On {self.itera} workstock: '+stri)
                self.last_log_workstock_string = stri
 
    def log_time(self,stri):
        if self.do_log_time:
            print(f' On {self.itera} time: '+stri) 

    def put_on_the_grid(self,struc,place):
        if struc in self.all_structures_tobuildwalk:
            siz = self.size_of_structure[struc]
            if siz % 2 == 0:
                x = round(place.x)
                y = round(place.y)
            else:
                x = round(place.x-0.5)+0.5
                y = round(place.y-0.5)+0.5
        else:
           x = round(place.x*2)/2
           y = round(place.y*2)/2
        self.function_result_Point2 = Point2((x,y))

    def write_layout(self,struc,place):
        self.put_on_the_grid(struc,place)
        x = self.function_result_Point2.x
        y = self.function_result_Point2.y
        if struc in self.all_structures_tobuildwalk:
            self.log_layout('write position '+struc.name+' '+str(place.x)+' '+str(place.y))
            siz = self.size_of_structure[struc]
            for vakx in range(round(x-siz/2),round(x+siz/2)):
                for vaky in range(round(y-siz/2),round(y+siz/2)):
                    layout_if.layout[vakx][vaky] = 4
            if struc in (BARRACKS,FACTORY,STARPORT):
                x = x+2.5
                y = y-0.5
                siz = 2
                for vakx in range(round(x-siz/2),round(x+siz/2)):
                    for vaky in range(round(y-siz/2),round(y+siz/2)):
                        layout_if.layout[vakx][vaky] = 4

    def check_layout(self,struc,place) -> bool:
        placable = True
        self.put_on_the_grid(struc,place)
        x = self.function_result_Point2.x
        y = self.function_result_Point2.y
        if (struc in self.all_structures_tobuildwalk) and (struc != REFINERY):
            self.log_layout('check position '+struc.name+' '+str(place.x)+' '+str(place.y))
            siz = self.size_of_structure[struc]
            for vakx in range(round(x-siz/2),round(x+siz/2)):
                for vaky in range(round(y-siz/2),round(y+siz/2)):
                    placable = placable and (layout_if.layout[vakx][vaky] == 0)
            if struc in (BARRACKS,FACTORY,STARPORT):
                x = x+2.5
                y = y-0.5
                siz = 2
                for vakx in range(round(x-siz/2),round(x+siz/2)):
                    for vaky in range(round(y-siz/2),round(y+siz/2)):
                        placable = placable and (layout_if.layout[vakx][vaky] == 0)
        return placable


#   distance
    def sdist(self,p,q) -> int:
        return (p[0]-q[0])**2 + (p[1]-q[1])**2
 
    def dist(self,p,q) -> int:
#       for int points in 200*200
#       tolerate non-int but then less precise
        sd = (p[0]-q[0])**2 + (p[1]-q[1])**2
        return self.squareroot(round(sd))
 
    def near(self,p,q,supdist) -> bool:
        return (self.sdist(p,q) < supdist**2)

    def squareroot(self,x):
#       x should be int with 0<=x<200*200*2
#       fast, not exact, increasing continue, small
#       self.squareroot(600) = sqrt(600) - 0.35
        if len(self.stored_root) == 0:
            self.stored_root = [sqrt(h) for h in range(0,400)]
            self.hulp_root = [(self.stored_root[h+1]-self.stored_root[h])/400.0 for h in range(0,399)]
        if x < 400:
           return self.stored_root[x]
        else:
           return self.stored_root[x//400]*20.0 + (x%400)*self.hulp_root[x//400]        




#   techtree
    def init_structures(self,barra,buildtime, size):
        self.routine = 'init_structures'
        self.log_fail((type(barra) == UnitTypeId),'')
        self.all_structures.append(barra)
        self.buildtime_of_structure[barra] = buildtime
        self.size_of_structure[barra] = size
        if barra not in (BARRACKSTECHLAB,FACTORYTECHLAB,STARPORTTECHLAB,PLANETARYFORTRESS):
            self.all_structures_tobuildwalk.append(barra)

    def init_techtree(self,facto,barra):
        self.routine = 'tech'
        self.log_fail((type(facto) in [UpgradeId,UnitTypeId]),'first arg')
        self.log_fail((type(barra) in [UpgradeId,UnitTypeId]),'second arg')
        self.techtree.append( (facto,barra) )

    def init_cradle(self,mari,barra):
        self.routine = 'init_cradle'
        self.log_fail((type(mari) in [UpgradeId,UnitTypeId]),'first arg')
        self.log_fail(barra in self.all_structures,'second arg')
        self.cradle.append( (mari,barra) )
        self.techtree.append( (mari,barra) )

    def compute_anything(self):
        self.anything = []
        for pair in self.techtree:
            something = pair[0]
            if something not in self.anything:
                self.anything.append(something)
            something = pair[1]
            if something not in self.anything:
                self.anything.append(something)
        
    def check_techtree(self,facto) -> bool:
        cando = True
        for pair in self.techtree:
            if pair[0] == facto:
                cando = cando and self.we_have_a(pair[1])
        return cando

    def check_future_techtree(self,facto) -> bool:
        cando = True
        for pair in self.techtree:
            if pair[0] == facto:
                cando = cando and self.we_started_a(pair[1])
        return cando

    def we_have_a(self,barra) -> bool:
#       ignore flying buildings (good for the techtree but bad for producing army)
        if type(barra) == UpgradeId:
            have = (self.already_pending_upgrade(barra) > 0.99)
        if type(barra) == UnitTypeId:
#           a structure or a unit
            if barra in self.all_structures:
                have = (len(self.structures(barra).ready) > 0)
                if barra == REFINERY:
                    have = have or (len(self.structures(REFINERYRICH).ready) > 0)
                if barra == SUPPLYDEPOT:
                    have = have or (len(self.structures(SUPPLYDEPOTLOWERED).ready) > 0)
            else:
                have = (len(self.units(barra).ready) > 0)
        return have

    def we_started_a(self,barra) -> int:
        have = False
        if type(barra) == UpgradeId:
            have = (self.already_pending_upgrade(barra) > 0.01)
        if type(barra) == UnitTypeId:
#           a structure or a unit
            if barra in self.all_structures:
                have = (len(self.structures(barra)) > 0)
                if barra == REFINERY:
                    have = have or (len(self.structures(REFINERYRICH)) > 0)
                if barra == SUPPLYDEPOT:
                    have = have or (len(self.structures(SUPPLYDEPOTLOWERED)) > 0)
#               plans and building ones are included
                for scvt in self.structure_of_trabu_scvt:
                    have = have or (self.structure_of_trabu_scvt[scvt] == barra)
            else:
                have = (self.already_pending(barra) > 0.01) or (len(self.units(barra).ready) > 0)
        return have

    def we_have_amount(self,barra) -> int:
        have = 0
        if type(barra) == UpgradeId:
            if (self.already_pending_upgrade(barra) > 0.99):
                have = 1
        if type(barra) == UnitTypeId:
#           a structure or a unit
            if barra in self.all_structures:
                have = len(self.structures(barra).ready)
                if barra == REFINERY:
                    have = have + len(self.structures(REFINERYRICH).ready)
                if barra == SUPPLYDEPOT:
                    have = have + len(self.structures(SUPPLYDEPOTLOWERED).ready)
            else:
                have = len(self.units(barra).ready)
        return have


    def we_started_amount(self,barra) -> int:
        have = 0
        if type(barra) == UpgradeId:
            if (self.already_pending_upgrade(barra) > 0.01):
                have = 1
        if type(barra) == UnitTypeId:
#           a structure or a unit
            if barra in self.all_structures_tobuildwalk:
#               using a set to get rid of doubles
                positions = set()
                for bar in self.structures(barra):
                    positions.add(bar.position)
                if barra == REFINERY:
                    for bar in self.structures(REFINERYRICH):
                        positions.add(bar.position)
                if barra == SUPPLYDEPOT:
                    for bar in self.structures(SUPPLYDEPOTLOWERED):
                        positions.add(bar.position)
#               add plans and building ones
                for scvt in self.structure_of_trabu_scvt:
                    if self.structure_of_trabu_scvt[scvt] == barra:
                        positions.add(self.goal_of_trabu_scvt[scvt])
                have = len(positions)
            elif barra in self.all_structures:
#               using a set to get rid of doubles
                strtags = set()
                for bar in self.structures(barra):
                    strtags.add(bar.tag)
#               add plans and building ones
                for strt in self.ambition_of_strt:
                    ambition = self.ambition_of_strt[strt]
                    if ambition == barra:
                        strtags.add(strt)
                have = len(strtags)        
            else:
#               armyunit
                have = self.already_pending(barra)+self.units(barra).amount
                if barra == SIEGETANK:
                    have = have + self.units(SIEGETANKSIEGED).amount
        return have



#   money handling with reservations
    def can_pay(self,thing,urgent) -> bool:
        if urgent:
            cost = self.calculate_cost(thing)
            return (self.minerals >= cost.minerals) and (self.vespene >= cost.vespene)
        else:
            cost = self.calculate_cost(thing)
            return (self.minerals >= self.reserved_minerals+cost.minerals) and (self.vespene >= self.reserved_vespene+cost.vespene)

    def calc_reserved_money(self):
        self.reserved_minerals = 0
        self.reserved_vespene = 0
        for cct in self.ambition_of_strt:
            ambition = self.ambition_of_strt[cct]
            cost = self.calculate_cost(ambition)
            self.reserved_minerals = self.reserved_minerals + cost.minerals
            self.reserved_vespene = self.reserved_vespene + cost.vespene
        for scvt in self.all_scvt:
            if self.job_of_scvt[scvt] == 'traveller':
                building = self.structure_of_trabu_scvt[scvt]
                cost = self.calculate_cost(building)
                self.reserved_minerals = self.reserved_minerals + cost.minerals
                self.reserved_vespene = self.reserved_vespene + cost.vespene


    def bug_can_pay(self,upg,urgent) -> bool:
#       circumvent a bug
        cost_minerals = 999
        cost_vespene = 999
#       numbers correct jun 2020
        if upg == TERRANVEHICLEANDSHIPARMORSLEVEL1:
            cost_minerals = 100
            cost_vespene = 100
        if upg == TERRANVEHICLEANDSHIPARMORSLEVEL2:
            cost_minerals = 175
            cost_vespene = 175
        if upg == TERRANVEHICLEANDSHIPARMORSLEVEL3:
            cost_minerals = 250
            cost_vespene = 250
        if urgent:
            return (self.minerals >= cost_minerals) and (self.vespene >= cost_vespene)
        else:
            return (self.minerals >= self.reserved_minerals+cost_minerals) and (self.vespene >= self.reserved_vespene+cost_vespene)

    def get_layout(self):
        layout_if.layout = []
#       layout is in a col=right,row=up notation
        for col in range(0,200):
            collist = []
            for row in range(0,200):
                info = 0
                point = Point2((col,row))
#               point2 is a (x=right,y=up notation)
                if (col<self.map_right) and (col>=self.map_left) and (row<self.map_top) and (row>=self.map_bottom):
                    if self.game_info.pathing_grid[point] == 0:
                        info = info+1
                    if self.game_info.placement_grid[point] == 0:
                        info = info+2
                else:
                    info = 3
                collist.append(info)
            layout_if.layout.append(collist)
        for mim in self.mineral_field:
            here = mim.position
            layout_if.layout[round(here.x-1)][round(here.y-0.5)] = 1
            layout_if.layout[round(here.x+0)][round(here.y-0.5)] = 1


#   fix secondary information
#   call just before using count_of_job when precize numbers are important
    def fix_count_of_job(self):
#       count_of_job
        for j in self.all_job:
            self.count_of_job[j] = 0
        for scvt in self.job_of_scvt:
            j = self.job_of_scvt[scvt]
            self.count_of_job[j] = self.count_of_job[j]+1

    def fix_count_of_mimt(self):
#       calculate the amount of gatherers on each mineral, using mimt_of_scvt
        self.count_of_mimt = {}
        for mimt in self.all_mimt:
            self.count_of_mimt[mimt] = 0
        for scvt in self.mimt_of_scvt:
            mimt = self.mimt_of_scvt[scvt]
            if mimt in self.all_mimt:
                self.count_of_mimt[mimt] = self.count_of_mimt[mimt]+1

    def fix_count_of_gast(self):
#       calculate the amount of gatherers on each gas, using gast_of_scvt
        self.count_of_gast = {}
        for gast in self.all_gast:
            self.count_of_gast[gast] = 0
        for scvt in self.gast_of_scvt:
            gast = self.gast_of_scvt[scvt]
            if gast in self.all_gast:
                self.count_of_gast[gast] = self.count_of_gast[gast]+1


    def mimminer_vacatures(self) -> bool:
        return  len(self.all_mimt)*2 - len(self.mimt_of_scvt)

    def gasminer_vacatures(self) -> bool:
        return  len(self.all_gast)*3 - len(self.gast_of_scvt)



#   get nearest
    def get_near_scvt_to_goodjob(self,point) -> int:
        best_sdist = 80000
        best_scvt = None
        for scv in self.units(SCV):
            scvt = scv.tag
            if scvt in self.all_scvt:
                if self.job_of_scvt[scvt] not in ('builder','shiprepairer','traveller','arearepairer','escorter'):
                    sd = self.sdist(scv.position,point)
#                   accept idler if 1.7 times as far
                    if self.job_of_scvt[scvt] in ('idler','applicant'):
                        sd = sd/3
#                   accept mimminer if 1.4 times as far
                    if self.job_of_scvt[scvt] == 'mimminer':
                        sd = sd/2
                    if sd < best_sdist:
                        best_sdist = sd
                        best_scvt = scvt
        scvt = best_scvt
        self.log_fail((best_sdist < 80000),'no scv left for the good job')
        return scvt        

    def get_near_scvt_idler(self,point) -> int:
#       suggestion: call    if self.count_of_job['idler'] > 0;
        best_sdist = 80000
        best_scvt = None
        for scv in self.units(SCV):
            scvt = scv.tag
            if scvt in self.all_scvt:
                if self.job_of_scvt[scvt] == 'idler':
                    sd = self.sdist(scv.position,point)
                    if sd < best_sdist:
                        best_sdist = sd
                        best_scvt = scvt
        scvt = best_scvt
        self.log_fail((best_sdist < 80000),'no idler found.')
        return scvt        

    def get_near_gast_free(self,point) -> int:
#       supposes done:   fix_count_of_gast
#       suggestion: call   if self.gasminer_vacatures() > 0:
        best_sdist = 80000
        best_gast = None
        for gas in self.all_refineries:
            gast = gas.tag
            if gast in self.all_gast:
                if self.count_of_gast[gast] < 3:
                    sd = self.sdist(gas.position,point)
                    if sd < best_sdist:
                        best_sdist = sd
                        best_gast = gast
        gast = best_gast
        self.log_fail((best_sdist < 80000),'no workposition on gas found.')
        return gast        

    def get_near_mimt_free(self,point) -> int:
#       supposes done:   fix_count_of_mimt
#       suggestion: call   if self.mimminer_vacatures() > 0:
        best_sdist = 80000
        best_mimt = None
        for mim in self.mineral_field:
            mimt = mim.tag
            if mimt in self.all_mimt:
                if self.count_of_mimt[mimt] < 2:
                    sd = self.sdist(mim.position,point)
                    if sd < best_sdist:
                        best_sdist = sd
                        best_mimt = mimt
        mimt = best_mimt
        self.log_fail((best_sdist < 80000),'no workposition on minerals found.')
        return mimt        

    def get_near_cct_wanted(self,point) -> int:
        best_sdist = 80000
        best_cct = None
        for cc in self.all_bases:
            cct = cc.tag
            if self.wanted_of_cct[cct] > 0:
                sd = self.sdist(cc.position,point)
                if sd < best_sdist:
                    best_sdist = sd
                    best_cct = cct
        cct = best_cct
        self.log_fail((best_sdist < 80000),'no workposition found.')
        return cct        


#   timing routines

    def time_techtree(self,facto) -> float:
        waittime = 0
        for pair in self.techtree:
            if pair[0] == facto:
                barra = pair[1]
                if not self.we_have_a(barra):
                    barratime = self.buildtime_of_structure[barra]
                    shortest = barratime
                    for bar in self.structures(barra):
                        shortest = min(shortest,(1.0-bar.build_progress)*barratime)
                    if barra == REFINERY:
                        for bar in self.structures(REFINERYRICH):
                            shortest = min(shortest,(1.0-bar.build_progress)*barratime)
                    waittime = max(waittime,shortest)
        return waittime   

    def walk_now(self,building, goal) -> bool:
        logstr = building.name
        cost = self.calculate_cost(building)
#       gas_time
        gas_miners = 0
        for scvt in self.job_of_scvt:
            if self.job_of_scvt[scvt] == 'gasminer':
                gas_miners = gas_miners+1
        gas_gap = self.reserved_vespene + cost.vespene - self.vespene
        if (cost.vespene == 0) or (gas_gap <= 0):
            gas_time = 0
        elif gas_miners == 0:
            gas_time = 9999
        else: 
            gas_time = gas_gap / (gas_miners*self.gas_speed)
        logstr = logstr+' gas '+str(gas_time)
#       mim_time
        mim_miners = 0
        for scvt in self.job_of_scvt:
            if self.job_of_scvt[scvt] == 'mimminer':
                mim_miners = mim_miners+1
        mim_gap = self.reserved_minerals + cost.minerals - self.minerals
        if (mim_gap <= 0):
            mim_time = 0
        elif mim_miners == 0:
            mim_time = 9999
        else: 
            mim_time = mim_gap / (mim_miners*self.mim_speed)
        logstr = logstr+' mim '+str(mim_time)
#       resource_time
        resource_time = max(mim_time,gas_time)
#       techtree_time
        techtree_time = self.time_techtree(building)
        logstr = logstr+' tech '+str(techtree_time)
        other_time = max(resource_time,techtree_time)
#       walk_time
#       hope there is a usable scv
        scvt = self.get_near_scvt_to_goodjob(goal)
        for scv in self.units(SCV).ready:
            if scv.tag == scvt:
                walk_time = self.dist(scv.position,goal) / self.walk_speed
        logstr = logstr+' walk '+str(walk_time)
        self.log_time(logstr)
        return (walk_time > other_time)



    def check_maxam(self,thing) -> bool:
        amount = self.maxam(thing)
        have = self.we_started_amount(thing)
        todo = amount - have
        return (todo > 0)



    def check_cradle_idle(self,thing) -> bool:
#       for things without a cradle return True
#       the cradle should not be blocked by an ambition for things except enlargements
        allow = True
        for pair in self.cradle:
            if pair[0] == thing:
                cradle = pair[1]
                allow = False
                for stu in self.structures(cradle).ready:
                    if stu.tag in self.idle_structure_tags:
                        if (stu.tag not in self.ambition_of_strt) or (thing in self.all_structures):
                            allow = True
        return allow



    def find_building_a_place(self,building) -> bool:
        self.routine = 'find_building_a_place'
        self.log_placing(building.name)
#       get a random place
#       if no place could be found, return False
        found = False
        if building == COMMANDCENTER:
            tried = 0
            searc = True
            while searc and (tried<10):
                place = random.choice(self.expansion_locations_list)
                searc = False
                searc = searc or (not self.check_layout(building,place))
                searc = searc or (self.near(place,self.enemyloc,50))
                searc = searc or (place in [tow.position for tow in self.all_bases])
                searc = searc or (place in self.goal_of_trabu_scvt.values())
                tried = tried+1
            found = not searc
        elif building == REFINERY:
#           no check_layout for there is a geyser
#           but please prevent doubles in workstock
            places = []
            for gey in self.vespene_geyser:
                free = True
                for gb in self.gas_buildings:
                    free = free and not self.near(gb.position,gey.position,2)
#                   free = free and (gb.position != gey.position)
                if free:
                    for cc in self.all_bases:
                        if self.near(gey.position,cc.position,12):
                            if gey.position not in self.goal_of_trabu_scvt.values():
                                if gey.position not in self.place_of_workstock.values():
                                    places.append(gey.position)
            if len(places) > 0:
                place = random.choice(places)
                found = True
        elif building in self.all_structures_tobuildwalk:
#           normal building
            if len(self.all_bases) > 0:
                found = False
                while not found:
                    cc = random.choice(self.all_bases)
                    dist = 12
                    if building == STARPORT:
                        dist = 6
                    if building == MISSILETURRET:
                        dist = random.randrange(-10,10) 
                    fixplace = cc.position.towards(self.game_info.map_center, dist)
                    self.put_on_the_grid(building,fixplace)
                    fixplace = self.function_result_Point2
                    place = fixplace
                    while not self.check_layout(building,place):
                        x = fixplace.x+random.randrange(-15,15)
                        y = fixplace.y+random.randrange(-15,15)
                        place = Point2((x,y))
                    found = True 
            else:
                fixplace = self.start_location.position
                self.put_on_the_grid(building,fixplace)
                fixplace = self.function_result_Point2
                place = fixplace
                while not self.check_layout(building,place):
                    x = fixplace.x+random.randrange(-15,15)
                    y = fixplace.y+random.randrange(-15,15)
                    place = Point2((x,y))
                found = True 
        else:
#           techlab, pf
            for pair in self.cradle:
                if pair[0] == building:
                    oldbuilding = pair[1]
                    for stu in self.structures(oldbuilding).ready:
#                       does not have to be idle yet
                        if stu.tag not in self.ambition_of_strt:
                            if not stu.has_add_on:
                                if stu.position not in self.add_on_denied:
                                    place = stu.position
                                    found = True
#       get place from * tips
        tipsfound = 0
        for nr in range(0,len(self.tips)):
            if (nr not in self.tips_used):
                ti = self.tips[nr]
                woord = ti.split()
                if (woord[0] == 'position') and (woord[2] == '*'):
                    if woord[1] == building.name:
                        maybe_place = Point2((float(woord[3]),float(woord[4])))
                        if self.check_layout(building,maybe_place):
                            tipsfound = tipsfound+1
                            if random.randrange(0,tipsfound) == 0:
                                place = maybe_place 
                                maybe_nr = nr
        if tipsfound>0: 
            found = True
            self.tips_used.append(maybe_nr)
#       get place from hard tips
        tipsfound = False
        for nr in range(0,len(self.tips)):
            if (nr not in self.tips_used):
                ti = self.tips[nr]
                woord = ti.split()
                if (woord[0] == 'position') and (woord[2] != '*'):
                    if woord[1] == building.name:
#                       in this case, layout is NOT checked
                        if not tipsfound:
                            tipsfound = True
                            place = Point2((float(woord[2]),float(woord[3]))) 
                            self.tips_used.append(nr)
                            self.log_success('using a hard placement tip')
                            found = True
#       
        if found:
            self.function_result_Point2 = place
        else:
            self.log_placing('not found')
        return found 



    def add_to_workstock(self,thing):
        if len(self.thing_of_workstock) < self.stocksize:
            workstock = 0
            while workstock in self.thing_of_workstock:
                workstock = workstock+1
            if thing in self.all_structures:
                if self.find_building_a_place(thing):
#                   now already should it be put in layout, otherwise plans could clash
                    goal = self.function_result_Point2
                    self.write_layout(thing,goal)
                    if self.do_log_layout:
                        layout_if.photo_layout()
                    self.thing_of_workstock[workstock] = thing
                    self.place_of_workstock[workstock] = goal
            else:
                self.thing_of_workstock[workstock] = thing
                self.place_of_workstock[workstock] = self.nowhere


    def blunt_to_workstock(self,thing):
        if thing not in self.thing_of_workstock.values():
            if self.check_techtree(thing):
               if self.check_maxam(thing):
                   if self.check_cradle_idle(thing):
                       self.add_to_workstock(thing)

    def fill_workstock(self):
        if self.rushing:
#           make in_stock, the indices in wish_now of the things in thing_of_workstock
#           make also_in_stock, the indices in also_wish_now of the things in thing_of_workstock
#           make to_cancel, workstocks that are neither in wish_now nor in also_wish_now 
            in_stock = []
            also_in_stock = []
            to_cancel = []
            for workstock in self.thing_of_workstock:
                orderedthing = self.thing_of_workstock[workstock]
                found_somewhere = False
                searc = True
                ri = 0
                while (ri<len(self.also_wish_now)) and searc:
                    thing = self.also_wish_now[ri]
                    if thing == orderedthing:
                        searc = False
                        found_somewhere = True
                        also_in_stock.append(ri)
                    ri=ri+1
                searc = True
                ri = 0
                while (ri<len(self.wish_now)) and searc:
                    thing = self.wish_now[ri]
                    if thing == orderedthing:
                        searc = False
                        found_somewhere = True
                        in_stock.append(ri)
                    ri=ri+1
                if not found_somewhere:
                    to_cancel.append(workstock)
                    self.log_workstock('cancelled '+orderedthing.name)
#           effect cancellations
            for workstock in to_cancel:
                del self.thing_of_workstock[workstock]
                del self.place_of_workstock[workstock]
#           now add the first things from also_wish_now to workstock
            ri = 0
            while (ri<len(self.also_wish_now)):
                if ri not in also_in_stock:
                    thing = self.also_wish_now[ri]
                    if self.check_future_techtree(thing):
                        if self.check_cradle_idle(thing):
                            self.add_to_workstock(thing)
#                           and add the thing to in_stock at the same time                  
                            searc = True
                            ra = 0
                            while (ra<len(self.wish_now)) and searc:
                               if ra not in in_stock:
                                   otherthing = self.wish_now[ra]
                                   if thing == otherthing:
                                       searc = False
                                       in_stock.append(ra)
                               ra=ra+1
                ri=ri+1
#           now add the first things from wish_now to workstock                  
            ri = 0
            while (ri<len(self.wish_now)):
                if ri not in in_stock:
                    thing = self.wish_now[ri]
                    if self.check_future_techtree(thing):
                        if self.check_cradle_idle(thing):
                            self.add_to_workstock(thing)
                ri=ri+1
        else:
#           advice on midgame stuck situations
            scvs = len(self.units(SCV))
            if (self.supply_left < 2+self.supply_used//6) and (self.supply_cap<200):
                if (SUPPLYDEPOT not in self.structure_of_trabu_scvt.values()) or (self.supply_left<2):
                    self.blunt_to_workstock(SUPPLYDEPOT)
            wanted_ccs = 1+(scvs+7)//22
            if (self.we_started_amount(COMMANDCENTER)+self.structures(PLANETARYFORTRESS).amount\
            +self.structures(ORBITALCOMMAND).amount < wanted_ccs):
                self.blunt_to_workstock(COMMANDCENTER)
            if (self.we_started_amount(SIEGETANK)<3) and (self.supply_used<120):
                self.blunt_to_workstock(SIEGETANK)
            if (not self.we_started_a(MISSILETURRET)) or (self.supply_used>100):
                self.blunt_to_workstock(MISSILETURRET)
            if (not self.we_started_a(ENGINEERINGBAY)) and (self.supply_used>40):
                self.blunt_to_workstock(ENGINEERINGBAY)
            if (self.supply_army*3 < self.supply_used):
                self.blunt_to_workstock(MARINE)
            if (self.minerals-self.reserved_minerals > 1500):
                self.blunt_to_workstock(PLANETARYFORTRESS)
                self.blunt_to_workstock(COMMANDCENTER)
                self.blunt_to_workstock(MISSILETURRET)
                self.blunt_to_workstock(STARPORT)
            if (self.minerals > 500) and (self.vespene < self.minerals-500):
                self.blunt_to_workstock(REFINERY)
            if (len(self.structures(STARPORT).ready.idle)>0):
                self.blunt_to_workstock(BATTLECRUISER)
            for sp in self.structures(STARPORT).ready:
                if not sp.has_add_on:
                    self.blunt_to_workstock(STARPORTTECHLAB)
            if not self.we_started_a(FACTORYTECHLAB):
                for sp in self.structures(FACTORY).ready:
                    if not sp.has_add_on:
                        self.blunt_to_workstock(FACTORYTECHLAB)
            if (len(self.structures(FUSIONCORE))==0):
                self.blunt_to_workstock(FUSIONCORE)
            if (len(self.structures(STARPORT))==0):
                self.blunt_to_workstock(STARPORT)
            if (len(self.structures(FACTORY))==0):
                self.blunt_to_workstock(FACTORY)
            if (len(self.structures(BARRACKS))==0):
                self.blunt_to_workstock(BARRACKS)
            if (len(self.structures(SUPPLYDEPOT))==0):
                self.blunt_to_workstock(SUPPLYDEPOT)
            if (len(self.structures(STARPORT).ready.idle)==0) and (len(self.structures(FUSIONCORE).ready)>0) \
            and (STARPORT not in self.structure_of_trabu_scvt.values()):
                self.blunt_to_workstock(STARPORT)
            if (self.we_started_amount(BATTLECRUISER) >= 3):
                self.blunt_to_workstock(ARMORY)
                self.blunt_to_workstock(RAVEN)
                self.blunt_to_workstock(BATTLECRUISERENABLESPECIALIZATIONS)
            if (len(self.structures(ARMORY).ready.idle) > 0):
                for pair in self.cradle:
                    if pair[1] == ARMORY:
                        self.blunt_to_workstock(pair[0])
        stri = ''
        for workstock in self.thing_of_workstock:
            thing = self.thing_of_workstock[workstock]
            stri = stri+' '+thing.name
        self.log_workstock(stri)


 
#   async routines


    async def gamestate(self):
        self.routine = 'gamestate'
#       
#   All existing refineries
        self.all_refineries = (self.structures(REFINERY).ready+self.structures(REFINERYRICH).ready)
#   
#   All existing not-flying ready commandcenters and orbitalcommands and all planetary fortresses
#       pf and oc morphing from cc are included
#       the pluscharacter appends lists
        self.all_bases = self.structures(COMMANDCENTER).ready+self.structures(ORBITALCOMMAND)+self.structures(PLANETARYFORTRESS)
#       ccs in construction nearly finished are included
        for cc in self.structures(COMMANDCENTER):
            if cc.build_progress>0.85:
                if cc not in self.all_bases:
                    self.all_bases.append(cc)
                
#
#   All idle structures
        self.idle_structure_tags = []
        for kind in self.all_structures:
            for one in self.structures(kind).ready.idle:
                self.idle_structure_tags.append(one.tag)
#
#   in the jump lost battlecruisers
#       uses old bct_in_repair info!
        count = 0
        for bc in self.units(BATTLECRUISER).ready:
            if (bc.tag in self.bct_in_repair):
                count = count+1
        if len(self.bct_in_repair) > count:
            self.bc_fear = min(500,self.bc_fear+40)
#       
#   bct_in_repair contains tags of living, unhealthy battlecruisers
        new_bct_in_repair = []
        for bc in self.units(BATTLECRUISER).ready:
            if (bc.tag in self.bct_in_repair) and (bc.health<525):
                new_bct_in_repair.append(bc.tag)
        self.bct_in_repair = new_bct_in_repair
#       
#   bestbctag is -1 or a tag of a living battlecruiser
        just_one_bctag = -1
        seen = False
        for bc in self.units(BATTLECRUISER).ready:
            just_one_bctag = bc.tag
            seen = seen or (bc.tag == self.bestbctag)
        if not seen:
            self.bestbctag = just_one_bctag
#       
#   ambition_of_strt contains tags of living commandcenters, barracks etc
        new_ambition_of_strt = {}
        for cc in self.structures.ready:
            if cc.tag in self.ambition_of_strt:
                new_ambition_of_strt[cc.tag] = self.ambition_of_strt[cc.tag]
        self.ambition_of_strt = new_ambition_of_strt
#       
#   rushing depends on endwish_am_of_th
#       only once per game toggle to True
        if self.rushing:
            rr = True
            for thing in self.enddemand_am_of_th:
                rr = rr and (self.we_started_amount(thing) >= self.enddemand_am_of_th[thing])
            if rr: 
                self.rushing = False
                self.log_success('rush reached!')
#   
#   wish_now is the reachable part of wish_am_of_th
#           this list contains doubles, and the first elements are most important
            self.wish_now = []
            lin = ''
            looppri = 10
            while looppri >= 0:
                for thing in self.wish_am_of_th:
                    am = self.wish_am_of_th[thing]
                    if self.wish_pri_of_th[thing] == looppri:
                        if self.check_future_techtree(thing):
#                           how many of those "thing" have been started or reserved?
                            have = self.we_started_amount(thing)
                            while have < am:
                                have = have+1
                                self.wish_now.append(thing)
                                lin = lin+' '+thing.name
                looppri = looppri - 1
            if len(self.wish_now)>0:
                self.log_wish(lin)
#   also_wish_now contains a supplydepot if supplyblock is near
            self.also_wish_now = []
            if (self.supply_left < 12) and (self.supply_cap<200):
                if SUPPLYDEPOT not in self.structure_of_trabu_scvt.values():
                        self.also_wish_now.append(SUPPLYDEPOT)
#           
#   Count battlecruisers
        self.lastcruisercount = self.cruisercount
        self.cruisercount = self.units(BATTLECRUISER).ready.amount
#   
#   scv 
#   The tag of existing own scvs, in this iteration
#       complication is the scv in a refinery, which does not exist temporarily
        limbo = self.supply_workers - self.units(SCV).amount
        if limbo == 0:
            self.all_scvt = [scv.tag for scv in self.units(SCV)]
            self.itera_of_missing_scvt = {}
        else:
            new_all_scvt = [scv.tag for scv in self.units(SCV)]
            for scvt in self.all_scvt:
                job = self.job_of_scvt[scvt]
                if (job == 'gasminer'):
                    if scvt not in new_all_scvt:
#                       self.log_limbo('a '+job+' in limbo '+self.name(scvt))
                        new_all_scvt.append(scvt)
                        if scvt in self.itera_of_missing_scvt:
                            time_lost = self.itera - self.itera_of_missing_scvt[scvt]
                        else:
                            time_lost = 0
                            self.itera_of_missing_scvt[scvt] = self.itera
                        if time_lost < 20:
                            new_all_scvt.append(scvt)
                        else:
                            self.log_limbo('give up hope '+self.name(scvt))
                if (job == 'builder'):
                    if (self.structure_of_trabu_scvt[scvt] in (REFINERY,REFINERYRICH)):
                        if scvt not in new_all_scvt:
#                           self.log_limbo('a '+job+' in limbo '+self.name(scvt))
                            new_all_scvt.append(scvt)
                            if scvt in self.itera_of_missing_scvt:
                                time_lost = self.itera - self.itera_of_missing_scvt[scvt]
                            else:
                                time_lost = 0
                                self.itera_of_missing_scvt[scvt] = self.itera
                            if time_lost < 20:
                                new_all_scvt.append(scvt)
                            else:
                                self.log_limbo('give up hope '+self.name(scvt))
#           Take seen scvs from the missing-list
#           Take old cases from the missing-list
            new_itera_of_missing_scvt = {}
            for scvt in self.itera_of_missing_scvt:
                if scvt not in [scv.tag for scv in self.units(SCV)]:
                    if self.itera_of_missing_scvt[scvt] >= self.itera - 20:
                        new_itera_of_missing_scvt[scvt] = self.itera_of_missing_scvt[scvt]
            self.itera_of_missing_scvt = new_itera_of_missing_scvt
#           
            self.log_limbo(str(limbo)+' scvs missing in gas, or killed. Remembering '+str(len(self.itera_of_missing_scvt)))
            self.all_scvt = new_all_scvt
#           
#   Name the scvs
        
        for scvt in self.all_scvt:
            if scvt not in self.name_of_scvt:
                if len(self.name_of_scvt) < len(self.all_names):
                    free_names = set(self.all_names) - set(self.name_of_scvt.values())
                    self.name_of_scvt[scvt] = random.choice(tuple(free_names))
                    self.log_workers('we have a new scv: '+self.name_of_scvt[scvt])
#           
#   The tag of existing refineries where we want to mine from, in this iteration
        self.all_gast = []
        for gas in self.all_refineries:
            gast = gas.tag
            if gas.vespene_contents > 0:
                for tow in self.all_bases:
                    towt = tow.tag
                    if self.near(gas.position,tow.position,10):
                        self.all_gast.append(gast)
#   The tag of existing minerals where we want to mine from, in this iteration
        self.all_mimt = []
        for mim in self.mineral_field:
            mimt = mim.tag
            if mim.mineral_contents > 0:
                for tow in self.all_bases:
                    towt = tow.tag
                    if self.near(mim.position,tow.position,10):
                        self.all_mimt.append(mimt) 
#   job_of_scvt contains the tag of all living scvs
        new_job_of_scvt = {}
        for scvt in self.all_scvt:
            if scvt in self.job_of_scvt:
                new_job_of_scvt[scvt] = self.job_of_scvt[scvt]
            else:
                new_job_of_scvt[scvt] = 'idler'
        self.job_of_scvt = new_job_of_scvt
#   count_of_job
        self.fix_count_of_job()
        self.log_population()
#   restrict mimt_of_scvt to existing worker and mineral
        new_mimt_of_scvt = {}
        for scvt in self.mimt_of_scvt:
            if scvt in self.all_scvt:
                mimt = self.mimt_of_scvt[scvt]
                if mimt in self.all_mimt:
                    new_mimt_of_scvt[scvt] = mimt
        self.mimt_of_scvt = new_mimt_of_scvt
        self.fix_count_of_mimt()
#   restrict gast_of_scvt to existing worker and mineral
        new_gast_of_scvt = {}
        for scvt in self.gast_of_scvt:
            if scvt in self.all_scvt:
                gast = self.gast_of_scvt[scvt]
                if gast in self.all_gast:
                    new_gast_of_scvt[scvt] = gast
        self.gast_of_scvt = new_gast_of_scvt
        self.fix_count_of_gast()
#   cottage_of_scvt contains the tag of living arearepairers
        new_cottage_of_scvt = {}
        for scvt in self.all_scvt:
            if self.job_of_scvt[scvt] == 'arearepairer':
                new_cottage_of_scvt[scvt] = self.cottage_of_scvt[scvt]
        self.cottage_of_scvt = new_cottage_of_scvt
#   vision_of_scvt contains the tag of living applicants and existing bases
        new_vision_of_scvt = {}
        for scvt in self.all_scvt:
            if self.job_of_scvt[scvt] == 'applicant':
                cct = self.vision_of_scvt[scvt]
                if cct in [cc.tag for cc in self.all_bases]:
                    new_vision_of_scvt[scvt] = cct
        self.vision_of_scvt = new_vision_of_scvt
#   goal_of_trabu_scvt contains the tag of living traveller or builder scvs
        new_goal_of_trabu_scvt = {}
        for scvt in self.all_scvt:
            if self.job_of_scvt[scvt] in ('traveller','builder'):
                new_goal_of_trabu_scvt[scvt] = self.goal_of_trabu_scvt[scvt]
        self.goal_of_trabu_scvt = new_goal_of_trabu_scvt
#   structure_of_trabu_scvt contains the tag of living builders and travellers
        new_structure_of_trabu_scvt = {}
        for scvt in self.all_scvt:
            if self.job_of_scvt[scvt] in ('traveller','builder'):
                new_structure_of_trabu_scvt[scvt] = self.structure_of_trabu_scvt[scvt]
        self.structure_of_trabu_scvt = new_structure_of_trabu_scvt
#           
#   if a traveller died, or a cc is lost that had ambition_to_pf, the cost should be taken off reserved
        self.calc_reserved_money()
#           



    async def build_worker(self,amount):
        self.routine = 'build_worker'
        todo = amount - (self.units(SCV).amount + self.already_pending(SCV))
        todo = min(todo,self.supply_left)
        if self.count_of_job['idler'] < 11:
            for cc in self.all_bases:
                if cc.tag in self.idle_structure_tags:
                    if cc.tag not in self.ambition_of_strt:
#                       always urgent
                        if self.can_pay(SCV,True):
                            if todo > 0:
                                todo = todo-1
                                self.log_workers('')
                                cc.train(SCV)
                                self.idle_structure_tags.remove(cc.tag)


    async def use_workstock(self):
#       if any is applicable now, do it.
        workdone = []
        for workstock in self.thing_of_workstock:
            thing = self.thing_of_workstock[workstock]
            place = self.place_of_workstock[workstock]
            if await self.build_thing(thing, place):
                workdone.append(workstock)
        for workstock in workdone:
            del self.thing_of_workstock[workstock]                
            del self.place_of_workstock[workstock]                



#   Build specific unit or structure
    async def build_thing(self,thing,place) -> bool:
#       print('DEBUG trying to build '+thing.name)
        self.routine = 'build_thing'
        if thing == COMMANDCENTER:
            didit = await self.build_commandcenter(place)
        elif thing in self.all_structures_tobuildwalk:
            didit = await self.build_building(thing,place) 
        elif thing in self.all_structures:
            didit = await self.enlarge_building(thing,place)
        elif type(thing) == UpgradeId:
            didit = await self.do_upgrade(thing)
        else:
            didit = await self.build_army(thing)
        return didit



    async def build_army(self,ship) -> bool:
        self.routine = 'build_army'
        didit = False
        if self.check_maxam(ship):
            if self.check_techtree(ship):
                if self.can_pay(ship,False):
                    if self.supply_left >= 6:
                        for pair in self.cradle:
                            if pair[0] == ship:
                                hangar = pair[1]
                                todo = 1                    
                                for sp in self.structures(hangar).ready:
                                    if sp.tag in self.idle_structure_tags:
                                        if (sp.has_add_on) or (ship == MARINE):
                                            if sp.tag not in self.ambition_of_strt:
                                                if todo>0:
                                                    todo = todo-1
                                                    self.log_success(ship.name)
                                                    sp.train(ship)
                                                    self.idle_structure_tags.remove(sp.tag)
                                                    didit = True
        return didit



    async def start_construction(self):
        self.routine = 'start_construction'
        for scvt in self.goal_of_trabu_scvt:
            if self.job_of_scvt[scvt] == 'traveller':
                goal = self.goal_of_trabu_scvt[scvt]
                building = self.structure_of_trabu_scvt[scvt] 
                if self.check_techtree(building):
                    if self.can_pay(building,True):
                        for scv in self.units(SCV):
                            if scv.tag == scvt:
                                if self.near(scv.position,goal,3):
                                    self.job_of_scvt[scvt] = 'builder'
                                    self.promotionsite_of_scvt[scvt] = scv.position
                                    self.log_workers('traveller became builder '+self.name(scvt))
                                    self.calc_reserved_money()
                                    self.log_workers('beginning '+building.name+' '+self.name(scvt))
                                    if building == REFINERY:
                                       for gey in self.vespene_geyser:
                                           if gey.position == goal:
                                               if scv.build_gas(gey):
                                                   self.log_workers('begun     '+building.name+' '+self.name(scvt))
                                    else:
                                        if scv.build(building, goal):
                                            self.log_workers('begun     '+building.name+' '+self.name(scvt))
#       also, realize an ambition
        todo = 1
        for oldbuilding in self.structures.ready:
             if oldbuilding.tag in self.idle_structure_tags:
                if oldbuilding.tag in self.ambition_of_strt: 
                    newbuilding = self.ambition_of_strt[oldbuilding.tag]
                    if self.check_techtree(newbuilding):
                        if self.can_pay(newbuilding,True):
                            if todo > 0:
                                todo = todo-1
                                del self.ambition_of_strt[oldbuilding.tag]
                                self.log_success(newbuilding.name)
                                oldbuilding.train(newbuilding)
                                self.calc_reserved_money()
                                self.idle_structure_tags.remove(oldbuilding.tag)



    async def build_building(self,building,goal) -> bool:
        self.routine = 'build_building'
#       for tobuildwalk buildings except COMMANDCENTER
        didit = False
        if self.check_maxam(building):
#           you do not have to wait for minerals and techtree
            if self.check_future_techtree(building):
                if self.walk_now(building,goal):
                    scvt = self.get_near_scvt_to_goodjob(goal)
                    for scv in self.units(SCV):
                        if scv.tag == scvt:
                            self.goal_of_trabu_scvt[scvt] = goal
                            self.structure_of_trabu_scvt[scvt] = building
#                           best to stop the scv from mining, for if the build does not start, it remains in old function
                            if scv.is_collecting:
                                scv(STOP)
                            self.job_of_scvt[scvt] = 'traveller'
                            self.promotionsite_of_scvt[scvt] = scv.position
                            self.log_workers('planning  '+building.name+' '+self.name(scvt))
                            if scv(MOVE_MOVE,goal):
                                self.log_workers('ordered   '+building.name+' '+self.name(scvt))
                            self.calc_reserved_money()
                            didit = True
        return didit



    async def build_commandcenter(self,goal) -> bool:
        self.routine = 'build_commandcenter'
        didit = False
        building = COMMANDCENTER
        if self.check_maxam(building):
#           you do not have to wait for minerals and techtree
            if self.walk_now(building,goal):
                scvt = self.get_near_scvt_to_goodjob(goal)
                for scv in self.units(SCV):
                    if scv.tag == scvt:
                        job = self.job_of_scvt[scvt]
                        self.job_of_scvt[scvt] = 'escorter'
                        self.promotionsite_of_scvt[scvt] = scv.position
                        self.log_workers(job+' became escorter '+self.name(scvt))
                        scv.attack(goal)
                if len(self.units(MARINE).ready) > 0:
                    mar = random.choice(self.units(MARINE).ready)
                    mar.attack(goal)
                if len(self.units(MARAUDER).ready) > 0:
                    mar = random.choice(self.units(MARAUDER).ready)
                    mar.attack(goal)
                scvt = self.get_near_scvt_to_goodjob(goal)
                for scv in self.units(SCV):
                    if scv.tag == scvt:
                        self.goal_of_trabu_scvt[scvt] = goal
                        self.structure_of_trabu_scvt[scvt] = building
                        job = self.job_of_scvt[scvt]
                        self.job_of_scvt[scvt] = 'traveller'
                        self.promotionsite_of_scvt[scvt] = scv.position
                        self.log_workers(job+' became traveller '+self.name(scvt))
                        scv(MOVE_MOVE, goal)
                        self.calc_reserved_money()
                didit = True
        return didit



    async def enlarge_building(self,ambition,place) -> bool:
#       puts a building in ambition_of_strt, then it will become idle, then be transformed
        self.routine = 'enlarge_building'
        didit = False
        if self.check_techtree(ambition):
            if self.can_pay(ambition,False):
                for cc in self.structures.ready:
                    if cc.position == place:
                        if cc.tag not in self.ambition_of_strt: 
                            self.ambition_of_strt[cc.tag] = ambition
                            self.calc_reserved_money()
                            didit = True
        return didit

    def good_army_position(self,point) -> bool:
        good = False
        if self.attack_type == 'center':
            good = self.near(point,self.army_center_point,10)
        elif self.attack_type == 'arc':
            good = self.near(point,self.enemyloc,100) and (not self.near(point,self.enemyloc,80))
        elif self.attack_type == 'agressive':
            good = self.near(point,self.enemyloc,15)
        return good

    async def attack(self):
        self.routine = 'attack'
        if self.attack_type == 'agressive':
            for bc in self.units(BATTLECRUISER).ready:
                if self.good_army_position(bc.position):
                    if bc.tag not in self.frozenbctags:
                        self.log_army('holding bc there')
                        bc(HOLDPOSITION_BATTLECRUISER)
                        self.frozenbctags.add(bc.tag)
            for bc in self.units(BATTLECRUISER).ready.idle:
                if not self.good_army_position(bc.position):
                    place = Point2((random.randrange(self.map_left,self.map_right),random.randrange(self.map_bottom,self.map_top)))
                    while not self.good_army_position(place):
                        place = Point2((random.randrange(self.map_left,self.map_right),random.randrange(self.map_bottom,self.map_top)))
                    abilities = (await self.get_available_abilities([bc]))[0]
                    if EFFECT_TACTICALJUMP in abilities:
                        bc(EFFECT_TACTICALJUMP,place)
                        self.log_army('jumping in a bc')
                    else:
                        bc.attack(place)
                        self.log_army('attacking with a bc')
            tp = self.enemyloc
        elif self.attack_type == 'chaos':
            tp = Point2((random.randrange(self.map_left,self.map_right),random.randrange(self.map_bottom,self.map_top)))
        elif self.attack_type == 'arc':
            tp = Point2((random.randrange(self.map_left,self.map_right),random.randrange(self.map_bottom,self.map_top)))
            while not self.good_army_position(tp):
                tp = Point2((random.randrange(self.map_left,self.map_right),random.randrange(self.map_bottom,self.map_top)))
        elif self.attack_type == 'arcpoint':
            tp = self.enemyloc
        elif self.attack_type == 'center':
            tp = self.army_center_point
        elif self.attack_type == 'centerpoint':
            tp = self.enemyloc
        sent = 0
        for srt in [BATTLECRUISER,MARINE,MARAUDER,VIKINGFIGHTER]:
            if (self.attack_type != 'agressive') or (srt != BATTLECRUISER):
                if (self.attack_type == 'chaos') and (srt == BATTLECRUISER) and (self.never_had_a_bc):
                    pass
                else:
                    for ar in self.units(srt).ready.idle:
                        if not (ar.tag in self.bct_in_repair):
                            if not self.good_army_position(ar.position):
                                sent = sent + 1
                                ar.attack(tp)
        if sent > 0:
            self.log_army(' with '+str(sent))
#       
#       attack_type changes
        if self.attack_type == 'agressive':
            if (self.cruisercount<self.lastcruisercount) or (len(self.frozenbctags) >= 3):
                self.attack_type = 'chaos'
                self.log_army('spreading the army')
                await self.log_attacktype('spreading the army')
#               unfreeze
                for bc in self.units(BATTLECRUISER).ready:
                    if bc.tag in self.frozenbctags:
                        bc(STOP)
                self.frozenbctags = set()
        elif self.attack_type == 'chaos':
            if self.supply_used > 190:
                self.attack_type = 'arc'
                self.log_army('arcing the army for a point attack')
                await self.log_attacktype('arcing the army for a point attack')
            if (self.cruisercount == 1) and (self.never_had_a_bc):
                self.never_had_a_bc = False
                self.attack_type = 'agressive'
                self.log_army('first bc, turning agressive.') 
                await self.log_attacktype('first bc, turning agressive.') 
        elif self.attack_type == 'arc':
            reached = 0
            total = 0
            for srt in [BATTLECRUISER,MARINE,MARAUDER,VIKINGFIGHTER]:
                for ar in self.units(srt).ready:
                    total = total+1
                    if self.good_army_position(ar.position):
                        if ar in self.units(srt).ready.idle:
                            reached = reached+1
            if reached*5 > total*4:
                self.attack_type = 'arcpoint'
                self.log_army('starting a arcpoint attack')
                await self.log_attacktype('starting a arcpoint attack')
        elif self.attack_type == 'arcpoint':
            self.attack_type = 'center'
            tp = Point2((random.randrange(self.map_left,self.map_right),random.randrange(self.map_bottom,self.map_top)))
            while self.near(tp,self.enemyloc,80) or (not self.near(tp,self.enemyloc,100)): 
                tp = Point2((random.randrange(self.map_left,self.map_right),random.randrange(self.map_bottom,self.map_top)))
            self.army_center_point = tp    
        elif self.attack_type == 'center':
            reached = 0
            total = 0
            for srt in [BATTLECRUISER,MARINE,MARAUDER,VIKINGFIGHTER]:
                for ar in self.units(srt).ready:
                    total = total+1
                    if self.good_army_position(ar.position):
                        if ar in self.units(srt).ready.idle:
                            reached = reached+1
            if reached*5 > total*4:
                self.attack_type = 'centerpoint'
                self.log_army('starting a center-to-point attack')
                await self.log_attacktype('starting a center-to-point attack')
        elif self.attack_type == 'centerpoint':
            self.attack_type = 'agressive'
            self.log_army('feeling agressive')
            await self.log_attacktype('feeling agressive')
#       
#       ravens should attack the best battlecruiser
        for rv in self.units(RAVEN).ready.idle:
            for bc in self.units(BATTLECRUISER).ready:
                if bc.tag == self.bestbctag:
                    rv.attack(bc)
                    self.log_army('raven will follow a bc')
#       suicider scvs
        if self.count_of_job['suicider'] > 0:
            for scv in self.units(SCV).idle:
                scvt = scv.tag
                if scvt in self.all_scvt:
                    if self.job_of_scvt[scvt] == 'suicider':
                        place = self.mineral_field.random.position
                        scv.attack(place)



    async def lift(self):
#       attacked buildings can fly, survive, be repaired, and land back.
        self.routine = 'lift'
        for srt in self.landable:
            for bu in self.structures(srt).ready:
                if bu.health >= bu.health_max-100:
                    self.log_success('down '+srt.name)
                    bu(LAND,self.home_of_flying_struct[bu.tag])
        for srt in self.liftable:
            for bu in self.structures(srt).ready:
                if bu.health < 700:
                    self.home_of_flying_struct[bu.tag] = bu.position
                    self.log_success('up '+srt.name)
                    bu(LIFT)



    async def do_updown(self):
        self.routine = 'do_updown'
        if self.updown == -1:
            if self.structures(SUPPLYDEPOT).ready.amount > 0:
                for sd in self.structures(SUPPLYDEPOT).ready:
                    self.updown = sd.tag
        for sd in self.structures(SUPPLYDEPOTLOWERED).ready:
            if sd.tag == self.updown:
                danger = False
                for ene in self.enemy_units:
                    if self.near(ene.position,sd.position,5):
                        danger = True
                if danger:
                    sd(MORPH_SUPPLYDEPOT_RAISE)
                    self.log_success('raising')
        for sd in self.structures(SUPPLYDEPOT).ready:
            if sd.tag == self.updown:
                danger = False
                for ene in self.enemy_units:
                    if self.near(ene.position,sd.position,5):
                        danger = True
                if not danger:
                    sd(MORPH_SUPPLYDEPOT_LOWER)
                    self.log_success('lowering')



    async def siege_tank(self):
#       siege tank at a random own base
        for tnk in self.units(SIEGETANK).ready.idle:
            tnkt = tnk.tag
            if tnkt in self.towt_of_tnkt:
                towt = self.towt_of_tnkt[tnkt]
                for tow in self.all_bases:
                    if tow.tag == towt:
                        if self.near(tnk.position,tow.position,10):
                            tnk(SIEGEMODE_SIEGEMODE)
                        else:
                            tnk.attack(tow.position)
            else:
                if len(self.all_bases) == 0:
                    tnk(SIEGEMODE_SIEGEMODE)
                else:
                    tow = random.choice(self.all_bases)
                    towt = tow.tag
                    self.towt_of_tnkt[tnkt] = towt
                    tnk.attack(tow.position)


    async def fire_yamato(self):
        for bc in self.units(BATTLECRUISER).ready:
            found = False
#           missing some
            for kind in (ARCHON,BATTLECRUISER,CARRIER,QUEEN,VIKINGFIGHTER,MISSILETURRET,SPORECRAWLER,PHOTONCANNON,\
            INFESTOR,HYDRALISK,THOR,VIPER,PHOENIX,RAVAGER):
                for ene in self.enemy_units(kind):
                    if self.near(ene.position,bc.position,8):
                        target = ene
                        found = True
            if found:
                abilities = (await self.get_available_abilities([bc]))[0]
                if YAMATO_YAMATOGUN in abilities:
                    bc(YAMATO_YAMATOGUN, target)
        for ra in self.units(RAVEN).ready:
            found = False
#           missing some
            for kind in (ARCHON,BATTLECRUISER,CARRIER,QUEEN,VIKINGFIGHTER,MISSILETURRET,SPORECRAWLER,PHOTONCANNON,\
            INFESTOR,HYDRALISK,THOR,VIPER,PHOENIX,RAVAGER):
                for ene in self.enemy_units(kind):
                    if self.near(ene.position,ra.position,8):
                        target = ene
                        found = True
            if found:
                abilities = (await self.get_available_abilities([ra]))[0]
                if EFFECT_ANTIARMORMISSILE in abilities:
                    ra(EFFECT_ANTIARMORMISSILE, target)



    async def do_upgrade(self,upg):
        self.routine = 'do_upgrade'
        didit = False
#       bug on COMBATSHIELD
        if type(upg) == UpgradeId:
            if self.already_pending_upgrade(upg) == 0:
                if self.check_techtree(upg):
                    for pair in self.cradle:
                        if pair[0] == upg:
                            cra = pair[1]
                            for ar in self.structures(cra).ready:
                                if ar.tag in self.idle_structure_tags:
                                    if self.can_pay(upg,False) or self.bug_can_pay(upg,False):
                                        didit = True
                                        self.log_success(upg.name)
#                                       circumvent some bugs
                                        if upg == TERRANVEHICLEANDSHIPARMORSLEVEL1:
                                            ar(AbilityId.ARMORYRESEARCH_TERRANVEHICLEANDSHIPPLATINGLEVEL1)
                                        elif upg == TERRANVEHICLEANDSHIPARMORSLEVEL2:
                                            ar(AbilityId.ARMORYRESEARCH_TERRANVEHICLEANDSHIPPLATINGLEVEL2)
                                        elif upg == TERRANVEHICLEANDSHIPARMORSLEVEL3:
                                            ar(AbilityId.ARMORYRESEARCH_TERRANVEHICLEANDSHIPPLATINGLEVEL3)       
                                        else:
                                            ar.research(upg)
                                        self.idle_structure_tags.remove(ar.tag)
        return didit




    async def battle_jump_home(self):
        self.routine = 'battle_jump_home'
        for bc in self.units(BATTLECRUISER).ready:
            if (bc.health <= self.bc_fear) and (bc.tag not in self.bct_in_repair):
#               jump bc home for repair
                self.log_success('')
                bc(EFFECT_TACTICALJUMP,self.shipyard)
                self.bct_in_repair.append(bc.tag)
                self.bc_fear = max(150,self.bc_fear-10)



    async def ruin(self):
        for s in self.structures_without_construction_SCVs():
            s(CANCEL)



    async def repair_it(self):
        self.routine = 'repair_it'
        for scv in self.units(SCV).ready:
            scvt = scv.tag
            if scvt in self.all_scvt:
                if self.job_of_scvt[scvt] == 'arearepairer':
                    if scvt in self.busy_arearepairer:
                        if scv.is_idle or scv.is_collecting:
                            self.busy_arearepairer.remove(scvt)
                            self.log_workers('finished '+self.name(scvt))
                    else:
                        low_qual = 1.0
                        wreck = None
                        for s in self.structures.ready:
                            if self.near(scv.position,s.position,15):
                                qual = s.health/s.health_max
                                if qual<low_qual:
                                    low_qual = qual
                                    wreck = s
                        if low_qual < 0.99:
#                           important work to do!
                            s = wreck
                            self.log_workers(' '+s.name+' '+self.name(scvt))
                            scv.repair(s)
                            self.busy_arearepairer.append(scvt)
                        elif scv.is_idle:
                            if self.near(scv.position,self.cottage_of_scvt[scvt],5):
#                               dream or mine unadministrated
                                self.fix_count_of_mimt()
                                if self.mimminer_vacatures() > 0:
                                    mimt = self.get_near_mimt_free(scv.position)
                                    for mim in self.mineral_field:
                                        if mim.tag == mimt:
                                            if self.near(mim.position,scv.position,12):
                                                scv.gather(mim)
                                                self.log_workers('arearepairer bored '+self.name(scvt))
                            else:
                                self.log_workers('going home '+self.name(scvt))
                                scv(MOVE_MOVE,self.cottage_of_scvt[scvt])



    async def manage_workers(self):
        self.routine = 'manage_workers'
#       
#       panic
        for scv in self.units(SCV):
            scvt = scv.tag
            if scvt in self.all_scvt:
                job = self.job_of_scvt[scvt]
                if job in ('gasminer','mimminer'):
                    panic = True
                    for tow in self.all_bases:
                        if self.near(scv.position,tow.position,self.miner_bound):
                            panic = False
                    if panic:
                        self.log_workers('fleeing '+job+' '+self.name(scvt))
                        self.job_of_scvt[scvt] = 'fleeer'
                        self.promotionsite_of_scvt[scvt] = scv.position
                        place = Point2((random.randrange(self.map_left,self.map_right),random.randrange(self.map_bottom,self.map_top)))
                        scv(MOVE_MOVE,place)
#       jobhaters 
        for scv in self.units(SCV).idle:
            scvt = scv.tag
            if scvt in self.all_scvt:
                job = self.job_of_scvt[scvt]
#               fleeer turns to idler if there is no danger
                if job == 'fleeer':
                    danger = False
                    for ene in self.enemy_units:
                        if self.near(ene.position,scv.position,7):
                            danger = True
                    if not danger:
                        if scv.position != self.promotionsite_of_scvt[scvt]:
                            self.log_workers('fired slacking '+job+' '+self.name(scvt))
                            self.job_of_scvt[scvt] = 'idler'
#               May idle: traveller, shiprepairer, arearepairer
                elif job in ('gasminer','mimminer','applicant','escorter','builder'):
                    if scv.position != self.promotionsite_of_scvt[scvt]:
                        self.log_workers('fired slacking '+job+' '+self.name(scvt))
                        self.job_of_scvt[scvt] = 'idler'
                elif job == 'traveller':
                    if not self.near(scv.position,self.goal_of_trabu_scvt[scvt],3):
#                       this can occur if the traveller has been blocked
                        scv(MOVE_MOVE,self.goal_of_trabu_scvt[scvt])
#       builders start to mine after building a geyser
        for scv in self.units(SCV):
            scvt = scv.tag
            if scvt in self.all_scvt:
                job = self.job_of_scvt[scvt]
                if job == 'builder':
                    if scv.is_collecting:
                        if self.gasminer_vacatures() > 0:
                            if scv.position != self.promotionsite_of_scvt[scvt]:
                                self.log_workers('jobswich mining builder '+self.name(scvt))
                                self.job_of_scvt[scvt] = 'gasminer'
                                gast = self.get_near_gast_free(scv.position)
                                self.gast_of_scvt[scvt] = gast
                                self.count_of_gast[gast] = self.count_of_gast[gast]+1
#       
        self.fix_count_of_job()
#
#       arearepairers
        wishr = min(len(self.all_scvt)//6,len(self.all_bases))
        if self.count_of_job['arearepairer'] > wishr:
#           get one that is far from each base
            best_dist = 0
            best_scvt = None
            for scv in self.units(SCV).ready:
                scvt = scv.tag
                if scvt in self.all_scvt:
                    if self.job_of_scvt[scvt] == 'arearepairer':
                        clos_dist = 80000
                        for tow in self.all_bases:
                            sd = self.sdist(self.cottage_of_scvt[scvt],tow.position)
                            clos_dist = min(clos_dist,sd)
                        if clos_dist > best_dist:
                            best_dist = clos_dist
                            best_scvt = scvt
            scvt = best_scvt
            for scv in self.units(SCV).ready:
                if scv.tag == scvt:
                    self.log_workers('fired arearepairer '+self.name(scvt))
                    self.job_of_scvt[scvt] = 'idler'
                    scv(STOP)
        if self.count_of_job['arearepairer'] < wishr:
#           get a base that is far from each cottage
            worst_towpos = None
            worst_dist = 0
            for tow in self.all_bases:
                towpos = tow.position
                clos_dist = 80000
                for scvt in self.all_scvt:
                    if self.job_of_scvt[scvt] == 'arearepairer':
                        sd = self.sdist(self.cottage_of_scvt[scvt],towpos)
                        clos_dist = min(clos_dist,sd)
                if clos_dist > worst_dist:
                    worst_dist = clos_dist
                    worst_towpos = towpos
            towpos = worst_towpos
#           promote an scv
            scvt = self.get_near_scvt_to_goodjob(towpos)
            for scv in self.units(SCV):
                if scv.tag == scvt:
                    job = self.job_of_scvt[scvt]
                    self.log_workers('promoted '+job+' to arearepairer '+self.name(scvt))
                    if scv.is_collecting:
                        scv(STOP)
                    self.job_of_scvt[scvt] = 'arearepairer'
                    self.promotionsite_of_scvt[scvt] = scv.position
                    self.cottage_of_scvt[scvt] = towpos
#       
#       shiprepairers
        amount = self.units(BATTLECRUISER).ready.amount
#       hire new shiprepairer
        todo = amount - self.count_of_job['shiprepairer']
        if todo > 0:
            scvt = self.get_near_scvt_to_goodjob(self.shipyard)
            for scv in self.units(SCV):
                if scv.tag == scvt:
                    job = self.job_of_scvt[scvt]
                    self.log_workers('promoted '+job+' to shiprepairer '+self.name(scvt))
                    if scv.is_collecting:
                        scv(STOP)
                    self.job_of_scvt[scvt] = 'shiprepairer'
                    self.promotionsite_of_scvt[scvt] = scv.position
#       fire some
        todo = self.count_of_job['shiprepairer'] - amount
        if todo > 0:
            for scvt in self.all_scvt:
                if self.job_of_scvt[scvt] == 'shiprepairer':
                    if todo > 0:
                        todo = todo-1
                        self.log_workers('fired shiprepairer '+self.name(scvt))
                        self.job_of_scvt[scvt] = 'idler'
#       whip them
        for scv in self.units(SCV).idle:
            scvt = scv.tag
            if scvt in self.all_scvt:
                if (self.job_of_scvt[scvt] == 'shiprepairer'):
                    if not self.near(scv.position,self.shipyard,15):
                        scv(MOVE_MOVE,self.shipyard)
                    elif len(self.bct_in_repair) > 0:
                        for bc in self.units(BATTLECRUISER).ready:
                            bct = bc.tag
                            if bct == self.bct_in_repair[0]:
                                if self.near(bc.position,self.shipyard,15):
                                    scv.repair(bc)
#       keep the bc in the shipyard
        if len(self.bct_in_repair) > 0:
            for bc in self.units(BATTLECRUISER).ready:
                bct = bc.tag
                if bct == self.bct_in_repair[0]:
                     if self.near(bc.position,self.shipyard,15) and not self.near(bc.position,self.shipyard,5):
                         bc(MOVE_MOVE,self.shipyard)



    def search_applicants(self):
        self.fix_count_of_job()
        total_wish = 0
        for cc in self.all_bases:
            total_wish = total_wish + self.wanted_of_cct[cc.tag]
        if total_wish < self.count_of_job['idler']:
            for cc in self.all_bases:
                while self.wanted_of_cct[cc.tag] > 0:
                    self.wanted_of_cct[cc.tag] = self.wanted_of_cct[cc.tag]-1
                    scvt = self.get_near_scvt_idler(cc.position)
                    for scv in self.units(SCV):
                        if scv.tag == scvt:
                            self.job_of_scvt[scvt] = 'applicant'
                            self.promotionsite_of_scvt[scvt] = scv.position
                            scv(MOVE_MOVE,cc.position.towards(self.game_info.map_center,-3))
                            self.log_workers('new applicant group '+self.name(scvt))
                            self.vision_of_scvt[scvt] = cc.tag
        else:
            for scv in self.units(SCV):
                scvt = scv.tag
                if self.job_of_scvt[scvt] == 'idler':
                    cct = self.get_near_cct_wanted(scv.position)
                    for cc in self.all_bases:
                        if cc.tag == cct:
                            self.wanted_of_cct[cc.tag] = self.wanted_of_cct[cc.tag]-1
                            self.job_of_scvt[scvt] = 'applicant'
                            self.promotionsite_of_scvt[scvt] = scv.position
                            scv(MOVE_MOVE,cc.position.towards(self.game_info.map_center,-3))
                            self.log_workers('new applicant '+self.name(scvt))
                            self.vision_of_scvt[scvt] = cc.tag



    async def manage_gas(self):
        self.routine = 'manage_gas'
        self.log_gasminer()
        for scvt in self.all_scvt:
            if self.job_of_scvt[scvt] == 'gasminer':
                if scvt not in self.gast_of_scvt:
                    self.log_workers('gasminer retired '+self.name(scvt))
                    self.job_of_scvt[scvt] = 'idler'
        self.fix_count_of_job()
        vacatures = self.gasminer_vacatures()
        if vacatures > 0:
#           new gas-mineral connections
            if vacatures < self.count_of_job['idler']:
                for gas in self.all_refineries:
                    gast = gas.tag
                    if gast in self.all_gast:
                        if self.count_of_gast[gast] < 3:
                            scvt = self.get_near_scvt_idler(gas.position)
                            for scv in self.units(SCV):
                                if scv.tag == scvt:
                                    if self.near(scv.position,gas.position,self.miner_bound):
                                        self.job_of_scvt[scvt] = 'gasminer'
                                        self.promotionsite_of_scvt[scvt] = scv.position
                                        scv.gather(gas)
                                        self.log_workers('new gasminer group '+self.name(scvt))
                                        self.gast_of_scvt[scvt] = gast
                                        self.count_of_gast[gast] = self.count_of_gast[gast]+1
            else:
                for scv in self.units(SCV):
                    scvt = scv.tag
                    if self.job_of_scvt[scvt] == 'idler':
                        gast = self.get_near_gast_free(scv.position)
                        for gas in self.all_refineries:
                            if gas.tag == gast:
                                if self.near(scv.position,gas.position,self.miner_bound):
                                    self.job_of_scvt[scvt] = 'gasminer'
                                    self.promotionsite_of_scvt[scvt] = scv.position
                                    scv.gather(gas)
                                    self.log_workers('new gasminer '+self.name(scvt))
                                    self.gast_of_scvt[scvt] = gast
                                    self.count_of_gast[gast] = self.count_of_gast[gast]+1
        self.log_gasminer()
#       after we tried local miner hiring, want applicants
        if self.mimminer_vacatures()+self.gasminer_vacatures() > len(self.vision_of_scvt):
            self.wanted_of_cct = {}
            for cc in self.all_bases:
                self.wanted_of_cct[cc.tag] = 0
            for gast in self.all_gast:
                if self.count_of_gast[gast]<3:
#                   get the gas, get its cc, increase its self.wanted_of_cct
                    for gas in self.all_refineries:
                        if gas.tag == gast:
                            for cc in self.all_bases:
                                if self.near(gas.position,cc.position,self.miner_bound):
                                    self.wanted_of_cct[cc.tag] = self.wanted_of_cct[cc.tag]+1
#           decrease self.wanted_of_cct for walking applicants
            for scvt in self.vision_of_scvt:
                cct = self.vision_of_scvt[scvt]
                self.wanted_of_cct[cct] = self.wanted_of_cct[cct]-1
            self.search_applicants()


    async def manage_minerals(self):
        self.routine = 'manage_minerals'
        for scvt in self.all_scvt:
            if self.job_of_scvt[scvt] == 'mimminer':
                if scvt not in self.mimt_of_scvt:
                    self.log_workers('miner retired '+self.name(scvt))
                    self.job_of_scvt[scvt] = 'idler'
        self.fix_count_of_job()
        vacatures = self.mimminer_vacatures()
        if vacatures > 0:
#           new mim-mineral connections
            if vacatures < self.count_of_job['idler']:
                for mim in self.mineral_field:
                    mimt = mim.tag
                    if mimt in self.all_mimt:
                        if self.count_of_mimt[mimt] < 2:
                            scvt = self.get_near_scvt_idler(mim.position)
                            for scv in self.units(SCV):
                                if scv.tag == scvt:
                                    if self.near(scv.position,mim.position,self.miner_bound):
                                        self.job_of_scvt[scvt] = 'mimminer'
                                        self.promotionsite_of_scvt[scvt] = scv.position
                                        scv.gather(mim)
                                        self.log_workers('new miner group '+self.name(scvt))
                                        self.mimt_of_scvt[scvt] = mimt
                                        self.count_of_mimt[mimt] = self.count_of_mimt[mimt]+1
            else:
                for scv in self.units(SCV):
                    scvt = scv.tag
                    if self.job_of_scvt[scvt] == 'idler':
                        mimt = self.get_near_mimt_free(scv.position)
                        for mim in self.mineral_field:
                            if mim.tag == mimt:
                                if self.near(scv.position,mim.position,self.miner_bound):
                                    self.job_of_scvt[scvt] = 'mimminer'
                                    self.promotionsite_of_scvt[scvt] = scv.position
                                    scv.gather(mim)
                                    self.log_workers('new miner '+self.name(scvt))
                                    self.mimt_of_scvt[scvt] = mimt
                                    self.count_of_mimt[mimt] = self.count_of_mimt[mimt]+1
#       after we tried local miner hiring, want applicants
        if self.mimminer_vacatures()+self.gasminer_vacatures() > len(self.vision_of_scvt):
            self.wanted_of_cct = {}
            for cc in self.all_bases:
                self.wanted_of_cct[cc.tag] = 0
            for mimt in self.all_mimt:
                if self.count_of_mimt[mimt]<2:
#                   get the mim, get its cc, increase its self.wanted_of_cct
                    for mim in self.mineral_field:
                        if mim.tag == mimt:
                            for cc in self.all_bases:
                                if self.near(mim.position,cc.position,self.miner_bound):
                                    self.wanted_of_cct[cc.tag] = self.wanted_of_cct[cc.tag]+1
#           decrease self.wanted_of_cct for walking applicants
            for scvt in self.vision_of_scvt:
                cct = self.vision_of_scvt[scvt]
                self.wanted_of_cct[cct] = self.wanted_of_cct[cct]-1
            self.search_applicants()



    async def manage_rest(self):
        self.routine = 'manage_rest'
        self.fix_count_of_job()
#       
#       applicant was walking to a cc with a problem
        for scvt in self.all_scvt:
            if self.job_of_scvt[scvt] == 'applicant':
                if scvt not in self.vision_of_scvt:
                    self.log_workers('applicant going nowhere '+self.name(scvt))
                    self.job_of_scvt[scvt] = 'idler'
                    for scv in self.units(SCV):
                        if scv.tag == scvt:
                            scv(STOP)
#       
#       max idle workers
        todo = self.count_of_job['idler'] - 22
        for scv in self.units(SCV):
            scvt = scv.tag
            if scvt in self.all_scvt:
                if self.job_of_scvt[scvt] == 'idler':
                    if todo > 0:
                        todo = todo-1
                        self.log_workers('suiciding idler '+self.name(scvt))
                        self.job_of_scvt[scvt] = 'suicider'
                        self.promotionsite_of_scvt[scvt] = scv.position
                        scv.attack(self.enemyloc)
#       job-swap for late game
        if (self.count_of_job['idler'] == 0) and (self.itera % 9 == 0):
            if self.minerals > self.vespene + 1000:
                todo = 1
                for scvt in self.all_scvt:
                    if (self.job_of_scvt[scvt] == 'mimminer'):
                        if todo > 0:
                            todo = todo-1
                            self.log_workers('floating minerals, fire '+self.name(scvt))
                            self.job_of_scvt[scvt] = 'idler'
                            for scv in self.units(SCV):
                                if scvt == scv.tag:
                                    scv(STOP) 
            if self.vespene > self.minerals + 1000:
                todo = 1
                for scvt in self.all_scvt:
                    if (self.job_of_scvt[scvt] == 'gasminer'):
                        if todo > 0:
                            todo = todo-1
                            self.log_workers('floating gas, fire '+self.name(scvt))
                            self.job_of_scvt[scvt] = 'idler'
                            for scv in self.units(SCV):
                                if scvt == scv.tag:
                                    scv(STOP) 
#       stop escorters lured to their death
        for scvt in self.all_scvt:
            if (self.job_of_scvt[scvt] == 'escorter'):
                for scv in self.units(SCV):
                    if scvt == scv.tag:
                        if self.near(scv.position,self.enemyloc,50):
                            self.job_of_scvt[scvt] = 'idler'
                            self.log_workers('Enemy fear stops escorter '+self.name(scvt))
                            scv(STOP) 



#   rush
    async def rush(self,thing,amount):
        self.routine = 'rush'
        self.endwish_am_of_th[thing] = amount
        if thing in self.wish_am_of_th:
            self.wish_am_of_th[thing] = max(self.wish_am_of_th[thing],amount)
        else:
            self.wish_am_of_th[thing] = amount
            self.wish_pri_of_th[thing] = 1
        self.log_wish('wishing '+thing.name+' '+str(amount))
        stable = False
        while not stable:
            stable = True
#           to change a dict while using it:
#           method 1:   old_wish = self.wish.copy()
#           method 2:   walk and merge
#           method 3:   elementswise copy
            workwish_am_of_th = {}
            workwish_pri_of_th = {}
            for th in self.wish_am_of_th:
                workwish_am_of_th[th] = self.wish_am_of_th[th]
                workwish_pri_of_th[th] = self.wish_pri_of_th[th]
            for th in self.wish_am_of_th:
                pri = self.wish_pri_of_th[th]
                for pair in self.techtree:
                    if pair[0] == th:
                        otherth = pair[1]
                        if otherth in self.wish_am_of_th:
                            if self.wish_pri_of_th[otherth] < pri+1:
                                workwish_pri_of_th[otherth] = pri+1
                                stable = False
                        else:
                            workwish_am_of_th[otherth] = 1
                            workwish_pri_of_th[otherth] = pri+1
                            stable = False
            for th in workwish_am_of_th:
                self.wish_am_of_th[th] = workwish_am_of_th[th]
                self.wish_pri_of_th[th] = workwish_pri_of_th[th]
        for th in self.wish_am_of_th:
            am = self.wish_am_of_th[th]
            pri = self.wish_pri_of_th[th]
            self.log_wish('so wishing '+th.name+'   amount '+str(am)+'   priority '+str(pri))

    async def rush_stop(self,thing,amount):
        self.routine = 'rush_stop'
        self.enddemand_am_of_th[thing] = amount




#       Easy/Medium/Hard/VeryHard
run_game(maps.get('ZenLE'), [
    Bot(Race.Terran, Chaosbot()),
    Computer(Race.Zerg, Difficulty.VeryHard)
    ], realtime=True)
