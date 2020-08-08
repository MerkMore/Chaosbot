# Merkbot.py containing Chaosbot
# author: MerkMore
# version 8 aug 2020
# Burny style
from typing import List,Set,Dict
#
import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer
from sc2.ids.ability_id import AbilityId
from sc2.ids.unit_typeid import UnitTypeId
from sc2.ids.upgrade_id import UpgradeId
from sc2.ids.effect_id import EffectId
from sc2.ids.buff_id import BuffId
from sc2.position import Point2
import random
from math import sqrt,cos,sin
from sc2.game_info import GameInfo
from layout_if_py import layout_if
# from sc2.constants import *
from sc2.ids.unit_typeid import SCV
from sc2.ids.unit_typeid import RAVEN
from sc2.ids.unit_typeid import STARPORT
from sc2.ids.unit_typeid import VIKINGFIGHTER
from sc2.ids.unit_typeid import MARINE
from sc2.ids.unit_typeid import BARRACKS
from sc2.ids.unit_typeid import BUNKER
from sc2.ids.unit_typeid import MARAUDER
from sc2.ids.unit_typeid import MEDIVAC
from sc2.ids.unit_typeid import SIEGETANK
from sc2.ids.unit_typeid import HELLION
from sc2.ids.unit_typeid import FACTORY
from sc2.ids.unit_typeid import BATTLECRUISER
from sc2.ids.unit_typeid import BARRACKSTECHLAB
from sc2.ids.unit_typeid import FACTORYTECHLAB
from sc2.ids.unit_typeid import STARPORTTECHLAB
from sc2.ids.upgrade_id import PUNISHERGRENADES
from sc2.ids.upgrade_id import TERRANSHIPWEAPONSLEVEL1
from sc2.ids.unit_typeid import ARMORY
from sc2.ids.upgrade_id import TERRANSHIPWEAPONSLEVEL2
from sc2.ids.upgrade_id import TERRANSHIPWEAPONSLEVEL3
from sc2.ids.upgrade_id import TERRANVEHICLEANDSHIPARMORSLEVEL1
from sc2.ids.upgrade_id import TERRANVEHICLEANDSHIPARMORSLEVEL2
from sc2.ids.upgrade_id import TERRANVEHICLEANDSHIPARMORSLEVEL3
from sc2.ids.upgrade_id import TERRANBUILDINGARMOR
from sc2.ids.unit_typeid import ENGINEERINGBAY
from sc2.ids.upgrade_id import TERRANINFANTRYWEAPONSLEVEL1
from sc2.ids.upgrade_id import TERRANINFANTRYWEAPONSLEVEL2
from sc2.ids.upgrade_id import TERRANINFANTRYWEAPONSLEVEL3
from sc2.ids.unit_typeid import PLANETARYFORTRESS
from sc2.ids.unit_typeid import ORBITALCOMMAND
from sc2.ids.unit_typeid import COMMANDCENTER
from sc2.ids.upgrade_id import BATTLECRUISERENABLESPECIALIZATIONS
from sc2.ids.unit_typeid import FUSIONCORE
from sc2.ids.unit_typeid import SUPPLYDEPOT
from sc2.ids.unit_typeid import SUPPLYDEPOTLOWERED
from sc2.ids.unit_typeid import REFINERY
from sc2.ids.unit_typeid import REFINERYRICH
from sc2.ids.unit_typeid import MISSILETURRET
from sc2.ids.unit_typeid import BARRACKSFLYING
from sc2.ids.unit_typeid import FACTORYFLYING
from sc2.ids.unit_typeid import STARPORTFLYING
from sc2.ids.unit_typeid import COMMANDCENTERFLYING
from sc2.ids.unit_typeid import SIEGETANKSIEGED
from sc2.ids.unit_typeid import ARCHON
from sc2.ids.unit_typeid import CARRIER
from sc2.ids.unit_typeid import QUEEN
from sc2.ids.unit_typeid import SPORECRAWLER
from sc2.ids.unit_typeid import PHOTONCANNON
from sc2.ids.unit_typeid import INFESTOR
from sc2.ids.unit_typeid import HYDRALISK
from sc2.ids.unit_typeid import THOR
from sc2.ids.unit_typeid import VIPER
from sc2.ids.unit_typeid import PHOENIX
from sc2.ids.unit_typeid import RAVAGER
from sc2.ids.unit_typeid import BANSHEE
from sc2.ids.unit_typeid import LIBERATOR
from sc2.ids.unit_typeid import OVERLORD
from sc2.ids.unit_typeid import BROODLORD
from sc2.ids.unit_typeid import ORACLE
from sc2.ids.unit_typeid import OBSERVER
from sc2.ids.unit_typeid import HATCHERY
from sc2.ids.unit_typeid import LAIR
from sc2.ids.unit_typeid import HIVE
from sc2.ids.unit_typeid import NEXUS
from sc2.ids.unit_typeid import CYCLONE
# with INFESTED is meant "close to the enemy".
from sc2.ids.unit_typeid import INFESTEDBARRACKS
from sc2.ids.unit_typeid import INFESTEDBUNKER
from sc2.ids.unit_typeid import INFESTEDFACTORY
from sc2.ids.unit_typeid import INFESTEDSTARPORT



class Chaosbot(sc2.BotAI):
#   ############### CHANGE VALUE AD LIB
    do_log_success = True
    do_log_workers = True
    do_log_population = False
    do_log_armysize = False
    do_log_army = False
    do_log_attacktype = False
    do_log_gasminer = False
    do_log_resource = False
    do_log_limbo = False
    do_log_wish = False
    do_log_buildseries = False
    do_log_placing = False
    do_log_planning = True
    do_log_buildplan = True
    do_log_time = False
    do_log_layout = False
    do_log_command = True
    do_log_cheese = True
#   ############### CONSTANT
#   constant over the iterations after iteration 0:
#   other
    nowhere = Point2((1,1))
    all_structures = []
    all_structures_tobuildwalk = []
    all_army = []
    all_upgrades = []
    all_labs = []
    builddura_of_thing = {}
    size_of_structure = {}
    liftable = []
    techtree = []
    anything = set()
    cradle = []
    shipyard = None
    bc_enemies = None
#   squareroots of integers from 0 to 200*200*2, 0<=x<400
    stored_root = []
#   timing constants
    gas_speed = 1.0
    mim_speed = 1.0
    walk_speed = 2.0
#   
    miner_bound = 10
    enemyloc = None
    enemy_target_base_loc = None
    map_left = 0
    map_right = 0
    map_bottom = 0
    map_top = 0
    dummytag = -1
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
    # idle in this iteration:
    idle_structure_tags = []
    last_log_buildseries_string = ''
#   ############### ARMY AND STRUCTURE MANAGEMENT
#   the supplydepot used as a gate:
    updown = dummytag
#   army coodination
    frozenbctags = set()
    attack_type = 'jumpy'
    cruisercount = 0
    lastcruisercount = 0
    home_of_flying_struct = {}
    landings_of_flying_struct = {}
    bct_in_repair = []
    bestbctag = dummytag
    bc_fear = 250
#   ambition contains commandcenters becoming a planetaryfortress, factories getting a techlab, etc.
    ambition_of_strt = {}
#   the barracks in the wall could be placed such as not to be able to get a techlab
    add_on_denied = []
    towt_of_tnkt = {}
    army_center_point = None
#   (struc,place,tag) for tobuildwalk plans with a layout. Administrate to enable erasing.
    designs = []
#   A barracks close to the enemy has to fly from build position to attack position
    infestedbarracks_build_position = None
    infestedfactory_build_position = None
    infested_land_position = None
    cheese_phase = 'A'
    cheese_prison = None
    cheese_barracks = None
    cheese_factory = None
    cheese_bunker = None
    cheese_scv = None
    cheese_marines = set()
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
#   interface planning / workers
    gas_advice = 0
#   ############### PLAY CHOICES
#   wish for mid_game
    game_phase = 'init'
    endwish_am_of_th = {}
    wish_am_of_th = {}
    wish_pri_of_th = {}
    log_wish_history = ''
#   the make_planning routine
    # buildseries is a list of buildings, that we want to make. It contains techtree predecessors.
    # buildorder is a list of (building,place) combinations. Or e.g. (MARINE,place-of-a-future-barracks)
    # executive is the chosen buildorder. Work has to be removed from the executive when the order is started.
    # executive contains work we will do, it just is not clear when to start it, money is not reserved yet
    buildseries = []
    buildorder = []
    buildorder_to_execute = []
    planning = []
    executive = []
    but_i_had_structures = 0
#   to capture the current situation for the planning:
    situation_mimminers = 0
    situation_gasminers = 0
    situation_minerals = 0
    situation_vespene = 0
    situation_running = set()
    situation_constructing = set()
    situation_training = set()
    situation_thingkinds = set()
    situation_buildings_and_parts = set()
    situation_events = set()
#   money handling with reservations
    reserved_minerals = 0
    reserved_vespene = 0
#   strategy
    strategy = []
    game_choice = []
    game_choices = 10
    game_result = 'doubt'

# *********************************************************************************************************************
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
        if (iteration % 5 == 0) and (iteration > 0):
            self.get_situation()
            self.make_planning(0)
            self.executive = self.planning.copy()
        self.log_resource()
        self.log_armysize()
        self.make_buildorder_to_execute()
        await self.build_worker(100-self.minerals//100)
        await self.follow_executive()
        await self.start_construction()
        await self.siege_tank()
        await self.fire_yamato()
        await self.battle_jump_home()
        await self.battle_dodge_bile()
        await self.hellion_dodge()
        await self.ruin()
        await self.repair_it()
        await self.supply_depots_adlib()
        await self.lift()
        await self.do_updown()
        await self.bunkercheese()
        await self.attack()
        await self.manage_workers()
        if self.minerals < self.vespene:
            await self.manage_minerals()
            await self.manage_gas()
        else:
            await self.manage_gas()
            await self.manage_minerals()
        await self.manage_rest()
        await self.win_loss()

# *********************************************************************************************************************
    async def my_init(self):
        self.routine = 'my_init'
        self.log_success('##############################################################################')
        random.seed()
#       liftable
        self.liftable = [BARRACKS,FACTORY,STARPORT,COMMANDCENTER, INFESTEDBARRACKS, INFESTEDFACTORY]
        self.landable = [BARRACKSFLYING,FACTORYFLYING,STARPORTFLYING,COMMANDCENTERFLYING]
#       enemy air with weak air defence
        self.viking_targets = [BANSHEE,LIBERATOR,ORACLE,BROODLORD,OVERLORD,OBSERVER]
#       enemy that can hurt a bc
        self.bc_enemies = (ARCHON, BATTLECRUISER, CARRIER, QUEEN, VIKINGFIGHTER, MISSILETURRET, SPORECRAWLER, \
            PHOTONCANNON, INFESTOR, HYDRALISK, THOR, VIPER, PHOENIX, RAVAGER, CYCLONE)
        # all_labs wegens verschoven plaatsing
        self.all_labs = (BARRACKSTECHLAB,FACTORYTECHLAB,STARPORTTECHLAB)
#       list of most structures, with builddura, size
        self.init_structures(SUPPLYDEPOT, 21, 2)
        self.init_structures(BARRACKS, 46, 3)
        self.init_structures(REFINERY, 24, 3)
        self.init_structures(BARRACKSTECHLAB, 18, 2)
        self.init_structures(FACTORY, 43, 3)
        self.init_structures(FACTORYTECHLAB, 18, 2)
        self.init_structures(STARPORT, 36, 3)
        self.init_structures(STARPORTTECHLAB, 18, 2)
        self.init_structures(FUSIONCORE,46, 3)
        self.init_structures(COMMANDCENTER, 71, 5)
        self.init_structures(PLANETARYFORTRESS, 36, 5)
        self.init_structures(ORBITALCOMMAND, 25, 5)
        self.init_structures(ENGINEERINGBAY, 25, 3)
        self.init_structures(MISSILETURRET,18, 2)
        self.init_structures(ARMORY, 46, 3)
        self.init_structures(BUNKER, 29, 3)
#       add for cheese with barracks and bunker
        self.init_structures(INFESTEDBARRACKS, 46, 3)
        self.init_structures(INFESTEDBUNKER, 29, 3)
        self.init_structures(INFESTEDFACTORY, 43, 3)
        self.init_structures(INFESTEDSTARPORT, 36, 3)
#       army, builddura 
        self.init_army(SCV,12)
        self.init_army(MARINE,18)
        self.init_army(MARAUDER,21)
        self.init_army(HELLION,21)
        self.init_army(CYCLONE,32)
        self.init_army(SIEGETANK,32)
        self.init_army(VIKINGFIGHTER,30)
        self.init_army(MEDIVAC,30)
        self.init_army(RAVEN,43)
        self.init_army(LIBERATOR,43)
        self.init_army(BATTLECRUISER,64)
#       upgrade, builddura
        self.init_upgrade(PUNISHERGRENADES, 43) #concussive shells
        self.init_upgrade(TERRANSHIPWEAPONSLEVEL1, 114)
        self.init_upgrade(TERRANSHIPWEAPONSLEVEL2, 136)
        self.init_upgrade(TERRANSHIPWEAPONSLEVEL3, 157)
        self.init_upgrade(TERRANVEHICLEANDSHIPARMORSLEVEL1, 114)
        self.init_upgrade(TERRANVEHICLEANDSHIPARMORSLEVEL2, 136)
        self.init_upgrade(TERRANVEHICLEANDSHIPARMORSLEVEL3, 157)
        self.init_upgrade(TERRANBUILDINGARMOR, 100)
        self.init_upgrade(TERRANINFANTRYWEAPONSLEVEL1, 114)
        self.init_upgrade(TERRANINFANTRYWEAPONSLEVEL2, 136)
        self.init_upgrade(TERRANINFANTRYWEAPONSLEVEL3, 157)
        self.init_upgrade(BATTLECRUISERENABLESPECIALIZATIONS, 100)
#       things that, to be built, need a cradle (a free building)
        self.init_cradle(RAVEN,STARPORT)
        self.init_cradle(MEDIVAC,STARPORT)
        self.init_cradle(VIKINGFIGHTER,STARPORT)
        self.init_cradle(LIBERATOR,STARPORT)
        self.init_cradle(MARINE,BARRACKS)
        self.init_cradle(MARAUDER,BARRACKS)
        self.init_cradle(SIEGETANK,FACTORY)
        self.init_cradle(CYCLONE,FACTORY)
        self.init_cradle(HELLION,FACTORY)
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
        self.init_cradle(ORBITALCOMMAND,COMMANDCENTER)
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
        self.init_techtree(ORBITALCOMMAND,BARRACKS)
        self.init_techtree(MISSILETURRET,ENGINEERINGBAY)
        self.init_techtree(FUSIONCORE,STARPORT)
        self.init_techtree(ARMORY,FACTORY)
#       added for cheese:        
        self.init_techtree(INFESTEDFACTORY,INFESTEDBARRACKS)
        self.init_techtree(INFESTEDSTARPORT,INFESTEDFACTORY)
        self.init_techtree(INFESTEDBARRACKS,SUPPLYDEPOT)
        self.init_techtree(INFESTEDBUNKER,INFESTEDBARRACKS)
#       First is unit
        self.init_techtree(BATTLECRUISER,STARPORTTECHLAB)
        self.init_techtree(BATTLECRUISER,FUSIONCORE)
        self.init_techtree(SIEGETANK,FACTORYTECHLAB)
        self.init_techtree(CYCLONE,FACTORYTECHLAB)
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
#       bootstrap code   after initial    from sc2constants import *
#       for thing in self.anything:
#           if type(thing) == UnitTypeId:
#               print('from sc2.ids.unit_typeid import '+thing.name)
#           if type(thing) == UpgradeId:
#               print('from sc2.ids.upgrade_id import '+thing.name)
        self.enemyloc = self.enemy_start_locations[0].position
        self.enemy_target_base_loc = self.enemyloc
        self.fix_count_of_job()
#       opening
#        self.buildseries_opening = [SUPPLYDEPOT, REFINERY, BARRACKS, SUPPLYDEPOT, MARINE, FACTORY, REFINERY, MARINE, \
#                                   STARPORT, COMMANDCENTER, FUSIONCORE, STARPORTTECHLAB, BATTLECRUISER]
#        self.buildseries_opening = [SUPPLYDEPOT, REFINERY, BARRACKS, SUPPLYDEPOT, MARINE]
        self.buildseries_opening = [SUPPLYDEPOT, INFESTEDBARRACKS, REFINERY, INFESTEDBUNKER, SUPPLYDEPOT, MARINE, MARINE, \
                                    BARRACKS, INFESTEDFACTORY, REFINERY, COMMANDCENTER, HELLION]
#       mid_game strategy
        await self.init_strategy()
        await self.mid_game(BATTLECRUISER,1)
        if self.game_choice[0]:
            await self.mid_game(SIEGETANK,1)
        if self.game_choice[1]:
            await self.mid_game(SIEGETANK,2)
        if self.game_choice[2]:
            await self.mid_game(MARINE,4)
        else:
            await self.mid_game(MARINE,8)
        if self.game_choice[3]:
            await self.mid_game(REFINERY,4)
            await self.mid_game(COMMANDCENTER,2)
            await self.mid_game(STARPORT,2)
        else:
            await self.mid_game(REFINERY,2)
        if self.game_choice[4]:
            await self.mid_game(ENGINEERINGBAY,1)
            await self.mid_game(MISSILETURRET,1)
        await self.mid_game(SUPPLYDEPOT,2)
        if False:
            await self.mid_game(INFESTEDBARRACKS,1)
            await self.mid_game(INFESTEDBUNKER,1)
#       circle
        self.make_circle()
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
        layout_if.enemyx = self.enemyloc.x
        layout_if.enemyy = self.enemyloc.y
        layout_if.save_layout()
#       shipyard
        self.shipyard = self.start_location.position.towards(self.game_info.map_center,5)
#       color the shipyard on the layout, so we will not build there ever
        yardx = round(self.shipyard.x)
        yardy = round(self.shipyard.y)
        for dx in range(-2,3):
            for dy in range(-2,3):
                layout_if.layout[yardx+dx][yardy+dy] = 5
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
        if len(self.tips) == 0:
            self.log_success('There are no placement tips for this map. Please run placer.py')
#       feedback the tips
        for nr in range(0,len(self.tips)):
            ti = self.tips[nr]
            self.log_placing(ti)
#       name_of_scvt: fun translation of scvt to english boy name
        pl = open('names.txt','r')
        self.all_names = pl.read().splitlines()
        pl.close()


#*********************************************************************************************************************
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

    def log_planning(self,stri):
        if self.do_log_planning:
            print(f' On {self.itera} planning {self.routine} '+stri)

    def log_command(self,stri):
        if self.do_log_command:
            print(f' On {self.itera} commands {self.routine} '+stri)

    def log_buildplan(self,bp):
        if self.do_log_buildplan:
            print(f' On {self.itera} buildplan '+str(bp[0])+' '+bp[1].name+' '+str(bp[2][0])+','+str(bp[2][1])+' '+\
                str(bp[3])+' '+str(bp[4])+' '+str(bp[5]))

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
            total = 0
            lin = ''
            for jo in self.count_of_job:
                co = self.count_of_job[jo]
                total = total+co
                lin = lin + jo[0]+jo[1]+jo[2]+' '+str(co)+'   '
            lin = lin + '  = '+str(total)
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

    def log_buildseries(self,stri):
        if self.do_log_buildseries:
            if stri != self.last_log_buildseries_string:
                print(f' On {self.itera} buildseries: '+stri)
                self.last_log_buildseries_string = stri
 
    def log_time(self,stri):
        if self.do_log_time:
            print(f' On {self.itera} time: '+stri)

    def log_cheese(self):
        if self.do_log_cheese:
            print(f' On {self.itera} cheese phase '+self.cheese_phase)

#*********************************************************************************************************************

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
        place = self.function_result_Point2
        x = place.x
        y = place.y
        if struc in self.all_structures_tobuildwalk:
            self.designs.append((struc,place,self.dummytag))
            self.log_layout('write position '+struc.name+' '+str(x)+' '+str(y))
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

    def erase_layout(self,struc,place):
        self.put_on_the_grid(struc,place)
        place = self.function_result_Point2
        x = place.x
        y = place.y
        if struc in self.all_structures_tobuildwalk:
            self.log_layout('erase position '+struc.name+' '+str(x)+' '+str(y))
            siz = self.size_of_structure[struc]
            for vakx in range(round(x-siz/2),round(x+siz/2)):
                for vaky in range(round(y-siz/2),round(y+siz/2)):
                    layout_if.layout[vakx][vaky] = 0
#           the add-on could still be there


    def check_layout(self,struc,place) -> bool:
        placable = True
        self.put_on_the_grid(struc,place)
        x = self.function_result_Point2.x
        y = self.function_result_Point2.y
        if (struc in self.all_structures_tobuildwalk):
            if (struc in (REFINERY,REFINERYRICH)):
                mustbecolor = 1
            else:
                mustbecolor = 0
            siz = self.size_of_structure[struc]
            for vakx in range(round(x-siz/2),round(x+siz/2)):
                for vaky in range(round(y-siz/2),round(y+siz/2)):
                    placable = placable and (layout_if.layout[vakx][vaky] == mustbecolor)
            if struc in (BARRACKS,FACTORY,STARPORT):
                x = x+2.5
                y = y-0.5
                siz = 2
                for vakx in range(round(x-siz/2),round(x+siz/2)):
                    for vaky in range(round(y-siz/2),round(y+siz/2)):
                        placable = placable and (layout_if.layout[vakx][vaky] == mustbecolor)
        return placable

#*********************************************************************************************************************

    def check_maxam(self,thing) -> bool:
        if thing in self.all_structures_tobuildwalk:
            maxam = 100
            if thing in (ARMORY,FUSIONCORE,ENGINEERINGBAY,BARRACKS,FACTORY):
                maxam = 2
            if thing == MISSILETURRET:
                maxam = self.all_bases.amount*5
            if thing in (INFESTEDBARRACKS,INFESTEDBUNKER, INFESTEDFACTORY):
                maxam = 1
        elif thing in self.all_structures:
            maxam = 100
        elif type(thing) == UpgradeId:
            maxam = 1
        else:
#           army
            maxam = 100
            if thing in (RAVEN,HELLION):
                maxam = 1
            if thing == VIKINGFIGHTER:
                maxam = 10
            if thing in (MARAUDER,SIEGETANK):
                maxam = 5
        started = self.we_started_amount(thing)
        return (started<maxam)

#*********************************************************************************************************************

#   distance
    def sdist(self,p,q) -> int:
        return (p[0]-q[0])**2 + (p[1]-q[1])**2
 
    def dist(self,p,q) -> int:
#       for int points in 200*200
#       tolerate non-int but then less precise
        sd = (p[0]-q[0])**2 + (p[1]-q[1])**2
        return self.squareroot(round(sd))
 
    def near(self,p,q,supdist) -> bool:
#       works for integers as well as for floats
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

    def make_circle(self):
#       10 points on the unitcircle
        self.circle = []
        for i in range(0,10):
            alfa = 0.63*i
            point = Point2((cos(alfa),sin(alfa)))
            self.circle.append(point)

    def flee(self,posi,dist) -> Point2:
#       get a random point at distance 'dist' from your point 'posi' 
        offset = random.choice(self.circle)
        return Point2((posi.x+offset.x*dist,posi.y+offset.y*dist))


#*********************************************************************************************************************

#   techtree
    def init_structures(self,barra,builddura, size):
        self.routine = 'init_structures'
        self.log_fail((type(barra) == UnitTypeId),'')
        self.all_structures.append(barra)
        self.builddura_of_thing[barra] = builddura
        self.size_of_structure[barra] = size
        if barra not in (BARRACKSTECHLAB,FACTORYTECHLAB,STARPORTTECHLAB,PLANETARYFORTRESS,ORBITALCOMMAND):
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
#       pairs from cradle are also in techtree
        self.anything = set()
        for pair in self.techtree:
            something = pair[0]
            self.anything.add(something)
            something = pair[1]
            self.anything.add(something)

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


    def init_army(self,thing,time):
        if thing != SCV:
            self.all_army.append(thing)
        self.builddura_of_thing[thing] = time

    def init_upgrade(self,thing,time):
        self.all_upgrades.append(thing)
        self.builddura_of_thing[thing] = time


    def we_have_a(self,barra) -> bool:
#       only used in the techtree, so include flying and lowered buildings
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
                if barra == BARRACKS:
                    have = have or (len(self.structures(BARRACKSFLYING).ready) > 0)
                if barra == FACTORY:
                    have = have or (len(self.structures(FACTORYFLYING).ready) > 0)
                if barra == STARPORT:
                    have = have or (len(self.structures(STARPORTFLYING).ready) > 0)
                if barra == COMMANDCENTER:
                    have = have or (len(self.structures(COMMANDCENTERFLYING).ready) > 0)
                if barra == INFESTEDBARRACKS:
                    have = have or (len(self.structures(BARRACKS).ready) > 0)
                    have = have or (len(self.structures(BARRACKSFLYING).ready) > 0)
                if barra == INFESTEDFACTORY:
                    have = have or (len(self.structures(FACTORY).ready) > 0)
                    have = have or (len(self.structures(FACTORYFLYING).ready) > 0)
                if barra == INFESTEDBUNKER:
                    have = have or (len(self.structures(BUNKER).ready) > 0)
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
                if barra == BARRACKS:
                    have = have or (len(self.structures(BARRACKSFLYING)) > 0)
                if barra == FACTORY:
                    have = have or (len(self.structures(FACTORYFLYING)) > 0)
                if barra == STARPORT:
                    have = have or (len(self.structures(STARPORTFLYING)) > 0)
                if barra == COMMANDCENTER:
                    have = have or (len(self.structures(COMMANDCENTERFLYING)) > 0)
                if barra == INFESTEDBARRACKS:
                    have = have or (len(self.structures(BARRACKS)) > 0)
                    have = have or (len(self.structures(BARRACKSFLYING)) > 0)
                if barra == INFESTEDFACTORY:
                    have = have or (len(self.structures(FACTORY)) > 0)
                    have = have or (len(self.structures(FACTORYFLYING)) > 0)
                if barra == INFESTEDBUNKER:
                    have = have or (len(self.structures(BUNKER)) > 0)
    #               plans and building ones are included
                for scvt in self.structure_of_trabu_scvt:
                    have = have or (self.structure_of_trabu_scvt[scvt] == barra)
            else:
                have = (self.already_pending(barra) > 0.01) or (len(self.units(barra).ready) > 0)
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
                if barra == BARRACKS:
                    for bar in self.structures(BARRACKSFLYING):
                        positions.add(bar.position)
                if barra == FACTORY:
                    for bar in self.structures(FACTORYFLYING):
                        positions.add(bar.position)
                if barra == STARPORT:
                    for bar in self.structures(STARPORTFLYING):
                        positions.add(bar.position)
                if barra == COMMANDCENTER:
                    for bar in self.structures(COMMANDCENTERFLYING):
                        positions.add(bar.position)
                if barra == INFESTEDBARRACKS:
                    for bar in self.structures(BARRACKS):
                        positions.add(bar.position)
                    for bar in self.structures(BARRACKSFLYING):
                        positions.add(bar.position)
                if barra == INFESTEDFACTORY:
                    for bar in self.structures(FACTORY):
                        positions.add(bar.position)
                    for bar in self.structures(FACTORYFLYING):
                        positions.add(bar.position)
                if barra == INFESTEDBUNKER:
                    for bar in self.structures(BUNKER):
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


#*********************************************************************************************************************

#   money handling with reservations
    def get_cost(self,building) -> Dict[str,float]:
        if building == INFESTEDBARRACKS:
            return self.calculate_cost(BARRACKS)
        elif building == INFESTEDBUNKER:
            return self.calculate_cost(BUNKER)
        elif building == INFESTEDFACTORY:
            return self.calculate_cost(FACTORY)
        else:
           return self.calculate_cost(building)

    def can_pay(self,thing,urgent) -> bool:
        if urgent:
            cost = self.get_cost(thing)
            return (self.minerals >= cost.minerals) and (self.vespene >= cost.vespene)
        else:
            cost = self.get_cost(thing)
            return (self.minerals >= self.reserved_minerals+cost.minerals) and (self.vespene >= self.reserved_vespene+cost.vespene)

    def calc_reserved_money(self):
        self.reserved_minerals = 0
        self.reserved_vespene = 0
        for cct in self.ambition_of_strt:
            ambition = self.ambition_of_strt[cct]
            cost = self.get_cost(ambition)
            self.reserved_minerals = self.reserved_minerals + cost.minerals
            self.reserved_vespene = self.reserved_vespene + cost.vespene
        for scvt in self.all_scvt:
            if self.job_of_scvt[scvt] == 'traveller':
                building = self.structure_of_trabu_scvt[scvt]
                cost = self.get_cost(building)
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

#*********************************************************************************************************************

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
        for gas in self.vespene_geyser:
            here = gas.position
            layout_if.layout[round(here.x-1.5)][round(here.y-1.5)] = 1
            layout_if.layout[round(here.x-1.5)][round(here.y-0.5)] = 1
            layout_if.layout[round(here.x-1.5)][round(here.y+0.5)] = 1
            layout_if.layout[round(here.x-0.5)][round(here.y-1.5)] = 1
            layout_if.layout[round(here.x-0.5)][round(here.y-0.5)] = 1
            layout_if.layout[round(here.x-0.5)][round(here.y+0.5)] = 1
            layout_if.layout[round(here.x+0.5)][round(here.y-1.5)] = 1
            layout_if.layout[round(here.x+0.5)][round(here.y-0.5)] = 1
            layout_if.layout[round(here.x+0.5)][round(here.y+0.5)] = 1


#*********************************************************************************************************************

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

    def maxmimminers(self) -> int:
        return len(self.all_mimt) * 2

    def maxgasminers(self) -> int:
        return len(self.all_gast) * 3


    def mimminer_vacatures(self) -> int:
        return self.maxmimminers() - len(self.mimt_of_scvt)

    def gasminer_vacatures(self) -> int:
        return self.maxgasminers() - len(self.gast_of_scvt)



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



#*********************************************************************************************************************
#   timing routine
#   order = (thing,place)
#   starting from now, make a planning for buildorder
#   planning is time duration, from now to the startmoment of construction
#   that is useful to get builders in time at the buildsites
#   and useful for comparing buildorders
#   the planning should be somewhat accurate for small current_moment
#   the model should be fairly simple
#   E.g. changes in the amount of miners are not in the model
#
#   the planning does not wait for currently planned buildings to finish or even start-to-construct
#   the planning does respect the minerals etc for already planned buildings, those are reserved in advance
#   the finishmoment of already planned buildings is calculated and used for the techtree and the emerging free scv
#   the planning does start-to-construct in the order given in buildorder
#
#   IN:
#       the current game situation and administration, those are called the "situation".
#       buildorder [(BARRACKS,(16,40)),(SUPPLYDEPOT,(119,3)),(MARINE,(16,40)),...
#   OUT:
#       planning [(tagJohn,BARRACKS,(16,40),4,17,22)
#                ,(tagMohamad,SUPPLYDEPOT,(119,3),8,23,30)
#                ,(dummytag,MARINE,(16,40),220,220,265),...
#       The 3 moments are: start-walk, start-construct,end-construct
#       For not tobuildwalk constructions and trainings, start_walk==start_construct and the tag is dummytag
#   LOCAL:
#       current_moment 17
#       current_minerals 254
#       current_vespene 0
#       current_free {(tagjohn,pos(14,107),since15),...
#           using buildplan (tagjohn,thingBARRACKS,goal(16,40),startwalk14,startconstruct17,finish19)
#       current_running {buildplan,...
#       current_constructing {buildplan,...
#           using trainplan (thingMARINE,place(16,40),starttrain20,finish40)
#       current_training {trainplan, ...
#       current_thingkinds {thingBARRACKS,...    (finished ones)
#       current_buildings_and_parts {(thingBARRACKS,x115,y87),...     (started construction, or finished)
#       current_events {(17,'start to walk',tagjohn,goal(16,40))
#                      ,(4,'start to construct',tageddy,goal(119,3))
#                      ,(19,'finished construct',tagjohn,goal(16,40))
#                      ,(2,'finished train',goal(16,40))
#


    def get_situation(self):
        routine = 'get_situation'
        now = 0
        self.situation_minerals = self.minerals
        self.situation_vespene = self.vespene
        self.situation_running = set()
        self.situation_constructing = set()
        self.situation_training = set()
        self.situation_thingkinds = set()
        #   buildings are identified by place not tag, so we can add future buildings
        self.situation_buildings_and_parts = set()
        self.situation_events = set()
        self.fix_count_of_job()
        self.situation_mimminers = self.count_of_job['mimminer']
        self.situation_gasminers = self.count_of_job['gasminer']
#       For existing plans, the minerals etc are reserved in advance
#       The finish event gives an scv and a techtree thing.
        for scv in self.units(SCV):
            scvt = scv.tag
            if scvt in self.goal_of_trabu_scvt:
                goal = self.goal_of_trabu_scvt[scvt]
                thing = self.structure_of_trabu_scvt[scvt]
                pos = scv.position
                cost = self.get_cost(thing)
                # Reserved in advance. No problem if it becomes negative.
                self.situation_minerals = self.situation_minerals - cost.minerals
                self.situation_vespene = self.situation_vespene - cost.vespene
                build_dura = self.builddura_of_thing[thing]
                if self.job_of_scvt[scvt] == 'traveller':
                    walk_dura = self.dist(pos,goal) / self.walk_speed
                    finishmoment = now + walk_dura + build_dura
                elif self.job_of_scvt[scvt] == 'builder':
                    # for the small duration where the build hasn't started
                    finishmoment = now + build_dura
                    for thatone in self.structures(thing):
                        if thatone.position == goal:
                            # the build has started and is payed; undo the reserving
                            self.situation_minerals = self.situation_minerals + cost.minerals
                            self.situation_vespene = self.situation_vespene + cost.vespene
                            finishmoment = now + build_dura*(1.0-thatone.build_progress)
                            self.situation_buildings_and_parts.add((thing, goal.x, goal.y))
                buildplan = (scvt,thing,goal,-1,-1,finishmoment)
                self.situation_constructing.add(buildplan)
                self.situation_events.add((finishmoment,'finished construct',scvt,goal))
        # structures without tobuildwalk; techlab, pf, ...
        scvt = None
        for thing in self.all_structures:
            if thing not in self.all_structures_tobuildwalk:
                for thatone in self.structures(thing):
                    if thatone.build_progress < 1.0:
                        goal = thatone.position
                        build_dura = self.builddura_of_thing[thing]
                        finishmoment = now + build_dura * (1.0 - thatone.build_progress)
                        trainplan = (thing, goal, -1, finishmoment)
                        self.situation_training.add(trainplan)
                        self.situation_events.add((finishmoment, 'finished train', None, goal))
        # ambitions
        for strt in self.ambition_of_strt:
            thing = self.ambition_of_strt[strt]
            for crad in self.all_structures:
                for cradje in self. structures(crad):
                    if (cradje.tag == strt):
                        if thing in self.all_labs:
                            goal = Point2((cradje.position.x+2.5,cradje.position.y-0.5))
                        else:
                            goal = cradje.position
                        cost = self.get_cost(thing)
                        # Reserved in advance. No problem if it becomes negative.
                        self.situation_minerals = self.situation_minerals - cost.minerals
                        self.situation_vespene = self.situation_vespene - cost.vespene
                        build_dura = self.builddura_of_thing[thing]
                        if cradje.tag in self.idle_structure_tags:
                            to_free_dura = 0
                        else:
                            # todo
                            to_free_dura = 10
                        finishmoment = now + build_dura + to_free_dura
                        trainplan = (thing, goal, -1, finishmoment)
                        self.situation_training.add(trainplan)
                        self.situation_events.add((finishmoment, 'finished train', None, goal))
        # marine
        for thing in self.all_army:
            for thatone in self.units(thing):
                if thatone.build_progress < 1.0:
                    goal = thatone.position
                    build_dura = self.builddura_of_thing[thing]
                    finishmoment = now + build_dura * (1.0 - thatone.build_progress)
                    trainplan = (thing, goal, -1, finishmoment)
                    self.situation_training.add(trainplan)
                    self.situation_events.add((finishmoment, 'finished train', None, goal))
        # upgrades
        for upgr in self.all_upgrades:
            progress = self.already_pending_upgrade(upgr)
            if  (progress != 0.0) and (progress < 1.0):
                # get its place
                for pair in self.cradle:
                    if pair[0] == upgr:
                        crad = pair[1]
                        abi = sc2.dicts.unit_research_abilities.RESEARCH_INFO[crad][upgr]['ability']
                        for cradje in self.structures(crad).ready:
                            if cradje.is_using_ability == abi:
                                goal = cradje.position
                                finishmoment = now + self.builddura_of_thing[upgr] * (1.0 - progress)
                                trainplan = (upgr, goal, -1, finishmoment)
                                self.situation_training.add(trainplan)
                                self.situation_events.add((finishmoment, 'finished train', None, goal))
        # potential builders
        self.situation_free = set()
        for scv in self.units(SCV):
            scvt = scv.tag
            if scvt in self.all_scvt:
                if self.job_of_scvt[scvt] in ('gasminer', 'mimminer', 'applicant', 'idler', 'suicider', 'fleeer'):
                    self.situation_free.add((scvt,scv.position,now))
        # for the techtree:
        self.situation_thingkinds = set()
        for kind in self.anything:
            if self.we_have_a(kind):
                self.situation_thingkinds.add(kind)
        # to make marines:
        # include unfinished buildings    to prevent a short disappearance
        # a lab has its own position, not its cradle's.
        self.situation_buildings_and_parts = set()
        for thing in self.all_structures:
            for thatone in self.structures(thing):
                self.situation_buildings_and_parts.add((thing, thatone.position.x, thatone.position.y))


    def make_planning(self,extragas):
        # usually extragas = 0. Here you can experiment with an extra gasminer
        routine = 'make_planning'
        self.log_planning('++++++++++++++++++++++++++ starting a plan with '+str(extragas)+' extra gas.')
        self.planning = []
        # The situation is taken into current, which will shift during the look-ahead.
        current_minerals = self.situation_minerals
        current_vespene = self.situation_vespene
        current_running = self.situation_running.copy()
        current_constructing = self.situation_constructing.copy()
        current_training = self.situation_training.copy()
        current_thingkinds = self.situation_thingkinds.copy()
        current_buildings_and_parts = self.situation_buildings_and_parts.copy()
        current_events = self.situation_events.copy()
        current_mimminers = self.situation_mimminers-extragas
        current_gasminers = self.situation_gasminers+extragas
        current_free = self.situation_free.copy()
        now = 0
        current_moment = 0
#
        plannable = True
        for (beautiful_thing,beautiful_place) in self.buildorder:
            if plannable:
                # calculate times
                self.log_planning('Planning a '+beautiful_thing.name)
                cost = self.get_cost(beautiful_thing)
                build_dura = self.builddura_of_thing[beautiful_thing]
                total_dura = 0
    #           mim_dura
                mim_gap = cost.minerals - current_minerals
                if (mim_gap <= 0):
                    mim_dura = 0
                elif current_mimminers == 0:
                    mim_dura = 9999
                else:
                    mim_dura = mim_gap / (current_mimminers*self.mim_speed)
                total_dura = max(total_dura,mim_dura)
    #           gas_dura
                gas_gap = cost.vespene - current_vespene
                if (gas_gap <= 0):
                    gas_dura = 0
                elif current_gasminers == 0:
                    gas_dura = 9999
                else:
                    gas_dura = gas_gap / (current_gasminers*self.gas_speed)
                total_dura = max(total_dura, gas_dura)
#           tree_dura
                tree_dura = 0
                for pair in self.techtree:
                    if pair[0] == beautiful_thing:
                        barra = pair[1]
                        if barra not in current_thingkinds:
    #                       expect it to be started; the buildplan should respect the techtree
                            earliest = 9999
                            for (scvt,thing,goal,startwalk,startconstruct,finish) in current_constructing:
                                if thing == barra:
                                    if finish<earliest:
                                        earliest = finish
                            # and for techlab, pf, marine:
                            for (thing,goal,startconstruct,finish) in current_training:
                                if thing == barra:
                                    if finish<earliest:
                                        earliest = finish
                            dura = earliest - current_moment
                            tree_dura = max(tree_dura,dura)
                total_dura = max(total_dura,tree_dura)
    #           walk_dura
                if beautiful_thing in self.all_structures_tobuildwalk:
        #           find a beautiful scv
                    beautiful_scvt = self.dummytag
                    arrive_quality = 9999
                    for (scvt,pos,since) in current_free:
                        walk_dura = self.dist(pos,beautiful_place) / self.walk_speed
                        could_arrive = max(current_moment,(since + walk_dura))
        #               next costants weigh reusing an scv that has to walk a little versus getting a fresh scv from far
                        if self.job_of_scvt[scvt] == 'gasminer':
                            could_arrive_quality = could_arrive + 0.15*walk_dura
                        else:
                            could_arrive_quality = could_arrive + 0.1*walk_dura
                        if could_arrive_quality < arrive_quality:
                            arrive_quality = could_arrive_quality
                            beautiful_scvt = scvt
                    for (scvt,pos,since) in current_free:
                        if scvt == beautiful_scvt:
                            walk_dura = self.dist(pos, beautiful_place) / self.walk_speed
                            could_arrive = max(current_moment, (since + walk_dura))
                            travel_dura = could_arrive - current_moment
                else:
                    beautiful_scvt = self.dummytag
                    travel_dura = 0
                    walk_dura = 0
                total_dura = max(total_dura,travel_dura)
                # cradle_dura: how long to wait for a cradle to become idle
                cradle_dura = 0
                for pair in self.cradle:
                    if pair[0] == beautiful_thing:
                        cradle = pair[1]
                        cradle_dura = 9999
                        for (th,x,y) in current_buildings_and_parts:
                            if th == cradle:
                                maxfinish = 0
                                for (scvt, thi, goal, startwalk, startconstruct, finish) in current_constructing:
                                    if (thi == cradle) and (goal.x == x) and (goal.y == y):
                                        maxfinish = max(maxfinish,finish)
                                # it can be in training
                                for (thi,goal,start,finish) in current_training:
                                    if (goal.x==x) and (goal.y==y):
                                        maxfinish = max(maxfinish,finish)
                                    if (thi in self.all_labs) and (goal.x == x+2.5) and (goal.y == y-0.5):
                                        maxfinish = max(maxfinish, finish)
                                this_cradle_dura = maxfinish - current_moment
                                cradle_dura = min(cradle_dura,this_cradle_dura)
                        # there could be some in the running phase, not in current_buildings_and_parts
                        for (scvt, th, goal, startwalk, startconstruct, finish) in current_running:
                            if th == cradle:
                                maxfinish = finish
                                # it can be in training
                                for (thi,traingoal,start,finish2) in current_training:
                                    if (traingoal == goal):
                                        maxfinish = max(maxfinish,finish2)
                                    if (thi in self.all_labs) and (traingoal.x == x + 2.5) and (traingoal.y == y - 0.5):
                                        maxfinish = max(maxfinish, finish2)
                                this_cradle_dura = maxfinish - current_moment
                                cradle_dura = min(cradle_dura,this_cradle_dura)
                total_dura = max(total_dura,cradle_dura)
                if total_dura == 0:
                    self.log_planning('bound by buildorder')
                else:
                    if total_dura == travel_dura:
                        self.log_planning('bound by travel')
                    if total_dura == mim_dura:
                        self.log_planning('bound by minerals')
                    if total_dura == gas_dura:
                        self.log_planning('bound by gas')
                    if total_dura == tree_dura:
                        self.log_planning('bound by techtree')
                    if total_dura == cradle_dura:
                        self.log_planning('bound by cradle')
                plan_moment = current_moment + total_dura
                if plan_moment > 8888:
                    plannable = False
                    self.log_planning('Planning failed')
                else:
                    self.log_planning('at '+str(round(plan_moment*10)/10))
                    if beautiful_thing in self.all_structures_tobuildwalk:
                        beautiful_buildplan = (beautiful_scvt,beautiful_thing,beautiful_place,plan_moment - walk_dura,plan_moment,plan_moment + build_dura)
                        current_events.add((plan_moment - walk_dura,'start to walk',beautiful_scvt,beautiful_place))
                        current_events.add((plan_moment,'start to construct',beautiful_scvt,beautiful_place))
                        current_events.add((plan_moment + build_dura,'finished construct',beautiful_scvt,beautiful_place))
                    else:
                        # marine,pf,lab,upgrade
                        beautiful_buildplan = (self.dummytag,beautiful_thing,beautiful_place,plan_moment,plan_moment,plan_moment + build_dura)
                        beautiful_trainplan = (beautiful_thing,beautiful_place,plan_moment,plan_moment + build_dura)
                        current_events.add((plan_moment, 'start to train', self.dummytag, beautiful_place))
                        current_events.add((plan_moment + build_dura, 'finished train', self.dummytag, beautiful_place))
                        # forward the time to "start to construct"
                    self.planning.append(beautiful_buildplan)
                    self.log_buildplan(beautiful_buildplan)
                    at_construction_start = False
                    while not at_construction_start:
                        nextmoment = 9999
                        for (moment,stri,scvt,goal) in current_events:
                            if (moment<nextmoment):
                                nextmoment = moment
                        # happen all events at nextmoment
                        # in the order: finish, start run, start build
                        del_current_events = set()
                        for (moment, stri, escvt, egoal) in current_events:
                            if (moment == nextmoment) and (stri == 'finished train'):
                                del_current_events.add((moment, stri, escvt, egoal))
                                del_current_training = set()
                                for trainplan in current_training:
                                    (thing, goal, starttrain, finish) = trainplan
                                    if (goal == egoal) and (moment == finish):
                                        del_current_training.add(trainplan)
                                        current_thingkinds.add(thing)
                                current_training = current_training - del_current_training
                        for (moment, stri, escvt, egoal) in current_events:
                            if (moment == nextmoment) and (stri == 'finished construct'):
                                del_current_events.add((moment, stri, escvt, egoal))
                                del_current_constructing = set()
                                for buildplan in current_constructing:
                                    (tag, thing, goal, startwalk,startconstruct,finish) = buildplan
                                    if (tag == escvt) and (goal == egoal) and (moment == finish):
                                        del_current_constructing.add(buildplan)
                                        current_free.add((tag,goal,finish))
                                        current_thingkinds.add(thing)
                                current_constructing = current_constructing - del_current_constructing
                        for (moment,stri,escvt,egoal) in current_events:
                            if (moment == nextmoment) and (stri == 'start to walk'):
                                del_current_events.add((moment,stri,escvt,egoal))
                                del_current_free = set()
                                for (tag, position, since) in current_free:
                                    if tag == escvt:
                                        del_current_free.add((tag, position, since))
                                        current_running.add(beautiful_buildplan)
                                current_free = current_free - del_current_free
                        for (moment, stri, escvt, egoal) in current_events:
                            if (moment == nextmoment) and (stri == 'start to construct'):
                                del_current_events.add((moment, stri, escvt, egoal))
                                # that must be the beautiful building, as the build has an order
                                at_construction_start = True
                                current_minerals = current_minerals - cost.minerals
                                current_vespene = current_vespene - cost.vespene
                                current_running.remove(beautiful_buildplan)
                                current_constructing.add(beautiful_buildplan)
                                current_buildings_and_parts.add((beautiful_thing, beautiful_place.x, beautiful_place.y))
                        for (moment, stri, escvt, egoal) in current_events:
                            if (moment == nextmoment) and (stri == 'start to train'):
                                del_current_events.add((moment, stri, escvt, egoal))
                                # that must be the beautiful marine, as the build has an order
                                at_construction_start = True
                                current_minerals = current_minerals - cost.minerals
                                current_vespene = current_vespene - cost.vespene
                                current_training.add(beautiful_trainplan)
                                # it could be a techlab or pf
                                if beautiful_thing in self.all_structures:
                                    current_buildings_and_parts.add((beautiful_thing, beautiful_place.x, beautiful_place.y))
                        current_events = current_events - del_current_events
    #               grow
                    dura = plan_moment - current_moment
                    current_minerals = current_minerals+dura*(current_mimminers*self.mim_speed)
                    current_vespene = current_vespene+dura*(current_gasminers*self.gas_speed)
                    current_moment = plan_moment


    def optimize_buildorder(self):
        # in: buildorder
        # out: buildorder
        routine = 'optimize_buildorder'
        self.get_situation()
        # experiment with extra gas
        if (self.situation_mimminers>0) and (self.situation_gasminers>0):
            self.make_planning(0)
            endtime0 = 0
            items0 = len(self.planning)
            for (scvt, thing, goal, sw, sc, finish) in self.planning:
                endtime0 = max(endtime0, finish)
            self.make_planning(1)
            endtime1 = 0
            items1 = len(self.planning)
            for (scvt,thing, goal, sw,sc,finish) in self.planning:
                endtime1 = max(endtime1,finish)
            self.make_planning(-1)
            endtimeneg = 0
            itemsneg = len(self.planning)
            for (scvt,thing, goal, sw,sc,finish) in self.planning:
                endtimeneg = max(endtimeneg,finish)
        # maybe more gas
        if (self.situation_mimminers > 0) and (self.situation_gasminers > 0):
            if (endtime1 < endtime0) and (items1 == items0):
                self.gas_advice = 1
            elif (endtimeneg < endtime0) and (itemsneg == items0):
                self.gas_advice = -1


#*********************************************************************************************************************

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


#*********************************************************************************************************************

    def find_tobuildwalk_a_place(self,building) -> bool:
        self.routine = 'find_tobuildwalk_a_place'
        self.log_placing(building.name)
#       get a random place
#       if no place could be found, return False
        # TODO adapt this routine for planning far ahead.
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
            places = []
            for gey in self.vespene_geyser:
                place = gey.position
                if self.check_layout(building, place):
                    for cc in self.all_bases:
                        if self.near(place,cc.position,12):
                            if place not in self.goal_of_trabu_scvt.values():
                                places.append(place)
            if len(places) > 0:
                place = random.choice(places)
                found = True
        elif building in self.all_structures_tobuildwalk:
#           normal building
            if len(self.all_bases) > 0:
                found = False
                while not found:
                    cc = random.choice(self.all_bases)
                    dist = 6
                    if building == MISSILETURRET:
                        dist = random.randrange(-10,10) 
                    fixplace = cc.position.towards(self.game_info.map_center, dist)
                    self.put_on_the_grid(building,fixplace)
                    fixplace = self.function_result_Point2
                    place = fixplace
                    while not self.check_layout(building,place):
                        x = fixplace.x+random.randrange(-8,8)
                        y = fixplace.y+random.randrange(-8,8)
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
            self.log_placing('using a soft placement tip')
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
                            self.log_placing('using a hard placement tip')
                            found = True
#       
        if found:
            self.function_result_Point2 = place
        else:
            self.log_placing('not found')
        return found 


    #*********************************************************************************************************************

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
#   bestbctag is dummytag or a tag of a living battlecruiser
        just_one_bctag = self.dummytag
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


#*********************************************************************************************************************

#   mid_game
    async def mid_game(self,thing,amount):
        self.routine = 'mid_game'
        self.endwish_am_of_th[thing] = amount
        if thing in self.wish_am_of_th:
            self.wish_am_of_th[thing] = max(self.wish_am_of_th[thing],amount)
        else:
            self.wish_am_of_th[thing] = amount
            if thing in (INFESTEDBARRACKS,INFESTEDBUNKER,INFESTEDFACTORY):
                self.wish_pri_of_th[thing] = 10
            else:
                self.wish_pri_of_th[thing] = 0
        self.log_wish('wishing '+thing.name+' '+str(amount))
        stable = False
        while not stable:
            stable = True
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


#*********************************************************************************************************************


    def blunt_to_buildseries(self,thing):
        if self.check_maxam(thing):
#           this time, no doubles. This still enables building mutiple ships at a moment.
            if thing not in self.buildseries:
                if self.check_techtree(thing):
                    self.buildseries.append(thing)


    def init_mid_game(self):
        # wish_am_of_th and pri are put in a buildseries
        # subtract started things from the amount
        self.buildseries = []
        maxpri = 0
        for th in self.wish_pri_of_th:
            pri = self.wish_pri_of_th[th]
            maxpri = max(maxpri, pri)
        while maxpri >= 0:
            for th in self.wish_pri_of_th:
                pri = self.wish_pri_of_th[th]
                am = self.wish_am_of_th[th]
                if pri == maxpri:
                    am = am - self.we_started_amount(th)
                    while am > 0:
                        self.buildseries.append(th)
                        am = am - 1
            maxpri = maxpri - 1
        # the buildseries has a crude executable order


    def make_buildorder_to_execute(self):
        # cut off a dream at the loss of a structure
        if len(self.structures) < self.but_i_had_structures:
            self. log_success('$$$$$$$ lost a building; breaking off the buildorder_to_execute')
            self.buildorder_to_execute = []
        self.but_i_had_structures = len(self.structures)
        # first make buildseries
        miners = self.count_of_job['mimminer']
        if (len(self.buildorder_to_execute) == 0) and (miners>0):
            if self.game_phase == 'init':
                self.game_phase = 'opening'
                self.log_success('============================================================ opening =========')
            elif self.game_phase == 'opening':
                self.game_phase = 'mid_game'
                self.log_success('============================================================ mid_game ======')
            elif self.game_phase == 'mid_game':
                self.game_phase = 'late_game'
                self.log_success('============================================================ late_game =======')
            # make buildseries
            if (self.game_phase == 'opening'):
                self.buildseries = self.buildseries_opening
            elif (self.game_phase == 'mid_game'):
                self.init_mid_game()
            elif (self.game_phase == 'late_game'):
                self.buildseries = []
                # late_game
                # advice on stuck situations
                # the order of these advices matters.
                scvs = len(self.units(SCV))
                # supplydepots elsewhere
                wanted_ccs = 1+(scvs+7)//22
                if (self.we_started_amount(COMMANDCENTER)+self.structures(PLANETARYFORTRESS).amount\
                +self.structures(ORBITALCOMMAND).amount < wanted_ccs):
                    self.blunt_to_buildseries(COMMANDCENTER)
                if (len(self.structures(STARPORT).ready.idle)>0):
                    self.blunt_to_buildseries(BATTLECRUISER)
                if (len(self.structures(FUSIONCORE))==0):
                    self.blunt_to_buildseries(FUSIONCORE)
                if (len(self.structures(STARPORT))==0):
                    self.blunt_to_buildseries(STARPORT)
                if (len(self.structures(FACTORY))==0):
                    self.blunt_to_buildseries(FACTORY)
                if (len(self.structures(BARRACKS))==0):
                    self.blunt_to_buildseries(BARRACKS)
                if (len(self.structures(SUPPLYDEPOT))==0):
                    self.blunt_to_buildseries(SUPPLYDEPOT)
                for sp in self.structures(STARPORT).ready:
                    if not sp.has_add_on:
                        self.blunt_to_buildseries(STARPORTTECHLAB)
                if (self.minerals > 500) and (self.vespene < self.minerals-500):
                    self.blunt_to_buildseries(REFINERY)
                vikings = 0
                for ene in self.enemy_units:
                    if (ene.type_id in self.viking_targets) and (ene.type_id != OVERLORD):
                        vikings = vikings+1
                if self.units(VIKINGFIGHTER).amount < vikings:
                    self.blunt_to_buildseries(VIKINGFIGHTER)
                if (self.minerals-self.reserved_minerals > 1500):
                    self.blunt_to_buildseries(PLANETARYFORTRESS)
                    self.blunt_to_buildseries(COMMANDCENTER)
                    self.blunt_to_buildseries(MISSILETURRET)
                    self.blunt_to_buildseries(STARPORT)
                if (self.supply_used<120):
                    self.blunt_to_buildseries(SIEGETANK)
                if (len(self.structures(STARPORT).ready.idle)==0) and (len(self.structures(FUSIONCORE).ready)>0) \
                and (STARPORT not in self.structure_of_trabu_scvt.values()):
                    self.blunt_to_buildseries(STARPORT)
                if (not self.we_started_a(MISSILETURRET)) or (self.supply_used>130):
                    self.blunt_to_buildseries(MISSILETURRET)
                if (not self.we_started_a(ENGINEERINGBAY)) and (self.supply_used>40):
                    self.blunt_to_buildseries(ENGINEERINGBAY)
                if (self.supply_army*3 < self.supply_used):
                    self.blunt_to_buildseries(MARINE)
                if not self.we_started_a(FACTORYTECHLAB):
                    for sp in self.structures(FACTORY).ready:
                        if not sp.has_add_on:
                            self.blunt_to_buildseries(FACTORYTECHLAB)
                if (self.we_started_amount(BATTLECRUISER) >= 4):
                    self.blunt_to_buildseries(RAVEN)
                if (self.we_started_amount(BATTLECRUISER) >= 3):
                    self.blunt_to_buildseries(ARMORY)
                    self.blunt_to_buildseries(BATTLECRUISERENABLESPECIALIZATIONS)
                if (len(self.structures(ARMORY).ready.idle) > 0):
                    for pair in self.cradle:
                        if pair[1] == ARMORY:
                            self.blunt_to_buildseries(pair[0])
            # buildseries is made.
            stri = ''
            for thing in self.buildseries:
                stri = stri+' '+thing.name
            self.log_buildseries(stri)
            # immediately fix the positions. Do this only once.
            self.buildorder_from_buildseries()
            self.optimize_buildorder()
            self.buildorder_to_execute = self.buildorder.copy()
            self.get_situation()
            self.make_planning(0)
            self.executive = self.planning.copy()


# *********************************************************************************************************************



    def buildorder_from_buildseries(self):
        # buildorder = buildseries + place
        self.routine = 'buildorder_from_buildseries'
        self.buildorder = []
        for thing in self.buildseries:
            if thing in self.all_structures_tobuildwalk:
                if self.find_tobuildwalk_a_place(thing):
                    goal = self.function_result_Point2
                    self.buildorder.append((thing, goal))
                    self.write_layout(thing, goal)
                    print('buildorder '+thing.name)
            else:
                # e.g. a marine. Its cradle is a barracks
                for pair in self.cradle:
                    if pair[0] == thing:
                        crad = pair[1]
                # crad could exist, or be ordered, or be in the buildorder
                crad_places = set()
                for str in self.structures(crad):
                    crad_places.add(str.position)
                for scvt in self.goal_of_trabu_scvt:
                    if self.structure_of_trabu_scvt[scvt] == crad:
                        crad_places.add(self.goal_of_trabu_scvt[scvt])
                for (otherthing,goal) in self.buildorder:
                    if otherthing == crad:
                        crad_places.add(goal)
                if thing == MARINE:
                    crad = INFESTEDBARRACKS
                    for (otherthing,goal) in self.buildorder:
                        if otherthing == crad:
                            crad_places.add(goal)
                if thing == HELLION:
                    crad = INFESTEDFACTORY
                    for (otherthing,goal) in self.buildorder:
                        if otherthing == crad:
                            crad_places.add(goal)
                # get a random cradle place
                # be aware later that this is not optimal
                if len(crad_places)==0:
                    print('could not place '+thing.name)
                    place = self.nowhere
                else:
                    place = random.sample(crad_places,1)[0]
                if thing in self.all_labs:
                    place = Point2((place.x+2.5,place.y-0.5))
                self.buildorder.append((thing, place))
                print('buildorder ' + thing.name)


    async def follow_executive(self):
        self.routine = 'follow_executive'
        needs_new_planning = False
        done_executive = []
        done_buildorder_to_execute = []
        for bp in self.executive:
            (scvt, thing, place, sr, sc, fi) = bp
            tp = (thing,place)
            if thing in self.all_structures_tobuildwalk:
                if sr == 0:
                    if await self.build_thing_towalk(scvt,thing, place):
                        done_executive.append(bp)
                        done_buildorder_to_execute.append(tp)
                        needs_new_planning = True
            else:
                if sc == 0:
                    if await self.build_thing(thing, place):
                        # for a lab, the labplace is given
                        done_executive.append(bp)
                        done_buildorder_to_execute.append(tp)
                        needs_new_planning = True
        for bp in done_executive:
            del self.executive[self.executive.index(bp)]
        for tp in done_buildorder_to_execute:
            del self.buildorder_to_execute[self.buildorder_to_execute.index(tp)]
        if needs_new_planning:
            self.buildorder = self.buildorder_to_execute.copy()
            self.get_situation()
            self.make_planning(0)
            self.executive = self.planning.copy()


    async def supply_depots_adlib(self):
        if (self.supply_left < 2 + self.supply_used // 6) and (self.supply_cap < 200):
            if (SUPPLYDEPOT not in self.structure_of_trabu_scvt.values()):
                if self.game_phase in ('mid_game','late_game'):
                    if self.find_tobuildwalk_a_place(SUPPLYDEPOT):
                        place = self.function_result_Point2
                        scvt = self.get_near_scvt_to_goodjob(place)
                        if await self.build_thing_towalk(scvt, SUPPLYDEPOT, place):
                            print('built extra supplydepot')

    #*********************************************************************************************************************


    async def build_thing_towalk(self,scvt,thing,place) -> bool:
#       print('DEBUG trying to build '+thing.name)
        self.routine = 'build_thing_towalk'
        if thing == COMMANDCENTER:
            didit = await self.build_commandcenter(scvt,place)
        elif thing in self.all_structures_tobuildwalk:
            didit = await self.build_building(scvt,thing,place) 
            if thing == INFESTEDBARRACKS:
                self.infestedbarracks_build_position = place
            elif thing == INFESTEDFACTORY:
                self.infestedfactory_build_position = place
        return didit

    async def build_thing(self,thing,place) -> bool:
#       print('DEBUG trying to build '+thing.name)
        # the place is an advice
        self.routine = 'build_thing'
        if thing in self.all_structures:
            didit = await self.enlarge_building(thing,place)
        elif type(thing) == UpgradeId:
            didit = await self.do_upgrade(thing,place)
        else:
            didit = await self.build_army(thing,place)
        return didit




    async def build_army(self,ship,dockpos) -> bool:
        # the dock is an advice, other ones can be used
        self.routine = 'build_army'
        didit = False
        if self.check_techtree(ship):
            if self.can_pay(ship,False):
                if self.supply_left >= 6:
                    todo = 1
                    for pair in self.cradle:
                        if pair[0] == ship:
                            hangar = pair[1]
                            for sp in self.structures(hangar).ready:
                                if sp.tag in self.idle_structure_tags:
                                    if (sp.has_add_on) or (ship in (MARINE,HELLION)):
                                        if sp.tag not in self.ambition_of_strt:
                                            if todo>0:
                                                if sp.position == dockpos:
                                                    todo = todo-1
                                                    self.log_success(ship.name)
                                                    self.log_command(hangar.name+'.train('+ship.name+')')
                                                    sp.train(ship)
                                                    self.idle_structure_tags.remove(sp.tag)
                                                    didit = True
                    for pair in self.cradle:
                        if pair[0] == ship:
                            hangar = pair[1]
                            for sp in self.structures(hangar).ready:
                                if sp.tag in self.idle_structure_tags:
                                    if (sp.has_add_on) or (ship in (MARINE,HELLION)):
                                        if sp.tag not in self.ambition_of_strt:
                                            if todo>0:
                                                todo = todo-1
                                                self.log_success(ship.name)
                                                self.log_command(hangar.name + '.train(' + ship.name + ')')
                                                sp.train(ship)
                                                self.idle_structure_tags.remove(sp.tag)
                                                didit = True
                                                self.rarely_executed_code()
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
                                               self.log_command('scv.build_gas(gey)')
                                               if scv.build_gas(gey):
                                                   self.log_workers('begun     '+building.name+' '+self.name(scvt))
                                    elif building == INFESTEDBARRACKS:
                                        self.log_command('scv.build(BARRACKS,goal)')
                                        if scv.build(BARRACKS, goal):
                                            self.log_workers('begun     ' + building.name + ' ' + self.name(scvt))
                                    elif building == INFESTEDBUNKER:
                                        self.log_command('scv.build(BUNKER,goal)')
                                        if scv.build(BUNKER, goal):
                                            self.log_workers('begun     ' + building.name + ' ' + self.name(scvt))
                                    elif building == INFESTEDFACTORY:
                                        self.log_command('scv.build(FACTORY,goal)')
                                        if scv.build(FACTORY, goal):
                                            self.log_workers('begun     ' + building.name + ' ' + self.name(scvt))
                                    else:
                                        self.log_command('scv.build('+building.name+',goal)')
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
                                self.log_command(oldbuilding.name+'.train('+newbuilding.name+')')
                                oldbuilding.train(newbuilding)
                                self.calc_reserved_money()
                                self.idle_structure_tags.remove(oldbuilding.tag)



    async def build_building(self,scvt,building,goal) -> bool:
        self.routine = 'build_building'
#       for tobuildwalk buildings except COMMANDCENTER
        didit = False
#       you do not have to wait for minerals and techtree
        if (self.check_future_techtree(building)) or (self.game_phase == 'opening'):
            for scv in self.units(SCV):
                if scv.tag == scvt:
                    self.goal_of_trabu_scvt[scvt] = goal
                    self.structure_of_trabu_scvt[scvt] = building
#                           best to stop the scv from mining, for if the build does not start, it remains in old function
                    if scv.is_collecting:
                        self.log_command('scv(Ability.STOP)')
                        scv(AbilityId.STOP)
                    self.job_of_scvt[scvt] = 'traveller'
                    self.promotionsite_of_scvt[scvt] = scv.position
                    self.log_workers('planning  '+building.name+' '+self.name(scvt))
                    self.log_command('scv(AbilityId.MOVE_MOVE,goal)')
                    if scv(AbilityId.MOVE_MOVE,goal):
                        self.log_workers('ordered   '+building.name+' '+self.name(scvt))
                    self.calc_reserved_money()
                    didit = True
        return didit



    async def build_commandcenter(self,trabu_scvt,goal) -> bool:
        self.routine = 'build_commandcenter'
        didit = False
        building = COMMANDCENTER
#       you do not have to wait for minerals and techtree
        scvt = self.get_near_scvt_to_goodjob(goal)
        for scv in self.units(SCV):
            if scv.tag == scvt:
                job = self.job_of_scvt[scvt]
                self.job_of_scvt[scvt] = 'escorter'
                self.promotionsite_of_scvt[scvt] = scv.position
                self.log_command('scv.build(BARRACKS,goal)')
                self.log_workers(job+' became escorter '+self.name(scvt))
                self.log_command('scv.attack(goal)')
                scv.attack(goal)
        if len(self.units(MARINE).ready) > 0:
            marin = random.choice(self.units(MARINE).ready)
            self.log_command('marin.attack(goal)')
            marin.attack(goal)
        if len(self.units(MARAUDER).ready) > 0:
            marau = random.choice(self.units(MARAUDER).ready)
            self.log_command('marau.attack(goal)')
            marau.attack(goal)
        scvt = trabu_scvt
        for scv in self.units(SCV):
            if scv.tag == scvt:
                self.goal_of_trabu_scvt[scvt] = goal
                self.structure_of_trabu_scvt[scvt] = building
                job = self.job_of_scvt[scvt]
                self.job_of_scvt[scvt] = 'traveller'
                self.promotionsite_of_scvt[scvt] = scv.position
                self.log_workers(job+' became traveller '+self.name(scvt))
                self.log_command('scv(AbilityId.MOVE_MOVE,goal)')
                scv(AbilityId.MOVE_MOVE, goal)
                self.calc_reserved_money()
        didit = True
        return didit



    async def enlarge_building(self,ambition,place) -> bool:
        # lab, pf
        # puts a building in ambition_of_strt, then it will become idle, then be transformed
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
                    # for a lab, the motherbuilding get the ambition
                    labpos = Point2((cc.position.x+2.5,cc.position.y-0.5))
                    if (ambition in self.all_labs) and (labpos == place):
                        if cc.tag not in self.ambition_of_strt:
                            self.ambition_of_strt[cc.tag] = ambition
                            self.calc_reserved_money()
                            didit = True
        return didit


    async def do_upgrade(self,upg,place):
        # the place is an advice
        self.routine = 'do_upgrade'
        didit = False
        # bug on COMBATSHIELD
        if type(upg) == UpgradeId:
            if self.already_pending_upgrade(upg) == 0:
                if self.check_techtree(upg):
                    for pair in self.cradle:
                        if pair[0] == upg:
                            cra = pair[1]
                            for ar in self.structures(cra).ready:
                                if (ar.position == place) and (ar.tag in self.idle_structure_tags):
                                    if self.can_pay(upg,False) or self.bug_can_pay(upg,False):
                                        if not didit:
                                            didit = True
                                            self.log_success(upg.name)
    #                                       circumvent some bugs
                                            if upg == TERRANVEHICLEANDSHIPARMORSLEVEL1:
                                                self.log_command('ar(AbilityId.ARMORYRESEARCH_TERRANVEHICLEANDSHIPPLATINGLEVEL1)')
                                                ar(AbilityId.ARMORYRESEARCH_TERRANVEHICLEANDSHIPPLATINGLEVEL1)
                                            elif upg == TERRANVEHICLEANDSHIPARMORSLEVEL2:
                                                self.log_command('ar(AbilityId.ARMORYRESEARCH_TERRANVEHICLEANDSHIPPLATINGLEVEL2)')
                                                ar(AbilityId.ARMORYRESEARCH_TERRANVEHICLEANDSHIPPLATINGLEVEL2)
                                            elif upg == TERRANVEHICLEANDSHIPARMORSLEVEL3:
                                                self.log_command('ar(AbilityId.ARMORYRESEARCH_TERRANVEHICLEANDSHIPPLATINGLEVEL3)')
                                                ar(AbilityId.ARMORYRESEARCH_TERRANVEHICLEANDSHIPPLATINGLEVEL3)
                                            else:
                                                self.log_command('ar.resrarch('+upg.name+')')
                                                ar.research(upg)
                                            self.idle_structure_tags.remove(ar.tag)
                            for ar in self.structures(cra).ready:
                                if (ar.tag in self.idle_structure_tags):
                                    if self.can_pay(upg, False) or self.bug_can_pay(upg, False):
                                        if not didit:
                                            didit = True
                                            self.log_success(upg.name)
                                            #                                       circumvent some bugs
                                            if upg == TERRANVEHICLEANDSHIPARMORSLEVEL1:
                                                self.log_command(
                                                    'ar(AbilityId.ARMORYRESEARCH_TERRANVEHICLEANDSHIPPLATINGLEVEL1)')
                                                ar(AbilityId.ARMORYRESEARCH_TERRANVEHICLEANDSHIPPLATINGLEVEL1)
                                            elif upg == TERRANVEHICLEANDSHIPARMORSLEVEL2:
                                                self.log_command(
                                                    'ar(AbilityId.ARMORYRESEARCH_TERRANVEHICLEANDSHIPPLATINGLEVEL2)')
                                                ar(AbilityId.ARMORYRESEARCH_TERRANVEHICLEANDSHIPPLATINGLEVEL2)
                                            elif upg == TERRANVEHICLEANDSHIPARMORSLEVEL3:
                                                self.log_command(
                                                    'ar(AbilityId.ARMORYRESEARCH_TERRANVEHICLEANDSHIPPLATINGLEVEL3)')
                                                ar(AbilityId.ARMORYRESEARCH_TERRANVEHICLEANDSHIPPLATINGLEVEL3)
                                            else:
                                                self.log_command('ar.resrarch(' + upg.name + ')')
                                                ar.research(upg)
                                            self.idle_structure_tags.remove(ar.tag)
        return didit


#*********************************************************************************************************************
#   army movement routines

    def close_to_a_my_base(self,pos) -> bool:
        clos = False
        for tow in self.all_bases:
            clos = clos or self.near(tow.position,pos,20)
        return clos

    def locally_improved(self,place) -> Point2:
#       verhoog quality met 400 pogingen in de omgeving (maxdist 3)
        bestplace = place
        qual = self.quality_of_army_position(place)
        for dx in range(-10,10):
            for dy in range(-10,10):
                altplace = Point2((place.x + dx/3, place.y + dy/3))
                altqual = self.quality_of_army_position(altplace)
                if altqual > qual:
                    bestplace = altplace
                    qual = altqual
        return bestplace


    def quality_of_army_position(self,point) -> int:
#       0=bad, 10= very good, >5 is acceptable
        qual = 0
        if self.attack_type == 'center':
            if self.near(point,self.army_center_point,10):
                qual = 10
        elif self.attack_type == 'arc':
            if self.near(point,self.enemyloc,100) and (not self.near(point,self.enemyloc,80)):
                qual = 10
        elif self.attack_type == 'jumpy':
#           bc.radius+bc.ground_range+hatchery.radius  estimate
            if self.near(point,self.enemy_target_base_loc,10):
                qual = 10
                for ene in self.enemy_units:
                    if ene.type_id in (MISSILETURRET,PHOTONCANNON,SPORECRAWLER):
#                       bc.radius+spore.air_range+spore.radius   estimate
                        if self.near(point,ene.position,8):
                            qual = qual-1
        return qual

    async def attack(self):
        self.routine = 'attack'
        if self.attack_type == 'jumpy':
            for bc in self.units(BATTLECRUISER).ready.idle:
                if self.quality_of_army_position(bc.position) > 5:
                    if bc.tag in self.frozenbctags:
                        seen = False
                        for ene in self.enemy_units:
                            if self.near(bc.position, ene.position, 7):
                                seen = True
                        for ene in self.enemy_structures:
                            if self.near(bc.position, ene.position, 7):
                                seen = True
                        if not seen:
                            self.log_command('bc(AbilityId.STOP)')
                            bc(AbilityId.STOP)
                            self.frozenbctags.remove(bc.tag)
                            tp = Point2((random.randrange(self.map_left, self.map_right),random.randrange(self.map_bottom, self.map_top)))
                            self.log_command('bc.attack(tp)')
                            bc.attack(tp)
                    else:
                        altpos = self.locally_improved(bc.position)
                        if altpos == bc.position:
                            self.log_army('holding bc there')
                            self.log_command('bc(AbilityId.HOLDPOSITION_BATTLECRUISER)')
                            bc(AbilityId.HOLDPOSITION_BATTLECRUISER)
                            self.frozenbctags.add(bc.tag)
                        else:
                            self.log_command('bc(MOVE_MOVE,altpos)')
                            bc(MOVE_MOVE,altpos)
            for bc in self.units(BATTLECRUISER).ready.idle:
                if self.quality_of_army_position(bc.position) <= 5:
                    if bc.tag not in self.bct_in_repair:
                        qual = 0
                        while qual <= 5:
                            place = Point2((random.randrange(self.map_left,self.map_right),random.randrange(self.map_bottom,self.map_top)))
                            qual = self.quality_of_army_position(place)
                        place = self.locally_improved(place)
                        abilities = (await self.get_available_abilities([bc]))[0]
                        if AbilityId.EFFECT_TACTICALJUMP in abilities:
                            self.log_command('bc(AbilityId.EFFECT_TACTICALJUMP,place)')
                            bc(AbilityId.EFFECT_TACTICALJUMP,place)
                            self.log_army('jumping in a bc')
                        else:
                            self.log_command('bc.move(place)')
                            bc.move(place)
                            self.log_army('moving in with a bc')
            tp = Point2((random.randrange(self.map_left,self.map_right),random.randrange(self.map_bottom,self.map_top)))
        elif self.attack_type == 'chaos':
            tp = Point2((random.randrange(self.map_left,self.map_right),random.randrange(self.map_bottom,self.map_top)))
        elif self.attack_type == 'arc':
            tp = Point2((random.randrange(self.map_left,self.map_right),random.randrange(self.map_bottom,self.map_top)))
            while self.quality_of_army_position(tp) <= 5:
                tp = Point2((random.randrange(self.map_left,self.map_right),random.randrange(self.map_bottom,self.map_top)))
        elif self.attack_type == 'arcpoint':
            tp = self.enemy_target_base_loc
        elif self.attack_type == 'center':
            tp = self.army_center_point
        elif self.attack_type == 'centerpoint':
            tp = self.enemy_target_base_loc
        sent = 0
        for srt in [BATTLECRUISER,MARINE,MARAUDER]:
            if (self.attack_type != 'jumpy') or (srt != BATTLECRUISER):
                for ar in self.units(srt).ready.idle:
                    if not (ar.tag in self.bct_in_repair):
                        if self.quality_of_army_position(ar.position) <= 5:
                            sent = sent + 1
                            self.log_command(srt.name+'.attack(tp)')
                            ar.attack(tp)
        if sent > 0:
            self.log_army(' with '+str(sent))
#       
#       attack_type changes
        it_changed = False
        if self.attack_type == 'jumpy':
            if (self.cruisercount<self.lastcruisercount) or (len(self.frozenbctags) >= 3):
                self.attack_type = 'chaos'
                self.log_army('spreading the army')
                await self.log_attacktype('spreading the army')
                it_changed = True
#               unfreeze
                for bc in self.units(BATTLECRUISER).ready:
                    if bc.tag in self.frozenbctags:
                        self.log_command('bc(AbilityId.STOP)')
                        bc(AbilityId.STOP)
                self.frozenbctags = set()
        elif self.attack_type == 'chaos':
            if self.supply_used > 190:
                self.attack_type = 'arc'
                self.log_army('arcing the army')
                await self.log_attacktype('arcing the army')
                it_changed = True
        elif self.attack_type == 'arc':
            reached = 0
            total = 0
            for srt in [BATTLECRUISER,MARINE,MARAUDER]:
                for ar in self.units(srt).ready:
                    total = total+1
                    if self.quality_of_army_position(ar.position) > 5:
                        if ar in self.units(srt).ready.idle:
                            reached = reached+1
            if reached*5 > total*4:
                self.attack_type = 'arcpoint'
                self.log_army('starting a arcpoint attack')
                await self.log_attacktype('starting a arcpoint attack')
                it_changed = True
        elif self.attack_type == 'arcpoint':
            self.attack_type = 'center'
            self.log_army('centering the army')
            await self.log_attacktype('centering the army')
            it_changed = True
            tp = Point2((random.randrange(self.map_left,self.map_right),random.randrange(self.map_bottom,self.map_top)))
            while self.near(tp,self.enemyloc,80) or (not self.near(tp,self.enemyloc,100)): 
                tp = Point2((random.randrange(self.map_left,self.map_right),random.randrange(self.map_bottom,self.map_top)))
            self.army_center_point = tp    
        elif self.attack_type == 'center':
            reached = 0
            total = 0
            for srt in [BATTLECRUISER,MARINE,MARAUDER]:
                for ar in self.units(srt).ready:
                    total = total+1
                    if self.quality_of_army_position(ar.position) > 5:
                        if ar in self.units(srt).ready.idle:
                            reached = reached+1
            if reached*5 > total*4:
                self.attack_type = 'centerpoint'
                self.log_army('starting a center-to-point attack')
                await self.log_attacktype('starting a center-to-point attack')
                it_changed = True
        elif self.attack_type == 'centerpoint':
            self.attack_type = 'jumpy'
            self.log_army('feeling jumpy')
            await self.log_attacktype('feeling jumpy')
            it_changed = True
#       
#       if the attack_type changed, get a new enemy_target_base_loc
        if it_changed:
            allloc = []
            for ene in self.enemy_structures.ready:
                if ene.type_id in (COMMANDCENTER,ORBITALCOMMAND,PLANETARYFORTRESS,HATCHERY,LAIR,HIVE,NEXUS):
                    allloc.append(ene.position)
            if len(allloc) == 0:
                self.enemy_target_base_loc = self.enemyloc
            else:
                self.enemy_target_base_loc = random.choice(allloc)
#               
#       the raven should attack the best battlecruiser
        for rv in self.units(RAVEN).ready.idle:
            for bc in self.units(BATTLECRUISER).ready:
                if bc.tag == self.bestbctag:
                    self.log_command('rv.attack(bc)')
                    rv.attack(bc)
                    self.log_army('raven will follow a bc')
#       vikings should defend viking targets
#       flying random defensive, although this could give away info
        for vk in self.units(VIKINGFIGHTER).ready.idle:
            target = None
            for ene in self.enemy_units:
                if (ene.type_id in self.viking_targets):
                    if self.close_to_a_my_base(ene.position):
                        target = ene
            if target == None:
                if len(self.all_bases) > 0:
                    bas = random.choice(self.all_bases)
                    basp = bas.position
                else:
                    basp = self.start_location
                pos = Point2((basp.x+random.randrange(-10,10),basp.y+random.randrange(-10,10)))
                self.log_command('vk.attack(pos)')
                vk.attack(pos)
            else:
                self.log_command('vk.attack('+ene.name+')')
                vk.attack(target)
#       suicider scvs
        if self.count_of_job['suicider'] > 0:
            for scv in self.units(SCV).idle:
                scvt = scv.tag
                if scvt in self.all_scvt:
                    if self.job_of_scvt[scvt] == 'suicider':
                        place = self.mineral_field.random.position
                        self.log_command('scv.attack(place)')
                        scv.attack(place)


    async def siege_tank(self):
#       siege tank at a random own base
        for tnk in self.units(SIEGETANK).ready.idle:
            tnkt = tnk.tag
            if tnkt in self.towt_of_tnkt:
                towt = self.towt_of_tnkt[tnkt]
                for tow in self.all_bases:
                    if tow.tag == towt:
                        if self.near(tnk.position,tow.position,10):
                            self.log_command('tnk(AbilityId.SIEGEMODE_SIEGEMODE)')
                            tnk(AbilityId.SIEGEMODE_SIEGEMODE)
                        else:
                            self.log_command('tnk.attack(tow.position)')
                            tnk.attack(tow.position)
            else:
                if len(self.all_bases) == 0:
                    self.log_command('tnk(AbilityId.SIEGEMODE_SIEGEMODE)')
                    tnk(AbilityId.SIEGEMODE_SIEGEMODE)
                else:
                    tow = random.choice(self.all_bases)
#                   halfheartedly prevent all tanks in startbase
                    if tow.position == self.start_location.position:
                        tow = random.choice(self.all_bases)
                    towt = tow.tag
                    self.towt_of_tnkt[tnkt] = towt
                    self.log_command('tnk.attack(tow.position.towards(self.game_info.map_center,3))')
                    tnk.attack(tow.position.towards(self.game_info.map_center,3))


    async def fire_yamato(self):
        for bc in self.units(BATTLECRUISER).ready:
            found = False
            for kind in self.bc_enemies:
                for ene in self.enemy_units(kind):
                    if self.near(ene.position,bc.position,8):
                        target = ene
                        found = True
            if found:
                abilities = (await self.get_available_abilities([bc]))[0]
                if AbilityId.YAMATO_YAMATOGUN in abilities:
                    self.log_command('bc(AbilityId.YAMATO_YAMATOGUN,'+target.name+')')
                    bc(AbilityId.YAMATO_YAMATOGUN, target)
        for ra in self.units(RAVEN).ready:
            found = False
            for kind in self.bc_enemies:
                for ene in self.enemy_units(kind):
                    if self.near(ene.position,ra.position,8):
                        target = ene
                        found = True
            if found:
                abilities = (await self.get_available_abilities([ra]))[0]
                if AbilityId.EFFECT_ANTIARMORMISSILE in abilities:
                    self.log_command('ra(AbilityId.EFFECT_ANTIARMORMISSILE,'+target.name+')')
                    ra(AbilityId.EFFECT_ANTIARMORMISSILE, target)




    async def battle_jump_home(self):
        self.routine = 'battle_jump_home'
        for bc in self.units(BATTLECRUISER).ready:
            if (bc.health <= self.bc_fear) and (bc.tag not in self.bct_in_repair):
#               jump bc home for repair
                self.log_success('')
                self.log_command('bc(AbilityId.EFFECT_TACTICALJUMP,self.shipyard)')
                bc(AbilityId.EFFECT_TACTICALJUMP,self.shipyard)
                self.bct_in_repair.append(bc.tag)
                self.bc_fear = max(150,self.bc_fear-10)


    async def battle_dodge_bile(self):
        self.routine = 'battle_dodge_bile'
        for effect in self.state.effects:
            if effect.id == EffectId.RAVAGERCORROSIVEBILECP:
                for bc in self.units(BATTLECRUISER).ready:
                    mustflee = False
                    for bileposition in effect.positions:
                        if self.near(bileposition,bc.position,3):
                            mustflee = True
                            abile = bileposition
                    if mustflee:
                        topoint = self.flee(bc.position,3.2)
                        while self.near(abile,topoint,3):
                            topoint = self.flee(bc.position, 3.2)
                        self.log_command('bc(AbilityId.MOVE_MOVE,topoint)')
                        bc(AbilityId.MOVE_MOVE,topoint)


    async def hellion_dodge(self):
        self.routine = 'hellion_dodge'
        wantpoint = self.enemy_start_locations[0].position.towards(self.game_info.map_center,-5)
        for hel in self.units(HELLION).ready:
            danger = False
            canshoot = False
            for ene in self.enemy_units:
                if self.near(ene.position, hel.position, 2):
                    danger = True
                    someenepos = ene.position
                if self.near(ene.position, hel.position, 3):
                    canshoot = True
            if danger:
                topoint = self.flee(hel.position, 3)
                while self.near(someenepos, topoint, 2):
                    topoint = self.flee(hel.position, 3)
                self.log_command('hel(AbilityId.MOVE_MOVE,topoint)')
                hel(AbilityId.MOVE_MOVE, topoint)
            elif not self.near(wantpoint,hel.position,2):
                if not canshoot:
                    self.log_command('hel(AbilityId.MOVE_MOVE,wantpoint)')
                    hel(AbilityId.MOVE_MOVE,wantpoint)


    async def bunkercheese(self):
        self.routine = 'bunkercheese'
        if self.cheese_phase == 'A':
            for nr in range(0, len(self.tips)):
                ti = self.tips[nr]
                woord = ti.split()
                if (woord[0] == 'position') and (woord[1] == 'PRISON'):
                    self.cheese_prison = Point2((float(woord[2]), float(woord[3])))
                    self.cheese_phase = 'B'
        elif self.cheese_phase == 'B':
            startedbuildings = 0
            for barra in self.structures(BARRACKS).ready:
                if barra.position != self.infestedbarracks_build_position:
                    if self.near(barra.position,self.infested_land_position,7):
                        self.cheese_barracks = barra
                        startedbuildings = startedbuildings+1
            for bunk in self.structures(BUNKER):
                if self.near(bunk.position,self.infested_land_position,7):
                    self.cheese_bunker = bunk
                    startedbuildings = startedbuildings + 1
            if startedbuildings == 2:
                self.log_command('self.cheese_barracks(AbilityId.RALLY_BUILDING,self.cheese_prison)')
                self.cheese_barracks(AbilityId.RALLY_BUILDING,self.cheese_prison)
                self.cheese_phase = 'C'
        elif self.cheese_phase == 'C':
            if self.cheese_bunker in self.structures(BUNKER).ready:
                for anscv in self.units(SCV):
                    if self.near(anscv.position,self.infested_land_position,7):
                        self.cheese_scv = anscv
                        scvt = self.cheese_scv.tag
                        self.log_workers('the cheese_scv is ' + self.name(scvt))
                # rally and load
                self.log_command('self.cheese_barracks(AbilityId.RALLY_BUILDING,self.cheese_bunker)')
                self.cheese_barracks(AbilityId.RALLY_BUILDING,self.cheese_bunker)
                self.log_command('self.cheese_bunker(AbilityId.RALLY_BUILDING,self.cheese_prison)')
                self.cheese_bunker(AbilityId.RALLY_BUILDING,self.cheese_prison)
                # warning: scv inside the bunker is not in self.units(SCV)
                self.log_command('self.cheese_bunker(AbilityId.LOAD_BUNKER,self.cheese_scv)')
                self.cheese_bunker(AbilityId.LOAD_BUNKER,self.cheese_scv)
                self.cheese_phase = 'D'
        elif self.cheese_phase == 'D':
            # temporarily load some marines to make place for the scv
            self.cheese_marines = set()
            for mari in self.units(MARINE):
                if self.near(mari.position, self.infested_land_position, 7):
                    self.cheese_marines.add(mari)
            for mari in self.cheese_marines:
                self.log_command('self.cheese_bunker(AbilityId.LOAD_BUNKER,mari)')
                self.cheese_bunker(AbilityId.LOAD_BUNKER,mari)
            self.cheese_phase = 'E'
        elif self.cheese_phase == 'E':
            # we want to unload the cheese_scv, but it is said only unloadall works
            self.log_command('self.cheese_bunker(AbilityId.UNLOADALL_BUNKER)')
            self.cheese_bunker(AbilityId.UNLOADALL_BUNKER)
            # promote cheese_scv to arearepairer
            scvt = self.cheese_scv.tag
            self.log_workers('promoted cheese_scv to arearepairer')
            self.job_of_scvt[scvt] = 'arearepairer'
            self.promotionsite_of_scvt[scvt] = self.cheese_scv.position
            self.cottage_of_scvt[scvt] = self.cheese_prison
            self.cheese_phase = 'F'
        elif self.cheese_phase == 'F':
            self.cheese_marines = set()
            for mari in self.units(MARINE):
                if self.near(mari.position, self.infested_land_position, 7):
                    self.cheese_marines.add(mari)
            for mari in self.cheese_marines:
                self.log_command('self.cheese_bunker(AbilityId.LOAD_BUNKER,mari)')
                self.cheese_bunker(AbilityId.LOAD_BUNKER,mari)
            self.cheese_phase = 'G'
        elif self.cheese_phase == 'G':
            for facta in self.structures(FACTORYFLYING).ready:
                if self.near(facta.position, self.infested_land_position, 4):
                    self.cheese_factory = facta
                    self.home_of_flying_struct[self.cheese_barracks.tag] = self.infestedbarracks_build_position
                    self.landings_of_flying_struct[self.cheese_barracks.tag] = 0
                    self.log_success('up INFESTEDBARRACKS')
                    self.log_command('self.cheese_barracks(AbilityId.LIFT)')
                    self.cheese_barracks(AbilityId.LIFT)
                    # it will try to land itself
                    self.cheese_phase = 'H'
        self.log_cheese()


#*********************************************************************************************************************

    async def lift(self):
#       attacked buildings can fly, survive, be repaired, and land back.
        self.routine = 'lift'
        for srt in self.landable:
            for bu in self.structures(srt).ready.idle:
                if bu.health >= bu.health_max-100:
                    # land (or move to landing spot)
                    if self.near(bu.position,self.home_of_flying_struct[bu.tag],4):
                        # land
                        if self.landings_of_flying_struct[bu.tag] > 7:
                            # try another landing place
                            self.landings_of_flying_struct[bu.tag] = 0
                            oldpoint = self.home_of_flying_struct[bu.tag]
                            altpoint = Point2((oldpoint.x+random.randrange(-4,4),(oldpoint.y+random.randrange(-4,4))))
                            tries = 0
                            while (not self.check_layout(BARRACKS,altpoint)) and (tries<10):
                                tries = tries + 1
                                altpoint = Point2((oldpoint.x+random.randrange(-4,4),(oldpoint.y+random.randrange(-4,4))))
                            self.home_of_flying_struct[bu.tag] = altpoint
                        self.log_success('down '+srt.name)
                        self.log_command('bu(AbilityId.LAND,self.home_of_flying_struct[bu.tag])')
                        bu(AbilityId.LAND,self.home_of_flying_struct[bu.tag])
                        self.landings_of_flying_struct[bu.tag] = self.landings_of_flying_struct[bu.tag] + 1
                    else:
                        # the move prevents over-early "can not land" warnings.
                        bu.move(self.home_of_flying_struct[bu.tag])
                elif not self.near(self.start_location.position,bu.position,10):
                    self.log_command('bu(AbilityId.MOVE_MOVE,self.shipyard)')
                    bu(AbilityId.MOVE_MOVE,self.shipyard)
        for srt in self.liftable:
            for bu in self.structures(srt).ready:
                if bu.health < 700:
                    self.home_of_flying_struct[bu.tag] = bu.position
                    self.landings_of_flying_struct[bu.tag] = 0
                    self.log_success('up '+srt.name)
                    self.log_command('bu(AbilityId.LIFT')
                    bu(AbilityId.LIFT)
#       fly in the cheese
        for bu in self.structures(BARRACKS).ready:
            if bu.position == self.infestedbarracks_build_position:
                if self.find_tobuildwalk_a_place(INFESTEDBARRACKS):
                    self.infested_land_position = self.function_result_Point2
                    self.home_of_flying_struct[bu.tag] = self.infested_land_position
                    self.landings_of_flying_struct[bu.tag] = 0
                    self.log_success('up INFESTEDBARRACKS')
                    self.log_command('bu(AbilityId.LIFT)')
                    bu(AbilityId.LIFT)
                    # it will try to land itself
#       fly in the cheese
        for bu in self.structures(FACTORY).ready:
            if bu.position == self.infestedfactory_build_position:
                self.home_of_flying_struct[bu.tag] = self.infested_land_position
                self.landings_of_flying_struct[bu.tag] = 0
                self.log_success('up INFESTEDFACTORY')
                self.log_command('bu(AbilityId.LIFT)')
                bu(AbilityId.LIFT)
                # it will try to land itself



    async def do_updown(self):
        self.routine = 'do_updown'
        if self.updown == self.dummytag:
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
                    self.log_command('sd(AbilityId.MORPH_SUPPLYDEPOT_RAISE)')
                    sd(AbilityId.MORPH_SUPPLYDEPOT_RAISE)
                    self.log_success('raising')
#               do not idle on the depot
                for scv in self.units(SCV).idle:
                    if self.near(scv.position,sd.position,1.5):
                        whereto = self.flee(sd.position,2)
                        scv.move(whereto)
        for sd in self.structures(SUPPLYDEPOT).ready:
            if sd.tag == self.updown:
                danger = False
                for ene in self.enemy_units:
                    if self.near(ene.position,sd.position,5):
                        danger = True
                if not danger:
                    self.log_command('sd(AbilityId.MORPH_SUPPLYDEPOT_LOWER)')
                    sd(AbilityId.MORPH_SUPPLYDEPOT_LOWER)
                    self.log_success('lowering')



    async def ruin(self):
        for s in self.structures_without_construction_SCVs():
            self.log_command(s.name+'(AbilityId.CANCEL)')
            s(AbilityId.CANCEL)


#*********************************************************************************************************************
# worker routines

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
                                self.log_command('cc.train(SCV)')
                                cc.train(SCV)
                                self.idle_structure_tags.remove(cc.tag)


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
                            self.log_command('scv.repair('+s.name+')')
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
                                                self.log_command('scv.garther(mim)')
                                                scv.gather(mim)
                                                self.log_workers('arearepairer bored '+self.name(scvt))
                            else:
                                self.log_workers('going home '+self.name(scvt))
                                self.log_command('scv(AbilityId.MOVE_MOVE,self.cottage_of_scvt[scvt])')
                                scv(AbilityId.MOVE_MOVE,self.cottage_of_scvt[scvt])



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
                        self.log_command('scv(AbilityId.MOVE_MOVE,place)')
                        scv(AbilityId.MOVE_MOVE,place)
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
                        self.log_command('scv(AbilityId.MOVE_MOVE,self.goal_of_trabu_scvt[scvt])')
                        scv(AbilityId.MOVE_MOVE,self.goal_of_trabu_scvt[scvt])
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
        wishr = min(len(self.all_scvt)//6, len(self.all_bases)+len(self.structures(COMMANDCENTERFLYING)))
        if self.cheese_phase >= 'F':
            wishr = wishr+1
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
                    self.log_command('scv(AbilityId.STOP)')
                    scv(AbilityId.STOP)
        if self.count_of_job['arearepairer'] < wishr:
#           get a base that is far from each cottage
            worst_towpos = None
            worst_dist = -1
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
                        self.log_command('scv(AbilityId.STOP)')
                        scv(AbilityId.STOP)
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
                        self.log_command('scv(AbilityId.STOP)')
                        scv(AbilityId.STOP)
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
                        self.log_command('scv(AbilityId.MOVE_MOVE,self.shipyard)')
                        scv(AbilityId.MOVE_MOVE,self.shipyard)
                    elif len(self.bct_in_repair) > 0:
                        for bc in self.units(BATTLECRUISER).ready:
                            bct = bc.tag
                            if bct == self.bct_in_repair[0]:
                                if self.near(bc.position,self.shipyard,15):
                                    self.log_command('scv.repair(bc)')
                                    scv.repair(bc)
#       keep the bc in the shipyard
        if len(self.bct_in_repair) > 0:
            for bc in self.units(BATTLECRUISER).ready:
                bct = bc.tag
                if bct == self.bct_in_repair[0]:
                     if self.near(bc.position,self.shipyard,15) and not self.near(bc.position,self.shipyard,5):
                         self.log_command('bc(AbilityId.MOVE_MOVE,self.shipyard)')
                         bc(AbilityId.MOVE_MOVE,self.shipyard)



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
                            self.log_command('scv(AbilityId.MOVE_MOVE,cc.position.towards(self.game_info.map_center,-3))')
                            scv(AbilityId.MOVE_MOVE,cc.position.towards(self.game_info.map_center,-3))
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
                            self.log_command('scv(AbilityId.MOVE_MOVE,cc.position.towards(self.game_info.map_center,-3))')
                            scv(AbilityId.MOVE_MOVE,cc.position.towards(self.game_info.map_center,-3))
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
                                        self.log_command('scv.gather(gas)')
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
                                    self.log_command('scv.gather(gas)')
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
                                        self.log_command('scv.gather(mim)')
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
                                    self.log_command('scv.gather(mim)')
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

    async def more_gas(self):
        # try to swap a mimminer to gasminer
        todo = 1
        self.fix_count_of_gast()
        if self.gasminer_vacatures() > 0:
            for gast in self.all_gast:
                if self.count_of_gast[gast] < 3:
                    thisgast = gast
            for gas in self.all_refineries:
                if gas.tag == thisgast:
                    for scv in self.units(SCV):
                        scvt = scv.tag
                        if self.job_of_scvt[scvt] == 'mimminer':
                            if self.near(scv.position, gas.position, self.miner_bound):
                                if todo>0:
                                    todo = todo-1
                                    self.job_of_scvt[scvt] = 'gasminer'
                                    self.promotionsite_of_scvt[scvt] = scv.position
                                    self.log_command('scv.gather(gas)')
                                    scv.gather(gas)
                                    self.log_workers('mimminer became gasminer ' + self.name(scvt))
                                    self.gast_of_scvt[scvt] = gast
                                    self.count_of_gast[gast] = self.count_of_gast[gast] + 1

    async def more_minerals(self):
        # try to swap a gasminer to mimminer
        todo = 1
        self.fix_count_of_mimt()
        if self.mimminer_vacatures() > 0:
            for mimt in self.all_mimt:
                if self.count_of_mimt[mimt] < 2:
                    thismimt = mimt
            for mim in self.mineral_field:
                if mim.tag == thismimt:
                    for scv in self.units(SCV):
                        scvt = scv.tag
                        if self.job_of_scvt[scvt] == 'gasminer':
                            if self.near(scv.position, mim.position, self.miner_bound):
                                if todo>0:
                                    todo = todo-1
                                    self.job_of_scvt[scvt] = 'mimminer'
                                    self.promotionsite_of_scvt[scvt] = scv.position
                                    self.log_command('scv.gather(mim)')
                                    scv.gather(mim)
                                    self.log_workers('gasminer became mimminer ' + self.name(scvt))
                                    self.mimt_of_scvt[scvt] = mimt
                                    self.count_of_mimt[mimt] = self.count_of_mimt[mimt] + 1


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
                            self.log_command('scv(AbillityId.STOP)')
                            scv(AbilityId.STOP)
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
                        self.log_command('scv.attack(self.enemyloc)')
                        scv.attack(self.enemyloc)
#       job-swap for late game
        if (self.count_of_job['idler'] == 0) and (self.itera % 19 == 0):
            if self.minerals > self.vespene + 2000:
                await self.more_gas()
            if self.vespene > self.minerals + 2000:
                await self.more_minerals()
#       follow gas_advice
        if self.gas_advice == 1:
            await self.more_gas()
        if self.gas_advice == -1:
            await self.more_minerals()
        self.gas_advice = 0
#       stop escorters lured to their death
        for scvt in self.all_scvt:
            if (self.job_of_scvt[scvt] == 'escorter'):
                for scv in self.units(SCV):
                    if scvt == scv.tag:
                        if self.near(scv.position,self.enemyloc,50):
                            self.job_of_scvt[scvt] = 'idler'
                            self.log_workers('Enemy fear stops escorter '+self.name(scvt))
                            self.log_command('scv(AbilityId.STOP)')
                            scv(AbilityId.STOP)

#*********************************************************************************************************************

    def rarely_executed_code(self):
#       designs: add tag to realized plans
        newdesigns = []
        for (struc,place,tag) in self.designs:
            if tag == self.dummytag:
                for astruc in self.structures:
#                   the cc could have become a pf already, accept flying
                    if astruc.position == place:
                        tag = astruc.tag
            newdesigns.append((struc,place,tag))
        self.designs = newdesigns.copy()
#       designs: erase if neither tag nor plan is found
        erase = []
        for (struc,place,tag) in self.designs:
            seen = False
            for astruc in self.structures:
#               the cc could have become a pf already, accept flying
                if tag == astruc.tag:
                    seen = True
            for scvt in self.goal_of_trabu_scvt:
                if place == self.goal_of_trabu_scvt[scvt]:
                    seen = True
            for (exething,exeplace) in self.buildorder_to_execute:
                if place == exeplace:
                    seen = True
            if not seen:
                erase.append((struc,place,tag))
        for (struc,place,tag) in erase:
            self.erase_layout(struc,place)
        newdesigns = []
        for (struc,place,tag) in self.designs:
            if (struc,place,tag) not in erase:
                newdesigns.append((struc,place,tag))
        self.designs = newdesigns.copy()
 

#*********************************************************************************************************************
#   strategy system
#   a strategy is, per game_choice, a probability to choose "yes".
#   the game choices can be made at the start of the game and are unknown to the opponent.
#
#   We can be fancy and feed back won-or-loss of a game to the strategy.
#
    def write_strategy(self):
        pl = open('strategy.txt','w')
        for nr in range(0,len(self.strategy)):
            pl.write(str(self.strategy[nr])+'\n')
        pl.close()


    async def init_strategy(self):
        for i in range(0,self.game_choices):
            self.strategy.append(0.5)
#       read from disk
        pl = open('strategy.txt','r')
        read_strategy = pl.read().splitlines()
        pl.close()
        for nr in range(0,len(read_strategy)):
            self.strategy[nr] = float(read_strategy[nr].rstrip())
#       init game_choice
        for nr in range(0,len(self.strategy)):
            self.game_choice.append(random.random() < self.strategy[nr])
        self.game_result = 'doubt'

    async def win_loss(self):
        if self.game_result == 'doubt':
            max_cc_health = 0
            for cc in self.all_bases:
                if cc.health > max_cc_health:
                    max_cc_health = cc.health
            if self.supply_used>190:
                self.game_result = 'win'
                await self._client.chat_send('probably a win', team_only=False)
                self.log_success('win')
                for nr in range(0, len(self.strategy)):
                    if self.game_choice[nr]:
                        self.strategy[nr] = 0.9*self.strategy[nr]+0.1
                    else:
                        self.strategy[nr] = 0.9*self.strategy[nr]
                self.write_strategy()
            elif max_cc_health < 500:
                self.game_result = 'loss'
                await self._client.chat_send('probably a loss', team_only=False)
                self.log_success('loss')
                for nr in range(0, len(self.strategy)):
                    if self.game_choice[nr]:
                        self.strategy[nr] = 0.9*self.strategy[nr]
                    else:
                        self.strategy[nr] = 0.9*self.strategy[nr]+0.1
                self.write_strategy()


#*********************************************************************************************************************
#       Easy/Medium/Hard/VeryHard
run_game(maps.get('ZenLE'), [
    Bot(Race.Terran, Chaosbot()),
    Computer(Race.Protoss, Difficulty.Hard)
    ], realtime=True)
