# Merkbot.py containing Chaosbot
# author: MerkMore
# version: see chat
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
from sc2.game_data import Cost
import random
from math import sqrt,cos,sin,pi
from sc2.game_info import GameInfo
from layout_if_py import layout_if
from rocks_if_py import rocks_if
from bunker_if_py import bunker_if
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
from sc2.ids.unit_typeid import GHOST
from sc2.ids.unit_typeid import NUKESILONOVA # indicates a GHOSTACADEMY with NUKE warhead
from sc2.ids.unit_typeid import FACTORY
from sc2.ids.unit_typeid import BATTLECRUISER
from sc2.ids.unit_typeid import BARRACKSTECHLAB
from sc2.ids.unit_typeid import FACTORYTECHLAB
from sc2.ids.unit_typeid import STARPORTTECHLAB
from sc2.ids.unit_typeid import SENSORTOWER
from sc2.ids.unit_typeid import GHOSTACADEMY
from sc2.ids.unit_typeid import BARRACKSREACTOR
from sc2.ids.unit_typeid import FACTORYREACTOR
from sc2.ids.unit_typeid import STARPORTREACTOR
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
from sc2.ids.upgrade_id import PERSONALCLOAKING
from sc2.ids.unit_typeid import ENGINEERINGBAY
from sc2.ids.upgrade_id import TERRANINFANTRYWEAPONSLEVEL1
from sc2.ids.upgrade_id import TERRANINFANTRYWEAPONSLEVEL2
from sc2.ids.upgrade_id import TERRANINFANTRYWEAPONSLEVEL3
from sc2.ids.unit_typeid import PLANETARYFORTRESS
from sc2.ids.unit_typeid import ORBITALCOMMAND
from sc2.ids.unit_typeid import ORBITALCOMMANDFLYING
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
from sc2.ids.unit_typeid import THOR
from sc2.ids.unit_typeid import BANSHEE
from sc2.ids.unit_typeid import LIBERATOR
from sc2.ids.unit_typeid import LIBERATORAG
from sc2.ids.unit_typeid import CYCLONE
from sc2.ids.unit_typeid import WIDOWMINE
from sc2.ids.unit_typeid import WIDOWMINEBURROWED
from sc2.ids.unit_typeid import MULE
# with INFESTED is meant "close to the enemy".
from sc2.ids.unit_typeid import INFESTEDBARRACKS
from sc2.ids.unit_typeid import INFESTEDBUNKER
from sc2.ids.unit_typeid import INFESTEDFACTORY
from sc2.ids.unit_typeid import INFESTEDSTARPORT
from sc2.ids.unit_typeid import INFESTEDCOCOON
# protoss
from sc2.ids.unit_typeid import NEXUS
from sc2.ids.unit_typeid import PROBE
from sc2.ids.unit_typeid import STALKER
from sc2.ids.unit_typeid import PHOENIX
from sc2.ids.unit_typeid import ORACLE
from sc2.ids.unit_typeid import OBSERVER
from sc2.ids.unit_typeid import ARCHON
from sc2.ids.unit_typeid import CARRIER
from sc2.ids.unit_typeid import TEMPEST
from sc2.ids.unit_typeid import NEXUS
from sc2.ids.unit_typeid import PYLON
from sc2.ids.unit_typeid import ASSIMILATOR
from sc2.ids.unit_typeid import GATEWAY
from sc2.ids.unit_typeid import FORGE
from sc2.ids.unit_typeid import PHOTONCANNON
from sc2.ids.unit_typeid import SHIELDBATTERY
from sc2.ids.unit_typeid import WARPGATE
from sc2.ids.unit_typeid import CYBERNETICSCORE
from sc2.ids.unit_typeid import TWILIGHTCOUNCIL
from sc2.ids.unit_typeid import ROBOTICSFACILITY
from sc2.ids.unit_typeid import STARGATE
from sc2.ids.unit_typeid import TEMPLARARCHIVE
from sc2.ids.unit_typeid import DARKSHRINE
from sc2.ids.unit_typeid import ROBOTICSBAY
from sc2.ids.unit_typeid import FLEETBEACON
from sc2.ids.unit_typeid import VOIDRAY
from sc2.ids.unit_typeid import HIGHTEMPLAR
from sc2.ids.unit_typeid import SENTRY
from sc2.ids.unit_typeid import ADEPTPHASESHIFT
# zerg
from sc2.ids.unit_typeid import DRONE
from sc2.ids.unit_typeid import QUEEN
from sc2.ids.unit_typeid import SPORECRAWLER
from sc2.ids.unit_typeid import INFESTOR
from sc2.ids.unit_typeid import CORRUPTOR
from sc2.ids.unit_typeid import HYDRALISK
from sc2.ids.unit_typeid import VIPER
from sc2.ids.unit_typeid import MUTALISK
from sc2.ids.unit_typeid import RAVAGER
from sc2.ids.unit_typeid import OVERLORD
from sc2.ids.unit_typeid import BROODLORD
from sc2.ids.unit_typeid import HATCHERY
from sc2.ids.unit_typeid import LAIR
from sc2.ids.unit_typeid import HIVE
from sc2.ids.unit_typeid import BROODLING


class Chaosbot(sc2.BotAI):
    #   ############### CHANGE VALUE AD LIB
    do_log_success = True
    do_log_fail = True
    do_log_command = True
    do_log_attacktype = False
    do_log_workers = False
    do_log_population = False
    do_log_armysize = False
    do_log_army = False
    do_log_bcs = False
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
    do_log_enemies = False
    do_log_thoughts = False
    do_log_preps = False
    do_log_eggs = False
    do_log_birds = False
    do_log_buildstate = False
    do_log_throw = False
    do_log_throwspots = False
    do_log_bunker = True
    #   ############### CONSTANT
    #   constant over the iterations after iteration 0:
    #   other
    nowhere = Point2((1,1))
    somewhere = Point2((2,2))
    notag = -1
    all_structures = []
    all_structures_tobuildwalk = []
    all_army = []
    all_labarmy = []
    all_workertypes = []
    all_upgrades = []
    all_labs = [] # for labs, with place, always its motherbuilding place will be used.
    all_pfoc = []
    basekind_of_kind = {}
    antiair_detector = [] # cannons
    supply_of_army = {}
    builddura_of_thing = {}
    size_of_structure = {}
    liftable = []
    techtree = []
    all_species_things = set()
    cradle = []
    shipyard = None
    viking_targets = []
    landable = []
    all_repairable_shooters = set()
    hometop = set() # empty squares near start, inside the wall, inside ramps
    homeramp_pos = None
    enemytop = set() # empty squares near enemyloc
    enemyramp_pos = None
    bcenemies = set()
    danger_of_bcenemy = {}
    hate_of_bcenemy = {}
    nobuild_path = set()
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
    #
    flee_circle = []
    #   ############### GAMESTATE
    #   gamestate values constant in this iteration after gamestate:
    itera = -1
    all_bases = []
    all_refineries = []
    army_supply = 0
    #   ############### REST
    circle = []
    # thought -> prep -> egg -> bird
    preps = set() # (bar,martype,pos,dura,owner) or (scv,thingtype,pos,dura,owner)
    eggs = set() # (bar,martype,buildingpos,dura) or (scv,thingtype,buildingpos,dura)
    birds = set() # (thingtype,pos)
    # for different constructionwish subsystems to interact
    # Systems must first put a thought in "thoughts" before they can build_thing.
    # The (thingtype,pos) must be unique
    # Sometimes you cannot add because of maxam.
    thoughts = [] # multiset (thingtype,pos,owner)
    unthinkable = set() # (thingtype,pos)
    routine = 'start'
    #   stored tips
    tips = []
    tips_used = []
    #   coding problem
    function_result_Point2 = None
    # idle in this iteration:
    idle_structure_tags = []
    neighbours = set()
    surrender = False
    #   ############### ARMY AND STRUCTURE MANAGEMENT
    seen_enemy_units = set()
    seen_enemy_structuretypes = set()
    last_health = {}
    #   army coodination
    goal_of_unittag = {} # control of unit movement
    last_sd_of_unittag = {} # control of unit movement
    shame_of_unittag = {} # control of unit movement
    detour_of_unittag = {} # control of unit movement
    #
    special_tags = set()    # walldepots, wallbarracks, hercule,
                            # cheese_tank, cheese_scv,
                            # cheese2_bunker, cheese2_scvs, ...
    #
    state_of_unittag = {} # jumpy bc state "lazy","repair", etc. Also for tanks.
    burrowpos_of_wmt = {}
    attack_type = 'jumpy'
    cruisercount = 0
    lastcruisercount = 0
    home_of_flying_struct = {}
    landings_of_flying_struct = {}
    bestbctag = notag
    bestbc_dist_to_goal = 99999
    bc_fear = 250
    lasttarget_of_bc = {}
    homepole_of_wmt = {} # for cheesemines a scoutplace near goal
    pole_of_wmt = {} # for cheesemines a next scoutplace
    phase_of_wmt = {} # for cheesemines attack or flee
    marauder_goal = Point2((100,100))
    viking_goal  = Point2((100,100))
    last_health_of_maraudert = {}
    tankplaces = set()
    #   ambition contains labs, pfoc, upgr, army  just before actual build
    ambition_of_strt = {}
    owner_of_ambistrt = {}
    army_center_point = None
    #   (struc,place,tag) for tobuildwalk plans with a layout. Administrate to enable erasing.
    designs = set()
    # wall_barracks
    wall_barracks_pos = None
    wall_depot0_pos = None
    wall_depot1_pos = None
    wall_barracks_managed = False
    wall_barracks = None
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
    cheese_mine_count = 0
    cheese_tank = None
    cheese_mines = set()
    cheese_bunker_last_health = 0
    cheese_frames = 0
    # cheese2
    cheese2_bunkspots = set()
    cheese2_triedexp = set()
    # cheese3
    specialplaces = []
    cheese3_phase = 'A'
    cheese3_barracks_pos = None
    cheese3_bunker_pos = None
    cheese3_cc_pos = None
    cheese3_landing_pos = None
    cheese3_prison_pos = None
    cheese3_barracks = None
    cheese3_bunker = None
    cheese3_cc = None
    cheese3_scvs = set()
    # for cocoon:
    cheese3_cocoon_pos = None
    cheese3_barracks2_pos = None
    cheese3_bunker2_pos = None
    cheese3_barracks2 = None
    cheese3_bunker2 = None
    #
    ghost_phase = 'A'
    ghost_calmdown = 0
    nuke_target = None
    #
    cc_destiny = {} # [pos] = 'oc'/'pf'
    #
    expansions_doubled = False
    expansion_doubles = set()
    expansion_double_phase = {}
    expansion_original = {}
    #   ############### SCV MANAGEMENT
    #   traveller and builder scvs have a goal
    #   traveller and builder scvs have a structure to build
    goal_of_trabu_scvt = {}
    structure_of_trabu_scvt = {}
    owner_of_trabu_scvt = {}
    #   scv management:
    #   The tag of existing own scvs, in this iteration
    all_scvt = []
    #   The tag of existing refineries where we want to mine from, in this iteration
    all_gast = []
    #   The tag of existing minerals where we want to mine from, in this iteration
    all_mimt = []
    #   job_of_scvt dictionary
    good_jobs = ('builder','shiprepairer','traveller','arearepairer','escorter','scout','cheeser','hercule')
    bad_jobs = ('gasminer','mimminer','applicant','fleeer','defender')
    no_jobs = ('idler','suicider','volunteer')
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
    scout_pole = 0
    # blocker
    blocker_pos = []
    blocker_tag = notag
    blocker_pole = 0
    blocker_scv = None
    #   interface planning / workers
    gas_advice = 0
    # checks
    minedirection_of_scvt = {}
    # the lifter of buildings and tanks
    hercule = None
    #   ############### PLAY CHOICES
    game_phase = 'init'
    #   the planning_of_buildorder routine
    # bagofthings is a list of things, that we want to be made. No infected.
    # bagoftree is a bagofthings including still needed techtree demands. No infected.
    # bagofcradle is a bagofthings, now also the cradle demand is met; flying is not sufficient.
    # buildseries is a list of buildings, that we want to make. It contains techtree predecessors and has an order. Can have infected.
    # buildorder is a list of (building,place) combinations. No infected.
    #    buildorder contains (thing,somewhere) for things with a cradle, i.e. army, upgr, pfoc, labs.
    #    So the choice can be made during the planning.
    # planning is a list of buildplans, including timing.
    # those plans have a _exe variant, the chosen actual one.
    # Work has to be removed from the _exe when the order is started.
    # It is not clear when to start the work in the _exe.
    bagofthings = []
    bagoftree = []
    bagofcradle = []
    buildseries = []
    buildorder = []
    planning = []
    #
    bagofthings_exe = []
    bagoftree_exe = []
    bagofcradle_exe = []
    buildseries_exe = []
    buildorder_exe = [] # like buildorder, but extra field: status='new'/'thought'/'prep'
    planning_exe = []
    #
    buildseries_opening = []
    #
    all_future_basepos = set() # used when making buildorder
    #
    throwspots = [] # (thing spot status='new'/'thought' owner prio=1/2/3)
    #
    but_i_had_structures = 0 # amount of own structures, excl bunkers
    but_i_had_flying = 0 # make new plans if a weak building lifted
    #
    buildandretry = set() # (scvt, building, goal, iter) for tobuildwalk buildings
    #
    midgame_things = []
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
    situation_gym = set() # for army and upgrade
    situation_training = set() # for army and upgrade
    situation_ambition = set() # for pf and lab
    situation_growing = set() # for pf and lab
    situation_thingkinds = set()
    situation_buildings_and_parts = set()
    situation_events = set()
    # to abort plans
    buildorderdelay = 0
    crad_places = set()
    bui_min_lab = {}
    happy_made = set()
    #   strategy[0] is vs Zerg []
    strategy = []
    game_choice = []
    radio_choices = 13
    game_choices = 32
    game_result = 'doubt'
    opening_name = 'no'
    #

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
        #  interface
        bunker_if.init_step(self)
        #
        await self.gamestate()
        self.get_eggs()
        self.get_preps() # after get_eggs
        await self.get_birds()
        self.log_thoughts() # there is no get_thoughts()
        self.log_resource()
        self.log_armysize()
        self.log_bcs()
        self.check_shipyard() # after gamestate, before buildorder stuff
        await self.bunkercheese()
        await self.bunkercheese2()
        if (iteration % 5 == 4):
            await self.implementing_buildorder_exe()
            await self.make_planning_exe()
            await self.follow_planning_exe()
        await self.build_worker(100-self.minerals//100)
        await self.throw_advance()
        await self.start_construction()
        await self.siege_tanks()
        await self.use_mine()
        await self.fire_yamato()
        await self.battle_dodge_bile()
        await self.hellion_dodge()
        await self.may_cancel()
        await self.ruin()
        await self.repair_bc()
        self.get_arearepairer()
        await self.repair_it()
        await self.supplydepots_adlib()
        if (iteration % 4 == 3):
            self.delaying_too_much()
            await self.build_minima()
            await self.refineries_adlib()
            await self.upgrades_adlib()
            self.army_adlib()
            self.armybuildings_adlib()
            self.expansion_advisor()
            self.big_spender()
            await self.lift()
        await self.manage_the_wall()
        await self.cheese_army()
        await self.attack_with_bc()
        await self.attack_with_rest()
        await self.manage_workers()
        if self.minerals < self.vespene:
            await self.manage_minerals()
            await self.manage_gas()
        else:
            await self.manage_gas()
            await self.manage_minerals()
        await self.manage_rest()
        await self.worker_defence()
        await self.scv_endgame()
        if (iteration % 7 == 6):
            await self.win_loss()
            await self.do_surrender()
            await self.mimminer_boss()
            await self.gasminer_boss()
        self.wall_barracks_redirect()
        self.see_enemies()
        if (iteration % 61 == 60):
            self.log_enemies()
            self.lower_some_depots()
            self.hop_cc()
        await self.mules()
        await self.do_buildandretry()
        await self.do_pf_rush()
        await self.do_cocoon()
        await self.catch_a_bug()
        self.log_throwspots()
        await self.do_hercule()
        self.extreme_spender()
        self.blocker()
        await self.ghost_fun()
        bunker_if.step()



# *********************************************************************************************************************
    async def my_init(self):
        self.routine = 'my_init'
        self.log_success('##############################################################################')
        random.seed()
        # liftable
        self.liftable = [BARRACKS,FACTORY,STARPORT,COMMANDCENTER,ORBITALCOMMAND]
        self.landable = [BARRACKSFLYING,FACTORYFLYING,STARPORTFLYING,COMMANDCENTERFLYING,ORBITALCOMMANDFLYING]
        # enemy air with weak air defence
        self.viking_targets = [BANSHEE,LIBERATOR,LIBERATORAG,ORACLE,BROODLORD,OVERLORD,OBSERVER,BATTLECRUISER,
                               CORRUPTOR,MUTALISK,TEMPEST,VIPER]
        # enemy that can hurt a bc, danger (run at sum 100), hate (shoot high first)
        self.init_bcenemy(ARCHON, 40, 5)
        self.init_bcenemy(CARRIER, 20, 4)
        self.init_bcenemy(QUEEN, 40, 4)
        self.init_bcenemy(CORRUPTOR, 30, 4)
        self.init_bcenemy(SPORECRAWLER, 60, 6)
        self.init_bcenemy(PHOTONCANNON, 60, 6)
        self.init_bcenemy(INFESTOR, 40, 6)
        if self.enemy_race != Race.Zerg:
            self.init_bcenemy(BATTLECRUISER, 50, 3)
            self.init_bcenemy(VIKINGFIGHTER, 30, 5)
            self.init_bcenemy(MISSILETURRET, 60, 6)
            self.init_bcenemy(THOR, 40, 3)
            self.init_bcenemy(PHOENIX, 30, 5)
            self.init_bcenemy(MARINE, 10, 2)
            self.init_bcenemy(SCV, 0, 1)
        self.init_bcenemy(HYDRALISK, 20, 3)
        self.init_bcenemy(VIPER, 30, 4)
        self.init_bcenemy(VOIDRAY, 30, 4)
        self.init_bcenemy(RAVAGER, 20, 2)
        self.init_bcenemy(CYCLONE, 50, 3)
        self.init_bcenemy(STALKER, 30, 4)
        self.init_bcenemy(SENTRY, 10, 4)
        self.init_bcenemy(HIGHTEMPLAR, 10, 4)
        self.init_bcenemy(TEMPEST, 20, 4)
        self.init_bcenemy(DRONE,0,1)
        self.init_bcenemy(PROBE,0,1)
        # anti-air detector structure
        self.antiair_detector = [MISSILETURRET,PHOTONCANNON,SPORECRAWLER]
        # all_labs wegens verschoven plaatsing etc
        self.all_labs = [BARRACKSTECHLAB,FACTORYTECHLAB,STARPORTTECHLAB,BARRACKSREACTOR,FACTORYREACTOR,STARPORTREACTOR]
        self.all_pfoc = [PLANETARYFORTRESS,ORBITALCOMMAND]
        self.all_workertypes = [SCV,PROBE,DRONE]
        # list of terran structures, with builddura, size. Not flying, can be lowered.
        self.init_structures(SUPPLYDEPOT, 21, 2)
        self.init_structures(SUPPLYDEPOTLOWERED, 21, 2)
        self.init_structures(BARRACKS, 46, 3)
        self.init_structures(REFINERY, 21, 3)
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
        self.init_structures(SENSORTOWER, 18, 2)
        self.init_structures(GHOSTACADEMY, 20, 3)
        self.init_structures(BARRACKSREACTOR, 36, 2)
        self.init_structures(FACTORYREACTOR, 36, 2)
        self.init_structures(STARPORTREACTOR, 36, 2)
        # protoss added for layout
        self.init_structures(NEXUS, 71, 5)
        self.init_structures(PYLON, 18, 2)
        self.init_structures(ASSIMILATOR, 21, 3)
        self.init_structures(GATEWAY, 46, 3)
        self.init_structures(FORGE, 32, 3)
        self.init_structures(PHOTONCANNON, 29, 2)
        self.init_structures(SHIELDBATTERY, 29, 2)
        self.init_structures(WARPGATE, 7, 3)
        self.init_structures(CYBERNETICSCORE, 36, 3)
        self.init_structures(TWILIGHTCOUNCIL, 36, 3)
        self.init_structures(ROBOTICSFACILITY, 46, 3)
        self.init_structures(STARGATE, 43, 3)
        self.init_structures(TEMPLARARCHIVE, 36, 3)
        self.init_structures(DARKSHRINE, 71, 2)
        self.init_structures(ROBOTICSBAY, 46, 3)
        self.init_structures(FLEETBEACON, 43, 3)
        # add for cheese with barracks and bunker
        # warning: this complicated much. Restrict to buildseries and placement.txt
        self.init_structures(INFESTEDBARRACKS, 46, 3)
        self.init_structures(INFESTEDBUNKER, 29, 3)
        self.init_structures(INFESTEDFACTORY, 43, 3)
        self.init_structures(INFESTEDSTARPORT, 36, 3)
        self.init_structures(INFESTEDCOCOON, 50, 8)
        # scv
        self.builddura_of_thing[SCV] = 12
        # army, builddura, supply
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
        self.init_army(GHOST,29,2)
        self.init_army(NUKESILONOVA,43,0)
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
        self.init_upgrade(PERSONALCLOAKING, 86)
        # for some strange things, the normal variant:
        self.basekind_of_kind = {}
        self.init_basekind(SUPPLYDEPOTLOWERED,SUPPLYDEPOT)
        self.init_basekind(REFINERYRICH,REFINERY)
        self.init_basekind(BARRACKSFLYING,BARRACKS)
        self.init_basekind(FACTORYFLYING,FACTORY)
        self.init_basekind(STARPORTFLYING,STARPORT)
        self.init_basekind(COMMANDCENTERFLYING,COMMANDCENTER)
        self.init_basekind(ORBITALCOMMANDFLYING,ORBITALCOMMAND)
        self.init_basekind(SIEGETANKSIEGED,SIEGETANK)
        self.init_basekind(WIDOWMINEBURROWED,WIDOWMINE)
        self.init_basekind(LIBERATORAG,LIBERATOR)
        self.init_basekind(INFESTEDBARRACKS,BARRACKS)
        self.init_basekind(INFESTEDBUNKER,BUNKER)
        self.init_basekind(INFESTEDFACTORY,FACTORY)
        self.init_basekind(INFESTEDSTARPORT,STARPORT)
        # things that, to be built, need a cradle (a free building)
        # cradle is unique, so scvs are omitted
        self.init_cradle(RAVEN,STARPORT)
        self.init_cradle(MEDIVAC,STARPORT)
        self.init_cradle(VIKINGFIGHTER,STARPORT)
        self.init_cradle(LIBERATOR,STARPORT)
        self.init_cradle(MARINE,BARRACKS)
        self.init_cradle(MARAUDER,BARRACKS)
        self.init_cradle(GHOST,BARRACKS)
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
        self.init_cradle(PERSONALCLOAKING,GHOSTACADEMY)
        self.init_cradle(PLANETARYFORTRESS,COMMANDCENTER)
        self.init_cradle(ORBITALCOMMAND,COMMANDCENTER)
        self.init_cradle(BATTLECRUISERENABLESPECIALIZATIONS,FUSIONCORE)
        self.init_cradle(NUKESILONOVA,GHOSTACADEMY)
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
        self.init_techtree(GHOST,BARRACKSTECHLAB)
        self.init_techtree(GHOST,GHOSTACADEMY)
        self.init_techtree(NUKESILONOVA,FACTORY)
        # First is upgrade
        self.init_techtree(TERRANSHIPWEAPONSLEVEL2,TERRANSHIPWEAPONSLEVEL1)
        self.init_techtree(TERRANSHIPWEAPONSLEVEL3,TERRANSHIPWEAPONSLEVEL2)
        self.init_techtree(TERRANVEHICLEANDSHIPARMORSLEVEL2,TERRANVEHICLEANDSHIPARMORSLEVEL1)
        self.init_techtree(TERRANVEHICLEANDSHIPARMORSLEVEL3,TERRANVEHICLEANDSHIPARMORSLEVEL2)
        self.init_techtree(TERRANINFANTRYWEAPONSLEVEL2,TERRANINFANTRYWEAPONSLEVEL1)
        self.init_techtree(TERRANINFANTRYWEAPONSLEVEL3,TERRANINFANTRYWEAPONSLEVEL2)
        self.compute_all_species_things()
        #       bootstrap code   after initial    from sc2constants import *
        #       for thing in self.all_species_things:
        #           if type(thing) == UnitTypeId:
        #               print('from sc2.ids.unit_typeid import '+thing.name)
        #           if type(thing) == UpgradeId:
        #               print('from sc2.ids.upgrade_id import '+thing.name)
        self.enemyloc = self.enemy_start_locations[0].position
        self.cheese2_triedexp.add(self.enemyloc)
        self.enemy_target_building_loc = self.enemyloc
        # all_repairable_shooters for repair priority
        self.all_repairable_shooters = {PLANETARYFORTRESS, MISSILETURRET, BUNKER}
        for ut in self.all_army:
            if ut not in [MARINE,MARAUDER]: # bio
                self.all_repairable_shooters.add(ut)
        # give gather init
        for mim in self.mineral_field:
            if self.near(mim.position, self.start_location.position, self.miner_bound):
                self.count_of_mimt[mim.tag] = 0
        for scv in self.units(SCV):
            self.job_of_scvt[scv.tag] = 'mimminer'
            self.promotionsite_of_scvt[scv.tag] = scv.position
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
            self.count_of_mimt[amimt] += 1
        self.fix_count_of_job()
        #
        # strategy choices
        await self.init_strategy()
        #
        # layout
        self.map_left = self.game_info.playable_area.x
        self.map_right = self.game_info.playable_area.width+self.game_info.playable_area.x
        self.map_bottom = self.game_info.playable_area.y
        self.map_top = self.game_info.playable_area.height+self.game_info.playable_area.y
        self.get_layout()
        self.write_layout(COMMANDCENTER,self.start_location.position)
        # append to layout.txt for placer.py to compute placement tips
        layout_if.mapname = self.game_info.map_name
        layout_if.startx = self.start_location.position.x
        layout_if.starty = self.start_location.position.y
        layout_if.enemyx = self.enemyloc.x
        layout_if.enemyy = self.enemyloc.y
        layout_if.save_layout()
        #
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
            elif (woord[0] == 'position') and (woord[1] == 'HOMERAMP'):
                self.homeramp_pos = Point2((float(woord[2]), float(woord[3])))
            elif (woord[0] == 'position') and (woord[1] == 'ENEMYRAMP'):
                self.enemyramp_pos = Point2((float(woord[2]), float(woord[3])))
            elif (woord[0] == 'position') and (woord[1] == 'INFESTEDCOCOON'):
                self.cheese3_cocoon_pos = Point2((float(woord[2]), float(woord[3])))
        # get nobuild_path tips
        self.nobuild_path = set()
        for nr in range(0, len(self.tips)):
            ti = self.tips[nr]
            woord = ti.split()
            if (woord[0] == 'path'):
                el = 1
                while el < len(woord):
                    self.nobuild_path.add(Point2((float(woord[el]), float(woord[el+1]))))
                    el += 2
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
        # nobuild a tankpath to the center
        for tile in self.nobuild_path:
            self.nobuild_tile(tile)
        # check if the barracks can have a lab
        self.write_layout(SUPPLYDEPOT,self.wall_depot0_pos)
        self.write_layout(SUPPLYDEPOT,self.wall_depot1_pos)
        if self.check_layout(BARRACKS,self.wall_barracks_pos):
            self.log_success('Nice wall, I can build a lab')
        else:
            self.log_success('Dumb wall, I can`t build a lab')
            self.make_unthinkable(BARRACKSTECHLAB,self.wall_barracks_pos)
            self.make_unthinkable(BARRACKSREACTOR,self.wall_barracks_pos)
        self.erase_layout(SUPPLYDEPOT,self.wall_depot0_pos)
        self.erase_layout(SUPPLYDEPOT,self.wall_depot1_pos)
        # opening
        if self.game_choice[0]:
            self.opening_name = 'twobase-bc'
            self.buildseries_opening = [SUPPLYDEPOT, REFINERY, BARRACKS, SUPPLYDEPOT, MARINE, REFINERY, FACTORY, MARINE, \
                                       STARPORT, COMMANDCENTER, FUSIONCORE, STARPORTTECHLAB, BATTLECRUISER]
        if self.game_choice[1]:
            self.opening_name = 'elementary'
            self.buildseries_opening = [SUPPLYDEPOT, REFINERY, BARRACKS, SUPPLYDEPOT, MARINE, ORBITALCOMMAND]
        if self.game_choice[2]:
            self.opening_name = 'cheese-expand'
            self.buildseries_opening = [SUPPLYDEPOT, INFESTEDBARRACKS, REFINERY, INFESTEDBUNKER, SUPPLYDEPOT, INFESTEDFACTORY, \
                                        BARRACKS, REFINERY, COMMANDCENTER]
        if self.game_choice[3]:
            self.opening_name = 'cheese-bc'
            self.buildseries_opening = [SUPPLYDEPOT, INFESTEDBARRACKS, REFINERY, INFESTEDBUNKER, \
                                        SUPPLYDEPOT, INFESTEDFACTORY, BARRACKS, REFINERY, \
                                        STARPORT, SUPPLYDEPOT, FUSIONCORE, STARPORTTECHLAB, SUPPLYDEPOT, BATTLECRUISER]
        if self.game_choice[4]:
            self.opening_name = 'expand'
            self.buildseries_opening = [SUPPLYDEPOT, COMMANDCENTER, BARRACKS, SUPPLYDEPOT]
        if self.game_choice[5]:
            self.opening_name = 'double-expand'
            self.buildseries_opening = [SUPPLYDEPOT, COMMANDCENTER, COMMANDCENTER, BARRACKS, SUPPLYDEPOT]
        if self.game_choice[6]:
            self.opening_name = 'cheesebunk'
            self.buildseries_opening = [SUPPLYDEPOT, INFESTEDBARRACKS, INFESTEDBUNKER, INFESTEDBUNKER,
                                        INFESTEDBUNKER, SUPPLYDEPOT, REFINERY, INFESTEDFACTORY, BARRACKS, REFINERY]
        if self.game_choice[7]:
            self.opening_name = 'rush-bc'
            self.buildseries_opening = [SUPPLYDEPOT, REFINERY, BARRACKS, SUPPLYDEPOT, MARINE, FACTORY, REFINERY, MARINE,
                                       STARPORT, FUSIONCORE, STARPORTTECHLAB, BATTLECRUISER, COMMANDCENTER]
        if self.game_choice[8]:
            self.opening_name = 'defence'
            self.buildseries_opening = [SUPPLYDEPOT, REFINERY, BARRACKS, SUPPLYDEPOT, MARINE, FACTORY, MARINE,
                                        FACTORYTECHLAB, MARINE, SUPPLYDEPOT, SIEGETANK, ENGINEERINGBAY]
        if self.game_choice[9]:
            self.opening_name = 'pf-rush'
            self.buildseries_opening = [SUPPLYDEPOT, BARRACKS, BUNKER, REFINERY, SUPPLYDEPOT, MARINE, COMMANDCENTER, MARINE,
                                        MARINE, ENGINEERINGBAY, REFINERY, MARINE, FACTORY]
            self.init_pf_rush()
        if self.game_choice[10]:
            self.opening_name = 'expa-ma'
            self.buildseries_opening = [SUPPLYDEPOT, COMMANDCENTER, BARRACKS, SUPPLYDEPOT, MARINE, REFINERY, COMMANDCENTER,
                                        MARINE, ORBITALCOMMAND, FACTORY, MARINE, COMMANDCENTER, FACTORYTECHLAB, MARINE,
                                        MARINE, ORBITALCOMMAND, SIEGETANK, MARINE]
        if self.game_choice[11]:
            self.opening_name = 'cocoon'
            self.buildseries_opening = [SUPPLYDEPOT, BARRACKS, BARRACKS, SUPPLYDEPOT, MARINE, BUNKER, MARINE, BUNKER, MARINE,
                                        MARINE, REFINERY, MARINE]
            self.init_cocoon()
        if self.game_choice[12]:
            self.opening_name = 'triple-expand'
            self.buildseries_opening = [SUPPLYDEPOT, COMMANDCENTER, COMMANDCENTER, BARRACKS, SUPPLYDEPOT, COMMANDCENTER, MARINE]
            self.game_choice[30] = True # bunkers
        # self.radio_choices = 13
        self.log_success('OPENING: '+self.opening_name)
        #
        #  preparing midgame
        self.midgame_things = []
        # The midgame really needs a battlecruiser, or the core is tooo late
        # This routine is called in the init phase, you cannot depend on e.g. amount of barracks
        self.midgame(BATTLECRUISER,1)
        if self.game_choice[20]:
            self.midgame(VIKINGFIGHTER,1)
        if self.game_choice[21]:
            self.midgame(SIEGETANK,1)
        if self.game_choice[22]:
            self.midgame(SIEGETANK,2)
        if self.game_choice[23]:
            self.midgame(MARINE, 2)
        else:
            self.midgame(MARINE, 5)
        self.midgame(REFINERY,2)
        if self.game_choice[24]:
            self.midgame(REFINERY,4)
            self.midgame(COMMANDCENTER,2)
            self.midgame(STARPORT,2)
            self.midgame(STARPORTTECHLAB,2)
        if self.game_choice[25]:
            self.midgame(ENGINEERINGBAY,1)
            self.midgame(MISSILETURRET,1)
            self.midgame(PLANETARYFORTRESS,1)
        # made self.midgame_things
        # circle
        self.make_circle(10)
        self.flee_circle = self.circle.copy()
        # blocker
        self.init_blocker()
        # rally
        for cc in self.structures(COMMANDCENTER):
            cc(AbilityId.RALLY_BUILDING,self.start_location.position.towards(self.game_info.map_center,-3))
        # get hometop, enemytop
        self.get_hometop()
        self.get_enemytop()
        # name_of_scvt: fun translation of scvt to english boy name
        pl = open('data/names.txt','r')
        self.all_names = pl.read().splitlines()
        pl.close()
        # get_shield_pos
        self.get_shield_pos()
        # mapspecific
        if self.game_info.map_name == 'Golden Wall LE':
            self.miner_bound = 18
        # chat
        await self._client.chat_send('Chaosbot version 13 nov 2020, made by MerkMore', team_only=False)

    #*********************************************************************************************************************
#   logging

    async def catch_a_bug(self):
        abug = False
        # put detectioncondition under here
        # put detectioncondition above here
        if abug:
            await self._client.chat_send('catch a bug', team_only=False)
            please_breakpoint_this_line = True

    def log_fail(self,bol,stri):
        if self.do_log_fail:
            if not bol:
                print(' On '+str(self.itera)+' fail '+self.routine+' '+stri)

    def log_success(self,stri):
        if self.do_log_success:
            print(' On '+str(self.itera)+' success '+self.routine+' '+stri) 

    def log_bunker(self,stri):
        if self.do_log_bunker:
            print(' On '+str(self.itera)+' bunker '+self.routine+' '+stri)

    def log_army(self,stri):
        if self.do_log_army:
            print(' On '+str(self.itera)+' army '+self.routine+' '+stri)

    def log_bcs(self):
        if self.do_log_bcs:
            atty = self.attack_type
            inrep = 0
            for bc in self.units(BATTLECRUISER):
                if self.state_of_unittag[bc.tag] == 'repair':
                    inrep +=1
            print(' On '+str(self.itera)+' attacktype '+self.routine+' '+atty+', in rep '+str(inrep))
            if atty == 'jumpy':
                for bc in self.units(BATTLECRUISER):
                    state = self.state_of_unittag[bc.tag]
                    if bc.tag in self.last_sd_of_unittag:
                        sd = self.last_sd_of_unittag[bc.tag]
                    else:
                        sd = -1
                    print('a bc '+state+' health '+str(bc.health)+' sd '+str(sd))

    async def log_attacktype(self,stri):
        if self.do_log_attacktype:
            print(' On '+str(self.itera)+' attacktype '+self.routine+' '+stri)

    def log_workers(self,stri):
        if self.do_log_workers:
            print(' On '+str(self.itera)+' workers '+self.routine+' '+stri) 

    def log_layout(self,stri):
        if self.do_log_layout:
            print(' On '+str(self.itera)+' layout '+self.routine+' '+stri) 

    def log_placing(self,stri):
        if self.do_log_placing:
            print(' On '+str(self.itera)+' placing '+self.routine+' '+stri) 

    def log_command(self,stri):
        if self.do_log_command:
            print(' On '+str(self.itera)+' commands '+self.routine+' '+stri)

    def log_planning_bp(self,bp):
        if self.do_log_planning:
            print(' On '+str(self.itera)+' planning '+self.name(bp[0])+' '+bp[1].name+' '+str(bp[2][0])+','+str(bp[2][1])+'   '+\
                str(bp[3])+'   '+str(bp[4])+'   '+str(bp[5]))

    def log_planning(self,stri):
        if self.do_log_planning:
            print(' On '+str(self.itera)+' planning '+stri)

    def log_throw(self,stri):
        if self.do_log_throw:
            print(' On '+str(self.itera)+' throw '+stri)

    def txt(self, point) -> str:
        return str(point.x)+','+str(point.y)

    def log_throwspots(self):
        if self.do_log_throwspots:
            if len(self.throwspots) > 0:
                print(' On '+str(self.itera)+' ---------- throwspots ----------')
                for priority in [1,2,3]:
                    for sta in ['new','thought']:
                        for (th,pl,st,ow, pri) in self.throwspots:
                            if (st == sta) and (pri == priority):
                                print(' On '+str(self.itera)+' --- '+th.name+' '+self.txt(pl)+' '+st+' '+ow+' '+str(pri))

    def log_boss(self,stri):
        if self.do_log_boss:
            print(' On '+str(self.itera)+' boss '+self.routine+' '+stri)

    def log_armysize(self):
        if self.do_log_armysize:
            stri = ''
            for ut in self.all_army:
                am = self.units(ut).amount
                if am>0:
                    stri = stri+'   '+ut.name+' '+str(am)
            print(' On '+str(self.itera)+' army'+stri)

    def name(self,scvt) -> str:
        if scvt in self.name_of_scvt:
            return self.name_of_scvt[scvt]
        else:
            return str(scvt)

    def log_gasminer(self):
        if self.do_log_gasminer:
            print(' On '+str(self.itera)+' gasminer: ')
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
            print(' On '+str(self.itera)+' population: '+lin)

    def log_limbo(self,stri):
        if self.do_log_limbo:
            print(' On '+str(self.itera)+' limbo: '+stri) 

    def log_resource(self):
        if self.do_log_resource:
            print(' On '+str(self.itera)+' minerals '+str(self.minerals)+'   gas '+str(self.vespene))

    def log_buildseries(self, instri):
        if self.do_log_buildseries:
            stri = instri
            for thing in self.buildseries:
                stri = stri+' '+thing.name
            print(' On '+str(self.itera)+' buildseries: '+stri)

    def log_buildsit(self, stri):
        if self.do_log_buildsit:
            print(' On '+str(self.itera)+' buildsit: '+stri)

    def log_time(self,stri):
        if self.do_log_time:
            print(' On '+str(self.itera)+' time: '+stri)

    def log_buildstate(self,stri):
        if self.do_log_buildstate:
            print(' On '+str(self.itera)+' buildstate: '+stri)

    def log_cheese(self):
        if self.do_log_cheese:
            if self.cheese_phase != 'Z':
                print(' On '+str(self.itera)+' cheese phase '+self.cheese_phase
                      +'   cheese3 '+self.cheese3_phase)


    def init_cheese_position(self, anchor,good_sdist,building) -> Point2:
        besttry = 99999
        found_spot = self.nowhere
        estimate = anchor.towards(self.game_info.map_center,sqrt(good_sdist))
        self.put_on_the_grid(building, estimate)
        estimate = self.function_result_Point2
        for dx in range(-10, 10):
            for dy in range(-10, 10):
                maypos = Point2((estimate.x + dx, estimate.y + dy))
                if self.check_layout(building, maypos):
                    sd = self.sdist(anchor, maypos)
                    try0 = (sd - good_sdist)*(sd-good_sdist) + self.circledist(maypos,self.start_location.position)
                    if try0 < besttry:
                        found_spot = maypos
                        besttry = try0
        if found_spot != self.nowhere:
            self.write_layout(building,found_spot)
        return found_spot


    def init_pf_rush(self):
        # fun placement of barracks, bunker, commandcenter, planetaryfortress
        # enemy_natural
        bestsd = 99999
        for pos in self.expansion_locations_list:
            if pos != self.enemyloc:
                sd = self.sdist(pos,self.enemyramp_pos)
                if sd < bestsd:
                    enemy_natural = pos
                    bestsd = sd
        self.write_layout(COMMANDCENTER,enemy_natural)
        self.cheese3_landing_pos = self.init_cheese_position(enemy_natural,115,COMMANDCENTER) # 115
        self.cheese3_bunker_pos = self.init_cheese_position(self.cheese3_landing_pos,38,BUNKER) # 38
        self.cheese3_barracks_pos = self.init_cheese_position(self.cheese3_bunker_pos,11,ARMORY) # 11 BARRACKS nolab
        self.cheese3_cc_pos = self.init_cheese_position(self.cheese3_barracks_pos,28,COMMANDCENTER) # 28
        self.cheese3_prison_pos = self.init_cheese_position(self.cheese3_bunker_pos,12,MISSILETURRET) # 8
        #layout_if.photo_layout()
        # erase
        self.erase_layout(COMMANDCENTER,enemy_natural)
        self.erase_layout(COMMANDCENTER,self.cheese3_landing_pos)
        self.erase_layout(BUNKER,self.cheese3_bunker_pos)
        self.erase_layout(ARMORY,self.cheese3_barracks_pos) # BARRACKS nolab
        self.erase_layout(COMMANDCENTER,self.cheese3_cc_pos)
        self.erase_layout(MISSILETURRET,self.cheese3_prison_pos)
        # use all
        self.specialplaces.append((BARRACKS,self.cheese3_barracks_pos))
        self.specialplaces.append((BUNKER,self.cheese3_bunker_pos))
        self.specialplaces.append((COMMANDCENTER,self.cheese3_cc_pos))


    def init_cocoon(self):
        # fun placement of barracks, bunker, barracks,bunker
        # enemy_natural
        bestsd = 99999
        for pos in self.expansion_locations_list:
            if pos != self.enemyloc:
                sd = self.sdist(pos,self.enemyramp_pos)
                if sd < bestsd:
                    enemy_natural = pos
                    bestsd = sd
        self.write_layout(COMMANDCENTER,enemy_natural)
        if self.cheese3_cocoon_pos is None:
            self.cheese3_cocoon_pos = self.init_cheese_position(enemy_natural,320,INFESTEDCOCOON)
        self.cheese3_bunker_pos = Point2((self.cheese3_cocoon_pos.x+2.5,self.cheese3_cocoon_pos.y-0.5))
        self.cheese3_bunker2_pos = Point2((self.cheese3_cocoon_pos.x+0.5,self.cheese3_cocoon_pos.y+2.5))
        self.cheese3_barracks_pos = Point2((self.cheese3_cocoon_pos.x-2.5,self.cheese3_cocoon_pos.y+0.5))
        self.cheese3_barracks2_pos = Point2((self.cheese3_cocoon_pos.x-0.5,self.cheese3_cocoon_pos.y-2.5))
        self.cheese3_prison_pos = self.cheese3_cocoon_pos
        #layout_if.photo_layout()
        # erase
        self.erase_layout(COMMANDCENTER,enemy_natural)
        self.erase_layout(INFESTEDCOCOON,self.cheese3_cocoon_pos)
        # use all
        self.specialplaces.append((BARRACKS,self.cheese3_barracks_pos))
        self.specialplaces.append((BUNKER,self.cheese3_bunker_pos))
        self.specialplaces.append((BARRACKS,self.cheese3_barracks2_pos))
        self.specialplaces.append((BUNKER,self.cheese3_bunker2_pos))



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

    def log_preps(self):
        if self.do_log_preps:
            for (bar,martype,pos,dura,owner) in self.preps:
                if bar in self.units(SCV):
                    print(' On '+str(self.itera)+' ' + self.name(bar.tag) + ' preps for a ' + martype.name + \
                          ' at ' + self.txt(pos) + ' dura ' + str(dura) + ' by '+owner)
                else:
                    print(' On '+str(self.itera)+' ' + bar.name + ' preps for a ' + martype.name + \
                          ' at '+self.txt(pos) + ' dura ' + str(dura) + ' by ' + owner)

    def log_eggs(self):
        if self.do_log_eggs:
            for (bar,martype,pos,dura) in self.eggs:
                if bar in self.units(SCV):
                    print(' On '+str(self.itera)+' ' + self.name(bar.tag) + ' eggs a ' + martype.name + \
                          ' at ' + self.txt(pos) + ' for '+str(dura))
                else:
                    print(' On '+str(self.itera)+' '+bar.name+' at '+self.txt(pos) + \
                          ' eggs a '+martype.name + ' for '+str(dura))

    def log_birds(self):
        if self.do_log_birds:
            for (thingtype,pos) in self.birds:
                if thingtype == SCV:
                    seen = False
                    for scv in self.units(SCV):
                        if scv.position == pos:
                            seen = True
                            print(' On '+str(self.itera)+' ' + self.name(scv.tag) + ' is at ' + self.txt(pos))
                    if not seen:
                        print(' On '+str(self.itera)+' ' + thingtype.name + ' is at ' + self.txt(pos))
                else:
                    print(' On '+str(self.itera)+' ' + thingtype.name + ' is at ' + self.txt(pos))

    def log_thoughts(self):
        if self.do_log_thoughts:
            for (thingtype,pos,owner) in self.thoughts:
                print(' On '+str(self.itera)+' ' + owner + ' is thinking of ' + thingtype.name + ' at ' + self.txt(pos))
            for (thingtype,pos) in self.unthinkable:
                print('Unthinkable is a ' + thingtype.name + ' at ' + self.txt(pos))

    #******************************************************************************************************************

    def read_layout(self, vakx,vaky) -> int:
        if (0 <= vakx) and (vakx < 200) and (0 <= vaky) and (vaky < 200):
            point = Point2((vakx,vaky))
            if self.has_creep(point):
                return 6
            else:
                return layout_if.layout[vakx][vaky]
        else:
            return 3

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
        if struc in self.all_structures:
            self.designs.add((struc,place,self.notag))
            self.log_layout('write position '+struc.name+' '+str(x)+' '+str(y))
            siz = self.size_of_structure[struc]
            for vakx in range(round(x-siz/2),round(x+siz/2)):
                for vaky in range(round(y-siz/2),round(y+siz/2)):
                    layout_if.layout[vakx][vaky] = 4
            if struc in [BARRACKS,FACTORY,STARPORT]:
                x += 2.5
                y -= 0.5
                siz = 2
                for vakx in range(round(x-siz/2),round(x+siz/2)):
                    for vaky in range(round(y-siz/2),round(y+siz/2)):
                        layout_if.layout[vakx][vaky] = 4

    def erase_layout(self,struc,place):
        self.put_on_the_grid(struc,place)
        place = self.function_result_Point2
        x = place.x
        y = place.y
        if struc in self.all_structures:
            self.log_layout('erase position '+struc.name+' '+str(x)+' '+str(y))
            siz = self.size_of_structure[struc]
            if (struc in [REFINERY,REFINERYRICH]):
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
        if (struc in self.all_structures):
            if (struc in [REFINERY,REFINERYRICH]):
                mustbecolor = 1
            else:
                mustbecolor = 0
            siz = self.size_of_structure[struc] # 5 for a cc, 2 for a depot etc
            for vakx in range(round(x-siz/2),round(x+siz/2)):
                for vaky in range(round(y-siz/2),round(y+siz/2)):
                    placable = placable and (self.read_layout(vakx,vaky) == mustbecolor)
            if struc in [BARRACKS,FACTORY,STARPORT]:
                x += 2.5
                y -= 0.5
                siz = 2
                for vakx in range(round(x-siz/2),round(x+siz/2)):
                    for vaky in range(round(y-siz/2),round(y+siz/2)):
                        placable = placable and (self.read_layout(vakx,vaky) == mustbecolor)
            if struc in [COMMANDCENTER,ORBITALCOMMAND]:
                # can not be placed close to a geyser or mineral
                siz = 10
                for vakx in range(round(x - siz / 2), round(x + siz / 2)):
                    for vaky in range(round(y - siz / 2), round(y + siz / 2)):
                        placable = placable and (self.read_layout(vakx,vaky) != 1)
        return placable

    def nobuild_tile(self,sq):
        layout_if.layout[round(sq.x) + 0][round(sq.y) + 0] = 5
        layout_if.layout[round(sq.x) - 1][round(sq.y) + 0] = 5
        layout_if.layout[round(sq.x) + 0][round(sq.y) - 1] = 5
        layout_if.layout[round(sq.x) - 1][round(sq.y) - 1] = 5

    #*********************************************************************************************************************

    async def do_surrender(self):
        if self.surrender:
            await self._client.chat_send('pineapple', team_only=False)
            self.surrender = False

    # *********************************************************************************************************************

    def random_chance(self, amount) -> bool:
        return (random.randrange(0, amount) == 0)

    def maxam_of_thing(self,thing) -> int:
        maxam = 100
        if thing in self.all_structures_tobuildwalk:
            if thing in [ARMORY,FUSIONCORE,ENGINEERINGBAY,GHOSTACADEMY]:
                maxam = 2
            if thing == FACTORY:
                maxam = 3
            if thing == MISSILETURRET:
                maxam = self.all_bases.amount*6
            if thing == BARRACKS:
                maxam = self.all_bases.amount*2
            if thing == STARPORT:
                maxam = self.all_bases.amount
        elif thing in self.all_structures:
            pass
        elif type(thing) == UpgradeId:
            maxam = 1
        else:
#           army
            if thing in [RAVEN,HELLION]:
                maxam = 1
            if thing in [MARAUDER,SIEGETANK,WIDOWMINE,VIKINGFIGHTER]:
                maxam = 10
        return maxam

    def future_maxam_of_thing(self,thing) -> int:
        self.get_all_future_basepos()
        maxam = 100
        if thing in self.all_structures_tobuildwalk:
            if thing in [ARMORY,FUSIONCORE,ENGINEERINGBAY,GHOSTACADEMY]:
                maxam = 2
            if thing == FACTORY:
                maxam = 3
            if thing == MISSILETURRET:
                maxam = len(self.all_future_basepos)*6
            if thing == BARRACKS:
                maxam = len(self.all_future_basepos)*2
            if thing == STARPORT:
                maxam = len(self.all_future_basepos)
        elif thing in self.all_structures:
            pass
        elif type(thing) == UpgradeId:
            maxam = 1
        else:
#           army
            if thing in [RAVEN,HELLION]:
                maxam = 1
            if thing in [MARAUDER,SIEGETANK,WIDOWMINE,VIKINGFIGHTER]:
                maxam = 10
        return maxam

#*********************************************************************************************************************

#   distance
    def sdist(self,p,q):
        return (p.x-q.x)*(p.x-q.x) + (p.y-q.y)*(p.y-q.y)
 
    def circledist(self,p,q):
#       for int points in 200*200
#       tolerate non-int but then less precise
        sd = (p.x-q.x)*(p.x-q.x) + (p.y-q.y)*(p.y-q.y)
        return self.squareroot(round(sd))
 
    def near(self,p,q,supdist) -> bool:
#       works for integers as well as for floats
        return (self.sdist(p,q) < supdist*supdist)

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

    def make_circle(self,n):
#       n points on the unitcircle
        self.circle = []
        for i in range(0,n):
            alfa = 2*pi*i/n
            point = Point2((cos(alfa),sin(alfa)))
            self.circle.append(point)

    def flee(self,posi,dist) -> Point2:
#       get a random point at distance 'dist' from your point 'posi' 
        offset = random.choice(self.flee_circle)
        return Point2((posi.x+offset.x*dist,posi.y+offset.y*dist))


#*********************************************************************************************************************

#   techtree
    def init_structures(self,barra,builddura, size):
        self.routine = 'init_structures'
        self.log_fail((type(barra) == UnitTypeId),'')
        self.all_structures.append(barra)
        self.builddura_of_thing[barra] = builddura
        self.size_of_structure[barra] = size
        if barra not in self.all_pfoc:
            if barra not in self.all_labs:
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

    def compute_all_species_things(self):
        # pairs from cradle are also in techtree
        self.routine = 'compute_all_species_things'
        self.all_species_things = set()
        for pair in self.techtree:
            something = pair[0]
            self.all_species_things.add(something)
            something = pair[1]
            self.all_species_things.add(something)
        for arm in self.all_army:
            self.all_species_things.add(arm)
        for deviation in self.basekind_of_kind:    
            self.all_species_things.add(deviation)
        self.all_species_things.add(MULE)
        self.all_species_things.add(SCV)

    def check_techtree(self,facto) -> bool:
        self.routine = 'check_techtree'
        cando = True
        for pair in self.techtree:
            if pair[0] == facto:
                cando = cando and self.we_finished_a(pair[1])
        return cando

    def check_future_techtree(self,facto) -> bool:
        self.routine = 'check-future_techtree'
        cando = True
        for pair in self.techtree:
            if pair[0] == facto:
                cando = cando and self.we_started_a(pair[1])
        return cando

    def init_bcenemy(self, thing, danger, hate):
        # shoot at most hated
        # flee at dangersum 100
        self.bcenemies.add(thing)
        self.danger_of_bcenemy[thing] = danger
        self.hate_of_bcenemy[thing] = hate

    def init_army(self,thing,dura,supply):
        self.routine = 'init_army'
        self.all_army.append(thing)
        if thing not in [MARINE,HELLION,VIKINGFIGHTER,MEDIVAC,WIDOWMINE]:
            self.all_labarmy.append(thing)
        self.supply_of_army[thing] = supply
        self.builddura_of_thing[thing] = dura

    def init_upgrade(self,thing,time):
        self.routine = 'init_upgrade'
        self.all_upgrades.append(thing)
        self.builddura_of_thing[thing] = time


    def we_finished_a(self,barra) -> bool:
        self.routine = 'we_finished_a'
        have = False
        for (thing,pos) in self.birds:
            have = have or (thing == barra)
        return have

    def we_started_a(self,barra) -> bool:
        self.routine = 'we_started_a'
        have = False
        for (thing,pos) in self.birds:
            have = have or (thing == barra)
        for (bar,marty,pos,dura) in self.eggs:
            have = have or (marty == barra)
        for (bar,marty,pos,dura,owner) in self.preps:
            have = have or (marty == barra)
        for (thing,pos,owner) in self.thoughts:
            have = have or (thing == barra)
        return have

    def we_started_at(self,barra,atpos) -> bool:
        self.routine = 'we_started_at'
        have = False
        for (thing,pos) in self.birds:
            have = have or ((thing == barra) and (pos == atpos))
        for (bar,marty,pos,dura) in self.eggs:
            have = have or ((marty == barra) and (pos == atpos))
        for (bar,marty,pos,dura,owner) in self.preps:
            have = have or ((marty == barra) and (pos == atpos))
        for (thing,pos,owner) in self.thoughts:
            have = have or ((thing == barra) and (pos == atpos))
        return have

    def we_started_amount(self,barra) -> int:
        self.routine = 'we_started_amount'
        have = 0
        for (thing,pos) in self.birds:
            if (thing == barra):
                have += 1
        for (bar,marty,pos,dura) in self.eggs:
            if (marty == barra):
                have += 1
        for (bar,marty,pos,dura,owner) in self.preps:
            if (marty == barra):
                have += 1
        for (thing,pos,owner) in self.thoughts:
            if (thing == barra):
                have += 1
        return have

#*********************************************************************************************************************

    def get_cost(self,building):
        if building == NUKESILONOVA:
            return Cost(100,100)
        else:
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

    def create_block(self, pos,measure):
        for tx in range(0,measure[0]):
            px = round(pos.x + tx - measure[0]/2)
            for ty in range(0,measure[1]):
                py = round(pos.y + ty - measure[1]/2)
                layout_if.layout[px][py] = 1

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
                        info += 1
                    if self.game_info.placement_grid[point] == 0:
                        info += 2
                else:
                    info = 3
                collist.append(info)
            layout_if.layout.append(collist)
        for mim in self.mineral_field:
            here = mim.position
            layout_if.layout[round(here.x-1)][round(here.y-0.5)] = 1
            layout_if.layout[round(here.x+0)][round(here.y-0.5)] = 1
        for gas in self.vespene_geyser:
            self.create_block(gas.position,(3,3))
        for rock in self.destructables:  # copied from Sharpy
            rock_type = rock.type_id
            if rock.name == "MineralField450":
                # Attempts to solve the issue with sc2 linux 4.10 vs Windows 4.11
                self.create_block(rock.position, (2, 1))
            elif rock_type in rocks_if.breakable_rocks_2x2:
                self.create_block(rock.position, (2, 2))
            elif rock_type in rocks_if.breakable_rocks_4x4:
                self.create_block(rock.position, (4, 3))
                self.create_block(rock.position, (3, 4))
            elif rock_type in rocks_if.breakable_rocks_6x6:
                self.create_block(rock.position, (6, 4))
                self.create_block(rock.position, (5, 5))
                self.create_block(rock.position, (4, 6))
            elif rock_type in rocks_if.breakable_rocks_4x2:
                self.create_block(rock.position, (4, 2))
            elif rock_type in rocks_if.breakable_rocks_2x4:
                self.create_block(rock.position, (2, 4))
            elif rock_type in rocks_if.breakable_rocks_6x2:
                self.create_block(rock.position, (6, 2))
            elif rock_type in rocks_if.breakable_rocks_2x6:
                self.create_block(rock.position, (2, 6))
            elif rock_type in rocks_if.breakable_rocks_diag_BLUR:
                for y in range(-4, 6):
                    if y == -4:
                        self.create_block(rock.position + Point2((y + 2, y)), (1, 1))
                    elif y == 5:
                        self.create_block(rock.position + Point2((y - 2, y)), (1, 1))
                    elif y == -3:
                        self.create_block(rock.position + Point2((y - 1, y)), (3, 1))
                    elif y == 4:
                        self.create_block(rock.position + Point2((y + 1, y)), (3, 1))
                    else:
                        self.create_block(rock.position + Point2((y, y)), (5, 1))
            elif rock_type in rocks_if.breakable_rocks_diag_ULBR:
                for y in range(-4, 6):
                    if y == -4:
                        self.create_block(rock.position + Point2((-y - 2, y)), (1, 1))
                    elif y == 5:
                        self.create_block(rock.position + Point2((-y + 2, y)), (1, 1))
                    elif y == -3:
                        self.create_block(rock.position + Point2((-y + 1, y)), (3, 1))
                    elif y == 4:
                        self.create_block(rock.position + Point2((-y - 1, y)), (3, 1))
                    else:
                        self.create_block(rock.position + Point2((-y, y)), (5, 1))

        # *********************************************************************************************************************

    def check_shipyard(self):
        if self.shipyard is None:
            ok = False
        else:
            ok = False
            for base in self.all_bases:
                if self.near(self.shipyard,base.position,10):
                    ok = True
        if not ok:
            oldshipyard = self.shipyard
            goodtow = None
            for base in self.all_bases:
                goodtow = base
            for base in self.structures(PLANETARYFORTRESS) & self.all_bases:
                goodtow = base
            if goodtow is not None:
                self.shipyard = goodtow.position.towards(self.game_info.map_center,5)
                # color the shipyard on the layout, so we will not build there ever
                yardx = round(self.shipyard.x)
                yardy = round(self.shipyard.y)
                for dx in range(-2,3):
                    for dy in range(-2,3):
                        layout_if.layout[yardx+dx][yardy+dy] = 5
                # redirect all ships in repair
                for atag in self.goal_of_unittag:
                    goal = self.goal_of_unittag[atag]
                    if goal == oldshipyard:
                        self.goal_of_unittag[atag] = self.shipyard

    #*********************************************************************************************************************

#   fix secondary information
#   call just before using count_of_job when precize numbers are important
    def fix_count_of_job(self):
        self.routine = 'fix_count_of_job'
#       count_of_job
        for j in (self.good_jobs + self.bad_jobs + self.no_jobs):
            self.count_of_job[j] = 0
        for scvt in self.job_of_scvt:
            j = self.job_of_scvt[scvt]
            self.count_of_job[j] += 1

    def fix_count_of_mimt(self):
        self.routine = 'fix_count_of_mimt'
#       calculate the amount of gatherers on each mineral, using mimt_of_scvt
        self.count_of_mimt = {}
        for mimt in self.all_mimt:
            self.count_of_mimt[mimt] = 0
        for scvt in self.mimt_of_scvt:
            mimt = self.mimt_of_scvt[scvt]
            if mimt in self.all_mimt:
                self.count_of_mimt[mimt] += 1

    def fix_count_of_gast(self):
        self.routine = 'fix_count_of_gast'
#       calculate the amount of gatherers on each gas, using gast_of_scvt
        self.count_of_gast = {}
        for gast in self.all_gast:
            self.count_of_gast[gast] = 0
        for scvt in self.gast_of_scvt:
            gast = self.gast_of_scvt[scvt]
            if gast in self.all_gast:
                self.count_of_gast[gast] += 1
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


    def get_hometop(self):
        # temporary draw the wall (armory to prevent add-on)
        self.write_layout(SUPPLYDEPOT,self.wall_depot0_pos)
        self.write_layout(SUPPLYDEPOT,self.wall_depot1_pos)
        self.write_layout(ARMORY,self.wall_barracks_pos)
        # get an empty square
        square = (round(self.start_location.position.x-0.5),round(self.start_location.position.y-0.5))
        while self.read_layout(square[0],square[1]) != 0:
            square = (square[0]+1,square[1])
        # expand that to the hometop
        self.hometop = {square}
        edge = {square}
        while (len(edge) > 0):
            newedge = set()
            for square in edge:
                self.get_neighbours(square)
                for nsquare in self.neighbours:
                    if nsquare not in self.hometop:
                        if self.read_layout(nsquare[0],nsquare[1]) == 0:
                            newedge.add(nsquare)
            self.hometop |= newedge
            edge = newedge.copy()
        # undraw the wall
        self.erase_layout(SUPPLYDEPOT,self.wall_depot0_pos)
        self.erase_layout(SUPPLYDEPOT,self.wall_depot1_pos)
        self.erase_layout(ARMORY,self.wall_barracks_pos)


    def get_enemytop(self):
        # get an empty square
        square = (round(self.enemyloc.x-0.5),round(self.enemyloc.y-0.5))
        while self.read_layout(square[0],square[1]) != 0:
            square = (square[0]+1,square[1])
        # expand that to the enemytop
        self.enemytop = {square}
        edge = {square}
        while (len(edge) > 0):
            newedge = set()
            for square in edge:
                self.get_neighbours(square)
                for nsquare in self.neighbours:
                    if nsquare not in self.enemytop:
                        if self.read_layout(nsquare[0],nsquare[1]) == 0:
                            newedge.add(nsquare)
            self.enemytop |= newedge
            edge = newedge.copy()


    def belongs_to(self, towpos: Point2, point: Point2) -> bool:
        sd = self.sdist(towpos, point)
        doubt = True
        if sd > 25*25:
            doubt = False
            bans = False
        elif sd < 15*15:
            doubt = False
            bans = True
        if doubt:
            if (towpos == self.start_location.position) and (len(self.hometop) > 0):
                square = (round(point.x-0.5),round(point.y-0.5))
                bans = (square in self.hometop)
            elif (towpos == self.enemyloc) and (len(self.enemytop) > 0):
                square = (round(point.x - 0.5), round(point.y - 0.5))
                bans = (square in self.enemytop)
            else:
                bans = (sd < 18*18)
        return bans

    # END OF some routines with t=(t[0],t[1]) notation

    #   get nearest
    def get_near_scvt_to_goodjob(self,point) -> int:
        self.routine = 'get_near_scvt_to_goodjob'
        stuck = set() # scvt for scvs with too little movespace
        reachset = set() # reachable squares for the best scv
        hope = True
        scvt = self.notag
        while (len(reachset) < 10) and hope:
            hope = False
            best_sdist = 99999
            best_scvt = self.notag
            for scv in self.units(SCV):
                scvt = scv.tag
                if (scvt in self.all_scvt) and (scvt not in stuck):
                    if self.job_of_scvt[scvt] in (self.bad_jobs + self.no_jobs):
                        hope = True
                        sd = self.sdist(scv.position,point)
    #                   accept idler if 1.7 times as far
                        if self.job_of_scvt[scvt] in self.no_jobs:
                            sd /= 3
    #                   accept mimminer if 1.4 times as far
                        if self.job_of_scvt[scvt] in ['applicant','mimminer']:
                            sd /= 2
                        if sd < best_sdist:
                            best_sdist = sd
                            best_scvt = scvt
            scvt = best_scvt
            for scv in self.units(SCV):
                if scv.tag == scvt:
                    # check whether it is stuck
                    scvhome = (round(scv.position.x-0.5),round(scv.position.y-0.5))
                    smallset = set()
                    reachset = {scvhome}
                    while (len(smallset) < len(reachset)) and (len(reachset)<10):
                        smallset = reachset.copy()
                        for square in smallset:
                            self.get_neighbours(square)
                            for nsquare in self.neighbours:
                                if self.read_layout(nsquare[0],nsquare[1]) in [0,2]:
                                    reachset.add(nsquare)
                    if len(reachset) < 10:
                        stuck.add(scvt)
        if not hope:
            self.surrender = True
            self.log_success('no scv left for the good job')
        return scvt

    def get_near_scvt_nojob(self,point) -> int:
        self.routine = 'get_near_scvt_nojob'
        # suggestion: call    if self.count_of_job['idler'] > 0;
        best_sdist = 99999
        best_scvt = self.notag
        for scv in self.units(SCV):
            scvt = scv.tag
            if scvt in self.all_scvt:
                if self.job_of_scvt[scvt] in self.no_jobs:
                    sd = self.sdist(scv.position,point)
                    if sd < best_sdist:
                        best_sdist = sd
                        best_scvt = scvt
        scvt = best_scvt
        self.log_fail((best_sdist < 99999),'no idler found.')
        return scvt        

    def get_near_scvt_nojob_or_applicant(self,point) -> int:
        self.routine = 'get_near_scvt_nojob_or_applicant'
        # suggestion: call    if self.count_of_job['idler'] > 0;
        best_sdist = 99999
        best_scvt = self.notag
        for scv in self.units(SCV):
            scvt = scv.tag
            if scvt in self.all_scvt:
                job = self.job_of_scvt[scvt]
                if (job in self.no_jobs) or (job == 'applicant'):
                    sd = self.sdist(scv.position,point)
                    if sd < best_sdist:
                        best_sdist = sd
                        best_scvt = scvt
        scvt = best_scvt
        self.log_fail((best_sdist < 99999),'no idler or applicant found.')
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

    def get_near_pole(self,point) -> int:
        self.routine = 'get_near_pole'
        bestsd = 99999
        for nr in range(0, len(self.scout_pos)):
            honk = self.scout_pos[nr]
            sd = self.sdist(point, honk)
            if sd < bestsd:
                bestsd = sd
                bestnr = nr
        return bestnr


    def init_basekind(self, derived,normal):
        self.basekind_of_kind[derived] = normal

    def basekind_of(self, kind):
        basekind = kind
        if kind in self.basekind_of_kind:
            basekind = self.basekind_of_kind[kind]
        return basekind


    async def get_birds(self):
        # overview of all own (living, existing) things
        # basekind e.g. SUPPLYDEPOT for SUPPLYDEPOTLOWERED
        # for labs, the mamaposition
        # for flying buildings: the landed buildingname, the actual pos
        # for nukes in silo: NUKESILONOVA
        self.birds = set()
        for kind in self.all_structures_tobuildwalk:
            for stru in self.structures(kind).ready:
                basekind = self.basekind_of(kind)
                pos = stru.position
                self.birds.add((basekind,pos))
        for kind in self.landable:
            for stru in self.structures(kind).ready:
                basekind = self.basekind_of(kind)
                pos = stru.position
                self.birds.add((basekind, pos))
        for kind in self.all_labs:
            for stru in self.structures(kind).ready:
                labpos = stru.position
                pos = Point2((labpos.x - 2.5, labpos.y + 0.5))
                self.birds.add((kind, pos))
        for kind in self.all_pfoc:
            for stru in self.structures(kind).ready:
                pos = stru.position
                self.birds.add((kind, pos))
        for upgr in self.state.upgrades:
                self.birds.add((upgr,self.nowhere))
        for kind in self.all_army:
            basekind = self.basekind_of(kind)
            for unt in self.units(kind):
                pos = unt.position
                self.birds.add((basekind,pos))
        # lowerbound SCV, misses some in gas or bunker.
        for unt in self.units(SCV):
            pos = unt.position
            self.birds.add((SCV,pos))
        # lowerbound for the amount of nukes-in-silo, misses if academy is upgrading
        for ga in self.structures(GHOSTACADEMY).ready.idle:
            if self.can_pay(NUKESILONOVA):
                if self.we_started_a(FACTORY):
                    if AbilityId.BUILD_NUKE not in await self.get_available_abilities(ga):
                        self.birds.add((NUKESILONOVA,ga.position))
        self.log_birds()


    def get_eggs(self):
        # overview of things currently being made
        self.eggs = set()
        for scv in self.units(SCV):
            scvt = scv.tag
            if scvt in self.goal_of_trabu_scvt:
                if self.job_of_scvt[scvt] == 'builder':
                    goal = self.goal_of_trabu_scvt[scvt]
                    thing = self.structure_of_trabu_scvt[scvt]
                    pos = scv.position
                    build_dura = self.builddura_of_thing[thing]
                    restdura = build_dura
                    for thatone in self.structures: # do not mention thing, for refineryrich and supplydepotlowered
                        if thatone.position == goal:
                            restdura = build_dura*(1.0-thatone.build_progress)
                    if restdura > 0:
                        self.eggs.add((scv,thing,goal,restdura))
        for pair in self.cradle:
            martype = pair[0]
            dura = self.builddura_of_thing[martype]
            bartype = pair[1]
            if martype in self.all_upgrades:
                abi = sc2.dicts.unit_research_abilities.RESEARCH_INFO[bartype][martype]['ability']
            elif martype in self.all_labs:
                abi = AbilityId.BUILD_TECHLAB
            elif martype == NUKESILONOVA:
                abi = AbilityId.BUILD_NUKE
            else:
                abi = sc2.dicts.unit_train_build_abilities.TRAIN_INFO[bartype][martype]['ability']
            for bar in self.structures(bartype).ready:
                if bar.is_using_ability(abi):
                    progress = bar.orders[0].progress
                    restdura = dura * (1.0 - progress)
                    pos = bar.position
                    self.eggs.add((bar,martype,pos,restdura))
        martype = SCV
        abi = AbilityId.COMMANDCENTERTRAIN_SCV
        for bartype in [COMMANDCENTER,ORBITALCOMMAND,PLANETARYFORTRESS]:
            for bar in self.structures(bartype).ready:
                if bar.is_using_ability(abi):
                    dura = self.builddura_of_thing[martype]
                    progress = bar.orders[0].progress
                    restdura = dura * (1.0 - progress)
                    pos = bar.position
                    self.eggs.add((bar, martype, pos, restdura))
        self.log_eggs()

    def get_preps(self):
        # overview of things currently being made
        self.preps = set()
        for scv in self.units(SCV):
            scvt = scv.tag
            if scvt in self.goal_of_trabu_scvt:
                if self.job_of_scvt[scvt] == 'traveller':
                    goal = self.goal_of_trabu_scvt[scvt]
                    thing = self.structure_of_trabu_scvt[scvt]
                    owner = self.owner_of_trabu_scvt[scvt]
                    pos = scv.position
                    restdura = self.walk_duration(pos,goal)
                    self.preps.add((scv, thing, goal, restdura, owner))
        for strt in self.ambition_of_strt:
            martype = self.ambition_of_strt[strt]
            owner = self.owner_of_ambistrt[strt]
            dura = 1
            for abar in self.structures:
                if abar.tag == strt:
                    bar = abar
                    pos = abar.position
            for (abar,dum1,dum2,itsrestdura) in self.eggs: # calc eggs first
                if abar.tag == strt:
                    dura = itsrestdura
            self.preps.add((bar, martype, pos, dura, owner))
        self.log_preps()

# *********************************************************************************************************************
#  bagofthings, bagoftree, bagofcradle, buildseries

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
        if building not in self.all_structures_tobuildwalk:
            self.log_success('BUG 26006 '+building.name)
        found = False
        # use special places
        todel = -1
        for nr in range(0,len(self.specialplaces)):
            (bu,pl) = self.specialplaces[nr]
            if (bu == building) and (not found):
                place = pl
                found = True
                todel = nr
        if todel >= 0:
            del self.specialplaces[todel]
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
                            tipsfound += 1
                            if self.random_chance(tipsfound):
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
        # try recycling
        if not found:
            for (th,pl) in self.recycling:
                if (th == building) and (not found):
                    found = True
                    place = pl
            if found:
                del self.recycling[self.recycling.index((building,place))]
                self.log_placing('using recycling')
        # find a new place directly
        if (building == COMMANDCENTER) and (not found):
            tried = 0
            found = False
            while (not found) and (tried < 20):
                place = random.choice(self.expansion_locations_list)
                found = True
                found = found and (self.check_layout(building, place))
                if len(self.all_bases) < 6:
                    found = found and (not self.near(place, self.enemyloc, 50))
                found = found and (place not in [tow.position for tow in self.all_future_basepos])
                tried += 1
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
                cc = random.choice(self.all_bases)
                dist = 6
                if building == MISSILETURRET:
                    dist = random.randrange(-10, 10)
                fixplace = cc.position.towards(self.game_info.map_center, dist)
                self.put_on_the_grid(building, fixplace)
                fixplace = self.function_result_Point2
                tries = 0
                radius = 0
                ok = False
                while (not ok):
                    if tries == radius*radius:
                        radius += 1
                    tries += 1
                    x = fixplace.x + random.randrange(-radius, radius)
                    y = fixplace.y + random.randrange(-radius, radius)
                    place = Point2((x, y))
                    ok = self.check_layout(building, place)
                found = True
            else:
                fixplace = self.start_location.position
                self.put_on_the_grid(building, fixplace)
                fixplace = self.function_result_Point2
                tries = 0
                radius = 0
                ok = False
                while (not ok):
                    if tries == radius*radius:
                        radius += 1
                    tries += 1
                    x = fixplace.x + random.randrange(-radius, radius)
                    y = fixplace.y + random.randrange(-radius, radius)
                    place = Point2((x, y))
                    ok = self.check_layout(building, place)
                found = True
        #
        if found:
            self.function_result_Point2 = place
        else:
            self.log_placing('not found')
        return found

    def bagoftree_of_bagofthings(self):
        self.routine = 'bagoftree_of_bagofthings'
        # add techtree parents
        stri = 'bagofthings: '
        for th in self.bagofthings:
            stri = stri + th.name + ' '
        self.log_success(stri)
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


    def bagofcradle_of_bagoftree(self):
        self.routine = 'bagofcradle_of_bagoftree'
        # Add cradle parents. Flying is not good enough.
        bag = self.bagoftree.copy()
        stable = False
        while not stable:
            stable = True
            extra = set()
            for th in bag:
                for pair in self.cradle:
                    if pair[0] == th:
                        barra = pair[1]
                        haveit = (barra in bag)
                        for (bar, marty, pos, dura) in self.eggs:
                            haveit = haveit or (marty == barra)
                        for (bar, marty, pos, dura, owner) in self.preps:
                            haveit = haveit or (marty == barra)
                        for (thing, pos, owner) in self.thoughts:
                            haveit = haveit or (thing == barra)
                        if barra in self.all_structures:
                            haveit = haveit or (len(self.structures(barra)) > 0)
                        else:
                            haveit = haveit or (len(self.units(barra)) > 0)
                        if not haveit:
                            extra.add(barra)
                            stable = False
            for th in extra:
                bag.append(th)
        self.bagofcradle = bag
        # now check the amounts for the transformables
        self.hoopy_get_sit()
        for thing in self.bagofcradle:
            self.hoopy_add(thing)
        for thing in [BARRACKS,FACTORY,STARPORT,COMMANDCENTER]:
            if self.transformable[thing] < 0:
                for am in range(0,-self.transformable[thing]):
                    self.bagofcradle.append(thing)
        # show
        stri = 'bagofcradle: '
        for th in self.bagofcradle:
            stri = stri + th.name + ' '
        self.log_success(stri)


    def buildseries_of_bagofcradle(self):
        self.routine = 'buildseries_of_bagofcradle'
        # sort until executable
        self.hoopy_get_sit()
        toput = self.bagofcradle.copy()
        series = []
        while len(toput) > 0:
            # There is always one in toput that you can do. Get one
            cando = None
            for th in toput:
                if self.hoopy_can_add(th):
                    cando = th
            # Then do it.
            if cando is None:
                for th in toput:
                    self.log_success('BUG cannot put all; not '+th.name)
            self.hoopy_add(cando)
            series.append(cando)
            del toput[toput.index(cando)]
        self.buildseries = series
        stri = 'buildseries: '
        for th in self.buildseries:
            stri = stri + th.name + ' '
        self.log_success(stri)


    def crad_places_for_thing(self, thing):
        # thing is labs, pfoc, upgr, or army. It has a unique cradle.
        crad = None
        for pair in self.cradle:
            if pair[0] == thing:
                crad = pair[1]
        # needslab ?/n/y
        needslab = '?'
        if thing in self.all_labs + self.all_pfoc:
            needslab = 'n'
        for pair in self.techtree:
            if pair[0] == thing:
                if pair[1] in self.all_labs:
                    needslab = 'y'
        # Everything has a cradle
        # crad could exist, or be ordered, or be in the buildorder
        self.crad_places = set()
        for stru in self.structures(crad).ready:
            pos = stru.position
            if pos in self.bui_min_lab:
                if (self.bui_min_lab[pos] == 1) and (needslab != 'y'):
                    self.crad_places.add(pos)
                if (self.bui_min_lab[pos] == 0) and (needslab != 'n'):
                    self.crad_places.add(pos)
            elif needslab == '?':
                self.crad_places.add(pos)
        for scvt in self.goal_of_trabu_scvt:
            if self.structure_of_trabu_scvt[scvt] == crad:
                pos = self.goal_of_trabu_scvt[scvt]
                if pos in self.bui_min_lab:
                    if (self.bui_min_lab[pos] == 1) and (needslab != 'y'):
                        self.crad_places.add(pos)
                    if (self.bui_min_lab[pos] == 0) and (needslab != 'n'):
                        self.crad_places.add(pos)
                elif needslab == '?':
                    self.crad_places.add(pos)
        for (otherthing, pos) in self.buildorder:
            if otherthing == crad:
                if pos in self.bui_min_lab:
                    if (self.bui_min_lab[pos] == 1) and (needslab != 'y'):
                        self.crad_places.add(pos)
                    if (self.bui_min_lab[pos] == 0) and (needslab != 'n'):
                        self.crad_places.add(pos)
                elif needslab == '?':
                    self.crad_places.add(pos)


    def buildorder_of_buildseries(self):
        # buildorder = buildseries + place
        # also: change infested to normal
        self.routine = 'buildorder_of_buildseries'
        self.buildorder = []
        self.happy_get_sit()
        for infathing in self.buildseries:
            thing = self.basekind_of(infathing)
            goal = self.nowhere
            if thing in self.all_structures_tobuildwalk:
                if goal == self.nowhere:
                    if self.find_tobuildwalk_a_place(infathing):
                        goal = self.function_result_Point2
                if goal == self.nowhere:
                    self.log_success('skipping a '+infathing.name+' because I found no position!')
                else:
                    self.buildorder.append((thing, goal))
                    self.write_layout(thing, goal)
                    self.happy_add(thing,goal)
            else: # army, labs, upgr, pfoc
                self.crad_places_for_thing(thing)
                # get a random cradle place
                if len(self.crad_places)==0:
                    self.log_success('Can not place '+thing.name)
                    place = self.nowhere
                else: # len==1 is not sure after a random
                    self.buildorder.append((thing, self.somewhere))
                    place = random.choice(tuple(self.crad_places))
                    self.happy_add(thing,place)


    # *********************************************************************************************************************
    # buildseries timing optimizing

    def check_buildseries(self) -> bool:
        self.routine = 'check_buildseries'
        # check if a buildseries is possible according to techtree
        is_pos = True
        front = set()
        for thing in self.buildseries:
            if is_pos:
                trans_thing = self.basekind_of(thing)
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


    def add_sit(self,thing, moment):
        self.routine = 'add_sit'
        self.sit_free.append((thing,moment))
        if thing in self.sit_exist:
            self.sit_exist[thing] = min(self.sit_exist[thing],moment)
        else:
            self.sit_exist[thing] = moment


    def get_sit(self):
        self.routine = 'get_sit'
        # sit_free      list of (thing,moment); freemoment with now=0. Uninfested.
        # sit_exist     dict of [thing] -> moment; readymoment with now=0. Uninfested.
        self.sit_free = []
        self.sit_exist = {}
        #
        for (thing,pos) in self.birds:
            self.add_sit(thing,0)
        for (bar,marty,pos,dura) in self.eggs:
            self.add_sit(marty,dura)
        for (bar,marty,pos,dura,owner) in self.preps:
            dura = dura + self.builddura_of_thing[marty]
            self.add_sit(marty,dura)
        # for thoughts, we have but a rough estimate
        maxdura = 0
        for (thing,dura) in self.sit_free:
            maxdura = max(maxdura,dura)
        for (thing,pos,owner) in self.thoughts:
            dura = maxdura + self.builddura_of_thing[thing]
            self.add_sit(thing,dura)
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



    def deficit_buildseries(self) -> int:
        self.routine = 'deficit_buildseries'
        # check_buildseries == True
        # duration according to techtree and cradle
        # buildstarts are 5 seconds apart just to get some ordering.
        # deficit is the sum over army-units of startbuildtime*power
        #        and the sum over ccs,refineries etc of starttime*half*power
        #        topped with a tank
        current_freethings = self.sit_free.copy() # list of (thing,moment); freemoment with now=0
        current_exist = self.sit_exist.copy() # dict of [thing] -> moment; readymoment with now=0
        current_moment = 0
        end_moment = 0
        deficit = 0
        for infa_thing in self.buildseries:
            thing = self.basekind_of(infa_thing)
            start_moment = current_moment
            # wait for tech
            for pair in self.techtree:
                if pair[0] == thing:
                    neededthing = pair[1]
                    first_moment = current_exist[neededthing]
                    start_moment = max(start_moment,first_moment)
            # maybe wait for cradle
            for pair in self.cradle:
                if pair[0] == thing:
                    cradle = pair[1]
                    first_moment = 9999
                    for (thcr,mo) in current_freethings:
                        if thcr == cradle:
                            if mo < first_moment:
                                chosen = (thcr,mo)
                                first_moment = mo
                    # remove 1 chosen from current_freethings
                    del current_freethings[current_freethings.index(chosen)]
                    start_moment = max(start_moment,first_moment)
                    end_moment = start_moment + self.builddura_of_thing[thing]
                    current_freethings.append((cradle,end_moment))
            # start_moment is calculated
            if thing in self.all_army:
                deficit += start_moment * self.unit_power(thing)
            if thing in [REFINERY,COMMANDCENTER,ORBITALCOMMAND,PLANETARYFORTRESS,MISSILETURRET,BUNKER]:
                deficit += start_moment * 0.5 * self.unit_power(thing)
            current_moment = start_moment + 5  # to keep the order of the series
            end_moment = start_moment + self.builddura_of_thing[thing]
            current_freethings.append((thing,end_moment))
            if thing not in current_exist:
                current_exist[thing] = end_moment
        deficit += end_moment * self.unit_power(SIEGETANK)
        return deficit


    def optimize_buildseries(self):
        self.routine = 'optimize_buildseries'
        self.get_sit()
        best_buildseries = self.buildseries.copy()
        if not self.check_buildseries():
            self.log_success('flying cat')
        best_deficit = self.deficit_buildseries()
        self.log_buildseries('Before: ' + str(best_deficit) + ': ')
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
                    deficit = self.deficit_buildseries()
                    self.log_buildseries('trying: ' + str(deficit) + ': ')
                    if deficit < best_deficit:
                        improved = True
                        best_buildseries = self.buildseries.copy()
                        best_deficit = deficit
        self.buildseries = best_buildseries.copy()
        self.log_buildseries('After: ' + str(best_deficit) + ': ')




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
#       buildorder [(BARRACKS,(16,40)),(SUPPLYDEPOT,(119,3)),(MARINE,somewhere),...
#   OUT:
#       planning [(tagJohn,BARRACKS,(16,40),4,17,22)
#                ,(tagMohamad,SUPPLYDEPOT,(119,3),8,23,30)
#                ,(notag,MARINE,(16,40),220,220,265),...
#       The 3 moments are: start-walk, start-construct,end-construct
#   LOCAL:
#       current_moment 17
#       current_spendable_minerals 254
#       current_spendable_vespene 0
#       current_freescvs {(tagjohn,pos(14,107),since15),...
#           using buildplan (tagjohn,thingBARRACKS,goal(16,40),startwalk14,startconstruct17,finish19)
#       current_walking {buildplan,...
#       current_constructing {buildplan,...
#           using trainplan (thingMARINE,place(16,40),startgym12,starttrain20,finish40)
#       current_ambition {trainplan, ...
#       current_growing {trainplan, ...
#       current_gym {trainplan, ...
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
        self.situation_spendable_minerals = self.minerals
        self.situation_spendable_vespene = self.vespene
        self.situation_walking = set()
        self.situation_constructing = set()
        self.situation_ambition = set()
        self.situation_growing = set()
        self.situation_gym = set()
        self.situation_training = set()
        self.situation_thingkinds = set()
        self.fix_count_of_job()
        self.situation_mimminers = self.count_of_job['mimminer'] + 3*len(self.structures(ORBITALCOMMAND))
        self.situation_gasminers = self.count_of_job['gasminer']
        # for the techtree:
        for (thing,pos) in self.birds:
            self.situation_thingkinds.add(thing)
        # walk
        for (scv,thing,pos,dura) in self.eggs:
            if scv.tag in self.all_scvt:
                buildplan = (scv.tag, thing, pos, -1, -1, dura)
                self.situation_constructing.add(buildplan)
        for (scv,thing,pos,dura,owner) in self.preps:
            if scv.tag in self.all_scvt:
                finishmoment = dura + self.builddura_of_thing[thing]
                buildplan = (scv.tag,thing,pos,-1,dura,finishmoment)
                self.situation_walking.add(buildplan)
        # labs, pfoc
        for (bar,thing,pos,dura) in self.eggs:
            if thing in self.all_labs + self.all_pfoc:
                scvt = self.notag
                trainplan = (thing, pos, -1, -1, dura)
                self.situation_growing.add(trainplan)
        for (bar,thing,pos,dura,owner) in self.preps:
            if thing in self.all_labs + self.all_pfoc:
                scvt = self.notag
                finishmoment = dura + self.builddura_of_thing[thing]
                trainplan = (thing, pos, -1, dura, finishmoment)
                self.situation_ambition.add(trainplan)
        # army, upgr
        for thing in self.all_army + self.all_upgrades:
            for (bar, martype, pos, dura) in self.eggs:
                if martype == thing:
                    trainplan = (thing, pos, -1, -1, dura)
                    self.situation_training.add(trainplan)
            for (bar,martype,pos,dura,owner) in self.preps:
                if martype == thing:
                    finishmoment = dura + self.builddura_of_thing[thing]
                    trainplan = (thing, pos, -1, dura, finishmoment)
                    self.situation_gym.add(trainplan)
        #
        # situation_events
        self.situation_events = set()
        for (upgr, goal, mi, startgrowmoment, finishmoment) in self.situation_gym:
            self.situation_events.add((startgrowmoment, 'start training', self.notag, goal))
            self.situation_events.add((finishmoment, 'finish training', self.notag, goal))
        for (upgr, goal, mi, minusone, finishmoment) in self.situation_training:
            self.situation_events.add((finishmoment, 'finish training', self.notag, goal))
        for (thing, goal, mi, startgrowmoment, finishmoment) in self.situation_ambition:
            self.situation_events.add((startgrowmoment, 'start growing', self.notag, goal))
            self.situation_events.add((finishmoment, 'finish growing', self.notag, goal))
        for (thing, goal, mi, minusone, finishmoment) in self.situation_growing:
            self.situation_events.add((finishmoment, 'finish growing', self.notag, goal))
        for (scvt, thing, goal, mi, constructmoment, finishmoment) in self.situation_walking:
            self.situation_events.add((constructmoment, 'start constructing', scvt, goal))
            self.situation_events.add((finishmoment, 'finish constructing', scvt, goal))
        for (scvt,thing,goal,mi,minusone,finishmoment) in self.situation_constructing:
            self.situation_events.add((finishmoment, 'finish constructing', scvt, goal))
        # potential builders
        self.situation_freescvs = set()
        for scv in self.units(SCV):
            scvt = scv.tag
            if scvt in self.all_scvt:
                if self.job_of_scvt[scvt] in (self.bad_jobs + self.no_jobs):
                    self.situation_freescvs.add((scvt,scv.position,0))
        # As the planning is remade often, builders should be included. They will appear at the buildposition.
        for (scv,thing,pos,dura,owner) in self.preps:
            scvt = scv.tag
            if scvt in self.all_scvt:
                dura += self.builddura_of_thing[thing]
                self.situation_freescvs.add((scvt, pos, dura))
        for (scv,thing,pos,dura) in self.eggs:
            scvt = scv.tag
            if scvt in self.all_scvt:
                self.situation_freescvs.add((scvt, pos, dura))
        # to make marines:
        # include unfinish buildings    to prevent a short disappearance
        # buildings are identified by place not tag, so we can add future buildings
        self.situation_buildings_and_parts = set()
        for (thing,pos) in self.birds:
            if thing in self.all_structures:
                self.situation_buildings_and_parts.add((thing, pos.x, pos.y))
        for (scv,thing,pos,dura) in self.eggs:
            if thing in self.all_structures:
                self.situation_buildings_and_parts.add((thing, pos.x, pos.y))


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
        current_gym = self.situation_gym.copy()
        current_training = self.situation_training.copy()
        current_ambition = self.situation_ambition.copy()
        current_growing = self.situation_growing.copy()
        current_thingkinds = self.situation_thingkinds.copy()
        current_buildings_and_parts = self.situation_buildings_and_parts.copy()
        current_events = self.situation_events.copy()
        current_mimminers = self.situation_mimminers+extraminerals
        current_gasminers = self.situation_gasminers+extragas
        current_freescvs = self.situation_freescvs.copy()
        current_moment = 0
#
        plannable = True
        for (beautiful_thing,beautiful_place) in self.buildorder:
            if plannable:
                # MAKE A BEAUTIFUL_BUILDPLAN, PLAN_MOMENT AND EVENTS, AND APPEND BP TO PLANNING
                started = False
                for buildplan in current_walking:
                    (scvt, th, pos, sr, sc, fi) = buildplan
                    if (th == beautiful_thing):
                        if (pos == beautiful_place) or (beautiful_place == self.somewhere):
                            if buildplan not in self.planning:
                                beautiful_buildplan = buildplan
                                started = True
                                self.planning.append(beautiful_buildplan)
                                plan_moment = sc
                for trainplan in current_ambition | current_gym:
                    (th, pos, sr, sc, fi) = trainplan
                    if (th == beautiful_thing):
                        if (pos == beautiful_place) or (beautiful_place == self.somewhere):
                            buildplan = (self.notag, th, pos, sr, sc, fi)
                            if buildplan not in self.planning:
                                beautiful_buildplan = buildplan
                                started = True
                                self.planning.append(beautiful_buildplan)
                                plan_moment = sc
                if (not started):
                    # choose a specific cradle if the choice was delayed
                    if (beautiful_place == self.somewhere):
                        # beautiful_thing is labs, pfoc, upgr, or army. It has a unique cradle.
                        cradle = None
                        for pair in self.cradle:
                            if pair[0] == beautiful_thing:
                                cradle = pair[1]
                        # needslab ?/n/y
                        needslab = '?'
                        if beautiful_thing in self.all_labs + self.all_pfoc:
                            needslab = 'n'
                        for pair in self.techtree:
                            if pair[0] == beautiful_thing:
                                if pair[1] in self.all_labs:
                                    needslab = 'y'
                        cradles = set()
                        for (thing,x,y) in current_buildings_and_parts:
                            if thing == cradle:
                                # cradle: walk,labs
                                cradle_place = Point2((x, y))
                                # cradle can be unfinished, or in use
                                maxfinish = current_moment
                                for (scvt, thi, goal, startwalk, startconstruct, finish) in current_constructing:
                                    if (goal == cradle_place):
                                        maxfinish = max(finish,maxfinish)
                                for (thi, goal, sg, start, finish) in current_growing | current_training:
                                    if (goal == cradle_place):
                                        maxfinish = max(finish,maxfinish)
                                cradle_dura = maxfinish - current_moment
                                haslab = 'n'
                                for (otherthing, otherx, othery) in current_buildings_and_parts:
                                    if (otherthing != thing) and (otherx == x) and (othery == y):
                                        haslab = 'y'
                                if (needslab == '?') or (needslab == haslab):
                                    cradles.add((cradle_place,cradle_dura))
                        # check
                        if len(cradles) == 0:
                            self.log_success('Strange, I have nowhere to build a '+beautiful_thing.name)
                            for (th,x,y) in current_buildings_and_parts:
                                self.log_success('I have a '+th.name)
                        # get earliest
                        bestdura = 99999
                        bestplace = self.nowhere
                        for (place,dura) in cradles:
                            if dura < bestdura:
                                bestdura = dura
                                bestplace = place
                        beautiful_place = bestplace
                    # calculate times
                    if (extragas == 0) and (extraminerals == 0):
                        self.log_planning('Planning a '+beautiful_thing.name)
                    cost = self.get_cost(beautiful_thing)
                    build_dura = self.builddura_of_thing[beautiful_thing]
                    total_dura = 0
                    # mim_dura
                    mim_gap = cost.minerals - current_spendable_minerals
                    if (mim_gap <= 0):
                        mim_dura = 0
                    elif current_mimminers == 0:
                        mim_dura = 99999
                    else:
                        mim_dura = mim_gap / (current_mimminers*self.mim_speed)
                    total_dura = max(total_dura,mim_dura)
                    # gas_dura
                    gas_gap = cost.vespene - current_spendable_vespene
                    if (gas_gap <= 0) or (cost.vespene == 0):
                        gas_dura = 0
                    elif current_gasminers == 0:
                        gas_dura = 99999
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
                                earliest = 99999
                                for (scvt,thing,goal,startwalk,startconstruct,finish) in current_constructing | current_walking:
                                    if thing == barra:
                                        if finish < earliest:
                                            earliest = finish
                                for (thing,goal,startambition,startgrow,finish) in current_ambition | current_growing | current_gym | current_training:
                                    if thing == barra:
                                        if finish < earliest:
                                            earliest = finish
                                dura = earliest - current_moment
                                tree_dura = max(tree_dura,dura)
                    total_dura = max(total_dura,tree_dura)
                    # walk_dura
                    if beautiful_thing in self.all_structures_tobuildwalk:
                        # find a beautiful scv
                        beautiful_scvt = self.notag
                        arrive_quality = 99999
                        for (scvt,pos,since) in current_freescvs:
                            walk_dura = self.walk_duration(pos,beautiful_place)
                            could_arrive = max(current_moment,(since + walk_dura))
                            # next constants weigh reusing an scv that has to walk a little versus getting a fresh scv from far
                            if self.job_of_scvt[scvt] == 'gasminer':
                                could_arrive_quality = could_arrive + 0.25*walk_dura
                            else:
                                could_arrive_quality = could_arrive + 0.2*walk_dura
                            if could_arrive_quality < arrive_quality:
                                arrive_quality = could_arrive_quality
                                beautiful_scvt = scvt
                        travel_dura = 99999
                        for (scvt,pos,since) in current_freescvs:
                            if scvt == beautiful_scvt:
                                walk_dura = self.walk_duration(pos, beautiful_place)
                                could_arrive = max(current_moment, (since + walk_dura))
                                travel_dura = could_arrive - current_moment
                    else:
                        beautiful_scvt = self.notag
                        travel_dura = 0
                        walk_dura = 0
                    total_dura = max(total_dura,travel_dura)
                    # cradle_dura: how long to wait for the cradle to become idle
                    cradle_dura = 0
                    for pair in self.cradle:
                        if pair[0] == beautiful_thing:
                            cradle = pair[1]
                            cradle_dura = 99999
                            maxfinish = current_moment
                            # Cradle could be unfinished. Or it could be busy e.g. growing something
                            for (scvt, thi, goal, startwalk, startconstruct, finish) in current_constructing:
                                if (goal == beautiful_place):
                                    maxfinish = max(finish,maxfinish)
                            for (thi,goal,sg,start,finish) in current_training | current_growing:
                                if (goal == beautiful_place):
                                    maxfinish = max(finish,maxfinish)
                            cradle_dura = maxfinish - current_moment
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
                            beautiful_buildplan = (beautiful_scvt,beautiful_thing,beautiful_place,plan_moment - walk_dura,plan_moment,
                                                   plan_moment + build_dura)
                            current_events.add((plan_moment - walk_dura,'start walking',beautiful_scvt,beautiful_place))
                            current_events.add((plan_moment,'start constructing',beautiful_scvt,beautiful_place))
                            current_events.add((plan_moment + build_dura,'finish constructing',beautiful_scvt,beautiful_place))
                        elif beautiful_thing in self.all_structures:
                            # pfoc,labs
                            beautiful_buildplan = (
                            self.notag, beautiful_thing, beautiful_place, plan_moment-20, plan_moment, plan_moment + build_dura)
                            beautiful_trainplan = (
                            beautiful_thing, beautiful_place, plan_moment-20, plan_moment, plan_moment + build_dura)
                            current_events.add((plan_moment-20, 'start ambition', self.notag, beautiful_place))
                            current_events.add((plan_moment, 'start growing', self.notag, beautiful_place))
                            current_events.add((plan_moment + build_dura, 'finish growing', self.notag, beautiful_place))
                        else:
                            # army,upgr
                            beautiful_buildplan = (self.notag,beautiful_thing,beautiful_place,plan_moment-20,plan_moment,plan_moment + build_dura)
                            beautiful_trainplan = (beautiful_thing,beautiful_place,plan_moment-20,plan_moment,plan_moment + build_dura)
                            current_events.add((plan_moment-20, 'start gym', self.notag, beautiful_place))
                            current_events.add((plan_moment, 'start training', self.notag, beautiful_place))
                            current_events.add((plan_moment + build_dura, 'finish training', self.notag, beautiful_place))
                            # forward the time to "start constructing"
                        self.planning.append(beautiful_buildplan)
                # play events out
                if plannable:
                    if (extragas == 0) and (extraminerals == 0):
                        self.log_planning_bp(beautiful_buildplan)
                    at_construction_start = (plan_moment < 0)
                    while (not at_construction_start) and (len(current_events) > 0):
                        nextmoment = 9999
                        for (moment,stri,scvt,goal) in current_events:
                            if (moment<nextmoment):
                                nextmoment = moment
                        # happen all events at nextmoment
                        # in the order: finish, start walk, start build
                        del_current_events = set()
                        #
                        for (moment, stri, escvt, egoal) in current_events:
                            if (moment == nextmoment) and (stri == 'finish training'):
                                del_current_events.add((moment, stri, escvt, egoal))
                                del_current_training = set()
                                for trainplan in current_training:
                                    (thing, goal, startgym, starttrain, finish) = trainplan
                                    if (goal == egoal) and (moment == finish):
                                        del_current_training.add(trainplan)
                                        current_thingkinds.add(thing)
                                current_training -= del_current_training
                        for (moment, stri, escvt, egoal) in current_events:
                            if (moment == nextmoment) and (stri == 'finish growing'):
                                del_current_events.add((moment, stri, escvt, egoal))
                                del_current_growing = set()
                                for trainplan in current_growing:
                                    (thing, goal, startambition,startgrow,finish) = trainplan
                                    if (goal == egoal) and (moment == finish):
                                        del_current_growing.add(trainplan)
                                        current_thingkinds.add(thing)
                                        if thing == ORBITALCOMMAND:
                                            current_mimminers += 3
                                current_growing -= del_current_growing
                        for (moment, stri, escvt, egoal) in current_events:
                            if (moment == nextmoment) and (stri == 'finish constructing'):
                                del_current_events.add((moment, stri, escvt, egoal))
                                del_current_constructing = set()
                                for buildplan in current_constructing:
                                    (tag, thing, goal, startwalk,startconstruct,finish) = buildplan
                                    if (tag == escvt) and (goal == egoal) and (moment == finish):
                                        del_current_constructing.add(buildplan)
                                        current_freescvs.add((tag,goal,finish))
                                        current_thingkinds.add(thing)
                                        if thing == REFINERY:
                                            current_gasminers += 3
                                current_constructing -= del_current_constructing
                        #
                        for (moment,stri,escvt,egoal) in current_events:
                            if (moment == nextmoment) and (stri == 'start walking'):
                                del_current_events.add((moment,stri,escvt,egoal))
                                del_current_freescvs = set()
                                for (tag, position, since) in current_freescvs:
                                    if tag == escvt:
                                        del_current_freescvs.add((tag, position, since))
                                        current_walking.add(beautiful_buildplan)
                                current_freescvs -= del_current_freescvs
                        for (moment,stri,escvt,egoal) in current_events:
                            if (moment == nextmoment) and (stri == 'start gym'):
                                del_current_events.add((moment,stri,escvt,egoal))
                                current_gym.add(beautiful_trainplan)
                        for (moment,stri,escvt,egoal) in current_events:
                            if (moment == nextmoment) and (stri == 'start ambition'):
                                del_current_events.add((moment,stri,escvt,egoal))
                                current_ambition.add(beautiful_trainplan)
                        #
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
                                        current_spendable_minerals -= cost.minerals
                                        current_spendable_vespene -= cost.vespene
                                        current_buildings_and_parts.add((thing, goal.x, goal.y))
                                        if (thing == beautiful_thing) and (goal == beautiful_place):
                                            at_construction_start = True
                                current_walking -= del_current_walking
                        for (moment, stri, escvt, egoal) in current_events:
                            if (moment == nextmoment) and (stri == 'start growing'):
                                del_current_events.add((moment, stri, escvt, egoal))
                                del_current_ambition = set()
                                for trainplan in current_ambition:
                                    (thing, goal, startambition,startgrow,finish) = trainplan
                                    if (goal == egoal) and (moment == startgrow):
                                        del_current_ambition.add(trainplan)
                                        current_growing.add(trainplan)
                                        cost = self.get_cost(thing)
                                        current_spendable_minerals -= cost.minerals
                                        current_spendable_vespene -= cost.vespene
                                        current_buildings_and_parts.add((thing, goal.x, goal.y))
                                        if (thing == beautiful_thing) and (goal == beautiful_place):
                                            at_construction_start = True
                                current_ambition -= del_current_ambition
                        for (moment, stri, escvt, egoal) in current_events:
                            if (moment == nextmoment) and (stri == 'start training'):
                                del_current_events.add((moment, stri, escvt, egoal))
                                del_current_gym = set()
                                for trainplan in current_gym:
                                    (thing, goal, startgym,startgrow,finish) = trainplan
                                    if (goal == egoal) and (moment == startgrow):
                                        del_current_gym.add(trainplan)
                                        current_training.add(trainplan)
                                        cost = self.get_cost(thing)
                                        current_spendable_minerals -= cost.minerals
                                        current_spendable_vespene -= cost.vespene
                                        if (thing == beautiful_thing) and (goal == beautiful_place):
                                            at_construction_start = True
                                current_gym -= del_current_gym
                        current_events -= del_current_events
                    if len(current_events) == 0:
                        self.log_success('INTERNAL ERROR planning order '+beautiful_thing.name)
                        # if the factory flies, a starport can give this error
                        plannable = False
                    # grow
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
        #       ccs in construction nearly finished are included
        for cc in self.structures(COMMANDCENTER):
            if cc.build_progress>0.85:
                if cc not in self.all_bases:
                    self.all_bases.append(cc)
        # exclude a cc for pf-rush
        if self.cheese3_cc in self.all_bases:
            del self.all_bases[self.all_bases.index(self.cheese3_cc)]
        #
        #   All idle structures
        self.idle_structure_tags = []
        for kind in self.all_structures:
            for one in self.structures(kind).ready.idle:
                self.idle_structure_tags.append(one.tag)
        #
        #   in the jump lost battlecruisers increase bc_fear
        #       uses old state_of_unittag info!
        living = 0
        for bc in self.units(BATTLECRUISER):
            if (bc.tag in self.state_of_unittag):
                if self.state_of_unittag[bc.tag] == 'repair':
                    living += 1
        past = 0
        for bct in self.state_of_unittag:
            if self.state_of_unittag[bct] == 'repair':
                past = past = 1
        if past > living:
            self.bc_fear = min(500,self.bc_fear+40)
        #
        # state_of_unittag  contains tags of all living battlecruisers, unhealthy if repairing
        new_state_of_unittag = {}
        for bc in self.units(BATTLECRUISER):
            if (bc.tag in self.state_of_unittag):
                if (self.state_of_unittag[bc.tag] == 'repair'):
                    if (bc.health<bc.health_max-25):
                        new_state_of_unittag[bc.tag] = 'repair'
                    else:
                        new_state_of_unittag[bc.tag] = 'lazy'
                else:
                    new_state_of_unittag[bc.tag] = self.state_of_unittag[bc.tag]
            else:
                new_state_of_unittag[bc.tag] = 'lazy'
        # also siegetanks
        for tnk in self.units(SIEGETANK) + self.units(SIEGETANKSIEGED):
            if (tnk.tag in self.state_of_unittag):
                new_state_of_unittag[tnk.tag] = self.state_of_unittag[tnk.tag]
        self.state_of_unittag = new_state_of_unittag
        #
        #   bestbctag is notag or a tag of a living battlecruiser
        just_one_bctag = self.notag
        seen = False
        for bc in self.units(BATTLECRUISER):
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
        # owner_of_ambistrt may have outdated info
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
                    if (self.structure_of_trabu_scvt[scvt] in [REFINERY,REFINERYRICH]):
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
        # cheesetag
        if self.cheese_scv is None:
            cheesetag = self.notag
        else:
            cheesetag = self.cheese_scv.tag
        #   job_of_scvt contains the tag of all living scvs
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
                    if (job not in ['mimminer','gasminer','builder','volunteer']):
                        self.log_success('collecting but wrong job ' + job + ' ' + name)
                else: # not collecting
                    if (job in ['mimminer', 'gasminer','volunteer']):
                        self.log_success('not collecting but job ' + job + ' ' + name)
                        self.log_command('scv.move(self.shipyard)')
                        scv.move(self.shipyard)
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
            if self.job_of_scvt[scvt] in ['traveller','builder']:
                new_goal_of_trabu_scvt[scvt] = self.goal_of_trabu_scvt[scvt]
        self.goal_of_trabu_scvt = new_goal_of_trabu_scvt
        #   structure_of_trabu_scvt contains the tag of living builders and travellers
        new_structure_of_trabu_scvt = {}
        for scvt in self.all_scvt:
            if self.job_of_scvt[scvt] in ['traveller','builder']:
                new_structure_of_trabu_scvt[scvt] = self.structure_of_trabu_scvt[scvt]
        self.structure_of_trabu_scvt = new_structure_of_trabu_scvt
        # owner_of_trabu_scvt may have outdated info
        #
        # army_supply
        self.army_supply = 0
        for mar in self.all_army:
            self.army_supply = self.army_supply + self.supply_of_army[mar] * len(self.units(mar))

    #*********************************************************************************************************************

    async def build_minima(self):
        self.routine = 'build_minima'
        # advice on stuck amount=0 situations into bagofthings
        ccs = self.we_started_amount(COMMANDCENTER) + self.structures(PLANETARYFORTRESS).amount \
              + self.structures(ORBITALCOMMAND).amount
        bcs = self.we_started_amount(BATTLECRUISER)
        if self.supply_used < 60: # ordered
            if (ccs == 0):
                self.one_in_bagofthings(COMMANDCENTER)
            if (not self.we_started_a(SUPPLYDEPOT)):
                self.one_in_bagofthings(SUPPLYDEPOT)
            if (not self.we_started_a(BARRACKS)):
                self.one_in_bagofthings(BARRACKS)
            if (not self.we_started_a(REFINERY)):
                self.one_in_bagofthings(REFINERY)
            if (not self.we_started_a(ENGINEERINGBAY)) and (ccs >= 2):
                self.one_in_bagofthings(ENGINEERINGBAY)
            if (not self.we_started_a(FACTORY)) and (ccs >= 2):
                self.one_in_bagofthings(FACTORY)
            if (not self.we_started_a(STARPORT)) and (ccs >= 2):
                self.one_in_bagofthings(STARPORT)
            if (not self.we_started_a(FUSIONCORE)) and (ccs >= 2):
                self.one_in_bagofthings(FUSIONCORE)
            if (not self.we_started_a(MISSILETURRET)) and (ccs >= 2):
                self.one_in_bagofthings(MISSILETURRET)
            if (not self.we_started_a(ARMORY)) and (ccs >= 4):
                self.one_in_bagofthings(ARMORY)
            if (not self.we_started_a(RAVEN)) and (bcs >= 4):
                self.one_in_bagofthings(RAVEN)
            if (not self.we_started_a(FACTORYTECHLAB)):
                self.one_in_bagofthings(FACTORYTECHLAB)
            if (not self.we_started_a(STARPORTTECHLAB)):
                self.one_in_bagofthings(STARPORTTECHLAB)
        else: # the same, but thrown
            if (ccs == 0):
                self.throw_if_rich(COMMANDCENTER,'build_minima',1)
            if (not self.we_started_a(SUPPLYDEPOT)):
                self.throw_if_rich(SUPPLYDEPOT,'build_minima',1)
            if (not self.we_started_a(BARRACKS)):
                self.throw_if_rich(BARRACKS,'build_minima',1)
            if (not self.we_started_a(REFINERY)):
                self.throw_if_rich(REFINERY,'build_minima',1)
            if (not self.we_started_a(ENGINEERINGBAY)) and (ccs >= 2):
                self.throw_if_rich(ENGINEERINGBAY,'build_minima',1)
            if (not self.we_started_a(FACTORY)) and (ccs >= 2):
                self.throw_if_rich(FACTORY,'build_minima',1)
            if (not self.we_started_a(STARPORT)) and (ccs >= 2):
                self.throw_if_rich(STARPORT,'build_minima',1)
            if (not self.we_started_a(FUSIONCORE)) and (ccs >= 2):
                self.throw_if_rich(FUSIONCORE,'build_minima',1)
            if (not self.we_started_a(MISSILETURRET)) and (ccs >= 2):
                self.throw_if_rich(MISSILETURRET,'build_minima',1)
            if (not self.we_started_a(ARMORY)) and (ccs >= 4):
                self.throw_if_rich(ARMORY,'build_minima',1)
            if (not self.we_started_a(RAVEN)) and (bcs >= 4):
                self.throw_if_rich(RAVEN,'build_minima',1)
            if (not self.we_started_a(FACTORYTECHLAB)):
                self.throw_if_rich(FACTORYTECHLAB,'build_minima',1)
            if (not self.we_started_a(STARPORTTECHLAB)):
                self.throw_if_rich(STARPORTTECHLAB,'build_minima',1)


    def lategame(self):
        self.routine = 'lategame'
        # make bagofthings
        # collect some things to add to bagofthings_exe
        # advice on stuck situations
        # not upgrades as they clutter
        scvs = len(self.units(SCV))
        ccs = self.we_started_amount(COMMANDCENTER) + self.structures(PLANETARYFORTRESS).amount \
              + self.structures(ORBITALCOMMAND).amount
        bcs = self.we_started_amount(BATTLECRUISER)
        mts = self.we_started_amount(MISSILETURRET)
        core = self.we_finished_a(FUSIONCORE)
        wms = self.we_started_amount(WIDOWMINE)
        good_drones_supply = min(self.supply_used / 2 + 10, 80)
        good_army_supply = self.supply_used - good_drones_supply
        # supplydepots elsewhere
        # refineries elsewhere
        # build_minima elsewhere
        #
        # fill out
        for sp in self.structures(FACTORY).ready:
            if not sp.has_add_on:
                self.blunt_to_bagofthings(FACTORYTECHLAB)
        for sp in self.structures(STARPORT).ready:
            if not sp.has_add_on:
                self.blunt_to_bagofthings(STARPORTTECHLAB)
        # army
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
        if (bcs >= 2) and (self.we_started_amount(ENGINEERINGBAY) < 1):
            self.blunt_to_bagofthings(ARMORY)
        # defence
        for cc in self.structures(ORBITALCOMMAND):
            if cc.position in self.cc_destiny:
                if self.cc_destiny[cc.position] == 'pf':
                    self.blunt_to_bagofthings(PLANETARYFORTRESS)
                else:
                    self.blunt_to_bagofthings(ORBITALCOMMAND)
        vikings = 0
        for ene in self.seen_enemy_units:
            if (ene.type_id in self.viking_targets) and (ene.type_id != OVERLORD):
                vikings += 1.5
        if self.we_started_amount(VIKINGFIGHTER) < vikings:
            self.blunt_to_bagofthings(VIKINGFIGHTER)
        # log
        stri = 'lategame added bagofthings: '
        for th in self.bagofthings:
            stri = stri + th.name + ' '
        self.log_success(stri)


    def midgame(self,thing,amount):
        self.routine = 'midgame'
        for t in range(0,amount):
            self.midgame_things.append(thing)

    def shrink_bagofthings_have(self):
        # from the midgame bagofthings plan, remove what the opening started building already
        kinds = set()
        for thing in self.bagofthings:
            kinds.add(thing)
        todel = []
        for thing in kinds:
            am = self.we_started_amount(thing)
            while am > 0:
                am -= 1
                if thing in self.bagofthings:
                    del self.bagofthings[self.bagofthings.index(thing)]

    ##############################################################################
    # hoopy: is this buildseries possible?
    #        is this buildseries executable in that order from current situation?
    # buildingswithout >= labs
    # check techtree
    #
    def hoopy_add(self, thing):
        self.hoopy_made.add(thing)
        if thing in [BARRACKS,FACTORY,STARPORT,COMMANDCENTER]:
            self.transformable[thing] += 1
        elif thing in self.all_labs + self.all_pfoc:
            for (th,crad) in self.cradle:
                if th == thing:
                    self.transformable[crad] -= 1

    def hoopy_can_add(self,thing) -> bool:
        isha = True
        if thing in self.all_labs + self.all_pfoc:
            for (th, crad) in self.cradle:
                if th == thing:
                    if self.transformable[crad] <= 0:
                        isha = False
                        self.log_buildstate('buildseries error 1')
        for (th, needs) in self.techtree:
            if th == thing:
                if needs not in self.hoopy_made:
                    isha = False
                    self.log_buildstate('buildseries error 2')
        return isha

    def hoopy_get_sit(self):
        self.routine = 'hoopy_get_sit'
        self.transformable = {}
        for thing in [BARRACKS,FACTORY,STARPORT,COMMANDCENTER]:
            self.transformable[thing] = 0
        self.hoopy_made = set()
        for (thing,pos) in self.birds:
            self.hoopy_add(thing)
            # a cc is hidden under a completed pf
            if thing in self.all_pfoc:
                self.transformable[COMMANDCENTER] +=1
        for (bar,thing,pos,dura) in self.eggs:
            self.hoopy_add(thing)
            # TODO test if the cc is in birds when the pf is in eggs
        for (bar,thing,pos,dura,owner) in self.preps:
            self.hoopy_add(thing)
        for (thing, pos, owner) in self.thoughts:
            self.hoopy_add(thing)


    def hoopy_buildseries(self) -> bool:
        # DEMANDS done is self.hoopy_get_sit()
        self.routine = 'hoopy_buildseries'
        isha = True
        for infa_thing in self.buildseries:
            thing = self.basekind_of(infa_thing)
            isha = isha and self.hoopy_can_add(thing)
            self.hoopy_add(thing)
        return isha

    ##############################################################################
    # happy: is this buildorder possible?
        # build labs on buildingswithout
        # build labarmy on buildingswith
        # check techtree

    def happy_add(self, thing,pos):
        self.happy_made.add(thing)
        if thing in [BARRACKS,FACTORY,STARPORT,COMMANDCENTER]:
            if pos in self.bui_min_lab:
                self.bui_min_lab[pos] += 1
            else:
                self.bui_min_lab[pos] = 1
        elif thing in self.all_labs + self.all_pfoc:
            if pos in self.bui_min_lab:
                self.bui_min_lab[pos] -= 1
            else:
                self.bui_min_lab[pos] = -1

    def happy_can_add(self,thing,pos) -> bool:
        isha = True
        if thing in self.all_labs + self.all_pfoc:
            if pos in self.bui_min_lab:
                if self.bui_min_lab[pos] != 1:
                    isha = False
                    self.log_buildstate('buildorder error 1')
            else:
                isha = False
                self.log_buildstate('buildorder error 2')
        for (th, needs) in self.techtree:
            if th == thing:
                if needs not in self.happy_made:
                    isha = False
                    self.log_buildstate('buildorder error 3 '+th.name+' needs '+needs.name)
        if thing in self.all_labarmy:
            if pos in self.bui_min_lab:
                if self.bui_min_lab[pos] != 0:
                    isha = False
                    self.log_buildstate('buildorder error 4')
            else:
                isha = False
                self.log_buildstate('buildorder error 5')
        return isha


    def happy_get_sit(self):
        self.routine = 'happy_get_sit'
        self.bui_min_lab = {}
        self.happy_made = set()
        for (thing,pos) in self.birds:
            self.happy_add(thing,pos)
            if thing in self.all_pfoc:
                self.bui_min_lab[pos] = 0
        for (bar,thing,pos,dura) in self.eggs:
            self.happy_add(thing, pos)
        for (bar,thing,pos,dura,owner) in self.preps:
            self.happy_add(thing, pos)
        for (thing, pos, owner) in self.thoughts:
            self.happy_add(thing, pos)

    def happy_buildorder(self) -> bool:
        # DEMANDS done is self.happy_get_sit()
        self.routine = 'happy_buildorder'
        isha = True
        # get the new part of self.buildorder
        buildorderstate = []
        for (thing, pos) in self.buildorder:
            buildorderstate.append((thing,pos,'new'))
        for (ba, th, po, du, ow) in self.preps:
            tps = (th,po,'new')
            if tps in buildorderstate:
                nr = buildorderstate.index(tps)
                buildorderstate[nr] = (th,po,'prep')
        for (th,po,ow) in self.thoughts:
            tps = (th,po,'new')
            if tps in buildorderstate:
                nr = buildorderstate.index(tps)
                buildorderstate[nr] = (th,po,'thought')
        # buildorderstate new should be ordered
        for (thing,pos,state) in buildorderstate:
            if state == 'new':
                # should be buildable in this order
                isha = isha and self.happy_can_add(thing,pos)
                self.happy_add(thing, pos)
        return isha

    #############################################################################


    def one_in_bagofthings(self,thing):
        self.routine = 'one_in_bagofthings'
        have = self.we_started_amount(thing)
        for th in self.bagofthings:
            if th == thing:
                have += 1
        if have < 1:
            self.bagofthings.append(thing)

    def blunt_to_bagofthings(self,thing):
        self.routine = 'blunt_to_bagofthings'
        have = self.we_started_amount(thing)
        for th in self.bagofthings:
            if th == thing:
                have += 1
        if have < self.maxam_of_thing(thing):
            self.bagofthings.append(thing)

    def buildseries_exe_from_bagofthings_exe(self):
        self.bagoftree_of_bagofthings()
        self.bagoftree_exe = self.bagoftree.copy()
        self.bagofcradle_of_bagoftree()
        self.bagofcradle_exe = self.bagofcradle.copy()
        self.buildseries_of_bagofcradle()
        self.optimize_buildseries()
        self.buildseries_exe = self.buildseries.copy()

    async def make_planning_exe(self):
        self.routine = 'make_planning_exe'
        # cut off a dream at the loss of a structure
        i_have_structures = len(self.structures) - len(self.structures(BUNKER))
        i_have_weak_flying = 0
        for kind in self.landable:
            for bu in self.structures(kind):
                if bu.health < 700:
                    i_have_weak_flying += 1
        if (i_have_structures < self.but_i_had_structures) or (i_have_weak_flying > self.but_i_had_flying):
            # bad situation; redo the planning but do not phase-change.
            self.log_success('$$$$$$$ lost a building; breaking off plannings')
            # keep self.bagofthings_exe
            self.bagoftree_exe = []
            self.bagofcradle_exe = []
            self.buildseries_exe = []
            for (th,po,status) in self.buildorder_exe:
                if (not self.near(po, self.enemyloc, 50)): # exclude proxies
                    self.recycling.append((th,po))
            self.buildorder_exe = []
            self.buildplan_exe = []
            todel = []
            for tpo in self.thoughts:
                (thing,pos,owner) = tpo
                if owner == 'follow_planning_exe':
                    todel.append(tpo)
            for tpo in todel:
                del self.thoughts[self.thoughts.index(tpo)]
            # cancel current orders too
            self.ambition_of_strt = {}
            self.owner_of_ambistrt = {}
            for scv in self.units(SCV):
                scvt = scv.tag
                if self.job_of_scvt[scvt] not in ['mimminer','gasminer','builder']:
                    # choosing not to use promote()
                    self.job_of_scvt[scvt] = 'idler'
                    self.promotionsite_of_scvt[scvt] = self.nowhere
                    if scvt in self.goal_of_trabu_scvt:
                        del self.goal_of_trabu_scvt[scvt]
                        del self.structure_of_trabu_scvt[scvt]
                    if not scv.is_idle:
                        self.log_command('scv(AbilityId.STOP)')
                        scv(AbilityId.STOP)
            vision_of_scvt = {}
            self.clean_layout()
            # remake plans
            self.buildseries_exe_from_bagofthings_exe()
        self.but_i_had_structures = i_have_structures
        self.but_i_had_flying = i_have_weak_flying
        # first make buildseries
        if ((len(self.buildorder_exe) == 0)):
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
                self.game_phase = 'lategame'
                self.log_buildseries('game_phase')
                self.log_success('============================================================ lategame =======')
            elif self.game_phase == 'lategame':
                self.game_phase = 'endgame'
                self.log_buildseries('game_phase')
                self.log_success('============================================================ endgame =======')
            # make optimized buildseries
            if (self.game_phase == 'opening'):
                self.buildseries = self.buildseries_opening
                self.buildseries_exe = self.buildseries.copy()
                # make the simpler bags
                self.bagofthings = []
                for infa_th in self.buildseries:
                    th = self.basekind_of(infa_th)
                    self.bagofthings.append(th)
                self.bagofthings_exe = self.bagofthings.copy()
                self.bagoftree_of_bagofthings()
                self.bagoftree_exe = self.bagoftree.copy()
                self.bagofcradle_of_bagoftree()
                self.bagofcradle_exe = self.bagofcradle.copy()
            elif (self.game_phase == 'midgame'):
                self.bagofthings = []
                for thing in self.midgame_things:
                    self.blunt_to_bagofthings(thing)
                self.shrink_bagofthings_have()
                # bagofthings is made. Build up from here.
                self.bagofthings_exe = self.bagofthings.copy()
                self.bagoftree_of_bagofthings()
                self.bagoftree_exe = self.bagoftree.copy()
                self.bagofcradle_of_bagoftree()
                self.bagofcradle_exe = self.bagofcradle.copy()
                self.buildseries_of_bagofcradle()
                self.optimize_buildseries()
                self.buildseries_exe = self.buildseries.copy()
            elif (self.game_phase == 'lategame'):
                self.bagofthings = []
                self.lategame()
                self.bagofthings_exe = self.bagofthings.copy()
                self.buildseries_exe_from_bagofthings_exe()
            elif (self.game_phase == 'endgame'):
                # make only thrown things, not ordered things
                self.bagofthings = []
                self.bagofthings_exe = self.bagofthings.copy()
                self.buildseries_exe_from_bagofthings_exe()
            # buildseries_exe is made
            # Keep old places for reuse.
            for (th,po,status) in self.buildorder_exe:
                if not self.near(po,self.enemyloc,50):
                    self.recycling.append((th,po))
            self.buildorder_of_buildseries()
            self.buildorder_exe = []
            for (th,pl) in self.buildorder:
                self.buildorder_exe.append((th,pl,'new'))
        # buildorder_exe is made
        self.buildorder = []
        for (th,pl,status) in self.buildorder_exe:
            self.buildorder.append((th,pl))
        self.happy_get_sit()
        if not self.happy_buildorder():
            self.log_success('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
            self.log_success('%%%%%%%%%%%%%%%%%%%%%%%%%%% TO DO %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
            self.log_success('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        self.get_situation()
        self.planning_of_buildorder(0,0)
        self.optimize_planning()
        self.planning_exe = self.planning.copy()

    # *********************************************************************************************************************

    def remove_from_planning_etc(self, thing, place):
        todel = set()
        first = True
        for bp in self.planning_exe:
            (sv, th, pl, sr, sc, fi) = bp
            if first and (th == thing) and (pl == place):
                todel.add(bp)
                first = False
        for bp in todel:
            del self.planning_exe[self.planning_exe.index(bp)]
        todel = set()
        first = True
        for tps in self.buildorder_exe:
            (th,pl,st) = tps
            if first and (th == thing) and (pl == place):
                todel.add(tps)
                first = False
        for tps in todel:
            del self.buildorder_exe[self.buildorder_exe.index(tps)]
        # recalc to INFESTED
        tp = (thing,place)
        infa_thing = thing
        if tp == (BUNKER, self.cheese_bunker_pos):
            infa_thing = INFESTEDBUNKER
        elif tp == (FACTORY, self.cheese_factory_pos):
            infa_thing = INFESTEDFACTORY
        elif tp == (BARRACKS, self.cheese_barracks_pos):
            infa_thing = INFESTEDBARRACKS
        elif tp == (STARPORT, self.cheese_starport_pos):
            infa_thing = INFESTEDSTARPORT
        if infa_thing in self.buildseries_exe:
            del self.buildseries_exe[self.buildseries_exe.index(infa_thing)]
        # no infested in the bags
        if thing in self.bagofcradle_exe:
            del self.bagofcradle_exe[self.bagofcradle_exe.index(thing)]
        if thing in self.bagoftree_exe:
            del self.bagoftree_exe[self.bagoftree_exe.index(thing)]
        if thing in self.bagofthings_exe:
            del self.bagofthings_exe[self.bagofthings_exe.index(thing)]



    async def implementing_buildorder_exe(self):
        self.routine = 'implementing_buildorder_exe'
        # new to thought
        for nr in range(0,len(self.buildorder_exe)):
            (thing,place,status) = self.buildorder_exe[nr]
            if status == 'new':
                donow = True
                for (th, po, ow) in self.thoughts:
                    if (th == thing) and (place == po) and (ow != 'follow_planning_exe'):
                        donow = False
                        self.log_success('In thoughts ' + ow + ' already put a ' + thing.name + ' ' + self.txt(place))
                if donow:
                    if self.add_thought(thing, place, 'follow_planning_exe'):
                        self.buildorder_exe[nr] = (thing,place,'thought')
                    else:
                        self.log_success('Could not add thought '+ thing.name + ' ' + self.txt(place))
                        # remove all buildorders with this place
                        for secnr in range(0,len(self.buildorder_exe)):
                            (th,pl,sta) = self.buildorder_exe[secnr]
                            if pl == place:
                                self.buildorder_exe[secnr] = (th,pl,'nogo')
                                self.log_success('So '+th.name+' '+self.txt(pl)+' is a nogo.')
        # prep to away
        done = set()
        for (thing,place,status) in self.buildorder_exe:
            if status in ['prep','nogo']:
                seen = False
                for (bar,martype,pos,dura,owner) in self.preps:
                    if (thing == martype):
                        if (place == pos) or (place == self.somewhere):
                            seen = True
                if not seen:
                    done.add((thing,place))
        # clean each _exe
        for (thing,place) in done:
            self.remove_from_planning_etc(thing,place)


    async def follow_planning_exe(self):
        self.routine = 'follow_planning_exe'
        # debug logging
        if len(self.buildorder_exe) > 0:
            stri = ''
            for nr in range(0,min(3,len(self.buildorder_exe))):
                (th, pl, status) = self.buildorder_exe[nr]
                stri = stri + th.name + ' '
            self.log_success('buildorder_exe starts with '+stri)
            for nr in range(0,min(3,len(self.planning_exe))):
                (scvt, thing, place, sr, sc, fi)  = self.planning_exe[nr]
                self.log_success('top 3 planning_exe '+thing.name+' '+str(sr)+' '+str(sc)+' at '+self.txt(place))
        #
        todel = set()
        for bp in self.planning_exe:
            (scvt, thing, place, sr, sc, fi) = bp
            for nr in range(0,len(self.buildorder_exe)):
                (th,pl,status) = self.buildorder_exe[nr]
                if (th == thing) and (status == 'thought'):
                    if (pl == place) or (pl == self.somewhere):
                        if thing in self.all_structures_tobuildwalk:
                            if sr <= 0:
                                if scvt not in self.goal_of_trabu_scvt:
                                    if await self.build_thing_tobuildwalk(scvt,thing, place, 'follow_planning_exe'):
                                        self.buildorder_exe[nr] = (th,place,'prep')
                        else: # labs, pfoc, army, upgr
                            if sc <= 0:
                                inambi = False
                                for abar in self.structures:
                                    if abar.position == place:
                                        if abar.tag in self.ambition_of_strt:
                                            inambi = True
                                if not inambi:
                                    if await self.build_thing(thing, place, 'follow_planning_exe'):
                                        self.buildorder_exe[nr] = (th, place, 'prep')


    def make_unthinkable(self, thing,pos):
        self.unthinkable.add((thing,pos))
        # remove from throwspots and recycling too
        todel = []
        for tps in self.throwspots:
            (th, po, status, ow, pri) = tps
            if (th == thing) and (po == pos):
                todel.append(tps)
        for tps in todel:
            del self.throwspots[self.throwspots.index(tps)]
        todel = []
        for tps in self.recycling:
            (th,po) = tps
            if (th == thing) and (po == pos):
                todel.append(tps)
        for tps in todel:
            del self.recycling[self.recycling.index(tps)]


    def add_thought(self, thing,pos,owner) -> bool:
        self.routine = 'add_thought'
        ok = True
        for (th,po,ow) in self.thoughts:
            if (th == thing) and (pos == po) and (ow != owner):
                ok = False
                self.log_success('Add_thought halted doubling of ' + thing.name + ' at ' + self.txt(pos) + ' by ' + ow + ' and ' + owner)
        if self.we_started_amount(thing) >= self.future_maxam_of_thing(thing):
            ok = False
            self.log_success('Add_thought halted by future maximum a ' + thing.name + ' by ' + owner)
        # no restrictions on e.g. minerals, free cradle, as those can become ok later
        if not self.check_future_techtree(thing):
            ok = False
            self.log_success('Add_thought halted by future techtree a '+thing.name+' by '+owner)
        if (thing,pos) in self.unthinkable:
            ok = False
            self.log_success('Add_thought halted unthinkable ' + thing.name +' at ' + self.txt(pos) + ' by ' + owner)
        if ok:
            self.thoughts.append((thing,pos,owner))
        return ok


    def throw_somewhere(self, thing, owner, priority):
        # per owner, thing: find or reuse a place, store it in throwspots
        # also write_layout
        # if not found, do nothing
        self.routine = 'throw_somewhere'
        self.log_throw(owner + ' throws somewhere a ' + thing.name)
        foundplace = False
        for (th,po,status, ow, pri) in self.throwspots:
            if (th == thing) and (ow == owner) and (pri == priority):
                place = po
                if (thing, place) not in self.unthinkable:
                    foundplace = True
        if not foundplace:
            if thing in self.all_structures_tobuildwalk:
                if self.find_tobuildwalk_a_place(thing):
                    place = self.function_result_Point2
                    if (thing,place) not in self.unthinkable:
                        foundplace = True
            elif thing in self.all_pfoc:
                for cc in self.structures(COMMANDCENTER).ready:
                    if cc.position in self.cc_destiny:
                        dest = self.cc_destiny[cc.position]
                        if (thing == PLANETARYFORTRESS) and (dest == 'pf'):
                            place = cc.position
                            if (thing, place) not in self.unthinkable:
                                foundplace = True
                        elif (thing == ORBITALCOMMAND) and (dest == 'oc'):
                            place = cc.position
                            if (thing, place) not in self.unthinkable:
                                foundplace = True
            elif thing in self.all_labs:
                for (th, bar) in self.cradle:
                    if th == thing:
                        sps = []
                        for aba in self.structures(bar).ready:
                            if not aba.has_add_on:
                                sps.append(aba)
                        if len(sps) > 0:
                            sp = random.choice(sps)
                            place = sp.position
                            if (thing, place) not in self.unthinkable:
                                foundplace = True
            else: # army, upgr
                for (th, bar) in self.cradle:
                    if th == thing:
                        needs_lab = False
                        for (thi, need) in self.techtree:
                            if thi == thing:
                                if need in self.all_labs:
                                    needs_lab = True
                        if needs_lab:
                            sps = []
                            spsi = []
                            for sp in self.structures(bar).ready:
                                if sp.has_add_on:
                                    sps.append(sp)
                                    if sp.is_idle:
                                        spsi.append(sp)
                        else:
                            sps = self.structures(bar).ready
                            spsi = self.structures(bar).ready.idle
                        if len(sps) > 0:
                            if len(spsi) > 0:
                                sp = random.choice(spsi)
                            else:
                                sp = random.choice(sps)
                            place = sp.position
                            if (thing, place) not in self.unthinkable:
                                foundplace = True
            if foundplace:
                self.throwspots.append((thing,place,'new',owner,priority))
                self.log_throw('placable')
                if thing in self.all_structures_tobuildwalk:
                    self.write_layout(thing, place)


    def throw_if_rich(self,thing,owner,priority):
        # checks thoughts money
        # checks amount
        # finds a place
        # fills throwspots
        # writes layout
        self.routine = 'throw_if_rich'
        self.log_throw(owner + ' throws if rich a ' + thing.name)
        cost = self.get_cost(thing)
        gasless = (cost.vespene == 0)
        if self.we_started_amount(thing) < self.maxam_of_thing(thing):
            # trow if money >= eps + bccost + half throwncost
            # half because there is time too, dont be too strict
            used_mim = 450
            used_gas = 350
            for (th,pl,ow) in self.thoughts:
                cost = self.get_cost(th)
                used_mim += cost.minerals/2
                used_gas += cost.vespene/2
            for (bar,martype,pos,dura,ow) in self.preps:
                cost = self.get_cost(martype)
                used_mim += cost.minerals/2
                used_gas += cost.vespene/2
            if (self.minerals >= used_mim):
                if (self.vespene >= used_gas) or gasless:
                    self.log_throw('payable')
                    self.throw_somewhere(thing, owner, priority)

    def throw_at_spot_if_rich(self,thing,place,owner, priority):
        # checks thoughts money
        # checks amount
        # fills throwspots
        # writes layout
        self.routine = 'throw_at_spot_if_rich'
        self.log_throw(owner + ' throws at spot a ' + thing.name)
        cost = self.get_cost(thing)
        gasless = (cost.vespene == 0)
        if self.we_started_amount(thing) < self.maxam_of_thing(thing):
            # trow if money >= eps + bccost + half throwncost
            # half because there is time too, dont be too strict
            used_mim = 450
            used_gas = 350
            for (th,pl,ow) in self.thoughts:
                cost = self.get_cost(th)
                used_mim += cost.minerals/2
                used_gas += cost.vespene/2
            for (bar,martype,pos,dura,ow) in self.preps:
                cost = self.get_cost(martype)
                used_mim += cost.minerals/2
                used_gas += cost.vespene/2
            if (self.minerals >= used_mim):
                if (self.vespene >= used_gas) or gasless:
                    self.throwspots.append((thing, place, 'new', owner, priority))
                    if thing in self.all_structures_tobuildwalk:
                        self.write_layout(thing, place)

    def throw_at_spot(self,thing,place,owner,priority):
        # checks amount
        # fills throwspots
        # writes layout
        self.routine = 'throw_at_spot'
        self.throwspots.append((thing, place, 'new', owner, priority))
        if thing in self.all_structures_tobuildwalk:
            self.write_layout(thing, place)


    async def throw_advance(self):        
        # push throwspots into thought
        for priority in [1, 2, 3]:
            for nr in range(0, len(self.throwspots)):
                (thing, place, status, ow, pri) = self.throwspots[nr]
                if (status == 'new') and (pri == priority):
                    if self.add_thought(thing, place, ow):
                        self.throwspots[nr] = (thing, place, 'thought', ow, pri)
            # build things into prep
            todel = []
            for tpso in self.throwspots:
                (thing,place,status, ow, pri) = tpso
                if (status == 'thought') and (pri == priority):
                    if thing in self.all_structures_tobuildwalk:
                        scvt = self.get_near_scvt_to_goodjob(place)
                        if await self.build_thing_tobuildwalk(scvt, thing, place,ow):
                            todel.append(tpso)
                            self.log_success('thrown '+thing.name+' for '+ow)
                    else: # labs, pfoc, army, upgr
                        if await self.build_thing(thing, place,ow):
                            todel.append(tpso)
                            self.log_success('thrown ' + thing.name+' for '+ow)
            for tpso in todel:
                del self.throwspots[self.throwspots.index(tpso)]


    async def supplydepots_adlib(self):
        self.routine = 'supplydepots_adlib'
        if (self.supply_left < 2 + self.supply_used // 6) and (self.supply_cap < 200):
            nprep = 0
            for (bar,martype,pos,dura,owner) in self.preps:
                if martype == SUPPLYDEPOT:
                    nprep += 1
            for (bar,martype,pos,dura) in self.eggs:
                if martype == SUPPLYDEPOT:
                    nprep += 1
            if (nprep == 0) or ((nprep == 1) and (self.supply_used > 90)):
                if len(self.structures) > 6:
                    self.throw_somewhere(SUPPLYDEPOT,'supplydepots_adlib',1)


    async def refineries_adlib(self):
        self.routine = 'refineries_adlib'
        if len(self.structures) > 8:
            nprep = 0
            for (bar,martype,pos,dura,owner) in self.preps:
                if martype == REFINERY:
                    nprep += 1
            if nprep == 0:
                self.throw_somewhere(REFINERY,'refineries_adlib',2)


    async def upgrades_adlib(self):
        self.routine = 'upgrades_adlib'
        for cradtype in [ARMORY,ENGINEERINGBAY,FUSIONCORE, BARRACKSTECHLAB, GHOSTACADEMY]:
            if cradtype in [ENGINEERINGBAY,BARRACKSTECHLAB]:
                loved = len(self.units(MARINE) + self.units(MARAUDER))
            else:
                loved = 2*len(self.units(BATTLECRUISER))
            if (len(self.structures(cradtype).ready.idle) > 0) and (len(self.all_bases) >= 3) and (loved >= 6):
                for pair in self.cradle:
                    if pair[1] == cradtype:
                        upg = pair[0]
                        if upg != NUKESILONOVA:
                            if self.check_techtree(upg):
                                if not self.we_started_a(upg):
                                    self.throw_if_rich(upg,'upgrades_adlib',3)
        # promote armory to hide widowmines
        loved = len(self.units(WIDOWMINE)) + len(self.units(WIDOWMINEBURROWED))
        if loved >= 6:
            if not self.we_started_a(ARMORY):
                self.throw_if_rich(ARMORY,'upgrades_adlib',3)

    def armybuildings_adlib(self):
        # reactive adding barrack, factory or starport with lab
        self.routine = 'armybuildings_adlib'
        ccs = self.we_started_amount(COMMANDCENTER) + self.structures(PLANETARYFORTRESS).amount \
              + self.structures(ORBITALCOMMAND).amount
        if ccs >= 3:
            for (lab_type,bui_type) in self.cradle:
                if lab_type in self.all_labs:
                    has_idle = False
                    for bui in self.structures(bui_type):
                        if bui.has_add_on and (bui.tag in self.idle_structure_tags):
                            has_idle = True
                    if not has_idle:
                        # need one more
                        canlab = self.we_started_amount(bui_type) - self.we_started_amount(lab_type)
                        for (th, po, status, ow, pri) in self.throwspots:
                            if (th == lab_type) and (status == 'new'):
                                canlab -=1
                            if (th == bui_type) and (status == 'new'):
                                canlab +=1
                        if canlab > 0:
                            self.throw_if_rich(lab_type,'armybuildings_adlib',2)
                        else:
                            bui_started = False
                            for (th, po, status, ow, pri) in self.throwspots:
                                if th == bui_type:
                                    bui_started = True
                            for (scv,th,pos,dura) in self.eggs:
                                if th == bui_type:
                                    bui_started = True
                            if not bui_started:
                                self.throw_if_rich(bui_type, 'armybuildings_adlib', 2)


    def army_adlib(self):
        self.routine = 'army_adlib'
        good_drones_supply = min(self.supply_used / 2 + 10, 80)
        good_army_supply = self.supply_used - good_drones_supply
        vikings = 0
        for ene in self.seen_enemy_units:
            if (ene.type_id in self.viking_targets) and (ene.type_id != OVERLORD):
                vikings += 1.5
        if (self.army_supply < good_army_supply) or (self.minerals > 1000):  # army
            if self.supply_used <= 194:
                self.throw_if_rich(BATTLECRUISER, 'army_adlib', 1)
                # RAVEN is in build_minima
                if self.we_started_amount(VIKINGFIGHTER) < vikings:
                    self.throw_if_rich(VIKINGFIGHTER, 'army_adlib', 2)
                self.throw_if_rich(SIEGETANK, 'army_adlib', 2)
                self.throw_if_rich(WIDOWMINE, 'army_adlib', 2)
                self.throw_if_rich(MARAUDER, 'army_adlib', 2)
            if self.supply_used < 200:
                self.throw_if_rich(MARINE, 'army_adlib', 2)

    def expansion_advisor(self):
        self.routine = 'expansion_advisor'
        good_drones_supply = min(self.supply_used / 2 + 10, 80)
        good_army_supply = self.supply_used - good_drones_supply
        if (self.army_supply >= good_army_supply) or (self.minerals > 600):
            if self.count_of_job['idler'] + self.count_of_job['volunteer'] > 5:
                self.throw_if_rich(COMMANDCENTER,'expansion_advisor',1)
            else:
                for cc in self.structures(COMMANDCENTER):
                    if cc.position in self.cc_destiny:
                        if self.cc_destiny[cc.position] == 'pf':
                            self.throw_if_rich(PLANETARYFORTRESS, 'expansion_advisor', 2)
                        else:
                            self.throw_if_rich(ORBITALCOMMAND, 'expansion_advisor', 1)


    def big_spender(self):
        # get rid of surplus money
        self.routine = 'big_spender'
        ccs = self.we_started_amount(COMMANDCENTER) + self.structures(PLANETARYFORTRESS).amount \
              + self.structures(ORBITALCOMMAND).amount
        mts = self.structures(MISSILETURRET).ready.amount
        good_drones_supply = min(self.supply_used / 2 + 10, 80)
        good_army_supply = self.supply_used - good_drones_supply
        if self.minerals > 500:
            if self.vespene > 400:
                if mts < ccs * 8:
                    self.throw_if_rich(MISSILETURRET,'big_spender',2)
            else: # no gas
                if self.supply_used < 194:
                    if (self.army_supply >= good_army_supply) or (self.minerals > 1000):  # expand, defend
                        if mts < ccs * 8:
                            self.throw_if_rich(MISSILETURRET,'big_spender',2)
                else: # maxsupply
                    if mts < ccs * 8:
                        self.throw_if_rich(MISSILETURRET,'big_spender',2)


    def extreme_spender(self):
        if (self.minerals > 2000) and (self.vespene > 1000) and (self.supply_used > 170):
            # try to control open area
            # reset unthinkable
            if not self.expansions_doubled:
                unthinkable = set()
                #
                self.log_success('doubling expansions')
                self.expansions_doubled = True
                self.expansion_doubles = set()
                self.expansion_double_phase = {}
                self.expansion_original = {}
                for pos in self.expansion_locations_list:
                    control_pos = self.init_cheese_position(pos, 115, COMMANDCENTER)
                    if control_pos != self.nowhere:
                        self.log_success('found a spot')
                        self.expansion_doubles.add(control_pos)
                        self.expansion_double_phase[control_pos] = 'A'
                        self.expansion_original[control_pos] = pos
            else: # expansions_doubled
                gotone = False
                for control_pos in self.expansion_doubles:
                    if not gotone:
                        if self.expansion_double_phase[control_pos] == 'E':
                            origin = self.expansion_original[control_pos]
                            for cc in self.structures(COMMANDCENTER).ready:
                                if cc.position == origin:
                                    gotone = True
                                    self.throw_at_spot(ORBITALCOMMAND, origin, 'extreme_spender', 2)
                                    self.expansion_double_phase[control_pos] = 'F'
                for control_pos in self.expansion_doubles:
                    if not gotone:
                        if self.expansion_double_phase[control_pos] == 'D':
                            gotone = True
                            origin = self.expansion_original[control_pos]
                            self.throw_at_spot(COMMANDCENTER, origin, 'extreme_spender', 2)
                            self.expansion_double_phase[control_pos] = 'E'
                for control_pos in self.expansion_doubles:
                    if not gotone:
                        if self.expansion_double_phase[control_pos] in ['B','C']: # someone else can have made pf
                            for cc in self.structures(PLANETARYFORTRESS).ready:
                                if cc.position == control_pos:
                                    gotone = True
                                    origin = self.expansion_original[control_pos]
                                    goal = self.init_cheese_position(origin,12,MISSILETURRET)
                                    self.throw_at_spot(MISSILETURRET, goal, 'extreme_spender', 2)
                                    self.expansion_double_phase[control_pos] = 'D'
                for control_pos in self.expansion_doubles:
                    if not gotone:
                        if self.expansion_double_phase[control_pos] == 'B':
                            for cc in self.structures(COMMANDCENTER).ready:
                                if cc.position == control_pos:
                                    gotone = True
                                    self.throw_at_spot(PLANETARYFORTRESS, control_pos, 'extreme_spender', 2)
                                    self.expansion_double_phase[control_pos] = 'C'
                for control_pos in self.expansion_doubles:
                    if not gotone:
                        if self.expansion_double_phase[control_pos] == 'A':
                            gotone = True
                            self.throw_at_spot(COMMANDCENTER, control_pos, 'extreme_spender', 2)
                            self.expansion_double_phase[control_pos] = 'B'

    #*********************************************************************************************************************

    def may_do_now(self, building,goal) -> bool:
        md = True
        if len(self.buildorder_exe) > 0:
            (bu, go, status) = self.buildorder_exe[0]
            matched = False
            for (bar,martype,pos,dura,owner) in self.preps:
                if (martype == building) and (pos == goal):
                    matched = True
                    if owner == 'follow_planning_exe':
                        if (building,goal) == (bu,go):
                            self.buildorderdelay = 0
                        else:
                            md = False
                            self.log_success('Delay of building a '+building.name+' because of buildorder_exe, after '+bu.name)
                            if self.can_pay(bu):
                                # what are we waiting for?
                                self.buildorderdelay += 1
            if not matched:
                md = False
                self.log_success('Delay of building a '+building.name+' because it is not prepaired.')
        return md


    def delaying_too_much(self):
        if (self.buildorderdelay >= 400): # 400
            self.log_success('Delaying too long. Aborting buildorder_exe[0]')
            self.buildorderdelay = 0
            # delete from thoughts, preps, bags, planning etc.
            (thing,goal,status) = self.buildorder_exe[0]
            self.delete_phantasy(thing,goal)
            # alas now there can be impossible plans
            stable = False
            while not stable:
                stable = True
                todel = []
                totry = self.thoughts.copy()
                self.happy_get_sit()
                for tps in totry:
                    (th,po,st) = tps
                    del self.thoughts[self.thoughts.index(tps)]
                    if not self.happy_can_add(th,po):
                        todel.append((th,po))
                        stable = False
                    self.thoughts.append(tps)
                for (th,po) in todel:
                    self.delete_phantasy(th,po)

    def delete_phantasy(self,thing,goal):
        # delete it from trabu
        found = False
        for scvt in self.goal_of_trabu_scvt:
            itsgoal = self.goal_of_trabu_scvt[scvt]
            itsbuilding = self.structure_of_trabu_scvt[scvt]
            if (itsbuilding,itsgoal) == (thing,goal):
                found = True
                itsscvt = scvt
        if found:
            for scv in self.units(SCV):
                if scv.tag == itsscvt:
                    self.promote(scv,'idler')
            del self.goal_of_trabu_scvt[itsscvt]
            del self.structure_of_trabu_scvt[itsscvt]
        # delete it from ambition
        todel = set()
        for strt in self.ambition_of_strt:
            martype = self.ambition_of_strt[strt]
            for abar in self.structures:
                if abar.tag == strt:
                    pos = abar.position
            if (martype,pos) == (thing,goal):
                found = True
                todel.add(strt)
        for strt in todel:
            del self.ambition_of_strt[strt]
        # delete one from thought
        todel = []
        for (th,go,st) in self.thoughts:
            if (thing == th) and (goal == go):
                found = True
                todel.append((th,go,st))
        for tps in todel:
            del self.thoughts[self.thoughts.index(tps)]
        for nr in range(0,len(self.throwspots)):
            (th,po,status, ow, pri) = self.throwspots[nr]
            if status == 'thought':
                self.throwspots[nr] = (th,po,'new', ow, pri)
        if found:
            self.log_success('Aborted '+thing.name+' '+self.txt(goal))
        else:
            self.log_success('Error aborting ' + thing.name + ' ' + self.txt(goal))
        # a bit rough ...
        if self.builddura_of_thing[thing] < 50:
            if goal == self.somewhere:
                self.log_success('I hesitate to think of this again.')
            else:
                self.make_unthinkable(thing,goal)
                self.log_success('I promise not to think of this again.')
        else:
            self.log_success('I may try this again, this always takes a long time.')
        #
        self.remove_from_planning_etc(thing,goal)


    async def build_thing_tobuildwalk(self,scvt,thing,place,owner) -> bool:
        self.routine = 'build_thing_tobuildwalk'
        didit = False
        if (thing,place,owner) in self.thoughts:
            if thing == COMMANDCENTER:
                didit = await self.build_commandcenter(scvt,place,owner)
            elif thing in self.all_structures_tobuildwalk:
                didit = await self.build_building(scvt,thing,place,owner)
        else: # not in thoughts
            self.log_success('BUG trying to build '+thing.name+' by '+owner+' but it is not in thoughts.')
            self.log_thoughts()
        if didit:
            del self.thoughts[self.thoughts.index((thing,place,owner))]
        return didit

    def supply_check(self,ship) -> bool:
        ok = True
        if ship in self.all_army:
            ok = (self.supply_left >= self.supply_of_army[ship])
        return ok

    async def do_buildandretry(self):
        # all is ready to start building a tobuildwalk. But sometimes the build command fails.
        self.routine = 'do_buildandretry'
        todel = set()
        for items in self.buildandretry:
            (scvt, building, goal, startitera) = items
            if (self.itera<startitera+50):
                if (scvt in self.all_scvt) and ((self.itera - startitera) % 2 == 0):
                    for scv in self.units(SCV):
                        if scv.tag == scvt:
                            if self.job_of_scvt[scvt] == 'builder':
                                if not scv.is_constructing_scv:
                                    # there we go (or go again)
                                    if building == REFINERY:
                                        for gey in self.vespene_geyser:
                                            if gey.position == goal:
                                                self.log_command('scv.build_gas(gey)')
                                                if scv.build_gas(gey):
                                                    self.log_success('prep to egg ' + building.name)
                                                    self.log_workers('begun     ' + building.name + ' ' + self.name(scvt))
                                    else:
                                        self.log_command('scv.build(' + building.name + ',goal)')
                                        if scv.build(building, goal):
                                            self.log_success('prep to egg ' + building.name)
                                            self.log_workers('begun     ' + building.name + ' ' + self.name(scvt))
            else:
                todel.add(items)
        self.buildandretry -= todel
        for (scvt, building, goal, startitera) in todel:
            # either we cucceeded or the build failed
            seen = False
            for (bar, thing, pos, dura) in self.eggs:
                if (thing == building) and (pos == goal):
                    seen = True
            if not seen:
                self.log_success('In buildandretry we discarded a '+building.name)
                for scv in self.units(SCV):
                    if scv.tag == scvt:
                        self.promote(scv,'idler')



    async def start_construction(self):
        # max 1 per iteration to protect can_pay
        self.routine = 'start_construction'
        todo = 1
        for scvt in self.goal_of_trabu_scvt:
            if self.job_of_scvt[scvt] == 'traveller':
                goal = self.goal_of_trabu_scvt[scvt]
                building = self.structure_of_trabu_scvt[scvt] 
                if self.check_techtree(building):
                    if self.can_pay(building):
                        if self.may_do_now(building, goal):
                            for scv in self.units(SCV):
                                if scv.tag == scvt:
                                    if self.near(scv.position,goal,3):
                                        if todo > 0:
                                            todo -= 1
                                            self.promote(scv,'builder')
                                            self.log_workers('beginning '+building.name+' '+self.name(scvt))
                                            self.buildandretry.add((scv.tag, building, goal, self.itera))
        # also, realize an ambition: labs, pfoc, upgr, army
        for oldbuilding in self.structures.ready:
             if oldbuilding.tag in self.idle_structure_tags:  # not in eggs
                if oldbuilding.tag in self.ambition_of_strt: 
                    newbuilding = self.ambition_of_strt[oldbuilding.tag]
                    if self.check_techtree(newbuilding):
                        if self.can_pay(newbuilding):
                            if self.supply_check(newbuilding):
                                pos = oldbuilding.position
                                if self.may_do_now(newbuilding,pos):
                                    if todo > 0:
                                        todo -= 1
                                        del self.ambition_of_strt[oldbuilding.tag]
                                        self.log_success('prep to egg '+newbuilding.name)
                                        self.clean_layout()
                                        if type(newbuilding) == UpgradeId:
                                            await self.do_upgrade(newbuilding,pos)
                                        else:
                                            self.log_command(oldbuilding.name+'.train('+newbuilding.name+')')
                                            oldbuilding.train(newbuilding)


    async def build_building(self,scvt,building,goal,owner) -> bool:
        self.routine = 'build_building'
#       for tobuildwalk buildings except COMMANDCENTER
        didit = False
#       you do not have to wait for minerals and techtree
        if (self.check_future_techtree(building)) or (self.game_phase == 'opening'):
            for scv in self.units(SCV):
                if scv.tag == scvt:
                    self.promote(scv,'traveller')
                    self.goal_of_trabu_scvt[scvt] = goal
                    self.structure_of_trabu_scvt[scvt] = building
                    self.owner_of_trabu_scvt[scvt] = owner
                    self.log_workers('planning  '+building.name+' '+self.name(scvt))
                    self.log_command('scv(AbilityId.MOVE_MOVE,goal)')
                    if scv(AbilityId.MOVE_MOVE,goal):
                        self.log_workers('ordered   '+building.name+' '+self.name(scvt))
                    didit = True
        return didit



    async def build_commandcenter(self,trabu_scvt,goal,owner) -> bool:
        self.routine = 'build_commandcenter'
        didit = False
        building = COMMANDCENTER
#       you do not have to wait for minerals and techtree
        scvt = self.get_near_scvt_to_goodjob(goal)
        for scv in self.units(SCV):
            if scv.tag == scvt:
                self.promote(scv,'escorter')
                self.log_command('scv.attack(goal)')
                scv.attack(goal)
        if len(self.units(MARINE).ready) > 0:
            marin = random.choice(self.units(MARINE).ready)
            self.log_command('marin.attack(goal)')
            marin.attack(goal)
        scvt = trabu_scvt
        for scv in self.units(SCV):
            if scv.tag == scvt:
                self.goal_of_trabu_scvt[scvt] = goal
                self.structure_of_trabu_scvt[scvt] = building
                self.owner_of_trabu_scvt[scvt] = owner
                self.promote(scv,'traveller')
                self.log_command('scv(AbilityId.MOVE_MOVE,goal)')
                scv(AbilityId.MOVE_MOVE, goal)
        didit = True
        # give the cc a cc_destiny
        if goal in self.expansion_locations_list:
            if self.sdist(goal,self.start_location.position) < self.sdist(goal, self.enemyloc):
                # 66 % oc
                if random.randrange(0,3) < 2:
                    self.cc_destiny[goal] = 'oc'
                else:
                    self.cc_destiny[goal] = 'pf'
            else:
                # 33 % oc
                if random.randrange(0,3) < 1:
                    self.cc_destiny[goal] = 'oc'
                else:
                    self.cc_destiny[goal] = 'pf'
        else: # secondary location
            self.cc_destiny[goal] = 'pf'
        return didit



    async def build_thing(self,ambition,place,owner) -> bool:
        # labs, pfoc, upgr, army
        # puts a building in ambition_of_strt, then it will become idle, then be transformed
        # all checks except cradleidle
        self.routine = 'build_thing'
        didit = False
        if ((ambition,self.somewhere,owner) in self.thoughts) or ((ambition,place,owner) in self.thoughts):
            if self.check_techtree(ambition):
                if self.can_pay(ambition):
                    for cc in self.structures.ready:
                        if cc.position == place:
                            if (ambition,cc.type_id) in self.cradle: # against flying
                                if cc.tag not in self.ambition_of_strt:
                                    if self.supply_check(ambition):
                                        if (ambition in self.all_labs):
                                            if not cc.has_add_on:
                                                self.ambition_of_strt[cc.tag] = ambition
                                                self.owner_of_ambistrt[cc.tag] = owner
                                                didit = True
                                        else: # pfoc, upgr, army
                                            self.ambition_of_strt[cc.tag] = ambition
                                            self.owner_of_ambistrt[cc.tag] = owner
                                            didit = True
        else: # not in thoughts
            self.log_success('BUG trying to build '+ambition.name+' by '+owner+' but it is not in thoughts.')
            self.log_thoughts()
        if didit:
            if (ambition,place,owner) in self.thoughts:
                del self.thoughts[self.thoughts.index((ambition,place,owner))]
            else:
                del self.thoughts[self.thoughts.index((ambition, self.somewhere, owner))]
        return didit


    async def do_upgrade(self,upg,place) -> bool:
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
        return didit


#*********************************************************************************************************************
#   army movement routines

    def random_mappoint(self) -> Point2:
        return Point2((random.randrange(self.map_left, self.map_right), random.randrange(self.map_bottom, self.map_top)))


    def go_move(self, bc,goal):
        tag = bc.tag
        self.goal_of_unittag[tag] = goal
        self.last_sd_of_unittag[tag] = self.sdist(bc.position, goal)
        self.shame_of_unittag[tag] = 0
        self.detour_of_unittag[tag] = False
        self.log_command('bc.move(goal)')
        bc.move(goal)

    def go_attack(self, bc,goal):
        tag = bc.tag
        self.goal_of_unittag[tag] = goal
        self.last_sd_of_unittag[tag] = self.sdist(bc.position, goal)
        self.shame_of_unittag[tag] = 0
        self.detour_of_unittag[tag] = False
        self.log_command('bc.attack(goal)')
        bc.attack(goal)

    async def go_jumpormove(self, bc,goal):
        bct = bc.tag
        self.goal_of_unittag[bct] = goal
        self.last_sd_of_unittag[bct] = 0
        self.shame_of_unittag[bct] = 0
        self.detour_of_unittag[bct] = False
        close = self.near(bc.position,goal,15)
        abilities = (await self.get_available_abilities([bc]))[0]
        if (AbilityId.EFFECT_TACTICALJUMP in abilities) and (not close):
            self.log_command('bc(AbilityId.EFFECT_TACTICALJUMP,goal)')
            bc(AbilityId.EFFECT_TACTICALJUMP, goal)
            self.log_army('jumping a bc')
        else:
            self.log_command('bc.move(goal)')
            bc.move(goal)
            self.log_army('moving a bc')

    def no_move(self, bc,maxshame) -> bool:
        nomo = False
        tag = bc.tag
        goal = self.goal_of_unittag[tag]
        sd = self.sdist(bc.position, goal)
        if sd < self.last_sd_of_unittag[tag]:
            self.shame_of_unittag[tag] = max(0, self.shame_of_unittag[tag] - 1)
        elif self.shame_of_unittag[tag] < maxshame:
            self.shame_of_unittag[tag] += 1
        elif self.detour_of_unittag[tag]:
            if bc in self.units.idle:
                self.log_command('bc.move(goal)')
                bc.move(goal)
                self.detour_of_unittag[tag] = False
                self.shame_of_unittag[tag] = 0
        else:
            nomo = True
        self.last_sd_of_unittag[tag] = sd
        return nomo

    def no_move_or_near(self, bc, maxshame, nearity) -> bool:
        nomo = False
        tag = bc.tag
        goal = self.goal_of_unittag[tag]
        sd = self.sdist(bc.position, goal)
        if sd < nearity*nearity:
            nomo = True
        elif sd < self.last_sd_of_unittag[tag]:
            self.shame_of_unittag[tag] = max(0, self.shame_of_unittag[tag] - 1)
        elif self.shame_of_unittag[tag] < maxshame:
            self.shame_of_unittag[tag] += 1
        elif self.detour_of_unittag[tag]:
            if bc in self.units.idle:
                self.log_command('bc.move(goal)')
                bc.move(goal)
                self.detour_of_unittag[tag] = False
                self.shame_of_unittag[tag] = 0
        else:
            nomo = True
        self.last_sd_of_unittag[tag] = sd
        return nomo


    def see_enemies(self):
        for ene in self.enemy_units:
            if ene.type_id not in self.all_workertypes:
                self.seen_enemy_units.add(ene)
        for ene in self.enemy_structures:
            if ene not in self.seen_enemy_structuretypes:
                self.seen_enemy_structuretypes.add(ene.type_id)
                self.write_layout(ene.type_id,ene.position)

    def close_to_a_my_base(self,pos) -> bool:
        clos = False
        for tow in self.all_bases:
            clos = clos or self.near(tow.position,pos,20)
        return clos

    def locally_improved(self,place) -> Point2:
#       verhoog quality met 400 pogingen in de omgeving (maxdist 5)
        bestplace = place
        qual = self.quality_of_bc_position(place)
        for nx in range(-10,10):
            for ny in range(-10,10):
                dx = nx / 2
                dy = ny / 2
                adist = abs(dx) + abs(dy) + max(abs(dx),abs(dy))
                altplace = Point2((place.x + dx, place.y + dy))
                altqual = self.quality_of_bc_position(altplace) - adist
                if altqual > qual:
                    bestplace = altplace
                    qual = altqual
        return bestplace


    def quality_of_bc_position(self,point) -> int:
        # 0=bad, 100= very good, >50 is acceptable
        # should be usable blind
        qual = 0
        if self.attack_type == 'center':
            if self.near(point,self.army_center_point,10):
                qual = 100
        elif self.attack_type == 'arc':
            if self.near(point,self.enemyloc,110) and (not self.near(point,self.enemyloc,90)):
                qual = 100
        elif self.attack_type == 'jumpy':
#           bc.radius+bc.ground_range+hatchery.radius  estimate
            if self.near(point,self.enemy_target_building_loc,10):
                qual = 100
                for ene in self.enemy_structures:
                    if ene.type_id in self.antiair_detector:
#                       bc.radius+spore.air_range+spore.radius  seems to still shoot at 10?!
                        if self.near(point,ene.position,11):
                            qual -= 10
                # bonus for a geyser in sight
                for gas in self.vespene_geyser:
                    if self.near(point,gas.position,7):
                        qual += 1
        return qual

    async def repair_bc(self):
        for bc in self.units(BATTLECRUISER):
            bct = bc.tag
            if self.state_of_unittag[bct] != 'repair':
                torep = (self.state_of_unittag[bct] != 'frozen') and (bc.health <= self.bc_fear)
                torep = torep or (bc.health < 65)
                if torep:
                    self.state_of_unittag[bct] = 'repair'
                    await self.go_jumpormove(bc,self.shipyard)
                    self.bc_fear = max(150, self.bc_fear - 10)
            if self.state_of_unittag[bct] == 'repair':
                # this state is partly a movement
                if self.no_move(bc,8):
                    # it should be repaired. Found anomality, thus next code
                    close = self.near(bc.position, self.shipyard, 15)
                    abilities = (await self.get_available_abilities([bc]))[0]
                    if (AbilityId.EFFECT_TACTICALJUMP in abilities) and (not close) and (bc.health <= self.bc_fear):
                        self.log_command('bc(AbilityId.EFFECT_TACTICALJUMP,self.shipyard)')
                        bc(AbilityId.EFFECT_TACTICALJUMP, self.shipyard)
                        self.log_army('jumping a bc')



    async def attack_with_bc(self):
        self.routine = 'attack_with_bc'
        if self.attack_type == 'jumpy':
            for bc in self.units(BATTLECRUISER):
                bct = bc.tag
                eneseen = False
                for ene in self.enemy_units + self.enemy_structures:
                    if self.near(ene.position, bc.position, 7):
                        eneseen = True
                state = self.state_of_unittag[bct]
                # handle diverse possibilities
                if state == 'repair':
                    pass # it will be repaired
                elif state == 'lazy':
                    if self.quality_of_bc_position(bc.position) <= 50:
                        qual = 0
                        while qual <= 50:
                            place = self.random_mappoint()
                            qual = self.quality_of_bc_position(place)
                        place = self.locally_improved(place)
                        await self.go_jumpormove(bc,place)
                        self.state_of_unittag[bct] = 'travels'
                    else:
                        self.go_move(bc,bc.position)
                        self.state_of_unittag[bct] = 'finetuning'
                elif state == 'travels':
                    # wait for the jump animation to finish, after that its position changes, and its vision returns
                    # or wait until it has flown ower.
                    if self.no_move_or_near(bc,8,2):
                        self.state_of_unittag[bct] = 'finetuning'
                        goal = self.locally_improved(bc.position)
                        self.go_move(bc,goal)
                        self.log_army('bc arrived, moving it a bit')
                elif state == 'finetuning':
                    if self.no_move(bc,8):
                        self.log_army('freezing bc there')
                        self.log_command('bc(AbilityId.HOLDPOSITION_BATTLECRUISER)')
                        bc(AbilityId.HOLDPOSITION_BATTLECRUISER)
                        self.state_of_unittag[bct] = 'frozen'
                elif state == 'frozen':
                    if (not eneseen):
                        self.log_army('unfreezing bc')
                        self.log_command('bc(AbilityId.STOP)')
                        bc(AbilityId.STOP)
                        self.state_of_unittag[bct] = 'towander'
                elif state == 'towander':
                    place = self.random_mappoint()
                    self.go_attack(bc,place)
                    self.state_of_unittag[bct] = 'wandering'
                elif state == 'wandering':
                    if self.no_move(bc,8):
                        self.state_of_unittag[bct] = 'towander'
        elif self.attack_type == 'chaos':
            tp = self.random_mappoint()
        elif self.attack_type == 'arc':
            for bc in self.units(BATTLECRUISER).idle:
                if self.quality_of_bc_position(bc.position) <= 50:
                    bestsd = 99999
                    for tries in range(0,3):
                        tp = self.random_mappoint()
                        while self.quality_of_bc_position(tp) <= 50:
                            tp = self.random_mappoint()
                        sd = self.sdist(bc.position,tp)
                        if sd < bestsd:
                            bestsd = sd
                            besttp = tp
                    tp = besttp
                    self.log_command('bc.attack(tp)')
                    bc.attack(tp)
        elif self.attack_type == 'arcpoint':
            tp = self.enemy_target_building_loc
        elif self.attack_type == 'center':
            tp = self.army_center_point
        elif self.attack_type == 'centerpoint':
            tp = self.enemy_target_building_loc
        if (self.attack_type not in ['jumpy','arc']):
            for bc in self.units(BATTLECRUISER).idle:
                if self.state_of_unittag[bc.tag] != 'repair':
                    if self.quality_of_bc_position(bc.position) <= 50:
                        self.log_command('bc.attack(tp)')
                        bc.attack(tp)
#
#       attack_type changes
        it_changed = False
        if self.attack_type == 'jumpy':
            frozen_or_wandering = 0
            for bct in self.state_of_unittag:
                if self.state_of_unittag[bct] in ['frozen','wandering']:
                    frozen_or_wandering += 1
            if (self.cruisercount<self.lastcruisercount) or (frozen_or_wandering >= 3):
                self.attack_type = 'chaos'
                self.log_army('spreading the army')
                await self.log_attacktype('spreading the army')
                it_changed = True
                self.bestbc_dist_to_goal = 99999
                for bc in self.units(BATTLECRUISER):
                    if self.state_of_unittag[bc.tag] == 'frozen':
                        self.log_command('bc(AbilityId.STOP)')
                        bc(AbilityId.STOP)
                    if self.state_of_unittag[bc.tag] != 'repair':
                        self.state_of_unittag[bc.tag] = 'lazy'
        elif self.attack_type == 'chaos':
            if self.supply_used > 190:
                change_the_type = True
                for bc in self.units(BATTLECRUISER):
                    if bc.tag == self.bestbctag:
                        sd = self.sdist(bc.position, self.enemy_target_building_loc)
                        if (sd < self.bestbc_dist_to_goal):
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
            for ar in self.units(BATTLECRUISER).ready:
                total += 1
                if self.quality_of_bc_position(ar.position) > 50:
                    if ar in self.units(BATTLECRUISER).idle:
                        reached += 1
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
                tp = self.random_mappoint()
                while self.near(tp,self.enemyloc,90) or (not self.near(tp,self.enemyloc,110)):
                    tp = self.random_mappoint()
                self.army_center_point = tp
        elif self.attack_type == 'center':
            reached = 0
            total = 0
            for ar in self.units(BATTLECRUISER).ready:
                total += 1
                if self.quality_of_bc_position(ar.position) > 50:
                    if ar in self.units(BATTLECRUISER).idle:
                        reached += 1
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
                if ene.type_id in [COMMANDCENTER,ORBITALCOMMAND,PLANETARYFORTRESS,HATCHERY,LAIR,HIVE,NEXUS]:
                    allloc.append(ene.position)
            if len(allloc) == 0:
                for ene in self.enemy_structures:
                    allloc.append(ene.position)
            if len(allloc) == 0:
                self.enemy_target_building_loc = self.enemyloc
            else:
                self.enemy_target_building_loc = random.choice(allloc)


    async def attack_with_rest(self):
        self.routine = 'attack_with_rest'
        # the raven should attack the best battlecruiser
        for rv in self.units(RAVEN).idle:
            for bc in self.units(BATTLECRUISER).ready:
                if bc.tag == self.bestbctag:
                    self.log_command('rv.attack(bc)')
                    rv.attack(bc)
                    self.log_army('raven will follow a bc')
        # vikings should defend viking targets
        # flying random defensive, although this could give away info
        reached = 0
        for vik in self.units(VIKINGFIGHTER):
            if vik.tag not in self.shame_of_unittag:
                self.log_command('vik.attack(self.viking_goal)')
                self.go_attack(vik,self.viking_goal)
            if self.no_move_or_near(vik,7,5):
                reached += 1
        if reached * 4 > 3 * len(self.units(VIKINGFIGHTER)):
            targetpos = self.nowhere
            for ene in self.enemy_units:
                if (ene.type_id in self.viking_targets):
                    if self.close_to_a_my_base(ene.position):
                        targetpos = ene.position
            if targetpos == self.nowhere:
                if len(self.all_bases) > 0:
                    bas = random.choice(self.all_bases)
                    basp = bas.position
                else:
                    basp = self.start_location
                targetpos = Point2((basp.x+random.randrange(-20,20),basp.y+random.randrange(-20,20)))
            self.viking_goal = targetpos
            self.log_army('viking goal set')
            for vik in self.units(VIKINGFIGHTER):
                self.go_attack(vik,self.viking_goal)
        # suicider scvs
        if self.count_of_job['suicider'] > 0:
            for scv in self.units(SCV).idle:
                scvt = scv.tag
                if scvt in self.all_scvt:
                    if self.job_of_scvt[scvt] == 'suicider':
                        place = self.mineral_field.random.position # mined out
                        self.log_command('scv.attack(place)')
                        scv.attack(place)
        # marines
        tp = self.mineral_field.random.position # mined out
        sent = 0
        for mar in self.units(MARINE).idle:
            if mar.tag not in self.special_tags:
                sent += 1
                self.log_command('mar.attack(tp)')
                mar.attack(tp)
        if sent > 0:
            self.log_army(' with marine '+str(sent))
        # marauders
        reached = 0
        for mar in self.units(MARAUDER):
            if mar.tag not in self.shame_of_unittag:
                self.log_command('mar.attack(self.marauder_goal)')
                self.go_attack(mar,self.marauder_goal)
                self.last_health_of_maraudert[mar.tag] = mar.health
            if mar.health != self.last_health_of_maraudert[mar.tag]:
                altpos = Point2((mar.position.x+random.randrange(-5,5)/5,mar.position.y+random.randrange(-5,5)/5))
                self.log_command('mar.move(altpos)')
                mar.move(altpos)
                self.last_health_of_maraudert[mar.tag] = mar.health
                self.detour_of_unittag[mar.tag] = True
            if self.no_move(mar,15):
                reached += 1
        if reached * 4 > 3 * len(self.units(MARAUDER)):
            self.marauder_goal = self.mineral_field.random.position # mined out
            if self.random_chance(5):
                allloc = []
                for ene in self.enemy_structures:
                    allloc.append(ene.position)
                if len(allloc) > 0:
                    self.marauder_goal = random.choice(allloc)
            self.log_army('marauder goal set')
            for mar in self.units(MARAUDER):
                self.go_attack(mar,self.marauder_goal)


    async def siege_tanks(self):
        self.routine = 'siege_tanks'
        # siege tank at a random own base
        for tnk in self.units(SIEGETANK) + self.units(SIEGETANKSIEGED):
            if tnk.tag not in self.special_tags:
                tnkt = tnk.tag
                if tnkt not in self.state_of_unittag:
                    self.state_of_unittag[tnkt] = 'new'
                elif self.state_of_unittag[tnkt] == 'new':
                    # get a good tank siege position
                    if (self.opening_name == 'cocoon') and (len(self.structures(BUNKER)) == 2) and (self.random_chance(2)):
                        goal = self.cheese3_prison_pos
                    elif len(self.all_bases) == 0:
                        goal = self.start_location.position
                    else:
                        tow = random.choice(self.all_bases)
                        # halfheartedly prevent all tanks in startbase
                        if tow.position == self.start_location.position:
                            tow = random.choice(self.all_bases)
                        # at first base, protect wall, at other bases, protect the tank
                        if tow.position == self.start_location.position:
                            goal = tow.position.towards(self.game_info.map_center, 3)
                        else:
                            goal = tow.position.towards(self.game_info.map_center, -3)
                    self.put_on_the_grid(MISSILETURRET, goal)
                    goal = self.function_result_Point2
                    place = goal
                    tries = 0
                    radius = 0
                    ok = False
                    while (not ok):
                        if tries == radius * radius:
                            radius += 1
                        tries += 1
                        x = goal.x + random.randrange(-radius, radius)
                        y = goal.y + random.randrange(-radius, radius)
                        place = Point2((x, y))
                        ok = self.check_layout(MISSILETURRET, place)
                        if self.near(place,self.start_location.position,20):
                            ok = ok and self.near(place, self.homeramp_pos, 16)
                            # expect the ramp near start
                    # Mark as used.
                    self.write_layout(MISSILETURRET, place)
                    self.tankplaces.add(place)
                    self.go_attack(tnk, place)
                    self.state_of_unittag[tnkt] = 'moving'
                elif self.state_of_unittag[tnkt] == 'moving':
                    if self.no_move_or_near(tnk,35,1): # yes there is a map with over 30 detour
                        self.log_command('tnk(AbilityId.SIEGEMODE_SIEGEMODE)')
                        tnk(AbilityId.SIEGEMODE_SIEGEMODE)
                        self.state_of_unittag[tnkt] = 'sieged'
                elif self.state_of_unittag[tnkt] == 'sieged':
                    hasbase = False
                    for cc in self.all_bases:
                        if self.near(tnk.position, cc.position, self.miner_bound):
                            hasbase = True
                    hasmins = False
                    for mim in self.mineral_field:
                        if self.near(tnk.position, mim.position, 16):
                            hasmins = True
                    hasbunkers = 0
                    for bu in self.structures(BUNKER):
                        if self.near(tnk.position, bu.position, 8):
                            hasbunkers += 1
                    if not (hasbase and hasmins):
                        if hasbunkers < 2:
                            self.log_command('tnk(AbilityId.UNSIEGE_UNSIEGE)')
                            tnk(AbilityId.UNSIEGE_UNSIEGE)
                            self.state_of_unittag[tnkt] = 'unsieging'
                elif self.state_of_unittag[tnkt] == 'unsieging':
                    if tnk in self.units(SIEGETANK):
                        self.state_of_unittag[tnkt] = 'new'



    async def use_mine(self):
        self.routine = 'use_mine'
        for wm in self.units(WIDOWMINE).ready:
            normal = True
            if (wm in self.cheese_mines):
                normal = False
            if self.cheese_factory is not None:
                if self.near(wm.position,self.cheese_landing_pos,7):
                    normal = False
            if normal:
                wmt = wm.tag
                if wmt in self.goal_of_unittag:
                    if self.no_move_or_near(wm,17,2) or (wm.health < wm.health_max):
                        self.log_command('wm(AbilityId.BURROWDOWN_WIDOWMINE)')
                        wm(AbilityId.BURROWDOWN_WIDOWMINE)
                else: # find a goal
                    enemims = set()
                    for mim in self.mineral_field:
                        if self.near(mim.position, self.enemyloc, 60):
                            enemims.add(mim)
                    if len(enemims) == 0:
                        for mim in self.mineral_field:
                            enemims.add(mim)
                    # no code for map-mined-out
                    # try to avoid cannons and spores
                    tries = 0
                    goodpoint = False
                    while (not goodpoint) and (tries < 20):
                        tries += 1
                        enemim = random.choice(tuple(enemims))
                        point = enemim.position.towards(self.game_info.map_center, -1)
                        goodpoint = True
                        for ene in self.enemy_structures:
                            if ene.type_id in self.antiair_detector:
                                if self.near(point,ene.position,8):
                                    goodpoint = False
                        nearmines = 0
                        for own in self.units(WIDOWMINEBURROWED):
                            if self.near(own.position,point,10):
                                nearmines +=1
                        if nearmines > 1:
                            goodpoint = False
                    self.go_move(wm,point)                

    async def fire_yamato(self):
        self.routine = 'fire_yamato'
        for bc in self.units(BATTLECRUISER).ready:
            # get targets and dangersum
            hatemax = 0
            dangersum = 0
            targets = set()
            for kind in self.bcenemies:
                hate = self.hate_of_bcenemy[kind]
                danger = self.danger_of_bcenemy[kind]
                for ene in self.enemy_units(kind):
                    if danger > 0:
                        if self.near(ene.position,bc.position,10):
                            dangersum += danger
                            adanger = ene.position
                    if hate > 0:
                        if self.near(ene.position, bc.position, 8):
                            if hate > hatemax:
                                targets = set()
                                hatemax = hate
                            if hate >= hatemax:
                                targets.add(ene)
            # dangersum must be divided by near bcs
            my_power = 0
            for myn in self.units:
                if self.near(bc.position, myn.position, 10):
                    my_power += self.unit_power(myn.type_id)
            for kind in [PLANETARYFORTRESS, MISSILETURRET, BUNKER]:
                for myn in self.structures(kind):
                    if self.near(bc.position, myn.position, 10):
                        my_power += self.unit_power(myn.type_id)
            myfactor = my_power / self.unit_power(BATTLECRUISER)
            dangersum = dangersum / myfactor
            # choose target, prefer lasttarget
            if hatemax > 0:
                if bc in self.lasttarget_of_bc:
                    if self.lasttarget_of_bc[bc] in targets:
                        target = self.lasttarget_of_bc[bc]
                    else:
                        target = random.choice(tuple(targets))
                else:
                    target = random.choice(tuple(targets))
            # if too dangerous, move away from adanger
            if (dangersum >= 100):
                away = Point2((1.5*bc.position.x-0.5*adanger.x, 1.5*bc.position.y-0.5*adanger.y))
                self.log_command('bc.move(away)')
                bc.move(away)
                self.detour_of_unittag[bc.tag] = True
            # maybe shoot
            if (hatemax > 0) and (dangersum < 100):
                if bc in self.lasttarget_of_bc:
                    if target != self.lasttarget_of_bc[bc]:
                        if (self.attack_type != 'jumpy'):
                            self.log_command('bc(AbilityId.SMART, target)')
                            bc(AbilityId.SMART, target)
                            self.detour_of_unittag[bc.tag] = True
            # set lasttarget
            if hatemax > 0:
                self.lasttarget_of_bc[bc] = target
            # yamato
            if (hatemax > 2) and (dangersum < 100):
                abilities = (await self.get_available_abilities([bc]))[0]
                if AbilityId.YAMATO_YAMATOGUN in abilities:
                    self.log_command('bc(AbilityId.YAMATO_YAMATOGUN,'+target.name+')')
                    bc(AbilityId.YAMATO_YAMATOGUN, target)
                    # the yamato stops the movement, so mark detour.
                    self.detour_of_unittag[bc.tag] = True
        for ra in self.units(RAVEN).ready:
            found = False
            for kind in self.bcenemies:
                for ene in self.enemy_units(kind):
                    if self.near(ene.position,ra.position,9):
                        target = ene
                        found = True
            if found:
                abilities = (await self.get_available_abilities([ra]))[0]
                if AbilityId.EFFECT_ANTIARMORMISSILE in abilities:
                    self.log_command('ra(AbilityId.EFFECT_ANTIARMORMISSILE,'+target.name+')')
                    ra(AbilityId.EFFECT_ANTIARMORMISSILE, target)




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


    def unit_power(self,thing) -> int:
        # estimate of fighting power
        cost = self.calculate_unit_value(thing)
        power = cost.minerals+2*cost.vespene
        return power

    async def worker_defence(self):
        self.routine = 'worker_defence'
        for tow in self.all_bases:
            if tow.tag not in self.special_tags:
                # calc enemies and enemy_power
                enemies = []
                enemy_power = 0
                cx = 0
                cy = 0
                n_enemies = 0
                for ene in self.enemy_units + self.enemy_structures:
                    if self.belongs_to(tow.position,ene.position):
                        if not ene.is_flying:
                            enemies.append(ene)
                        enemy_power += self.unit_power(ene.type_id)
                        cx = cx + ene.position.x
                        cy = cy + ene.position.y
                        n_enemies += 1
                if n_enemies > 0:
                    center_enemies = Point2((cx / n_enemies, cy / n_enemies))
                # calc my_power
                my_power = 0
                for myn in self.units:
                    if self.belongs_to(tow.position,myn.position):
                        my_power += self.unit_power(myn.type_id)
                for kind in [PLANETARYFORTRESS,MISSILETURRET,BUNKER]:
                    for myn in self.structures(kind):
                        if self.belongs_to(tow.position,myn.position):
                            my_power += self.unit_power(myn.type_id)
                if my_power * 3 < enemy_power * 2:
                    # no hope
                    self.log_success('eeeeek!!!')
                    away = Point2((1.5*tow.position.x-0.5*center_enemies.x, 1.5*tow.position.y-0.5*center_enemies.y))
                    for myscv in self.units(SCV):
                        if self.belongs_to(tow.position,myscv.position):
                            job = self.job_of_scvt[myscv.tag]
                            if (job in self.bad_jobs + self.no_jobs) and (job != 'fleeer'):
                                self.promote(myscv,'fleeer')
                                self.log_command('my_scv.move(away)')
                                myscv.move(away)
                                # at the moment this does not cooperate with the fleeer handling
                                # idea per expansionloc a state 'falling'
                else:
                    if len(enemies) > 0:
                        wished_defenders = enemy_power/50 + 2
                    else:
                        wished_defenders = 0
                    # calc defenders
                    defenders = set()
                    for myscv in self.units(SCV):
                        scvt = myscv.tag
                        if scvt in self.all_scvt:
                            job = self.job_of_scvt[scvt]
                            if (job == 'defender'):
                                # wider than belongs_to, to allow stop chasing
                                if self.near(tow.position, myscv.position,25):
                                    defenders.add(myscv)
                    if len(defenders) > 0:
                        # dismiss veterans
                        veterans = set()
                        for myscv in defenders:
                            if myscv.health < 12:
                                veterans.add(myscv)
                                self.promote(myscv,'fleeer')
                        defenders -= veterans
                    if len(enemies) > 0:
                        # get new defenders
                        toget = wished_defenders - len(defenders)
                        if toget > 0:
                            candidates = set()
                            for myscv in self.units(SCV):
                                if self.belongs_to(tow.position,myscv.position):
                                    if myscv.health >= 12:
                                        scvt = myscv.tag
                                        if scvt in self.all_scvt:
                                            job = self.job_of_scvt[scvt]
                                            if job in (self.bad_jobs + self.no_jobs):
                                                candidates.add(myscv)
                            while (toget > 0) and (len(candidates) > 0):
                                bestsd = 99999
                                for myscv in candidates:
                                    sd = self.sdist(myscv.position,center_enemies)
                                    if sd < bestsd:
                                        bestscv = myscv
                                        bestsd = sd
                                myscv = bestscv
                                scvt = myscv.tag
                                candidates.remove(myscv)
                                # promote to defender and let idle
                                toget -= 1
                                self.promote(myscv,'defender')
                                if not myscv.is_idle:
                                    self.log_command('myscv(AbilityId.STOP)')
                                    myscv(AbilityId.STOP)
                    if (len(defenders) > wished_defenders) or (len(enemies) == 0):
                        # dismiss defenders
                        todel = len(defenders) - wished_defenders
                        if len(enemies) == 0:
                            todel = len(defenders)
                        for myscv in defenders:
                            if (todel > 0):
                                todel -= 1
                                self.promote(myscv,'idler')
                                self.log_command('myscv.move(tow.position)')
                                myscv.move(tow.position)
                    if len(enemies) > 0:
                        # decide if it is grouped
                        grouped = False
                        for ene in enemies:
                            if self.near(center_enemies,ene.position,3):
                                grouped = True
                        if grouped:
                            # group attack
                            for myscv in defenders:
                                self.log_command('myscv.attack(center_enemies)')
                                myscv.attack(center_enemies)
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
            thing = MARINE
            if (self.cheese_phase >= 'B') and (self.cheese_phase < 'Z'):
                if self.cheese_barracks in self.structures(BARRACKS).ready.idle:
                    if self.can_pay(thing):
                        if self.supply_check(thing):
                            self.log_command('self.cheese_barracks.train(thing)')
                            self.cheese_barracks.train(thing)
                            self.cheese_marine_count += 1
        if self.cheese_tank_count < 1:
            thing = SIEGETANK
            if (self.cheese_phase >= 'K') and (self.cheese_phase < 'Z'):
                if self.cheese_factory in self.structures(FACTORY).ready.idle:
                    if self.can_pay(thing):
                        if self.supply_check(thing):
                            self.log_command('self.cheese_factory.train(thing)')
                            self.cheese_factory.train(thing)
                            self.cheese_tank_count += 1
        if self.cheese_mine_count < 2:
            thing = WIDOWMINE
            if (self.cheese_phase >= 'N') and (self.cheese_phase < 'Z'):
                if self.cheese_factory in self.structures(FACTORY).ready.idle:
                    if self.can_pay(thing):
                        if self.supply_check(thing):
                            self.log_command('self.cheese_factory.train(thing)')
                            self.cheese_factory.train(thing)
                            self.cheese_mine_count += 1





    async def bunkercheese(self):
        self.routine = 'bunkercheese'
        # break off the cheese?
        if (self.cheese_phase >= 'B') and (self.cheese_phase < 'Z'):
            startedbuildings = 0
            for barra in self.structures(BARRACKS).ready:
                if barra.position != self.cheese_barracks_pos:
                    if self.near(barra.position,self.cheese_landing_pos,7):
                        startedbuildings += 1
            for bunk in self.structures(BUNKER):
                if bunk.position == self.cheese_bunker_pos:
                    self.cheese_bunker = bunk
                    startedbuildings += 1
            if startedbuildings == 0:
                self.cheese_phase = 'Y cleanup'
        # follow a large series of phases
        if self.cheese_phase == 'Anobunker':
            if self.cheese_scv is None:
                self.cheese_phase = 'Y cleanup'
            elif self.add_thought(BUNKER, self.cheese_bunker_pos,'bunkercheese'):
                self.cheese_phase = 'Athought'
        elif self.cheese_phase == 'Athought':
            if await self.build_thing_tobuildwalk(self.cheese_scv.tag, BUNKER, self.cheese_bunker_pos,'bunkercheese'):
                self.cheese_bunker_last_health = 0
                self.cheese_phase = 'A'
        elif self.cheese_phase == 'A':
            for barra in self.structures(BARRACKS):
                if barra.position == self.cheese_barracks_pos:
                    self.cheese_barracks = barra
                    self.special_tags.add(barra.tag)
            # wait for landed barracks and building bunker
            startedbuildings = 0
            for barra in self.structures(BARRACKS).ready:
                if barra.position != self.cheese_barracks_pos:
                    if self.near(barra.position,self.cheese_landing_pos,7):
                        startedbuildings += 1
            for bunk in self.structures(BUNKER):
                if bunk.position == self.cheese_bunker_pos:
                    self.cheese_bunker = bunk
                    startedbuildings += 1
            if startedbuildings == 2:
                for anscv in self.units(SCV):
                    scvt = anscv.tag
                    if scvt in self.goal_of_trabu_scvt:
                        if self.goal_of_trabu_scvt[scvt] == self.cheese_bunker_pos:
                            self.promote(anscv,'cheeser')
                            self.cheese_scv = anscv
                            self.special_tags.add(self.cheese_scv.tag)
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
                            self.special_tags.add(self.cheese_scv.tag)
                            self.scout_tag = self.notag
                            self.promote(scv,'cheeser')
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
            self.cheese_frames += 1
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
            # wait for the factory and rally it
            for facta in self.structures(FACTORY).ready:
                if facta.position == self.cheese_factory_pos:
                    self.cheese_factory = facta
                    point = self.cheese_tank_pos
                    self.log_command('self.cheese_factory(AbilityId.RALLY_BUILDING, point)')
                    self.cheese_factory(AbilityId.RALLY_BUILDING, point)
                    self.cheese_phase = 'I'
        elif self.cheese_phase == 'I':
            # make a lab
            if self.can_pay(FACTORYTECHLAB):
                self.log_command('self.cheese_factory.train(FACTORYTECHLAB)')
                self.cheese_factory.train(FACTORYTECHLAB)
                self.cheese_phase = 'J'
        elif self.cheese_phase == 'J':
            for tl in self.structures(FACTORYTECHLAB).ready:
                self.cheese_phase = 'K'
        elif self.cheese_phase == 'K':
            # wait for tank to be made
            if self.cheese_tank_count == 1:
                for st in self.units(SIEGETANK).ready:
                    if self.near(st.position,self.cheese_factory_pos,7):
                        self.cheese_tank = st
                        self.special_tags.add(self.cheese_tank.tag)
                        # toward cheese_tank_pos
                        self.log_command('self.cheese_tank.attack(self.cheese_tank_pos)')
                        self.cheese_tank.attack(self.cheese_tank_pos)
                        # fly the factory in
                        bu = self.cheese_factory
                        self.home_of_flying_struct[bu.tag] = self.cheese_landing_pos
                        self.landings_of_flying_struct[bu.tag] = 0
                        self.log_success('up FACTORY')
                        self.log_command('bu(AbilityId.LIFT')
                        bu(AbilityId.LIFT)
                        # next phase
                        self.cheese_phase = 'L'
        elif self.cheese_phase == 'L':
            # wait for tank to arrive, then siege it
            if self.cheese_tank in self.units(SIEGETANK).idle:
                self.log_command('self.cheese_tank(AbilityId.SIEGEMODE_SIEGEMODE)')
                self.cheese_tank(AbilityId.SIEGEMODE_SIEGEMODE)
                self.cheese_phase = 'M'
        elif self.cheese_phase == 'M':
            # fly the barracks out
            bu = self.cheese_barracks
            self.home_of_flying_struct[bu.tag] = self.cheese_factory_pos
            self.landings_of_flying_struct[bu.tag] = 0
            self.log_success('up BARRACKS')
            self.log_command('bu(AbilityId.LIFT')
            bu(AbilityId.LIFT)
            self.cheese_phase = 'N'
        elif self.cheese_phase == 'N':
            # wait for landing of factory and rally it
            if self.cheese_factory in self.structures(FACTORY):
                # cheese_factory.position is wrong the old position
                point = self.cheese_bunker.position.towards(self.enemyloc,2)
                self.log_command('self.cheese_factory(AbilityId.RALLY_BUILDING, point)')
                self.cheese_factory(AbilityId.RALLY_BUILDING, point)
                self.cheese_phase = 'O'
        elif self.cheese_phase == 'O':
            # wait for 2 cheese_mines
            for wm in self.units(WIDOWMINE).ready:
                wmt = wm.tag
                if self.near(wm.position,self.cheese_landing_pos,7):
                    if wm not in self.cheese_mines:
                        self.cheese_mines.add(wm)
                        found = False
                        while not found:
                            mim = self.mineral_field.random
                            if self.near(mim.position, self.enemyloc, self.miner_bound):
                                goal = mim.position.towards(self.game_info.map_center,-2)
                                found = True
                        self.burrowpos_of_wmt[wmt] = goal
                        pole = self.get_near_pole(goal)
                        self.homepole_of_wmt[wmt] = pole
                        pole = self.get_near_pole(wm.position)
                        pole = (pole + 1) % len(self.scout_pos)
                        self.pole_of_wmt[wmt] = pole
                        self.phase_of_wmt[wmt] = 'flee'
                        if len(self.cheese_mines) < 2:
                            self.log_command('wm(AbilityId.BURROWDOWN_WIDOWMINE)')
                            wm(AbilityId.BURROWDOWN_WIDOWMINE)
            if len(self.cheese_mines) == 2:
                for wm in self.cheese_mines:
                    wmt = wm.tag
                    if (wm in self.units(WIDOWMINEBURROWED)):
                        self.log_command('wm(AbilityId.BURROWUP_WIDOWMINE)')
                        wm(AbilityId.BURROWUP_WIDOWMINE)
                    pole = self.pole_of_wmt[wmt]
                    goal = self.scout_pos[pole]
                    self.go_move(wm,goal)
                self.cheese_phase = 'P'
        elif self.cheese_phase == 'P':
            # manage cheesemines
            for wm in self.cheese_mines:
                wmt = wm.tag
                if self.phase_of_wmt[wmt] == 'attack':
                    if (wm in self.units(WIDOWMINE)):
                        if self.no_move_or_near(wm,4,1):
                            self.log_command('wm(AbilityId.BURROWDOWN_WIDOWMINE)')
                            wm(AbilityId.BURROWDOWN_WIDOWMINE)
                    if (wm in self.units(WIDOWMINEBURROWED)):
                        abilities = (await self.get_available_abilities([wm]))[0]
                        if AbilityId.WIDOWMINEATTACK_WIDOWMINEATTACK not in abilities:
                            # it fired!
                            self.log_command('wm(AbilityId.BURROWUP_WIDOWMINE)')
                            wm(AbilityId.BURROWUP_WIDOWMINE)
                            self.phase_of_wmt[wmt] = 'flee'
                            pole = self.homepole_of_wmt[wmt]
                            pole = (pole + 1) % len(self.scout_pos)
                            self.pole_of_wmt[wmt] = pole
                            goal = self.scout_pos[pole]
                            self.go_move(wm,goal)
                if self.phase_of_wmt[wmt] == 'flee':
                    pole = self.pole_of_wmt[wmt]
                    goal = self.scout_pos[pole]
                    if self.no_move_or_near(wm,4,4):
                        pole = (pole + 1) % len(self.scout_pos)
                        if pole == self.homepole_of_wmt[wmt]:
                            goal = self.burrowpos_of_wmt[wmt]
                            self.phase_of_wmt[wmt] = 'attack'
                        else:
                            goal = self.scout_pos[pole]
                        self.pole_of_wmt[wmt] = pole
                        self.go_move(wm,goal)
            if len(self.cheese_mines) == 0: #todo living
                self.cheese_phase = 'Y cleanup'
        elif self.cheese_phase == 'Y cleanup':
            # clean up
            if (self.cheese_scv is not None) and (self.cheese_scv in self.units(SCV)):
                self.special_tags.remove(self.cheese_scv.tag)
                self.promote(self.cheese_scv,'idler')
            self.cheese_scv = None
            if self.cheese_tank in self.units(SIEGETANKSIEGED):
                self.log_command('self.cheese_tank(AbilityId.UNSIEGE_UNSIEGE)')
                self.cheese_tank(AbilityId.UNSIEGE_UNSIEGE)
                self.log_command('self.cheese_tank.attack(self.shipyard)')
                self.cheese_tank.attack(self.shipyard)
            if self.cheese_tank is not None:
                if self.cheese_tank.tag in self.special_tags:
                    self.special_tags.remove(self.cheese_tank.tag)
            self.cheese_tank = None
            if self.cheese_barracks in self.units(BARRACKS):
                bu = self.cheese_barracks
                if bu.tag in self.special_tags:
                    self.special_tags.remove(bu.tag)
                self.log_command('bu(AbilityId.CANCEL)')
                bu(AbilityId.CANCEL)
                self.home_of_flying_struct[bu.tag] = self.wall_barracks_pos
                self.landings_of_flying_struct[bu.tag] = 0
                self.log_success('up CHEESE_BARRACKS')
                self.log_command('bu(AbilityId.LIFT')
                bu(AbilityId.LIFT)
            self.cheese_barracks = None
            self.cheese_mines = set()
            self.log_success('ending the bunkercheese')
            self.cheese_phase = 'Z'
        #
        self.log_cheese()

    ################ cheese2 ########################

    async def bunkercheese2(self):
        self.routine = 'bunkercheese2'
        # hiding_spot
        if bunker_if.hiding_spot is None:
            place = self.random_mappoint()
            while self.near(place, self.enemyloc, 50) or self.near(place, self.start_location.position, 50):
                place = self.random_mappoint()
            bunker_if.hiding_spot = place
        if self.game_choice[30]:
            if not (self.game_choice[2] or self.game_choice[3] or self.game_choice[7] or self.game_choice[9]): # tight openings
                if (self.we_started_amount(BUNKER) < 2 * len(self.all_bases)) and (len(self.units(MARINE)) > 0):
                    todo = 1
                    for goal in self.expansion_locations_list:
                        if goal not in self.cheese2_triedexp:
                            if todo > 0:
                                todo -= 1
                                self.cheese2_triedexp.add(goal)
                                pos = self.init_cheese_position(goal,79,BUNKER)
                                self.throw_at_spot(BUNKER,pos,'bunkercheese2',1)
                                self.cheese2_bunkspots.add(pos)
                                self.throw_somewhere(MARINE,'bunkercheese2',1)
                for bu in self.structures(BUNKER):
                    if bu.position in self.cheese2_bunkspots:
                        bunker_if.bunkertags.add(bu.tag)
                if len(bunker_if.marinetags) < 2 * len(bunker_if.bunkertags):
                    todo = 1
                    for mar in self.units(MARINE):
                        if todo > 0:
                            todo -= 1
                            bunker_if.marinetags.add(mar.tag)
                            self.special_tags.add(mar.tag)
                if len(bunker_if.bunkertags) > 0:
                    if len(bunker_if.scvtags) < 2:
                        scvt = self.get_near_scvt_to_goodjob(self.start_location.position)
                        for scv in self.units(SCV):
                            if scv.tag == scvt:
                                self.promote(scv,'cheeser')
                                bunker_if.scvtags.add(scv.tag)
                # salvage bunker
                for tow in self.expansion_locations_list:
                    # calc static my_power
                    my_power = 0
                    for kind in [SIEGETANKSIEGED,WIDOWMINEBURROWED]:
                        for myn in self.units(kind):
                            if self.belongs_to(tow.position,myn.position):
                                my_power += self.unit_power(myn.type_id)
                    for kind in [PLANETARYFORTRESS]:
                        for myn in self.structures(kind):
                            if self.belongs_to(tow.position,myn.position):
                                my_power += self.unit_power(myn.type_id)
                    if my_power > 200:
                        for bun in self.structures(BUNKER):
                            if self.belongs_to(tow.position,bun.position):
                                # salvage
                                for mar in bun.passengers:
                                    if mar.tag in self.special_tags:
                                        self.special_tags.remove(mar.tag)
                                await bunker_if.salvage(bun)
                if self.supply_used > 190:
                    # bunkers not useful any more
                    mintag = self.notag
                    first = True
                    for bun in self.structures(BUNKER):
                        if first:
                            mintag = bun.tag
                            first = False
                        mintag = min(bun.tag,mintag)
                    for bun in self.structures(BUNKER):
                        if bun.tag == mintag:
                            # salvage
                            for mar in bun.passengers:
                                if mar.tag in self.special_tags:
                                    self.special_tags.remove(mar.tag)
                            await bunker_if.salvage(bun)


    ################ cheese3 ########################


    async def cheese3_internals(self):
        # name cheesebunker
        for bu in self.structures(BUNKER):
            if bu.position == self.cheese3_bunker_pos:
                self.cheese3_bunker = bu
        # died scvs
        todel = set()
        for scv in self.cheese3_scvs:
            if scv not in self.units(SCV):
                todel.add(scv)
        self.cheese3_scvs -= todel
        # get scvs
        if len(self.cheese3_scvs) < 2:
            scvt = self.get_near_scvt_to_goodjob(self.cheese3_prison_pos)
            for scv in self.units(SCV):
                if scv.tag == scvt:
                    self.promote(scv,'cheeser')
                    scv.move(self.cheese3_prison_pos)
                    self.cheese3_scvs.add(scv)
        # move scvs
        for scv in self.cheese3_scvs:
            if scv.is_idle:
                if not self.near(scv.position, self.cheese3_prison_pos, 3):
                    scv.move(self.cheese3_prison_pos)
        # move marines
        if self.cheese3_bunker in self.structures(BUNKER): # also when building
            if len(self.cheese3_bunker.passengers) < 4:
                for mari in self.units(MARINE):
                    if not self.near(mari.position, self.cheese3_bunker_pos, 7):
                        mari.move(self.cheese3_bunker_pos)
            else: # bunker full
                for mari in self.units(MARINE):
                    if self.near(mari.position, self.cheese3_bunker_pos, 7):
                        mari.attack(self.shipyard)
        # load marines
        if self.cheese3_bunker in self.structures(BUNKER).ready:
            if len(self.cheese3_bunker.passengers) < 4:
                for mari in self.units(MARINE):
                    if self.near(mari.position, self.cheese3_bunker_pos, 7):
                        self.log_command('self.cheese3_bunker(AbilityId.LOAD_BUNKER,mari)')
                        self.cheese3_bunker(AbilityId.LOAD_BUNKER, mari)
        # rebuild bunker
        if self.cheese3_bunker not in self.structures(BUNKER):
            if not self.we_started_a(BUNKER):
                self.throw_at_spot_if_rich(BUNKER, self.cheese3_bunker_pos, 'do_pf_rush',1)
        # repair bunker
        if self.cheese3_bunker in self.structures(BUNKER).ready:
            if self.cheese3_bunker.health < self.cheese3_bunker.health_max:
                for scv in self.cheese3_scvs:
                    if scv.is_idle:
                        scv.repair(self.cheese3_bunker)


    async def do_pf_rush(self):
        self.routine = 'do_pf_rush'
        if self.opening_name == 'pf-rush':
            if self.cheese3_phase == 'A':
                # while (nothing)
                # continue
                for bu in self.structures(BARRACKS):
                    if bu.position == self.cheese3_barracks_pos:
                        # init (barracks is constructing)
                        self.cheese3_barracks = bu
                        self.cheese3_phase = 'B'
            elif self.cheese3_phase == 'B':
                # while (barracks is constructing)
                #clean
                if self.cheese3_barracks not in self.structures(BARRACKS):
                    self.cheese3_phase = 'Y'
                # continue
                for bu in self.structures(BUNKER):
                    if bu.position == self.cheese3_bunker_pos:
                        # init (bunker is constructing)
                        self.cheese3_bunker = bu
                        for scvt in self.goal_of_trabu_scvt:
                            if self.goal_of_trabu_scvt[scvt] == self.cheese3_bunker_pos:
                                for scv in self.units(SCV):
                                    if scv.tag == scvt:
                                        self.cheese3_scvs.add(scv)
                                        # still builder, late rto be cheeser
                        self.cheese3_phase = 'C'
            elif self.cheese3_phase == 'C':
                # while (bunker is constructing)
                await self.cheese3_internals()
                #clean
                if self.cheese3_barracks not in self.structures(BARRACKS):
                    self.cheese3_phase = 'Y'
                # continue
                for bu in self.structures(BUNKER).ready:
                    if bu.position == self.cheese3_bunker_pos:
                        # init (bunker ready)
                        self.cheese3_barracks(AbilityId.RALLY_BUILDING,self.cheese3_bunker)
                        for scv in self.cheese3_scvs:
                            self.promote(scv,'cheeser')
                            scv.move(self.cheese3_prison_pos)
                        self.cheese3_phase = 'D'
            elif self.cheese3_phase == 'D':
                # while (bunker ready)
                await self.cheese3_internals()
                #clean
                if self.cheese3_barracks not in self.structures(BARRACKS):
                    self.cheese3_phase = 'Y'
                # continue
                for cc in self.structures(COMMANDCENTER):
                    if cc.position == self.cheese3_cc_pos:
                        # init (cc constructing)
                        self.cheese3_cc = cc
                        self.cheese3_phase = 'E'
            elif self.cheese3_phase == 'E':
                # while (cc constructing)
                await self.cheese3_internals()
                # chosen is no redo if the cc-build is interrupted
                #clean
                if self.cheese3_barracks not in self.structures(BARRACKS):
                    self.cheese3_phase = 'Y'
                if self.cheese3_cc not in self.structures(COMMANDCENTER):
                    self.cheese3_phase = 'Y'
                # continue
                for cc in self.structures(COMMANDCENTER).ready:
                    if cc.position == self.cheese3_cc_pos:
                        # init (cc ready)
                        self.home_of_flying_struct[cc.tag] = self.cheese3_landing_pos
                        self.landings_of_flying_struct[cc.tag] = 0
                        self.log_success('up cheese COMMANDCENTER')
                        self.log_command('cc(AbilityId.LIFT')
                        cc(AbilityId.LIFT)
                        self.cheese3_phase = 'F'
            elif self.cheese3_phase == 'F':
                # while (cc flies)
                await self.cheese3_internals()
                #clean
                if self.cheese3_barracks not in self.structures(BARRACKS):
                    self.cheese3_phase = 'Y'
                if self.cheese3_cc not in (self.structures(COMMANDCENTER) + self.structures(COMMANDCENTERFLYING)):
                    self.cheese3_phase = 'Y'
                # continue
                for cc in self.structures(COMMANDCENTER).ready:
                    if self.near(cc.position,self.cheese3_landing_pos,10) and (cc.position != self.cheese3_cc_pos):
                        # init (cc landed)
                        self.cheese3_cc(AbilityId.RALLY_BUILDING,self.cheese3_prison_pos)
                        self.throw_at_spot_if_rich(PLANETARYFORTRESS,cc.position,'do_pf_rush',1)
                        self.cheese3_phase = 'G'
            elif self.cheese3_phase == 'G':
                # while (cc landed)
                await self.cheese3_internals()
                #clean
                if self.cheese3_cc not in self.structures(COMMANDCENTER) + self.structures(PLANETARYFORTRESS):
                    self.cheese3_phase = 'Y'
                # repair
                for scv in self.cheese3_scvs:
                    if scv.is_idle:
                        if self.cheese3_cc.health < self.cheese3_cc.health_max:
                            scv.repair(self.cheese3_cc)
                # continue
                if (self.cheese3_cc in self.structures(PLANETARYFORTRESS).ready):
                    # init (pf ready)
                    self.cheese3_phase = 'H'
            elif self.cheese3_phase == 'H':
                # while (pf ready)
                await self.cheese3_internals()
                #clean
                if self.cheese3_cc not in self.structures(PLANETARYFORTRESS):
                    self.cheese3_phase = 'Y'
                # repair
                for scv in self.cheese3_scvs:
                    if scv.is_idle:
                        if self.cheese3_cc.health < self.cheese3_cc.health_max:
                            scv.repair(self.cheese3_cc)
                # make
                if self.cheese3_cc in self.structures(PLANETARYFORTRESS).ready.idle:
                    if self.count_of_job['idler'] + self.count_of_job['volunteer'] < 11:
                        if self.can_pay(SCV):
                            self.cheese3_cc.train(SCV)
                # continue
            elif self.cheese3_phase == 'Y':
                # clean up the cheese
                for scv in self.units(SCV):
                    scvt = scv.tag
                    if self.job_of_scvt[scvt] == 'cheeser':
                        self.promote(scv,'fleeer')
                self.cheese3_scvs = set()
                if self.cheese3_barracks in self.structures(BARRACKS):
                    if self.cheese3_barracks not in self.structures(BARRACKS).ready:
                        self.log_command('self.cheese3_barracks(AbilityId.CANCEL)')
                        self.cheese3_barracks(AbilityId.CANCEL)
                if self.cheese3_barracks in self.structures(BARRACKS).ready:
                    if self.find_tobuildwalk_a_place(BARRACKS):
                        goal = self.function_result_Point2
                        self.write_layout(BARRACKS, goal)
                        cc = self.cheese3_barracks
                        if not cc.is_idle:
                            self.log_command('cc(AbilityId.CANCEL)')
                            cc(AbilityId.CANCEL)
                        self.home_of_flying_struct[cc.tag] = goal
                        self.landings_of_flying_struct[cc.tag] = 0
                        self.log_success('move cheese BARRACKS')
                        self.log_command('cc(AbilityId.LIFT')
                        cc(AbilityId.LIFT)
                if self.cheese3_barracks in self.structures(BARRACKSFLYING):
                    if self.find_tobuildwalk_a_place(BARRACKS):
                        goal = self.function_result_Point2
                        self.write_layout(BARRACKS, goal)
                        cc = self.cheese3_barracks
                        if not cc.is_idle:
                            self.log_command('cc(AbilityId.CANCEL)')
                            cc(AbilityId.CANCEL)
                        self.home_of_flying_struct[cc.tag] = goal
                        self.landings_of_flying_struct[cc.tag] = 0
                        self.log_success('move cheese BARRACKS')
                if self.cheese3_cc in self.structures(COMMANDCENTER):
                    if self.cheese3_cc not in self.structures(COMMANDCENTER).ready:
                        self.log_command('self.cheese3_cc(AbilityId.CANCEL)')
                        self.cheese3_cc(AbilityId.CANCEL)
                if self.cheese3_cc in self.structures(COMMANDCENTER).ready:
                    if self.find_tobuildwalk_a_place(COMMANDCENTER):
                        goal = self.function_result_Point2
                        self.write_layout(COMMANDCENTER, goal)
                        cc = self.cheese3_cc
                        if not cc.is_idle:
                            self.log_command('cc(AbilityId.CANCEL)')
                            cc(AbilityId.CANCEL)
                        self.home_of_flying_struct[cc.tag] = goal
                        self.landings_of_flying_struct[cc.tag] = 0
                        self.log_success('move cheese COMMANDCENTER')
                        self.log_command('cc(AbilityId.LIFT')
                        cc(AbilityId.LIFT)
                if self.cheese3_cc in self.structures(COMMANDCENTERFLYING):
                    if self.find_tobuildwalk_a_place(COMMANDCENTER):
                        goal = self.function_result_Point2
                        self.write_layout(COMMANDCENTER, goal)
                        cc = self.cheese3_cc
                        if not cc.is_idle:
                            self.log_command('cc(AbilityId.CANCEL)')
                            cc(AbilityId.CANCEL)
                        self.home_of_flying_struct[cc.tag] = goal
                        self.landings_of_flying_struct[cc.tag] = 0
                        self.log_success('move cheese COMMANDCENTER')
                self.cheese3_bunker = None
                self.cheese3_barracks = None
                self.cheese3_cc = None
                self.cheese3_phase = 'Z'


    async def cocoon_internals(self):
        # name cheesebunker
        for bu in self.structures(BUNKER):
            if bu.position == self.cheese3_bunker_pos:
                self.cheese3_bunker = bu
        # name cheesebunker2
        for bu in self.structures(BUNKER):
            if bu.position == self.cheese3_bunker2_pos:
                self.cheese3_bunker2 = bu
        # died scvs
        todel = set()
        for scv in self.cheese3_scvs:
            if scv not in self.units(SCV):
                todel.add(scv)
        self.cheese3_scvs -= todel
        # get scvs
        if len(self.cheese3_scvs) < 2:
            scvt = self.get_near_scvt_to_goodjob(self.cheese3_prison_pos)
            for scv in self.units(SCV):
                if scv.tag == scvt:
                    self.promote(scv,'cheeser')
                    scv.move(self.cheese3_prison_pos)
                    self.cheese3_scvs.add(scv)
        # move scvs
        for scv in self.cheese3_scvs:
            if scv.is_idle:
                if not self.near(scv.position, self.cheese3_prison_pos, 3):
                    scv.move(self.cheese3_prison_pos)
        # move marines
        if self.cheese3_bunker in self.structures(BUNKER): # also when building
            if len(self.cheese3_bunker.passengers) < 4:
                for mari in self.units(MARINE):
                    if not self.near(mari.position, self.cheese3_prison_pos, 7):
                        mari.move(self.cheese3_prison_pos)
        if self.cheese3_bunker2 in self.structures(BUNKER):  # also when building
            if len(self.cheese3_bunker2.passengers) < 4:
                for mari in self.units(MARINE):
                    if not self.near(mari.position, self.cheese3_prison_pos, 7):
                        mari.move(self.cheese3_prison_pos)
        # load marines
        if self.cheese3_bunker in self.structures(BUNKER).ready:
            if len(self.cheese3_bunker.passengers) < 4:
                for mari in self.units(MARINE):
                    if self.near(mari.position, self.cheese3_prison_pos, 7):
                        self.log_command('self.cheese3_bunker(AbilityId.LOAD_BUNKER,mari)')
                        self.cheese3_bunker(AbilityId.LOAD_BUNKER, mari)
        if self.cheese3_bunker2 in self.structures(BUNKER).ready:
            if len(self.cheese3_bunker2.passengers) < 4:
                for mari in self.units(MARINE):
                    if self.near(mari.position, self.cheese3_prison_pos, 7):
                        self.log_command('self.cheese3_bunker2(AbilityId.LOAD_BUNKER,mari)')
                        self.cheese3_bunker2(AbilityId.LOAD_BUNKER, mari)
        # rebuild bunker
        if self.cheese3_bunker not in self.structures(BUNKER):
            if not self.we_started_at(BUNKER, self.cheese3_bunker_pos):
                self.throw_at_spot_if_rich(BUNKER, self.cheese3_bunker_pos, 'cocoon',1)
        # rebuild bunker2
        if self.cheese3_bunker2 not in self.structures(BUNKER):
            if not self.we_started_at(BUNKER, self.cheese3_bunker2_pos):
                self.throw_at_spot_if_rich(BUNKER, self.cheese3_bunker2_pos, 'cocoon',1)
        # repair bunker
        if self.cheese3_bunker in self.structures(BUNKER).ready:
            if self.cheese3_bunker.health < self.cheese3_bunker.health_max:
                for scv in self.cheese3_scvs:
                    if scv.is_idle:
                        scv.repair(self.cheese3_bunker)
        # repair bunker2
        if self.cheese3_bunker2 in self.structures(BUNKER).ready:
            if self.cheese3_bunker2.health < self.cheese3_bunker2.health_max:
                for scv in self.cheese3_scvs:
                    if scv.is_idle:
                        scv.repair(self.cheese3_bunker2)


    async def do_cocoon(self):
        self.routine = 'do_cocoon'
        if self.opening_name == 'cocoon':
            if self.cheese3_phase == 'A':
                # while (nothing)
                # continue
                for bu in self.structures(BARRACKS):
                    if bu.position == self.cheese3_barracks_pos:
                        # init (barracks is constructing)
                        self.cheese3_barracks = bu
                        self.special_tags.add(bu.tag)
                        self.cheese3_barracks(AbilityId.RALLY_BUILDING, self.cheese3_prison_pos)
                        self.cheese3_phase = 'B'
                    if bu.position == self.cheese3_barracks2_pos:
                        # init (barracks is constructing)
                        self.cheese3_barracks2 = bu
                        self.special_tags.add(bu.tag)
                        self.cheese3_barracks2(AbilityId.RALLY_BUILDING, self.cheese3_prison_pos)
                        self.cheese3_phase = 'C'
            elif self.cheese3_phase == 'B':
                # while (nothing)
                # continue
                for bu in self.structures(BARRACKS):
                    if bu.position == self.cheese3_barracks2_pos:
                        # init (barracks is constructing)
                        self.cheese3_barracks2 = bu
                        self.special_tags.add(bu.tag)
                        self.cheese3_barracks2(AbilityId.RALLY_BUILDING, self.cheese3_prison_pos)
                        self.cheese3_phase = 'D'
            elif self.cheese3_phase == 'C':
                # while (nothing)
                # continue
                for bu in self.structures(BARRACKS):
                    if bu.position == self.cheese3_barracks_pos:
                        # init (barracks is constructing)
                        self.cheese3_barracks = bu
                        self.special_tags.add(bu.tag)
                        self.cheese3_barracks(AbilityId.RALLY_BUILDING, self.cheese3_prison_pos)
                        self.cheese3_phase = 'D'
            elif self.cheese3_phase == 'D':
                # while (barracks is constructing)
                #clean
                if self.cheese3_barracks not in self.structures(BARRACKS):
                    self.cheese3_phase = 'Y'
                if self.cheese3_barracks2 not in self.structures(BARRACKS):
                    self.cheese3_phase = 'Y'
                # continue
                for bu in self.structures(BUNKER):
                    if bu.position == self.cheese3_bunker_pos:
                        # init (bunker is constructing)
                        self.cheese3_bunker = bu
                        for scvt in self.goal_of_trabu_scvt:
                            if self.goal_of_trabu_scvt[scvt] == self.cheese3_bunker_pos:
                                for scv in self.units(SCV):
                                    if scv.tag == scvt:
                                        self.cheese3_scvs.add(scv)
                                        # still builder, later to be cheeser
                                        self.cheese3_phase = 'E'
                    if bu.position == self.cheese3_bunker2_pos:
                        # init (bunker is constructing)
                        self.cheese3_bunker2 = bu
                        for scvt in self.goal_of_trabu_scvt:
                            if self.goal_of_trabu_scvt[scvt] == self.cheese3_bunker2_pos:
                                for scv in self.units(SCV):
                                    if scv.tag == scvt:
                                        self.cheese3_scvs.add(scv)
                                        # still builder, later to be cheeser
                                        self.cheese3_phase = 'F'
            elif self.cheese3_phase == 'E':
                # while (barracks is constructing)
                # clean
                if self.cheese3_barracks not in self.structures(BARRACKS):
                    self.cheese3_phase = 'Y'
                if self.cheese3_barracks2 not in self.structures(BARRACKS):
                    self.cheese3_phase = 'Y'
                # continue
                for bu in self.structures(BUNKER):
                    if bu.position == self.cheese3_bunker2_pos:
                        # init (bunker is constructing)
                        self.cheese3_bunker2 = bu
                        for scvt in self.goal_of_trabu_scvt:
                            if self.goal_of_trabu_scvt[scvt] == self.cheese3_bunker2_pos:
                                for scv in self.units(SCV):
                                    if scv.tag == scvt:
                                        self.cheese3_scvs.add(scv)
                                        # still builder, later to be cheeser
                                        self.cheese3_phase = 'G'
            elif self.cheese3_phase == 'F':
                # while (barracks is constructing)
                #clean
                if self.cheese3_barracks not in self.structures(BARRACKS):
                    self.cheese3_phase = 'Y'
                if self.cheese3_barracks2 not in self.structures(BARRACKS):
                    self.cheese3_phase = 'Y'
                # continue
                for bu in self.structures(BUNKER):
                    if bu.position == self.cheese3_bunker_pos:
                        # init (bunker is constructing)
                        self.cheese3_bunker = bu
                        for scvt in self.goal_of_trabu_scvt:
                            if self.goal_of_trabu_scvt[scvt] == self.cheese3_bunker_pos:
                                for scv in self.units(SCV):
                                    if scv.tag == scvt:
                                        self.cheese3_scvs.add(scv)
                                        # still builder, later to be cheeser
                                        self.cheese3_phase = 'G'
            elif self.cheese3_phase == 'G':
                # while (bunker is constructing)
                await self.cocoon_internals()
                #clean
                if self.cheese3_barracks not in self.structures(BARRACKS):
                    self.cheese3_phase = 'Y'
                if self.cheese3_barracks2 not in self.structures(BARRACKS):
                    self.cheese3_phase = 'Y'
                # continue
                bus = 0
                for bu in self.structures(BUNKER).ready:
                    if bu.position == self.cheese3_bunker_pos:
                        # init (bunker ready)
                        self.cheese3_barracks(AbilityId.RALLY_BUILDING,self.cheese3_bunker)
                        bus += 1
                        for scv in self.cheese3_scvs:
                            self.promote(scv,'cheeser')
                            scv.move(self.cheese3_prison_pos)
                    if bu.position == self.cheese3_bunker2_pos:
                        # init (bunker ready)
                        self.cheese3_barracks2(AbilityId.RALLY_BUILDING, self.cheese3_bunker2)
                        bus += 1
                        for scv in self.cheese3_scvs:
                            self.promote(scv, 'cheeser')
                            scv.move(self.cheese3_prison_pos)
                if bus == 2:
                    self.cheese3_phase = 'H'
            elif self.cheese3_phase == 'H':
                # while (bunker ready)
                await self.cocoon_internals()
                #clean
                if self.cheese3_barracks not in self.structures(BARRACKS):
                    self.cheese3_phase = 'Y'
                if self.cheese3_barracks2 not in self.structures(BARRACKS):
                    self.cheese3_phase = 'Y'
                # continue
                if (self.cheese3_bunker in self.structures(BUNKER)) and (self.cheese3_bunker2 in self.structures(BUNKER)):
                    if len(self.cheese3_bunker.passengers) + len(self.cheese3_bunker2.passengers) >= 5:
                        self.cheese3_phase = 'Y'
            elif self.cheese3_phase == 'Y':
                # clean up the cheese
                for scv in self.units(SCV):
                    scvt = scv.tag
                    if self.job_of_scvt[scvt] == 'cheeser':
                        self.promote(scv,'fleeer')
                self.cheese3_scvs = set()
                if self.cheese3_barracks in self.structures(BARRACKS):
                    if self.cheese3_barracks not in self.structures(BARRACKS).ready:
                        self.log_command('self.cheese3_barracks(AbilityId.CANCEL)')
                        self.cheese3_barracks(AbilityId.CANCEL)
                if self.cheese3_barracks in self.structures(BARRACKS).ready:
                    if self.find_tobuildwalk_a_place(BARRACKS):
                        goal = self.function_result_Point2
                        self.write_layout(BARRACKS, goal)
                        cc = self.cheese3_barracks
                        if not cc.is_idle:
                            self.log_command('cc(AbilityId.CANCEL)')
                            cc(AbilityId.CANCEL)
                        self.home_of_flying_struct[cc.tag] = goal
                        self.landings_of_flying_struct[cc.tag] = 0
                        self.log_success('move cheese BARRACKS')
                        self.log_command('cc(AbilityId.LIFT')
                        cc(AbilityId.LIFT)
                if self.cheese3_barracks in self.structures(BARRACKSFLYING):
                    if self.find_tobuildwalk_a_place(BARRACKS):
                        goal = self.function_result_Point2
                        self.write_layout(BARRACKS, goal)
                        cc = self.cheese3_barracks
                        if not cc.is_idle:
                            self.log_command('cc(AbilityId.CANCEL)')
                            cc(AbilityId.CANCEL)
                        self.home_of_flying_struct[cc.tag] = goal
                        self.landings_of_flying_struct[cc.tag] = 0
                        self.log_success('move cheese BARRACKS')
                if self.cheese3_barracks2 in self.structures(BARRACKS):
                    if self.cheese3_barracks2 not in self.structures(BARRACKS).ready:
                        self.log_command('self.cheese3_barracks2(AbilityId.CANCEL)')
                        self.cheese3_barracks2(AbilityId.CANCEL)
                if self.cheese3_barracks2 in self.structures(BARRACKS).ready:
                    if self.find_tobuildwalk_a_place(BARRACKS):
                        goal = self.function_result_Point2
                        self.write_layout(BARRACKS, goal)
                        cc = self.cheese3_barracks2
                        if not cc.is_idle:
                            self.log_command('cc(AbilityId.CANCEL)')
                            cc(AbilityId.CANCEL)
                        self.home_of_flying_struct[cc.tag] = goal
                        self.landings_of_flying_struct[cc.tag] = 0
                        self.log_success('move cheese BARRACKS')
                        self.log_command('cc(AbilityId.LIFT')
                        cc(AbilityId.LIFT)
                if self.cheese3_barracks2 in self.structures(BARRACKSFLYING):
                    if self.find_tobuildwalk_a_place(BARRACKS):
                        goal = self.function_result_Point2
                        self.write_layout(BARRACKS, goal)
                        cc = self.cheese3_barracks2
                        if not cc.is_idle:
                            self.log_command('cc(AbilityId.CANCEL)')
                            cc(AbilityId.CANCEL)
                        self.home_of_flying_struct[cc.tag] = goal
                        self.landings_of_flying_struct[cc.tag] = 0
                        self.log_success('move cheese BARRACKS')
                self.cheese3_bunker = None
                self.cheese3_barracks = None
                self.cheese3_bunker2 = None
                self.cheese3_barracks2 = None
                self.cheese3_phase = 'Z'




    def get_shield_pos(self):
        self.write_layout(BUNKER,self.cheese_bunker_pos)
        self.write_layout(ARMORY,self.cheese_landing_pos)
        keep = []
        found = 0
        for r in range(1,15):
            if found < 2:
                for x in range(-r,r):
                    for y in range(-r,r):
                        if abs(x)+abs(y)+max(abs(x),abs(y)) == r:
                            point = Point2((self.cheese_bunker_pos.x+x,self.cheese_bunker_pos.y+y))
                            if self.check_layout(BUNKER,point):
                                goodpoint = point
                                self.recycling.append((INFESTEDBUNKER, goodpoint))
                                self.write_layout(BUNKER, goodpoint)
                                keep.append(goodpoint)
                                found += 1
        self.erase_layout(BUNKER,self.cheese_bunker_pos)
        self.erase_layout(ARMORY,self.cheese_landing_pos)
        self.erase_layout(BUNKER,keep[0])
        self.erase_layout(BUNKER,keep[1])

    #*********************************************************************************************************************

    async def lift(self):
#       attacked buildings can fly, survive, be repaired, and land back.
        self.routine = 'lift'
        for srt in self.landable:
            basekind = self.basekind_of(srt)
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
                            tries = 0
                            radius = 0
                            ok = False
                            while (not ok):
                                if tries == radius * radius:
                                    radius += 1
                                tries += 1
                                x = oldpoint.x + random.randrange(-radius, radius)
                                y = oldpoint.y + random.randrange(-radius, radius)
                                altpoint = Point2((x, y))
                                ok = self.check_layout(basekind,altpoint)
                            self.home_of_flying_struct[bu.tag] = altpoint
                        self.log_success('down '+srt.name)
                        self.log_command('bu(AbilityId.LAND,self.home_of_flying_struct[bu.tag])')
                        bu(AbilityId.LAND,self.home_of_flying_struct[bu.tag])
                        self.landings_of_flying_struct[bu.tag] += 1
                    else:
                        # the move prevents over-early "can not land" warnings.
                        bu.move(self.home_of_flying_struct[bu.tag])
                elif not self.near(self.shipyard,bu.position,7):
                    self.log_command('bu(AbilityId.MOVE_MOVE,self.shipyard)')
                    bu(AbilityId.MOVE_MOVE,self.shipyard)
        for srt in self.liftable:
            for bu in self.structures(srt).ready:
                if bu.health < 700:
                    if bu.tag not in self.special_tags:
                        if not bu.is_idle:
                            self.log_command('bu(AbilityId.CANCEL)')
                            bu(AbilityId.CANCEL)
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
                self.special_tags.add(bu.tag)
            if bu.tag in self.home_of_flying_struct:
                if self.home_of_flying_struct[bu.tag] == self.wall_barracks_pos:
                    wallseen = True
                    self.special_tags.add(bu.tag)
        if not wallseen:
            first = True
            for bu in self.structures(BARRACKS).ready.idle + self.structures(BARRACKSFLYING):
                if bu.tag not in self.special_tags:
                    if first:
                        first = False
                        self.log_success('redirecting a barracks to the wall')
                        self.home_of_flying_struct[bu.tag] = self.wall_barracks_pos
                        if bu not in self.structures(BARRACKSFLYING):
                            self.landings_of_flying_struct[bu.tag] = 0
                            self.log_success('up BARRACKS')
                            self.log_command('bu(AbilityId.LIFT')
                            bu(AbilityId.LIFT)


    async def manage_the_wall(self):
        self.routine = 'manage_the_wall'
        havehome = False
        for cc in self.all_bases:
            if cc.position == self.start_location:
                havehome = True
        updowns = set()
        if havehome:
            wall_recollect = set()
            wall_recollect.add((BARRACKS, self.wall_barracks_pos))
            wall_recollect.add((SUPPLYDEPOT, self.wall_depot0_pos))
            wall_recollect.add((SUPPLYDEPOT, self.wall_depot1_pos))
            barracksseen = False
            for (struc_type,position) in wall_recollect:
                seen = False
                for struc in self.structures(struc_type) + self.structures(SUPPLYDEPOTLOWERED):
                    if (struc.position == position):
                        seen = True
                        self.special_tags.add(struc.tag)
                        if (struc_type == SUPPLYDEPOT):
                            updowns.add(struc.tag)
                        if (struc_type == BARRACKS):
                            barracksseen = True
                            if (not self.wall_barracks_managed):
                                self.wall_barracks_managed = True
                                self.wall_barracks = struc
                                struc(AbilityId.RALLY_BUILDING, struc.position.towards(self.start_location, 2))
                if self.we_started_at(struc_type,position):
                    seen = True
                if not seen:
                    if (struc_type,position) not in self.specialplaces:
                        self.specialplaces.append((struc_type,position))
            if not barracksseen:
                self.wall_barracks_managed = False
        for sd in self.structures(SUPPLYDEPOTLOWERED).ready + self.structures(SUPPLYDEPOT).ready:
            if sd.tag in updowns:
                danger = False
                for ene in self.enemy_units:
                    if self.near(ene.position,sd.position,5):
                        danger = True
                # close
                if (danger) and (sd in self.structures(SUPPLYDEPOTLOWERED).ready):
                    self.log_command('sd(AbilityId.MORPH_SUPPLYDEPOT_RAISE)')
                    sd(AbilityId.MORPH_SUPPLYDEPOT_RAISE)
                    self.log_success('raising')
                # open
                if (not danger) and (sd in self.structures(SUPPLYDEPOT).ready):
                    self.log_command('sd(AbilityId.MORPH_SUPPLYDEPOT_LOWER)')
                    sd(AbilityId.MORPH_SUPPLYDEPOT_LOWER)
                    self.log_success('lowering')
                # do not idle on the depot
                for scv in self.units(SCV).idle:
                    if self.near(scv.position,sd.position,1.5):
                        whereto = self.flee(sd.position,2)
                        self.log_command('scv.move(whereto)')
                        scv.move(whereto)
                # marine
                if danger and self.wall_barracks_managed:
                    if self.wall_barracks.tag in self.idle_structure_tags:
                        if self.can_pay(MARINE):
                            if self.supply_check(MARINE):
                                self.log_command('self.wall_barracks.train(MARINE)')
                                self.wall_barracks.train(MARINE)
                                self.idle_structure_tags.remove(self.wall_barracks.tag)


    def lower_some_depots(self):
        for sd in self.structures(SUPPLYDEPOT):
            near = False
            for mim in self.mineral_field:
                if self.near(sd.position,mim.position,5):
                    near = True
            for gas in self.vespene_geyser:
                if self.near(sd.position,gas.position,5):
                    near = True
            if self.near(sd.position,self.shipyard,5): # shipyard can be moved
                near = True
            if near:
                self.log_command('sd(AbilityId.MORPH_SUPPLYDEPOT_LOWER)')
                sd(AbilityId.MORPH_SUPPLYDEPOT_LOWER)
                self.log_success('lowering')


    async def may_cancel(self):
        self.routine = 'may_cancel'
        for stru in self.structures:
            if stru.position not in [self.cheese_bunker_pos, self.cheese_landing_pos, self.cheese3_landing_pos]:
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
        # ignore self.already_pending(SCV) as it is slow
        todo = amount - self.units(SCV).amount
        todo = min(todo,self.supply_left)
        if todo > 0:
            todo = 1 # max 1 per iteration
            if self.count_of_job['idler'] + self.count_of_job['volunteer'] < 11:
                # build scv or orbital
                if self.count_of_job['idler'] + self.count_of_job['volunteer'] > 2:
                    # try oc first
                    for cc in self.structures(COMMANDCENTER):
                        if cc.tag in self.idle_structure_tags:
                            if cc.position in self.cc_destiny:
                                if self.cc_destiny[cc.position] == 'oc':
                                    if self.can_pay(ORBITALCOMMAND):
                                        if todo > 0:
                                            todo -= 1
                                            self.throw_at_spot(ORBITALCOMMAND,cc.position,'build_worker',1)
                for cc in self.all_bases:
                    if cc.tag in self.idle_structure_tags:
                        if cc.tag not in self.ambition_of_strt:
                            # always urgent
                            if self.can_pay(SCV):
                                if todo > 0:
                                    todo -= 1
                                    self.log_workers('')
                                    self.log_command('cc.train(SCV)')
                                    dummy = cc.train(SCV)
                                    self.idle_structure_tags.remove(cc.tag)

    async def mules(self):
        for oc in self.structures(ORBITALCOMMAND).ready:
            if oc.energy >= 50:
                if len(self.mineral_field) > 0:
                    bestsd = 99999
                    bestmim = random.choice(self.mineral_field)
                    pog = 0
                    while (pog < 100) and ((bestsd > 100) or (pog < 20)):
                        pog += 1
                        mim = random.choice(self.mineral_field)
                        itssd = 99999
                        for kind in [COMMANDCENTER,ORBITALCOMMAND,PLANETARYFORTRESS]:
                            for cc in self.structures(kind).ready:
                                sd = self.sdist(cc.position,mim.position)
                                itssd = min(itssd,sd)
                        if itssd < bestsd:
                            bestsd = itssd
                            bestmim = mim
                    mim = bestmim
                    oc(AbilityId.CALLDOWNMULE_CALLDOWNMULE, mim)


    async def be_gasminer(self,scv,gas):
        self.routine = 'be_gasminer'
        self.log_command('scv.gather(gas)')
        dummy = scv.gather(gas)
        self.gast_of_scvt[scv.tag] = gas.tag
        self.count_of_gast[gas.tag] += 1

    async def be_mimminer(self,scv,mim):
        self.routine = 'be_mimminer'
        self.log_command('scv.gather(mim)')
        dummy = scv.gather(mim)
        self.mimt_of_scvt[scv.tag] = mim.tag
        self.count_of_mimt[mim.tag] += 1

    def promote(self, scv,new_job):
        self.routine = 'promote'
        scvt = scv.tag
        old_job = self.job_of_scvt[scvt]
        if old_job == 'gasminer':
            if scvt in self.gast_of_scvt:
                gast = self.gast_of_scvt[scvt]
                self.count_of_gast[gast] -= 1
                del self.gast_of_scvt[scvt]
        elif old_job == 'mimminer':
            if scvt in self.mimt_of_scvt:
                mimt = self.mimt_of_scvt[scvt]
                self.count_of_mimt[mimt] -= 1
                del self.mimt_of_scvt[scvt]
        self.count_of_job[old_job] -= 1
        self.count_of_job[new_job] += 1
        if scv.is_collecting:
            self.log_command('scv(AbilityId.STOP)')
            scv(AbilityId.STOP)
        self.job_of_scvt[scvt] = new_job
        self.promotionsite_of_scvt[scvt] = scv.position
        self.log_workers('promoted ' + old_job + ' to ' + new_job + ' ' + self.name(scvt))

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
                        if self.near(scv.position, s.position, 15):
                            scvt = scv.tag
                            if scvt in self.all_scvt:
                                job = self.job_of_scvt[scvt]
                                if job == 'arearepairer':
                                    hasrepairers += 1
                                elif job in (self.bad_jobs + self.no_jobs):
                                    couldhaverep = True
                    if (hasrepairers < 3) and (couldhaverep):
                        low_qual = qual
                        wreck = s
        if low_qual < 0.99:
            # we have a wreck needing repair
            scvt = self.get_near_scvt_to_goodjob(s.position)
            for scv in self.units(SCV):
                if scv.tag == scvt:
                    self.promote(scv,'arearepairer')



    async def repair_it(self):
        self.routine = 'repair_it'
        for scv in self.units(SCV).ready:
            scvt = scv.tag
            if scvt in self.all_scvt:
                if self.job_of_scvt[scvt] in ['arearepairer','cheeser']:
                    if scvt in self.busy_arearepairer:
                        if scv.is_idle:
                            self.busy_arearepairer.remove(scvt)
                            self.log_workers(self.name(scvt)+' finished repairing')
                    else:
                        # check important structures
                        low_qual = 1.0
                        wreck = self.notag
                        for strtype in self.all_repairable_shooters:
                            for s in self.structures(strtype).ready + self.units(strtype):
                                if self.near(scv.position,s.position,15):
                                    qual = s.health/s.health_max
                                    if qual<low_qual:
                                        low_qual = qual
                                        wreck = s
                        if low_qual >= 0.99:
                            # check all structures
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



    async def manage_workers(self):
        self.routine = 'manage_workers'
        #
        # panic
        for scv in self.units(SCV):
            scvt = scv.tag
            if scvt in self.all_scvt:
                job = self.job_of_scvt[scvt]
                if job in ['gasminer','mimminer']:
                    panic = True
                    for tow in self.all_bases:
                        if self.near(scv.position,tow.position,self.miner_bound):
                            panic = False
                    if panic:
                        self.promote(scv,'fleeer')
        # jobhaters
        for scv in self.units(SCV).idle:
            scvt = scv.tag
            if scvt in self.all_scvt:
                job = self.job_of_scvt[scvt]
                # fleeer turns to idler if there is no danger, if danger run
                if job == 'fleeer':
                    danger = False
                    for ene in self.enemy_units:
                        if self.near(ene.position,scv.position,7):
                            danger = True
                    if danger:
                        place = self.random_mappoint()
                        self.log_command('scv(AbilityId.MOVE_MOVE,place)')
                        scv(AbilityId.MOVE_MOVE, place)
                    else:
                        if scv.position != self.promotionsite_of_scvt[scvt]:
                            self.promote(scv,'idler')
                # May not idle:
                elif job in ['gasminer','mimminer','escorter','builder','arearepairer']:
                    if scv.position != self.promotionsite_of_scvt[scvt]:
                        self.promote(scv,'idler')
                elif job == 'traveller':
                    if not self.near(scv.position,self.goal_of_trabu_scvt[scvt],3):
                        # this can occur if the traveller has been blocked
                        self.log_command('scv(AbilityId.MOVE_MOVE,self.goal_of_trabu_scvt[scvt])')
                        scv(AbilityId.MOVE_MOVE,self.goal_of_trabu_scvt[scvt])
        # builders start to mine after building a geyser
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
                                    self.promote(scv,'gasminer')
                                    await self.be_gasminer(scv,gas)
        #
        #
        #
        # shiprepairers
        amount = self.units(BATTLECRUISER).ready.amount
        # hire new shiprepairer
        todo = amount - self.count_of_job['shiprepairer']
        if todo > 0:
            scvt = self.get_near_scvt_to_goodjob(self.shipyard)
            for scv in self.units(SCV):
                if scv.tag == scvt:
                    self.promote(scv,'shiprepairer')
        # fire some
        todo = self.count_of_job['shiprepairer'] - amount
        if todo > 0:
            for scv in self.units(SCV):
                scvt = scv.tag
                if self.job_of_scvt[scvt] == 'shiprepairer':
                    if todo > 0:
                        todo -= 1
                        self.promote(scv,'idler')
        # whip them
        for scv in self.units(SCV).idle:
            scvt = scv.tag
            if scvt in self.all_scvt:
                if (self.job_of_scvt[scvt] == 'shiprepairer'):
                    if not self.near(scv.position,self.shipyard,12):
                        self.log_command('scv(AbilityId.MOVE_MOVE,self.shipyard)')
                        scv(AbilityId.MOVE_MOVE,self.shipyard)
                    else:
                        first = True
                        for bc in self.units(BATTLECRUISER):
                            bct = bc.tag
                            if first:
                                if self.state_of_unittag[bct] == 'repair':
                                    if self.near(bc.position,self.shipyard,12):
                                        self.log_command('scv.repair(bc)')
                                        scv.repair(bc)
                                        first = False
        # get a targetpos. Once, the exact shipyard was not reachable for shiprepairers.
        targetpos = self.shipyard
        for scv in self.units(SCV):
            scvt = scv.tag
            if scvt in self.all_scvt:
                if (self.job_of_scvt[scvt] == 'shiprepairer'):
                    if self.near(scv.position, self.shipyard, 6):
                        targetpos = scv.position
        # keep the bc in the shipyard. Who is pulling it away?
        for bc in self.units(BATTLECRUISER):
            bct = bc.tag
            if self.state_of_unittag[bct] == 'repair':
                 if self.near(bc.position,self.shipyard,12) and not self.near(bc.position,targetpos,2):
                     self.log_command('bc(AbilityId.MOVE_MOVE,targetpos)')
                     bc(AbilityId.MOVE_MOVE,targetpos)
        # 1 scout please
        if (self.scout_tag == self.notag) and (len(self.structures) >= 2):
            scvt = self.get_near_scvt_to_goodjob(self.enemyloc)
            for scv in self.units(SCV):
                if scv.tag == scvt:
                    self.promote(scv,'scout')
                    # mark it and start running around
                    self.scout_tag = scvt
                    self.scout_pole = 0
                    self.go_move(scv,self.scout_pos[0])
        # expansionblocker
        if self.game_choice[31]:
            if (self.blocker_tag == self.notag):
                self.blocker_tag = self.get_near_scvt_to_goodjob(self.enemyloc)
                for scv in self.units(SCV):
                    if scv.tag == self.blocker_tag:
                        self.blocker_scv = scv
                        self.promote(self.blocker_scv, 'scout')
                        self.blocker_pole = 0
                        self.blocker_scv.move(self.blocker_pos[0])

    def blocker(self):
        if self.game_choice[31]:
            if self.blocker_scv in self.units(SCV):
                self.blocker_pole = (self.blocker_pole + 1) % len(self.blocker_pos)
                goal = self.blocker_pos[self.blocker_pole]
                # high APM command not logged
                self.blocker_scv.move(goal)
                if self.blocker_pole == 0:
                    for ene in self.enemy_structures:
                        if self.near(ene.position,self.enemy_expand_pos,5):
                            self.next_blocker()

    def init_blocker(self):
        self.make_circle(12) # emperical max
        self.enemy_expansions = []
        self.enemy_expand_pos = self.enemyloc
        self.next_blocker()

    def next_blocker(self):
        self.enemy_expansions.append(self.enemy_expand_pos)
        bestsd = 99999
        for pos in self.expansion_locations_list:
            if pos not in self.enemy_expansions:
                sd = self.sdist(pos,self.enemyramp_pos)
                if sd < bestsd:
                    self.enemy_expand_pos = pos
                    bestsd = sd
        self.blocker_pos = []
        for point in self.circle:
            self.blocker_pos.append(Point2((self.enemy_expand_pos.x+4*point.x,self.enemy_expand_pos.y+4*point.y)))


    def search_applicants(self):
        self.routine = 'search_applicants'
        self.fix_count_of_job()
        total_wish = 0
        for cc in self.all_bases:
            total_wish = total_wish + self.wanted_of_cct[cc.tag]
        if total_wish < self.count_of_job['idler'] + self.count_of_job['volunteer']:
            for cc in self.all_bases:
                while self.wanted_of_cct[cc.tag] > 0:
                    self.wanted_of_cct[cc.tag] -= 1
                    scvt = self.get_near_scvt_nojob(cc.position)
                    for scv in self.units(SCV):
                        if scv.tag == scvt:
                            self.promote(scv,'applicant')
                            self.log_command('scv(AbilityId.MOVE_MOVE,cc.position.towards(self.game_info.map_center,-3))')
                            scv(AbilityId.MOVE_MOVE,cc.position.towards(self.game_info.map_center,-3))
                            self.vision_of_scvt[scvt] = cc.tag
        else:
            for scv in self.units(SCV):
                scvt = scv.tag
                if self.job_of_scvt[scvt] in self.no_jobs:
                    cct = self.get_near_cct_wanted(scv.position)
                    for cc in self.all_bases:
                        if cc.tag == cct:
                            self.wanted_of_cct[cc.tag] -= 1
                            self.promote(scv,'applicant')
                            self.log_command('scv(AbilityId.MOVE_MOVE,cc.position.towards(self.game_info.map_center,-3))')
                            scv(AbilityId.MOVE_MOVE,cc.position.towards(self.game_info.map_center,-3))
                            self.vision_of_scvt[scvt] = cc.tag



    async def manage_gas(self):
        self.routine = 'manage_gas'
        self.log_gasminer()
        for scvt in self.all_scvt:
            if self.job_of_scvt[scvt] == 'gasminer':
                if scvt not in self.gast_of_scvt:
                    for scv in self.units(SCV):
                        if scv.tag == scvt:
                            self.promote(scv,'idler')
        vacatures = self.gasminer_vacatures()
        if vacatures > 0:
#           new gas-mineral connections
            if vacatures < self.count_of_job['idler'] + self.count_of_job['volunteer'] + self.count_of_job['applicant']:
                for gas in self.all_refineries:
                    gast = gas.tag
                    if gast in self.all_gast:
                        if self.count_of_gast[gast] < 3:
                            scvt = self.get_near_scvt_nojob_or_applicant(gas.position)
                            for scv in self.units(SCV):
                                if scv.tag == scvt:
                                    if self.near(scv.position,gas.position,self.miner_bound):
                                        self.promote(scv, 'gasminer')
                                        await self.be_gasminer(scv,gas)
            else:
                for scv in self.units(SCV):
                    scvt = scv.tag
                    job = self.job_of_scvt[scvt]
                    if (job in self.no_jobs) or (job == 'applicant'):
                        gast = self.get_near_gast_free(scv.position)
                        for gas in self.all_refineries:
                            if gas.tag == gast:
                                if self.near(scv.position,gas.position,self.miner_bound):
                                    self.promote(scv,'gasminer')
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
                                    self.wanted_of_cct[cc.tag] += 1
#           decrease self.wanted_of_cct for walking applicants
            for scvt in self.vision_of_scvt:
                cct = self.vision_of_scvt[scvt]
                self.wanted_of_cct[cct] -= 1
            self.search_applicants()


    async def manage_minerals(self):
        self.routine = 'manage_minerals'
        for scvt in self.all_scvt:
            if self.job_of_scvt[scvt] == 'mimminer':
                if scvt not in self.mimt_of_scvt:
                    for scv in self.units(SCV):
                        if scv.tag == scvt:
                            self.promote(scv,'idler')
        self.fix_count_of_job()
        vacatures = self.mimminer_vacatures()
        if vacatures > 0:
#           new mim-mineral connections
            if vacatures < self.count_of_job['idler'] + self.count_of_job['volunteer'] + self.count_of_job['applicant']:
                for mim in self.mineral_field:
                    mimt = mim.tag
                    if mimt in self.all_mimt:
                        if self.count_of_mimt[mimt] < 2:
                            scvt = self.get_near_scvt_nojob_or_applicant(mim.position)
                            for scv in self.units(SCV):
                                if scv.tag == scvt:
                                    if self.near(scv.position,mim.position,self.miner_bound):
                                        self.promote(scv, 'mimminer')
                                        await self.be_mimminer(scv,mim)
            else:
                for scv in self.units(SCV):
                    scvt = scv.tag
                    job = self.job_of_scvt[scvt]
                    if (job in self.no_jobs) or (job == 'applicant'):
                        mimt = self.get_near_mimt_free(scv.position)
                        for mim in self.mineral_field:
                            if mim.tag == mimt:
                                if self.near(scv.position,mim.position,self.miner_bound):
                                    self.promote(scv,'mimminer')
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
                                    self.wanted_of_cct[cc.tag] += 1
#           decrease self.wanted_of_cct for walking applicants
            for scvt in self.vision_of_scvt:
                cct = self.vision_of_scvt[scvt]
                self.wanted_of_cct[cct] -= 1
            self.search_applicants()

    async def more_gas(self):
        self.routine = 'more_gas'
        # try to swap a mimminer to gasminer
        todo = 1
        self.fix_count_of_gast()
        if self.gasminer_vacatures() > 0:
            thisgast = self.notag
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
                                    todo -= 1
                                    self.promote(scv,'gasminer')
                                    await self.be_gasminer(scv,gas)

    async def more_minerals(self):
        self.routine = 'more_minerals'
        # try to swap a gasminer to mimminer
        todo = 1
        self.fix_count_of_mimt()
        if self.mimminer_vacatures() > 0:
            thismimt = self.notag
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
                                    todo -= 1
                                    self.promote(scv,'mimminer')
                                    await self.be_mimminer(scv,mim)


    async def manage_rest(self):
        self.routine = 'manage_rest'
        self.fix_count_of_job()
#       
#       applicant was walking to a cc with a problem
        for scvt in self.all_scvt:
            if self.job_of_scvt[scvt] == 'applicant':
                if scvt not in self.vision_of_scvt:
                    for scv in self.units(SCV):
                        if scv.tag == scvt:
                            self.promote(scv,'idler')
#
#       max idle workers
        todo = self.count_of_job['idler'] + self.count_of_job['volunteer'] - 22
        for scv in self.units(SCV):
            scvt = scv.tag
            if scvt in self.all_scvt:
                if self.job_of_scvt[scvt] in self.no_jobs:
                    if todo > 0:
                        todo -= 1
                        self.promote(scv,'suicider')
                        self.log_command('scv.attack(self.enemyloc)')
                        scv.attack(self.enemyloc)
#       job-swap for late game
        if (self.count_of_job['idler'] + self.count_of_job['volunteer'] == 0) and (self.itera % 19 == 0):
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
                            self.promote(scv,'idler')
                            self.log_workers('Enemy fear stops escorter '+self.name(scvt))
                            self.log_command('scv(AbilityId.STOP)')
                            scv(AbilityId.STOP)
        # scout
        for scv in self.units(SCV):
            if scv.tag == self.scout_tag:
                if self.no_move_or_near(scv,4,4):
                    self.scout_pole = (self.scout_pole+1) % len(self.scout_pos)
                    goal = self.scout_pos[self.scout_pole]
                    self.go_move(scv,goal)
        # idler leisure walks
        for scv in self.units(SCV):
            scvt = scv.tag
            if scvt in self.all_scvt:
                if self.job_of_scvt[scvt] == 'idler':
                    # get a point, not too far
                    sd = 99999
                    while sd > 70 * 70:
                        tp = self.random_mappoint()
                        sd = self.sdist(tp, self.start_location)
                    if self.near(scv.position,self.start_location,80):
                        if scv in self.units(SCV).idle:
                            self.log_command('scv.attack(tp)')
                            scv.attack(tp)
                    else: # too far
                        self.log_command('scv.move(tp)')
                        scv.move(tp)



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
                                            self.count_of_mimt[mimt] += 1
                                            self.count_of_mimt[assigned_mimt] -= 1
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
                                            self.count_of_mimt[mimt] += 1
                                            self.count_of_mimt[assigned_mimt] -= 1
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
                                            self.count_of_gast[gast] += 1
                                            self.count_of_gast[assigned_gast] -= 1
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
                                            self.count_of_gast[gast] += 1
                                            self.count_of_gast[assigned_gast] -= 1
                                            if self.count_of_gast[gast] > 3:
                                                self.log_boss('Now I have a patch with ' + str(self.count_of_gast[gast]))
                            # correct the minedirection administration for the next look.
                            if scv.is_returning:
                                self.minedirection_of_scvt[scvt] = 'R'
                            if scv.is_gathering:
                                self.minedirection_of_scvt[scvt] = 'G'

    async def scv_endgame(self):
        # volunteer to idler
        for scv in self.units(SCV).idle:
            scvt = scv.tag
            if scvt in self.all_scvt: # of course
                if self.job_of_scvt[scvt] == 'volunteer':
                    self.promote(scv,'idler')
        # idler to volunteer
        if self.minerals < 999:
            for scvt in self.all_scvt:
                if self.job_of_scvt[scvt] == 'idler':
                    if len(self.mineral_field) > 0:
                        mim = self.mineral_field.random  # ? contains lastseen nonempty
                        tries = 0
                        while (mim.tag in self.all_mimt) and (tries<100):
                            tries += 1
                            mim = self.mineral_field.random
                        for scv in self.units(SCV):
                            if scv.tag == scvt:
                                self.promote(scv,'volunteer')
                                scv.gather(mim)

    def hop_cc(self):
        tomove = set()
        for cc in self.structures(COMMANDCENTER).ready + self.structures(ORBITALCOMMAND).ready:
            patches = 0
            for mim in self.mineral_field:
                if self.near(mim.position,cc.position,self.miner_bound):
                    patches +=1
            if patches < 4:
                tomove.add(cc)
        if len(tomove) > 0:
            moveto = set()
            for ccpos in self.expansion_locations_list:
                used = False
                for cc in self.all_bases:
                    if self.near(cc.position,ccpos,5):
                        used = True
                if not used:
                    patches = 0
                    for mim in self.mineral_field:
                        if self.near(mim.position, cc.position, self.miner_bound):
                            patches += 1
                    if patches >= 4:
                        moveto.add(ccpos)
            if len(moveto) > 0:
                minsd = 99999
                for cc in tomove:
                    for ccpos in moveto:
                        sd = self.sdist(cc.position,ccpos)
                        if sd < minsd:
                            bestcc = cc
                            bestccpos = ccpos
                            minsd = sd
                if minsd < 99999:
                    # hop bestcc to bestccpos
                    place_pos = self.init_cheese_position(bestccpos, 0, COMMANDCENTER)
                    if place_pos != self.nowhere:
                        if not bestcc.is_idle:
                            self.log_command('bestcc(AbilityId.CANCEL)')
                            bestcc(AbilityId.CANCEL)
                        self.home_of_flying_struct[bestcc.tag] = place_pos
                        self.landings_of_flying_struct[bestcc.tag] = 0
                        self.log_success('up base')
                        self.log_command('bestcc(AbilityId.LIFT')
                        bestcc(AbilityId.LIFT)
                        # give a hopped cc always an oc destiny
                        self.cc_destiny[place_pos] = 'oc'

    #*********************************************************************************************************************

    def clean_layout(self):
        self.routine = 'clean_layout'
#       designs: add tag to realized plans
        newdesigns = set()
        for (struc,place,tag) in self.designs:
            if tag == self.notag:
                for astruc in self.structures:
#                   the cc could have become a pf already, accept flying
                    if astruc.position == place:
                        tag = astruc.tag
            newdesigns.add((struc,place,tag))
        self.designs = newdesigns.copy()
#       designs: erase if neither tag nor plan is found
        erase = set()
        for (struc,place,tag) in self.designs:
            seen = False
            for astruc in self.structures:
#               the cc could have become a pf already, accept flying
                if tag == astruc.tag:
                    seen = True
            for scvt in self.goal_of_trabu_scvt:
                if place == self.goal_of_trabu_scvt[scvt]:
                    seen = True
            for (exething,exeplace,status) in self.buildorder_exe:
                if place == exeplace:
                    seen = True
            for (exething,exeplace) in self.recycling:
                if place == exeplace:
                    seen = True
            if place in self.tankplaces:
                seen = True
            if not seen:
                erase.add((struc,place,tag))
        for (struc,place,tag) in erase:
            self.erase_layout(struc,place)
        self.designs -= erase
 

#*********************************************************************************************************************
#   strategy system
#   a strategy is, per game_choice, a probability to choose "yes".
#   the game choices can be made at the start of the game and are unknown to the opponent.
#
#   We are fancy and feed back won-or-loss of a game to the strategy.
#
    def write_strategy(self):
        pl = open('data/strategy.txt','w')
        for nr in range(0,self.game_choices):
            stri = ''
            for spec in range(0,4):
                rou = round(self.strategy[spec][nr]*100000)/100000
                stri = stri+str(rou)+' '
            pl.write(stri+'\n')
        pl.close()


    async def init_strategy(self):
        # strategy is a list of chances to choose a strategic aspect.
        # e.g. radio_choices = 3, then the first 3 chances should add up to 1
        # The rest of the choices is free (between 0 and 1)
        self.routine = 'init_strategy'
        # blind init strategy    
        self.strategy = []    
        for spec in range(0, 4):
            astrategy = []
            for i in range(0,self.game_choices):
                astrategy.append(0.5)
            self.strategy.append(astrategy)    
        # read from disk
        pl = open('data/strategy.txt','r')
        read_strategy = pl.read().splitlines()
        pl.close()
        for nr in range(0,len(read_strategy)):
            woord = read_strategy[nr].split()
            for spec in range(0, 4):
                self.strategy[spec][nr] = float(woord[spec])
        # enemy species
        if self.enemy_race == Race.Zerg:
            self.species = 0
        elif self.enemy_race == Race.Terran:
            self.species = 1
        elif self.enemy_race == Race.Protoss:
            self.species = 2
        else:
            self.species = 3
        spec = self.species    
        # radio tuning
        sum = 0.0
        for nr in range(0,self.radio_choices):
            sum = sum + self.strategy[spec][nr]
        for nr in range(0,self.radio_choices):
            self.strategy[spec][nr] = self.strategy[spec][nr] / sum
        # init game_choice
        self.game_choice = []
        # find radio_nr with an overwrite calculation
        radio_nr = 0
        sum = 0.0
        for nr in range(0,self.radio_choices):
            sum = sum + self.strategy[spec][nr]
            if random.random() * sum < self.strategy[spec][nr]:
                radio_nr = nr
        # TO TEST use next line
        radio_nr = 12
        for nr in range(0,self.radio_choices):
            self.game_choice.append(nr == radio_nr)
        for nr in range(self.radio_choices,self.game_choices):
            self.game_choice.append(random.random() < self.strategy[spec][nr])
        self.game_result = 'doubt'

    async def win_loss(self):
        # win means "the opening went well"
        self.routine = 'win_loss'
        spec = self.species
        if self.game_result == 'doubt':
            max_cc_health = 0
            for cc in self.all_bases:
                if cc.health > max_cc_health:
                    max_cc_health = cc.health
            if self.supply_used>190:
                self.game_result = 'win'
                self.log_success('probably a win')
                for nr in range(0,self.game_choices):
                    if self.game_choice[nr]:
                        self.strategy[spec][nr] = 0.9*self.strategy[spec][nr]+0.1
                    else:
                        self.strategy[spec][nr] *= 0.9
            elif max_cc_health < 500:
                self.game_result = 'loss'
                self.log_success('probably a loss')
                self.surrender = True
                for nr in range(0, self.game_choices):
                    addum = 0.1
                    if nr < self.radio_choices:
                        addum = 0.1 / self.radio_choices
                    if self.game_choice[nr]:
                        self.strategy[spec][nr] *= 0.9
                    else:
                        self.strategy[spec][nr] = 0.9*self.strategy[spec][nr]+addum
            # write
            if self.game_result in ['win','loss']:
                # min 0.02, max 0.98
                for nr in range(0, self.game_choices):
                    self.strategy[spec][nr] = max(self.strategy[spec][nr], 0.02)
                    self.strategy[spec][nr] = min(self.strategy[spec][nr], 0.98)
                # radio tuning
                sum = 0.0
                for nr in range(0, self.radio_choices):
                    sum = sum + self.strategy[spec][nr]
                for nr in range(0, self.radio_choices):
                    self.strategy[spec][nr] = self.strategy[spec][nr] / sum
                self.write_strategy()

#*********************************************************************************************************************

    def get_area(self,point) -> str:
        roundpoint = (round(point.x-0.5),round(point.y-0.5))
        stri = 'middle'
        if roundpoint in self.hometop:
            stri = 'home'
        elif roundpoint in self.enemytop:
            stri = 'enemy'
        return stri
            
    def walk_duration(self,pointa,pointb) -> float:
        areaa = self.get_area(pointa)
        areab = self.get_area(pointb)
        if areaa == areab:
            walk_dist = self.circledist(pointa, pointb)
        else:
            var1 = self.circledist(pointa,self.homeramp_pos) + self.circledist(self.homeramp_pos,pointb)
            var2 = self.circledist(pointa,self.enemyramp_pos) + self.circledist(self.enemyramp_pos,pointb)
            walk_dist = min(var1,var2)
        walk_dura = walk_dist / self.walk_speed
        return walk_dura

    async def do_hercule(self):
        if (len(self.all_scvt) >= 30):
            # next line needs the sieged for a very new Hercule
            if (self.hercule in self.units(SCV) + self.units(SIEGETANK) + self.units(SIEGETANKSIEGED)):
                if self.no_move_or_near(self.hercule,40,2):
                    goal = self.goal_of_unittag[self.hercule.tag]
                    if not self.near(self.hercule.position,goal,2):
                        # lift buildings etc
                        self.log_success('You can not stop Hercule!')
                        for sd in self.structures(SUPPLYDEPOT):
                            if self.near(sd.position, self.hercule.position, 5):
                                self.log_command('sd(AbilityId.MORPH_SUPPLYDEPOT_LOWER)')
                                sd(AbilityId.MORPH_SUPPLYDEPOT_LOWER)
                                self.log_success('Move out of the way, supplydepot')
                        for tnk in self.units(SIEGETANKSIEGED):
                            if self.near(tnk.position, self.hercule.position, 5):
                                self.log_success('Move out of the way, tank')
                                self.log_command('tnk(AbilityId.UNSIEGE_UNSIEGE)')
                                tnk(AbilityId.UNSIEGE_UNSIEGE)
                                if self.find_tobuildwalk_a_place(MISSILETURRET):
                                    goal = self.function_result_Point2
                                    self.go_move(tnk,goal)
                                    self.state_of_unittag[tnk.tag] = 'moving'
                        for kind in self.liftable:
                            if kind not in [COMMANDCENTER,ORBITALCOMMAND]:
                                for bu in self.structures(kind):
                                    if self.near(bu.position, self.hercule.position, 5):
                                        if not bu.is_idle:
                                            self.log_command('bu(AbilityId.CANCEL)')
                                            bu(AbilityId.CANCEL)
                                        if self.find_tobuildwalk_a_place(kind):
                                            goal = self.function_result_Point2
                                            self.write_layout(kind, goal)
                                            self.home_of_flying_struct[bu.tag] = goal
                                            self.landings_of_flying_struct[bu.tag] = 0
                                            self.log_success('Move out of the way, ' + kind.name)
                                            self.log_command('bu(AbilityId.LIFT')
                                            bu(AbilityId.LIFT)
                    # reached, get a new goal
                    # preferred dist 30.
                    best = 99999
                    while best == 99999:
                        for tries in range(0, 99):
                            place = self.random_mappoint()
                            dist = self.circledist(self.hercule.position, place)
                            good = abs(dist - 30)
                            if good < best:
                                if self.check_layout(MISSILETURRET, place):
                                    goal = place
                                    best = good
                    if self.random_chance(20):
                        goal = self.shipyard
                    self.go_move(self.hercule, goal)
            else: # no hercule
                # make a hercule
                self.log_success('Making a Hercule')
                got_one = False
                for tnk in self.units(SIEGETANK) + self.units(SIEGETANKSIEGED):
                    if tnk.tag not in self.special_tags:
                        if not got_one:
                            got_one = True
                            self.special_tags.add(tnk.tag)
                            self.hercule = tnk
                            if tnk in self.units(SIEGETANKSIEGED):
                                self.log_command('tnk(AbilityId.UNSIEGE_UNSIEGE)')
                                tnk(AbilityId.UNSIEGE_UNSIEGE)
                            self.go_move(self.hercule,self.shipyard)
                for scv in self.units(SCV):
                    if not got_one:
                        job = self.job_of_scvt[scv.tag]
                        if job in self.bad_jobs + self.no_jobs:
                            got_one = True
                            self.special_tags.add(scv.tag)
                            self.hercule = scv
                            self.promote(scv,'hercule')
                            self.go_move(self.hercule,self.shipyard)
        else: # few scvs
            if (self.hercule in self.units(SCV)):
                self.promote(self.hercule,'idler')
            if self.hercule is not None:
                if self.hercule.tag in self.special_tags:
                    self.special_tags.remove(self.hercule.tag)
            self.hercule = None


#*********************************************************************************************************************

    def get_nuke_target(self):
        # -> self.nuke_target
        self.nuke_target = self.enemyloc
        bestnears = 0
        for ene in self.enemy_structures:
            nears = 0
            for are in self.enemy_structures:
                if self.near(ene.position,are.position,4):
                    nears += 1
            if nears > bestnears:
                bestnears = nears
                self.nuke_target = ene.position


    async def ghost_fun(self):
        self.routine = 'ghost_fun'
        if self.ghost_phase > 'A':
            self.log_success('ghost_phase '+self.ghost_phase)
        if self.ghost_calmdown > 0:
            self.ghost_calmdown -= 1
        # fall back
        if self.we_started_amount(GHOSTACADEMY) < 1:
            self.ghost_phase = min('B',self.ghost_phase)
        if self.we_started_amount(BARRACKS) < 2: # Force second barracks as the first sometimes cannot lab.
            self.ghost_phase = min('B',self.ghost_phase)
        if self.we_started_amount(BARRACKSTECHLAB) < 1:
            self.ghost_phase = min('B',self.ghost_phase)
        if self.we_started_amount(FACTORY) < 1:
            self.ghost_phase = min('B', self.ghost_phase)
        if self.we_started_amount(GHOST) < 1:
            self.ghost_phase = min('C', self.ghost_phase)
        # phases
        if self.ghost_phase == 'A':
            #continue
            if (self.supply_used > 180):
                self.ghost_phase = 'B'
        elif self.ghost_phase == 'B':
            # build buildings
            done = 0
            if self.we_started_amount(GHOSTACADEMY) < 1:
                if self.ghost_calmdown == 0:
                    self.throw_if_rich(GHOSTACADEMY,'ghost_fun',1)
                    self.ghost_calmdown = 10
            else:
                done += 1
            if self.we_started_amount(BARRACKS) < 2:
                if self.ghost_calmdown == 0:
                    self.throw_if_rich(BARRACKS, 'ghost_fun', 1)
                    self.ghost_calmdown = 10
            else:
                done += 1
            if self.we_started_amount(BARRACKSTECHLAB) < 1:
                self.throw_if_rich(BARRACKSTECHLAB, 'ghost_fun', 1)
            else:
                done += 1
            if self.we_started_amount(FACTORY) < 1:
                if self.ghost_calmdown == 0:
                    self.throw_if_rich(FACTORY, 'ghost_fun', 1)
                    self.ghost_calmdown = 10
            else:
                done += 1
            # continue
            if done >= 4:
                self.ghost_phase = 'C'
        elif self.ghost_phase == 'C':
            # buildings are started
            # build cloack, ghosts, nukes
            # cloack goes via upgrades
            done = 0
            if self.we_started_amount(GHOST) < 1:
                if self.ghost_calmdown == 0:
                    self.throw_if_rich(GHOST,'ghost_fun',1)
                    self.ghost_calmdown = 10
            else:
                done += 1
            if self.we_started_amount(PERSONALCLOAKING) == 1:
                done += 1
            for ga in self.structures(GHOSTACADEMY).ready.idle:
                if self.can_pay(NUKESILONOVA):
                    ga(AbilityId.BUILD_NUKE)
            done += self.we_started_amount(NUKESILONOVA)
            if done >= 3:
                self.ghost_phase = 'D'
                #init
                for ghost in self.units(GHOST):
                    self.go_move(ghost,self.shipyard)
        elif self.ghost_phase == 'D':
            # wait for ghost some energy, nuke, restdura max 20 sec
            # continue
            done = 0
            if len(self.units(GHOST)) >= 1:
                done += 1
            for ghost in self.units(GHOST):
                if ghost.energy < 100:
                    done -= 1
            if self.we_started_amount(NUKESILONOVA) >= 1:
                done += 1
            for (bar, martype, pos, dura) in self.eggs:
                if (martype == NUKESILONOVA) and (dura > 20):
                    done -= 1
            if done >= 2:
                self.ghost_phase = 'E'
                # init
                self.get_nuke_target()
                target = self.nuke_target
                radius = 12
                tooclose = True
                tries = 0
                while (tries < 100) and tooclose:
                    tries += 1
                    x = target.x + random.randrange(-radius, radius)
                    y = target.y + random.randrange(-radius, radius)
                    goal = Point2((x, y))
                    tooclose = False
                    for ene in self.enemy_structures:
                        if ene.type_id in self.antiair_detector:
                            if self.near(goal, ene.position, 11):
                                tooclose = True
                for ghost in self.units(GHOST):
                    self.go_move(ghost,goal)
        elif self.ghost_phase == 'E':
            # moving to goals
            done = 0
            for ghost in self.units(GHOST):
                if self.near(ghost.position,self.nuke_target,70):
                    if AbilityId.BEHAVIOR_CLOAKON_GHOST in await self.get_available_abilities(ghost):
                        ghost(AbilityId.BEHAVIOR_CLOAKON_GHOST)
                if ghost.tag in self.goal_of_unittag: # dont ask me, it occurred
                    if not self.no_move(ghost,8):
                        done -= 1
            if done >= 0:
                self.ghost_phase = 'F'
        elif self.ghost_phase == 'F':
            # goal reached
            # call nuke
            done = 0
            for ghost in self.units(GHOST):
                if AbilityId.TACNUKESTRIKE_NUKECALLDOWN in await self.get_available_abilities(ghost):
                    ghost(AbilityId.TACNUKESTRIKE_NUKECALLDOWN, self.nuke_target)
                    done += 1
            # continue
            if done >= 1:
                self.ghost_calmdown = 10
                self.ghost_phase = 'G'
        elif self.ghost_phase == 'G':
            # waiting for strike
            if self.ghost_calmdown == 0:
                self.ghost_phase = 'H'
                # init
                for ghost in self.units(GHOST):
                    self.go_move(ghost,self.shipyard)
        elif self.ghost_phase == 'H':
            # walking home
            done = 0
            for ghost in self.units(GHOST):
                if not self.near(ghost.position,self.nuke_target,70):
                    if AbilityId.BEHAVIOR_CLOAKOFF_GHOST in await self.get_available_abilities(ghost):
                        ghost(AbilityId.BEHAVIOR_CLOAKOFF_GHOST)
                if not self.no_move(ghost,8):
                    done -= 1
            # continue
            if done >= 0:
                self.ghost_phase = 'C'
                # init
                for ghost in self.units(GHOST):
                    if AbilityId.BEHAVIOR_CLOAKOFF_GHOST in await self.get_available_abilities(ghost):
                        ghost(AbilityId.BEHAVIOR_CLOAKOFF_GHOST)

#*********************************************************************************************************************
def main():
    # Easy/Medium/Hard/VeryHard
    all_maps = ['OxideLE','PillarsofGoldLE','RomanticideLE','SubmarineLE','DeathauraLE','JagannathaLE','LightshadeLE']
    map = random.choice(all_maps)
    # TO TEST use next line
    #map = 'LightshadeLE'
    opponentspecies = random.choice([Race.Terran,Race.Zerg,Race.Protoss])
    # TO TEST use next line
    #opponentspecies = Race.Zerg
    run_game(maps.get(map), [
        Bot(Race.Terran, Chaosbot()),
        Computer(opponentspecies, Difficulty.VeryHard)
        ], realtime = True)

if __name__ == "__main__":
    main()
