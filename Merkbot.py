# Merkbot.py containing Chaosbot
# author: MerkMore
# version 19 sep 2020
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
from sc2.ids.unit_typeid import PROBE
from sc2.ids.unit_typeid import DRONE
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
from sc2.ids.upgrade_id import HISECAUTOTRACKING
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
from sc2.ids.unit_typeid import TEMPEST
from sc2.ids.unit_typeid import MUTALISK
from sc2.ids.unit_typeid import PHOENIX
from sc2.ids.unit_typeid import RAVAGER
from sc2.ids.unit_typeid import BANSHEE
from sc2.ids.unit_typeid import LIBERATOR
from sc2.ids.unit_typeid import LIBERATORAG
from sc2.ids.unit_typeid import OVERLORD
from sc2.ids.unit_typeid import BROODLORD
from sc2.ids.unit_typeid import ORACLE
from sc2.ids.unit_typeid import OBSERVER
from sc2.ids.unit_typeid import HATCHERY
from sc2.ids.unit_typeid import LAIR
from sc2.ids.unit_typeid import HIVE
from sc2.ids.unit_typeid import NEXUS
from sc2.ids.unit_typeid import CYCLONE
from sc2.ids.unit_typeid import WIDOWMINE
from sc2.ids.unit_typeid import WIDOWMINEBURROWED
# with INFESTED is meant "close to the enemy".
from sc2.ids.unit_typeid import INFESTEDBARRACKS
from sc2.ids.unit_typeid import INFESTEDBUNKER
from sc2.ids.unit_typeid import INFESTEDFACTORY
from sc2.ids.unit_typeid import INFESTEDSTARPORT


class Chaosbot(sc2.BotAI):
    #   ############### CHANGE VALUE AD LIB
    do_log_success = False
    do_log_fail = False
    do_log_command = False
    do_log_attacktype = False
    do_log_workers = False
    do_log_population = False
    do_log_armysize = False
    do_log_army = False
    do_log_gasminer = False
    do_log_resource = False
    do_log_limbo = False
    do_log_buildsit = False
    do_log_buildseries = False
    do_log_placing = False
    do_log_planning = False
    do_log_time = False
    do_log_layout = False
    do_log_cheese = False
    do_log_boss = False
    do_log_ambiwalk = False
    do_log_enemies = False
    #   ############### CONSTANT
    #   constant over the iterations after iteration 0:
    #   other
    nowhere = Point2((1,1))
    notag = -1
    all_structures = []
    all_structures_tobuildwalk = []
    all_army = []
    all_workertypes = []
    all_upgrades = []
    all_labs = [] # for labs, with place, always its motherbuilding place will be used.
    supply_of_army = {}
    builddura_of_thing = {}
    size_of_structure = {}
    liftable = []
    techtree = []
    all_things = set()
    cradle = []
    shipyard = None
    basetop = set() # empty squares near start, inside the wall, inside ramps
    bc_enemies = None
    #   squareroots of integers from 0 to 200*200*2, 0<=x<400
    stored_root = []
    # timing constants
    gas_speed = 0.6
    # empirical value, fit for the situation with automatic minerbuild
    mim_speed = 0.6
    # empirical value, fit to the euclid walkdistance with slight underestimation
    walk_speed = 2.3
    #
    miner_bound = 10
    enemyloc = None
    enemy_target_building_loc = None
    map_left = 0
    map_right = 0
    map_bottom = 0
    map_top = 0
    #   ############### GAMESTATE
    #   gamestate values constant in this iteration after gamestate:
    itera = -1
    all_bases = []
    all_refineries = []
    army_supply = 0
    #   ############### REST
    eggs = set() # (bar,martype,restdura)
    routine = 'start'
    #   stored tips
    tips = []
    tips_used = []
    #   coding problem
    function_result_Point2 = None
    # idle in this iteration:
    idle_structure_tags = []
    #   ############### ARMY AND STRUCTURE MANAGEMENT
    seen_enemy_units = set()
    seen_enemy_structuretypes = set()
    #   the tags of the 2 supplydepots used as a gate:
    updowns = set()
    last_health = {}
    #   army coodination
    frozenbctags = set()
    attack_type = 'jumpy'
    cruisercount = 0
    lastcruisercount = 0
    home_of_flying_struct = {}
    landings_of_flying_struct = {}
    bct_in_repair = []
    bestbctag = notag
    bestbc_dist_to_goal = 99999
    bc_fear = 250
    goal_of_wmt = {}
    sd_of_wmt = {}
    shame_of_wmt = {}
    martag_to_bunker = set()
    #   ambition contains commandcenters becoming a planetaryfortress, factories getting a techlab.
    ambition_of_strt = {}
    #   the barracks in the wall could be placed such as not to be able to get a techlab
    add_on_denied = []
    towt_of_tnkt = {}
    army_center_point = None
    #   (struc,place,tag) for tobuildwalk plans with a layout. Administrate to enable erasing.
    designs = []
    # wall_barracks
    wall_barracks_pos = None
    wall_depot0_pos = None
    wall_depot1_pos = None
    wall_barracks_managed = False
    #   A barracks close to the enemy has to fly from build position to attack position
    cheese_barracks_pos = None
    cheese_factory_pos = None
    cheese_starport_pos = None
    cheese_landing_pos = None
    cheese_bunker_pos = None
    cheese_prison_pos = None
    cheese_tank_pos = None
    cheese_phase = 'A'
    cheese_barracks = None
    cheese_factory = None
    cheese_starport = None
    cheese_bunker = None
    cheese_scv = None
    cheese_marines = set()
    cheese_marine_count = 0
    cheese_tank_count = 0
    cheese_tank = None
    cheese_mine = None
    cheese_bunker_last_health = 0
    cheese_frames = 0
    # cheese2
    cheese2_phase = 'A'
    cheese2_bunker = None
    cheese2_bunker_pos = None
    #   ############### SCV MANAGEMENT
    #   traveller and builder scvs have a goal
    #   traveller and builder scvs have a structure to build
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
    good_jobs = ('builder','shiprepairer','traveller','arearepairer','escorter','scout','cheeser')
    bad_jobs = ('gasminer','mimminer','applicant','idler','suicider','fleeer','defender')
    job_of_scvt = {}
    count_of_job = {}
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
    # scout
    scout_pos = []
    scout_tag = notag
    scout_nr = 0
    scout_last_sdist = 0
    scout_bad_count = 0
    #   interface planning / workers
    gas_advice = 0
    # checks
    minedirection_of_scvt = {}
    #   ############### PLAY CHOICES
    game_phase = 'init'
    #   the planning_of_buildorder routine
    # bagofthings is a list of things, that we want to be made. No infected.
    # bagoftree is a bagofthings including still needed techtree demands. No infected.
    # buildseries is a list of buildings, that we want to make. It contains techtree predecessors and has an order. Can have infected.
    # buildorder is a list of (building,place) combinations. Or e.g. (MARINE,place-of-a-future-barracks). No infected.
    # planning is a list of buildplans, including timing.
    # those plans have a _exe variant, the chosen actual one.
    # Work has to be removed from the _exe when the order is started.
    # It is not clear when to start the work in the _exe.
    bagofthings = []
    bagoftree = []
    buildseries = []
    buildorder = []
    planning = []
    #
    bagofthings_exe = []
    bagoftree_exe = []
    buildseries_exe = []
    buildorder_exe = []
    planning_exe = []
    # for started plans: (for ambitions, scvt==notag)
    ambiwalk_exe = set() # (scvt,th,pl) just before actual payment start in buildorder_exe[0]
    ambiwalk_thrown = set() # (scvt,th,pl) between throw request and actual payment start
    #
    all_future_basepos = set() # used when making buildorder
    #
    but_i_had_structures = 0 # amount of own structures, excl bunkers
    #
    midgame_bagofthings = []
    # placings that already have been in buildorder_exe:
    recycling = []
    #   the current sit for the buildseries
    sit_exist = {}   # for a thing: the dura until the first one will be ready
    sit_free = []   # (thing, freedura)
    #   to capture the current situation for the planning:
    situation_mimminers = 0
    situation_gasminers = 0
    situation_spendable_minerals = 0 # inside the look-ahead, spendable_minerals = minerals
    situation_spendable_vespene = 0
    situation_walking = set() # for tobuildwalk
    situation_constructing = set() # for tobuildwalk
    situation_training = set() # for army and upgrade
    situation_ambition = set() # for pf and lab
    situation_growing = set() # for pf and lab
    situation_thingkinds = set()
    situation_buildings_and_parts = set()
    situation_events = set()
    #   strategy
    strategy = []
    game_choice = []
    game_choices = 10
    game_result = 'doubt'

# *********************************************************************************************************************
    async def on_step(self, iteration: int):
        # make iteration available for logging
        self.itera = iteration
        # init stuff
        if len(self.techtree) == 0:
            await self.my_init()
        #
        #       main iteree:
        #
        await self.gamestate()
        self.get_eggs()
        self.log_resource()
        self.log_armysize()
        await self.bunkercheese()
        await self.bunkercheese2()
        if (iteration % 5 == 4):
            await self.realized_planning_exe()
            await self.make_planning_exe()
            await self.follow_planning_exe()
        await self.build_worker(100-self.minerals//100)
        await self.start_construction()
        await self.siege_tank()
        await self.use_mine()
        await self.fire_yamato()
        await self.battle_jump_home()
        await self.battle_dodge_bile()
        await self.hellion_dodge()
        await self.ruin()
        await self.may_cancel()
        self.get_arearepairer()
        await self.repair_it()
        await self.supplydepots_adlib()
        await self.refineries_adlib()
        await self.big_spender()
        await self.lift()
        await self.do_wall_barracks()
        await self.do_updown()
        await self.cheese_army()
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
        await self.worker_defence()
        await self.mimminer_boss()
        await self.gasminer_boss()
        self.wall_barracks_redirect()
        self.reset_workers()
        self.see_enemies()
        if (iteration % 100 == 4):
            self.log_enemies()

# *********************************************************************************************************************
    async def my_init(self):
        self.routine = 'my_init'
        self.log_success('##############################################################################')
        random.seed()
        # liftable
        self.liftable = [BARRACKS,FACTORY,STARPORT,COMMANDCENTER]
        self.landable = [BARRACKSFLYING,FACTORYFLYING,STARPORTFLYING,COMMANDCENTERFLYING]
        # enemy air with weak air defence
        self.viking_targets = [BANSHEE,LIBERATOR,LIBERATORAG,ORACLE,BROODLORD,OVERLORD,OBSERVER,BATTLECRUISER,MUTALISK,TEMPEST,VIPER]
        # enemy that can hurt a bc
        self.bc_enemies = (ARCHON, BATTLECRUISER, CARRIER, QUEEN, VIKINGFIGHTER, MISSILETURRET, SPORECRAWLER, \
            PHOTONCANNON, INFESTOR, HYDRALISK, THOR, VIPER, PHOENIX, RAVAGER, CYCLONE)
        # all_labs wegens verschoven plaatsing
        self.all_labs = (BARRACKSTECHLAB,FACTORYTECHLAB,STARPORTTECHLAB)
        self.all_workertypes = (SCV,PROBE,DRONE)
        # list of most structures, with builddura, size. Not flying, not lowered.
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
        # add for cheese with barracks and bunker
        # warning: this complicated much. Restrict to buildseries and placement.txt
        self.init_structures(INFESTEDBARRACKS, 46, 3)
        self.init_structures(INFESTEDBUNKER, 29, 3)
        self.init_structures(INFESTEDFACTORY, 43, 3)
        self.init_structures(INFESTEDSTARPORT, 36, 3)
        # army, builddura, supply
        self.init_army(SCV,12,1)
        self.init_army(MARINE,18,1)
        self.init_army(MARAUDER,21,2)
        self.init_army(HELLION,21,2)
        self.init_army(CYCLONE,32,3)
        self.init_army(WIDOWMINE,21,2)
        self.init_army(WIDOWMINEBURROWED,21,2)
        self.init_army(SIEGETANK,32,3)
        self.init_army(SIEGETANKSIEGED,32,3)
        self.init_army(VIKINGFIGHTER,30,2)
        self.init_army(MEDIVAC,30,2)
        self.init_army(RAVEN,43,2)
        self.init_army(LIBERATOR,43,3)
        self.init_army(LIBERATORAG,43,3)
        self.init_army(BATTLECRUISER,64,6)
        # upgrade, builddura
        self.init_upgrade(PUNISHERGRENADES, 43) #concussive shells
        self.init_upgrade(TERRANSHIPWEAPONSLEVEL1, 114)
        self.init_upgrade(TERRANSHIPWEAPONSLEVEL2, 136)
        self.init_upgrade(TERRANSHIPWEAPONSLEVEL3, 157)
        self.init_upgrade(TERRANVEHICLEANDSHIPARMORSLEVEL1, 114)
        self.init_upgrade(TERRANVEHICLEANDSHIPARMORSLEVEL2, 136)
        self.init_upgrade(TERRANVEHICLEANDSHIPARMORSLEVEL3, 157)
        self.init_upgrade(TERRANBUILDINGARMOR, 100)
        self.init_upgrade(HISECAUTOTRACKING,57)
        self.init_upgrade(TERRANINFANTRYWEAPONSLEVEL1, 114)
        self.init_upgrade(TERRANINFANTRYWEAPONSLEVEL2, 136)
        self.init_upgrade(TERRANINFANTRYWEAPONSLEVEL3, 157)
        self.init_upgrade(BATTLECRUISERENABLESPECIALIZATIONS, 100)
        # things that, to be built, need a cradle (a free building)
        self.init_cradle(RAVEN,STARPORT)
        self.init_cradle(MEDIVAC,STARPORT)
        self.init_cradle(VIKINGFIGHTER,STARPORT)
        self.init_cradle(LIBERATOR,STARPORT)
        self.init_cradle(MARINE,BARRACKS)
        self.init_cradle(MARAUDER,BARRACKS)
        self.init_cradle(SIEGETANK,FACTORY)
        self.init_cradle(CYCLONE,FACTORY)
        self.init_cradle(WIDOWMINE,FACTORY)
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
        self.init_cradle(HISECAUTOTRACKING,ENGINEERINGBAY)
        self.init_cradle(TERRANINFANTRYWEAPONSLEVEL1,ENGINEERINGBAY)
        self.init_cradle(TERRANINFANTRYWEAPONSLEVEL2,ENGINEERINGBAY)
        self.init_cradle(TERRANINFANTRYWEAPONSLEVEL3,ENGINEERINGBAY)
        self.init_cradle(PLANETARYFORTRESS,COMMANDCENTER)
        self.init_cradle(ORBITALCOMMAND,COMMANDCENTER)
        self.init_cradle(BATTLECRUISERENABLESPECIALIZATIONS,FUSIONCORE)
        # Some preconditions.
        # Each element is a unit, upgrade, or structure. First can not be produced without second.
        # In the init, those mentioned in init_cradle are not repeated.
        # The techtree does not contain multistep dependencies.
        # First is structure
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
        self.init_techtree(BUNKER,BARRACKS)
        # First is unit
        self.init_techtree(BATTLECRUISER,STARPORTTECHLAB)
        self.init_techtree(BATTLECRUISER,FUSIONCORE)
        self.init_techtree(SIEGETANK,FACTORYTECHLAB)
        self.init_techtree(CYCLONE,FACTORYTECHLAB)
        self.init_techtree(MARAUDER,BARRACKSTECHLAB)
        self.init_techtree(RAVEN,STARPORTTECHLAB)
        # First is upgrade
        self.init_techtree(TERRANSHIPWEAPONSLEVEL2,TERRANSHIPWEAPONSLEVEL1)
        self.init_techtree(TERRANSHIPWEAPONSLEVEL3,TERRANSHIPWEAPONSLEVEL2)
        self.init_techtree(TERRANVEHICLEANDSHIPARMORSLEVEL2,TERRANVEHICLEANDSHIPARMORSLEVEL1)
        self.init_techtree(TERRANVEHICLEANDSHIPARMORSLEVEL3,TERRANVEHICLEANDSHIPARMORSLEVEL2)
        self.init_techtree(TERRANINFANTRYWEAPONSLEVEL2,TERRANINFANTRYWEAPONSLEVEL1)
        self.init_techtree(TERRANINFANTRYWEAPONSLEVEL3,TERRANINFANTRYWEAPONSLEVEL2)
        self.compute_all_things()
        #       bootstrap code   after initial    from sc2constants import *
        #       for thing in self.all_things:
        #           if type(thing) == UnitTypeId:
        #               print('from sc2.ids.unit_typeid import '+thing.name)
        #           if type(thing) == UpgradeId:
        #               print('from sc2.ids.upgrade_id import '+thing.name)
        self.enemyloc = self.enemy_start_locations[0].position
        self.enemy_target_building_loc = self.enemyloc
        # all_repairable_shooters for repair priority
        self.all_repairable_shooters = set([PLANETARYFORTRESS,MISSILETURRET,BUNKER])
        for ut in self.all_army:
            if ut not in (MARINE,MARAUDER):
                self.all_repairable_shooters.add(ut)
        # give some loosely fitting init
        for mim in self.mineral_field:
            if self.near(mim.position, self.start_location.position, self.miner_bound):
                self.count_of_mimt[mim.tag] = 0
        for scv in self.units(SCV):
            self.job_of_scvt[scv.tag] = 'mimminer'
            amimt = self.notag
            best_sd = 99999
            for mim in self.mineral_field:
                if self.near(mim.position, self.start_location.position, self.miner_bound):
                    if self.count_of_mimt[mim.tag] < 2:
                        sd = self.sdist(scv.position,mim.position)
                        if sd < best_sd:
                            best_sd = sd
                            amim = mim
                            amimt = mim.tag
            scv.gather(amim)
            self.mimt_of_scvt[scv.tag] = amimt
            self.count_of_mimt[amimt] = self.count_of_mimt[amimt] + 1
        self.fix_count_of_job()
        # opening
        ops = 0
        ops = ops + 1
        if random.randrange(0, ops) == 0:
            # twobase bc:
            self.buildseries_opening = [SUPPLYDEPOT, REFINERY, BARRACKS, SUPPLYDEPOT, MARINE, FACTORY, REFINERY, MARINE, \
                                       STARPORT, COMMANDCENTER, FUSIONCORE, STARPORTTECHLAB, BATTLECRUISER]
        ops = ops + 1
        if random.randrange(0, ops) == 0:
            # elementary:
            self.buildseries_opening = [SUPPLYDEPOT, REFINERY, BARRACKS, SUPPLYDEPOT, MARINE]
        ops = ops + 1
        if random.randrange(0, ops) == 0:
            #cheese-expand:
            self.buildseries_opening = [SUPPLYDEPOT, INFESTEDBARRACKS, REFINERY, INFESTEDBUNKER, SUPPLYDEPOT, INFESTEDFACTORY, \
                                        BARRACKS, REFINERY, COMMANDCENTER]
        ops = ops + 1
        if random.randrange(0, ops) == 0:
            # full cheese:
            self.buildseries_opening = [SUPPLYDEPOT, INFESTEDBARRACKS, REFINERY, INFESTEDBUNKER, SUPPLYDEPOT, INFESTEDFACTORY, \
                                        BARRACKS, REFINERY, \
                                        STARPORT, SUPPLYDEPOT, FUSIONCORE, STARPORTTECHLAB, SUPPLYDEPOT, BATTLECRUISER]
        ops = ops + 1
        if random.randrange(0, ops) == 0:
            # expand:
            self.buildseries_opening = [SUPPLYDEPOT, COMMANDCENTER, BARRACKS, MARINE]
        # strategy choices
        await self.init_strategy()
        #  midgame
        self.bagofthings = []
        self.midgame(BATTLECRUISER,1)
        if self.game_choice[0]:
            self.midgame(SIEGETANK,1)
        if self.game_choice[1]:
            self.midgame(SIEGETANK,2)
        if self.game_choice[2]:
            self.midgame(MARINE,3)
        else:
            self.midgame(MARINE,6)
        if self.game_choice[3]:
            self.midgame(REFINERY,4)
            self.midgame(COMMANDCENTER,2)
            self.midgame(STARPORT,2)
            self.midgame(STARPORTTECHLAB,2)
        else:
            self.midgame(REFINERY,2)
        if self.game_choice[4]:
            self.midgame(ENGINEERINGBAY,1)
            self.midgame(MISSILETURRET,1)
        self.midgame(SUPPLYDEPOT,2)
        self.midgame_bagofthings = self.bagofthings.copy()
        # circle
        self.make_circle()
        # layout
        self.map_left = self.game_info.playable_area.x
        self.map_right = self.game_info.playable_area.width+self.game_info.playable_area.x
        self.map_bottom = self.game_info.playable_area.y
        self.map_top = self.game_info.playable_area.height+self.game_info.playable_area.y
        self.get_layout()
        self.write_layout(COMMANDCENTER,self.start_location.position)
        # make layout.txt for placer.py to compute placement tips
        layout_if.mapname = self.game_info.map_name
        layout_if.startx = self.start_location.position.x
        layout_if.starty = self.start_location.position.y
        layout_if.enemyx = self.enemyloc.x
        layout_if.enemyy = self.enemyloc.y
        layout_if.save_layout()
        # shipyard
        self.shipyard = self.start_location.position.towards(self.game_info.map_center,5)
        # color the shipyard on the layout, so we will not build there ever
        yardx = round(self.shipyard.x)
        yardy = round(self.shipyard.y)
        for dx in range(-2,3):
            for dy in range(-2,3):
                layout_if.layout[yardx+dx][yardy+dy] = 5
        # rally
        for cc in self.structures(COMMANDCENTER):
            cc(AbilityId.RALLY_BUILDING,self.start_location.position.towards(self.game_info.map_center,-3))
        # use stored placement tips
        mapplace = 'map: '+layout_if.mapname+' '+str(layout_if.startx)+' '+str(layout_if.starty)
        self.log_success(mapplace)
        pl = open('data/placement.txt','r')
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
        # feedback the tips
        for nr in range(0,len(self.tips)):
            ti = self.tips[nr]
            self.log_placing(ti)
        # put cheese tips in constants
        for nr in range(0, len(self.tips)):
            ti = self.tips[nr]
            woord = ti.split()
            if (woord[0] == 'position') and (woord[1] == 'INFESTEDPRISON'):
                self.cheese_prison_pos = Point2((float(woord[2]), float(woord[3])))
            elif (woord[0] == 'position') and (woord[1] == 'INFESTEDBARRACKS'):
                self.cheese_barracks_pos = Point2((float(woord[2]), float(woord[3])))
            elif (woord[0] == 'position') and (woord[1] == 'INFESTEDFACTORY'):
                self.cheese_factory_pos = Point2((float(woord[2]), float(woord[3])))
            elif (woord[0] == 'position') and (woord[1] == 'INFESTEDLANDING'):
                self.cheese_landing_pos = Point2((float(woord[2]), float(woord[3])))
            elif (woord[0] == 'position') and (woord[1] == 'INFESTEDBUNKER'):
                self.cheese_bunker_pos = Point2((float(woord[2]), float(woord[3])))
            elif (woord[0] == 'position') and (woord[1] == 'INFESTEDTANK'):
                self.cheese_tank_pos = Point2((float(woord[2]), float(woord[3])))
            elif (woord[0] == 'position') and (woord[1] == 'INFESTEDSTARPORT'):
                self.cheese_starport_pos = Point2((float(woord[2]), float(woord[3])))
        # put scout-series in scout_pos
        for nr in range(0, len(self.tips)):
            ti = self.tips[nr]
            woord = ti.split()
            if (woord[0] == 'position') and (woord[1] == 'SCOUT'):
                scpos = Point2((float(woord[2]), float(woord[3])))
                self.scout_pos.append(scpos)
        # wall position
        self.wall_barracks_pos = self.nowhere
        self.wall_depot0_pos = self.nowhere
        self.wall_depot1_pos = self.nowhere
        for nr in range(0, len(self.tips)):
            ti = self.tips[nr]
            woord = ti.split()
            if (woord[0] == 'position') and (woord[1] == 'BARRACKS'):
                if self.wall_barracks_pos == self.nowhere:
                    self.wall_barracks_pos = Point2((float(woord[2]), float(woord[3])))
            if (woord[0] == 'position') and (woord[1] == 'SUPPLYDEPOT'):
                if self.wall_depot0_pos == self.nowhere:
                    self.wall_depot0_pos = Point2((float(woord[2]), float(woord[3])))
                elif self.wall_depot1_pos == self.nowhere:
                    self.wall_depot1_pos = Point2((float(woord[2]), float(woord[3])))
        # get basetop
        self.get_basetop()
        # name_of_scvt: fun translation of scvt to english boy name
        pl = open('data/names.txt','r')
        self.all_names = pl.read().splitlines()
        pl.close()
        # chat
        await self._client.chat_send('Chaosbot version 19 sep 2020, made by MerkMore', team_only=False)

    #*********************************************************************************************************************
#   logging
    def log_fail(self,bol,stri):
        if self.do_log_fail:
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

    def log_workers(self,stri):
        if self.do_log_workers:
            print(f' On {self.itera} workers {self.routine} '+stri) 

    def log_layout(self,stri):
        if self.do_log_layout:
            print(f' On {self.itera} layout {self.routine} '+stri) 

    def log_placing(self,stri):
        if self.do_log_placing:
            print(f' On {self.itera} placing {self.routine} '+stri) 

    def log_command(self,stri):
        if self.do_log_command:
            print(f' On {self.itera} commands {self.routine} '+stri)

    def log_planning_bp(self,bp):
        if self.do_log_planning:
            print(f' On {self.itera} planning '+self.name(bp[0])+' '+bp[1].name+' '+str(bp[2][0])+','+str(bp[2][1])+'   '+\
                str(bp[3])+'   '+str(bp[4])+'   '+str(bp[5]))

    def log_planning(self,stri):
        if self.do_log_planning:
            print(f' On {self.itera} planning '+stri)

    def log_ambiwalk(self):
        if self.do_log_ambiwalk:
            print(f' On {self.itera} ambiwalk:')
            for (sc,th,po) in self.ambiwalk_exe | self.ambiwalk_thrown:
                print('ambiwalk '+self.name(sc)+' '+th.name+' '+str(po.x)+','+str(po.y))

    def log_boss(self,stri):
        if self.do_log_boss:
            print(f' On {self.itera} boss {self.routine} '+stri)

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

    def log_resource(self):
        if self.do_log_resource:
            print(f' On {self.itera} minerals '+str(self.minerals)+'   gas '+str(self.vespene))

    def log_buildseries(self, instri):
        if self.do_log_buildseries:
            stri = instri
            for thing in self.buildseries:
                stri = stri+' '+thing.name
            print(f' On {self.itera} buildseries: '+stri)

    def log_buildsit(self, stri):
        if self.do_log_buildsit:
            print(f' On {self.itera} buildsit: '+stri)

    def log_time(self,stri):
        if self.do_log_time:
            print(f' On {self.itera} time: '+stri)

    def log_cheese(self):
        if self.do_log_cheese:
            if self.cheese_phase != 'Z':
                print(f' On {self.itera} cheese phase '+self.cheese_phase+'    cheese2 '+self.cheese2_phase)


    def log_enemies(self):
        if self.do_log_enemies:
            stri = 'ENEMY_UNITS:'
            for ene in self.seen_enemy_units:
                stri = stri+' '+ene.name
            print(stri)
            stri = 'ENEMY_STRUCTURETYPES:'
            for ene in self.seen_enemy_structuretypes:
                stri = stri+' '+ene.name
            print(stri)


    #******************************************************************************************************************

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
            self.designs.append((struc,place,self.notag))
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
            if (struc in (REFINERY,REFINERYRICH)):
                mustbecolor = 1
            else:
                mustbecolor = 0
            for vakx in range(round(x-siz/2),round(x+siz/2)):
                for vaky in range(round(y-siz/2),round(y+siz/2)):
                    layout_if.layout[vakx][vaky] = mustbecolor
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

    def maxam_of_thing(self,thing) -> int:
        maxam = 100
        if thing in self.all_structures_tobuildwalk:
            if thing in (ARMORY,FUSIONCORE,ENGINEERINGBAY,FACTORY):
                maxam = 2
            if thing == MISSILETURRET:
                maxam = self.all_bases.amount*7
            if thing == STARPORT:
                maxam = self.all_bases.amount + 1
        elif thing in self.all_structures:
            pass
        elif type(thing) == UpgradeId:
            maxam = 1
        else:
#           army
            if thing in (RAVEN,HELLION):
                maxam = 1
            if thing == VIKINGFIGHTER:
                maxam = 10
            if thing in (MARAUDER,SIEGETANK,WIDOWMINE):
                maxam = 8
        return maxam

#*********************************************************************************************************************

#   distance
    def sdist(self,p,q):
        return (p.x-q.x)**2 + (p.y-q.y)**2
 
    def dist(self,p,q):
#       for int points in 200*200
#       tolerate non-int but then less precise
        sd = (p.x-q.x)**2 + (p.y-q.y)**2
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
        self.routine = 'init_techtree'
        self.log_fail((type(facto) in [UpgradeId,UnitTypeId]),'first arg')
        self.log_fail((type(barra) in [UpgradeId,UnitTypeId]),'second arg')
        self.techtree.append( (facto,barra) )

    def init_cradle(self,mari,barra):
        self.routine = 'init_cradle'
        self.log_fail((type(mari) in [UpgradeId,UnitTypeId]),'first arg')
        self.log_fail(barra in self.all_structures,'second arg')
        self.cradle.append( (mari,barra) )
        self.techtree.append( (mari,barra) )

    def compute_all_things(self):
#       pairs from cradle are also in techtree
        self.routine = 'compute_all_things'
        self.all_things = set()
        for pair in self.techtree:
            something = pair[0]
            self.all_things.add(something)
            something = pair[1]
            self.all_things.add(something)

    def check_techtree(self,facto) -> bool:
        self.routine = 'check_techtree'
        cando = True
        for pair in self.techtree:
            if pair[0] == facto:
                cando = cando and self.we_have_a(pair[1])
        return cando

    def check_future_techtree(self,facto) -> bool:
        self.routine = 'check-future_techtree'
        cando = True
        for pair in self.techtree:
            if pair[0] == facto:
                cando = cando and self.we_started_a(pair[1])
        return cando


    def init_army(self,thing,dura,supply):
        self.routine = 'init_army'
        if thing != SCV:
            self.all_army.append(thing)
            self.supply_of_army[thing] = supply
        self.builddura_of_thing[thing] = dura

    def init_upgrade(self,thing,time):
        self.routine = 'init_upgrade'
        self.all_upgrades.append(thing)
        self.builddura_of_thing[thing] = time


    def we_have_a(self,barra) -> bool:
        self.routine = 'we_have_a'
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
            else:
                have = (len(self.units(barra).ready) > 0)
        return have

    def we_started_a(self,barra) -> bool:
        self.routine = 'we_started_a'
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
    #               plans and building ones are included
                for scvt in self.structure_of_trabu_scvt:
                    have = have or (self.structure_of_trabu_scvt[scvt] == barra)
            else:
                have = (self.already_pending(barra) > 0.01) or (len(self.units(barra).ready) > 0)
        return have

    def we_started_amount(self,barra) -> int:
        self.routine = 'we_started_amount'
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
                elif barra == WIDOWMINE:
                    have = have + self.units(WIDOWMINEBURROWED).amount
        return have


#*********************************************************************************************************************

    def get_cost(self,building) -> Dict[str,float]:
        return self.calculate_cost(building)

    def can_pay(self,thing) -> bool:
        cost = self.get_cost(thing)
        return (self.minerals >= cost.minerals) and (self.vespene >= cost.vespene)

    def bug_can_pay(self,upg) -> bool:
        self.routine = 'bug_can_pay'
#       circumvent a bug
        cost_minerals = 9999
        cost_vespene = 9999
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
        return (self.minerals >= cost_minerals) and (self.vespene >= cost_vespene)

#*********************************************************************************************************************

    def get_layout(self):
        self.routine = 'get_layout'
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
        for rock in self.destructables:
            here = rock.position
            # until now, only integers are seen. Approximated 3x3.
            layout_if.layout[round(here.x-1)][round(here.y-1)] = 1
            layout_if.layout[round(here.x-1)][round(here.y+0)] = 1
            layout_if.layout[round(here.x-1)][round(here.y+1)] = 1
            layout_if.layout[round(here.x+0)][round(here.y-1)] = 1
            layout_if.layout[round(here.x+0)][round(here.y+0)] = 1
            layout_if.layout[round(here.x+0)][round(here.y+1)] = 1
            layout_if.layout[round(here.x+1)][round(here.y-1)] = 1
            layout_if.layout[round(here.x+1)][round(here.y+0)] = 1
            layout_if.layout[round(here.x+1)][round(here.y+1)] = 1



    #*********************************************************************************************************************

#   fix secondary information
#   call just before using count_of_job when precize numbers are important
    def fix_count_of_job(self):
        self.routine = 'fix_count_of_job'
#       count_of_job
        for j in self.good_jobs + self.bad_jobs:
            self.count_of_job[j] = 0
        for scvt in self.job_of_scvt:
            j = self.job_of_scvt[scvt]
            self.count_of_job[j] = self.count_of_job[j]+1

    def fix_count_of_mimt(self):
        self.routine = 'fix_count_of_mimt'
#       calculate the amount of gatherers on each mineral, using mimt_of_scvt
        self.count_of_mimt = {}
        for mimt in self.all_mimt:
            self.count_of_mimt[mimt] = 0
        for scvt in self.mimt_of_scvt:
            mimt = self.mimt_of_scvt[scvt]
            if mimt in self.all_mimt:
                self.count_of_mimt[mimt] = self.count_of_mimt[mimt]+1

    def fix_count_of_gast(self):
        self.routine = 'fix_count_of_gast'
#       calculate the amount of gatherers on each gas, using gast_of_scvt
        self.count_of_gast = {}
        for gast in self.all_gast:
            self.count_of_gast[gast] = 0
        for scvt in self.gast_of_scvt:
            gast = self.gast_of_scvt[scvt]
            if gast in self.all_gast:
                self.count_of_gast[gast] = self.count_of_gast[gast]+1
        for gast in self.all_gast:
            cg = self.count_of_gast[gast]
            self.log_workers('count_of_gast['+str(gast)+'] = '+str(cg))

    def maxmimminers(self) -> int:
        return len(self.all_mimt) * 2

    def maxgasminers(self) -> int:
        return len(self.all_gast) * 3


    def mimminer_vacatures(self) -> int:
        return self.maxmimminers() - len(self.mimt_of_scvt)

    def gasminer_vacatures(self) -> int:
        return self.maxgasminers() - len(self.gast_of_scvt)

    # some routines with t=(t[0],t[1]) notation

    def get_neighbours(self, square):
        self.neighbours = set()
        self.neighbours.add((square[0] - 1, square[1] + 0))
        self.neighbours.add((square[0] + 0, square[1] - 1))
        self.neighbours.add((square[0] + 1, square[1] + 0))
        self.neighbours.add((square[0] + 0, square[1] + 1))
        self.neighbours.add((square[0] - 1, square[1] - 1))
        self.neighbours.add((square[0] + 1, square[1] - 1))
        self.neighbours.add((square[0] + 1, square[1] + 1))
        self.neighbours.add((square[0] - 1, square[1] + 1))


    def get_basetop(self):
        # temporary draw the wall (armory to prevent add-on)
        self.write_layout(SUPPLYDEPOT,self.wall_depot0_pos)
        self.write_layout(SUPPLYDEPOT,self.wall_depot1_pos)
        self.write_layout(ARMORY,self.wall_barracks_pos)
        # get an empty square
        square = (round(self.start_location.position.x-0.5),round(self.start_location.position.y-0.5))
        while layout_if.layout[square[0]][square[1]] != 0:
            square = (square[0]+1,square[1])
        # expand that to the basetop
        self.basetop = set([square])
        edge = set([square])
        while (len(edge) > 0):
            newedge = set()
            for square in edge:
                self.get_neighbours(square)
                for nsquare in self.neighbours:
                    if nsquare not in self.basetop:
                        if layout_if.layout[nsquare[0]][nsquare[1]] == 0:
                            newedge.add(nsquare)
            self.basetop = self.basetop | newedge
            edge = newedge.copy()
        # undraw the wall
        self.erase_layout(SUPPLYDEPOT,self.wall_depot0_pos)
        self.erase_layout(SUPPLYDEPOT,self.wall_depot1_pos)
        self.erase_layout(ARMORY,self.wall_barracks_pos)


    def belongs_to(self, towpos: Point2, point: Point2) -> bool:
        if (towpos == self.start_location.position) and (len(self.basetop) > 0):
            square = (round(point.x-0.5),round(point.y-0.5))
            return (square in self.basetop)
        else:
            return self.near(towpos,point,20)

    # END OF some routines with t=(t[0],t[1]) notation

    #   get nearest
    def get_near_scvt_to_goodjob(self,point) -> int:
        self.routine = 'get_near_scvt_to_goodjob'
        stuck = set() # scvt for scvs with too little movespace
        reachset = set() # reachable squares for the best scv
        while len(reachset) < 10:
            best_sdist = 80000
            best_scvt = self.notag
            for scv in self.units(SCV):
                scvt = scv.tag
                if (scvt in self.all_scvt) and (scvt not in stuck):
                    if self.job_of_scvt[scvt] in self.bad_jobs:
                        sd = self.sdist(scv.position,point)
    #                   accept idler if 1.7 times as far
                        if self.job_of_scvt[scvt] in ('idler','applicant','fleeer','suicider'):
                            sd = sd/3
    #                   accept mimminer if 1.4 times as far
                        if self.job_of_scvt[scvt] == 'mimminer':
                            sd = sd/2
                        if sd < best_sdist:
                            best_sdist = sd
                            best_scvt = scvt
                            best_scv = scv
            scvt = best_scvt
            scv = best_scv
            # check whether it is stuck
            scvhome = (round(scv.position.x-0.5),round(scv.position.y-0.5))
            smallset = set()
            reachset = set([scvhome])
            while (len(smallset) < len(reachset)) and (len(reachset)<10):
                smallset = reachset.copy()
                for square in smallset:
                    self.get_neighbours(square)
                    for nsquare in self.neighbours:
                        if layout_if.layout[nsquare[0]][nsquare[1]] in (0,2):
                            reachset.add(nsquare)
            if len(reachset) < 10:
                stuck.add(scvt)
        self.log_fail((best_sdist < 80000),'no scv left for the good job')
        return scvt

    def get_near_scvt_idler(self,point) -> int:
        self.routine = 'get_near_scvt_idler'
#       suggestion: call    if self.count_of_job['idler'] > 0;
        best_sdist = 80000
        best_scvt = self.notag
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
        self.routine = 'get_near_gast_free'
#       supposes done:   fix_count_of_gast
#       suggestion: call   if self.gasminer_vacatures() > 0:
        best_sdist = 80000
        best_gast = self.notag
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
        self.routine = 'get_near_mimt_free'
#       supposes done:   fix_count_of_mimt
#       suggestion: call   if self.mimminer_vacatures() > 0:
        best_sdist = 80000
        best_mimt = self.notag
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
        self.routine = 'get_near_cct_wanted'
        best_sdist = 80000
        best_cct = self.notag
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


    def get_eggs(self):
        self.eggs = set()
        for pair in self.cradle:
            martype = pair[0]
            dura = self.builddura_of_thing[martype]
            bartype = pair[1]
            if type(martype) == UpgradeId:
                abi = sc2.dicts.unit_research_abilities.RESEARCH_INFO[bartype][martype]['ability']
            elif martype in self.all_labs:
                if bartype == BARRACKS:
                    abi = AbilityId.BUILD_TECHLAB_BARRACKS
                elif bartype == FACTORY:
                    abi = AbilityId.BUILD_TECHLAB_FACTORY
                elif bartype == STARPORT:
                    abi = AbilityId.BUILD_TECHLAB_STARPORT
            else:
                abi = sc2.dicts.unit_train_build_abilities.TRAIN_INFO[bartype][martype]['ability']
            for bar in self.structures(bartype).ready:
                if bar.is_using_ability(abi):
                    progress = bar.orders[0].progress
                    restdura = dura * (1.0 - progress)
                    pos = bar.position
                    self.eggs.add((bar,martype,restdura))


# *********************************************************************************************************************
#  bagofthings, bagoftree, buildseries

    def get_all_future_basepos(self):
        self.routine = 'get_all_future_basepos'
        afb = set()
        for cc in self.all_bases:
            afb.add(cc.position)
        for scvt in self.goal_of_trabu_scvt:
            if self.structure_of_trabu_scvt[scvt] == COMMANDCENTER:
                ccp = self.goal_of_trabu_scvt[scvt]
                afb.add(ccp)
        for (th, pl) in self.buildorder:
            if th == COMMANDCENTER:
                afb.add(pl)
        for (th,pl) in self.recycling:
            if th == COMMANDCENTER:
                afb.add(pl)
        self.all_future_basepos = afb
        

    def find_tobuildwalk_a_place(self, building) -> bool:
        self.routine = 'find_tobuildwalk_a_place'
        self.log_placing(building.name)
        #  Get a random place
        #  If no place could be found, return False
        #  Also for future buildings.
        #  Use goal_of_trabu_scvt, buildorder, check_layout
        if building not in self.all_structures:
            self.log_success('BUG 26006 '+building.name)
        found = False
        # try recycling
        for (th,pl) in self.recycling:
            if (th == building) and (not found):
                found = True
                place = pl
        if found:
            del self.recycling[self.recycling.index((building,place))]
            self.log_placing('using recycling')
        # get place from * tips
        tipsfound = 0
        for nr in range(0, len(self.tips)):
            if (nr not in self.tips_used) and (not found):
                ti = self.tips[nr]
                woord = ti.split()
                if (woord[0] == 'position') and (woord[2] == '*'):
                    if woord[1] == building.name:
                        maybe_place = Point2((float(woord[3]), float(woord[4])))
                        if self.check_layout(building, maybe_place):
                            tipsfound = tipsfound + 1
                            if random.randrange(0, tipsfound) == 0:
                                place = maybe_place
                                maybe_nr = nr
        if tipsfound > 0:
            found = True
            self.tips_used.append(maybe_nr)
            self.log_placing('using a soft placement tip')
        # get place from hard tips
        for nr in range(0, len(self.tips)):
            if (nr not in self.tips_used) and (not found):
                ti = self.tips[nr]
                woord = ti.split()
                if (woord[0] == 'position') and (woord[2] != '*'):
                    if woord[1] == building.name:
                        # in this case, layout is NOT checked
                        place = Point2((float(woord[2]), float(woord[3])))
                        self.tips_used.append(nr)
                        self.log_placing('using a hard placement tip')
                        found = True
        # find a new place directly
        if (building == COMMANDCENTER) and (not found):
            tried = 0
            searc = True
            while searc and (tried < 20):
                place = random.choice(self.expansion_locations_list)
                searc = False
                searc = searc or (not self.check_layout(building, place))
                searc = searc or (self.near(place, self.enemyloc, 50))
                searc = searc or (place in [tow.position for tow in self.all_future_basepos])
                tried = tried + 1
            found = not searc
        elif (building == REFINERY) and (not found):
            # first try with existing bases, then with future bases.
            places = []
            for gey in self.vespene_geyser:
                place = gey.position
                if self.check_layout(building, place):
                    if place not in self.goal_of_trabu_scvt.values():
                        if place not in [pl for (th, pl) in self.buildorder]:
                            for cc in self.all_bases:
                                if self.near(place, cc.position, self.miner_bound):
                                    places.append(place)
            if len(places) > 0:
                place = random.choice(places)
                found = True
            # Then with future bases.
            if not found:
                self.get_all_future_basepos()
                places = []
                for gey in self.vespene_geyser:
                    place = gey.position
                    if self.check_layout(building, place):
                        if place not in self.goal_of_trabu_scvt.values():
                            if place not in [pl for (th, pl) in self.buildorder]:
                                for ccp in self.all_future_basepos:
                                    if self.near(place, ccp, self.miner_bound):
                                        places.append(place)
                if len(places) > 0:
                    place = random.choice(places)
                    found = True
        elif (building in self.all_structures_tobuildwalk) and (not found):
            # normal building
            if len(self.all_bases) > 0:
                # chosen not to build near future bases
                found = False
                while not found:
                    cc = random.choice(self.all_bases)
                    dist = 6
                    if building == MISSILETURRET:
                        dist = random.randrange(-10, 10)
                    fixplace = cc.position.towards(self.game_info.map_center, dist)
                    self.put_on_the_grid(building, fixplace)
                    fixplace = self.function_result_Point2
                    place = fixplace
                    tries = 0
                    while (not self.check_layout(building, place)) and (tries < 100):
                        tries = tries + 1
                        x = fixplace.x + random.randrange(-8, 8)
                        y = fixplace.y + random.randrange(-8, 8)
                        place = Point2((x, y))
                    found = self.check_layout(building, place)
            else:
                fixplace = self.start_location.position
                self.put_on_the_grid(building, fixplace)
                fixplace = self.function_result_Point2
                place = fixplace
                tries = 0
                while (not self.check_layout(building, place)) and (tries < 100):
                    x = fixplace.x + random.randrange(-15, 15)
                    y = fixplace.y + random.randrange(-15, 15)
                    place = Point2((x, y))
                found = self.check_layout(building, place)
        #       
        if found:
            self.function_result_Point2 = place
        else:
            self.log_placing('not found')
        return found

    def uninfest(self, thing: UnitTypeId) -> UnitTypeId:
        self.routine = 'uninfest'
        trans_thing = thing
        if thing in (INFESTEDBARRACKS, INFESTEDFACTORY, INFESTEDBUNKER, INFESTEDSTARPORT):
            if thing == INFESTEDBARRACKS:
                trans_thing = BARRACKS
            elif thing == INFESTEDFACTORY:
                trans_thing = FACTORY
            elif thing == INFESTEDSTARPORT:
                trans_thing = STARPORT
            elif thing == INFESTEDBUNKER:
                trans_thing = BUNKER
        return trans_thing


    def bagoftree_of_bagofthings(self):
        self.routine = 'bagoftree_of_bagofthings'
        # add techtree parents
        bag = self.bagofthings.copy()
        stable = False
        while not stable:
            stable = True
            extra = set()
            for th in bag:
                for pair in self.techtree:
                    if pair[0] == th:
                        otherth = pair[1]
                        haveit = (otherth in bag) or (self.we_started_a(otherth))
                        if not haveit:
                            extra.add(otherth)
                            stable = False
            for th in extra:
                bag.append(th)
        self.bagoftree = bag
        stri = 'bagoftree: '
        for th in self.bagoftree:
            stri = stri + th.name + ' '
        self.log_success(stri)


    def buildseries_of_bagoftree(self):
        self.routine = 'buildseries_of_bagoftree'
        # sort until executable
        toput = self.bagoftree.copy()
        series = []
        while len(toput) > 0:
            for th in toput:
                hasdad = False
                for pair in self.techtree:
                    if pair[0] == th:
                        otherth = pair[1]
                        hasdad = hasdad or (otherth in toput)
                if not hasdad:
                    cando = th
            series.append(cando)
            del toput[toput.index(cando)]
        self.buildseries = series
        stri = 'buildseries: '
        for th in self.buildseries:
            stri = stri + th.name + ' '
        self.log_success(stri)



    def buildorder_of_buildseries(self):
        # buildorder = buildseries + place
        # also: change infested to normal
        self.routine = 'buildorder_of_buildseries'
        self.buildorder = []
        for thing in self.buildseries:
            if thing in self.all_structures_tobuildwalk:
                trans_thing = self.uninfest(thing)
                goal = self.nowhere
                if self.find_tobuildwalk_a_place(thing):
                    goal = self.function_result_Point2
                if goal == self.nowhere:
                    self.log_success('skipping a '+thing.name+' because I found no position!')
                else:
                    self.buildorder.append((trans_thing, goal))
                    self.write_layout(trans_thing, goal)
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
                # get a random cradle place
                # be aware later that this is not optimal
                if len(crad_places)==0:
                    self.log_success('could not place '+thing.name)
                    place = self.nowhere
                else:
                    place = random.sample(crad_places,1)[0]
                self.buildorder.append((thing, place))

# *********************************************************************************************************************
    # buildseries timing optimizing

    def check_buildseries(self) -> bool:
        self.routine = 'check_buildseries'
        # check if a buildseries is possible according to techtree
        is_pos = True
        front = set()
        for thing in self.buildseries:
            if is_pos:
                trans_thing = self.uninfest(thing)
                for pair in self.techtree:
                    if pair[0] == trans_thing:
                        neededthing = pair[1]
                        seen = False
                        if self.we_started_a(neededthing):
                            seen = True
                        if neededthing in front:
                            seen = True
                        is_pos = is_pos and seen
                front.add(trans_thing)
        return is_pos


    def add_sit(self,infa_thing, moment):
        self.routine = 'add_sit'
        thing = self.uninfest(infa_thing)
        basething = thing
        if thing == BARRACKSFLYING:
            basething = BARRACKS
        elif thing == FACTORYFLYING:
            basething = FACTORY
        elif thing == STARPORTFLYING:
            basething = STARPORT
        elif thing in (COMMANDCENTERFLYING, ORBITALCOMMAND, PLANETARYFORTRESS):
            basething = COMMANDCENTER
        self.sit_free.append((basething,moment))
        if basething in self.sit_exist:
            self.sit_exist[basething] = min(self.sit_exist[basething],moment)
        else:
            self.sit_exist[basething] = moment


    def get_sit(self):
        self.routine = 'get_sit'
        # sit_free      list of (thing,moment); freemoment with now=0. Uninfested.
        # sit_exist     dict of [thing] -> moment; readymoment with now=0. Uninfested.
        self.sit_free = []
        self.sit_exist = {}
        now = 0
        #
        # ready things
        for kind in self.all_structures + self.landable:
            for stru in self.structures(kind).ready:
                self.add_sit(kind,0)
        # ignore army, scv
        for upgr in self.all_upgrades:
            progress = self.already_pending_upgrade(upgr)
            if  (progress == 1.0):
                self.add_sit(upgr,0)
        #
        # things not ready yet
        for scv in self.units(SCV):
            scvt = scv.tag
            if scvt in self.goal_of_trabu_scvt:
                goal = self.goal_of_trabu_scvt[scvt]
                thing = self.structure_of_trabu_scvt[scvt]
                pos = scv.position
                build_dura = self.builddura_of_thing[thing]
                if self.job_of_scvt[scvt] == 'traveller':
                    walk_dura = self.dist(pos,goal) / self.walk_speed
                    constructmoment = now + walk_dura
                    finishmoment = now + walk_dura + build_dura
                elif self.job_of_scvt[scvt] == 'builder':
                    # for the small duration where the build hasn't started
                    finishmoment = now + build_dura
                    for thatone in self.structures(thing):
                        if thatone.position == goal:
                            # the build has started and is payed; undo the reserving
                            finishmoment = now + build_dura*(1.0-thatone.build_progress)
                self.add_sit(thing,finishmoment)
        # structures without tobuildwalk; lab, pf
        for thing in self.all_structures:
            if thing not in self.all_structures_tobuildwalk:
                for thatone in self.structures(thing):
                    if thatone.build_progress < 1.0:
                        build_dura = self.builddura_of_thing[thing]
                        finishmoment = now + build_dura * (1.0 - thatone.build_progress)
                        self.add_sit(thing, finishmoment)
        # ambitions; pf or lab
        for strt in self.ambition_of_strt:
            thing = self.ambition_of_strt[strt]
            for crad in self.all_structures:
                for cradje in self.structures(crad):
                    if (cradje.tag == strt):
                        build_dura = self.builddura_of_thing[thing]
                        to_free_dura = 1
                        for (bar,martype,restdura) in self.eggs:
                            if bar == cradje:
                                to_free_dura = restdura
                        finishmoment = now + to_free_dura + build_dura
                        self.add_sit(thing, finishmoment)
        # marine
        for thing in self.all_army:
            for thatone in self.units(thing):
                if thatone.build_progress < 1.0: # doubted code
                    build_dura = self.builddura_of_thing[thing]
                    finishmoment = now + build_dura * (1.0 - thatone.build_progress)
                    self.add_sit(thing, finishmoment)
        # upgrades
        for upgr in self.all_upgrades:
            progress = self.already_pending_upgrade(upgr)
            if  (progress != 0.0) and (progress < 1.0):
                finishmoment = now + self.builddura_of_thing[upgr] * (1.0 - progress)
                self.add_sit(upgr, finishmoment)
        # show
        stri = 'sit_exist:'
        for thing in self.sit_exist:
            moment = self.sit_exist[thing]
            stri = stri+'   '+thing.name+' '+str(moment)
        self.log_buildsit(stri)
        stri = 'sit_free:'
        for (thing,moment) in self.sit_free:
            stri = stri + '   ' + thing.name + ' ' + str(moment)
        self.log_buildsit(stri)



    def dura_buildseries(self) -> int:
        self.routine = 'dura_buildseries'
        # check_buildseries == True
        # duration according to techtree and cradle
        # buildstarts are 5 seconds apart just to get some ordering.
        current_free = self.sit_free.copy() # list of (thing,moment); freemoment with now=0
        current_exist = self.sit_exist.copy() # dict of [thing] -> moment; readymoment with now=0
        current_moment = 0
        max_end = 0
        for infa_thing in self.buildseries:
            thing = self.uninfest(infa_thing)
            start_moment = current_moment
            # wait for tech
            for pair in self.techtree:
                if pair[0] == thing:
                    neededthing = pair[1]
                    first_moment = current_exist[neededthing] # BUG if the needed barracks is flying
                    start_moment = max(start_moment,first_moment)
            # maybe wait for cradle
            for pair in self.cradle:
                if pair[0] == thing:
                    cradle = pair[1]
                    first_moment = 9999
                    for (thcr,mo) in current_free:
                        if thcr == cradle:
                            if mo < first_moment:
                                chosen = (thcr,mo)
                                first_moment = mo
                    # remove 1 chosen from current_free
                    del current_free[current_free.index(chosen)]
                    start_moment = max(start_moment,first_moment)
                    end_moment = start_moment + self.builddura_of_thing[thing]
                    current_free.append((cradle,end_moment))
            # start_moment is calculated
            current_moment = start_moment + 5  # to keep the order of the series
            end_moment = start_moment + self.builddura_of_thing[thing]
            current_free.append((thing,end_moment))
            if thing not in current_exist:
                current_exist[thing] = end_moment
            # if it exists, that one will end earlier
            max_end = max(max_end,end_moment)
        return max_end


    def optimize_buildseries(self):
        self.routine = 'optimize_buildseries'
        self.get_sit()
        best_buildseries = self.buildseries.copy()
        if not self.check_buildseries():
            self.log_success('flying cat')
        best_dura = self.dura_buildseries()
        self.log_buildseries('Before: ' + str(best_dura) + ': ')
        improved = True
        while improved:
            improved = False
            for nr in range(1,len(best_buildseries)): # skipping 0
                # copy, swap nr-1 and nr
                self.buildseries = []
                for ix in range(0,len(best_buildseries)):
                    if ix == nr - 1:
                        self.buildseries.append(best_buildseries[ix+1])
                    elif ix == nr:
                        self.buildseries.append(best_buildseries[ix-1])
                    else:
                        self.buildseries.append(best_buildseries[ix])
                if self.check_buildseries():
                    dura = self.dura_buildseries()
                    self.log_buildseries('trying: ' + str(dura) + ': ')
                    if dura < best_dura:
                        improved = True
                        best_buildseries = self.buildseries.copy()
                        best_dura = dura
        self.buildseries = best_buildseries.copy()
        self.log_buildseries('After: ')




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
#   the finishmoment of already planned buildings is calculated and used for the techtree and the emerging free scv
#   the planning does start-to-construct in the order given in buildorder
#
#   IN:
#       the current game situation and administration, those are called the "situation".
#       buildorder [(BARRACKS,(16,40)),(SUPPLYDEPOT,(119,3)),(MARINE,(16,40)),...
#   OUT:
#       planning [(tagJohn,BARRACKS,(16,40),4,17,22)
#                ,(tagMohamad,SUPPLYDEPOT,(119,3),8,23,30)
#                ,(notag,MARINE,(16,40),220,220,265),...
#       The 3 moments are: start-walk, start-construct,end-construct
#       For not tobuildwalk constructions and trainings, start_walk==start_construct and the tag is notag
#   LOCAL:
#       current_moment 17
#       current_spendable_minerals 254
#       current_spendable_vespene 0
#       current_free {(tagjohn,pos(14,107),since15),...
#           using buildplan (tagjohn,thingBARRACKS,goal(16,40),startwalk14,startconstruct17,finish19)
#       current_walking {buildplan,...
#       current_constructing {buildplan,...
#           using trainplan (thingMARINE,place(16,40),starttrain20,finish40)
#       current_training {trainplan, ...
#       current_thingkinds {thingBARRACKS,...    (finish ones)
#       current_buildings_and_parts {(thingBARRACKS,x115,y87),...     (started construction, or finished)
#       current_events {(17,'start walking',tagjohn,goal(16,40))
#                      ,(4,'start constructing',tageddy,goal(119,3))
#                      ,(19,'finish constructing',tagjohn,goal(16,40))
#                      ,(2,'finish training',goal(16,40))
#


    def get_situation(self):
        routine = 'get_situation'
        now = 0
        self.situation_spendable_minerals = self.minerals
        self.situation_spendable_vespene = self.vespene
        self.situation_walking = set()
        self.situation_constructing = set()
        self.situation_training = set()
        self.situation_ambition = set()
        self.situation_growing = set()
        self.situation_thingkinds = set()
        #   buildings are identified by place not tag, so we can add future buildings
        self.situation_buildings_and_parts = set()
        self.fix_count_of_job()
        self.situation_mimminers = self.count_of_job['mimminer']
        self.situation_gasminers = self.count_of_job['gasminer']
        # for the techtree:
        self.situation_thingkinds = set()
        for kind in self.all_things:
            if self.we_have_a(kind):
                self.situation_thingkinds.add(kind)
        # store started buildplans and trainplans
        for scv in self.units(SCV):
            scvt = scv.tag
            if scvt in self.goal_of_trabu_scvt:
                goal = self.goal_of_trabu_scvt[scvt]
                thing = self.structure_of_trabu_scvt[scvt]
                pos = scv.position
                build_dura = self.builddura_of_thing[thing]
                if self.job_of_scvt[scvt] == 'traveller':
                    walk_dura = self.dist(pos,goal) / self.walk_speed
                    constructmoment = now + walk_dura
                    finishmoment = now + walk_dura + build_dura
                    buildplan = (scvt, thing, goal, -1, constructmoment, finishmoment)
                    self.situation_walking.add(buildplan)
                elif self.job_of_scvt[scvt] == 'builder':
                    finishmoment = now + build_dura
                    for thatone in self.structures(thing):
                        if thatone.position == goal:
                            finishmoment = now + build_dura*(1.0-thatone.build_progress)
                    self.situation_buildings_and_parts.add((thing, goal.x, goal.y))
                    buildplan = (scvt,thing,goal,-1,-1,finishmoment)
                    self.situation_constructing.add(buildplan)
        # structures without tobuildwalk; lab, pf
        scvt = self.notag
        for thing in self.all_structures:
            if thing not in self.all_structures_tobuildwalk:
                for thatone in self.structures(thing):
                    if thatone.build_progress < 1.0:
                        goal = thatone.position
                        build_dura = self.builddura_of_thing[thing]
                        finishmoment = now + build_dura * (1.0 - thatone.build_progress)
                        buildplan = (self.notag, thing, goal, -1, -1, finishmoment)
                        self.situation_growing.add(buildplan)
        # ambitions; pf or lab
        for strt in self.ambition_of_strt:
            thing = self.ambition_of_strt[strt]
            for crad in self.all_structures:
                for cradje in self.structures(crad):
                    if (cradje.tag == strt):
                        goal = cradje.position
                        build_dura = self.builddura_of_thing[thing]
                        to_free_dura = 1
                        for (bar,martype,restdura) in self.eggs:
                            if bar == cradje:
                                to_free_dura = restdura
                        startgrowmoment = now + to_free_dura
                        finishmoment = now + to_free_dura + build_dura
                        buildplan = (self.notag, thing, goal, -1, startgrowmoment, finishmoment)
                        self.situation_ambition.add(buildplan)
        # marine
        for thing in self.all_army:
            for thatone in self.units(thing):
                if thatone.build_progress < 1.0: # doubted code
                    goal = thatone.position
                    build_dura = self.builddura_of_thing[thing]
                    finishmoment = now + build_dura * (1.0 - thatone.build_progress)
                    trainplan = (thing, goal, -1, finishmoment)
                    self.situation_training.add(trainplan)
                    self.log_success('GOOD, this code is reached 89768564')
        # upgrades
        for upgr in self.all_upgrades:
            progress = self.already_pending_upgrade(upgr)
            if  (progress != 0.0) and (progress < 1.0):
                # get its place
                for (bar,martype,restdura) in self.eggs:
                    if martype == upgr:
                        goal = bar.position
                        finishmoment = now + restdura
                        trainplan = (upgr, goal, -1, finishmoment)
                        self.situation_training.add(trainplan)
        # restore dependencies:
        # expected are only little shifts.
        # startconstructing may have to wait for finishconstructing (techtree)
        # expect no startgrowing ordered before finishconstructing
        # startgrowing may have to wait for finishtraining (in use)
        #
        # startconstructing may have to wait for finishconstructing (techtree)
        todel = set()
        toadd = set()
        for bp in self.situation_walking:
            (scvt, thing, goal, minusone, startconstr, finishmoment) = bp
            for pair in self.techtree:
                if pair[0] == thing:
                    neededthing = pair[1]
                    if neededthing not in self.situation_thingkinds:
                        minfi = 9999
                        for (sv,th,go,sw,sc,fi) in self.situation_constructing | self.situation_walking:
                            if th == neededthing:
                                minfi = min(minfi,fi)
                        if startconstr < minfi:
                            if minfi >= finishmoment:
                                self.log_success('bug 756473: tech predecessor not started '+thing.name+' '+neededthing.name)
                            else:
                                todel.add(bp)
                                toadd.add((scvt,thing,goal,minusone,minfi,finishmoment))
        self.situation_walking = (self.situation_walking | toadd) - todel
        #
        # situation_events
        self.situation_events = set()
        for (upgr, goal, minusone, finishmoment) in self.situation_training:
            self.situation_events.add((finishmoment, 'finish training', self.notag, goal))
        for (nonotag, thing, goal, minusone, startgrowmoment, finishmoment) in self.situation_ambition:
            self.situation_events.add((startgrowmoment, 'start growing', self.notag, goal))
            self.situation_events.add((finishmoment, 'finish growing', self.notag, goal))
        for (nonotag, thing, goal, minusone, minusother, finishmoment) in self.situation_growing:
            self.situation_events.add((finishmoment, 'finish growing', self.notag, goal))
        for (scvt,thing,goal,minusone,minusother,finishmoment) in self.situation_constructing:
            self.situation_events.add((finishmoment, 'finish constructing', scvt, goal))
        for (scvt, thing, goal, minusone, constructmoment, finishmoment) in self.situation_walking:
            self.situation_events.add((constructmoment, 'start constructing', scvt, goal))
            self.situation_events.add((finishmoment, 'finish constructing', scvt, goal))
        # potential builders
        self.situation_free = set()
        for scv in self.units(SCV):
            scvt = scv.tag
            if scvt in self.all_scvt:
                if self.job_of_scvt[scvt] in self.bad_jobs:
                    self.situation_free.add((scvt,scv.position,now))
        # to make marines:
        # include unfinish buildings    to prevent a short disappearance
        # a lab has its own position, not its cradle's.
        self.situation_buildings_and_parts = set()
        for thing in self.all_structures:
            for thatone in self.structures(thing):
                self.situation_buildings_and_parts.add((thing, thatone.position.x, thatone.position.y))


    def planning_of_buildorder(self,extragas,extraminerals):
        # usually extragas = 0. Here you can experiment with an extra gasminer
        routine = 'planning_of_buildorder'
        if (extragas == 0) and (extraminerals == 0):
            self.log_planning('start')
        self.planning = []
        # The situation is taken into current, which will shift during the look-ahead.
        current_spendable_minerals = self.situation_spendable_minerals
        current_spendable_vespene = self.situation_spendable_vespene
        current_walking = self.situation_walking.copy()
        current_constructing = self.situation_constructing.copy()
        current_training = self.situation_training.copy()
        current_ambition = self.situation_ambition.copy()
        current_growing = self.situation_growing.copy()
        current_thingkinds = self.situation_thingkinds.copy()
        current_buildings_and_parts = self.situation_buildings_and_parts.copy()
        current_events = self.situation_events.copy()
        current_mimminers = self.situation_mimminers+extraminerals
        current_gasminers = self.situation_gasminers+extragas
        current_free = self.situation_free.copy()
        current_moment = 0
#
        plannable = True
        for (beautiful_thing,beautiful_place) in self.buildorder:
            if plannable:
                # MAKE A BEAUTIFUL_BUILDPLAN, PLAN_MOMENT AND EVENTS, AND APPEND BP TO PLANNING
                started = False
                for buildplan in current_walking | current_ambition | current_constructing | current_growing:
                    (scvt, th, pos, sr, sc, fi) = buildplan
                    if (th == beautiful_thing) and (pos == beautiful_place):
                        beautiful_buildplan = buildplan
                        started = True
                        self.planning.append(beautiful_buildplan)
                        plan_moment = sc
                if (not started):
                    # calculate times
                    if (extragas == 0) and (extraminerals == 0):
                        self.log_planning('Planning a '+beautiful_thing.name)
                    cost = self.get_cost(beautiful_thing)
                    build_dura = self.builddura_of_thing[beautiful_thing]
                    total_dura = 0
        #           mim_dura
                    mim_gap = cost.minerals - current_spendable_minerals
                    if (mim_gap <= 0):
                        mim_dura = 0
                    elif current_mimminers == 0:
                        mim_dura = 9999
                    else:
                        mim_dura = mim_gap / (current_mimminers*self.mim_speed)
                    total_dura = max(total_dura,mim_dura)
        #           gas_dura
                    gas_gap = cost.vespene - current_spendable_vespene
                    if (gas_gap <= 0) or (cost.vespene == 0):
                        gas_dura = 0
                    elif current_gasminers == 0:
                        gas_dura = 9999
                    else:
                        gas_dura = gas_gap / (current_gasminers*self.gas_speed)
                    total_dura = max(total_dura, gas_dura)
                    # tree_dura
                    tree_dura = 0
                    for pair in self.techtree:
                        if pair[0] == beautiful_thing:
                            barra = pair[1]
                            if barra not in current_thingkinds:
                                # expect it to be started; the buildplan should respect the techtree
                                # barra could be in constructing
                                earliest = 9999
                                for (scvt,thing,goal,startwalk,startconstruct,finish) in current_constructing:
                                    if thing == barra:
                                        l_build_dura = finish - startconstruct
                                        for thatone in self.structures(thing):
                                            if thatone.position == goal:
                                                progress = thatone.build_progress
                                                l_build_dura = l_build_dura * (1.0 - progress)
                                        moment = current_moment + l_build_dura
                                        if moment < earliest:
                                            earliest = moment
                                # or barra could be in walking
                                for (scvt,thing,goal,startwalk,startconstruct,finish) in current_walking:
                                    if thing == barra:
                                        l_walk_dura = startconstruct - startwalk
                                        l_build_dura = finish - startconstruct
                                        for scv in self.units(SCV):
                                            if scv.tag == scvt:
                                                pos = scv.position
                                                l_walk_dura = self.dist(pos, goal) / self.walk_speed
                                        moment = current_moment + l_walk_dura + l_build_dura
                                        if moment < earliest:
                                            earliest = moment
                                # or barra (lab, pf) could be in ambition
                                for (scvt,thing,goal,startambition,startgrow,finish) in current_ambition:
                                    if thing == barra:
                                        l_ambition_dura = 10
                                        l_grow_dura = finish - startgrow
                                        moment = current_moment + l_ambition_dura + l_grow_dura
                                        if moment < earliest:
                                            earliest = moment
                                # or barra (lab, pf) could be in growing
                                for (dum,thing,goal,startambition,startgrow,finish) in current_growing:
                                    if thing == barra:
                                        l_build_dura = finish - startgrow
                                        for thatone in self.structures(thing):
                                            if thatone.position == goal:
                                                progress = thatone.build_progress # doubted code
                                                l_build_dura = l_build_dura * (1.0 - progress)
                                        moment = current_moment + l_build_dura
                                        if moment < earliest:
                                            earliest = moment
                                dura = earliest - current_moment
                                tree_dura = max(tree_dura,dura)
                                # marine, upg:
                                for (thing, goal, startconstruct, finish) in current_training:
                                    if thing == barra:
                                        l_build_dura = finish - startconstruct
                                        for thatone in self.structures(thing):
                                            if thatone.position == goal:
                                                progress = thatone.build_progress # doubted code
                                                l_build_dura = l_build_dura * (1.0 - progress)
                                        moment = current_moment + l_build_dura
                                        if moment < earliest:
                                            earliest = moment
                                dura = earliest - current_moment
                                tree_dura = max(tree_dura, dura)
                    total_dura = max(total_dura,tree_dura)
                    # walk_dura
                    if beautiful_thing in self.all_structures_tobuildwalk:
                        # find a beautiful scv
                        beautiful_scvt = self.notag
                        arrive_quality = 9999
                        for (scvt,pos,since) in current_free:
                            walk_dura = self.dist(pos,beautiful_place) / self.walk_speed
                            could_arrive = max(current_moment,(since + walk_dura))
                            # next constants weigh reusing an scv that has to walk a little versus getting a fresh scv from far
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
                        beautiful_scvt = self.notag
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
                                    maxfinish = current_moment
                                    for (scvt, thi, goal, startwalk, startconstruct, finish) in current_constructing:
                                        if (thi == cradle) and (goal.x == x) and (goal.y == y):
                                            maxfinish = max(maxfinish,finish)
                                    # it can be in training
                                    for (thi,goal,start,finish) in current_training:
                                        if (goal.x==x) and (goal.y==y):
                                            maxfinish = max(maxfinish,finish)
                                    this_cradle_dura = maxfinish - current_moment
                                    cradle_dura = min(cradle_dura,this_cradle_dura)
                            # there could be some in walking
                            for (scvt, th, goal, startwalk, startconstruct, finish) in current_walking:
                                if th == cradle:
                                    maxfinish = finish
                                    # it can be in training
                                    for (thi,traingoal,start,finish2) in current_training:
                                        if (traingoal == goal):
                                            maxfinish = max(maxfinish,finish2)
                                    this_cradle_dura = maxfinish - current_moment
                                    cradle_dura = min(cradle_dura,this_cradle_dura)
                            # there could be some in ambition (e.g. the barrackstechlab for the concussiveupgrade)
                            for (scvt, th, goal, startwalk, startconstruct, finish) in current_ambition:
                                if th == cradle:
                                    maxfinish = finish
                                    this_cradle_dura = maxfinish - current_moment
                                    cradle_dura = min(cradle_dura, this_cradle_dura)
                            # there could be some in growing
                            for (scvt, th, goal, startwalk, startconstruct, finish) in current_growing:
                                if th == cradle:
                                    maxfinish = finish
                                    this_cradle_dura = maxfinish - current_moment
                                    cradle_dura = min(cradle_dura, this_cradle_dura)
                    total_dura = max(total_dura,cradle_dura)
                    if (extragas == 0) and (extraminerals == 0):
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
                        if (extragas == 0) and (extraminerals == 0):
                            self.log_planning('Planning failed')
                    else:
                        if beautiful_thing in self.all_structures_tobuildwalk:
                            beautiful_buildplan = (beautiful_scvt,beautiful_thing,beautiful_place,plan_moment - walk_dura,plan_moment,plan_moment + build_dura)
                            current_events.add((plan_moment - walk_dura,'start walking',beautiful_scvt,beautiful_place))
                            current_events.add((plan_moment,'start constructing',beautiful_scvt,beautiful_place))
                            current_events.add((plan_moment + build_dura,'finish constructing',beautiful_scvt,beautiful_place))
                        elif beautiful_thing in self.all_structures:
                            # pf,lab
                            beautiful_buildplan = (
                            self.notag, beautiful_thing, beautiful_place, plan_moment-20, plan_moment, plan_moment + build_dura)
                            current_events.add((plan_moment-20, 'start ambition', self.notag, beautiful_place))
                            current_events.add((plan_moment, 'start growing', self.notag, beautiful_place))
                            current_events.add((plan_moment + build_dura, 'finish growing', self.notag, beautiful_place))
                        else:
                            # marine,upgrade
                            beautiful_buildplan = (self.notag,beautiful_thing,beautiful_place,plan_moment,plan_moment,plan_moment + build_dura)
                            beautiful_trainplan = (beautiful_thing,beautiful_place,plan_moment,plan_moment + build_dura)
                            current_events.add((plan_moment, 'start training', self.notag, beautiful_place))
                            current_events.add((plan_moment + build_dura, 'finish training', self.notag, beautiful_place))
                            # forward the time to "start constructing"
                        self.planning.append(beautiful_buildplan)
                # play events out
                if plannable:
                    if (extragas == 0) and (extraminerals == 0):
                        self.log_planning_bp(beautiful_buildplan)
                    at_construction_start = (plan_moment <= 0)
                    while (not at_construction_start) and (len(current_events) > 0):
                        nextmoment = 9999
                        for (moment,stri,scvt,goal) in current_events:
                            if (moment<nextmoment):
                                nextmoment = moment
                        # happen all events at nextmoment
                        # in the order: finish, start walk, start build
                        del_current_events = set()
                        for (moment, stri, escvt, egoal) in current_events:
                            if (moment == nextmoment) and (stri == 'finish training'):
                                del_current_events.add((moment, stri, escvt, egoal))
                                del_current_training = set()
                                for trainplan in current_training:
                                    (thing, goal, starttrain, finish) = trainplan
                                    if (goal == egoal) and (moment == finish):
                                        del_current_training.add(trainplan)
                                        current_thingkinds.add(thing)
                                current_training = current_training - del_current_training
                        for (moment, stri, escvt, egoal) in current_events:
                            if (moment == nextmoment) and (stri == 'finish constructing'):
                                del_current_events.add((moment, stri, escvt, egoal))
                                del_current_constructing = set()
                                for buildplan in current_constructing:
                                    (tag, thing, goal, startwalk,startconstruct,finish) = buildplan
                                    if (tag == escvt) and (goal == egoal) and (moment == finish):
                                        del_current_constructing.add(buildplan)
                                        current_free.add((tag,goal,finish))
                                        current_thingkinds.add(thing)
                                current_constructing = current_constructing - del_current_constructing
                        for (moment, stri, escvt, egoal) in current_events:
                            if (moment == nextmoment) and (stri == 'finish growing'):
                                del_current_events.add((moment, stri, escvt, egoal))
                                del_current_growing = set()
                                for buildplan in current_growing:
                                    (tag, thing, goal, startambition,startgrow,finish) = buildplan
                                    if (tag == escvt) and (goal == egoal) and (moment == finish):
                                        del_current_growing.add(buildplan)
                                        current_thingkinds.add(thing)
                                current_growing = current_growing - del_current_growing
                        for (moment,stri,escvt,egoal) in current_events:
                            if (moment == nextmoment) and (stri == 'start walking'):
                                del_current_events.add((moment,stri,escvt,egoal))
                                del_current_free = set()
                                for (tag, position, since) in current_free:
                                    if tag == escvt:
                                        del_current_free.add((tag, position, since))
                                        current_walking.add(beautiful_buildplan)
                                current_free = current_free - del_current_free
                        for (moment,stri,escvt,egoal) in current_events:
                            if (moment == nextmoment) and (stri == 'start ambition'):
                                del_current_events.add((moment,stri,escvt,egoal))
                                current_ambition.add(beautiful_buildplan)
                        for (moment, stri, escvt, egoal) in current_events:
                            if (moment == nextmoment) and (stri == 'start constructing'):
                                del_current_events.add((moment, stri, escvt, egoal))
                                del_current_walking = set()
                                for buildplan in current_walking:
                                    (tag, thing, goal, startwalk,startconstruct,finish) = buildplan
                                    if (tag == escvt) and (goal == egoal) and (moment == startconstruct):
                                        del_current_walking.add(buildplan)
                                        current_constructing.add(buildplan)
                                        cost = self.get_cost(thing)
                                        current_spendable_minerals = current_spendable_minerals - cost.minerals
                                        current_spendable_vespene = current_spendable_vespene - cost.vespene
                                        current_buildings_and_parts.add((thing, goal.x, goal.y))
                                        if (thing == beautiful_thing) and (goal == beautiful_place):
                                            at_construction_start = True
                                current_walking = current_walking - del_current_walking
                        for (moment, stri, escvt, egoal) in current_events:
                            if (moment == nextmoment) and (stri == 'start growing'):
                                del_current_events.add((moment, stri, escvt, egoal))
                                del_current_ambition = set()
                                for buildplan in current_ambition:
                                    (tag, thing, goal, startambition,startgrow,finish) = buildplan
                                    if (tag == escvt) and (goal == egoal) and (moment == startgrow):
                                        del_current_ambition.add(buildplan)
                                        current_growing.add(buildplan)
                                        cost = self.get_cost(thing)
                                        current_spendable_minerals = current_spendable_minerals - cost.minerals
                                        current_spendable_vespene = current_spendable_vespene - cost.vespene
                                        current_buildings_and_parts.add((thing, goal.x, goal.y))
                                        if (thing == beautiful_thing) and (goal == beautiful_place):
                                            at_construction_start = True
                                current_ambition = current_ambition - del_current_ambition
                        for (moment, stri, escvt, egoal) in current_events:
                            if (moment == nextmoment) and (stri == 'start training'):
                                del_current_events.add((moment, stri, escvt, egoal))
                                # that must be the beautiful marine, as the build has an order
                                at_construction_start = True
                                current_training.add(beautiful_trainplan)
                                cost = self.get_cost(beautiful_thing)
                                current_spendable_minerals = current_spendable_minerals - cost.minerals
                                current_spendable_vespene = current_spendable_vespene - cost.vespene
                        current_events = current_events - del_current_events
                    if len(current_events) == 0:
                        self.log_success('INTERNAL ERROR 227860 '+beautiful_thing.name)
    #               grow
                    dura = plan_moment - current_moment
                    current_spendable_minerals = current_spendable_minerals+dura*(current_mimminers*self.mim_speed)
                    current_spendable_vespene = current_spendable_vespene+dura*(current_gasminers*self.gas_speed)
                    current_moment = plan_moment


    def optimize_planning(self):
        # in: planning
        # out: planning
        # get_situation should be done
        routine = 'optimize_planning'
        best_planning = self.planning.copy()
        endtime0 = 0
        items0 = len(self.planning)
        for (scvt, thing, goal, sw, sc, finish) in self.planning:
            endtime0 = max(endtime0, finish)
        # experiment with extra gas
        if (self.situation_mimminers>0) and (self.situation_gasminers>0):
            self.planning_of_buildorder(1,-1)
            endtimealt = 0
            itemsalt = len(self.planning)
            for (scvt,thing, goal, sw,sc,finish) in self.planning:
                endtimealt = max(endtimealt,finish)
            if (endtimealt < endtime0) and (itemsalt == items0):
                self.gas_advice = 1
                best_planning = self.planning.copy()
        # experiment with less gas
        if (self.situation_mimminers>0) and (self.situation_gasminers>0):
            self.planning_of_buildorder(-1,1)
            endtimealt = 0
            itemsalt = len(self.planning)
            for (scvt,thing, goal, sw,sc,finish) in self.planning:
                endtimealt = max(endtimealt,finish)
            if (endtimealt < endtime0) and (itemsalt == items0):
                self.gas_advice = -1
                best_planning = self.planning.copy()
        # result
        self.planning = best_planning.copy()



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
        #       ccs in construction nearly finish are included
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
        #   bestbctag is notag or a tag of a living battlecruiser
        just_one_bctag = self.notag
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
                        # self.log_limbo('a '+job+' in limbo '+self.name(scvt))
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
                            # self.log_limbo('a '+job+' in limbo '+self.name(scvt))
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
                    if self.near(gas.position,tow.position,self.miner_bound):
                        self.all_gast.append(gast)
        #   The tag of existing minerals where we want to mine from, in this iteration
        self.all_mimt = []
        for mim in self.mineral_field:
            mimt = mim.tag
            if mim.mineral_contents > 0:
                for tow in self.all_bases:
                    towt = tow.tag
                    if self.near(mim.position,tow.position,self.miner_bound):
                        self.all_mimt.append(mimt) 
        #   job_of_scvt contains the tag of all living scvs
        if self.cheese_scv == None:
            cheesetag = self.notag
        else:
            cheesetag = self.cheese_scv.tag
        new_job_of_scvt = {}
        for scvt in self.all_scvt:
            if scvt in self.job_of_scvt:
                new_job_of_scvt[scvt] = self.job_of_scvt[scvt]
            elif scvt == cheesetag:
                new_job_of_scvt[scvt] = 'cheeser'
                self.log_workers('cheeser came out of the bunker '+self.name(scvt))
            else:
                new_job_of_scvt[scvt] = 'idler'
                self.log_workers('had no job, now is idler '+self.name(scvt))
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
        for scvt in set(self.mimt_of_scvt) - set(new_mimt_of_scvt):
            self.log_workers('from mimt_of_scvt gone is '+str(mimt)+'_of_'+str(scvt))
        self.mimt_of_scvt = new_mimt_of_scvt
        self.fix_count_of_mimt()
        #   restrict gast_of_scvt to existing worker and mineral
        new_gast_of_scvt = {}
        for scvt in self.gast_of_scvt:
            if scvt in self.all_scvt:
                gast = self.gast_of_scvt[scvt]
                if gast in self.all_gast:
                    new_gast_of_scvt[scvt] = gast
        for scvt in set(self.gast_of_scvt) - set(new_gast_of_scvt):
            self.log_workers('from gast_of_scvt gone is '+str(gast)+'_of_'+str(scvt))
        self.gast_of_scvt = new_gast_of_scvt
        self.fix_count_of_gast()
        #   check consistency
        for scvt in self.mimt_of_scvt:
            job = self.job_of_scvt[scvt]
            name = self.name(scvt)
            if (job != 'mimminer'):
                self.log_success('not a mimminer, yet in mimt_of_scvt '+job+' '+name)
        for scvt in self.gast_of_scvt:
            job = self.job_of_scvt[scvt]
            name = self.name(scvt)
            if (job != 'gasminer'):
                self.log_success('not a gasminer, yet in gast_of_scvt ' + job + ' ' + name)
        for scv in self.units(SCV):
            if scv.tag in self.all_scvt:
                job = self.job_of_scvt[scv.tag]
                name = self.name(scv.tag)
                if scv.is_collecting:
                    if (job not in ('mimminer','gasminer','builder')):
                        self.log_success('collecting but wrong job ' + job + ' ' + name)
                else: # not collecting
                    if (job in ('mimminer', 'gasminer')):
                        self.log_success('not collecting but job ' + job + ' ' + name)
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
        #   army_supply
        self.army_supply = 0
        for mar in self.all_army:
            self.army_supply = self.army_supply + self.supply_of_army[mar] * len(self.units(mar))

    #*********************************************************************************************************************

    def endgame(self):
        self.routine = 'endgame'
        # make bagofthings
        self.bagofthings = []  # collect some things to add to bagofthings_exe
        # advice on stuck situations
        scvs = len(self.units(SCV))
        ccs = self.we_started_amount(COMMANDCENTER) + self.structures(PLANETARYFORTRESS).amount \
              + self.structures(ORBITALCOMMAND).amount
        bcs = self.we_started_amount(BATTLECRUISER)
        mts = self.we_started_amount(MISSILETURRET)
        core = self.we_have_a(FUSIONCORE)
        wms = self.we_started_amount(WIDOWMINE)
        # supplydepots elsewhere
        # refineries elsewhere
        # amount == 0
        if (not self.we_started_a(COMMANDCENTER)) and (len(self.structures(ORBITALCOMMAND)) == 0):
            self.blunt_to_bagofthings(COMMANDCENTER)
        if (not self.we_started_a(SUPPLYDEPOT)):
            self.blunt_to_bagofthings(SUPPLYDEPOT)
        if (not self.we_started_a(BARRACKS)):
            self.blunt_to_bagofthings(BARRACKS)
        if (not self.we_started_a(REFINERY)):
            self.blunt_to_bagofthings(REFINERY)
        if (not self.we_started_a(FACTORY)) and (ccs >= 2):
            self.blunt_to_bagofthings(FACTORY)
        if (not self.we_started_a(STARPORT)) and (ccs >= 2):
            self.blunt_to_bagofthings(STARPORT)
        if (not self.we_started_a(FUSIONCORE)) and (ccs >= 2):
            self.blunt_to_bagofthings(FUSIONCORE)
        if (not self.we_started_a(ENGINEERINGBAY)) and (ccs >= 2):
            self.blunt_to_bagofthings(ENGINEERINGBAY)
        if (not self.we_started_a(MISSILETURRET)) and (ccs >= 2) and (mts < 8 * ccs):
            self.blunt_to_bagofthings(MISSILETURRET)
        if (not self.we_started_a(ARMORY)) and (ccs >= 3):
            self.blunt_to_bagofthings(ARMORY)
        if (not self.we_started_a(RAVEN)) and (bcs >= 4):
            self.blunt_to_bagofthings(RAVEN)
        # fill out
        for sp in self.structures(FACTORY).ready:
            if not sp.has_add_on:
                self.blunt_to_bagofthings(FACTORYTECHLAB)
        for sp in self.structures(STARPORT).ready:
            if not sp.has_add_on:
                self.blunt_to_bagofthings(STARPORTTECHLAB)
        # army
        good_drones_supply = min(self.supply_used / 2 + 10, 80)
        good_army_supply = self.supply_used - good_drones_supply
        if (self.army_supply < good_army_supply):
            if core:
                if (len(self.structures(STARPORT).ready.idle) > 0):
                    self.blunt_to_bagofthings(BATTLECRUISER)
                else:
                    self.blunt_to_bagofthings(STARPORT)
            elif (len(self.structures(FACTORY).ready.idle) > 0):
                self.blunt_to_bagofthings(SIEGETANK)
            else:
                self.blunt_to_bagofthings(MARINE)
            if (wms < 5) and (ccs > 1) and (len(self.structures(FACTORY).ready.idle) > 0):
                self.blunt_to_bagofthings(WIDOWMINE)
        else:
            self.blunt_to_bagofthings(COMMANDCENTER)
        # upgrades
        if (bcs >= 4) and (self.we_started_amount(ARMORY) < 2):
            self.blunt_to_bagofthings(ARMORY)
        if (bcs >= 3):
            self.blunt_to_bagofthings(BATTLECRUISERENABLESPECIALIZATIONS)
        if (len(self.structures(ARMORY).ready.idle) > 0):
            for pair in self.cradle:
                if pair[1] == ARMORY:
                    self.blunt_to_bagofthings(pair[0])
        if (len(self.structures(ENGINEERINGBAY).ready.idle) > 0):
            for pair in self.cradle:
                if pair[1] == ENGINEERINGBAY:
                    self.blunt_to_bagofthings(pair[0])
        # defence
        if (self.we_started_amount(PLANETARYFORTRESS) * 2 < ccs):
            self.blunt_to_bagofthings(PLANETARYFORTRESS)
        vikings = 0
        for ene in self.enemy_units:
            if (ene.type_id in self.viking_targets) and (ene.type_id != OVERLORD):
                vikings = vikings + 1
        if self.units(VIKINGFIGHTER).amount < vikings:
            self.blunt_to_bagofthings(VIKINGFIGHTER)
        # log
        stri = 'endgame added bagofthings: '
        for th in self.bagofthings:
            stri = stri + th.name + ' '
        self.log_success(stri)


    def midgame(self,thing,amount):
        self.routine = 'midgame'
        for t in range(0,amount):
            self.bagofthings.append(thing)


    def blunt_to_bagofthings(self,thing):
        self.routine = 'blunt_to_bagofthings'
        have = self.we_started_amount(thing)
        for th in self.bagofthings + self.bagofthings_exe:
            if th == thing:
                have = have + 1
        if have < self.maxam_of_thing(thing):
            if self.check_techtree(thing):
                self.bagofthings.append(thing)


    async def make_planning_exe(self):
        self.routine = 'make_planning_exe'
        # cut off a dream at the loss of a structure
        i_have_structures = len(self.structures) - len(self.structures(BUNKER))
        if i_have_structures < self.but_i_had_structures:
            self.log_success('$$$$$$$ lost a building; breaking off _exe')
            self.bagofthings_exe = []
            self.bagoftree_exe = []
            self.buildseries_exe = []
            for (th,po) in self.buildorder_exe:
                if po not in (self.cheese_barracks_pos,self.cheese_bunker_pos,self.cheese_factory_pos,self.cheese_starport_pos):
                    self.recycling.append((th,po))
            self.buildorder_exe = []
            self.buildplan_exe = []
            self.clean_layout()
            # cancel current orders too
            self.ambition_of_strt = {}
            self.ambiwalk_exe = set()
            self.ambiwalk_thrown = set()
            for scv in self.units(SCV):
                scvt = scv.tag
                if self.job_of_scvt[scvt] not in ('mimminer','gasminer','builder'):
                    self.job_of_scvt[scvt] = 'idler'
                    if scvt in self.goal_of_trabu_scvt:
                        del self.goal_of_trabu_scvt[scvt]
                        del self.structure_of_trabu_scvt[scvt]
                    if not scv.is_idle:
                        self.log_command('scv(AbilityId.STOP)')
                        scv(AbilityId.STOP)
            vision_of_scvt = {}
        self.but_i_had_structures = i_have_structures
        # first make buildseries
        if ((len(self.buildorder_exe) == 0)) \
        or ((len(self.buildorder_exe) < 5) and (self.game_phase == 'endgame')):
            # phase
            if self.game_phase == 'init':
                self.game_phase = 'opening'
                self.log_success('============================================================ opening =========')
                self.log_buildseries('game_phase')
            elif self.game_phase == 'opening':
                self.game_phase = 'midgame'
                self.log_buildseries('game_phase')
                self.log_success('============================================================ midgame ======')
            elif self.game_phase == 'midgame':
                self.game_phase = 'endgame'
                self.log_buildseries('game_phase')
                self.log_success('============================================================ endgame =======')
            # make optimized buildseries
            if (self.game_phase == 'opening'):
                self.buildseries = self.buildseries_opening
                # make the simpler bags
                self.bagofthings = []
                for infa_th in self.buildseries:
                    th = self.uninfest(infa_th)
                    self.bagofthings.append(th)
                self.bagofthings_exe = self.bagofthings.copy()
                self.bagoftree_of_bagofthings()
                self.bagoftree_exe = self.bagoftree.copy()
            elif (self.game_phase == 'midgame'):
                self.bagofthings = self.midgame_bagofthings.copy()
                # bagofthings is made. Build up from here.
                self.bagofthings_exe.extend(self.bagofthings)
                self.bagofthings = self.bagofthings_exe.copy()
                self.bagoftree_of_bagofthings()
                self.bagoftree_exe = self.bagoftree.copy()
                self.buildseries_of_bagoftree()
                self.optimize_buildseries()
            elif (self.game_phase == 'endgame'):
                self.endgame()
                # bagofthings is made. Build up from here.
                for th in self.bagofthings:
                    if th not in self.bagofthings_exe:
                        self.bagofthings_exe.append(th)
                self.bagofthings = self.bagofthings_exe.copy()
                self.bagoftree_of_bagofthings()
                self.bagoftree_exe = self.bagoftree.copy()
                self.buildseries_of_bagoftree()
                self.optimize_buildseries()
            # optimized buildseries is made
            self.buildseries_exe = self.buildseries.copy()
            # Keep old places for reuse.
            self.recycling.extend(self.buildorder_exe)
            self.buildorder_of_buildseries()
            self.buildorder_exe = self.buildorder.copy()
        # buildorder_exe is made
        self.buildorder = self.buildorder_exe.copy()
        self.get_situation()
        self.planning_of_buildorder(0,0)
        self.optimize_planning()
        self.planning_exe = self.planning.copy()

    # *********************************************************************************************************************

    async def realized_planning_exe(self):
        self.routine = 'realized_planning_exe'
        # administrate ended buildorder_exe (succeeded or failed)
        # administrate ended ambiwalk_thrown
        done_stp = set()
        for stp in self.ambiwalk_thrown:
            (scvt, thing, place) = stp
            seen = False
            if thing in self.all_structures_tobuildwalk:
                if (scvt in self.structure_of_trabu_scvt) and (scvt in self.job_of_scvt):
                    if self.job_of_scvt[scvt] == 'traveller':
                        if (self.structure_of_trabu_scvt[scvt] == thing) and (self.goal_of_trabu_scvt[scvt] == place):
                            seen = True
            elif thing in self.all_structures: # lab, pf
                for stru in self.structures.ready:
                    if stru.position == place:
                        if stru.tag in self.ambition_of_strt:
                            seen = True
            if not seen:
                done_stp.add(stp)
        self.ambiwalk_thrown = self.ambiwalk_thrown - done_stp
        # administrate ended buildorder_exe (succeeded or failed)
        done_stp = set()
        for stp in self.ambiwalk_exe:
            (scvt, thing, place) = stp
            seen = False
            if thing in self.all_structures_tobuildwalk:
                if (scvt in self.structure_of_trabu_scvt) and (scvt in self.job_of_scvt):
                    if self.job_of_scvt[scvt] == 'traveller':
                        if (self.structure_of_trabu_scvt[scvt] == thing) and (self.goal_of_trabu_scvt[scvt] == place):
                            seen = True
            elif thing in self.all_structures: # lab, pf
                for stru in self.structures.ready:
                    if stru.position == place:
                        if stru.tag in self.ambition_of_strt:
                            seen = True
            if not seen:
                done_stp.add(stp)
        self.ambiwalk_exe = self.ambiwalk_exe - done_stp
        # clean each _exe
        for stp in done_stp:
            (scvt, thing, place) = stp
            first = True
            for  bp in self.planning_exe:
                (sv, th, pl, sr, sc, fi) = bp
                if first and (sv == scvt) and (th == thing) and (pl == place):
                    del self.planning_exe[self.planning_exe.index(bp)]
                    first = False
            tp = (thing,place)
            if tp in self.buildorder_exe:
                del self.buildorder_exe[self.buildorder_exe.index(tp)]
            else:
                self.log_success('BUG ALARM ' + thing.name + ' ' + str(place.x) + ',' + str(place.y) + '  NOT IN:')
                for (th, pl) in self.buildorder_exe:
                    self.log_success('BUG ALARM ' + th.name + ' ' + str(pl.x) + ',' + str(pl.y))
            # recalc to INFESTED
            infa_thing = thing
            if tp == (BUNKER,self.cheese_bunker_pos):
                infa_thing = INFESTEDBUNKER
            elif tp == (FACTORY,self.cheese_factory_pos):
                infa_thing = INFESTEDFACTORY
            elif tp == (BARRACKS,self.cheese_barracks_pos):
                infa_thing = INFESTEDBARRACKS
            elif tp == (STARPORT,self.cheese_starport_pos):
                infa_thing = INFESTEDSTARPORT
            if infa_thing in self.buildseries_exe:
                del self.buildseries_exe[self.buildseries_exe.index(infa_thing)]
            # no infested in the bags
            if thing in self.bagoftree_exe:
                del self.bagoftree_exe[self.bagoftree_exe.index(thing)]
            if thing in self.bagofthings_exe:
                del self.bagofthings_exe[self.bagofthings_exe.index(thing)]
        # log
        self.log_ambiwalk()



    async def follow_planning_exe(self):
        self.routine = 'follow_planning_exe'
        todel = set()
        for bp in self.planning_exe:
            (scvt, thing, place, sr, sc, fi) = bp
            stp = (scvt, thing, place)
            if stp not in self.ambiwalk_exe:
                if thing in self.all_structures_tobuildwalk:
                    if sr <= 0:
                        # a possibly needed extra check to prevent double building
                        if scvt not in self.goal_of_trabu_scvt:
                            if await self.build_thing_tobuildwalk(scvt,thing, place):
                                self.ambiwalk_exe.add(stp)
                elif thing in self.all_structures: # lab, pf
                    if sr <= 0:
                        if await self.build_thing(thing, place):
                            self.ambiwalk_exe.add(stp)
                else: # mar, upg
                    if sc <= 0:
                        if await self.build_thing(thing, place):
                            todel.add(bp)
        for bp in todel: # mar, upg
            (scvt, thing, place, sr, sc, fi) = bp
            del self.planning_exe[self.planning_exe.index(bp)]
            tp = (thing, place)
            if tp in self.buildorder_exe:
                del self.buildorder_exe[self.buildorder_exe.index(tp)]
            else:
                self.log_success('BUG ALARM2 ' + thing.name + ' ' + str(place.x) + ',' + str(place.y) + '  NOT IN:')
                for (th, pl) in self.buildorder_exe:
                    self.log_success('BUG ALARM2 ' + th.name + ' ' + str(pl.x) + ',' + str(pl.y))
            if thing in self.buildseries_exe:
                del self.buildseries_exe[self.buildseries_exe.index(thing)]
            if thing in self.bagoftree_exe:
                del self.bagoftree_exe[self.bagoftree_exe.index(thing)]
            if thing in self.bagofthings_exe:
                del self.bagofthings_exe[self.bagofthings_exe.index(thing)]


    async def throw(self,thing):
        self.routine = 'throw'
        # trow if money >= eps + bccost + throwncost
        used_mim = 450
        used_gas = 350
        for (scvt,th,pl) in self.ambiwalk_thrown:
            cost = self.get_cost(th)
            used_mim = used_mim + cost.minerals
            used_gas = used_gas + cost.vespene
        if (self.minerals >= used_mim) and (self.vespene >= used_gas):
            await self.throw_nopaycheck(thing)


    async def throw_nopaycheck(self,thing):
        self.routine = 'throw_nopaycheck'
        # build the thing if possible
        # ambiwalk_thrown: (scvt,th,pl) between throw request and actual payment start
        # throw max 5 parallel
        parallel = 0
        for scvt in self.structure_of_trabu_scvt:
            if self.structure_of_trabu_scvt[scvt] == thing:
                parallel = parallel + 1
        if parallel < 5:
            if thing == REFINERY:
                if self.find_tobuildwalk_a_place(thing):
                    place = self.function_result_Point2
                    scvt = self.get_near_scvt_to_goodjob(place)
                    if await self.build_thing_tobuildwalk(scvt, thing, place):
                        self.write_layout(thing, place)
                        self.log_success('thrown ' + thing.name)
                        self.ambiwalk_thrown.add((scvt,thing, place))
            elif thing in self.all_structures_tobuildwalk:
                if self.find_tobuildwalk_a_place(thing):
                    place = self.function_result_Point2
                    scvt = self.get_near_scvt_to_goodjob(place)
                    if await self.build_thing_tobuildwalk(scvt, thing, place):
                        self.write_layout(thing, place)
                        self.log_success('thrown '+thing.name)
                        self.ambiwalk_thrown.add((scvt,thing,place))
            elif thing in (ORBITALCOMMAND,PLANETARYFORTRESS):
                ccs = self.structures(COMMANDCENTER).ready
                if len(ccs) > 0:
                    cc = random.choice(ccs)
                    place = cc.position
                    if await self.build_thing(thing, place):
                        self.log_success('thrown ' + thing.name)
                        self.ambiwalk_thrown.add((self.notag, thing, place))
            elif thing in self.all_upgrades:
                cc = random.choice(self.structures(ARMORY).ready)
                place = cc.position
                if await self.build_thing(thing, place):
                    self.log_success('thrown ' + thing.name)
            elif thing in self.all_labs:
                for strtype in (BARRACKS,FACTORY,STARPORT):
                    sps = self.structures(strtype).ready
                    if len(sps) > 0:
                        sp = random.choice(sps)
                        place = sp.position
                        if await self.build_thing(thing, place):
                            self.log_success('thrown ' + thing.name)
                            self.ambiwalk_thrown.add((self.notag,thing, place))
            else: # mar
                place = self.nowhere
                if await self.build_thing(thing, place):
                    self.log_success('thrown '+thing.name)


    async def supplydepots_adlib(self):
        self.routine = 'supplydepots_adlib'
        if (self.supply_left < 2 + self.supply_used // 6) and (self.supply_cap < 200):
            if (SUPPLYDEPOT not in self.structure_of_trabu_scvt.values()):
                if len(self.structures) > 7:
                    await self.throw_nopaycheck(SUPPLYDEPOT)

    async def refineries_adlib(self):
        self.routine = 'refineries_adlib'
        if (REFINERY not in self.structure_of_trabu_scvt.values()):
            if self.game_phase in ('midgame','endgame'):
                await self.throw(REFINERY)



    async def big_spender(self):
        # get rid of surplus money
        self.routine = 'big_spender'
        # core, pfs, ccs
        ccs = self.we_started_amount(COMMANDCENTER) + self.structures(PLANETARYFORTRESS).amount \
              + self.structures(ORBITALCOMMAND).amount
        pfs = self.we_started_amount(PLANETARYFORTRESS)
        core = self.we_have_a(FUSIONCORE)
        mts = self.structures(MISSILETURRET).ready.amount
        good_drones_supply = min(self.supply_used / 2 + 10, 80)
        good_army_supply = self.supply_used - good_drones_supply
        if self.minerals > 500:
            if self.vespene > 400:
                if self.supply_used < 194:
                    # army
                    if (self.army_supply < good_army_supply) or (self.minerals > 1000): # army
                        if core:
                            sps = self.structures(STARPORT).ready.idle
                            if len(sps) > 0:
                                await self.throw(STARPORTTECHLAB)
                                await self.throw(BATTLECRUISER)
                            else: # no free starport
                                await self.throw(STARPORT)
                        else:
                            await self.throw(SIEGETANK)
                            await self.throw(MARINE)
                    if (self.army_supply >= good_army_supply) or (self.minerals > 1000): # expand, defend
                        await self.throw(COMMANDCENTER)
                        if mts < ccs * 8:
                            await self.throw(MISSILETURRET)
                        if pfs < ccs / 2:
                            await self.throw(PLANETARYFORTRESS)
                else: # maxsupply
                    if mts < ccs * 8:
                        await self.throw(MISSILETURRET)
                    await self.throw(PLANETARYFORTRESS)
                    await self.throw(COMMANDCENTER)
                if self.supply_used > 100:
                    if (len(self.structures(ARMORY).ready.idle) > 0):
                        for pair in self.cradle:
                            if pair[1] == ARMORY:
                                await self.throw(pair[0])
            else: # no gas
                if self.supply_used < 194:
                    if (self.army_supply < good_army_supply):
                        await self.throw(MARINE)
                        if self.minerals > 1500:
                            await self.throw(BARRACKS)
                    else: # expand, defend
                        if mts < ccs * 8:
                            await self.throw(MISSILETURRET)
                        await self.throw(COMMANDCENTER)
                else: # maxsupply
                    if mts < ccs * 8:
                        await self.throw(MISSILETURRET)
                    await self.throw(COMMANDCENTER)

    def reset_workers(self):
        self.routine = 'reset_workers'
        if self.count_of_job['traveller'] > 10:
            self.log_success('Something went terribly wrong. Resetting workers.')
            for scvt in self.all_scvt:
                self.job_of_scvt[scvt] = 'idler'
            self.goal_of_trabu_scvt = {}
            self.structure_of_trabu_scvt = {}
            self.ambiwalk_exe = set()
            self.ambiwalk_thrown = set()
            self.ambition_of_strt = {}
            self.mimt_of_scvt = {}
            self.gast_of_scvt = {}

#*********************************************************************************************************************

    def may_do_now(self, scvt,building,goal) -> bool:
        md = ((scvt, building, goal) in self.ambiwalk_thrown)
        if len(self.buildorder_exe) > 0:
            md = md or ((building, goal) == self.buildorder_exe[0])
        return md

    async def build_thing_tobuildwalk(self,scvt,thing,place) -> bool:
#       self.log_success('DEBUG trying to build '+thing.name)
        self.routine = 'build_thing_tobuildwalk'
        if thing == COMMANDCENTER:
            didit = await self.build_commandcenter(scvt,place)
        elif thing in self.all_structures_tobuildwalk:
            didit = await self.build_building(scvt,thing,place) 
        return didit

    async def build_thing(self,thing,place) -> bool:
#       self.log_success('DEBUG trying to build '+thing.name)
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
            if self.can_pay(ship):
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
                                    if (sp.has_add_on) or (ship in (MARINE,HELLION,WIDOWMINE)):
                                        if sp.tag not in self.ambition_of_strt:
                                            if todo>0:
                                                todo = todo-1
                                                self.log_success(ship.name)
                                                self.log_command(hangar.name + '.train(' + ship.name + ')')
                                                sp.train(ship)
                                                self.idle_structure_tags.remove(sp.tag)
                                                didit = True
                                                self.clean_layout()
        return didit



    async def start_construction(self):
        self.routine = 'start_construction'
        for scvt in self.goal_of_trabu_scvt:
            if self.job_of_scvt[scvt] == 'traveller':
                goal = self.goal_of_trabu_scvt[scvt]
                building = self.structure_of_trabu_scvt[scvt] 
                if self.check_techtree(building):
                    if self.can_pay(building):
                        for scv in self.units(SCV):
                            if scv.tag == scvt:
                                if self.near(scv.position,goal,3):
                                    if self.may_do_now(scvt,building,goal):
                                        self.job_of_scvt[scvt] = 'builder'
                                        self.promotionsite_of_scvt[scvt] = scv.position
                                        self.log_workers('traveller became builder '+self.name(scvt))
                                        self.log_workers('beginning '+building.name+' '+self.name(scvt))
                                        if building == REFINERY:
                                            for gey in self.vespene_geyser:
                                               if gey.position == goal:
                                                   self.log_command('scv.build_gas(gey)')
                                                   if scv.build_gas(gey):
                                                       self.log_workers('begun     '+building.name+' '+self.name(scvt))
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
                        if self.can_pay(newbuilding):
                            pos = oldbuilding.position
                            if self.may_do_now(self.notag,newbuilding,pos):
                                if todo > 0:
                                    todo = todo-1
                                    del self.ambition_of_strt[oldbuilding.tag]
                                    self.log_success(newbuilding.name)
                                    self.log_command(oldbuilding.name+'.train('+newbuilding.name+')')
                                    oldbuilding.train(newbuilding)
                                    self.idle_structure_tags.remove(oldbuilding.tag)



    async def build_building(self,scvt,building,goal) -> bool:
        self.routine = 'build_building'
#       for tobuildwalk buildings except COMMANDCENTER
        didit = False
#       you do not have to wait for minerals and techtree
        if (self.check_future_techtree(building)) or (self.game_phase == 'opening'):
            for scv in self.units(SCV):
                if scv.tag == scvt:
                    job = self.job_of_scvt[scvt]
                    if job == 'mimminer':
                        self.was_mimminer(scv)
                    if job == 'gasminer':
                        self.was_gasminer(scv)
                    self.job_of_scvt[scvt] = 'traveller'
                    self.goal_of_trabu_scvt[scvt] = goal
                    self.structure_of_trabu_scvt[scvt] = building
                    self.promotionsite_of_scvt[scvt] = scv.position
                    self.log_workers('planning  '+building.name+' '+self.name(scvt))
                    self.log_command('scv(AbilityId.MOVE_MOVE,goal)')
                    if scv(AbilityId.MOVE_MOVE,goal):
                        self.log_workers('ordered   '+building.name+' '+self.name(scvt))
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
                if job == 'mimminer':
                    self.was_mimminer(scv)
                if job == 'gasminer':
                    self.was_gasminer(scv)
                self.job_of_scvt[scvt] = 'escorter'
                self.promotionsite_of_scvt[scvt] = scv.position
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
                if job == 'mimminer':
                    self.was_mimminer(scv)
                if job == 'gasminer':
                    self.was_gasminer(scv)
                self.job_of_scvt[scvt] = 'traveller'
                self.promotionsite_of_scvt[scvt] = scv.position
                self.log_workers(job+' became traveller '+self.name(scvt))
                self.log_command('scv(AbilityId.MOVE_MOVE,goal)')
                scv(AbilityId.MOVE_MOVE, goal)
        didit = True
        return didit



    async def enlarge_building(self,ambition,place) -> bool:
        # lab, pf
        # puts a building in ambition_of_strt, then it will become idle, then be transformed
        self.routine = 'enlarge_building'
        didit = False
        if self.check_techtree(ambition):
            if self.can_pay(ambition):
                for cc in self.structures.ready:
                    if cc.position == place:
                        if cc.tag not in self.ambition_of_strt:
                            if (ambition in self.all_labs) and (not cc.has_add_on):
                                self.ambition_of_strt[cc.tag] = ambition
                                didit = True
                            elif cc in self.structures(COMMANDCENTER).ready:
                                self.ambition_of_strt[cc.tag] = ambition
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
                                    if self.can_pay(upg) or self.bug_can_pay(upg):
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
                                                self.log_command('ar.research('+upg.name+')')
                                                ar.research(upg)
                                            self.idle_structure_tags.remove(ar.tag)
                            for ar in self.structures(cra).ready:
                                if (ar.tag in self.idle_structure_tags):
                                    if self.can_pay(upg) or self.bug_can_pay(upg):
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

    def see_enemies(self):
        for ene in self.enemy_units:
            if ene.type_id not in self.all_workertypes:
                self.seen_enemy_units.add(ene)
        for ene in self.enemy_structures:
            self.seen_enemy_structuretypes.add(ene.type_id)

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
            if self.near(point,self.enemy_target_building_loc,10):
                qual = 10
                for ene in self.enemy_structures:
                    if ene.type_id in (MISSILETURRET,PHOTONCANNON,SPORECRAWLER):
#                       bc.radius+spore.air_range+spore.radius   estimate 1.5+7+0.5
                        if self.near(point,ene.position,9):
                            qual = qual-1
        return qual

    def may_unfreeze(self,bc):
        self.routine = 'may_unfreeze'
        seen = False
        for ene in self.enemy_units:
            if self.near(bc.position, ene.position, 6):
                seen = True
        for ene in self.enemy_structures:
            if self.near(bc.position, ene.position, 6):
                seen = True
        if not seen:
            self.log_command('bc(AbilityId.STOP)')
            bc(AbilityId.STOP)
            self.frozenbctags.remove(bc.tag)
            tp = Point2(
                (random.randrange(self.map_left, self.map_right), random.randrange(self.map_bottom, self.map_top)))
            self.log_command('bc.move(tp)')
            bc.move(tp)


    async def attack(self):
        self.routine = 'attack'
        if self.attack_type == 'jumpy':
            for bc in self.units(BATTLECRUISER).ready.idle:
                if bc.tag in self.frozenbctags:
                    self.may_unfreeze(bc)
                if self.quality_of_army_position(bc.position) > 5:
                    if bc.tag not in self.frozenbctags:
                        altpos = self.locally_improved(bc.position)
                        if altpos == bc.position:
                            self.log_army('holding bc there')
                            self.log_command('bc(AbilityId.HOLDPOSITION_BATTLECRUISER)')
                            bc(AbilityId.HOLDPOSITION_BATTLECRUISER)
                            self.frozenbctags.add(bc.tag)
                        else:
                            self.log_command('bc.move(altpos)')
                            bc.move(altpos)
                else: # self.quality_of_army_position(bc.position) <= 5:
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
            tp = self.enemy_target_building_loc
        elif self.attack_type == 'center':
            tp = self.army_center_point
        elif self.attack_type == 'centerpoint':
            tp = self.enemy_target_building_loc
        sent = 0
        for srt in [BATTLECRUISER,MARINE,MARAUDER]:
            if (self.attack_type != 'jumpy') or (srt != BATTLECRUISER):
                for ar in self.units(srt).ready.idle:
                    if (self.cheese_phase in ('A','Z')) or (not self.near(ar.position,self.cheese_prison_pos,4)):
                        if ar.tag not in self.martag_to_bunker:
                            if ar.tag not in self.bct_in_repair:
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
                self.bestbc_dist_to_goal = 99999
                for bc in self.units(BATTLECRUISER).ready:
                    if bc.tag in self.frozenbctags:
                        self.log_command('bc(AbilityId.STOP)')
                        bc(AbilityId.STOP)
                        self.frozenbctags.remove(bc.tag)
        elif self.attack_type == 'chaos':
            if self.supply_used > 190:
                change_the_type = True
                for bc in self.units(BATTLECRUISER):
                    if bc.tag == self.bestbctag:
                        sd = self.sdist(bc.position, self.enemy_target_building_loc)
                        if (sd > 9) and (sd <= self.bestbc_dist_to_goal):
                            self.bestbc_dist_to_goal = sd
                            change_the_type = False
                if change_the_type:
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
                self.bestbc_dist_to_goal = 99999
                it_changed = True
        elif self.attack_type == 'arcpoint':
            change_the_type = True
            for bc in self.units(BATTLECRUISER):
                if bc.tag == self.bestbctag:
                    sd = self.sdist(bc.position,self.enemy_target_building_loc)
                    if (sd > 9) and (sd <= self.bestbc_dist_to_goal):
                        self.bestbc_dist_to_goal = sd
                        change_the_type = False
            if change_the_type:
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
                self.bestbc_dist_to_goal = 99999
                it_changed = True
        elif self.attack_type == 'centerpoint':
            change_the_type = True
            for bc in self.units(BATTLECRUISER):
                if bc.tag == self.bestbctag:
                    sd = self.sdist(bc.position,self.enemy_target_building_loc)
                    if (sd > 9) and (sd <= self.bestbc_dist_to_goal):
                        self.bestbc_dist_to_goal = sd
                        change_the_type = False
            if change_the_type:
                self.attack_type = 'jumpy'
                self.log_army('feeling jumpy')
                await self.log_attacktype('feeling jumpy')
                it_changed = True
#       
#       if the attack_type changed, get a new enemy_target_building_loc
        if it_changed:
            allloc = []
            for ene in self.enemy_structures.ready:
                if ene.type_id in (COMMANDCENTER,ORBITALCOMMAND,PLANETARYFORTRESS,HATCHERY,LAIR,HIVE,NEXUS):
                    allloc.append(ene.position)
            if len(allloc) == 0:
                for ene in self.enemy_structures:
                    allloc.append(ene.position)
            if len(allloc) == 0:
                self.enemy_target_building_loc = self.enemyloc
            else:
                self.enemy_target_building_loc = random.choice(allloc)
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
            target = self.notag
            for ene in self.enemy_units:
                if (ene.type_id in self.viking_targets):
                    if self.close_to_a_my_base(ene.position):
                        target = ene
            if target == self.notag:
                if len(self.all_bases) > 0:
                    bas = random.choice(self.all_bases)
                    basp = bas.position
                else:
                    basp = self.start_location
                pos = Point2((basp.x+random.randrange(-10,10),basp.y+random.randrange(-10,10)))
                self.log_command('vk.attack(pos)')
                vk.attack(pos)
            else:
                self.log_command('vk.attack('+target.name+')')
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
        self.routine = 'siege_tank'
#       siege tank at a random own base
        for tnk in self.units(SIEGETANK).ready.idle:
            if tnk != self.cheese_tank:
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
                        # at first base, protect wall, at other bases, protect the tank
                        if tow.position == self.start_location.position:
                            self.log_command('tnk.attack(tow.position.towards(self.game_info.map_center,3))')
                            tnk.attack(tow.position.towards(self.game_info.map_center, 3))
                        else:
                            self.log_command('tnk.attack(tow.position.towards(self.game_info.map_center,-3))')
                            tnk.attack(tow.position.towards(self.game_info.map_center,-3))

    async def use_mine(self):
        self.routine = 'use_mine'
        for wm in self.units(WIDOWMINE).ready:
            if wm != self.cheese_mine:
                wmt = wm.tag
                if wmt in self.goal_of_wmt:
                    sd = self.sdist(wm.position,self.goal_of_wmt[wmt])
                    if sd < self.sd_of_wmt[wmt]:
                        self.shame_of_wmt[wmt] = 0
                    else:
                        self.shame_of_wmt[wmt] = self.shame_of_wmt[wmt] + 1
                    self.sd_of_wmt[wmt] = sd
                    if (wm.health < wm.health_max) or (sd<4) or (self.shame_of_wmt[wmt] >= 9):
                        self.log_command('wm(AbilityId.BURROWDOWN_WIDOWMINE)')
                        wm(AbilityId.BURROWDOWN_WIDOWMINE)
                else: # put wm in goal_of_wmt
                    enemims = set()
                    for mim in self.mineral_field:
                        if self.near(mim.position, self.enemyloc, 60):
                            enemims.add(mim)
                    enemim = random.choice(tuple(enemims))
                    point = enemim.position.towards(self.game_info.map_center, -2)
                    self.goal_of_wmt[wmt] = point
                    self.log_command('wm.move(point)')
                    wm.move(point)
                    self.sd_of_wmt[wmt] = 99999
                    self.shame_of_wmt[wmt] = 0

    async def fire_yamato(self):
        self.routine = 'fire_yamato'
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
                abilities = (await self.get_available_abilities([bc]))[0]
                if AbilityId.EFFECT_TACTICALJUMP in abilities:
                    self.log_success('')
                    self.log_command('bc(AbilityId.EFFECT_TACTICALJUMP,self.shipyard)')
                    bc(AbilityId.EFFECT_TACTICALJUMP,self.shipyard)
                    self.bct_in_repair.append(bc.tag)
                    self.bc_fear = max(150,self.bc_fear-10)
                    # unfreeze
                    if bc.tag in self.frozenbctags:
                        self.frozenbctags.remove(bc.tag)



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


    async def worker_defence(self):
        self.routine = 'worker_defence'
        if self.game_phase != 'endgame':
            for tow in self.all_bases:
                # calc enemies and defenders
                enemies = []
                for ene in self.enemy_units + self.enemy_structures:
                    if self.belongs_to(tow.position,ene.position):
                        if not ene.is_flying:
                            enemies.append(ene)
                defenders = set()
                for myscv in self.units(SCV):
                    scvt = myscv.tag
                    if scvt in self.all_scvt:
                        job = self.job_of_scvt[scvt]
                        if (job == 'defender'):
                            if self.belongs_to(tow.position, myscv.position):
                                defenders.add(myscv)
                if len(defenders) > 0:
                    # dismiss veterans
                    veterans = set()
                    for myscv in defenders:
                        if myscv.health < 12:
                            veterans.add(myscv)
                            # promote to fleeer and run it
                            scvt = myscv.tag
                            job = self.job_of_scvt[scvt]
                            self.log_workers('promoted '+job+' to fleeer '+self.name(scvt))
                            self.job_of_scvt[scvt] = 'fleeer'
                            self.promotionsite_of_scvt[scvt] = myscv.position
                            place = Point2((random.randrange(self.map_left, self.map_right),
                                            random.randrange(self.map_bottom, self.map_top)))
                            self.log_command('myscv(AbilityId.MOVE_MOVE,place)')
                            myscv(AbilityId.MOVE_MOVE, place)
                    defenders = defenders - veterans
                if len(enemies) > 0:
                    # get defenders
                    toget = len(enemies) + 3 - len(defenders)
                    for myscv in self.units(SCV):
                        if toget > 0:
                            if self.belongs_to(tow.position,myscv.position):
                                if myscv.health >= 12:
                                    scvt = myscv.tag
                                    if scvt in self.all_scvt:
                                        job = self.job_of_scvt[scvt]
                                        if job in self.bad_jobs:
                                            # promote to defender and let idle
                                            toget = toget - 1
                                            job = self.job_of_scvt[scvt]
                                            if job == 'mimminer':
                                                self.was_mimminer(myscv)
                                            if job == 'gasminer':
                                                self.was_gasminer(myscv)
                                            self.log_workers('promoted ' + job + ' to defender ' + self.name(scvt))
                                            self.job_of_scvt[scvt] = 'defender'
                                            self.promotionsite_of_scvt[scvt] = myscv.position
                                            if not myscv.is_idle:
                                                self.log_command('myscv(AbilityId.STOP)')
                                                myscv(AbilityId.STOP)
                if len(defenders) > len(enemies) + 3:
                    # dismiss defenders
                    todel = len(defenders) - (len(enemies) + 3)
                    if len(enemies) == 0:
                        todel = len(defenders)
                    for myscv in defenders:
                        if (todel > 0):
                            todel = todel - 1
                            # promote to idler and move home
                            scvt = myscv.tag
                            self.log_workers('promoted defender to idler ' + self.name(scvt))
                            self.job_of_scvt[scvt] = 'idler'
                            self.promotionsite_of_scvt[scvt] = myscv.position
                            self.log_command('myscv.move(tow.position)')
                            myscv.move(tow.position)
                if len(enemies) > 0:
                    # calc center
                    cx = 0
                    cy = 0
                    n = 0
                    for ene in enemies:
                        cx = cx + ene.position.x
                        cy = cy + ene.position.y
                        n = n + 1
                    center = Point2((cx / n, cy / n))
                    # decide if it is grouped
                    grouped = False
                    for ene in enemies:
                        if self.near(center,ene.position,3):
                            grouped = True
                    if grouped:
                        # group attack
                        for myscv in defenders:
                            self.log_command('myscv.attack(center)')
                            myscv.attack(center)
                    else:
                        # individual attack
                        for myscv in defenders:
                            if myscv.is_idle:
                                target = random.choice(enemies)
                                self.log_command('myscv.attack(target)')
                                myscv.attack(target)


    async def cheese_army(self):
        self.routine = 'cheese_army'
        if self.cheese_marine_count < 4:
            if (self.cheese_phase >= 'B') and (self.cheese_phase < 'Z'):
                if self.cheese_barracks in self.structures(BARRACKS).ready.idle:
                    if self.minerals >= 50:
                        if self.supply_left >= 1:
                            self.log_command('self.cheese_barracks.train(MARINE)')
                            self.cheese_barracks.train(MARINE)
                            self.cheese_marine_count = self.cheese_marine_count + 1
        if self.cheese_tank_count == 0:
            if (self.cheese_phase >= 'J') and (self.cheese_phase < 'Z'):
                if self.cheese_factory in self.structures(FACTORY).ready.idle:
                    if self.can_pay(SIEGETANK):
                        if self.supply_left >= 3:
                            self.log_command('self.cheese_factory.train(SIEGETANK)')
                            self.cheese_factory.train(SIEGETANK)
                            self.cheese_tank_count = self.cheese_tank_count + 1


    def recruite(self):
        # recruit 2 marines and send them to cheese2_bunker
        for mari in self.units(MARINE):
            if len(self.martag_to_bunker) < 2:
                if mari.tag not in self.martag_to_bunker:
                    if self.cheese_bunker == None:
                        self.log_command('mari.move(self.cheese2_bunker_pos)')
                        mari.move(self.cheese2_bunker_pos)
                        self.martag_to_bunker.add(mari.tag)
                    elif len(self.cheese_bunker.passengers) == 4:
                        self.log_command('mari.move(self.cheese2_bunker_pos)')
                        mari.move(self.cheese2_bunker_pos)
                        self.martag_to_bunker.add(mari.tag)
                    elif not self.near(mari.position,self.cheese_bunker.position,7):
                        self.log_command('mari.move(self.cheese2_bunker_pos)')
                        mari.move(self.cheese2_bunker_pos)
                        self.martag_to_bunker.add(mari.tag)
        if len(self.martag_to_bunker) < 2:
            for bar in self.structures(BARRACKS).ready.idle:
                if self.can_pay(MARINE) and not self.we_started_a(MARINE):
                    self.log_command('bar.train(MARINE)')
                    bar.train(MARINE)



    async def bunkercheese2(self):
        self.routine = 'bunkercheese2'
        if self.cheese2_phase == 'A':
            if (self.cheese_phase >= 'B') and (self.cheese_phase < 'Z'):
                for ene in self.enemy_structures:
                    if ene.type_id in (COMMANDCENTER,NEXUS,HATCHERY):
                        if ene.position != self.enemyloc:
                            # get place for a bunker
                            besttry = 9999
                            self.cheese2_bunker_pos = self.nowhere
                            for dx in range(-10,10):
                                for dy in range(-10,10):
                                    maypos = Point2((ene.position.x+dx, ene.position.y+dy))
                                    self.put_on_the_grid(BUNKER, maypos)
                                    maypos = self.function_result_Point2
                                    if self.check_layout(BUNKER,maypos):
                                        sd = self.sdist(ene.position,maypos)
                                        # next constant is the ideal distance for the bunker
                                        try0 = abs(sd-79)
                                        if try0 < besttry:
                                            self.cheese2_bunker_pos = maypos
                                            besttry = try0
                                            self.cheese2_phase = 'B'
        elif self.cheese2_phase == 'B':
            # build a bunker near his second townhall
            place = self.cheese2_bunker_pos
            thing = BUNKER
            scvt = self.get_near_scvt_to_goodjob(place)
            if await self.build_thing_tobuildwalk(scvt, thing, place):
                self.write_layout(thing, place)
                self.log_success('thrown ' + thing.name)
                self.ambiwalk_thrown.add((scvt, thing, place))
                self.cheese2_phase = 'C'
        elif self.cheese2_phase == 'C':
            for bu in self.structures(BUNKER):
                if bu.position == self.cheese2_bunker_pos:
                    self.cheese2_bunker = bu
                    self.cheese2_phase = 'D'
        elif self.cheese2_phase == 'D':
            # recruit
            self.recruite()
            # bunker still there?
            if self.cheese2_bunker not in self.structures(BUNKER):
                self.cheese2_phase = 'Z'
                self.martag_to_bunker = set()
            # wait for bunker ready
            for bu in self.structures(BUNKER).ready:
                if bu.position == self.cheese2_bunker_pos:
                    self.cheese2_phase = 'E'
        elif self.cheese2_phase == 'E':
            # recruit
            self.recruite()
            # bunker still there?
            if self.cheese2_bunker not in self.structures(BUNKER):
                self.cheese2_phase = 'Z'
                self.martag_to_bunker = set()
            # repair that bunker
            if self.cheese_scv != None:
                scv = self.cheese_scv
                scv.move(self.cheese2_bunker_pos)
                self.job_of_scvt[scv.tag] = 'arearepairer'
                self.cheese_scv = None
            # bunker ready, load
            for mari in self.units(MARINE):
                if mari.tag in self.martag_to_bunker:
                    if self.near(mari.position,self.cheese2_bunker_pos,7):
                        self.log_command('self.cheese2_bunker(AbilityId.LOAD_BUNKER,mari)')
                        self.cheese2_bunker(AbilityId.LOAD_BUNKER,mari)
            if len(self.cheese2_bunker.passengers) >= 2:
                self.cheese2_phase = 'Z'




    async def bunkercheese(self):
        self.routine = 'bunkercheese'
        # break off the cheese?
        if (self.cheese_phase >= 'B') and (self.cheese_phase < 'Z'):
            startedbuildings = 0
            for barra in self.structures(BARRACKS).ready:
                if barra.position != self.cheese_barracks_pos:
                    if self.near(barra.position,self.cheese_landing_pos,7):
                        startedbuildings = startedbuildings+1
            for bunk in self.structures(BUNKER):
                if self.near(bunk.position,self.cheese_bunker_pos,7):
                    self.cheese_bunker = bunk
                    startedbuildings = startedbuildings + 1
            if startedbuildings == 0:
                self.cheese_phase = 'Z'
                self.cheese_scv = None
                self.cheese_tank = None
                self.cheese_mine = None
                self.log_success('ending the bunkercheese')
        # follow a large series of phases
        if self.cheese_phase == 'Anobunker':
            if await self.build_thing_tobuildwalk(self.cheese_scv.tag, BUNKER, self.cheese_bunker_pos):
                self.ambiwalk_thrown.add((self.cheese_scv.tag,BUNKER,self.cheese_bunker_pos))
                self.cheese_bunker_last_health = 0
                self.cheese_phase = 'A'
        elif self.cheese_phase == 'A':
            for barra in self.structures(BARRACKS):
                if barra.position == self.cheese_barracks_pos:
                    self.cheese_barracks = barra
            # wait for landed barracks and building bunker
            startedbuildings = 0
            for barra in self.structures(BARRACKS).ready:
                if barra.position != self.cheese_barracks_pos:
                    if self.near(barra.position,self.cheese_landing_pos,7):
                        startedbuildings = startedbuildings+1
            for bunk in self.structures(BUNKER):
                if self.near(bunk.position,self.cheese_bunker_pos,7):
                    self.cheese_bunker = bunk
                    startedbuildings = startedbuildings + 1
            if startedbuildings == 2:
                for anscv in self.units(SCV):
                    scvt = anscv.tag
                    if scvt in self.job_of_scvt:
                        if self.near(anscv.position, self.cheese_bunker_pos, 5):
                            if self.job_of_scvt[scvt] == 'builder':
                                self.job_of_scvt[scvt] = 'cheeser'
                                self.cheese_scv = anscv
                                self.log_workers('the cheese_scv is ' + self.name(scvt))
                self.cheese_marine_count = 0
                self.cheese_tank_count = 0
                self.cheese_phase = 'B'
        elif self.cheese_phase == 'B':
            self.log_command('self.cheese_barracks(AbilityId.RALLY_BUILDING,self.cheese_prison_pos)')
            self.cheese_barracks(AbilityId.RALLY_BUILDING,self.cheese_prison_pos)
            self.cheese_phase = 'C'
        elif self.cheese_phase == 'C':
            # wait for bunker ready
            # check for a lost cause
            if self.cheese_bunker.health < 0.67 * self.cheese_bunker_last_health:
                # cancel the build
                self.cheese_bunker(AbilityId.CANCEL)
                self.cheese_phase = 'Anobunker'
                # execute bunkercheese before make_planning_exe
                self.but_i_had_structures = 0
                self.cheese_bunker_last_health = 0
            else:
                self.cheese_bunker_last_health = self.cheese_bunker.health
            # first, try back-to-track
            if (self.cheese_scv not in self.units(SCV)) and (self.scout_tag != self.notag):
                # promote scout to cheese_scv
                for scv in self.units(SCV):
                    if scv.tag == self.scout_tag:
                        if self.near(scv.position,self.cheese_prison_pos,20):
                            self.cheese_scv = scv
                            self.scout_tag = self.notag
                            self.log_workers('the cheese_scv is ' + self.name(scv.tag))
                            self.job_of_scvt[scv.tag] = 'cheeser'
                            if self.cheese_bunker in self.structures(BUNKER):
                                self.log_command('self.cheese_scv(AbilityId.SMART,self.cheese_bunker)')
                                self.cheese_scv(AbilityId.SMART,self.cheese_bunker)
            if self.cheese_bunker not in self.structures(BUNKER):
                if self.cheese_scv in self.units(SCV):
                    self.cheese_phase = 'Anobunker'
            if self.cheese_bunker in self.structures(BUNKER).ready:
                # rally and load
                self.log_command('self.cheese_barracks(AbilityId.RALLY_BUILDING,self.cheese_bunker)')
                self.cheese_barracks(AbilityId.RALLY_BUILDING,self.cheese_bunker)
                self.log_command('self.cheese_bunker(AbilityId.RALLY_BUILDING,self.cheese_prison_pos)')
                self.cheese_bunker(AbilityId.RALLY_BUILDING,self.cheese_prison_pos)
                # warning: scv inside the bunker is not in self.units(SCV)
                self.log_command('self.cheese_bunker(AbilityId.LOAD_BUNKER,self.cheese_scv)')
                self.cheese_bunker(AbilityId.LOAD_BUNKER,self.cheese_scv)
                self.cheese_phase = 'D'
        elif self.cheese_phase == 'D':
            # temporarily load some marines to make place for the scv
            self.cheese_marines = set()
            for mari in self.units(MARINE):
                if self.near(mari.position, self.cheese_landing_pos, 7):
                    self.cheese_marines.add(mari)
            for mari in self.cheese_marines:
                if len(self.cheese_bunker.passengers) < 4:
                    self.log_command('self.cheese_bunker(AbilityId.LOAD_BUNKER,mari)')
                    self.cheese_bunker(AbilityId.LOAD_BUNKER,mari)
            self.cheese_phase = 'E'
        elif self.cheese_phase == 'E':
            # we want to unload the cheese_scv, but it is said only unloadall works
            self.log_command('self.cheese_bunker(AbilityId.UNLOADALL_BUNKER)')
            self.cheese_bunker(AbilityId.UNLOADALL_BUNKER)
            self.cheese_frames = 0
            self.cheese_phase = 'F'
        elif self.cheese_phase == 'F':
            # The scv sometimes does not come out. Maybe if a marine goes out and starts shooting?
            self.cheese_frames = self.cheese_frames + 1
            if self.cheese_frames == 3:
                self.cheese_phase = 'G'
        elif self.cheese_phase == 'G':
            if self.cheese_scv in self.units(SCV):
                self.cheese_marines = set()
                for mari in self.units(MARINE):
                    if self.near(mari.position, self.cheese_landing_pos, 7):
                        self.cheese_marines.add(mari)
                for mari in self.cheese_marines:
                    if len(self.cheese_bunker.passengers) < 4:
                        self.log_command('self.cheese_bunker(AbilityId.LOAD_BUNKER,mari)')
                        self.cheese_bunker(AbilityId.LOAD_BUNKER,mari)
                self.cheese_phase = 'H'
            else: # cheese_scv is still inside the bunker
                self.cheese_phase = 'E'
        elif self.cheese_phase == 'H':
            # repeat the load command as it is seen to be disobeyed
            self.cheese_marines = set()
            for mari in self.units(MARINE):
                if self.near(mari.position, self.cheese_landing_pos, 7):
                    self.cheese_marines.add(mari)
            for mari in self.cheese_marines:
                if len(self.cheese_bunker.passengers) < 4:
                    self.log_command('self.cheese_bunker(AbilityId.LOAD_BUNKER,mari)')
                    self.cheese_bunker(AbilityId.LOAD_BUNKER,mari)
            # the real meaning of this phase is to wait for the factory
            for facta in self.structures(FACTORY).ready:
                if facta.position == self.cheese_factory_pos:
                    self.cheese_factory = facta
                    point = self.cheese_tank_pos
                    self.log_command('self.cheese_factory(AbilityId.RALLY_BUILDING, point)')
                    self.cheese_factory(AbilityId.RALLY_BUILDING, point)
                    # make a lab
                    if self.can_pay(FACTORYTECHLAB):
                        self.log_command('self.cheese_factory.train(FACTORYTECHLAB)')
                        self.cheese_factory.train(FACTORYTECHLAB)
                        self.ambiwalk_thrown.add((self.notag,FACTORYTECHLAB, self.cheese_factory.position))
                        self.cheese_phase = 'I'
        elif self.cheese_phase == 'I':
            for tl in self.structures(FACTORYTECHLAB).ready:
                self.cheese_phase = 'J'
        elif self.cheese_phase == 'J':
            if self.cheese_tank_count == 1:
                for st in self.units(SIEGETANK).ready:
                    if self.near(st.position,self.cheese_factory_pos,7):
                        self.cheese_tank = st
                        self.log_command('self.cheese_tank.attack(self.cheese_tank_pos)')
                        self.cheese_tank.attack(self.cheese_tank_pos)
                        self.cheese_phase = 'K'
        elif self.cheese_phase == 'K':
            if self.can_pay(WIDOWMINE) and not self.we_started_a(WIDOWMINE):
                self.log_command('self.cheese_factory.train(WIDOWMINE)')
                self.cheese_factory.train(WIDOWMINE)
            if self.cheese_tank in self.units(SIEGETANK).ready.idle:
                point = self.cheese_factory_pos.towards(self.game_info.map_center, 3)
                self.log_command('self.cheese_factory(AbilityId.RALLY_BUILDING, point)')
                self.cheese_factory(AbilityId.RALLY_BUILDING, point)
                self.log_command('self.cheese_tank(AbilityId.SIEGEMODE_SIEGEMODE)')
                self.cheese_tank(AbilityId.SIEGEMODE_SIEGEMODE)
                self.cheese_phase = 'L'
        elif self.cheese_phase == 'L':
            if self.can_pay(WIDOWMINE) and not self.we_started_a(WIDOWMINE):
                self.log_command('self.cheese_factory.train(WIDOWMINE)')
                self.cheese_factory.train(WIDOWMINE)
            # lift the barracks and move a bit towards enemy
            ba = self.cheese_barracks
            oldpoint = ba.position
            oldsdist = self.sdist(oldpoint,self.enemyloc)
            self.erase_layout(ARMORY, oldpoint)
            altpoint = oldpoint
            altsdist = oldsdist
            tries = 0
            while ((not self.check_layout(ARMORY, altpoint)) or (altsdist >= oldsdist)) and (tries < 100) :
                tries = tries + 1
                altpoint = Point2((oldpoint.x + random.randrange(-4, 4), (oldpoint.y + random.randrange(-4, 4))))
                altsdist = self.sdist(altpoint,self.enemyloc)
            if tries < 100:
                if not self.cheese_barracks.is_idle:
                    self.log_command('self.cheese_barracks(AbilityId.CANCEL)')
                    self.cheese_barracks(AbilityId.CANCEL)
                self.home_of_flying_struct[ba.tag] = altpoint
                self.landings_of_flying_struct[ba.tag] = 0
                self.log_success('up cheesebarracks')
                self.log_command('ba(AbilityId.LIFT')
                ba(AbilityId.LIFT)
                self.write_layout(ARMORY, altpoint)
                self.cheese_phase = 'M'
            else:
                self.write_layout(ARMORY, oldpoint)
        elif self.cheese_phase == 'M':
            if self.can_pay(WIDOWMINE) and not self.we_started_a(WIDOWMINE):
                self.log_command('self.cheese_factory.train(WIDOWMINE)')
                self.cheese_factory.train(WIDOWMINE)
            for wm in self.units(WIDOWMINE).ready:
                if self.near(wm.position,self.cheese_factory_pos,7):
                    self.cheese_mine = wm
                    for mim in self.mineral_field:
                        if self.near(mim.position, self.enemyloc, self.miner_bound):
                            enemim = mim
                    point = enemim.position.towards(self.game_info.map_center,-4)
                    self.log_command('self.cheese_mine.move(point)')
                    self.cheese_mine.move(point)
                    self.cheese_phase = 'N'
        elif self.cheese_phase == 'N':
            if self.cheese_mine in self.units(WIDOWMINE).ready.idle:
                self.log_command('self.cheese_mine(AbilityId.BURROWDOWN_WIDOWMINE)')
                self.cheese_mine(AbilityId.BURROWDOWN_WIDOWMINE)
                self.cheese_phase = 'Z'
        # call the last phase Z
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
                            # neglect space for an add-on
                            self.landings_of_flying_struct[bu.tag] = 0
                            oldpoint = self.home_of_flying_struct[bu.tag]
                            altpoint = Point2((oldpoint.x+random.randrange(-4,4),(oldpoint.y+random.randrange(-4,4))))
                            tries = 0
                            while (not self.check_layout(ARMORY,altpoint)) and (tries<100):
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
                elif not self.near(self.shipyard,bu.position,7):
                    self.log_command('bu(AbilityId.MOVE_MOVE,self.shipyard)')
                    bu(AbilityId.MOVE_MOVE,self.shipyard)
        for srt in self.liftable:
            for bu in self.structures(srt).ready:
                if bu.health < 700:
                    if bu.position != self.wall_barracks_pos:
                        self.home_of_flying_struct[bu.tag] = bu.position
                        self.landings_of_flying_struct[bu.tag] = 0
                        self.log_success('up '+srt.name)
                        self.log_command('bu(AbilityId.LIFT')
                        bu(AbilityId.LIFT)
#       fly in the cheese
        for bu in self.structures(BARRACKS).ready:
            if bu.position == self.cheese_barracks_pos:
                self.home_of_flying_struct[bu.tag] = self.cheese_landing_pos
                self.landings_of_flying_struct[bu.tag] = 0
                self.log_success('up cheese-BARRACKS')
                self.log_command('bu(AbilityId.LIFT)')
                bu(AbilityId.LIFT)
                # it will try to land itself


    def wall_barracks_redirect(self):
        wallseen = False
        for bu in self.structures(BARRACKS) + self.structures(BARRACKSFLYING):
            if bu.position == self.wall_barracks_pos:
                wallseen = True
            if bu.tag in self.home_of_flying_struct:
                if self.home_of_flying_struct[bu.tag] == self.wall_barracks_pos:
                    wallseen = True
        if not wallseen:
            first = True
            for bu in self.structures(BARRACKS).ready.idle + self.structures(BARRACKSFLYING):
                if (self.cheese_phase == 'Z') or (bu != self.cheese_barracks):
                    if first:
                        first = False
                        self.log_success('redirecting a barracks to the wall')
                        self.home_of_flying_struct[bu.tag] = self.wall_barracks_pos
                        if bu not in self.structures(BARRACKSFLYING):
                            self.landings_of_flying_struct[bu.tag] = 0
                            self.log_success('up BARRACKS')
                            self.log_command('bu(AbilityId.LIFT')
                            bu(AbilityId.LIFT)


    async def do_wall_barracks(self):
        self.routine = 'do_wall_barracks'
        if not self.wall_barracks_managed:
            for bar in self.structures(BARRACKS).ready:
                if bar.position == self.wall_barracks_pos:
                    self.wall_barracks_managed = True
                    bar(AbilityId.RALLY_BUILDING, bar.position.towards(self.game_info.map_center, -2))


    async def do_updown(self):
        self.routine = 'do_updown'
        if len(self.updowns) < 2:
            for sd in self.structures(SUPPLYDEPOT).ready:
                self.updowns.add(sd.tag)
        for sd in self.structures(SUPPLYDEPOTLOWERED).ready:
            if sd.tag in self.updowns:
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
                        self.log_command('scv.move(whereto)')
                        scv.move(whereto)
        for sd in self.structures(SUPPLYDEPOT).ready:
            if sd.tag in self.updowns:
                danger = False
                for ene in self.enemy_units:
                    if self.near(ene.position,sd.position,5):
                        danger = True
                if not danger:
                    self.log_command('sd(AbilityId.MORPH_SUPPLYDEPOT_LOWER)')
                    sd(AbilityId.MORPH_SUPPLYDEPOT_LOWER)
                    self.log_success('lowering')


    async def may_cancel(self):
        self.routine = 'may_cancel'
        for stru in self.structures:
            if not self.near(self.cheese_prison_pos,stru.position,10):
                if stru.tag in self.last_health:
                    if stru.health < 0.67 * self.last_health[stru.tag]:
                        stru(AbilityId.CANCEL)
                    else:
                        self.last_health[stru.tag] = stru.health
                else:
                    self.last_health[stru.tag] = 0


    async def ruin(self):
        self.routine = 'ruin'
        for s in self.structures_without_construction_SCVs():
            if (self.cheese_phase == 'Z') or (not self.near(s.position,self.cheese_prison_pos,10)):
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
                        if self.can_pay(SCV):
                            if todo > 0:
                                todo = todo-1
                                self.log_workers('')
                                self.log_command('cc.train(SCV)')
                                dummy = cc.train(SCV)
                                self.idle_structure_tags.remove(cc.tag)


    async def be_gasminer(self,scv,gas):
        self.routine = 'be_gasminer'
        self.job_of_scvt[scv.tag] = 'gasminer'
        self.count_of_job['gasminer'] = self.count_of_job['gasminer'] + 1
        self.promotionsite_of_scvt[scv.tag] = scv.position
        self.log_command('scv.gather(gas)')
        dummy = scv.gather(gas)
        self.log_workers('be gasminer ' + self.name(scv.tag))
        self.gast_of_scvt[scv.tag] = gas.tag
        self.count_of_gast[gas.tag] = self.count_of_gast[gas.tag] + 1

    async def be_mimminer(self,scv,mim):
        self.routine = 'be_mimminer'
        self.job_of_scvt[scv.tag] = 'mimminer'
        self.promotionsite_of_scvt[scv.tag] = scv.position
        self.log_command('scv.gather(mim)')
        dummy = scv.gather(mim)
        self.log_workers('be mimminer ' + self.name(scv.tag))
        self.mimt_of_scvt[scv.tag] = mim.tag
        self.count_of_mimt[mim.tag] = self.count_of_mimt[mim.tag] + 1

    def was_gasminer(self,scv):
        self.routine = 'was_gasminer'
        if scv.tag in self.gast_of_scvt:
            gast = self.gast_of_scvt[scv.tag]
            self.count_of_gast[gast] = self.count_of_gast[gast] - 1
            del self.gast_of_scvt[scv.tag]
        self.log_workers('was gasminer ' + self.name(scv.tag))
        self.job_of_scvt[scv.tag] = ''
        self.count_of_job['gasminer'] = self.count_of_job['gasminer'] - 1
        if scv.is_collecting:
            self.log_command('scv(AbilityId.STOP)')
            scv(AbilityId.STOP)

    def was_mimminer(self, scv):
        self.routine = 'was_mimminer'
        if scv.tag in self.mimt_of_scvt:
            mimt = self.mimt_of_scvt[scv.tag]
            self.count_of_mimt[mimt] = self.count_of_mimt[mimt] - 1
            del self.mimt_of_scvt[scv.tag]
        self.log_workers('was mimminer ' + self.name(scv.tag))
        self.job_of_scvt[scv.tag] = ''
        self.count_of_job['mimminer'] = self.count_of_job['mimminer'] - 1
        if scv.is_collecting:
            self.log_command('scv(AbilityId.STOP)')
            scv(AbilityId.STOP)

    def get_arearepairer(self):
        self.routine = 'get_arearepairer'
        # If something needs repair, and has no repairer near, promote someone to arearepairer
        low_qual = 1.0
        wreck = self.notag
        for s in self.structures.ready:
            if (not self.near(s.position,self.enemyloc,50)) or (self.near(s.position,self.cheese_prison_pos,5)):
                qual = s.health / s.health_max
                if qual < low_qual:
                    hasrepairers = 0
                    couldhaverep = False
                    for scv in self.units(SCV):
                        if self.near(scv.position, s.position, 12):
                            scvt = scv.tag
                            if scvt in self.all_scvt:
                                job = self.job_of_scvt[scvt]
                                if job == 'arearepairer':
                                    hasrepairers = hasrepairers + 1
                                elif job in self.bad_jobs:
                                    couldhaverep = True
                    if (hasrepairers < 3) and (couldhaverep):
                        low_qual = qual
                        wreck = s
        if low_qual < 0.99:
            # we have a wreck needing repair
            scvt = self.get_near_scvt_to_goodjob(s.position)
            for scv in self.units(SCV):
                if scv.tag == scvt:
                    job = self.job_of_scvt[scvt]
                    if job == 'mimminer':
                        self.was_mimminer(scv)
                    if job == 'gasminer':
                        self.was_gasminer(scv)
                    self.log_workers('promoted '+job+' to arearepairer '+self.name(scvt))
                    self.job_of_scvt[scvt] = 'arearepairer'
                    self.promotionsite_of_scvt[scvt] = scv.position



    async def repair_it(self):
        self.routine = 'repair_it'
        for scv in self.units(SCV).ready:
            scvt = scv.tag
            if scvt in self.all_scvt:
                if self.job_of_scvt[scvt] in ('arearepairer','cheeser'):
                    if scvt in self.busy_arearepairer:
                        if scv.is_idle:
                            self.busy_arearepairer.remove(scvt)
                            self.log_workers('finish '+self.name(scvt))
                    else:
                        # check important structures
                        low_qual = 1.0
                        wreck = self.notag
                        for strtype in self.all_repairable_shooters:
                            for s in self.structures(strtype).ready + self.units(strtype):
                                if self.near(scv.position,s.position,12):
                                    qual = s.health/s.health_max
                                    if qual<low_qual:
                                        low_qual = qual
                                        wreck = s
                        if low_qual >= 0.99:
                            # check all structures
                            for s in self.structures.ready:
                                if self.near(scv.position,s.position,12):
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
                        if job == 'mimminer':
                            self.was_mimminer(scv)
                        if job == 'gasminer':
                            self.was_gasminer(scv)
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
#               May not idle:
                elif job in ('gasminer','mimminer','applicant','escorter','builder','arearepairer'):
                    if scv.position != self.promotionsite_of_scvt[scvt]:
                        if job == 'mimminer':
                            self.was_mimminer(scv)
                        if job == 'gasminer':
                            self.was_gasminer(scv)
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
                        if scv.position != self.promotionsite_of_scvt[scvt]:
                            gast = self.get_near_gast_free(scv.position)
                            for gas in self.all_refineries:
                                if gas.tag == gast:
                                    self.log_workers('jobswich mining builder '+self.name(scvt))
                                    await self.be_gasminer(scv,gas)
#
        self.fix_count_of_job()
        #
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
                    if job == 'mimminer':
                        self.was_mimminer(scv)
                    if job == 'gasminer':
                        self.was_gasminer(scv)
                    self.log_workers('promoted '+job+' to shiprepairer '+self.name(scvt))
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
        # 1 scout please
        if (self.scout_tag == self.notag) and (len(self.structures) >= 2):
            scvt = self.get_near_scvt_to_goodjob(self.shipyard)
            for scv in self.units(SCV):
                if scv.tag == scvt:
                    job = self.job_of_scvt[scvt]
                    if job == 'mimminer':
                        self.was_mimminer(scv)
                    if job == 'gasminer':
                        self.was_gasminer(scv)
                    self.log_workers('promoted '+job+' to scout '+self.name(scvt))
                    self.job_of_scvt[scvt] = 'scout'
                    self.promotionsite_of_scvt[scvt] = scv.position
                    # mark it and start running around
                    self.scout_tag = scvt
                    scoutgoal = self.scout_pos[0]
                    self.scout_bad_count = 0
                    self.scout_last_sdist = 9999
                    self.log_command('scv.move(scoutgoal)')
                    scv.move(scoutgoal)




    def search_applicants(self):
        self.routine = 'search_applicants'
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
                    # It appeared it must be stopped from mining elsewhere
                    for scv in self.units(SCV):
                        if scv.tag == scvt:
                            self.log_command('scv(AbillityId.STOP)')
                            scv(AbilityId.STOP)
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
                                        await self.be_gasminer(scv,gas)
            else:
                for scv in self.units(SCV):
                    scvt = scv.tag
                    if self.job_of_scvt[scvt] == 'idler':
                        gast = self.get_near_gast_free(scv.position)
                        for gas in self.all_refineries:
                            if gas.tag == gast:
                                if self.near(scv.position,gas.position,self.miner_bound):
                                    await self.be_gasminer(scv,gas)
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
                    # It appeared it must be stopped from mining elsewhere
                    for scv in self.units(SCV):
                        if scv.tag == scvt:
                            self.log_command('scv(AbillityId.STOP)')
                            scv(AbilityId.STOP)
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
                                        await self.be_mimminer(scv,mim)
            else:
                for scv in self.units(SCV):
                    scvt = scv.tag
                    if self.job_of_scvt[scvt] == 'idler':
                        mimt = self.get_near_mimt_free(scv.position)
                        for mim in self.mineral_field:
                            if mim.tag == mimt:
                                if self.near(scv.position,mim.position,self.miner_bound):
                                    await self.be_mimminer(scv,mim)
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
        self.routine = 'more_gas'
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
                                    self.was_mimminer(scv)
                                    await self.be_gasminer(scv,gas)

    async def more_minerals(self):
        self.routine = 'more_minerals'
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
                                    self.was_gasminer(scv)
                                    await self.be_mimminer(scv,mim)


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
        # scout
        for scv in self.units(SCV):
            if scv.tag == self.scout_tag:
                goal = self.scout_pos[self.scout_nr]
                sd = self.sdist(scv.position,goal)
                if (sd < 16) or (self.scout_bad_count > 9):
                    self.scout_nr = (self.scout_nr+1) % len(self.scout_pos)
                    goal = self.scout_pos[self.scout_nr]
                    scv.move(goal)
                    self.scout_last_sdist = 9999
                    self.scout_bad_count = 0
                elif sd < self.scout_last_sdist:
                    self.scout_last_sdist = sd
                    self.scout_bad_count = 0
                elif sd < 100:
                    self.scout_bad_count = self.scout_bad_count + 1


    async def mimminer_boss(self):
        self.routine = 'mimminer_boss'
        # mimminers can shift off their assigned patch.
        # the boss will see this, and correct the administration.
        for scv in self.units(SCV):
            scvt = scv.tag
            if scvt in self.all_scvt:
                if self.job_of_scvt[scvt] == 'mimminer':
                    assigned_mimt = self.mimt_of_scvt[scvt]
                    for mim in self.mineral_field:
                        if mim.tag == assigned_mimt:
                            if scvt in self.minedirection_of_scvt:
                                if scv.is_returning and (self.minedirection_of_scvt[scvt] == 'G'):
                                    # it is turning round towards the base
                                    if not self.near(mim.position,scv.position,2):
                                        self.log_boss('Hey a shifted mimminer '+self.name(scvt)+' should mine '+str(assigned_mimt))
                                        # find closest mineralpatch. In equal cases promote one with less miners.
                                        best_sdist = 80000
                                        best_mimt = self.notag
                                        for mim in self.mineral_field:
                                            mimt = mim.tag
                                            if mimt in self.all_mimt:
                                                sd = self.sdist(mim.position, scv.position)
                                                sd = sd + self.count_of_mimt[mimt]
                                                if sd < best_sdist:
                                                    best_sdist = sd
                                                    best_mimt = mimt
                                        mimt = best_mimt
                                        if best_sdist == 8000:
                                            self.log_boss('Hey no minerals found.')
                                        else:
                                            self.log_boss('He appears to mine '+str(mimt))
                                            self.mimt_of_scvt[scvt] = mimt
                                            self.count_of_mimt[mimt] = self.count_of_mimt[mimt] + 1
                                            self.count_of_mimt[assigned_mimt] = self.count_of_mimt[assigned_mimt] - 1
                                            if self.count_of_mimt[mimt] >2:
                                                self.log_boss('Now I have a patch with '+str(self.count_of_mimt[mimt]))
                                if scv.is_gathering and (self.minedirection_of_scvt[scvt] == 'R'):
                                    # miner just starts from base to patch
                                    mimt = scv.order_target
                                    if mimt != assigned_mimt:
                                        self.log_boss((self.name(scvt)+' he says '+str(mimt)+' but administrated is '+str(assigned_mimt)))
                                        if mimt in self.count_of_mimt:
                                            self.log_boss('I reassign him.')
                                            self.mimt_of_scvt[scvt] = mimt
                                            self.count_of_mimt[mimt] = self.count_of_mimt[mimt] + 1
                                            self.count_of_mimt[assigned_mimt] = self.count_of_mimt[assigned_mimt] - 1
                                            if self.count_of_mimt[mimt] > 2:
                                                self.log_boss('Now I have a patch with ' + str(self.count_of_mimt[mimt]))
                            # correct the minedirection administration for the next look.
                            if scv.is_returning:
                                self.minedirection_of_scvt[scvt] = 'R'
                            if scv.is_gathering:
                                self.minedirection_of_scvt[scvt] = 'G'


    async def gasminer_boss(self):
        self.routine = 'gasminer_boss'
        # gasminers can shift off their assigned patch.
        # the boss will see this, and correct the administration.
        for scv in self.units(SCV):
            scvt = scv.tag
            if scvt in self.all_scvt:
                if self.job_of_scvt[scvt] == 'gasminer':
                    assigned_gast = self.gast_of_scvt[scvt]
                    for gas in self.all_refineries:
                        if gas.tag == assigned_gast:
                            if scvt in self.minedirection_of_scvt:
                                if scv.is_returning and (self.minedirection_of_scvt[scvt] == 'G'):
                                    # it is turning round towards the base
                                    if not self.near(gas.position, scv.position, 4):
                                        self.log_boss('Hey a shifted gasminer ' + self.name(scvt) + ' should mine ' + str(
                                            assigned_gast))
                                        # find closest vespenepatch. In equal cases promote one with less miners.
                                        best_sdist = 80000
                                        best_gast = self.notag
                                        for gas in self.all_refineries:
                                            gast = gas.tag
                                            if gast in self.all_gast:
                                                sd = self.sdist(gas.position, scv.position)
                                                sd = sd + self.count_of_gast[gast]
                                                if sd < best_sdist:
                                                    best_sdist = sd
                                                    best_gast = gast
                                        gast = best_gast
                                        if best_sdist == 8000:
                                            self.log_boss('Hey no vespene found.')
                                        else:
                                            self.log_boss('He appears to mine ' + str(gast))
                                            self.gast_of_scvt[scvt] = gast
                                            self.count_of_gast[gast] = self.count_of_gast[gast] + 1
                                            self.count_of_gast[assigned_gast] = self.count_of_gast[assigned_gast] - 1
                                            if self.count_of_gast[gast] > 3:
                                                self.log_boss('Now I have a patch with ' + str(self.count_of_gast[gast]))
                                if scv.is_gathering and (self.minedirection_of_scvt[scvt] == 'R'):
                                    # miner just starts from base to patch
                                    gast = scv.order_target
                                    if gast != assigned_gast:
                                        self.log_boss((self.name(scvt) + ' he says ' + str(gast) + ' but administrated is ' + str(assigned_gast)))
                                        if gast in self.count_of_gast:
                                            self.log_boss('I reassign him.')
                                            self.gast_of_scvt[scvt] = gast
                                            self.count_of_gast[gast] = self.count_of_gast[gast] + 1
                                            self.count_of_gast[assigned_gast] = self.count_of_gast[assigned_gast] - 1
                                            if self.count_of_gast[gast] > 3:
                                                self.log_boss('Now I have a patch with ' + str(self.count_of_gast[gast]))
                            # correct the minedirection administration for the next look.
                            if scv.is_returning:
                                self.minedirection_of_scvt[scvt] = 'R'
                            if scv.is_gathering:
                                self.minedirection_of_scvt[scvt] = 'G'

#*********************************************************************************************************************

    def clean_layout(self):
        self.routine = 'clean_layout'
#       designs: add tag to realized plans
        newdesigns = []
        for (struc,place,tag) in self.designs:
            if tag == self.notag:
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
            for (exething,exeplace) in self.buildorder_exe:
                if place == exeplace:
                    seen = True
            for (exething,exeplace) in self.recycling:
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
        pl = open('data/strategy.txt','w')
        for nr in range(0,len(self.strategy)):
            pl.write(str(self.strategy[nr])+'\n')
        pl.close()


    async def init_strategy(self):
        self.routine = 'init_strategy'
        for i in range(0,self.game_choices):
            self.strategy.append(0.5)
#       read from disk
        pl = open('data/strategy.txt','r')
        read_strategy = pl.read().splitlines()
        pl.close()
        for nr in range(0,len(read_strategy)):
            self.strategy[nr] = float(read_strategy[nr].rstrip())
#       init game_choice
        for nr in range(0,len(self.strategy)):
            self.game_choice.append(random.random() < self.strategy[nr])
        self.game_result = 'doubt'

    async def win_loss(self):
        self.routine = 'win_loss'
        if self.game_result == 'doubt':
            max_cc_health = 0
            for cc in self.all_bases:
                if cc.health > max_cc_health:
                    max_cc_health = cc.health
            if self.supply_used>190:
                self.game_result = 'win'
                self.log_success('probably a win')
                for nr in range(0, len(self.strategy)):
                    if self.game_choice[nr]:
                        self.strategy[nr] = 0.9*self.strategy[nr]+0.1
                    else:
                        self.strategy[nr] = 0.9*self.strategy[nr]
                self.write_strategy()
            elif max_cc_health < 500:
                self.game_result = 'loss'
                self.log_success('probably a loss')
                for nr in range(0, len(self.strategy)):
                    if self.game_choice[nr]:
                        self.strategy[nr] = 0.9*self.strategy[nr]
                    else:
                        self.strategy[nr] = 0.9*self.strategy[nr]+0.1
                self.write_strategy()


#*********************************************************************************************************************
def main():
    # Easy/Medium/Hard/VeryHard
    all_maps = ['ThunderbirdLE','EternalEmpireLE','EverDreamLE','NightshadeLE','SimulacrumLE','ZenLE','GoldenWallLE']
    map = random.choice(all_maps)
    #map = 'ZenLE'
    species = random.choice([Race.Terran,Race.Zerg,Race.Protoss])
    #species = Race.Zerg
    run_game(maps.get(map), [
        Bot(Race.Terran, Chaosbot()),
        Computer(species, Difficulty.VeryHard)
        ], realtime = False)

if __name__ == "__main__":
    main()
    