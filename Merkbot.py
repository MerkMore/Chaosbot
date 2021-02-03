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
import time
from math import sqrt,cos,sin,pi,acos
from sc2.game_info import GameInfo
from layout_if_py import layout_if
from rocks_if_py import rocks_if
from bunker_if_py import bunker_if
from version_if_py import version_if
# from sc2.constants import *
from sc2.ids.unit_typeid import SCV
from sc2.ids.unit_typeid import RAVEN
from sc2.ids.unit_typeid import STARPORT
from sc2.ids.unit_typeid import VIKINGFIGHTER
from sc2.ids.unit_typeid import MARINE
from sc2.ids.unit_typeid import BARRACKS
from sc2.ids.unit_typeid import BUNKER
from sc2.ids.unit_typeid import MARAUDER
from sc2.ids.unit_typeid import REAPER
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
from sc2.ids.unit_typeid import TECHLAB
from sc2.ids.unit_typeid import SENSORTOWER
from sc2.ids.unit_typeid import GHOSTACADEMY
from sc2.ids.unit_typeid import BARRACKSREACTOR
from sc2.ids.unit_typeid import FACTORYREACTOR
from sc2.ids.unit_typeid import STARPORTREACTOR
from sc2.ids.unit_typeid import REACTOR
from sc2.ids.upgrade_id import PUNISHERGRENADES
from sc2.ids.upgrade_id import STIMPACK
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
from sc2.ids.upgrade_id import TERRANINFANTRYARMORSLEVEL1
from sc2.ids.upgrade_id import TERRANINFANTRYARMORSLEVEL2
from sc2.ids.upgrade_id import TERRANINFANTRYARMORSLEVEL3
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
# mark possible expansions:
from sc2.ids.unit_typeid import MAINCELLBLOCK
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
from sc2.ids.unit_typeid import ORACLESTASISTRAP
# zerg
from sc2.ids.unit_typeid import EXTRACTOR
from sc2.ids.unit_typeid import SPAWNINGPOOL
from sc2.ids.unit_typeid import SPINECRAWLER
from sc2.ids.unit_typeid import EVOLUTIONCHAMBER
from sc2.ids.unit_typeid import ROACHWARREN
from sc2.ids.unit_typeid import BANELINGNEST
from sc2.ids.unit_typeid import HYDRALISKDEN
from sc2.ids.unit_typeid import LURKERDEN
from sc2.ids.unit_typeid import SPIRE
from sc2.ids.unit_typeid import GREATERSPIRE
from sc2.ids.unit_typeid import NYDUSNETWORK
from sc2.ids.unit_typeid import NYDUSCANAL
from sc2.ids.unit_typeid import INFESTATIONPIT
from sc2.ids.unit_typeid import ULTRALISKCAVERN
from sc2.ids.unit_typeid import CREEPTUMOR
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
    do_version410 = False
    do_slowdown = False
    do_log_success = False
    do_log_fail = False
    do_log_command = False
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
    do_log_event = False
    do_log_time = False
    do_log_layout = False
    do_log_cheese = False
    do_log_boss = False
    do_log_thoughts = False
    do_log_preps = False
    do_log_eggs = False
    do_log_birds = False
    do_log_buildstate = False
    do_log_throw = False
    do_log_throwspots = False
    do_log_bunker = False
    do_log_earn = False
    do_log_orders = False
    do_log_buildorder = False
    #   ############### CONSTANT
    #   constant over the frames after frame 0:
    chosen_game_step = 2 # the amount of frames between program-step-runs
    frame = 0 # will have even numbers if game_step=2
    frames_per_second = 22.4 # a gameclient property
    #
    reaper_speed_official = 5.25
    scv_speed_official = 3.94
    # The circledistance a unit travels per frame.
    reaper_step = reaper_speed_official / frames_per_second
    scv_step = scv_speed_official / frames_per_second
    # other
    # strength = sqrt(dps * (health + shield))
    # without armor, splash, focussing or upgrades, a fight will be dependant on strength
    marine_strength = 21
    worker_strength = 15
    bc_strength = 165.5
    pf_strength = 245
    cannon_strength = 82
    #
    nowhere = Point2((1,1))
    somewhere = Point2((2,2))
    fixed_somewhere = Point2((0,0))
    notag = -1
    patience = 100 # amount of frames to retry building etc.
    gracetime = 20 # amount of frames may-not-idle
    all_structures = []
    all_structures_tobuildwalk = []
    all_army = []
    all_labarmy = []
    all_workertypes = []
    all_upgrades = []
    all_labs = [] # for labs, with place, always its motherbuilding place will be used.
    standalone_labs = [] # TECHLAB, REACTOR
    all_pfoc = []
    basekind_of_kind = {}
    antiair_detector = [] # cannons
    supply_of_army = {}
    airground_of_unit = {} # 'air'/'ground'
    builddura_of_thing = {}
    size_of_structure = {}
    species_of_structure = {}
    liftable = []
    techtree = []
    all_species_things = set()
    cradle = []
    shipyard = None
    viking_targets = []
    landable = []
    all_repairable_shooters = set()
    thingtag_of_repairertag = {} # for repairers
    hometop = set() # empty squares near start, inside the wall, inside ramps
    homeramp_pos = None
    enemytop = set() # empty squares near enemy_pos
    enemyramp_pos = None
    enemynatural_pos = None
    enemythird_pos = None
    enemynaturalchoke_pos = None
    bcenemies = set()
    danger_of_bcenemy = {}
    hate_of_bcenemy = {}
    nobuild_path = set()
    set_rally = set() # of (point where a building comes, the rallypoint that is not set yet)
    # timing constants
    gas_speed = 0.95 # simplified from liquipedia
    mim_speed = 0.95
    # empirical value, fit to the euclid walkdistance with slight underestimation
    walk_speed = 2.8
    #
    miner_bound = 10
    enemy_pos = None
    loved_pos = None
    loved_expo = 0
    target_loc = None
    map_left = 0
    map_right = 0
    map_bottom = 0
    map_top = 0
    #
    flee_circle = []
    #
    maxhealth = {}  # per unit the health_max
    #
    #   ############### grouping by expo
    maptile_width = 10
    maptile_half = maptile_width // 2
    maptile_amount = (200+maptile_half) // maptile_width
    maptiles = maptile_amount * maptile_amount
    expos = 0 # expansionlocations
    expo_of_maptile = {}
    pos_of_expo = {}
    minerals_of_expo = {} # mineral_field
    vespene_of_expo = {} #
    units_of_expo = {} # units
    scvs_of_expo = {} # units(SCV)
    structures_of_expo = {} # structures
    enemy_units_of_expo = {} # enemy_units
    enemy_structures_of_expo = {} # enemy_structures
    # strength = dps * health
    ground_strength_of_expo = {} # strength of me minus enemy
    air_strength_of_expo = {} # strength of me minus enemy
    worth_of_expo = {} # positive, only buildings: mineralcost + 2*gascost
    #
    #   ############### GAMESTATE
    #   gamestate values constant in this frame after gamestate:
    all_bases = []
    all_refineries = []
    army_supply = 0
    all_scvtags = set() # simple, no limbo like in all_scvt
    all_basetags = set() # simple
    all_structuretags = set() # simple
    all_bunkertags = set() # simple
    # some average counts related to supply from some gsl games:
    supply_rate = 0.17
    good_worker_supply = 0
    good_army_supply = 0
    good_bases = 0
    good_armybuildings = 0
    good_upgradebuildings = 0
    #   ############### REST
    circle = []
    # thought -> prep -> egg -> bird
    preps = set() # (martype,bartype,pos,dura,owner) or (thingtype,scv,buildpos,dura,owner)
    eggs = set() # (martype,bartype,buildingpos,dura) or (thingtype,scv,buildpos,dura)
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
    tips_used = set()
    #   coding problem
    function_result_Point2 = None
    doubling_frame = {}
    # idle in this frame:
    idle_structure_tags = []
    neighbours = set()
    #   ############### ARMY AND STRUCTURE MANAGEMENT
    rushopening = False
    opening_create_units = 0
    opening_create_kind = None
    opening_create_hadmax = 0
    marine_attacked = False
    marine_opening_bases = 0
    marine_attackframe = 0
    marine_goal = nowhere
    flown_in = set() # to fly in just once
    liberator_spots = set() # of [name,siegeattack,siegeship]
    libspot = {} # per liberatortag: [name,siegeattack,siegeship]
    lib_factory_tag = notag
    lib_turret_tries = 7
    lib_turpos = nowhere
    firstlib = True
    secondlib = False
    #
    vulture_pole = 0
    vulture_pos = []
    #
    # permanent means that this info about the enemy is kept when out of sight.
    enemy_buidings_permanent = {} # per tag the position
    #
    last_enemies = set() # of (tag,position)
    #
    yamatoed = {} # per enemytag the shootframe. To prevent a group of bcs overkilling the same target.
    #
    last_health = {}
    #   army coodination
    goal_of_unittag = {} # control of unit movement
    last_sd_of_unittag = {} # control of unit movement
    shame_of_unittag = {} # control of unit movement
    detour_of_unittag = {} # control of unit movement
    #
    special_tags = set()    # walldepots, wallbarracks, ...
                            # cheese_tank, cheese_scv, ...
    bunker_marines = set()
    cleaning_tank_tags = set()
    cleaning_object_found = False
    cleaning_object_tag = notag
    cleaning_object_pos = nowhere
    cleaning_tank_siegepos = {}
    cleaning_tank_shotframe = {}
    cleaning_tank_trailnr = {}
    #
    emotion_of_unittag = {} # jumpy bc emotion "lazy","repair", etc. Also for tanks.
    burrowpos_of_wmt = {}
    attack_type = 'jumpy'
    cruisercount = 0
    lastcruisercount = 0
    goal_of_flying_struct = {} # initially its own position
    landings_of_flying_struct = {}
    bestbctag = notag
    bestbc_dist_to_goal = 99999
    bc_fear = 250
    lasttargettag_of_bctag = {}
    homepole_of_wmt = {} # for cheesemines a scoutplace near goal
    pole_of_wmt = {} # for cheesemines a next scoutplace
    phase_of_wmt = {} # for cheesemines attack or flee
    marauder_goal = Point2((100,100))
    viking_goal  = Point2((100,100))
    #
    trail = {} # per unittag, of the last 10 seconds, the position
    #
    tankplaces = set()
    ambition_of_strt = {} # ambition contains labs, pfoc  just before actual build
    gym_of_strt = {} # reserve structure to soon train upgr, army
    ambitiondura = 10 # less than scv_build_time 12
    gymdura = 8 # less than ambitiondura, so upgrade cc works
    owner_of_ambigymstrt = {}
    army_center_point = None
    #   (struc,place,tag) for tobuildwalk plans with a layout. Administrate to enable erasing.
    designs = set()
    # wall
    wall_barracks_pos = None
    wall_depot0_pos = None
    wall_depot1_pos = None
    wall = set() # ((SUPPLYDEPOT, point), ...)
    #
    reaper_status = {}
    reaper_focus = nowhere
    reaper_ideal_dist = 7
    advice_text = 'run' # 'hit'/'run'
    advice_goal = nowhere # Point2 if 'run'
    advice_hit = None # Unit if 'hit'
    reaper_barracks_pos = nowhere
    reaper_bunker1_pos = nowhere
    reaper_bunker2_pos = nowhere
    reaper_prison_pos = nowhere
    reaper_center = nowhere
    forcex = 0
    forcey = 0
    compensatorx = 0
    compensatory = 0
    remember_terrain = {} # per alfasegment a tuple (compensatorx, compensatory, signature)
    #
    #   A barracks close to the enemy has to fly from build position to attack position
    cheese_barracks_pos = nowhere
    cheese_factory_pos = nowhere
    cheese_starport_pos = nowhere
    cheese_landing_pos = nowhere
    cheese_bunker_pos = nowhere
    cheese_prison_pos = nowhere
    cheese_tank_pos = nowhere
    cheese_phase = 'A'
    cheese_barracks_tag = notag
    cheese_factory_tag = notag
    cheese_starport_tag = notag
    cheese_bunker_tag = notag
    cheese_scv_tag = notag
    cheese_marine_tags = set()
    cheese_marine_count = 0
    cheese_tank_count = 0
    cheese_mine_count = 0
    cheese_tank_tag = notag
    cheese_mine_tags = set()
    cheese_frames = 0
    # cheese2
    cheese2_bunkspots = set()
    cheese2_triedexp = set()
    wished_marines_per_bunker = 2
    # cheese3
    chosenplaces = []
    cheese3_phase = 'A'
    cheese3_barracks_pos = nowhere
    cheese3_bunker_pos = nowhere
    cheese3_cc_pos = nowhere
    cheese3_landing_pos = nowhere
    cheese3_prison_pos = nowhere
    cheese3_barracks_tag = notag
    cheese3_bunker_tag = notag
    cheese3_cc_tag = notag
    # for cocoon:
    cheese3_cocoon_pos = nowhere
    cheese3_barracks2_pos = nowhere
    cheese3_bunker2_pos = nowhere
    cheese3_barracks2_tag = notag
    cheese3_bunker2_tag = notag
    #
    ghost_phase = 'A'
    ghost_calmdown = 0
    nuke_target = None
    #
    cc_destiny_rush = False
    cc_destiny = {} # [pos] = 'oc'/'pf'
    #
    # painted on the layout, so as not to build other things there. Yet can place cc there.
    possible_cc_positions = set()
    #
    #   ############### SCV MANAGEMENT
    #   traveller -> settler -> fencer -> builder scvs have a goal
    #   traveller, settler, fencer and builder scvs have a structure to build
    goal_of_trabu_scvt = {}
    structure_of_trabu_scvt = {}
    owner_of_trabu_scvt = {}
    #   scv management:
    #   The tag of existing own scvs, in this frame. scvs in limbo included.
    all_scvt = []
    #   The tag of existing refineries where we want to mine from, in this frame
    all_gast = []
    #   The tag of existing minerals where we want to mine from, in this frame
    all_mimt = []
    #   job_of_scvt dictionary
    good_jobs = ('builder','settler','fencer','traveller','gasper','repairer','escorter','scout','cheeser')
    bad_jobs = ('gasminer','mimminer','applicant','defender')
    no_jobs = ('idler','suicider','volunteer','inshock','fleeer')
    #
    jobs_may_idle = ('fencer','settler','scout','cheeser','applicant','idler','gasper')
    #
    expected_orders = set()
    #
    job_of_scvt = {}
    count_of_job = {}
    #   applicants have a vision, a tag of a base to walk to
    vision_of_scvt = {}
    #   recalculated each frame:
    wanted_of_cct = {}
    #   gas harvesting assignments
    gast_of_scvt = {}
    count_of_gast = {}
    #   mineral harvesting assignments
    mimt_of_scvt = {}
    count_of_mimt = {}
    lazyness_of_scvt = {} # per tag idling scv, the amount of frames it idles
    #   defenders attack something
    targettag_of_defendertag = {}
    last_center_enemies = nowhere
    #   for missing scvs (fallen or in gaslimbo), the frame is stored
    frame_of_missing_scvt = {}
    #   fun translate output scvt to names
    all_names = []
    name_of_scvt = {}
    # scout1 enemy_pos
    scout1_pos = []
    scout1_tag = notag
    scout1_pole = 0
    # scout2 grande tour
    scout2_pos = []
    scout2_tag = notag
    scout2_pole = 0
    scout2_direction = 1
    # blocker
    blocker_pos = []
    blocker_tag = notag
    blocker_pole = 0
    # checks
    minedirection_of_scvt = {}
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
    extra_planning = [] # for automatic production of scvs, supplydepots etc
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
    throwspots = [] # (thing spot status='new'/'thought' owner prio=1/2/3)     (thing,spot) will be unique
    #
    but_i_had_structures = 0 # amount of own structures, excl bunkers
    but_i_had_flying = 0 # make new plans if a weak building lifted
    #
    # next structures are to retry when stopped by mappart occupied
    buildandretry = set() # (scvt, building, goal, frame) for tobuildwalk buildings
    trainandretry = set() # (oldbuildingtag, newbuilding, frame) for labs and pfoc
    purse = Cost(0,0) # to reserve the cost for the retry
    #
    midgame_things = []
    #   the current sit for the buildseries
    sit_exist = {}   # for a thing: the dura until the first one will be ready
    sit_free = []   # (thing, freedura)
    #   to capture the current situation for the planning:
    situation_walking = set() # for tobuildwalk
    situation_constructing = set() # for tobuildwalk
    situation_gym = set() # for army and upgrade
    situation_training = set() # for army and upgrade
    situation_ambition = set() # for pfoc and lab
    situation_growing = set() # for pfoc and lab
    situation_thingkinds = set()
    situation_buildings_and_parts = set()
    situation_events = set()
    #
    production_pause = set() # of (thing, amount, building, bam). Postpone adlib thing production at amount, until bam buildings are finished.
    # to abort plans
    buildorderdelay = 0
    crad_places = set()
    bui_min_lab = {}
    bui_of_pos = {}
    happy_made = set()
    #   strategy[0] is vs Zerg []
    strategy = []
    game_choice = []
    radio_choices = 26
    game_choices = 52
    game_result = 'doubt'
    opening_name = 'no'
    #
    # internal model for earnings:
    earn_mim = 0
    earn_gas = 0
    earn_supply_left = 0
    earn_supply_used = 0
    earn_supply_cap = 0
    earn_supply_egg = 0 # 4 for every supplydepot under construction
    earn_tags = set()
    earn_halls = set()
    earn_orbitals = set()
    earn_growing = set()
    earn_refineries = set()
    earn_scvs = set()
    earn_mimmers = set()
    earn_gassers = set()
    earn_idlers = set()
    earn_specials = set()
    earn_builders = set()
    earn_show = True
    #

    # *********************************************************************************************************************
    async def on_start(self):
        self._client.game_step = self.chosen_game_step
        if self.do_version410:
            version_if.version410()

    async def on_step(self, iteration: int):
        self.frame = iteration * self.chosen_game_step
        # init stuff
        if len(self.techtree) == 0:
            await self.my_init()
        #
        #       main iteree:
        #
        #  interface
        bunker_if.init_step(self)
        #
        self.slowed_down()
        self.init_step_expo()
        await self.gamestate()
        self.get_eggs()
        self.get_preps() # after get_eggs
        await self.get_birds()
        self.log_thoughts() # there is no get_thoughts()
        self.log_resource()
        self.log_armysize()
        self.log_bcs()
        self.log_orders()
        self.check_shipyard() # after gamestate, before buildorder stuff
        await self.manage_workers() # before planning
        if self.minerals < self.vespene:
            await self.manage_minerals()
            await self.manage_gas()
        else:
            await self.manage_gas()
            await self.manage_minerals()
        await self.manage_rest()
        await self.bunker_handling()
        await self.bunkercheese()
        await self.bunkercheese2()
        if (self.frame % 5 == 4):
            await self.implementing_buildorder_exe()
            await self.make_planning_exe()
            await self.follow_planning_exe()
        await self.build_worker(100-self.minerals//100)
        await self.throw_advance()
        await self.start_construction()
        await self.siege_tanks()
        await self.use_mine()
        await self.bc_micro()
        await self.raven_micro()
        await self.battle_dodge_bile()
        self.liberator()
        await self.destroyed()
        await self.deserted()
        await self.repair_bc()
        self.do_repair()
        if (self.frame % 7 == 6):
            await self.supplydepots_adlib()
            self.delaying_too_much()
            await self.build_minima()
            await self.refineries_adlib()
            await self.upgrades_adlib()
            self.army_adlib()
            self.armybuildings_adlib()
            self.expansion_advisor()
            self.turrets_adlib()
            await self.lift()
            self.do_rally()
            self.opening_create_cut()
        await self.manage_the_wall()
        await self.cheese_army()
        await self.attack_with_bc()
        await self.attack_with_rest()
        await self.worker_defence()
        await self.scv_endgame()
        if (self.frame % 11 == 10):
            await self.win_loss()
            await self.mimminer_boss()
            await self.gasminer_boss()
        if (self.frame % 31 == 30):
            self.clean_layout()
            self.clean_doubling()
            self.lower_some_depots()
            self.hop_cc()
            self.yamato_admin()
        await self.mules()
        if (self.frame % 3 == 2):
            await self.do_buildandretry()
            await self.do_trainandretry()
        await self.do_pf_rush()
        await self.do_cocoon()
        self.do_reaper()
        await self.catch_a_bug()
        self.log_throwspots()
        self.extreme_spender()
        self.blocker()
        await self.ghost_fun()
        bunker_if.step()
        self.vulture()
        self.marine_fun()
        #
        # preparation for next step
        self.get_last_enemies()
        self.get_last_health()
        self.get_trail()
        #



    # *********************************************************************************************************************
    async def my_init(self):
        self.routine = 'my_init'
        self.log_success('##############################################################################')
        random.seed()
        self.init_expo()
        # expected_order
        self.init_expected_order('mimminer', AbilityId.HARVEST_RETURN)
        self.init_expected_order('mimminer', AbilityId.HARVEST_GATHER)
        self.init_expected_order('gasminer', AbilityId.HARVEST_RETURN)
        self.init_expected_order('gasminer', AbilityId.HARVEST_GATHER)
        self.init_expected_order('volunteer', AbilityId.HARVEST_RETURN)
        self.init_expected_order('volunteer', AbilityId.HARVEST_GATHER)
        self.init_expected_order('inshock', AbilityId.MOVE)
        self.init_expected_order('fleeer', AbilityId.MOVE)
        self.init_expected_order('traveller', AbilityId.MOVE)
        self.init_expected_order('settler', AbilityId.MOVE)
        self.init_expected_order('fencer', AbilityId.MOVE)
        self.init_expected_order('escorter', AbilityId.ATTACK)
        self.init_expected_order('applicant', AbilityId.MOVE)
        self.init_expected_order('scout', AbilityId.MOVE)
        self.init_expected_order('suicider', AbilityId.ATTACK)
        self.init_expected_order('defender', AbilityId.ATTACK)
        self.init_expected_order('repairer',AbilityId.EFFECT_REPAIR)
        # liftable
        self.liftable = [BARRACKS,FACTORY,STARPORT,COMMANDCENTER,ORBITALCOMMAND]
        self.landable = [BARRACKSFLYING,FACTORYFLYING,STARPORTFLYING,COMMANDCENTERFLYING,ORBITALCOMMANDFLYING]
        # enemy air with weak air defence, and fighters
        self.viking_targets = [BANSHEE,LIBERATOR,LIBERATORAG,ORACLE,BROODLORD,OVERLORD,OBSERVER,BATTLECRUISER,
                               CORRUPTOR,MUTALISK,TEMPEST,VIPER, VIKINGFIGHTER,PHOENIX]
        # townhalls
        self.hall_types = [COMMANDCENTER, ORBITALCOMMAND, PLANETARYFORTRESS, HATCHERY, LAIR, HIVE, NEXUS]
        # enemy that can hurt a bc, danger (run at sum 100), hate (shoot high first)
        self.init_bcenemy(ARCHON, 40, 5)
        self.init_bcenemy(CARRIER, 20, 4)
        self.init_bcenemy(QUEEN, 40, 4)
        self.init_bcenemy(CORRUPTOR, 35, 5)
        self.init_bcenemy(SPORECRAWLER, 60, 6)
        self.init_bcenemy(PHOTONCANNON, 60, 6)
        self.init_bcenemy(INFESTOR, 40, 6)
        if self.enemy_race != Race.Zerg:
            self.init_bcenemy(BATTLECRUISER, 50, 3)
            self.init_bcenemy(VIKINGFIGHTER, 35, 5)
            self.init_bcenemy(MISSILETURRET, 60, 6)
            self.init_bcenemy(THOR, 40, 3)
            self.init_bcenemy(PHOENIX, 35, 5)
            self.init_bcenemy(MARINE, 10, 2)
            self.init_bcenemy(SCV, 0, 1)
        self.init_bcenemy(HYDRALISK, 20, 3)
        self.init_bcenemy(VIPER, 30, 4)
        self.init_bcenemy(VOIDRAY, 35, 5)
        self.init_bcenemy(RAVAGER, 20, 2)
        self.init_bcenemy(CYCLONE, 50, 3)
        self.init_bcenemy(STALKER, 30, 4)
        self.init_bcenemy(SENTRY, 10, 4)
        self.init_bcenemy(HIGHTEMPLAR, 10, 4)
        self.init_bcenemy(TEMPEST, 20, 5)
        self.init_bcenemy(DRONE,0,1)
        self.init_bcenemy(PROBE,0,1)
        # anti-air detector structure
        self.antiair_detector = [MISSILETURRET,PHOTONCANNON,SPORECRAWLER]
        # all_labs wegens verschoven plaatsing etc
        self.all_labs = [BARRACKSTECHLAB,FACTORYTECHLAB,STARPORTTECHLAB,BARRACKSREACTOR,FACTORYREACTOR,STARPORTREACTOR,TECHLAB,REACTOR]
        self.standalone_labs = [TECHLAB,REACTOR]
        self.all_pfoc = [PLANETARYFORTRESS,ORBITALCOMMAND]
        self.all_workertypes = [SCV,PROBE,DRONE]
        # list of structures, with builddura, size. Can be flying, can be lowered.
        self.init_structures('T',SUPPLYDEPOT, 21, 2)
        self.init_structures('T',SUPPLYDEPOTLOWERED, 21, 2)
        self.init_structures('T',BARRACKS, 46, 3)
        self.init_structures('T',BARRACKSFLYING, 46, 3)
        self.init_structures('T',REFINERY, 21, 3)
        self.init_structures('T',BARRACKSTECHLAB, 18, 2)
        self.init_structures('T',FACTORY, 43, 3)
        self.init_structures('T',FACTORYFLYING, 43, 3)
        self.init_structures('T',FACTORYTECHLAB, 18, 2)
        self.init_structures('T',STARPORT, 36, 3)
        self.init_structures('T',STARPORTFLYING, 36, 3)
        self.init_structures('T',STARPORTTECHLAB, 18, 2)
        self.init_structures('T',TECHLAB, 18, 2)
        self.init_structures('T',FUSIONCORE,46, 3)
        self.init_structures('T',COMMANDCENTER, 71, 5)
        self.init_structures('T',COMMANDCENTERFLYING, 71, 5)
        self.init_structures('T',PLANETARYFORTRESS, 36, 5)
        self.init_structures('T',ORBITALCOMMAND, 25, 5)
        self.init_structures('T',ORBITALCOMMANDFLYING, 25, 5)
        self.init_structures('T',ENGINEERINGBAY, 25, 3)
        self.init_structures('T',MISSILETURRET,18, 2)
        self.init_structures('T',ARMORY, 46, 3)
        self.init_structures('T',BUNKER, 29, 3)
        self.init_structures('T',SENSORTOWER, 18, 2)
        self.init_structures('T',GHOSTACADEMY, 20, 3)
        self.init_structures('T',BARRACKSREACTOR, 36, 2)
        self.init_structures('T',FACTORYREACTOR, 36, 2)
        self.init_structures('T',STARPORTREACTOR, 36, 2)
        self.init_structures('T',REACTOR, 36, 2)
        # protoss added for layout
        self.init_structures('P',NEXUS, 71, 5)
        self.init_structures('P',PYLON, 18, 2)
        self.init_structures('P',ASSIMILATOR, 21, 3)
        self.init_structures('P',GATEWAY, 46, 3)
        self.init_structures('P',FORGE, 32, 3)
        self.init_structures('P',PHOTONCANNON, 29, 2)
        self.init_structures('P',SHIELDBATTERY, 29, 2)
        self.init_structures('P',WARPGATE, 7, 3)
        self.init_structures('P',CYBERNETICSCORE, 36, 3)
        self.init_structures('P',TWILIGHTCOUNCIL, 36, 3)
        self.init_structures('P',ROBOTICSFACILITY, 46, 3)
        self.init_structures('P',STARGATE, 43, 3)
        self.init_structures('P',TEMPLARARCHIVE, 36, 3)
        self.init_structures('P',DARKSHRINE, 71, 2)
        self.init_structures('P',ROBOTICSBAY, 46, 3)
        self.init_structures('P',FLEETBEACON, 43, 3)
        self.init_structures('P',ORACLESTASISTRAP, 11, 1)
        # zerg
        self.init_structures('Z',HATCHERY, 71, 5)
        self.init_structures('Z',LAIR, 57, 5)
        self.init_structures('Z',HIVE, 71, 5)
        self.init_structures('Z',EXTRACTOR, 21, 3)
        self.init_structures('Z',SPAWNINGPOOL, 46, 3)
        self.init_structures('Z',SPINECRAWLER, 36, 2)
        self.init_structures('Z',SPORECRAWLER, 21, 2)
        self.init_structures('Z',EVOLUTIONCHAMBER, 25, 3)
        self.init_structures('Z',ROACHWARREN, 39, 3)
        self.init_structures('Z',BANELINGNEST, 43, 3)
        self.init_structures('Z',HYDRALISKDEN, 29, 3)
        self.init_structures('Z',LURKERDEN, 57, 3)
        self.init_structures('Z',SPIRE, 71, 3)
        self.init_structures('Z',GREATERSPIRE, 71, 3)
        self.init_structures('Z',NYDUSNETWORK, 36, 3)
        self.init_structures('Z',NYDUSCANAL, 14, 3)
        self.init_structures('Z',INFESTATIONPIT, 36, 3)
        self.init_structures('Z',ULTRALISKCAVERN, 46, 3)
        self.init_structures('Z',CREEPTUMOR, 11, 1)
        # add for cheese with barracks and bunker
        # warning: this complicated much. Restrict to buildseries and placement.txt
        self.init_structures('T',INFESTEDBARRACKS, 46, 3)
        self.init_structures('T',INFESTEDBUNKER, 29, 3)
        self.init_structures('T',INFESTEDFACTORY, 43, 3)
        self.init_structures('T',INFESTEDSTARPORT, 36, 3)
        self.init_structures('T',INFESTEDCOCOON, 50, 8)
        self.init_structures('T',MAINCELLBLOCK, 0, 5)
        # scv
        self.builddura_of_thing[SCV] = 12
        self.airground_of_unit[SCV] = 'ground'
        # army, builddura, supply, is air/ground
        self.init_army(MARINE,18,1,'ground')
        self.init_army(MARAUDER,21,2,'ground')
        self.init_army(REAPER,32,1,'ground')
        self.init_army(HELLION,21,2,'ground')
        self.init_army(CYCLONE,32,3,'ground')
        self.init_army(WIDOWMINE,21,2,'ground')
        self.init_army(WIDOWMINEBURROWED,21,2,'ground')
        self.init_army(SIEGETANK,32,3,'ground')
        self.init_army(SIEGETANKSIEGED,32,3,'ground')
        self.init_army(VIKINGFIGHTER,30,2,'air')
        self.init_army(MEDIVAC,30,2,'air')
        self.init_army(RAVEN,43,2,'air')
        self.init_army(LIBERATOR,43,3,'air')
        self.init_army(LIBERATORAG,43,3,'air')
        self.init_army(BANSHEE,43,2,'air')
        self.init_army(BATTLECRUISER,64,6,'air')
        self.init_army(GHOST,29,2,'ground')
        self.init_army(NUKESILONOVA,43,0,'ground')
        # upgrade, builddura
        self.init_upgrade(PUNISHERGRENADES, 43) #concussive shells
        self.init_upgrade(STIMPACK, 100)
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
        self.init_upgrade(TERRANINFANTRYARMORSLEVEL1, 114)
        self.init_upgrade(TERRANINFANTRYARMORSLEVEL2, 136)
        self.init_upgrade(TERRANINFANTRYARMORSLEVEL3, 157)
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
        # cradle is unique, so omitted are: SCV, freestanding REACTOR, TECHLAB
        self.init_cradle(RAVEN,STARPORT)
        self.init_cradle(MEDIVAC,STARPORT)
        self.init_cradle(VIKINGFIGHTER,STARPORT)
        self.init_cradle(LIBERATOR,STARPORT)
        self.init_cradle(BANSHEE,STARPORT)
        self.init_cradle(MARINE,BARRACKS)
        self.init_cradle(MARAUDER,BARRACKS)
        self.init_cradle(REAPER,BARRACKS)
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
        self.init_cradle(STIMPACK,BARRACKSTECHLAB)
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
        self.init_cradle(TERRANINFANTRYARMORSLEVEL1,ENGINEERINGBAY)
        self.init_cradle(TERRANINFANTRYARMORSLEVEL2,ENGINEERINGBAY)
        self.init_cradle(TERRANINFANTRYARMORSLEVEL3,ENGINEERINGBAY)
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
        self.init_techtree(TECHLAB,REFINERY)
        self.init_techtree(BARRACKSREACTOR,REFINERY)
        self.init_techtree(FACTORYREACTOR,REFINERY)
        self.init_techtree(STARPORTREACTOR,REFINERY)
        self.init_techtree(REACTOR,REFINERY)
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
        self.init_techtree(BANSHEE,STARPORTTECHLAB)
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
        self.init_techtree(TERRANINFANTRYARMORSLEVEL2,TERRANINFANTRYARMORSLEVEL1)
        self.init_techtree(TERRANINFANTRYARMORSLEVEL3,TERRANINFANTRYARMORSLEVEL2)
        self.init_techtree(TERRANINFANTRYWEAPONSLEVEL2,ARMORY)
        self.init_techtree(TERRANINFANTRYWEAPONSLEVEL3,ARMORY)
        self.init_techtree(TERRANINFANTRYARMORSLEVEL2,ARMORY)
        self.init_techtree(TERRANINFANTRYARMORSLEVEL3,ARMORY)
        self.compute_all_species_things()
        #       bootstrap code   after initial    from sc2constants import *
        #       for thing in self.all_species_things:
        #           if type(thing) == UnitTypeId:
        #               print('from sc2.ids.unit_typeid import '+thing.name)
        #           if type(thing) == UpgradeId:
        #               print('from sc2.ids.upgrade_id import '+thing.name)
        self.init_labarmy()
        #
        # unfortunately health_max sometimes fails. Thus this list.
        self.maxhealth = {} # per unit the health_max
        self.init_maxhealth(SUPPLYDEPOT, 400)
        self.init_maxhealth(SUPPLYDEPOTLOWERED, 400)
        self.init_maxhealth(BARRACKS, 1000)
        self.init_maxhealth(BARRACKSFLYING, 1000)
        self.init_maxhealth(REFINERY, 500)
        self.init_maxhealth(REFINERYRICH, 500)
        self.init_maxhealth(BARRACKSTECHLAB, 400)
        self.init_maxhealth(FACTORY, 1250)
        self.init_maxhealth(FACTORYFLYING, 1250)
        self.init_maxhealth(FACTORYTECHLAB, 400)
        self.init_maxhealth(STARPORT, 1300)
        self.init_maxhealth(STARPORTFLYING, 1300)
        self.init_maxhealth(STARPORTTECHLAB, 400)
        self.init_maxhealth(TECHLAB, 400)
        self.init_maxhealth(FUSIONCORE, 750)
        self.init_maxhealth(COMMANDCENTER, 1500)
        self.init_maxhealth(COMMANDCENTERFLYING, 1500)
        self.init_maxhealth(PLANETARYFORTRESS, 1500)
        self.init_maxhealth(ORBITALCOMMAND, 1500)
        self.init_maxhealth(ORBITALCOMMANDFLYING, 1500)
        self.init_maxhealth(ENGINEERINGBAY, 850)
        self.init_maxhealth(MISSILETURRET, 250)
        self.init_maxhealth(ARMORY, 750)
        self.init_maxhealth(BUNKER, 400)
        self.init_maxhealth(SENSORTOWER, 200)
        self.init_maxhealth(GHOSTACADEMY, 1250)
        self.init_maxhealth(BARRACKSREACTOR, 400)
        self.init_maxhealth(FACTORYREACTOR, 400)
        self.init_maxhealth(STARPORTREACTOR, 400)
        self.init_maxhealth(REACTOR, 400)
        self.init_maxhealth(NEXUS, 1000)
        self.init_maxhealth(PYLON, 200)
        self.init_maxhealth(ASSIMILATOR, 300)
        self.init_maxhealth(GATEWAY, 500)
        self.init_maxhealth(FORGE, 400)
        self.init_maxhealth(PHOTONCANNON, 150)
        self.init_maxhealth(SHIELDBATTERY, 150)
        self.init_maxhealth(WARPGATE, 500)
        self.init_maxhealth(CYBERNETICSCORE, 550)
        self.init_maxhealth(TWILIGHTCOUNCIL, 500)
        self.init_maxhealth(ROBOTICSFACILITY, 450)
        self.init_maxhealth(STARGATE, 600)
        self.init_maxhealth(TEMPLARARCHIVE, 500)
        self.init_maxhealth(DARKSHRINE, 500)
        self.init_maxhealth(ROBOTICSBAY, 500)
        self.init_maxhealth(FLEETBEACON, 500)
        self.init_maxhealth(ORACLESTASISTRAP, 30)
        self.init_maxhealth(HATCHERY, 1500)
        self.init_maxhealth(LAIR, 2000)
        self.init_maxhealth(HIVE, 2500)
        self.init_maxhealth(EXTRACTOR, 500)
        self.init_maxhealth(SPAWNINGPOOL, 1000)
        self.init_maxhealth(SPINECRAWLER, 300)
        self.init_maxhealth(SPORECRAWLER, 400)
        self.init_maxhealth(EVOLUTIONCHAMBER, 750)
        self.init_maxhealth(ROACHWARREN, 850)
        self.init_maxhealth(BANELINGNEST, 850)
        self.init_maxhealth(HYDRALISKDEN, 850)
        self.init_maxhealth(LURKERDEN, 850)
        self.init_maxhealth(SPIRE, 850)
        self.init_maxhealth(GREATERSPIRE, 1000)
        self.init_maxhealth(NYDUSNETWORK, 850)
        self.init_maxhealth(NYDUSCANAL, 300)
        self.init_maxhealth(INFESTATIONPIT, 850)
        self.init_maxhealth(ULTRALISKCAVERN, 850)
        self.init_maxhealth(CREEPTUMOR, 50)
        self.init_maxhealth(INFESTEDBARRACKS, 1000)
        self.init_maxhealth(INFESTEDBUNKER, 400)
        self.init_maxhealth(INFESTEDFACTORY, 1250)
        self.init_maxhealth(INFESTEDSTARPORT, 1300)
        self.init_maxhealth(INFESTEDCOCOON, 0)
        self.init_maxhealth(MAINCELLBLOCK, 0)
        self.init_maxhealth(MARINE, 45)
        self.init_maxhealth(MARAUDER, 125)
        self.init_maxhealth(REAPER, 60)
        self.init_maxhealth(HELLION, 90)
        self.init_maxhealth(CYCLONE, 120)
        self.init_maxhealth(WIDOWMINE, 90)
        self.init_maxhealth(WIDOWMINEBURROWED, 90)
        self.init_maxhealth(SIEGETANK, 175)
        self.init_maxhealth(SIEGETANKSIEGED, 175)
        self.init_maxhealth(VIKINGFIGHTER, 125)
        self.init_maxhealth(MEDIVAC, 150)
        self.init_maxhealth(RAVEN, 140)
        self.init_maxhealth(LIBERATOR, 180)
        self.init_maxhealth(LIBERATORAG, 180)
        self.init_maxhealth(BANSHEE, 140)
        self.init_maxhealth(BATTLECRUISER, 550)
        self.init_maxhealth(GHOST, 100)
        self.init_maxhealth(NUKESILONOVA, 0)
        #
        self.enemy_pos = self.enemy_start_locations[0].position
        self.loved_pos = self.start_location.position
        self.loved_expo = self.expo_of_pos(self.loved_pos)
        self.cheese2_triedexp.add(self.enemy_pos)
        self.target_loc = self.enemy_pos
        self.cc_destiny[self.loved_pos] = 'oc'
        # vulture
        self.init_vulture()
        # all_repairable_shooters for repair priority
        self.all_repairable_shooters = {PLANETARYFORTRESS, MISSILETURRET, BUNKER}
        for ut in self.all_army:
            if ut not in [MARINE,MARAUDER,REAPER,GHOST]: # bio
                self.all_repairable_shooters.add(ut)
        # give gather init
        for mim in self.mineral_field:
            self.count_of_mimt[mim.tag] = 0
        for scv in self.units(SCV):
            self.job_of_scvt[scv.tag] = 'mimminer'
            amimt = self.notag
            best_sd = 99999
            for mim in self.mineral_field:
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
        # append base positions to layout.txt for placer.py to compute placement tips
        for pos in self.expansion_locations_list:
            self.write_layout(COMMANDCENTER,pos)
        #
        layout_if.mapname = self.game_info.map_name
        layout_if.startx = self.loved_pos.x
        layout_if.starty = self.loved_pos.y
        layout_if.enemyx = self.enemy_pos.x
        layout_if.enemyy = self.enemy_pos.y
        #
        layout_if.save_layout() # saves as data\layout.txt for placer.py
        # now we use layout ourselves too
        #
        for pos in self.expansion_locations_list:
            self.erase_layout(COMMANDCENTER,pos)
        # possible_cc_positions, layout MAINCELLBLOCK to prevent future misuse
        self.possible_cc_positions = set()
        for pos in self.expansion_locations_list:
            self.add_possible_cc_position(pos)
        #
        self.write_layout(COMMANDCENTER,self.loved_pos)
        self.write_layout(COMMANDCENTER,self.enemy_pos)
        self.last_enemies.add((self.notag,self.enemy_pos))
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
            elif (woord[0] == 'position') and (woord[1] == 'REAPERPRISON'):
                self.reaper_prison_pos = Point2((float(woord[2]), float(woord[3])))
            elif (woord[0] == 'position') and (woord[1] == 'REAPERBARRACKS'):
                self.reaper_barracks_pos = Point2((float(woord[2]), float(woord[3])))
            elif (woord[0] == 'position') and (woord[1] == 'REAPERBUNKER1'):
                self.reaper_bunker1_pos = Point2((float(woord[2]), float(woord[3])))
            elif (woord[0] == 'position') and (woord[1] == 'REAPERBUNKER2'):
                self.reaper_bunker2_pos = Point2((float(woord[2]), float(woord[3])))
            elif (woord[0] == 'position') and (woord[1] == 'HOMERAMP'):
                self.homeramp_pos = Point2((float(woord[2]), float(woord[3])))
            elif (woord[0] == 'position') and (woord[1] == 'ENEMYRAMP'):
                self.enemyramp_pos = Point2((float(woord[2]), float(woord[3])))
            elif (woord[0] == 'position') and (woord[1] == 'ENEMYNATURAL'):
                self.enemynatural_pos = Point2((float(woord[2]), float(woord[3])))
            elif (woord[0] == 'position') and (woord[1] == 'ENEMYTHIRD'):
                self.enemythird_pos = Point2((float(woord[2]), float(woord[3])))
            elif (woord[0] == 'position') and (woord[1] == 'ENEMYNATURALCHOKE'):
                self.enemynaturalchoke_pos = Point2((float(woord[2]), float(woord[3])))
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
        # put scout-series in scout1_pos
        for nr in range(0, len(self.tips)):
            ti = self.tips[nr]
            woord = ti.split()
            if (woord[0] == 'position') and (woord[1] == 'SCOUT'):
                scpos = Point2((float(woord[2]), float(woord[3])))
                self.scout1_pos.append(scpos)
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
                    self.tips_used.add(nr)
            if (woord[0] == 'position') and (woord[1] == 'SUPPLYDEPOT'):
                if self.wall_depot0_pos == self.nowhere:
                    self.wall_depot0_pos = Point2((float(woord[2]), float(woord[3])))
                    self.tips_used.add(nr)
                elif self.wall_depot1_pos == self.nowhere:
                    self.wall_depot1_pos = Point2((float(woord[2]), float(woord[3])))
                    self.tips_used.add(nr)
        self.set_rally.add((self.wall_barracks_pos,self.wall_barracks_pos.towards(self.loved_pos, 2)))
        self.chosenplaces.append((BARRACKS,self.wall_barracks_pos))
        self.chosenplaces.append((SUPPLYDEPOT,self.wall_depot0_pos))
        self.chosenplaces.append((SUPPLYDEPOT,self.wall_depot1_pos))
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
        #
        # put scout-series in scout2_pos
        scout2_pos = []
        visit = []
        for pos in self.expansion_locations_list:
            if pos != self.enemy_pos:
                if self.proxy(pos):
                    visit.append(pos.towards(self.game_info.map_center, 4))
                    visit.append(pos.towards(self.game_info.map_center, 6))
                else:
                    visit.append(pos.towards(self.game_info.map_center, -1))
        nowpos = self.loved_pos
        while len(visit) > 0:
            bestsd = 99999
            for apos in visit:
                sd = self.sdist(apos,nowpos)
                if sd < bestsd:
                    bestsd = sd
                    bestpos = apos
            del visit[visit.index(bestpos)]
            self.scout2_pos.append(bestpos)
            nowpos = bestpos
        #
        # mapspecific
        if self.game_info.map_name == 'Golden Wall LE':
            self.miner_bound = 18
        #
        self.init_liberator_spots()
        self.init_expansion_doubles()
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
            self.rushopening = True
            self.buildseries_opening = [SUPPLYDEPOT, INFESTEDBARRACKS, REFINERY, INFESTEDBUNKER, SUPPLYDEPOT, INFESTEDFACTORY, \
                                        BARRACKS, REFINERY, COMMANDCENTER]
        if self.game_choice[3]:
            self.opening_name = 'cheese-bc'
            self.rushopening = True
            self.buildseries_opening = [SUPPLYDEPOT, INFESTEDBARRACKS, REFINERY, INFESTEDBUNKER,
                                        SUPPLYDEPOT, INFESTEDFACTORY, BARRACKS, REFINERY,
                                        STARPORT, SUPPLYDEPOT, FUSIONCORE, STARPORTTECHLAB, SUPPLYDEPOT, BATTLECRUISER]
        if self.game_choice[4]:
            self.opening_name = 'expand'
            self.buildseries_opening = [SUPPLYDEPOT, COMMANDCENTER, BARRACKS, SUPPLYDEPOT]
        if self.game_choice[5]:
            self.opening_name = 'double-expand'
            self.buildseries_opening = [SUPPLYDEPOT, COMMANDCENTER, COMMANDCENTER, BARRACKS, SUPPLYDEPOT, ENGINEERINGBAY]
        if self.game_choice[6]:
            self.opening_name = 'cheese-bunk'
            self.rushopening = True
            self.buildseries_opening = [SUPPLYDEPOT, INFESTEDBARRACKS, INFESTEDBUNKER, INFESTEDBUNKER,
                                        INFESTEDBUNKER, SUPPLYDEPOT, REFINERY, INFESTEDFACTORY, BARRACKS, REFINERY]
            self.get_shield_pos()
        if self.game_choice[7]:
            self.opening_name = 'rush-bc'
            self.rushopening = True
            self.buildseries_opening = [SUPPLYDEPOT, REFINERY, BARRACKS, SUPPLYDEPOT, MARINE, FACTORY, REFINERY, MARINE,
                                       STARPORT, FUSIONCORE, STARPORTTECHLAB, BATTLECRUISER, COMMANDCENTER]
        if self.game_choice[8]:
            self.opening_name = 'defence'
            self.buildseries_opening = [SUPPLYDEPOT, REFINERY, BARRACKS, SUPPLYDEPOT, MARINE, FACTORY, MARINE,
                                        FACTORYTECHLAB, MARINE, SUPPLYDEPOT, SIEGETANK, ENGINEERINGBAY]
        if self.game_choice[9]:
            self.opening_name = 'pf-rush'
            self.rushopening = True
            self.buildseries_opening = [SUPPLYDEPOT, BARRACKS, BUNKER, REFINERY, SUPPLYDEPOT, MARINE, COMMANDCENTER, MARINE,
                                        ENGINEERINGBAY, MARINE, REFINERY, MARINE, FACTORY]
            self.init_pf_rush()
        if self.game_choice[10]:
            self.opening_name = 'expa-ma'
            self.buildseries_opening = [SUPPLYDEPOT, COMMANDCENTER, BARRACKS, SUPPLYDEPOT, MARINE, REFINERY, COMMANDCENTER,
                                        MARINE, ORBITALCOMMAND, FACTORY, MARINE, COMMANDCENTER, FACTORYTECHLAB, MARINE,
                                        MARINE, ORBITALCOMMAND, SIEGETANK, MARINE]
        if self.game_choice[11]:
            self.opening_name = 'cocoon'
            self.rushopening = True
            self.buildseries_opening = [SUPPLYDEPOT, BARRACKS, BARRACKS, SUPPLYDEPOT, MARINE, BUNKER, MARINE, BUNKER, MARINE,
                                        REFINERY, MARINE, INFESTEDFACTORY, MARINE, COMMANDCENTER, MARINE, FACTORYTECHLAB, SIEGETANK]
            self.init_cocoon()
        if self.game_choice[12]:
            self.opening_name = 'triple-expand'
            self.buildseries_opening = [SUPPLYDEPOT, COMMANDCENTER, COMMANDCENTER, BARRACKS, SUPPLYDEPOT, COMMANDCENTER, MARINE, ENGINEERINGBAY]
        if self.game_choice[13]:
            self.opening_name = 'liberator-cc'
            self.rushopening = True
            self.buildseries_opening = [SUPPLYDEPOT, REFINERY, BARRACKS, SUPPLYDEPOT, MARINE, INFESTEDFACTORY, REFINERY,
                                        STARPORT, LIBERATOR, COMMANDCENTER]
            self.place_proxy(STARPORT, 60)
        if self.game_choice[14]:
            self.opening_name = 'liberator-bc'
            self.rushopening = True
            self.buildseries_opening = [SUPPLYDEPOT, REFINERY, BARRACKS, SUPPLYDEPOT, MARINE, INFESTEDFACTORY, REFINERY,
                                        STARPORT, LIBERATOR, FUSIONCORE, STARPORTTECHLAB, BATTLECRUISER, COMMANDCENTER]
            self.place_proxy(STARPORT,60)
        if self.game_choice[15]:
            self.opening_name = 'liberator-tank'
            self.rushopening = True
            self.buildseries_opening = [SUPPLYDEPOT, REFINERY, BARRACKS, SUPPLYDEPOT, MARINE, FACTORY, REFINERY,
                                        STARPORT, FACTORYTECHLAB, LIBERATOR, SIEGETANK, LIBERATOR]
            self.place_proxy(STARPORT, 60)
            self.place_proxy(FACTORY, 60)
        if self.game_choice[16]:
            self.opening_name = 'reapers'
            self.buildseries_opening = [SUPPLYDEPOT, REFINERY, BARRACKS, REAPER, SUPPLYDEPOT, REAPER, BUNKER, BUNKER,
                                        BARRACKS, REFINERY]
            self.init_reapers()
            self.opening_create_units = 3
            self.opening_create_kind = REAPER
        if self.game_choice[17]:
            self.opening_name = 'two liberators'
            self.rushopening = True
            self.buildseries_opening = [SUPPLYDEPOT, REFINERY, BARRACKS, SUPPLYDEPOT, REFINERY, FACTORY, MARINE,
                                        STARPORT, STARPORT, LIBERATOR, LIBERATOR]
            self.place_proxy(STARPORT,45)
            self.place_proxy(STARPORT, 40)
        if self.game_choice[18]:
            self.opening_name = 'marauders'
            self.rushopening = True
            self.buildseries_opening = [SUPPLYDEPOT, BARRACKS, REFINERY, SUPPLYDEPOT,
                                        INFESTEDBARRACKS, INFESTEDBARRACKS, ORBITALCOMMAND,
                                        BARRACKSTECHLAB, BARRACKSTECHLAB, BARRACKSTECHLAB,
                                        MARAUDER, MARAUDER, MARAUDER, PUNISHERGRENADES]
            for (lab,pos) in self.unthinkable:
                if lab == BARRACKSTECHLAB:
                    del self.buildseries_opening[self.buildseries_opening.index(BARRACKSTECHLAB)]
                    del self.buildseries_opening[self.buildseries_opening.index(MARAUDER)]
            self.init_marauders()
            self.opening_create_units = 12
            self.opening_create_kind = MARAUDER
            self.production_pause.add((SCV,18,BARRACKS,2))
        if self.game_choice[19]:
            self.opening_name = 'stimmed-marauders'
            self.rushopening = True
            self.buildseries_opening = [SUPPLYDEPOT, BARRACKS, REFINERY, SUPPLYDEPOT,
                                        INFESTEDBARRACKS, INFESTEDBARRACKS, ORBITALCOMMAND,
                                        BARRACKSTECHLAB, BARRACKSTECHLAB, BARRACKSTECHLAB,
                                        STIMPACK, MARAUDER, MARAUDER, MARAUDER, PUNISHERGRENADES]
            for (lab,pos) in self.unthinkable:
                if lab == BARRACKSTECHLAB:
                    del self.buildseries_opening[self.buildseries_opening.index(BARRACKSTECHLAB)]
                    del self.buildseries_opening[self.buildseries_opening.index(MARAUDER)]
            self.init_marauders()
            self.opening_create_units = 20
            self.opening_create_kind = MARAUDER
        if self.game_choice[20]:
            self.init_marine_opening(1)
        elif self.game_choice[21]:
            self.init_marine_opening(2)
        elif self.game_choice[22]:
            self.init_marine_opening(3)
        elif self.game_choice[23]:
            self.init_marine_opening(4)
        elif self.game_choice[24]:
            self.init_marine_opening(5)
        elif self.game_choice[25]:
            self.init_marine_opening(6)
        # radio_choices = 26
        self.log_success('OPENING: '+self.opening_name)
        #
        #  preparing midgame
        self.midgame_things = []
        # The midgame really needs a battlecruiser, or the core is too late
        # This routine is called in the init phase, you cannot depend on e.g. amount of barracks
        self.midgame(BATTLECRUISER,1)
        if self.game_choice[40]:
            self.midgame(VIKINGFIGHTER,1)
        if self.game_choice[41]:
            self.midgame(SIEGETANK,1)
        if self.game_choice[42]:
            self.midgame(SIEGETANK,2)
        if self.game_choice[43]:
            self.midgame(MARINE, 2)
        else:
            self.midgame(MARINE, 5)
        if self.game_choice[44]:
            self.midgame(COMMANDCENTER,2)
            self.midgame(STARPORT,2)
            self.midgame(STARPORTTECHLAB,2)
        if self.game_choice[45]:
            self.midgame(ENGINEERINGBAY,1)
            self.midgame(MISSILETURRET,1)
            self.midgame(PLANETARYFORTRESS,1)
        if self.game_choice[46]:
            self.midgame(LIBERATOR,1)
        # made self.midgame_things
        # circle
        self.make_circle(10)
        self.flee_circle = self.circle.copy()
        # blocker
        self.init_blocker()
        # rally
        for cc in self.structures(COMMANDCENTER):
            cc(AbilityId.RALLY_BUILDING,self.loved_pos.towards(self.game_info.map_center,-3))
        # get hometop, enemytop
        self.get_hometop()
        self.get_enemytop()
        # name_of_scvt: fun translation of scvt to english boy name
        pl = open('data/names.txt','r')
        self.all_names = pl.read().splitlines()
        pl.close()
        # chat
        await self._client.chat_send('Chaosbot version 3 feb 2021, made by MerkMore', team_only=False)
        #
        #layout_if.photo_layout()

    def init_marine_opening(self, nbases):
        # 1 <= nbases <= 6
        self.marine_opening_bases = nbases
        self.opening_name = 'marine'
        self.rushopening = True
        self.cc_destiny_rush = True
        if nbases == 1:
            self.buildseries_opening = [SUPPLYDEPOT, BARRACKS]
        else:    
            self.buildseries_opening = [SUPPLYDEPOT, COMMANDCENTER, BARRACKS]
            ccs = 2
            while ccs < nbases:
                self.buildseries_opening.append(COMMANDCENTER)
                ccs += 1
        # orbitals (not thrown, as it would be pushed to later)
        ocs = 0
        while ocs < nbases:
            self.buildseries_opening.append(ORBITALCOMMAND)
            ocs += 1
        # start stim
        self.buildseries_opening.append(REFINERY)
        # barracks (in the opening, so scvs can travel in advance)
        bars = 1
        while bars < 4 * nbases:
            self.buildseries_opening.append(BARRACKS)
            bars += 1
        # barracks random placing
        bars = 1
        while bars < 4 * nbases:
            around = self.random_mappoint()
            while self.proxy(around) or (not self.near(around,self.game_info.map_center,60)):
                around = self.random_mappoint()
            place = self.place_around(BARRACKS, around)
            nearminerals = False
            for mim in self.mineral_field:
                if self.near(place,mim.position,2):
                    nearminerals = True
            if not nearminerals:
                self.chosenplaces.append((BARRACKS, place))
                bars += 1
        # bunker placing
        self.buildseries_opening.append(BUNKER)
        goal = self.enemynatural_pos
        pos = self.init_cheese_position(goal, 79, BUNKER)
        self.chosenplaces.append((BUNKER, pos))
        #
        self.production_pause.add((SUPPLYDEPOT, 1, ORBITALCOMMAND, 1))
        self.production_pause.add((SCV, 16 + nbases, ORBITALCOMMAND, 1))
        self.production_pause.add((REFINERY, 0, FACTORY, 1))
        self.opening_create_units = nbases * 12 # 4 barracks * 3 marines/barrack
        self.opening_create_kind = MARINE
        self.supply_rate = 0.12 + 0.03 * nbases

    #*********************************************************************************************************************
    #   logging

    async def catch_a_bug(self):
        abug = False
        # put detectioncondition under here
        # put detectioncondition above here
        if abug:
            await self._client.chat_send('catch a bug ', team_only=False)
            #do_slowdown = True
            please_breakpoint_this_line = True

    def log_fail(self,bol,stri):
        if self.do_log_fail:
            if not bol:
                print(' On '+str(self.frame)+' fail '+self.routine+' '+stri)

    def log_success(self,stri):
        if self.do_log_success:
            print(' On '+str(self.frame)+' success '+self.routine+' '+stri) 

    def log_bunker(self,stri):
        if self.do_log_bunker:
            print(' On '+str(self.frame)+' bunker '+self.routine+' '+stri)

    def log_army(self,stri):
        if self.do_log_army:
            print(' On '+str(self.frame)+' army '+self.routine+' '+stri)

    def log_bcs(self):
        if self.do_log_bcs:
            atty = self.attack_type
            inrep = 0
            for bc in self.units(BATTLECRUISER):
                if self.emotion_of_unittag[bc.tag] == 'recovering':
                    inrep +=1
            print(' On '+str(self.frame)+' attacktype '+self.routine+' '+atty+', in rep '+str(inrep))
            if atty == 'jumpy':
                for bc in self.units(BATTLECRUISER):
                    emotion = self.emotion_of_unittag[bc.tag]
                    if bc.tag in self.last_sd_of_unittag:
                        sd = self.last_sd_of_unittag[bc.tag]
                    else:
                        sd = -1
                    print('a bc '+emotion+' health '+str(bc.health)+' sd '+str(sd))

    async def log_attacktype(self,stri):
        if self.do_log_attacktype:
            print(' On '+str(self.frame)+' attacktype '+self.routine+' '+stri)

    def log_workers(self,stri):
        if self.do_log_workers:
            print(' On '+str(self.frame)+' workers '+self.routine+' '+stri) 

    def log_layout(self,stri):
        if self.do_log_layout:
            print(' On '+str(self.frame)+' layout '+self.routine+' '+stri) 

    def log_placing(self,stri):
        if self.do_log_placing:
            print(' On '+str(self.frame)+' placing '+self.routine+' '+stri) 

    def log_command(self,stri):
        if self.do_log_command:
            print(' On '+str(self.frame)+' commands '+self.routine+' '+stri)

    def frame_of_sec(self, secs) -> str:
        frame = self.frame + round(secs * self.frames_per_second)
        return str(frame)+' '

    def stri_of_eh(self, what):
        if type(what) == int:
            stri = str(what)
        else:
            stri = what.name
        return stri

    def log_prediction(self):
        if self.do_log_planning:
            moments = set()
            for bp in self.planning + self.extra_planning:
                moments.add(bp[3])
                moments.add(bp[4])
                moments.add(bp[5])
            for (martype,bartype,pos,dura) in self.eggs:
                moments.add(dura)
            for moment in sorted(moments):
                if moment >= 0:
                    for bp in self.planning + self.extra_planning:
                        if bp[3] == moment:
                            print('prediction ' + self.frame_of_sec(moment) + bp[0].name + '   '+self.stri_of_eh(bp[1]) + ' ' + self.txt(bp[2]) + ' prep')
                        if bp[4] == moment:
                            print('prediction ' + self.frame_of_sec(moment) + bp[0].name + '   ' + self.stri_of_eh(bp[1]) + ' ' + self.txt(bp[2]) + ' egg')
                        if bp[5] == moment:
                            print('prediction ' + self.frame_of_sec(moment) + bp[0].name + '   ' + self.stri_of_eh(bp[1]) + ' ' + self.txt(bp[2]) + ' bird')
                    for (martype,bartype,pos,dura) in self.eggs:
                        if dura == moment:
                            print('prediction ' + self.frame_of_sec(moment) + martype.name + '   ' + self.stri_of_eh(bartype) + ' ' + self.txt(pos) + ' bird')

    def log_planning(self,stri):
        if self.do_log_planning:
            print(' On '+str(self.frame)+' planning '+stri)

    def log_event(self,stri):
        if self.do_log_event:
            print('event: '+stri)

    def log_earn(self, stri):
        if self.do_log_earn and self.earn_show:
            print('earn: '+stri)

    def log_throw(self,stri):
        if self.do_log_throw:
            print(' On '+str(self.frame)+' throw '+stri)

    def txt(self, point) -> str:
        return str(point.x)+','+str(point.y)

    def log_throwspots(self):
        if self.do_log_throwspots:
            if len(self.throwspots) > 0:
                print(' On '+str(self.frame)+' ---------- throwspots ----------')
                for priority in [1,2,3]:
                    for sta in ['new','thought']:
                        for (th,pl,st,ow, pri) in self.throwspots:
                            if (st == sta) and (pri == priority):
                                print(' On '+str(self.frame)+' --- '+th.name+' '+self.txt(pl)+' '+st+' '+ow+' '+str(pri))

    def log_boss(self,stri):
        if self.do_log_boss:
            print(' On '+str(self.frame)+' boss '+self.routine+' '+stri)

    def log_armysize(self):
        if self.do_log_armysize:
            stri = ''
            for ut in self.all_army:
                am = self.units(ut).amount
                if am>0:
                    stri = stri+'   '+ut.name+' '+str(am)
            print(' On '+str(self.frame)+' army'+stri)

    def name(self,scvt) -> str:
        if scvt in self.name_of_scvt:
            return self.name_of_scvt[scvt]
        else:
            return str(scvt)

    def log_gasminer(self):
        if self.do_log_gasminer:
            print(' On '+str(self.frame)+' gasminer: ')
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
            print(' On '+str(self.frame)+' population: '+lin)

    def log_limbo(self,stri):
        if self.do_log_limbo:
            print(' On '+str(self.frame)+' limbo: '+stri) 

    def log_resource(self):
        if self.do_log_resource:
            print(' On '+str(self.frame)+' minerals '+str(self.minerals)+'   gas '+str(self.vespene))

    def log_buildseries(self, instri):
        if self.do_log_buildseries:
            stri = instri
            for thing in self.buildseries:
                stri = stri+' '+thing.name
            print(' On '+str(self.frame)+' buildseries: '+stri)

    def log_buildsit(self, stri):
        if self.do_log_buildsit:
            print(' On '+str(self.frame)+' buildsit: '+stri)

    def log_time(self,stri):
        if self.do_log_time:
            print(' On '+str(self.frame)+' time: '+stri)

    def log_buildstate(self,stri):
        if self.do_log_buildstate:
            print(' On '+str(self.frame)+' buildstate: '+stri)

    def log_cheese(self):
        if self.do_log_cheese:
            if self.cheese_phase != 'Z':
                print(' On '+str(self.frame)+' cheese phase '+self.cheese_phase
                      +'   cheese3 '+self.cheese3_phase)




    def slowed_down(self):
        if self.do_slowdown:
            time.sleep(0.25) # 0.25


    def position_of_building(self, bui) -> Point2:
        if bui.type_id in self.all_labs:
            pos = Point2((bui.position.x - 2.5, bui.position.y + 0.5))
        else:
            pos = bui.position
        return pos


    def init_expected_order(self, job, abil):
        self.expected_orders.add((job,abil))

    def init_cheese_position(self, anchor,good_sdist,building) -> Point2:
        besttry = 99999
        found_spot = self.nowhere
        estimate = anchor.towards(self.loved_pos,sqrt(good_sdist))
        estimate = self.put_on_the_grid(building, estimate)
        for dx in range(-12, 12):
            for dy in range(-12, 12):
                maypos = Point2((estimate.x + dx, estimate.y + dy))
                if self.check_layout(building, maypos):
                    sd = self.sdist(anchor, maypos)
                    try0 = (sd - good_sdist)*(sd-good_sdist) + self.circledist(maypos,self.loved_pos)
                    if try0 < besttry:
                        found_spot = maypos
                        besttry = try0
        if found_spot != self.nowhere:
            self.write_layout(building,found_spot)
        return found_spot


    def init_pf_rush(self):
        # fun placement of barracks, bunker, commandcenter, planetaryfortress
        self.write_layout(COMMANDCENTER,self.enemynatural_pos)
        self.cheese3_landing_pos = self.init_cheese_position(self.enemynatural_pos,115,COMMANDCENTER) # 115
        sd = 38
        self.cheese3_bunker_pos = self.init_cheese_position(self.cheese3_landing_pos,sd,BUNKER)
        while self.near(self.cheese3_bunker_pos,self.enemynatural_pos,12):
            sd += 30
            self.cheese3_bunker_pos = self.init_cheese_position(self.cheese3_landing_pos, sd, BUNKER)
        self.cheese3_barracks_pos = self.init_cheese_position(self.cheese3_bunker_pos,11,ARMORY) # 11 BARRACKS nolab
        self.cheese3_cc_pos = self.init_cheese_position(self.cheese3_barracks_pos,28,COMMANDCENTER) # 28
        self.cheese3_prison_pos = self.init_cheese_position(self.cheese3_bunker_pos,12,MISSILETURRET) # 12
        bunker_if.hiding_spot = self.init_cheese_position(self.cheese3_bunker_pos,70,MISSILETURRET) # 12
        # erase
        self.erase_layout(COMMANDCENTER,self.enemynatural_pos)
        self.erase_layout(COMMANDCENTER,self.cheese3_landing_pos)
        self.erase_layout(BUNKER,self.cheese3_bunker_pos)
        self.erase_layout(ARMORY,self.cheese3_barracks_pos) # BARRACKS nolab
        self.erase_layout(COMMANDCENTER,self.cheese3_cc_pos)
        self.erase_layout(MISSILETURRET,self.cheese3_prison_pos)
        # use all
        self.chosenplaces.insert(0,(BARRACKS,self.cheese3_barracks_pos))
        self.chosenplaces.append((BUNKER,self.cheese3_bunker_pos))
        self.chosenplaces.append((COMMANDCENTER,self.cheese3_cc_pos))
        #
        self.production_pause.add((SCV,20,ENGINEERINGBAY,1))
        self.wished_marines_per_bunker = 4

    def place_proxy(self, building, dist):
        # Add to chosenplaces, for a building-with-lab, a random place distance 'dist' to enemyramp
        best = 0
        bestpoint = self.nowhere
        for pog in range(0,50):
            ok = False
            while not ok:
                ok = True
                point = self.random_mappoint()
                ok = ok and self.near(point,self.enemyramp_pos,dist+7)
                ok = ok and not self.near(point,self.enemyramp_pos,dist-7)
                if ok: # speedup
                    point = self.put_on_the_grid(building, point)
                    ok = ok and self.check_layout(building,point)
                    worth = 2 * self.circledist(point,self.enemy_pos) + self.circledist(point,self.loved_pos)
            if worth > best:
                best = worth
                bestpoint = point
        self.chosenplaces.append((building,bestpoint))
        self.write_layout(building, bestpoint)

    def add_spot(self, name,where,away):
        # a liberator position attacking 'where' with its tail away from 'away'
        d = self.circledist(where, away)
        vec = Point2(((where.x - away.x), (where.y - away.y)))
        vec = Point2(((vec.x / d), (vec.y / d)))
        siegeattack = where
        siegeship = Point2(((where.x + 5 * vec.x), (where.y + 5 * vec.y)))
        self.liberator_spots.add((name, siegeattack, siegeship))

    def add_mineral_spot(self, name,base):
        # a liberator spot attacking minerals of a base
        sumx = 0
        sumy = 0
        n = 0
        for mim in self.mineral_field:
            if self.near(mim.position,base,self.miner_bound):
                sumx += mim.position.x
                sumy += mim.position.y
                n += 1
        if n > 0:
            mimcenter = Point2((sumx/n,sumy/n))
            where = Point2((1.3*mimcenter.x-0.3*base.x, 1.3*mimcenter.y-0.3*base.y))
            self.add_spot(name,where,base)


    def init_liberator_spots(self):
        self.routine = 'init_liberator_spots'
        self.add_spot('contain1',self.enemyramp_pos,self.enemy_pos)
        self.add_spot('contain2',self.enemynaturalchoke_pos,self.enemynatural_pos)
        self.add_spot('base1',self.enemy_pos,self.enemyramp_pos)
        self.add_spot('base2',self.enemynatural_pos,self.enemyramp_pos)
        self.add_mineral_spot('mim1',self.enemy_pos)
        self.add_mineral_spot('mim2',self.enemynatural_pos)

    def init_reapers(self):
        if self.reaper_bunker1_pos == self.nowhere:
            self.reaper_bunker1_pos = self.init_cheese_position(self.enemynatural_pos, 79, BUNKER)
        if self.reaper_bunker2_pos == self.nowhere:
            self.reaper_bunker2_pos = self.init_cheese_position(self.enemynatural_pos, 200, BUNKER)
        self.chosenplaces.append((BUNKER,self.reaper_bunker1_pos))
        self.chosenplaces.append((BUNKER,self.reaper_bunker2_pos))
        self.chosenplaces.insert(0,(BARRACKS,self.reaper_barracks_pos))
        self.init_reaper_attack(self.enemy_pos)

    def init_cocoon(self):
        # funny placement of barracks, bunker, barracks,bunker
        self.write_layout(COMMANDCENTER,self.enemynatural_pos)
        if self.cheese3_cocoon_pos == self.nowhere:
            self.cheese3_cocoon_pos = self.init_cheese_position(self.enemynatural_pos,320,INFESTEDCOCOON)
        self.cheese3_bunker_pos = Point2((self.cheese3_cocoon_pos.x+2.5,self.cheese3_cocoon_pos.y-0.5))
        self.cheese3_bunker2_pos = Point2((self.cheese3_cocoon_pos.x+0.5,self.cheese3_cocoon_pos.y+2.5))
        self.cheese3_barracks_pos = Point2((self.cheese3_cocoon_pos.x-2.5,self.cheese3_cocoon_pos.y+0.5))
        self.cheese3_barracks2_pos = Point2((self.cheese3_cocoon_pos.x-0.5,self.cheese3_cocoon_pos.y-2.5))
        self.cheese3_prison_pos = self.cheese3_cocoon_pos
        # erase
        self.erase_layout(COMMANDCENTER,self.enemynatural_pos)
        self.erase_layout(INFESTEDCOCOON,self.cheese3_cocoon_pos)
        # use all
        self.chosenplaces.insert(0,(BARRACKS,self.cheese3_barracks_pos))
        self.chosenplaces.append((BUNKER,self.cheese3_bunker_pos))
        self.chosenplaces.insert(0,(BARRACKS,self.cheese3_barracks2_pos))
        self.chosenplaces.append((BUNKER,self.cheese3_bunker2_pos))
        #
        self.wished_marines_per_bunker = 4
        # production_pause seems not to help
        #self.production_pause.add((SCV, 16, BARRACKS, 1))


    def init_marauders(self):
        bar1_pos = self.init_cheese_position(self.enemythird_pos,200,BARRACKS)
        bar2_pos = self.init_cheese_position(bar1_pos,1,BARRACKS)
        self.chosenplaces.append((INFESTEDBARRACKS,bar1_pos))
        self.chosenplaces.append((INFESTEDBARRACKS,bar2_pos))
        self.marauder_goal = bar1_pos.towards(self.loved_pos,3)
        self.production_pause.add((SCV,23,FACTORY,1))
        self.production_pause.add((REFINERY,1,FACTORY,1))
        self.set_rally.add((bar1_pos,self.marauder_goal))
        self.set_rally.add((bar2_pos,self.marauder_goal))


    def log_preps(self):
        if self.do_log_preps:
            for (martype,bartype,pos,dura,owner) in self.preps:
                if bartype in self.units(SCV):
                    scv = bartype
                    print(' On '+str(self.frame)+' ' + self.name(scv.tag) + ' preps for a ' + martype.name + \
                          ' at ' + self.txt(pos) + ' dura ' + str(dura) + ' by '+owner)
                else:
                    print(' On '+str(self.frame)+' ' + bartype.name + ' preps for a ' + martype.name + \
                          ' at '+self.txt(pos) + ' dura ' + str(dura) + ' by ' + owner)

    def log_eggs(self):
        if self.do_log_eggs:
            for (martype,bartype,pos,dura) in self.eggs:
                if bartype in self.units(SCV):
                    scv = bartype
                    job = self.job_of_scvt[scv.tag]
                    print(' On '+str(self.frame)+' ' + job + ' ' + self.name(scv.tag) + ' eggs a ' + martype.name + \
                          ' at ' + self.txt(pos) + ' for '+str(dura))
                else:
                    print(' On '+str(self.frame)+' '+bartype.name+' at '+self.txt(pos) + \
                          ' eggs a '+martype.name + ' for '+str(dura))

    def log_birds(self):
        if self.do_log_birds:
            for (thingtype,pos) in self.birds:
                if thingtype == SCV:
                    seen = False
                    for scv in self.units(SCV):
                        if scv.position == pos:
                            seen = True
                            print(' On '+str(self.frame)+' ' + self.name(scv.tag) + ' is at ' + self.txt(pos))
                    if not seen:
                        print(' On '+str(self.frame)+' ' + thingtype.name + ' is at ' + self.txt(pos))
                else:
                    print(' On '+str(self.frame)+' ' + thingtype.name + ' is at ' + self.txt(pos))

    def log_thoughts(self):
        if self.do_log_thoughts:
            for (thingtype,pos,owner) in self.thoughts:
                print(' On '+str(self.frame)+' ' + owner + ' is thinking of ' + thingtype.name + ' at ' + self.txt(pos))
            for (thingtype,pos) in self.unthinkable:
                print('Unthinkable is a ' + thingtype.name + ' at ' + self.txt(pos))

    def log_buildorder(self, stri):
        if self.do_log_buildorder:
            print(' On ' + str(self.frame) + ' buildorder ' + stri)

    def log_orders(self):
        # order 0 will be executed first
        # a bump can insert a move
        # attack point but see enemy can insert attack enemy
        if self.do_log_orders:
            for scv in self.units(SCV):
                normal = False
                job = self.job_of_scvt[scv.tag]
                if len(scv.orders) == 2:
                    if job == 'defender':
                        if scv.orders[0].ability.id == AbilityId.ATTACK:
                            if scv.orders[1].ability.id == AbilityId.ATTACK:
                                normal = True
                if (len(scv.orders) == 1):
                    if (job,scv.orders[0].ability.id) in self.expected_orders:
                        normal = True
                    if job in ('fencer','builder','gasper'):
                        if scv.is_constructing_scv:
                            normal = True
                if (len(scv.orders) == 0):
                    if job in self.jobs_may_idle:
                        normal = True
                if not normal:
                    orders = ""
                    for order in scv.orders:
                        if type(order.target) == int:
                            orders = orders + '    ' + str(order.ability.id) + ', ' + str(order.target) + ', ' + str(order.progress)
                        else:
                            orders = orders + '   ' + str(order.ability.id) + ', ' + self.txt(order.target) + ', ' + str(order.progress)
                    print(' On '+str(self.frame)+' ' + 'orders ' + job + ' ' + self.name(scv.tag) + orders)

    #******************************************************************************************************************

    def read_layout(self, vakx,vaky) -> int:
        if (self.map_left <= vakx) and (vakx < self.map_right) and (self.map_bottom <= vaky) and (vaky < self.map_top):
            point = Point2((vakx,vaky))
            if self.has_creep(point):
                return 6
            else:
                return layout_if.layout[vakx][vaky]
        else:
            return 3

    def put_on_the_grid(self,struc,place) -> Point2:
        if struc in self.all_structures:
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
        return Point2((x,y))

    def add_possible_cc_position(self, place):
        # administrate, and draw a 5x5 exclusive the middlepoint
        place = self.put_on_the_grid(MAINCELLBLOCK,place)
        self.possible_cc_positions.add(place)
        self.write_layout(MAINCELLBLOCK, place)
        self.log_success('possible_cc_position '+self.txt(place))

    def write_layout(self,struc,place):
        place = self.put_on_the_grid(struc,place)
        x = place.x
        y = place.y
        if struc in self.all_structures:
            self.designs.add((struc,place,self.notag))
            self.log_layout('write position '+struc.name+' '+str(x)+' '+str(y))
            siz = self.size_of_structure[struc]
            if place in self.possible_cc_positions:
                if (siz == 5) and (struc != MAINCELLBLOCK):
                    siz = 1
            if struc == MAINCELLBLOCK:
                for vakx in range(round(x-siz/2),round(x+siz/2)):
                    for vaky in range(round(y-siz/2),round(y+siz/2)):
                        if (vakx != round(x-0.5)) or (vaky != round(y-0.5)):
                            layout_if.layout[vakx][vaky] = 4
            else:
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
        place = self.put_on_the_grid(struc,place)
        x = place.x
        y = place.y
        if struc in self.all_structures:
            todel = set()
            for (astruc,aplace,atag) in self.designs:
                if (astruc == struc) and (aplace == place):
                    todel.add((astruc,aplace,atag))
            self.designs -= todel
            self.log_layout('erase position '+struc.name+' '+str(x)+' '+str(y))
            siz = self.size_of_structure[struc]
            if place in self.possible_cc_positions:
                if (siz == 5) and (struc != MAINCELLBLOCK):
                    siz = 1
            if (struc in [REFINERY,REFINERYRICH]):
                mustbecolor = 1
            else:
                mustbecolor = 0
            if struc == MAINCELLBLOCK:
                for vakx in range(round(x-siz/2),round(x+siz/2)):
                    for vaky in range(round(y-siz/2),round(y+siz/2)):
                        if (vakx != round(x-0.5)) or (vaky != round(y-0.5)):
                            layout_if.layout[vakx][vaky] = mustbecolor
            else:
                for vakx in range(round(x-siz/2),round(x+siz/2)):
                    for vaky in range(round(y-siz/2),round(y+siz/2)):
                        layout_if.layout[vakx][vaky] = mustbecolor
            #    the add-on could still be there


    def check_layout(self,struc,place) -> bool:
        placable = True
        gridplace = self.put_on_the_grid(struc,place)
        x = gridplace.x
        y = gridplace.y
        if (struc in self.all_structures):
            if (struc in [REFINERY,REFINERYRICH]):
                mustbecolor = 1
            else:
                mustbecolor = 0
            siz = self.size_of_structure[struc] # 5 for a cc, 2 for a depot etc
            if gridplace in self.possible_cc_positions:
                if (siz == 5) and (struc != MAINCELLBLOCK):
                    siz = 1
            if struc == MAINCELLBLOCK:
                for vakx in range(round(x-siz/2),round(x+siz/2)):
                    for vaky in range(round(y-siz/2),round(y+siz/2)):
                        if (vakx != round(x-0.5)) or (vaky != round(y-0.5)):
                            placable = placable and (self.read_layout(vakx, vaky) == mustbecolor)
            else:
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
                siz = 9
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

    def random_chance(self, amount) -> bool:
        # bv random_chance(3) is kans 0.333
        return (random.randrange(0, amount) == 0)

    def maxam_of_thing(self,thing) -> int:
        maxam = 100
        if thing in self.all_structures_tobuildwalk:
            if thing in [ARMORY,FUSIONCORE,ENGINEERINGBAY,GHOSTACADEMY]:
                maxam = 2
            if thing == FACTORY:
                maxam = 3
            if thing == MISSILETURRET:
                maxam = len(self.all_bases)*6
            if thing == BARRACKS:
                if self.opening_name != 'marine':
                    maxam = len(self.all_bases)*2+1
            if thing == STARPORT:
                if self.opening_name != 'two liberators':
                    maxam = len(self.all_bases)
        elif thing in self.all_structures:
            pass
        elif type(thing) == UpgradeId:
            maxam = 1
        else:
            # army
            if thing in [RAVEN,HELLION]:
                maxam = 1
            if thing in [MARAUDER,SIEGETANK,WIDOWMINE,VIKINGFIGHTER, REAPER]:
                maxam = 15
            if thing == LIBERATOR:
                maxam = 3
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
                if self.opening_name != 'marine':
                    maxam = len(self.all_future_basepos)*2+1
            if thing == STARPORT:
                if self.opening_name != 'two liberators':
                    maxam = len(self.all_future_basepos)
        elif thing in self.all_structures:
            pass
        elif type(thing) == UpgradeId:
            maxam = 1
        else:
            #           army
            if thing in [RAVEN,HELLION]:
                maxam = 1
            if thing in [MARAUDER,SIEGETANK,WIDOWMINE,VIKINGFIGHTER,REAPER]:
                maxam = 15
            if thing == LIBERATOR:
                maxam = 3
        return maxam

    #*********************************************************************************************************************

    # distance
    def sdist(self,p,q):
        return (p.x-q.x)*(p.x-q.x) + (p.y-q.y)*(p.y-q.y)
 
    def circledist(self,p,q):
        # common distance
        sd = (p.x-q.x)*(p.x-q.x) + (p.y-q.y)*(p.y-q.y)
        return sqrt(sd)

    def simpledist(self,p,q):
        dx = abs(p.x-q.x)
        dy = abs(p.y-q.y)
        return dx + dy + max(dx,dy)
 
    def near(self,p,q,supdist) -> bool:
        # works for integers as well as for floats
        return (self.sdist(p,q) < supdist*supdist)

    def make_circle(self,n):
        # n points on the unitcircle
        self.circle = []
        for i in range(0,n):
            alfa = 2*pi*i/n
            point = Point2((cos(alfa),sin(alfa)))
            self.circle.append(point)

    def flee(self,posi,dist) -> Point2:
        #  get a random point at distance 'dist' from your point 'posi'
        offset = random.choice(self.flee_circle)
        return Point2((posi.x+offset.x*dist,posi.y+offset.y*dist))

    ########################## OVERVIEW OF THE MAP PER EXPO

    # a "maptile" is a 10*10 square tile, the maptiles cover the map
    def maptile_of_pos(self, pos: Point2) -> int:
        return (round(pos.x) // self.maptile_width) + self.maptile_amount * (round(pos.y) // self.maptile_width)

    def pos_of_maptile(self, maptile: int) -> Point2:
        return Point2(((maptile % self.maptile_amount)*self.maptile_width+self.maptile_half,
                       (maptile // self.maptile_amount)*self.maptile_width+self.maptile_half))

    # a expo is a group of maptiles, roughly around an expansion
    def init_expo(self):
        self.expos = len(self.expansion_locations_list)
        self.pos_of_expo = {}
        for expo in range(0, self.expos):
            self.pos_of_expo[expo] = self.expansion_locations_list[expo]
        self.expo_of_maptile = {}
        for maptile in range(0,self.maptiles):
            tile_pos = self.pos_of_maptile(maptile)
            bestsd = 99999
            for expo in range(0,self.expos):
                expo_pos = self.pos_of_expo[expo]
                sd = self.sdist(tile_pos,expo_pos)
                if sd < bestsd:
                    bestsd = sd
                    chosen_expo = expo
            self.expo_of_maptile[maptile] = chosen_expo

    def expo_of_pos(self, pos: Point2) -> int:
        return self.expo_of_maptile[self.maptile_of_pos(pos)]


    def ground_strength(self, one) -> float:
        return sqrt(one.ground_dps * (one.health + one.shield))

    def air_strength(self, one) -> float:
        return sqrt(one.air_dps * (one.health + one.shield))


    def init_step_expo(self):
        self.minerals_of_expo = {}
        self.vespene_of_expo = {}
        self.scvs_of_expo = {}
        self.units_of_expo = {}
        self.structures_of_expo = {}
        self.enemy_units_of_expo = {}
        self.enemy_structures_of_expo = {}
        self.ground_strength_of_expo = {}
        self.air_strength_of_expo = {}
        self.worth_of_expo = {}
        for expo in range(0,self.expos):
            self.minerals_of_expo[expo] = set()
            self.vespene_of_expo[expo] = set()
            self.scvs_of_expo[expo] = set()
            self.structures_of_expo[expo] = set()
            self.enemy_units_of_expo[expo] = set()
            self.units_of_expo[expo] = set()
            self.ground_strength_of_expo[expo] = 0
            self.enemy_structures_of_expo[expo] = set()
            self.air_strength_of_expo[expo] = 0
            self.worth_of_expo[expo] = 0
        #
        for one in self.mineral_field:
            expo = self.expo_of_pos(one.position)
            self.minerals_of_expo[expo].add(one)
        for one in self.vespene_geyser:
            place = one.position
            for bui in self.structures(REFINERY) + self.structures(REFINERYRICH):
                if bui.position == place:
                    self.vespene_of_expo[expo].add(one)
        for one in self.units(SCV):
            expo = self.expo_of_pos(one.position)
            self.scvs_of_expo[expo].add(one)
        for one in self.units:
            expo = self.expo_of_pos(one.position)
            self.units_of_expo[expo].add(one)
            self.ground_strength_of_expo[expo] += self.ground_strength(one)
            self.air_strength_of_expo[expo] += self.air_strength(one)
        for one in self.enemy_units:
            expo = self.expo_of_pos(one.position)
            self.enemy_units_of_expo[expo].add(one)
            self.ground_strength_of_expo[expo] -= self.ground_strength(one)
            self.air_strength_of_expo[expo] -= self.air_strength(one)
        for one in self.structures:
            expo = self.expo_of_pos(one.position)
            kind = one.type_id
            self.structures_of_expo[expo].add(one)
            self.ground_strength_of_expo[expo] += self.ground_strength(one)
            self.air_strength_of_expo[expo] += self.air_strength(one)
            cost = self.get_total_cost(kind)
            self.worth_of_expo[expo] += cost.minerals + 2*cost.vespene
        for one in self.enemy_structures:
            expo = self.expo_of_pos(one.position)
            kind = one.type_id
            self.enemy_structures_of_expo[expo].add(one)
            self.ground_strength_of_expo[expo] -= self.ground_strength(one)
            self.air_strength_of_expo[expo] -= self.air_strength(one)
            cost = self.get_total_cost(kind)
            self.worth_of_expo[expo] += cost.minerals + 2 * cost.vespene
        #

    #*********************************************************************************************************************

    #   techtree
    def init_structures(self,species,barra,builddura, size):
        self.routine = 'init_structures'
        self.log_fail((species in {'T','P','Z'}),'')
        self.log_fail((type(barra) == UnitTypeId),'')
        self.all_structures.append(barra)
        self.builddura_of_thing[barra] = builddura
        self.size_of_structure[barra] = size
        self.species_of_structure[barra] = species
        if species == 'T':
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

    def cradle_of_thing(self, mari):
        barra = None
        for pair in self.cradle:
            if pair[0] == mari:
                barra = pair[1]
        return barra

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

    def init_maxhealth(self, thing, maxh):
        self.routine = 'init_maxhealth'
        self.maxhealth[thing] = maxh

    def init_bcenemy(self, thing, danger, hate):
        # shoot at most hated
        # flee at dangersum 100
        self.bcenemies.add(thing)
        self.danger_of_bcenemy[thing] = danger
        self.hate_of_bcenemy[thing] = hate

    def init_army(self,thing,dura,supply,airground):
        self.routine = 'init_army'
        self.all_army.append(thing)
        self.supply_of_army[thing] = supply
        self.builddura_of_thing[thing] = dura
        self.airground_of_unit[thing] = airground

    def init_labarmy(self):
        for thing in self.all_army:
            needslab = False
            for pair in self.techtree:
                if pair[0] == thing:
                    if pair[1] in self.all_labs:
                        needslab = True
            if needslab:
                self.all_labarmy.append(thing)

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

    def we_finished_amount(self, barra) -> int:
        self.routine = 'we_finished_amount'
        have = 0
        for (thing,pos) in self.birds:
            if (thing == barra):
                have += 1
        return have

    def we_started_a(self,barra) -> bool:
        self.routine = 'we_started_a'
        have = False
        for (thing,pos) in self.birds:
            have = have or (thing == barra)
        for (marty,bartype,pos,dura) in self.eggs:
            have = have or (marty == barra)
        for (marty,bartype,pos,dura,owner) in self.preps:
            have = have or (marty == barra)
        for (thing,pos,owner) in self.thoughts:
            have = have or (thing == barra)
        return have

    def we_started_at(self,barra,atpos) -> bool:
        self.routine = 'we_started_at'
        have = False
        for (thing,pos) in self.birds:
            have = have or ((thing == barra) and (pos == atpos))
        for (marty,bartype,pos,dura) in self.eggs:
            have = have or ((marty == barra) and (pos == atpos))
        for (marty,bartype,pos,dura,owner) in self.preps:
            have = have or ((marty == barra) and (pos == atpos))
        for (thing,pos,owner) in self.thoughts:
            have = have or ((thing == barra) and (pos == atpos))
        return have

    def we_started_hall_at(self, atpos) -> bool:
        self.routine = 'we_started_hall_at'
        have = False
        kinds = [COMMANDCENTER,ORBITALCOMMAND,PLANETARYFORTRESS]
        for (thing,pos) in self.birds:
            have = have or ((pos == atpos) and (thing in kinds))
        for (marty,bartype,pos,dura) in self.eggs:
            have = have or ((pos == atpos) and (marty in kinds))
        for (marty,bartype,pos,dura,owner) in self.preps:
            have = have or ((pos == atpos) and (marty in kinds))
        for (thing,pos,owner) in self.thoughts:
            have = have or ((pos == atpos) and (thing in kinds))
        return have

    def we_started_amount(self,barra) -> int:
        self.routine = 'we_started_amount'
        have = 0
        for (thing,pos) in self.birds:
            if (thing == barra):
                have += 1
        for (marty,bartype,pos,dura) in self.eggs:
            if (marty == barra):
                have += 1
        for (marty,bartype,pos,dura,owner) in self.preps:
            if (marty == barra):
                have += 1
        for (thing,pos,owner) in self.thoughts:
            if (thing == barra):
                have += 1
        return have

    #*********************************************************************************************************************

    def no_doubling(self, tag) -> bool:
        # checks against reissuing a command within 5 frames, the order may not have been seen yet.
        may = True
        if tag in self.doubling_frame:
            if self.doubling_frame[tag] + 5 > self.frame:
                may = False
        if may:
            self.doubling_frame[tag] = self.frame
        return may

    def clean_doubling(self):
        # occasional cleanup
        new_doubling_frame = {}
        for tag in self.doubling_frame:
            if self.doubling_frame[tag] + 5 > self.frame:
                new_doubling_frame[tag] = self.doubling_frame[tag]
        self.doubling_frame = new_doubling_frame

    def get_total_cost(self,building):
        if building == NUKESILONOVA:
            return Cost(100,100)
        else:
            return self.calculate_unit_value(building)

    def get_added_cost(self,building):
        if building == NUKESILONOVA:
            return Cost(100,100)
        else:
            return self.calculate_cost(building)

    def can_pay(self,thing) -> bool:
        # purse contains a small amount for max self.patience frames
        cost = self.get_added_cost(thing)
        return (self.minerals >= self.purse.minerals + cost.minerals) and (self.vespene >= self.purse.vespene + cost.vespene)

    def bug_can_pay(self,upg) -> bool:
        self.routine = 'bug_can_pay'
        # circumvent a bug
        cost_minerals = 9999
        cost_vespene = 9999
        # numbers correct jun 2020
        if upg == TERRANVEHICLEANDSHIPARMORSLEVEL1:
            cost_minerals = 100
            cost_vespene = 100
        if upg == TERRANVEHICLEANDSHIPARMORSLEVEL2:
            cost_minerals = 175
            cost_vespene = 175
        if upg == TERRANVEHICLEANDSHIPARMORSLEVEL3:
            cost_minerals = 250
            cost_vespene = 250
        return (self.minerals >= self.purse.minerals + cost_minerals) and (self.vespene >= self.purse.vespene + cost_vespene)

    #*********************************************************************************************************************

    def create_block(self, pos,measure):
        for tx in range(0,measure[0]):
            px = round(pos.x + tx - measure[0]/2)
            for ty in range(0,measure[1]):
                py = round(pos.y + ty - measure[1]/2)
                layout_if.layout[px][py] = 1

    def get_layout(self):
        self.routine = 'get_layout'
        #
        #  terrain_height is in a col=right,row=up notation
        layout_if.height = []
        for col in range(0,200):
            collist = []
            for row in range(0,200):
                point = Point2((col,row))
                #  point2 is a (x=right,y=up notation)
                if (col<self.map_right) and (col>=self.map_left) and (row<self.map_top) and (row>=self.map_bottom):
                    info = self.game_info.terrain_height[point]
                else:
                    info = 0
                collist.append(info)
            layout_if.height.append(collist)
        #  layout is in a col=right,row=up notation
        layout_if.layout = []
        for col in range(0,200):
            collist = []
            for row in range(0,200):
                info = 0
                point = Point2((col,row))
                #  point2 is a (x=right,y=up notation)
                if (col<self.map_right) and (col>=self.map_left) and (row<self.map_top) and (row>=self.map_bottom):
                    if self.game_info.pathing_grid[point] == 0:
                        info += 1
                    if self.game_info.placement_grid[point] == 0:
                        info += 2
                    # h = self.get_terrain_height(point)
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
        square = (round(self.loved_pos.x-0.5),round(self.loved_pos.y-0.5))
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
        self.log_success('hometop '+str(len(self.hometop)))


    def get_enemytop(self):
        # get an empty square
        square = (round(self.enemy_pos.x-0.5),round(self.enemy_pos.y-0.5))
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
        self.log_success('enemytop '+str(len(self.enemytop)))

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
                        #  accept idler if 1.7 times as far
                        if self.job_of_scvt[scvt] in self.no_jobs:
                            sd /= 3
                        #   accept mimminer if 1.4 times as far
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
        best_sdist = 99999
        best_mimt = self.notag
        expo = self.expo_of_pos(point)
        for mim in self.minerals_of_expo[expo]:
            mimt = mim.tag
            if mimt in self.all_mimt:
                if self.count_of_mimt[mimt] < 2:
                    sd = self.sdist(mim.position,point)
                    if sd < best_sdist:
                        best_sdist = sd
                        best_mimt = mimt
        if best_sdist == 99999:
            for mim in self.mineral_field:
                mimt = mim.tag
                if mimt in self.all_mimt:
                    if self.count_of_mimt[mimt] < 2:
                        sd = self.sdist(mim.position,point)
                        if sd < best_sdist:
                            best_sdist = sd
                            best_mimt = mimt
        mimt = best_mimt
        self.log_fail((best_sdist < 99999),'no workposition on minerals found.')
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
        for nr in range(0, len(self.scout1_pos)):
            honk = self.scout1_pos[nr]
            sd = self.sdist(point, honk)
            if sd < bestsd:
                bestsd = sd
                bestnr = nr
        return bestnr

    def proxy(self, point) -> bool:
        return self.near(point,self.enemy_pos,63)


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
        # a cc is deleted from birds when it eggs into a pfoc
        self.birds = set()
        for kind in self.all_structures:
            for stru in self.structures(kind).ready:
                basekind = self.basekind_of(kind)
                pos = self.position_of_building(stru)
                self.birds.add((basekind,pos))
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
        # a cc is deleted from birds when it eggs into a pfoc
        todel = set()
        for (cctype,pfoctype,pos,dura) in self.eggs:
            if pfoctype in self.all_pfoc:
                todel.add((cctype,pos))
        self.birds -= todel
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
                    for thatone in self.structures: # do not mention thing, for refineryrich
                        if thatone.position == goal:
                            restdura = build_dura*(1.0-thatone.build_progress)
                    if restdura > 0:
                        self.eggs.add((thing,scv,goal,restdura))
        for pair in self.cradle:
            martype = pair[0]
            dura = self.builddura_of_thing[martype]
            bartype = pair[1]
            if martype in self.all_upgrades:
                abi = sc2.dicts.unit_research_abilities.RESEARCH_INFO[bartype][martype]['ability']
            elif martype in self.all_labs:
                if martype in [BARRACKSREACTOR,FACTORYREACTOR,STARPORTREACTOR,REACTOR]:
                    abi = AbilityId.BUILD_REACTOR
                else:
                    abi = AbilityId.BUILD_TECHLAB
            elif martype == NUKESILONOVA:
                abi = AbilityId.BUILD_NUKE
            else:
                abi = sc2.dicts.unit_train_build_abilities.TRAIN_INFO[bartype][martype]['ability']
            for bar in self.structures(bartype).ready:
                if bar.is_using_ability(abi):
                    progress = bar.orders[0].progress
                    restdura = dura * (1.0 - progress)
                    pos = self.position_of_building(bar)
                    self.eggs.add((martype,bartype,pos,restdura))
        martype = SCV
        abi = AbilityId.COMMANDCENTERTRAIN_SCV
        for bartype in [COMMANDCENTER,ORBITALCOMMAND,PLANETARYFORTRESS]:
            for bar in self.structures(bartype).ready:
                if bar.is_using_ability(abi):
                    dura = self.builddura_of_thing[martype]
                    progress = bar.orders[0].progress
                    restdura = dura * (1.0 - progress)
                    pos = bar.position
                    self.eggs.add((martype,bartype,pos,restdura))
        self.log_eggs()

    def get_preps(self):
        # overview of things currently being prepaired
        self.preps = set()
        for scv in self.units(SCV):
            scvt = scv.tag
            if scvt in self.goal_of_trabu_scvt:
                if self.job_of_scvt[scvt] in ('traveller','settler','fencer'):
                    goal = self.goal_of_trabu_scvt[scvt]
                    thing = self.structure_of_trabu_scvt[scvt]
                    owner = self.owner_of_trabu_scvt[scvt]
                    pos = scv.position
                    restdura = self.walk_duration(pos,goal)
                    self.preps.add((thing, scv, goal, restdura, owner))
        for strt in self.ambition_of_strt: # pfoc, labs
            martype = self.ambition_of_strt[strt]
            owner = self.owner_of_ambigymstrt[strt]
            dura = self.ambitiondura
            for abar in self.structures:
                if abar.tag == strt:
                    bar = abar
                    pos = self.position_of_building(abar)
            for (othermartype,otherbartype,otherpos,otherdura) in self.eggs: # calc eggs first
                if (otherbartype == bar.type_id) and (otherpos == pos):
                    dura = otherdura
            self.preps.add((martype, bar.type_id, pos, dura, owner))
        for strt in self.gym_of_strt: # upgr, army
            martype = self.gym_of_strt[strt]
            owner = self.owner_of_ambigymstrt[strt]
            dura = self.gymdura
            for abar in self.structures:
                if abar.tag == strt:
                    bar = abar
                    pos = self.position_of_building(abar)
            for (othermartype,otherbartype,otherpos,otherdura) in self.eggs: # calc eggs first
                if (otherbartype == bar.type_id) and (otherpos == pos):
                    dura = otherdura
            self.preps.add((martype, bar.type_id, pos, dura, owner))
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
        for (th,pl) in self.chosenplaces:
            if th == COMMANDCENTER:
                afb.add(pl)
        self.all_future_basepos = afb
        

    def find_tobuildwalk_a_place(self, building) -> bool:
        self.routine = 'find_tobuildwalk_a_place'
        self.log_placing('find a place for '+building.name)
        #  Get a random place
        #  If no place could be found, return False
        #  Also for future buildings.
        #  Use buildorder, check_layout
        #  Do write_layout after calling this
        for (bu,pl) in self.chosenplaces:
            self.log_placing('   chosenplace '+bu.name+' '+self.txt(pl))
        if building not in self.all_structures_tobuildwalk:
            self.log_success('BUG 26006 '+building.name)
        found = False
        # use chosen places
        todel = -1
        for nr in range(0,len(self.chosenplaces)):
            (bu,pl) = self.chosenplaces[nr]
            if (bu == building) and (not found):
                place = pl
                found = True
                todel = nr
        if todel >= 0:
            del self.chosenplaces[todel]
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
            self.tips_used.add(maybe_nr)
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
                        self.tips_used.add(nr)
                        self.log_placing('using a hard placement tip')
                        found = True
        # find a new place directly
        if (building == COMMANDCENTER) and (not found):
            tried = 0
            found = False
            while (not found) and (tried < 20):
                place = random.choice(self.expansion_locations_list)
                found = True
                found = found and (self.check_layout(building, place))
                if len(self.all_bases) < 6:
                    found = found and (not self.proxy(place))
                found = found and (place not in [tow.position for tow in self.all_future_basepos])
                tried += 1
        elif (building == REFINERY) and (not found):
            # first try with existing bases, then with future bases.
            places = []
            for gey in self.vespene_geyser:
                place = gey.position
                if self.check_layout(building, place):
                    if not self.we_started_at(building,place):
                        if place not in [pl for (th, pl) in self.buildorder]:
                            seen = False
                            for cc in self.all_bases:
                                if self.near(place, cc.position, self.miner_bound):
                                    seen = True
                            if seen:
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
                        if not self.we_started_at(building, place):
                            if place not in [pl for (th, pl) in self.buildorder]:
                                seen = False
                                for cc in self.all_bases:
                                    if self.near(place, cc.position, self.miner_bound):
                                        seen = True
                                if seen:
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
                place = self.place_around(building, fixplace)
                found = True
            else:
                fixplace = self.loved_pos
                place = self.place_around(building, fixplace)
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
                barra = self.cradle_of_thing(th)
                haveit = (barra in bag)
                for (marty, bartype, pos, dura) in self.eggs:
                    haveit = haveit or (marty == barra)
                for (marty, bartype, pos, dura, owner) in self.preps:
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
        crad = self.cradle_of_thing(thing)
        # needslab ?/n/y
        needslab = '?'
        if thing in self.all_labs + self.all_pfoc:
            needslab = 'n'
        for pair in self.techtree:
            if pair[0] == thing:
                if (pair[1] in self.all_labs) and (pair[1] != crad):
                    # stimpack is upgraded IN a lab, but that lab does not need a lab.
                    needslab = 'y'
        # Everything has a cradle
        # crad could exist, or be ordered, or be in the buildorder
        self.crad_places = set()
        for stru in self.structures(crad).ready:
            pos = self.position_of_building(stru)
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
                elif (needslab == '?') or (pos == self.somewhere):
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
        for (marty,bartype,pos,dura) in self.eggs:
            self.add_sit(marty,dura)
        for (marty,bartype,pos,dura,owner) in self.preps:
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
            cradle = self.cradle_of_thing(thing)
            if cradle is not None:
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


    ################################################################################

    def earn_paysupply(self, thing):
        if thing == SCV:
            self.earn_supply_left -= 1
            self.earn_supply_used += 1
        elif thing in self.all_army:
            sup = self.supply_of_army[thing]
            self.earn_supply_left -= sup
            self.earn_supply_used += sup

    def earn_pay(self, thing):
        cost = self.get_added_cost(thing)
        self.earn_mim -= cost.minerals
        self.earn_gas -= cost.vespene
        self.earn_paysupply(thing)
        self.log_earn('payed min '+str(cost.minerals)+'   gas '+str(cost.vespene)+'   for a '+thing.name)

    def earn_during(self, dura):
        self.log_earn('having min '+str(self.earn_mim)+'   gas '+str(self.earn_gas)+'   supleft '+str(self.earn_supply_left))
        self.log_earn('time '+str(dura))
        mimmers = len(self.earn_mimmers) + 6 * len(self.earn_orbitals)
        gassers = len(self.earn_gassers)
        self.earn_mim = self.earn_mim + dura * (mimmers * self.mim_speed)
        self.earn_gas = self.earn_gas + dura * (gassers * self.gas_speed)
        self.log_earn('having min '+str(self.earn_mim)+'   gas '+str(self.earn_gas)+'   supleft '+str(self.earn_supply_left))


    def earn_dura_of_minerals(self, thing) -> float:
        cost = self.get_added_cost(thing)
        mim_gap = cost.minerals - self.earn_mim
        mimmers = len(self.earn_mimmers) + 6 * len(self.earn_orbitals)
        if (mim_gap <= 0):
            mim_dura = 0
        elif mimmers == 0:
            mim_dura = 99999
        else:
            mim_dura = mim_gap / (mimmers * self.mim_speed)
        return mim_dura

    def earn_dura_of_minerals_minusoneman(self, thing) -> float:
        cost = self.get_added_cost(thing)
        mim_gap = cost.minerals - self.earn_mim
        mimmers = max(0, len(self.earn_mimmers) + 6 * len(self.earn_orbitals) - 1)
        if (mim_gap <= 0):
            mim_dura = 0
        elif mimmers == 0:
            mim_dura = 99999
        else:
            mim_dura = mim_gap / (mimmers * self.mim_speed)
            # during this time, a new scv can be needed
        return mim_dura


    def earn_dura_of_gas(self, thing) -> float:
        cost = self.get_added_cost(thing)
        gas_gap = cost.vespene - self.earn_gas
        gassers = len(self.earn_gassers)
        if (gas_gap <= 0) or (cost.vespene == 0):
            gas_dura = 0
        elif gassers == 0:
            gas_dura = 99999
        else:
            gas_dura = gas_gap / (gassers * self.gas_speed)
        return gas_dura


    def earn_situation(self):
        self.routine = 'earn_situation'
        self.earn_show = False
        self.earn_tags = set()
        self.earn_halls = set()
        self.earn_orbitals = set()
        self.earn_growing = set()
        self.earn_refineries = set()
        self.earn_scvs = set()
        self.earn_mimmers = set()
        self.earn_gassers = set()
        self.earn_idlers = set()
        self.earn_specials = set()
        self.earn_builders = set()
        #
        self.earn_mim = 0 # temporary value
        self.earn_gas = 0 # temporary value
        self.earn_supply_left = 0
        self.earn_supply_used = 0
        self.earn_supply_cap = 0
        self.earn_supply_egg = 0
        for (martype, bartype, pos, dura) in self.eggs:
            self.earn_paysupply(martype)
            if martype == SUPPLYDEPOT:
                self.earn_event('start depot')
        for (th, pos) in self.birds:
            self.earn_paysupply(th)
            if th in [COMMANDCENTER, ORBITALCOMMAND, PLANETARYFORTRESS]:
                self.earn_event('new hall')
            if th == ORBITALCOMMAND:
                self.earn_event('new orbital')
            if th == REFINERY:
                self.earn_event('new refinery')
            if th == SCV:
                self.earn_event('new scv')
            if th == SUPPLYDEPOT:
                self.earn_event('start depot')
                self.earn_event('new depot')
        for scvt in self.structure_of_trabu_scvt:
            self.earn_event('start build')
        for scvt in self.job_of_scvt:
            if self.job_of_scvt[scvt] in ['scout', 'cheeser']:
                self.earn_event('new special')
        for (martype, bartype, pos, dura) in self.eggs:
            if (martype in self.all_pfoc):
                self.earn_event('start grow')
        self.earn_mim = self.minerals
        self.earn_gas = self.vespene
        self.earn_show = True
        self.log_earn('This is the current situation')


    def earn_wantdepot(self) -> bool:
        wa = False
        if (self.earn_supply_left + self.earn_supply_egg < 4 + self.earn_supply_used * self.supply_rate) and (self.earn_supply_cap < 200):
            if self.earn_supply_used >= 20: # do not interfere at the start
                wa = True
        return wa


    def earn_wantscv(self) -> bool:
        wa = True
        if len(self.earn_idlers) >= 11:
            wa = False
        if len(self.earn_scvs) >= 100 - ((self.earn_gas + self.earn_mim) / 150):
            wa = False
        return wa


    def earn_event(self, event):
        # Model to grow from a given gamesituation
        # tags
        #    halls
        #       orbitals     autoproduces minerals
        #       growing      halls that can not produce scvs
        #    refineries
        #    scvs
        #       mimmers
        #       gassers
        #       idlers
        #       specials
        #       builders
        #
        # Reminders:
        #    minerals and gas never empty
        #    no place
        #    no enemies
        #    orbitals always mule
        #
        new_tag = random.randrange(0, 99999)
        while new_tag in self.earn_tags:
            new_tag = random.randrange(0, 99999)
        self.earn_tags.add(new_tag)
        #
        if event == 'new scv':
            scv = new_tag
            self.earn_scvs.add(scv)
            self.earn_idlers.add(scv)
            # in the end of this routine, filling of gas and minerals
        elif event == 'new refinery':
            # earn fills gas
            ref = new_tag
            self.earn_refineries.add(ref)
        elif event == 'new hall':
            hall = new_tag
            self.earn_halls.add(hall)
            self.earn_supply_left += 15
            self.earn_supply_cap += 15
        elif event == 'start depot':
            self.earn_supply_egg += 4
        elif event == 'new depot':
            self.earn_supply_left += 8
            self.earn_supply_cap += 8
            self.earn_supply_egg -= 4
        elif event == 'new orbital':
            orbi = new_tag
            self.earn_orbitals.add(orbi)
        elif event == 'new special':
            work = 1
            todel = set()
            for scv in self.earn_idlers:
                if work > 0:
                    self.earn_specials.add(scv)
                    todel.add(scv)
                    work -= 1
            self.earn_idlers -= todel
            todel = set()
            for scv in self.earn_mimmers:
                if work > 0:
                    self.earn_specials.add(scv)
                    todel.add(scv)
                    work -= 1
            self.earn_mimmers -= todel
            todel = set()
            for scv in self.earn_gassers:
                if work > 0:
                    self.earn_specials.add(scv)
                    todel.add(scv)
                    work -= 1
            self.earn_gassers -= todel
        elif event == 'start build':
            work = 1
            todel = set()
            for scv in self.earn_idlers:
                if work > 0:
                    self.earn_builders.add(scv)
                    todel.add(scv)
                    work -= 1
            self.earn_idlers -= todel
            todel = set()
            for scv in self.earn_mimmers:
                if work > 0:
                    self.earn_builders.add(scv)
                    todel.add(scv)
                    work -= 1
            self.earn_mimmers -= todel
            todel = set()
            for scv in self.earn_gassers:
                if work > 0:
                    self.earn_builders.add(scv)
                    todel.add(scv)
                    work -= 1
            self.earn_gassers -= todel
        elif event == 'stop build':
            work = 1
            todel = set()
            for scv in self.earn_builders:
                if work > 0:
                    self.earn_idlers.add(scv)
                    todel.add(scv)
                    work -= 1
            self.earn_builders -= todel
        elif event == 'start grow':
            work = 1
            for hall in self.earn_halls:
                if work > 0:
                    self.earn_growing.add(hall)
                    work -= 1
        elif event == 'stop grow':
            work = 1
            todel = set()
            for hall in self.earn_growing:
                if work > 0:
                    todel.add(hall)
                    work -= 1
            self.earn_growing -= todel
        else:
            print('earn_event no event')
        #
        work = 3 * len(self.earn_refineries) - len(self.earn_gassers)
        if work > 0:
            todel = set()
            for scv in self.earn_idlers:
                if work > 0:
                    self.earn_gassers.add(scv)
                    todel.add(scv)
                    work -= 1
            self.earn_idlers -= todel
            todel = set()
            for scv in self.earn_mimmers:
                if work > 0:
                    self.earn_gassers.add(scv)
                    todel.add(scv)
                    work -= 1
            self.earn_mimmers -= todel
        work = 16 * len(self.earn_halls) - len(self.earn_mimmers)
        if work > 0:
            todel = set()
            for scv in self.earn_idlers:
                if work > 0:
                    self.earn_mimmers.add(scv)
                    todel.add(scv)
                    work -= 1
            self.earn_idlers -= todel
        self.log_earn(event + '   mimmers ' + str(len(self.earn_mimmers)) + '   gassers ' + str(len(self.earn_gassers))
                  + '   idl ' + str(len(self.earn_idlers)) + '   hal ' + str(len(self.earn_halls))
                  + '   orb ' + str(len(self.earn_orbitals)) + '   gas ' + str(len(self.earn_refineries)))

#*********************************************************************************************************************
#   timing routine
#   order = (thing,place)
#   starting from now, make a planning for buildorder
#   planning is time duration, from now to the startmoment of construction
#   that is useful to get builders in time at the buildsites
#   and useful for comparing buildorders
#   the planning should be somewhat accurate for small current_moment
#
#   the planning does not wait for currently planned buildings to finish or even start-to-construct
#   the finishmoment of already planned buildings is calculated and used for the techtree and the emerging free scv
#   the planning does start-to-construct in the order given in buildorder
#
#   IN:
#       the current game situation and administration, those are called the "situation".
#       buildorder [(BARRACKS,(16,40)),(SUPPLYDEPOT,(119,3)),(MARINE,somewhere),...
#   OUT:
#       planning [(BARRACKS,TagJohn,(16,40),4,17,22)
#                ,(SUPPLYDEPOT,tagMohamad,(119,3),8,23,30)
#                ,(MARINE,notag,(16,40),220,220,265),...
#       The 3 moments are: start-walk, start-construct,end-construct
#   LOCAL:
#       current_moment 17
#       current_freescvs {(tagjohn,pos(14,107),since15),...
#           using buildplan (thingBARRACKS,tagJohn,goal(16,40),startwalk14,startconstruct17,finish19)
#       current_walking {buildplan,...
#       current_constructing {buildplan,...
#           using trainplan (thingMARINE,ataBARRACKS,place(16,40),startgym12,starttrain20,finish40)
#       current_ambition {trainplan, ...
#       current_growing {trainplan, ...
#       current_gym {trainplan, ...
#       current_training {trainplan, ...
#       current_thingkinds {thingBARRACKS,...    (finish ones)
#       current_buildings_and_parts {(thingBARRACKS,x115,y87),...     (started construction, or finished)
#       current_events {(17,'start walking',tagjohn,goal(16,40),thingBARRACKS)
#                      ,(4,'start constructing',tageddy,goal(119,3),thingBARRACKS)
#                      ,(19,'finish constructing',tagjohn,goal(16,40),thingBARRACKS)
#                      ,(2,'finish training',goal(16,40),thingSCV)
#


    def get_situation(self):
        routine = 'get_situation'
        self.situation_walking = set()
        self.situation_constructing = set()
        self.situation_ambition = set()
        self.situation_growing = set()
        self.situation_gym = set()
        self.situation_training = set()
        self.situation_thingkinds = set()
        self.fix_count_of_job()
        # for the techtree:
        for (thing,pos) in self.birds:
            self.situation_thingkinds.add(thing)
        # walk
        for (thing,scv,pos,dura) in self.eggs:
            if scv in self.units(SCV):
                buildplan = (thing, scv.tag, pos, -1, -1, dura)
                self.situation_constructing.add(buildplan)
        for (thing,scv,pos,dura,owner) in self.preps:
            if scv in self.units(SCV):
                finishmoment = dura + self.builddura_of_thing[thing]
                buildplan = (thing,scv.tag,pos,-1,dura,finishmoment)
                self.situation_walking.add(buildplan)
        # labs, pfoc
        for (thing,bartype,pos,dura) in self.eggs:
            if thing in self.all_labs + self.all_pfoc:
                scvt = self.notag
                trainplan = (thing, bartype, pos, -1, -1, dura)
                self.situation_growing.add(trainplan)
        for (thing,bartype,pos,dura,owner) in self.preps:
            if thing in self.all_labs + self.all_pfoc:
                scvt = self.notag
                finishmoment = dura + self.builddura_of_thing[thing]
                trainplan = (thing, bartype, pos, -1, dura, finishmoment)
                self.situation_ambition.add(trainplan)
        # army, upgr
        for thing in self.all_army + self.all_upgrades:
            for (martype, bartype, pos, dura) in self.eggs:
                if martype == thing:
                    trainplan = (thing, bartype, pos, -1, -1, dura)
                    self.situation_training.add(trainplan)
            for (martype,bartype,pos,dura,owner) in self.preps:
                if martype == thing:
                    finishmoment = dura + self.builddura_of_thing[thing]
                    trainplan = (thing, bartype, pos, -1, dura, finishmoment)
                    self.situation_gym.add(trainplan)
        # scv
        thing = SCV
        for (martype, bartype, pos, dura) in self.eggs:
            if martype == thing:
                trainplan = (thing, bartype, pos, -1, -1, dura)
                self.situation_training.add(trainplan)
        #
        # situation_events
        self.situation_events = set()
        for (upgr, ata, goal, mi, startgrowmoment, finishmoment) in self.situation_gym:
            self.situation_events.add((startgrowmoment, 'start training', self.notag, goal, upgr))
            self.situation_events.add((finishmoment, 'finish training', self.notag, goal, upgr))
        for (upgr, ata, goal, mi, minusone, finishmoment) in self.situation_training:
            self.situation_events.add((finishmoment, 'finish training', self.notag, goal, upgr))
        for (thing, ata, goal, mi, startgrowmoment, finishmoment) in self.situation_ambition:
            self.situation_events.add((startgrowmoment, 'start growing', self.notag, goal, thing))
            self.situation_events.add((finishmoment, 'finish growing', self.notag, goal, thing))
        for (thing, ata, goal, mi, minusone, finishmoment) in self.situation_growing:
            self.situation_events.add((finishmoment, 'finish growing', self.notag, goal, thing))
        for (thing,scvt, goal, mi, constructmoment, finishmoment) in self.situation_walking:
            self.situation_events.add((constructmoment, 'start constructing', scvt, goal, thing))
            self.situation_events.add((finishmoment, 'finish constructing', scvt, goal, thing))
        for (thing,scvt,goal,mi,minusone,finishmoment) in self.situation_constructing:
            self.situation_events.add((finishmoment, 'finish constructing', scvt, goal, thing))
        # potential builders
        self.situation_freescvs = set()
        for scv in self.units(SCV):
            scvt = scv.tag
            if scvt in self.all_scvt:
                if self.job_of_scvt[scvt] in (self.bad_jobs + self.no_jobs):
                    self.situation_freescvs.add((scvt,scv.position,0))
        # As the planning is remade often, builders should be included. They will appear at the buildposition.
        for (thing,scv,pos,dura,owner) in self.preps:
            if scv in self.units(SCV):
                dura += self.builddura_of_thing[thing]
                self.situation_freescvs.add((scv.tag, pos, dura))
        for (thing,scv,pos,dura) in self.eggs:
            if scv in self.units(SCV):
                self.situation_freescvs.add((scv.tag, pos, dura))
        # to make marines:
        # include unfinish buildings    to prevent a short disappearance
        # buildings are identified by place not tag, so we can add future buildings
        self.situation_buildings_and_parts = set()
        for (thing,pos) in self.birds:
            if thing in self.all_structures:
                self.situation_buildings_and_parts.add((thing, pos.x, pos.y))
        for (thing,scv,pos,dura) in self.eggs:
            if thing in self.all_structures:
                self.situation_buildings_and_parts.add((thing, pos.x, pos.y))
        # init earn
        self.earn_situation()


    def planning_of_buildorder(self):
        routine = 'planning_of_buildorder'
        self.log_planning('start')
        self.planning = []
        self.extra_planning = []
        # The situation is taken into current, which will shift during the look-ahead.
        current_walking = self.situation_walking.copy()
        current_constructing = self.situation_constructing.copy()
        current_gym = self.situation_gym.copy()
        current_training = self.situation_training.copy()
        current_ambition = self.situation_ambition.copy()
        current_growing = self.situation_growing.copy()
        current_thingkinds = self.situation_thingkinds.copy()
        current_buildings_and_parts = self.situation_buildings_and_parts.copy()
        current_events = self.situation_events.copy()
        current_freescvs = self.situation_freescvs.copy()
        current_moment = 0
        #
        plannable = True
        for (beautiful_thing,beautiful_place) in self.buildorder:
            if plannable:
                self.log_planning('Planning a ' + beautiful_thing.name)
                # MAKE A BEAUTIFUL_BUILDPLAN, PLAN_MOMENT AND EVENTS, AND APPEND BP TO PLANNING
                started = False
                for buildplan in current_walking:
                    (th, scvt, pos, sr, sc, fi) = buildplan
                    if (th == beautiful_thing):
                        if (pos == beautiful_place) or (beautiful_place == self.somewhere):
                            if buildplan not in self.planning:
                                beautiful_buildplan = buildplan
                                started = True
                                self.planning.append(beautiful_buildplan)
                                plan_moment = sc
                for trainplan in current_ambition | current_gym:
                    (th, ata, pos, sr, sc, fi) = trainplan
                    if (th == beautiful_thing):
                        if (pos == beautiful_place) or (beautiful_place == self.somewhere):
                            buildplan = (th, self.notag, pos, sr, sc, fi)
                            if buildplan not in self.planning:
                                beautiful_buildplan = buildplan
                                started = True
                                self.planning.append(beautiful_buildplan)
                                plan_moment = sc
                if (not started):
                    beautiful_cradle = self.cradle_of_thing(beautiful_thing)
                    # fix_somewhere, but in the current situation
                    # choose a specific cradle if the choice was delayed with 'somewhere'
                    if (beautiful_place == self.somewhere):
                        # beautiful_thing is labs, pfoc, upgr, or army. It has a unique cradle.
                        # needslab ?/n/y
                        needslab = '?'
                        if beautiful_thing in self.all_labs + self.all_pfoc:
                            needslab = 'n'
                        for pair in self.techtree:
                            if pair[0] == beautiful_thing:
                                if (pair[1] in self.all_labs) and (pair[1] != beautiful_cradle):
                                    needslab = 'y'
                        cradles = set()
                        for (thing,x,y) in current_buildings_and_parts:
                            if thing == beautiful_cradle:
                                # cradle: walk,labs
                                cradle_place = Point2((x, y))
                                # cradle can be unfinished
                                maxfinish = current_moment
                                for (thi, scvt, goal, startwalk, startconstruct, finish) in current_constructing:
                                    if (goal == cradle_place) and (thi == beautiful_cradle):
                                        maxfinish = max(finish,maxfinish)
                                for (thi, ata, goal, sg, start, finish) in current_growing | current_training:
                                    if (goal == cradle_place) and (thi == beautiful_cradle):
                                        maxfinish = max(finish,maxfinish)
                                # cradle can be in use
                                for (thi, ata, goal, sg, start, finish) in current_growing | current_training:
                                    if (goal == cradle_place) and (ata == beautiful_cradle):
                                        maxfinish = max(finish,maxfinish)
                                cradle_dura = maxfinish - current_moment
                                haslab = 'n'
                                for (otherthing, otherx, othery) in current_buildings_and_parts:
                                    if (otherthing != thing) and (otherx == x) and (othery == y) and (otherthing in self.all_labs + self.all_pfoc):
                                        haslab = 'y'
                                if (needslab == '?') or (needslab == haslab):
                                    exception = ((beautiful_thing,cradle_place) in self.unthinkable)
                                    if not exception:
                                        cradles.add((cradle_place,cradle_dura))
                        # check
                        if len(cradles) == 0:
                            self.log_success('Skipping, I have nowhere to build a '+beautiful_thing.name)
                            # maybe some other routine already built the starporttechlab
                            started = True
                            plan_moment = -1
                        # get earliest
                        bestdura = 99999
                        bestplace = self.nowhere
                        for (place,dura) in cradles:
                            if dura < bestdura:
                                bestdura = dura
                                bestplace = place
                        beautiful_place = bestplace
                if (not started):
                    # calculate times
                    build_dura = self.builddura_of_thing[beautiful_thing]
                    total_dura = 0
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
                                could_arrive_quality = could_arrive + 0.13*walk_dura
                            else:
                                could_arrive_quality = could_arrive + 0.1*walk_dura
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
                    # mim_dura
                    mim_dura = self.earn_dura_of_minerals(beautiful_thing)
                    if travel_dura > mim_dura:
                        mim_dura = self.earn_dura_of_minerals_minusoneman(beautiful_thing)
                    total_dura = max(total_dura,mim_dura)
                    # gas_dura
                    gas_dura = self.earn_dura_of_gas(beautiful_thing)
                    total_dura = max(total_dura, gas_dura)
                    # tree_dura
                    tree_dura = 0
                    for pair in self.techtree:
                        if pair[0] == beautiful_thing:
                            barra = pair[1]
                            if barra not in current_thingkinds:
                                # expect it to be started; the buildplan should respect the techtree
                                earliest = 99999
                                for (thing,scvt,goal,startwalk,startconstruct,finish) in current_constructing | current_walking:
                                    if thing == barra:
                                        if finish < earliest:
                                            earliest = finish
                                for (thing,ata,goal,startambition,startgrow,finish) in current_ambition | current_growing | current_gym | current_training:
                                    if thing == barra:
                                        if finish < earliest:
                                            earliest = finish
                                dura = earliest - current_moment
                                tree_dura = max(tree_dura,dura)
                    total_dura = max(total_dura,tree_dura)
                    # cradle_dura: how long to wait for the cradle to become idle
                    cradle_dura = 0
                    cradle_dura = 99999
                    maxfinish = current_moment
                    # cradle could be unfinished
                    for (thi, scvt, goal, startwalk, startconstruct, finish) in current_constructing:
                        if (goal == beautiful_place) and (thi == beautiful_cradle):
                            maxfinish = max(finish,maxfinish)
                    for (thi,ata,goal,sg,start,finish) in current_growing:
                        if (goal == beautiful_place) and (thi == beautiful_cradle):
                            maxfinish = max(finish,maxfinish)
                    # cradle could be busy
                    for (thi,ata,goal,sg,start,finish) in current_training | current_growing:
                        if (goal == beautiful_place) and (ata == beautiful_cradle):
                            maxfinish = max(finish,maxfinish)
                    cradle_dura = maxfinish - current_moment
                    total_dura = max(total_dura,cradle_dura)
                    #
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
                        if beautiful_thing in self.all_structures_tobuildwalk:
                            beautiful_buildplan = (beautiful_thing,beautiful_scvt,beautiful_place,plan_moment - walk_dura,plan_moment,
                                                   plan_moment + build_dura)
                            current_events.add((plan_moment - walk_dura,'start walking',beautiful_scvt,beautiful_place,beautiful_thing))
                            current_events.add((plan_moment,'start constructing',beautiful_scvt,beautiful_place,beautiful_thing))
                            current_events.add((plan_moment + build_dura,'finish constructing',beautiful_scvt,beautiful_place,beautiful_thing))
                        elif beautiful_thing in self.all_structures:
                            # pfoc,labs
                            beautiful_buildplan = (
                            beautiful_thing, self.notag, beautiful_place, plan_moment-self.ambitiondura, plan_moment, plan_moment + build_dura)
                            beautiful_trainplan = (
                            beautiful_thing, beautiful_cradle, beautiful_place, plan_moment-self.ambitiondura, plan_moment, plan_moment + build_dura)
                            current_events.add((plan_moment-self.ambitiondura, 'start ambition', self.notag, beautiful_place,beautiful_thing))
                            current_events.add((plan_moment, 'start growing', self.notag, beautiful_place,beautiful_thing))
                            current_events.add((plan_moment + build_dura, 'finish growing', self.notag, beautiful_place,beautiful_thing))
                        else:
                            # army,upgr
                            beautiful_buildplan = (beautiful_thing,self.notag,beautiful_place,plan_moment-self.gymdura,plan_moment,plan_moment + build_dura)
                            beautiful_trainplan = (beautiful_thing,beautiful_cradle,beautiful_place,plan_moment-self.gymdura,plan_moment,plan_moment + build_dura)
                            current_events.add((plan_moment-self.gymdura, 'start gym', self.notag, beautiful_place,beautiful_thing))
                            current_events.add((plan_moment, 'start training', self.notag, beautiful_place,beautiful_thing))
                            current_events.add((plan_moment + build_dura, 'finish training', self.notag, beautiful_place,beautiful_thing))
                            # forward the time to "start constructing"
                        self.planning.append(beautiful_buildplan)
                # play events out
                if plannable:
                    current_events.add((current_moment, 'realtimeevents', self.notag, self.nowhere, DRONE))
                    at_construction_start = (plan_moment < 0)
                    while (not at_construction_start) and (len(current_events) > 0):
                        nextmoment = 99999
                        for (moment,stri,scvt,goal,ething) in current_events:
                            if (moment<nextmoment):
                                nextmoment = moment
                        # happen all events at nextmoment
                        # in the order: finish, start walk, start build
                        del_current_events = set()
                        # show
                        self.log_event('frame '+self.frame_of_sec(nextmoment)+':')
                        for (moment, stri, scvt, goal, ething) in current_events:
                            if moment == nextmoment:
                                if stri == 'realtimeevents':
                                    self.log_event('   realtimeevents')
                                else:    
                                    self.log_event('   '+stri+' '+self.name(scvt)+' '+self.txt(goal)+' '+ething.name)
                        #
                        new_current_events = set()
                        for (moment, stri, escvt, egoal, ething) in current_events:
                            if (moment == nextmoment) and (stri == 'finish training'):
                                del_current_events.add((moment, stri, escvt, egoal, ething))
                                del_current_training = set()
                                for trainplan in current_training:
                                    (thing, ata, goal, startgym, starttrain, finish) = trainplan
                                    if (goal == egoal) and (moment == finish):
                                        del_current_training.add(trainplan)
                                        current_thingkinds.add(thing)
                                        if thing == SCV:
                                            self.earn_event('new scv')
                                            new_current_events.add((moment, 'realtimeevents', self.notag, self.nowhere, DRONE))
                                current_training -= del_current_training
                        for (moment, stri, escvt, egoal, ething) in current_events:
                            if (moment == nextmoment) and (stri == 'finish growing'):
                                del_current_events.add((moment, stri, escvt, egoal, ething))
                                del_current_growing = set()
                                for trainplan in current_growing:
                                    (thing, ata, goal, startambition,startgrow,finish) = trainplan
                                    if (goal == egoal) and (moment == finish):
                                        del_current_growing.add(trainplan)
                                        current_thingkinds.add(thing)
                                        if thing == ORBITALCOMMAND:
                                            self.earn_event('new orbital')
                                        if thing in self.all_pfoc:
                                            self.earn_event('stop grow')
                                            new_current_events.add((moment, 'realtimeevents', self.notag, self.nowhere, DRONE))
                                current_growing -= del_current_growing
                        for (moment, stri, escvt, egoal, ething) in current_events:
                            if (moment == nextmoment) and (stri == 'finish constructing'):
                                del_current_events.add((moment, stri, escvt, egoal, ething))
                                del_current_constructing = set()
                                for buildplan in current_constructing:
                                    (thing, tag, goal, startwalk,startconstruct,finish) = buildplan
                                    if (tag == escvt) and (goal == egoal) and (moment == finish):
                                        del_current_constructing.add(buildplan)
                                        if tag != self.notag: # self.notag is a dummy for an ad-hoc supplydepot
                                            current_freescvs.add((tag,goal,finish))
                                        current_thingkinds.add(thing)
                                        if thing == REFINERY:
                                            self.earn_event('new refinery')
                                        elif thing == COMMANDCENTER:
                                            self.earn_event('new hall')
                                            new_current_events.add((moment, 'realtimeevents', self.notag, self.nowhere, DRONE))
                                        elif thing == SUPPLYDEPOT:
                                            self.earn_event('new depot')
                                        self.earn_event('stop build')
                                current_constructing -= del_current_constructing
                        current_events |= new_current_events
                        #
                        new_current_events = set()
                        for (moment, stri, escvt, egoal, ething) in current_events:
                            if (moment == nextmoment) and (stri == 'realtimeevents'):
                                del_current_events.add((moment, stri, escvt, egoal, ething))
                                if moment >= current_moment:
                                    # The model expects continuous scv production.
                                    # If a hall is not training an scv, start it up.
                                    if self.earn_wantscv():
                                        for (hall, x, y) in current_buildings_and_parts:
                                            if hall in [COMMANDCENTER, ORBITALCOMMAND, PLANETARYFORTRESS]:
                                                hall_place = Point2((x, y))
                                                blocked = False
                                                for tp in current_gym | current_training |current_ambition | current_growing:
                                                    (thi, ata, goal, claim, moment, finish) = tp
                                                    if (ata == hall) and (goal == hall_place):
                                                        blocked = True
                                                for (thi, scvt, goal, startwalk, startconstruct, finish) in current_constructing:
                                                    if (thi == hall) and (goal == hall_place):
                                                        blocked = True
                                                for trainplan in current_growing:
                                                    (thi, ata, goal, startambition, startgrow, finish) = trainplan
                                                    if (thi == hall) and (goal == hall_place):
                                                        blocked = True
                                                if not blocked:
                                                    claim = nextmoment - self.gymdura
                                                    finish = nextmoment + self.builddura_of_thing[SCV]
                                                    trainplan = (
                                                    SCV, hall, hall_place, claim, nextmoment,finish)
                                                    extra_buildplan = (SCV,self.notag,hall_place,claim, nextmoment,finish)
                                                    self.extra_planning.append(extra_buildplan)
                                                    current_gym.add(trainplan)  # like start_gym
                                                    new_current_events.add(
                                                        (nextmoment, 'start training', self.notag, hall_place, SCV))
                                                    self.log_event('   start training ' + self.txt(hall_place) + ' SCV')
                                                    new_current_events.add((finish, 'finish training',
                                                                        self.notag, hall_place, SCV))
                                    # The model expects adequate supplydepot production.
                                    if self.earn_wantdepot():
                                        start_walk = nextmoment - 5
                                        depot_place = self.nowhere
                                        an_scvt = self.notag
                                        finish = nextmoment + self.builddura_of_thing[SUPPLYDEPOT]
                                        extra_buildplan = (SUPPLYDEPOT,an_scvt,depot_place,start_walk,nextmoment,finish)
                                        self.extra_planning.append(extra_buildplan)
                                        current_walking.add(extra_buildplan) # like start walking
                                        self.earn_event('start build') # like start walking
                                        new_current_events.add((nextmoment, 'start constructing', an_scvt, depot_place, SUPPLYDEPOT))
                                        self.log_event('   start constructing SUPPLYDEPOT')
                                        new_current_events.add((finish, 'finish constructing', an_scvt,depot_place, SUPPLYDEPOT))
                        current_events |= new_current_events
                        #
                        for (moment,stri,escvt,egoal,ething) in current_events:
                            if (moment == nextmoment) and (stri == 'start walking'):
                                del_current_events.add((moment,stri,escvt,egoal,ething))
                                del_current_freescvs = set()
                                for (tag, position, since) in current_freescvs:
                                    if tag == escvt:
                                        del_current_freescvs.add((tag, position, since))
                                current_walking.add(beautiful_buildplan)
                                self.earn_event('start build')
                                current_freescvs -= del_current_freescvs
                        for (moment,stri,escvt,egoal,ething) in current_events:
                            if (moment == nextmoment) and (stri == 'start gym'):
                                del_current_events.add((moment,stri,escvt,egoal,ething))
                                current_gym.add(beautiful_trainplan)
                        for (moment,stri,escvt,egoal,ething) in current_events:
                            if (moment == nextmoment) and (stri == 'start ambition'):
                                del_current_events.add((moment,stri,escvt,egoal,ething))
                                current_ambition.add(beautiful_trainplan)
                                if beautiful_thing == COMMANDCENTER:
                                    self.earn_event('start grow')
                        #
                        for (moment, stri, escvt, egoal,ething) in current_events:
                            if (moment == nextmoment) and (stri == 'start constructing'):
                                del_current_events.add((moment, stri, escvt, egoal, ething))
                                del_current_walking = set()
                                for buildplan in current_walking:
                                    (thing, tag, goal, startwalk,startconstruct,finish) = buildplan
                                    if (tag == escvt) and (goal == egoal) and (moment == startconstruct):
                                        del_current_walking.add(buildplan)
                                        current_constructing.add(buildplan)
                                        self.earn_pay(thing)
                                        if thing == SUPPLYDEPOT:
                                            self.earn_event('start depot')
                                        current_buildings_and_parts.add((thing, goal.x, goal.y))
                                        if (thing == beautiful_thing) and (goal == beautiful_place):
                                            at_construction_start = True
                                current_walking -= del_current_walking
                        for (moment, stri, escvt, egoal, ething) in current_events:
                            if (moment == nextmoment) and (stri == 'start growing'):
                                del_current_events.add((moment, stri, escvt, egoal, ething))
                                del_current_ambition = set()
                                for trainplan in current_ambition:
                                    (thing, ata, goal, startambition,startgrow,finish) = trainplan
                                    if (goal == egoal) and (moment == startgrow):
                                        del_current_ambition.add(trainplan)
                                        current_growing.add(trainplan)
                                        self.earn_pay(thing)
                                        current_buildings_and_parts.add((thing, goal.x, goal.y))
                                        if thing in self.all_pfoc: # delete cc at the growth of a pfoc
                                            if (ata,goal.x,goal.y) in current_buildings_and_parts: # strange
                                                current_buildings_and_parts.remove((ata, goal.x, goal.y))
                                        if (thing == beautiful_thing) and (goal == beautiful_place):
                                            at_construction_start = True
                                current_ambition -= del_current_ambition
                        for (moment, stri, escvt, egoal, ething) in current_events:
                            if (moment == nextmoment) and (stri == 'start training'):
                                del_current_events.add((moment, stri, escvt, egoal, ething))
                                del_current_gym = set()
                                for trainplan in current_gym:
                                    (thing, ata, goal, startgym,startgrow,finish) = trainplan
                                    if (goal == egoal) and (moment == startgrow):
                                        del_current_gym.add(trainplan)
                                        current_training.add(trainplan)
                                        self.earn_pay(thing)
                                        if (thing == beautiful_thing) and (goal == beautiful_place):
                                            at_construction_start = True
                                current_gym -= del_current_gym
                        current_events -= del_current_events
                        if nextmoment > current_moment:
                            dura = nextmoment - current_moment
                            self.earn_during(dura)
                            current_moment = nextmoment
                    if len(current_events) == 0:
                        self.log_success('INTERNAL ERROR planning order '+beautiful_thing.name)
                        # if the factory flies, a starport can give this error
                        plannable = False
        self.log_prediction()



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
        self.all_bases = []
        for cc in self.structures(COMMANDCENTER).ready+self.structures(ORBITALCOMMAND)+self.structures(PLANETARYFORTRESS):
            if cc.tag != self.cheese3_cc_tag: # exclude a cc for pf-rush
                self.all_bases.append(cc)
        #   ccs in construction nearly finished are included
        for cc in self.structures(COMMANDCENTER):
            if cc.build_progress > 0.85:
                if cc not in self.all_bases:
                    if cc.tag != self.cheese3_cc_tag:  # exclude a cc for pf-rush
                        self.all_bases.append(cc)
        #
        self.all_scvtags = {scv.tag for scv in self.units(SCV)}
        self.all_basetags = {cc.tag for cc in self.all_bases}
        self.all_structuretags = {struc.tag for struc in self.structures}
        self.all_bunkertags = {bun.tag for bun in self.structures(BUNKER)}
        #
        #   All idle structures
        self.idle_structure_tags = []
        for kind in self.all_structures:
            for one in self.structures(kind).ready.idle:
                self.idle_structure_tags.append(one.tag)
        #
        #   in the jump lost battlecruisers increase bc_fear
        #       uses old emotion_of_unittag info!
        living = 0
        for bc in self.units(BATTLECRUISER):
            if (bc.tag in self.emotion_of_unittag):
                if self.emotion_of_unittag[bc.tag] == 'recovering':
                    living += 1
        past = 0
        for bct in self.emotion_of_unittag:
            if self.emotion_of_unittag[bct] == 'recovering':
                past += 1
        if past > living:
            self.bc_fear = min(500,self.bc_fear+40)
        #
        # emotion_of_unittag  contains tags of all living battlecruisers, unhealthy if repairing
        new_emotion_of_unittag = {}
        for bc in self.units(BATTLECRUISER):
            if (bc.tag in self.emotion_of_unittag):
                if (self.emotion_of_unittag[bc.tag] == 'recovering'):
                    if (bc.health<self.maxhealth[bc.type_id]):
                        new_emotion_of_unittag[bc.tag] = 'recovering'
                    else:
                        new_emotion_of_unittag[bc.tag] = 'lazy'
                else:
                    new_emotion_of_unittag[bc.tag] = self.emotion_of_unittag[bc.tag]
            else:
                new_emotion_of_unittag[bc.tag] = 'lazy'
        # also siegetanks
        for tnk in self.units(SIEGETANK) + self.units(SIEGETANKSIEGED):
            if (tnk.tag in self.emotion_of_unittag):
                new_emotion_of_unittag[tnk.tag] = self.emotion_of_unittag[tnk.tag]
        self.emotion_of_unittag = new_emotion_of_unittag
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
        #
        #   gym_of_strt contains tags of living commandcenters, barracks etc
        new_gym_of_strt = {}
        for cc in self.structures.ready:
            if cc.tag in self.gym_of_strt:
                new_gym_of_strt[cc.tag] = self.gym_of_strt[cc.tag]
        self.gym_of_strt = new_gym_of_strt
        # owner_of_ambigymstrt may have outdated info
        #
        #   Count battlecruisers
        self.lastcruisercount = self.cruisercount
        self.cruisercount = self.units(BATTLECRUISER).ready.amount
        #
        #   scv
        #   The tag of existing own scvs, in this frame
        #       complication is the scv in a refinery, which does not exist temporarily
        limbo = self.supply_workers - self.units(SCV).amount
        if limbo == 0:
            self.all_scvt = [scv.tag for scv in self.units(SCV)]
            self.frame_of_missing_scvt = {}
        else:
            new_all_scvt = [scv.tag for scv in self.units(SCV)]
            for scvt in self.all_scvt:
                job = self.job_of_scvt[scvt]
                if (job == 'gasminer'):
                    if scvt not in new_all_scvt:
                        # self.log_limbo('a '+job+' in limbo '+self.name(scvt))
                        if scvt in self.frame_of_missing_scvt:
                            time_lost = self.frame - self.frame_of_missing_scvt[scvt]
                        else:
                            time_lost = 0
                            self.frame_of_missing_scvt[scvt] = self.frame
                        if time_lost < 60:
                            new_all_scvt.append(scvt)
                        else:
                            self.log_limbo('give up hope '+self.name(scvt))
                if (job == 'builder'):
                    if (self.structure_of_trabu_scvt[scvt] in [REFINERY,REFINERYRICH]):
                        if scvt not in new_all_scvt:
                            # self.log_limbo('a '+job+' in limbo '+self.name(scvt))
                            if scvt in self.frame_of_missing_scvt:
                                time_lost = self.frame - self.frame_of_missing_scvt[scvt]
                            else:
                                time_lost = 0
                                self.frame_of_missing_scvt[scvt] = self.frame
                            if time_lost < 60:
                                new_all_scvt.append(scvt)
                            else:
                                self.log_limbo('give up hope '+self.name(scvt))
            #           Take seen scvs from the missing-list
            #           Take old cases from the missing-list
            new_frame_of_missing_scvt = {}
            for scvt in self.frame_of_missing_scvt:
                if scvt not in self.all_scvtags:
                    if self.frame_of_missing_scvt[scvt] >= self.frame - 60:
                        new_frame_of_missing_scvt[scvt] = self.frame_of_missing_scvt[scvt]
            self.frame_of_missing_scvt = new_frame_of_missing_scvt
            #
            self.log_limbo(str(limbo)+' scvs missing in gas, or killed. Remembering '+str(len(self.frame_of_missing_scvt)))
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
        #   The tag of existing refineries where we want to mine from, in this frame
        self.all_gast = []
        for tow in self.all_bases:
            expo = self.expo_of_pos(tow.position)
            if self.ground_strength_of_expo[expo] >= 0:
                for gas in self.all_refineries:
                    gast = gas.tag
                    if gas.vespene_contents > 0:
                        if self.near(gas.position,tow.position,self.miner_bound):
                            self.all_gast.append(gast)
        #   The tag of existing minerals where we want to mine from, in this frame
        self.all_mimt = []
        for tow in self.all_bases:
            expo = self.expo_of_pos(tow.position)
            if self.ground_strength_of_expo[expo] >= 0:
                for mim in self.minerals_of_expo[expo]:
                    self.all_mimt.append(mim.tag)
        #   job_of_scvt contains the tag of all living scvs
        new_job_of_scvt = {}
        for scvt in self.all_scvt:
            if scvt in self.job_of_scvt:
                new_job_of_scvt[scvt] = self.job_of_scvt[scvt]
            elif scvt == self.cheese_scv_tag:
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
        #   vision_of_scvt contains the tag of living applicants and existing bases
        new_vision_of_scvt = {}
        for scvt in self.all_scvt:
            if self.job_of_scvt[scvt] == 'applicant':
                cct = self.vision_of_scvt[scvt]
                if cct in self.all_basetags:
                    new_vision_of_scvt[scvt] = cct
        self.vision_of_scvt = new_vision_of_scvt
        #   goal_of_trabu_scvt contains the tag of living traveller -> settler -> fencer -> builder scvs
        new_goal_of_trabu_scvt = {}
        for scvt in self.all_scvt:
            if self.job_of_scvt[scvt] in ['traveller','settler','fencer','builder']:
                new_goal_of_trabu_scvt[scvt] = self.goal_of_trabu_scvt[scvt]
        self.goal_of_trabu_scvt = new_goal_of_trabu_scvt
        #   structure_of_trabu_scvt contains the tag of living travellers, settlers, fencers and builders
        new_structure_of_trabu_scvt = {}
        for scvt in self.all_scvt:
            if self.job_of_scvt[scvt] in ['traveller','settler','fencer','builder']:
                new_structure_of_trabu_scvt[scvt] = self.structure_of_trabu_scvt[scvt]
        self.structure_of_trabu_scvt = new_structure_of_trabu_scvt
        # goal_of_flying_struct, structure exists
        new_goal_of_flying_struct = {}
        for structag in self.goal_of_flying_struct:
            goal = self.goal_of_flying_struct[structag]
            if structag in self.all_structuretags:
                new_goal_of_flying_struct[structag] = goal
        self.goal_of_flying_struct = new_goal_of_flying_struct
        # owner_of_trabu_scvt may have outdated info
        #
        # check for ready finished buildings
        todel = set()
        for scvt in self.structure_of_trabu_scvt:
            if self.job_of_scvt[scvt] == 'builder':
                struc = self.structure_of_trabu_scvt[scvt]
                goal = self.goal_of_trabu_scvt[scvt]
                for st in self.structures(struc).ready:
                    if self.position_of_building(st) == goal:
                        todel.add(scvt)
        # Funny, the structure is ready before the build order of the scv ends.
        # The scv will get a short time to gasp, then it will become idler.
        for scvt in todel:
            del self.structure_of_trabu_scvt[scvt]
            del self.goal_of_trabu_scvt[scvt]
            self.job_of_scvt[scvt] = 'gasper'
        #
        # scout2 died
        if self.scout2_tag != self.notag:
            if self.scout2_tag not in self.all_scvt:
                self.scout2_tag = self.notag
                self.scout2_direction = len(self.scout2_pos) - self.scout2_direction
        # army_supply
        self.army_supply = 0
        for mar in self.all_army:
            self.army_supply = self.army_supply + self.supply_of_army[mar] * len(self.units(mar))
        # enemy_buidings_permanent
        for ene in self.enemy_structures:
            self.enemy_buidings_permanent[ene.tag] = ene.position
        # some average counts related to supply from some gsl games:
        self.good_worker_supply = min(self.supply_used / 2 + 10, 80)
        self.good_army_supply = self.supply_used - self.good_worker_supply
        self.good_bases = 1 + self.supply_used / 50
        self.good_armybuildings = self.supply_used / 10
        self.good_upgradebuildings = self.supply_used / 60
        #
        # thingtag_of_repairertag: thing exists and is not full health, repairer is scv certain job
        new_thingtag_of_repairertag = {}
        for reptag in self.thingtag_of_repairertag:
            if reptag in self.all_scvt:
                job = self.job_of_scvt[reptag]
                if job in ('cheeser','repairer'):
                    thitag = self.thingtag_of_repairertag[reptag]
                    for thing in self.structures + self.units:
                        if thing.tag == thitag:
                            if thing.health < self.maxhealth[thing.type_id]:
                                new_thingtag_of_repairertag[reptag] = thitag
        self.thingtag_of_repairertag = new_thingtag_of_repairertag


    #*********************************************************************************************************************

    async def build_minima(self):
        self.routine = 'build_minima'
        if self.opening_create_units <= 0:
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
        if (self.army_supply < self.good_army_supply):
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
            self.blunt_to_bagofthings(ENGINEERINGBAY)
        # defence
        for cc in self.structures(COMMANDCENTER):
            if cc.position in self.cc_destiny:
                if self.cc_destiny[cc.position] == 'pf':
                    self.blunt_to_bagofthings(PLANETARYFORTRESS)
                else:
                    self.blunt_to_bagofthings(ORBITALCOMMAND)
        vikings = 0
        for ene in self.enemy_units:
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
    # hoopy: is this buildseries (no positions) possible?
    #        is this buildseries executable in that order from current situation?
    # buildingswithout >= labs
    # check techtree
    #
    def hoopy_add(self, thing):
        self.hoopy_made.add(thing)
        if thing in [BARRACKS,FACTORY,STARPORT,COMMANDCENTER]:
            self.transformable[thing] += 1
        elif thing in self.all_labs + self.all_pfoc:
            if thing not in self.standalone_labs:
                crad = self.cradle_of_thing(thing)
                self.transformable[crad] -= 1

    def hoopy_can_add(self,thing) -> bool:
        isha = True
        if thing in self.all_labs + self.all_pfoc:
            if thing not in self.standalone_labs:
                crad = self.cradle_of_thing(thing)
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
        for (thing,bartype,pos,dura) in self.eggs:
            self.hoopy_add(thing)
            # TODO test if the cc is in birds when the pf is in eggs
        for (thing,bartype,pos,dura,owner) in self.preps:
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
        # 'somewhere' takes a random one
        # check techtree

    def happy_add(self, thing,pos):
        # may be called in wrong order
        self.happy_made.add(thing)
        if thing in [BARRACKS,FACTORY,STARPORT,COMMANDCENTER]:
            # these not somewhere
            self.bui_of_pos[pos] = thing
            if pos in self.bui_min_lab:
                self.bui_min_lab[pos] += 1
            else:
                self.bui_min_lab[pos] = 1
        elif thing in self.all_labs + self.all_pfoc:
            if thing not in self.standalone_labs:
                basething = self.cradle_of_thing(thing)
                if pos == self.somewhere:
                    found = False
                    for pp in self.bui_of_pos:
                        if self.bui_of_pos[pp] == basething:
                            if self.bui_min_lab[pp] > 0:
                                if not found:
                                    found = True
                                    self.bui_min_lab[pp] -= 1
                else: # real pos
                    self.bui_of_pos[pos] = basething
                    if pos in self.bui_min_lab:
                        self.bui_min_lab[pos] -= 1
                    else:
                        self.bui_min_lab[pos] = -1

    def happy_can_add(self,thing,pos) -> bool:
        isha = True
        if thing in self.all_labs + self.all_pfoc:
            if thing not in self.standalone_labs:
                basething = self.cradle_of_thing(thing)
                if pos in self.bui_min_lab:
                    if self.bui_of_pos[pos] != basething:
                        isha = False
                        self.log_buildstate('buildorder error 1 ' + thing.name)
                    if self.bui_min_lab[pos] != 1:
                        isha = False
                        self.log_buildstate('buildorder error 2 '+thing.name)
                elif pos == self.somewhere:
                    found = False
                    for pp in self.bui_of_pos:
                        if self.bui_of_pos[pp] == basething:
                            if self.bui_min_lab[pp] > 0:
                                found = True
                    if not found:
                        isha = False
                else:
                    isha = False
                    self.log_buildstate('buildorder error 3 '+thing.name)
        for (th, needs) in self.techtree:
            if th == thing:
                if needs not in self.happy_made:
                    isha = False
                    self.log_buildstate('buildorder error 4 '+th.name+' needs '+needs.name)
        if thing in self.all_labarmy:
            basething = self.cradle_of_thing(thing)
            if pos in self.bui_min_lab:
                if self.bui_of_pos[pos] != basething:
                    isha = False
                    self.log_buildstate('buildorder error 5 '+thing.name)
                if self.bui_min_lab[pos] != 0:
                    isha = False
                    self.log_buildstate('buildorder error 6 '+thing.name)
            elif pos == self.somewhere:
                found = False
                for pp in self.bui_of_pos:
                    if self.bui_of_pos[pp] == basething:
                        if self.bui_min_lab[pp] == 0:
                            found = True
                if not found:
                    isha = False
                    self.log_buildstate('buildorder error 7 '+thing.name)
            else:
                isha = False
                self.log_buildstate('buildorder error 8 '+thing.name)
        return isha


    def happy_get_sit(self):
        self.routine = 'happy_get_sit'
        self.bui_min_lab = {}
        self.bui_of_pos = {}
        self.happy_made = set()
        for (thing,pos) in self.birds:
            self.happy_add(thing,pos)
            if thing in self.all_pfoc:
                self.bui_min_lab[pos] = 0
        for (thing,bartype,pos,dura) in self.eggs:
            self.happy_add(thing, pos)
        for (thing,bartype,pos,dura,owner) in self.preps:
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
        for (th, ba, po, du, ow) in self.preps:
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
            self.log_buildorder('showing buildorder: '+thing.name+' '+state)
            if state == 'new':
                if not self.happy_can_add(thing,pos):
                    self.log_success('Not happy with '+thing.name)
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
        self.bagofthings = self.bagofthings_exe.copy()
        self.bagoftree_of_bagofthings()
        self.bagoftree_exe = self.bagoftree.copy()
        self.bagofcradle_of_bagoftree()
        self.bagofcradle_exe = self.bagofcradle.copy()
        self.buildseries_of_bagofcradle()
        self.optimize_buildseries()
        self.buildseries_exe = self.buildseries.copy()

    async def make_planning_exe(self):
        self.routine = 'make_planning_exe'
        # first make buildseries
        if ((len(self.buildorder_exe) == 0)) and ((self.opening_create_units <= 0) or (self.game_phase != 'opening')):
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
                self.buildseries_exe_from_bagofthings_exe()
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
                if not self.proxy(po):
                    if po != self.somewhere:
                        self.chosenplaces.append((th,po))
            self.buildorder_of_buildseries()
            self.buildorder_exe = []
            for (th,pl) in self.buildorder:
                self.buildorder_exe.append((th,pl,'new'))
        # buildorder_exe is made
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
                if not self.proxy(po):
                    if po != self.somewhere:
                        self.chosenplaces.append((th,po))
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
            self.gym_of_strt = {}
            self.owner_of_ambigymstrt = {}
            for scv in self.units(SCV):
                scvt = scv.tag
                if self.job_of_scvt[scvt] not in ['mimminer','gasminer','builder']:
                    self.promote(scv,'idler')
                    if scvt in self.goal_of_trabu_scvt:
                        del self.goal_of_trabu_scvt[scvt]
                        del self.structure_of_trabu_scvt[scvt]
            self.vision_of_scvt = {}
            # this changes preps and eggs
            self.get_eggs()
            self.get_preps()  # after get_eggs
            # remake plans
            self.buildseries_exe_from_bagofthings_exe()
            # Keep old places for reuse.
            for (th, po, status) in self.buildorder_exe:
                if not self.proxy(po):
                    if po != self.somewhere:
                        self.chosenplaces.append((th, po))
            self.buildorder_of_buildseries()
            self.buildorder_exe = []
            for (th, pl) in self.buildorder:
                self.buildorder_exe.append((th, pl, 'new'))
        # buildorder_exe is made
        self.but_i_had_structures = i_have_structures
        self.but_i_had_flying = i_have_weak_flying
        #
        self.buildorder = []
        for (th,pl,status) in self.buildorder_exe:
            self.buildorder.append((th,pl))
        self.happy_get_sit()
        if not self.happy_buildorder():
            self.log_success('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
            self.log_success('%%%%%%%%%%%%%%%%%%%%%%%%%%% TO DO %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
            self.log_success('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        self.get_situation()
        self.planning_of_buildorder()
        self.planning_exe = self.planning.copy()

    # *********************************************************************************************************************

    def remove_from_planning_etc(self, thing, place):
        todel = set()
        first = True
        for bp in self.planning_exe:
            (th, sv, pl, sr, sc, fi) = bp
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
                        if place != self.somewhere:
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
                for (martype,bartype,pos,dura,owner) in self.preps:
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
        #  logging
        if len(self.buildorder_exe) > 0:
            stri = ''
            for nr in range(0,min(3,len(self.buildorder_exe))):
                (th, pl, status) = self.buildorder_exe[nr]
                stri = stri + th.name + ' '
            self.log_success('buildorder_exe starts with '+stri)
            for nr in range(0,min(3,len(self.planning_exe))):
                (thing, scvt, place, sr, sc, fi)  = self.planning_exe[nr]
                self.log_success('top 3 planning_exe '+thing.name+' '+str(sr)+' '+str(sc)+' at '+self.txt(place))
        #
        todel = set()
        for bp in self.planning_exe:
            (thing, scvt, place, sr, sc, fi) = bp
            for nr in range(0,len(self.buildorder_exe)):
                (th,pl,status) = self.buildorder_exe[nr]
                if (th == thing) and (status == 'thought'):
                    if (pl == place) or (pl == self.somewhere):
                        if thing in self.all_structures_tobuildwalk:
                            if sr <= 0:
                                if scvt not in self.goal_of_trabu_scvt:
                                    if await self.build_thing_tobuildwalk(scvt,thing, place, 'follow_planning_exe'):
                                        self.buildorder_exe[nr] = (th,place,'prep')
                        elif thing in self.all_pfoc + self.all_labs:
                            if sr <= 0:
                                inuse = False
                                for abar in self.structures:
                                    if self.position_of_building(abar) == place:
                                        if abar.tag in (self.ambition_of_strt.keys() | self.gym_of_strt.keys()):
                                            inuse = True
                                if not inuse:
                                    if await self.build_thing(thing, place, 'follow_planning_exe'):
                                        self.buildorder_exe[nr] = (th, place, 'prep')
                        else: # upgr, army
                            if sr <= 0:
                                inuse = False
                                for abar in self.structures:
                                    if self.position_of_building(abar) == place:
                                        if abar.tag in (self.ambition_of_strt.keys() | self.gym_of_strt.keys()):
                                            inuse = True
                                if not inuse:
                                    if await self.build_thing(thing, place, 'follow_planning_exe'):
                                        self.buildorder_exe[nr] = (th, place, 'prep')

    def addthrowspots(self, th, po, sta, ow, pri):
        # technic; append respecting unique (th,po), respect unthinkable.
        # also write_layout
        seen = False
        for (thing, pos, status, owner, priority) in self.throwspots:
            if (thing == th) and (pos == po):
                seen = True
        if (th,po) in self.unthinkable:
            seen = True
        if not seen:
            self.throwspots.append((th, po, sta, ow, pri))
            if th in self.all_structures_tobuildwalk:
                self.write_layout(th, po)

    def make_unthinkable(self, thing,pos):
        self.unthinkable.add((thing,pos))
        # remove from throwspots and chosenplaces too
        todel = []
        for tps in self.throwspots:
            (th, po, status, ow, pri) = tps
            if (th == thing) and (po == pos):
                todel.append(tps)
        for tps in todel:
            del self.throwspots[self.throwspots.index(tps)]
        todel = []
        for tps in self.chosenplaces:
            (th,po) = tps
            if (th == thing) and (po == pos):
                todel.append(tps)
        for tps in todel:
            del self.chosenplaces[self.chosenplaces.index(tps)]


    def add_thought(self, thing,pos,owner) -> bool:
        self.routine = 'add_thought'
        ok = True
        todel = set()
        if self.we_started_at(thing,pos):
            ok = False
            # only an army thought by the same owner can be multiple
            for (th,po,ow) in self.thoughts:
                if (th == thing) and (pos == po) and (ow == owner):
                    if (th in self.all_army) or (pos == self.somewhere):
                        ok = True
            if not ok:
                self.log_success('Add_thought halted doubling of ' + thing.name + ' at ' + self.txt(pos) + ' (by ' + owner + ')')
                # thought-stealing by 'follow_planning_exe'
                if owner == 'follow_planning_exe':
                    for (th, po, ow) in self.thoughts:
                        if (th == thing) and (pos == po) and (ow != owner):
                            self.log_success('thought stolen')
                            todel.add((th,po,ow))
                            ok = True
                            # remove (th,po,ow) from throwspots
                            todel_ = []
                            for tps in self.throwspots:
                                (th_, po_, status_, ow_, pri_) = tps
                                if (th == th_) and (po == po_) and (ow == ow_):
                                    todel_.append(tps)
                            for tps in todel_:
                                del self.throwspots[self.throwspots.index(tps)]
        if self.we_started_amount(thing) >= self.future_maxam_of_thing(thing):
            ok = False
            self.log_success('Add_thought halted by future maximum a ' + thing.name + ' by ' + owner)
        # no restrictions on e.g. minerals, free cradle, as those can become ok later
        if not self.check_future_techtree(thing):
            ok = False
            self.log_success('Add_thought halted by future techtree a '+thing.name+' by '+owner)
        if thing == REFINERY:
            # This code forbids gas-stealing. Could have to change later.
            expa = self.nowhere
            for ccpos in self.expansion_locations_list:
                if self.near(pos,ccpos,self.miner_bound):
                    expa = ccpos
            if not self.we_started_hall_at(expa):
                ok = False
                self.log_success('Add_thought halted a hallless refinery by '+owner)
        if (thing,pos) in self.unthinkable:
            ok = False
            self.log_success('Add_thought halted unthinkable ' + thing.name +' at ' + self.txt(pos) + ' by ' + owner)
        if ok:
            self.thoughts.append((thing,pos,owner))
            for tpo in todel:
                del self.thoughts[self.thoughts.index(tpo)]
        else:
            # remove this from throwspots and chosenplaces
            todel = []
            for tps in self.throwspots:
                (th, po, status, ow, pri) = tps
                if (th == thing) and (po == pos) and (ow == owner):
                    todel.append(tps)
            for tps in todel:
                del self.throwspots[self.throwspots.index(tps)]
            todel = []
            for tps in self.chosenplaces:
                (th, po) = tps
                if (th == thing) and (po == pos) and ('follow_planning_exe' == owner):
                    todel.append(tps)
            for tps in todel:
                del self.chosenplaces[self.chosenplaces.index(tps)]
        return ok


    def throw_chaos_if_rich(self, thing, owner, priority):
        # thing must be BARRACKS
        # per owner, thing: find or reuse a place, store it in throwspots
        # also write_layout
        self.routine = 'throw_chaos_if_rich'
        self.log_throw(owner + ' throws chaos a ' + thing.name)
        cost = self.get_added_cost(thing)
        gasless = (cost.vespene == 0)
        if self.we_started_amount(thing) < self.maxam_of_thing(thing):
            # trow if money >= eps + bccost + half throwncost
            # half because there is time too, dont be too strict
            used_mim = 450
            used_gas = 350
            for (th,pl,ow) in self.thoughts:
                cost = self.get_added_cost(th)
                used_mim += cost.minerals/2
                used_gas += cost.vespene/2
            for (martype,bartype,pos,dura,ow) in self.preps:
                cost = self.get_added_cost(martype)
                used_mim += cost.minerals/2
                used_gas += cost.vespene/2
            if (self.minerals >= used_mim):
                if (self.vespene >= used_gas) or gasless:
                    self.log_throw('payable')
                    foundplace = False
                    for (th,po,status, ow, pri) in self.throwspots:
                        if (th == thing) and (ow == owner) and (pri == priority):
                            place = po
                            foundplace = True
                    if not foundplace:
                        around = self.random_mappoint()
                        while self.proxy(around):
                            around = self.random_mappoint()
                        place = self.place_around(thing, around)
                        self.addthrowspots(thing,place,'new',owner,priority)
                        self.log_throw('placable')

    def throw_treepayno(self, thing, owner, priority):
        self.routine = 'throw_treepayno'
        if not self.we_started_a(thing):
            if self.check_techtree(thing):
                if self.can_pay(thing):
                    self.throw_somewhere(thing, owner, priority)


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
                foundplace = True
        if not foundplace:
            if thing in self.all_structures_tobuildwalk:
                if self.find_tobuildwalk_a_place(thing):
                    place = self.function_result_Point2
                    if (thing,place) not in self.unthinkable:
                        foundplace = True
            elif thing in self.all_pfoc:
                for cc in self.structures(COMMANDCENTER).ready:
                    if cc.tag not in self.ambition_of_strt:
                        growing = False
                        for (martype,bartype,pos,dura) in self.eggs:
                            if (bartype == COMMANDCENTER) and (pos == cc.position):
                                if martype in self.all_pfoc:
                                    growing = True
                        if not growing:
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
                bar = self.cradle_of_thing(thing) # no standalone lab
                sps = []
                for aba in self.structures(bar).ready:
                    if aba.tag not in self.ambition_of_strt:
                        growing = False
                        for (martype,bartype,pos,dura) in self.eggs:
                            if (bartype == bar) and (pos == aba.position):
                                if martype in self.all_labs:
                                    growing = True
                        if not growing:
                            if not aba.has_add_on:
                                sps.append(aba)
                if len(sps) > 0:
                    sp = random.choice(sps)
                    place = self.position_of_building(sp)
                    if (thing, place) not in self.unthinkable:
                        foundplace = True
            else: # army, upgr
                bar = self.cradle_of_thing(thing)
                needslab = False
                for (thi, need) in self.techtree:
                    if thi == thing:
                        if (need in self.all_labs) and (need != bar):
                            needslab = True
                if needslab:
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
                    place = self.position_of_building(sp)
                    if (thing, place) not in self.unthinkable:
                        foundplace = True
            if foundplace:
                self.addthrowspots(thing,place,'new',owner,priority)
                self.log_throw('placable')


    def throw_if_rich(self,thing,owner,priority):
        # checks thoughts money
        # checks amount
        # finds a place
        # fills throwspots
        # writes layout
        self.routine = 'throw_if_rich'
        self.log_throw(owner + ' throws if rich a ' + thing.name)
        cost = self.get_added_cost(thing)
        gasless = (cost.vespene == 0)
        if self.we_started_amount(thing) < self.maxam_of_thing(thing):
            # trow if money >= eps + bccost + half throwncost
            # half because there is time too, dont be too strict
            used_mim = 450
            used_gas = 350
            for (th,pl,ow) in self.thoughts:
                cost = self.get_added_cost(th)
                used_mim += cost.minerals/2
                used_gas += cost.vespene/2
            for (martype,bartype,pos,dura,ow) in self.preps:
                cost = self.get_added_cost(martype)
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
        cost = self.get_added_cost(thing)
        gasless = (cost.vespene == 0)
        if self.we_started_amount(thing) < self.maxam_of_thing(thing):
            # trow if money >= eps + bccost + half throwncost
            # half because there is time too, dont be too strict
            used_mim = 450
            used_gas = 350
            for (th,pl,ow) in self.thoughts:
                cost = self.get_added_cost(th)
                used_mim += cost.minerals/2
                used_gas += cost.vespene/2
            for (martype,bartype,pos,dura,ow) in self.preps:
                cost = self.get_added_cost(martype)
                used_mim += cost.minerals/2
                used_gas += cost.vespene/2
            if (self.minerals >= used_mim):
                if (self.vespene >= used_gas) or gasless:
                    self.addthrowspots(thing, place, 'new', owner, priority)

    def throw_at_spot(self,thing,place,owner,priority):
        # checks amount
        # fills throwspots
        # writes layout
        self.routine = 'throw_at_spot'
        self.addthrowspots(thing, place, 'new', owner, priority)


    async def throw_advance(self):        
        # push throwspots into thought
        for priority in [1, 2, 3]:
            nr = 0
            while nr < len(self.throwspots): # add_thought can delete a throwspot
                (thing, place, status, ow, pri) = self.throwspots[nr]
                if (status == 'new') and (pri == priority):
                    if self.add_thought(thing, place, ow):
                        self.throwspots[nr] = (thing, place, 'thought', ow, pri)
                nr += 1
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
                        if await self.build_thing(thing, place, ow):
                            todel.append(tpso)
                            self.log_success('thrown ' + thing.name+' for '+ow)
            for tpso in todel:
                del self.throwspots[self.throwspots.index(tpso)]



    def init_expansion_doubles(self):
        self.routine = 'init_expansion_doubles'
        for pos in self.expansion_locations_list:
            control_pos = self.init_cheese_position(pos, 115, COMMANDCENTER)
            if control_pos != self.nowhere:
                self.erase_layout(COMMANDCENTER,control_pos)
                self.add_possible_cc_position(control_pos)


    async def supplydepots_adlib(self):
        self.routine = 'supplydepots_adlib'
        pause = False
        for (th,am,bu,bam) in self.production_pause:
            if th == SUPPLYDEPOT:
                if self.we_finished_amount(bu) < bam:
                    if self.we_started_amount(th) >= am:
                        pause = True
        if not pause:
            if (self.supply_cap < 200):
                wantedmarginsupply = 2 + self.supply_used * self.supply_rate
                wanteddepots = (wantedmarginsupply - self.supply_left) / 8
                satisfied = False
                # buildorder_exe is around frame 5
                if self.frame < 10:
                    satisfied = True
                for (exething,exeplace,status) in self.buildorder_exe:
                    if exething == SUPPLYDEPOT:
                        satisfied = True
                for (th, pl, st, ow, pri) in self.throwspots:
                    if th == SUPPLYDEPOT:
                        satisfied = True
                if not satisfied:
                    npiped = 0
                    for (martype,bartype,pos,dura,owner) in self.preps:
                        if martype == SUPPLYDEPOT:
                            npiped += 1
                    for (martype,bartype,pos,dura) in self.eggs:
                        if martype == SUPPLYDEPOT:
                            npiped += 1
                    if (npiped < wanteddepots):
                        self.throw_somewhere(SUPPLYDEPOT,'supplydepots_adlib',1)

    async def refineries_adlib(self):
        self.routine = 'refineries_adlib'
        pause = False
        for (th,am,bu,bam) in self.production_pause:
            if th == REFINERY:
                if self.we_finished_amount(bu) < bam:
                    if self.we_started_amount(th) >= am:
                        pause = True
        if not pause:
            satisfied = False
            if self.frame < 2700: # 2 minutes
                satisfied = True
            for (exething, exeplace, status) in self.buildorder_exe:
                if exething == REFINERY:
                    satisfied = True
            for (th, pl, st, ow, pri) in self.throwspots:
                if th == REFINERY:
                    satisfied = True
            if not satisfied:
                self.throw_somewhere(REFINERY,'refineries_adlib',2)

    def opening_create_cut(self):
        # stop with opening_create_units when heavy losses
        if self.opening_create_units > 0:
            have = len(self.units(self.opening_create_kind))
            if have > self.opening_create_hadmax:
                self.opening_create_hadmax = have
            if 2 * have + self.opening_create_units < 2 * self.opening_create_hadmax:
                self.opening_create_units = 0

    async def upgrades_adlib(self):
        self.routine = 'upgrades_adlib'
        if self.opening_create_units <= 0:
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
            # second armory
            bcs = len(self.units(BATTLECRUISER))
            if (bcs >= 4) and (self.we_started_amount(ARMORY) < 2):
                self.throw_if_rich(ARMORY, 'upgrades_adlib', 2)
            # second engineeringbay
            mars = len(self.units(MARINE)) + len(self.units(MARAUDER))
            if (mars >= 12) and (self.we_started_amount(ENGINEERINGBAY) < 2):
                self.throw_if_rich(ENGINEERINGBAY, 'upgrades_adlib', 2)


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
                            for (th,scv,pos,dura) in self.eggs:
                                if th == bui_type:
                                    bui_started = True
                            if not bui_started:
                                self.throw_if_rich(bui_type, 'armybuildings_adlib', 2)


    def army_adlib(self):
        self.routine = 'army_adlib'
        # monobattle openings
        if self.opening_create_units > 0:
            mim_tospend = self.minerals
            gas_tospend = self.vespene
            mar_todo = self.opening_create_units
            mar_cost = self.get_added_cost(self.opening_create_kind)
            avoid_pos = set()
            # protect the possible buildorder_exe tail
            for (item, goal, status) in self.buildorder_exe:
                avoid_pos.add(goal)
                basekind = self.basekind_of(item)
                cost = self.get_added_cost(basekind)
                mim_tospend -= cost.minerals
                gas_tospend -= cost.vespene
            # already in the pipeline:
            for tps in self.throwspots:
                (th, po, status, ow, pri) = tps
                avoid_pos.add(po)
                if th == self.opening_create_kind:
                    mar_todo -= 1
                    mim_tospend -= mar_cost.minerals
                    gas_tospend -= mar_cost.vespene
            for (martype, bartype, pos, dura, owner) in self.preps:
                avoid_pos.add(pos)
                if martype == self.opening_create_kind:
                    mar_todo -= 1
                    mim_tospend -= mar_cost.minerals
                    gas_tospend -= mar_cost.vespene
            # go make new ones
            for bar in self.structures(BARRACKS).idle:
                if bar.position not in avoid_pos:
                    if (mim_tospend >= mar_cost.minerals) and (gas_tospend >= mar_cost.vespene):
                        if mar_todo > 0:
                            self.throw_at_spot(self.opening_create_kind, bar.position, 'army_adlib', 1)
                            mar_todo -= 1
                            mim_tospend -= mar_cost.minerals
                            gas_tospend -= mar_cost.vespene
        else: # after opening
            vikings = 0
            for ene in self.enemy_units:
                if (ene.type_id in self.viking_targets) and (ene.type_id != OVERLORD):
                    vikings += 1.5
            if (self.army_supply < self.good_army_supply) or (self.minerals > 800):  # army
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
        if self.opening_create_units <= 0:
            if (self.army_supply >= self.good_army_supply) or (self.minerals > 600):
                if self.count_of_job['idler'] + self.count_of_job['volunteer'] > 5:
                    self.throw_if_rich(COMMANDCENTER,'expansion_advisor',1)
                else:
                    for cc in self.structures(COMMANDCENTER):
                        if cc.position in self.cc_destiny:
                            if self.cc_destiny[cc.position] == 'pf':
                                self.throw_if_rich(PLANETARYFORTRESS, 'expansion_advisor', 2)
                            else:
                                self.throw_if_rich(ORBITALCOMMAND, 'expansion_advisor', 1)
                    self.throw_if_rich(COMMANDCENTER, 'expansion_advisor', 1)


    def turrets_adlib(self):
        # get rid of surplus money
        self.routine = 'turrets_adlib'
        ccs = self.we_started_amount(COMMANDCENTER) + self.structures(PLANETARYFORTRESS).amount \
              + self.structures(ORBITALCOMMAND).amount
        mts = self.structures(MISSILETURRET).amount
        if self.opening_create_units <= 0:
            if self.we_finished_a(ENGINEERINGBAY):
                if (mts < ccs * 8) and (self.minerals > 650):
                    self.throw_if_rich(MISSILETURRET,'turrets_adlib',2)

    def extreme_spender(self):
        self.routine = 'extreme_spender'
        if (self.minerals > 1500) and (self.vespene > 750) and (self.supply_used > 170):
            # try to control open area
            gotone = False
            # first try cc to pf
            for cc in self.structures(COMMANDCENTER):
                if not gotone:
                    gotone = True
                    self.throw_at_spot(PLANETARYFORTRESS, cc.position, 'extreme_spender', 2)
            # else try new cc
            for pos in self.expansion_locations_list:
                if self.check_layout(COMMANDCENTER, pos):
                    if not gotone:
                        gotone = True
                        self.throw_at_spot(COMMANDCENTER, pos, 'extreme_spender', 2)
            # else try new cc at odd position
            for pos in self.possible_cc_positions:
                if self.check_layout(COMMANDCENTER, pos):
                    if not gotone:
                        gotone = True
                        self.throw_at_spot(COMMANDCENTER, pos, 'extreme_spender', 2)

    #*********************************************************************************************************************

    def fix_somewhere(beautiful_thing) -> bool:
        # Choose a specific cradle. The choice was delayed with 'somewhere'.
        # beautiful_thing is labs, pfoc, upgr, or army.
        # calculates self.fixed_somewhere
        beautiful_cradle = self.cradle_of_thing(beautiful_thing)
        # needslab ?/n/y
        needslab = '?'
        if beautiful_thing in self.all_labs + self.all_pfoc:
            needslab = 'n'
        for pair in self.techtree:
            if pair[0] == beautiful_thing:
                if (pair[1] in self.all_labs) and (pair[1] != beautiful_cradle):
                    needslab = 'y'
        cradles = set()
        # finished cradles
        for (thing,cradle_place) in self.birds:
            if thing == beautiful_cradle:
                cradle_dura = 0
                # cradle has finished lab
                haslab = 'n'
                for (otherthing,otherplace) in self.birds:
                    if (otherplace == cradle_place) and (otherthing != thing):
                        if (otherthing in self.all_labs + self.all_pfoc):
                            haslab = 'y'
                # cradle has unfinished lab
                for (otherthing, bartype, otherplace, dura) in self.eggs:
                    if (otherplace == cradle_place) and (otherthing != thing):
                        if (otherthing in self.all_labs + self.all_pfoc):
                            haslab = 'y'
                            cradle_dura = dura
                # cradle is in use
                for (otherthing, bartype, otherplace, dura) in self.eggs:
                    if (bartype == beautiful_cradle) and (otherplace == cradle_place):
                        cradle_dura = dura
                # cradle is reserved
                free = True
                for (martype,bartype,pos,dura,owner) in self.preps:
                    if (bartype == beautiful_cradle) and (pos == cradle_place):
                        free = False
                if free:
                    if (needslab == '?') or (needslab == haslab):
                        exception = ((beautiful_thing, cradle_place) in self.unthinkable)
                        if not exception:
                            cradles.add((cradle_place, cradle_dura))
        # unfinished cradles
        for (cradle_thing,dummy,cradle_place,cradle_dura) in self.eggs:
            if cradle_thing == beautiful_cradle:
                # cradle has finished lab
                haslab = 'n'
                for (otherthing,otherplace) in self.birds:
                    if (otherplace == cradle_place) and (otherthing != cradle_thing):
                        if (otherthing in self.all_labs + self.all_pfoc):
                            haslab = 'y'
                # cradle is reserved
                free = True
                for (martype,bartype,pos,dura,owner) in self.preps:
                    if (bartype == cradle_thing) and (pos == cradle_place):
                        free = False
                if free:
                    if (needslab == '?') or (needslab == haslab):
                        exception = ((beautiful_thing, cradle_place) in self.unthinkable)
                        if not exception:
                            cradles.add((cradle_place, cradle_dura))
        # check
        if len(cradles) == 0:
            canfix = False
        else:
            canfix = True
            # get earliest
            bestdura = 99999
            bestplace = self.nowhere
            for (place,dura) in cradles:
                if dura < bestdura:
                    bestdura = dura
                    bestplace = place
            self.fixed_somewhere = bestplace
        return canfix



    def may_egg_now(self, thing,goal) -> bool:
        md = True
        if len(self.buildorder_exe) > 0:
            (bu, go, status) = self.buildorder_exe[0]
            matched = False
            for (martype,bartype,pos,dura,owner) in self.preps:
                if (martype == thing) and (pos == goal):
                    matched = True
                    if owner == 'follow_planning_exe':
                        if (thing,goal) == (bu,go):
                            self.buildorderdelay = 0
                        else:
                            md = False
                            self.log_success('Delay of creating a '+thing.name+' because of buildorder_exe, after '+bu.name)
                            if self.can_pay(bu):
                                if self.check_techtree(bu):
                                    cradle_type = self.cradle_of_thing(bu)
                                    for cra in self.structures(cradle_type).ready:
                                        if self.position_of_building(cra) == go:
                                            # what are we waiting for?
                                            self.buildorderdelay += self.chosen_game_step
            if not matched:
                md = False
                self.log_success('Delay of creating a '+thing.name+' because it is not prepaired.')
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
                    pos = self.position_of_building(abar)
            if (martype,pos) == (thing,goal):
                found = True
                todel.add(strt)
        for strt in todel:
            del self.ambition_of_strt[strt]
        # delete it from gym
        todel = set()
        for strt in self.gym_of_strt:
            martype = self.gym_of_strt[strt]
            for abar in self.structures:
                if abar.tag == strt:
                    pos = self.position_of_building(abar)
            if (martype,pos) == (thing,goal):
                found = True
                todel.add(strt)
        for strt in todel:
            del self.gym_of_strt[strt]
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
            elif thing == REFINERY:
                # no refinery before its commandcenter
                expa = self.nowhere
                for ccpos in self.expansion_locations_list:
                    if self.near(place, ccpos, self.miner_bound):
                        expa = ccpos
                canbuild = False
                for (th,po) in self.birds:
                    if (po == expa) and (th in [COMMANDCENTER,ORBITALCOMMAND,PLANETARYFORTRESS]):
                        canbuild = True
                if expa in self.goal_of_trabu_scvt.values():
                    canbuild = True
                if canbuild:
                    didit = await self.build_building(scvt,thing,place,owner)
                else: # can not build
                    seen = False
                    for (th, po, ow) in self.thoughts:
                        if (th == COMMANDCENTER) and (po == expa):
                            seen = True
                    if not seen:
                        # remove from thoughts and throwspots
                        self.thoughts.remove((thing,place,owner))
                        todel = set()
                        for tps in self.throwspots:
                            (th, po, status, ow, pri) = tps
                            if (th == thing) and (po == place):
                                todel.add(tps)
                        for tps in todel:
                            del self.throwspots[self.throwspots.index(tps)]
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
        # give the command some frames to reach is_constructing; call not every gamestep
        self.routine = 'do_buildandretry'
        todel = set()
        for items in self.buildandretry:
            (scvt, building, goal, startframe) = items
            if (self.frame<startframe+self.patience):
                if (scvt in self.all_scvt):
                    for scv in self.units(SCV):
                        if scv.tag == scvt:
                            if self.job_of_scvt[scvt] == 'fencer':
                                #
                                is_building_it = False
                                if scv.is_constructing_scv:
                                    for order in scv.orders:
                                        if type(order.target) == int:
                                            if building == REFINERY:
                                                if order.ability.id == AbilityId.TERRANBUILD_REFINERY:
                                                    is_building_it = True
                                        else:
                                            if (order.target.x == goal.x) and (order.target.y == goal.y): # fails as one condition
                                                is_building_it = True
                                #
                                if is_building_it:
                                    self.promote(scv,'builder')
                                    todel.add(items)
                                else:
                                    # there we go (or go again)
                                    if building == REFINERY:
                                        for gey in self.vespene_geyser:
                                            if gey.position == goal:
                                                self.log_command('scv.build_gas(gey)')
                                                if scv.build_gas(gey):
                                                    self.log_success('succeeded prep to egg ' + building.name)
                                                    self.log_workers('begun     ' + building.name + ' ' + self.name(scvt))
                                    else:
                                        self.log_command('scv.build(' + building.name + ',goal)')
                                        if scv.build(building, goal):
                                            self.log_success('succeeded prep to egg ' + building.name)
                                            self.log_workers('begun     ' + building.name + ' ' + self.name(scvt))
            else: # failed to build
                todel.add(items)
                for scv in self.units(SCV):
                    if scv.tag == scvt:
                        self.promote(scv, 'idler')
                        self.log_success('In buildandretry we discarded a ' + building.name)
        self.buildandretry -= todel
        for (scvt, building, goal, startframe) in todel:
            cost = self.get_added_cost(building)
            self.purse -= cost


    async def do_trainandretry(self):
        # all is ready to start training a pfoc or lab. But sometimes the lab command fails.
        self.routine = 'do_trainandretry'
        todel = set()
        for items in self.trainandretry:
            (oldbuildingtag, newbuilding, startframe) = items
            if (self.frame<startframe+self.patience):
                for oldbuilding in self.structures:
                    if oldbuilding.tag == oldbuildingtag:
                        if oldbuildingtag in self.idle_structure_tags:
                            # there we go (or go again)
                            self.log_command(oldbuilding.name + '.train(' + newbuilding.name + ')')
                            if oldbuilding.train(newbuilding):
                                self.log_success('succeeded prep to egg ' + newbuilding.name)
                        else: # oldbuilding is busy
                            todel.add(items)
            else:
                todel.add(items)
                self.log_success('In trainandretry we discarded a ' + newbuilding.name)
        self.trainandretry -= todel
        for (oldbuildingtag, newbuilding, startframe) in todel:
            cost = self.get_added_cost(newbuilding)
            self.purse -= cost
            if oldbuildingtag in self.ambition_of_strt: # it could e.g. be killed
                del self.ambition_of_strt[oldbuildingtag]

    async def start_construction(self):
        # max 1 per frame to protect can_pay
        self.routine = 'start_construction'
        for scvt in self.goal_of_trabu_scvt:
            if self.job_of_scvt[scvt] == 'traveller':
                goal = self.goal_of_trabu_scvt[scvt]
                for scv in self.units(SCV):
                    if scv.tag == scvt:
                        # unburrow widowines
                        if self.near(scv.position, goal, 20):
                            for wm in self.units(WIDOWMINEBURROWED):
                                if self.near(wm.position,goal,3):
                                    self.log_command('wm(AbilityId.BURROWUP_WIDOWMINE)')
                                    wm(AbilityId.BURROWUP_WIDOWMINE)
                                    self.goal_of_unittag[wm.tag] = wm.position.towards(self.loved_pos,4)
                        # settling
                        if self.near(scv.position, goal, 3):
                            self.log_success('build site reached')
                            self.promote(scv,'settler')
        for scvt in self.goal_of_trabu_scvt:
            if self.job_of_scvt[scvt] == 'settler':
                goal = self.goal_of_trabu_scvt[scvt]
                building = self.structure_of_trabu_scvt[scvt]
                self.log_success('trying prep to egg '+building.name)
                if self.check_techtree(building):
                    if self.can_pay(building):
                        if self.may_egg_now(building, goal):
                            for scv in self.units(SCV):
                                if scv.tag == scvt:
                                    if self.near(scv.position,goal,3):
                                        self.promote(scv,'fencer')
                                        self.log_workers('fencing '+building.name+' '+self.name(scvt))
                                        cost = self.get_added_cost(building)
                                        self.purse += cost
                                        self.buildandretry.add((scv.tag, building, goal, self.frame))
                                    else:
                                        self.log_success('not near')
                                        # try back-to-track
                                        if len(scv.orders) == 0:
                                            scv.move(goal)
                        else:
                            self.log_success('not now')
                    else:
                        self.log_success('no pay')
                else:
                    self.log_success('no techtree')
        # also, realize an ambition: pfoc, labs
        for oldbuilding in self.structures.ready:
             if oldbuilding.tag in self.idle_structure_tags:  # not in eggs
                if oldbuilding.tag in self.ambition_of_strt: 
                    newbuilding = self.ambition_of_strt[oldbuilding.tag]
                    self.log_success('trying prep to egg '+newbuilding.name)
                    if self.check_techtree(newbuilding):
                        if self.can_pay(newbuilding):
                            if self.supply_check(newbuilding):
                                pos = self.position_of_building(oldbuilding)
                                if self.may_egg_now(newbuilding,pos):
                                    inretry = False
                                    for (obt,bui,fra) in self.trainandretry:
                                        if bui == newbuilding:
                                            inretry = True
                                    if not inretry:
                                        cost = self.get_added_cost(newbuilding)
                                        self.purse += cost
                                        self.trainandretry.add((oldbuilding.tag, newbuilding, self.frame))
                                else:
                                    self.log_success('not now')
                            else:
                                self.log_success('no supply')
                        else:
                            self.log_success('no pay')
                    else:
                        self.log_success('no techtree')
        # also, realize a gym: upgr, army
        for building in self.structures.ready:
             if building.tag in self.idle_structure_tags:  # not in eggs
                if building.tag in self.gym_of_strt:
                    trainee = self.gym_of_strt[building.tag]
                    if self.check_techtree(trainee):
                        if self.can_pay(trainee):
                            if self.supply_check(trainee):
                                pos = self.position_of_building(building)
                                if self.may_egg_now(trainee,pos):
                                    del self.gym_of_strt[building.tag]
                                    self.log_success('succeeded prep to egg '+trainee.name)
                                    if type(trainee) == UpgradeId:
                                        await self.do_upgrade(trainee,pos)
                                    else:
                                        self.log_command(building.name+'.train('+trainee.name+')')
                                        building.train(trainee)
                                else:
                                    self.log_success('not now')
                            else:
                                self.log_success('no supply')
                        else:
                            self.log_success('no pay')
                    else:
                        self.log_success('no techtree')


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
                    # add to preps for restcode in this step
                    restdura = self.walk_duration(scv.position,goal)
                    self.preps.add((building, scv, goal, restdura, owner))
        return didit



    async def build_commandcenter(self,trabu_scvt,goal,owner) -> bool:
        self.routine = 'build_commandcenter'
        didit = False
        building = COMMANDCENTER
#       you do not have to wait for minerals and techtree
        if self.frame >= 2000:
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
                # add to preps for restcode in this step
                restdura = self.walk_duration(scv.position, goal)
                self.preps.add((building, scv, goal, restdura, owner))
        didit = True
        # give the cc a cc_destiny
        if goal in self.expansion_locations_list:
            if self.cc_destiny_rush:
                self.cc_destiny[goal] = 'oc'
            else:
                if self.sdist(goal,self.loved_pos) < self.sdist(goal, self.enemy_pos):
                    if self.random_chance(3):
                        self.cc_destiny[goal] = 'pf'
                    else:
                        self.cc_destiny[goal] = 'oc'
                else:
                    if self.random_chance(3):
                        self.cc_destiny[goal] = 'oc'
                    else:
                        self.cc_destiny[goal] = 'pf'
        else: # secondary location
            self.cc_destiny[goal] = 'pf'
        return didit


    def delthought(self, trainee, place, owner):
        if (trainee, place, owner) in self.thoughts:
            del self.thoughts[self.thoughts.index((trainee, place, owner))]
        else:
            del self.thoughts[self.thoughts.index((trainee, self.somewhere, owner))]

    def disappeared_building(self, goneplace):
        # thoughts
        todel = []
        for tpo in self.thoughts:
            (trainee, place, owner) = tpo
            if place == goneplace:
                todel.append(tpo)
        for tpo in todel:
            del self.thoughts[self.thoughts.index(tpo)]
        # throwspots
        todel = []
        for tps in self.throwspots:
            (th, po, status, ow, pri) = tps
            if po == goneplace:
                todel.append(tps)
        for tps in todel:
            del self.throwspots[self.throwspots.index(tps)]


    async def build_thing(self,ambition,place,owner) -> bool:
        # labs, pfoc, upgr, army
        # puts a building in ambition_of_strt, then it will become idle, then be transformed
        # or in gym_of_strt, when it is idle it will start training that army or upgrade
        # all checks except cradleidle
        # fixes place==somewhere. This is sometimes done in planning.
        self.routine = 'build_thing'
        self.log_success('trying to prep '+ambition.name)
        didit = False
        fixplace = place
        if place == self.somewhere:
            if self.fix_somewhere(ambition):
                fixplace = self.fixed_somewhere
            else:
                fixplace = self.nowhere
        cradle_type = self.cradle_of_thing(ambition)
        if ambition in self.all_pfoc + self.all_labs:
            if ((ambition,place,owner) in self.thoughts) or ((ambition,self.somewhere,owner) in self.thoughts):
                if self.check_techtree(ambition):
                    if self.can_pay(ambition):
                        for cc in self.structures(cradle_type).ready:
                            if self.position_of_building(cc) == fixplace:
                                if cc.tag not in self.ambition_of_strt:
                                    if cc.tag not in self.gym_of_strt:
                                        if self.supply_check(ambition):
                                            if (ambition in self.all_labs):
                                                if not cc.has_add_on:
                                                    self.ambition_of_strt[cc.tag] = ambition
                                                    self.owner_of_ambigymstrt[cc.tag] = owner
                                                    didit = True
                                            else: # pfoc
                                                self.ambition_of_strt[cc.tag] = ambition
                                                self.owner_of_ambigymstrt[cc.tag] = owner
                                                didit = True
            else: # not in thoughts
                self.log_success('BUG trying to build '+ambition.name+' by '+owner+' but it is not in thoughts.')
                self.log_thoughts()
            if didit:
                if (ambition,place,owner) in self.thoughts:
                    del self.thoughts[self.thoughts.index((ambition,place,owner))]
                else:
                    del self.thoughts[self.thoughts.index((ambition,self.somewhere,owner))]
                self.log_success('thought to prep ' + ambition.name)
        else: # army, upgr
            trainee = ambition
            if ((trainee, place, owner) in self.thoughts) or ((trainee, self.somewhere, owner) in self.thoughts):
                if self.check_techtree(trainee):
                    if self.can_pay(trainee):
                        seen = False
                        for cc in self.structures(cradle_type):
                            if self.position_of_building(cc) == fixplace:
                                seen = True
                                if cc in self.structures(cradle_type).ready:
                                    if (trainee, cradle_type) in self.cradle:  # against flying
                                        if cc.tag not in self.ambition_of_strt:
                                            if cc.tag not in self.gym_of_strt:
                                                if self.supply_check(trainee):
                                                    self.gym_of_strt[cc.tag] = trainee
                                                    self.owner_of_ambigymstrt[cc.tag] = owner
                                                    didit = True
                                                    # a bit overdone but I want to put it in preps
                                                    dura = 1
                                                    self.preps.add((trainee, cradle_type, fixplace, dura, owner))
                                                    if self.opening_create_kind == trainee:
                                                        self.log_success('Ha onother ' + trainee.name + '!')
                                                        self.opening_create_units -= 1
                        if not seen:
                            self.log_success('That building is gone')
                            self.disappeared_building(place)
            else:  # not in thoughts
                self.log_success('BUG trying to train ' + trainee.name + ' by ' + owner + ' but it is not in thoughts.')
                self.log_thoughts()
            if didit:
                if (trainee, place, owner) in self.thoughts:
                    self.delthought(trainee, place, owner)
                else:
                    self.delthought(trainee, self.somewhere, owner)
                self.log_success('thought to prep '+ambition.name)
        return didit


    async def do_upgrade(self,upg,place) -> bool:
        self.routine = 'do_upgrade'
        didit = False
        if type(upg) == UpgradeId:
            if self.already_pending_upgrade(upg) == 0:
                if self.check_techtree(upg):
                    cra = self.cradle_of_thing(upg)
                    for ar in self.structures(cra).ready:
                        if (self.position_of_building(ar) == place):
                            if (ar.tag in self.idle_structure_tags):
                                if self.can_pay(upg) or self.bug_can_pay(upg):
                                    if not didit:
                                        didit = True
                                        self.log_success(upg.name)
                                        # circumvent some bugs
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

    def kill_a_base(self, pos):
        # put a bunker near very weak bases
        around = pos.towards(self.game_info.map_center, -7)
        place = self.place_around(BUNKER, around)
        self.throw_at_spot(BUNKER,place,'kill_a_base',1)


    def init_vulture(self):
        # needs target_loc
        self.vulture_pos = []
        self.make_circle(344) # 344
        for point in self.circle:
            self.vulture_pos.append(Point2((self.target_loc.x + 7 * point.x, self.target_loc.y + 7 * point.y)))

    def vulture(self):
        # needs init_vulture
        self.vulture_pole = (self.vulture_pole + self.chosen_game_step) % len(self.vulture_pos)
        goal = self.vulture_pos[self.vulture_pole]
        for bc in self.units(BATTLECRUISER):
            # gamestate gives emotion_of_unittag
            if self.emotion_of_unittag[bc.tag] == 'vulturing':
                # high APM command not logged
                bc.move(goal)

    def get_goal(self) -> Point2:
        allloc = []
        for ene in self.enemy_structures.ready:
            if ene.type_id in self.hall_types:
                allloc.append(ene.position)
        if len(allloc) == 0:
            for ene in self.enemy_structures:
                allloc.append(ene.position)
        if len(allloc) == 0:
            goal = self.enemy_pos
        else:
            goal = random.choice(allloc)
        return goal


    def marine_fun(self):
        self.routine = 'marine_fun'
        if self.opening_name == 'marine':
            # stimpack when there is gas
            self.throw_treepayno(BARRACKSTECHLAB, 'marine_fun', 2)
            self.throw_treepayno(STIMPACK, 'marine_fun', 2)
            # transition
            #if (self.minerals > self.opening_create_units * 50):
            #    self.throw_treepayno(FACTORY, 'marine_fun', 2)
            #    self.throw_treepayno(STARPORT, 'marine_fun', 2)
            #    self.throw_treepayno(FUSIONCORE, 'marine_fun', 2)
            #    if self.we_started_amount(COMMANDCENTER) < self.marine_opening_bases + 1:
            #        if self.can_pay(COMMANDCENTER):
            #            self.throw_somewhere(COMMANDCENTER, 'marine_fun', 3)
            # start the attack
            if (self.opening_create_units <= 0):
                if not self.marine_attacked:
                    self.marine_attacked = True
                    self.marine_attackframe = self.frame
                    # find an army gather point
                    self.marine_goal = self.loved_pos
                    while not self.near(self.marine_goal, self.game_info.map_center, 15):
                        around = self.random_mappoint()
                        self.marine_goal = self.place_around(ARMORY,around)
                    for mar in self.units(MARINE):
                        self.special_tags.add(mar.tag)
                        mar.attack(self.marine_goal)
                    # try agressive bunkers
                    for hall_type in self.hall_types:
                        for stru in self.enemy_structures(hall_type):
                            self.kill_a_base(stru.position)
            # 20 sec of new marines are sent in too
            if self.frame % 17 == 16:
                if self.frame < self.marine_attackframe + 22.4 * 18: # builddura of marine
                    for mar in self.units(MARINE):
                        if mar.tag not in self.special_tags:
                            mar.attack(self.marine_goal)
                            self.special_tags.add(mar.tag)
            # idle marines are sent to work
            for mar in self.units(MARINE).idle:
                if mar.tag in self.special_tags:
                    if not self.near(mar.position, self.marine_goal, 5):
                        mar.attack(self.marine_goal)
            # set a new goal
            if self.frame % 37 == 36:
                reached = 0
                total = 0
                for mar in self.units(MARINE):
                    if mar.tag in self.special_tags:
                        total += 1
                        if self.near(mar.position,self.marine_goal,5):
                            reached += 1
                if reached * 4 > 3 * total:
                    self.marine_goal = self.get_goal()
                    for mar in self.units(MARINE):
                        if mar.tag in self.special_tags:
                            mar.attack(self.marine_goal)
            # fly the barracks in
            if self.marine_attacked:
                for bar in self.structures(BARRACKS).idle:
                    if bar.tag not in self.flown_in:
                        self.flown_in.add(bar.tag)
                        newplace = self.place_around(ARMORY,self.enemy_pos)
                        self.goal_of_flying_struct[bar.tag] = newplace
                        self.write_layout(ARMORY,newplace)
                        self.landings_of_flying_struct[bar.tag] = 0
                        self.log_success('up BARRACKS')
                        self.log_command('bar(AbilityId.LIFT')
                        bar(AbilityId.LIFT)



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
        close = self.near(bc.position,goal,25)
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
            self.shame_of_unittag[tag] += self.chosen_game_step
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
        # min nearity 0.001
        nomo = False
        tag = bc.tag
        goal = self.goal_of_unittag[tag]
        sd = self.sdist(bc.position, goal)
        if sd < nearity*nearity:
            nomo = True
        elif sd < self.last_sd_of_unittag[tag]:
            self.shame_of_unittag[tag] = max(0, self.shame_of_unittag[tag] - 1)
        elif self.shame_of_unittag[tag] < maxshame:
            self.shame_of_unittag[tag] += self.chosen_game_step
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


    def get_last_enemies(self):
        # collect positions for next step
        # also write layout
        self.last_enemies = set()
        for ene in self.enemy_units:
            self.last_enemies.add((ene.tag,ene.position))
        for ene in self.enemy_structures:
            self.last_enemies.add((ene.tag,ene.position))
            if not ene.is_flying:
                self.write_layout(ene.type_id,ene.position)
                

    def get_last_health(self):
        # collect health for next step
        for ene in self.units:
            self.last_health[ene.tag] = ene.health
        for ene in self.structures:
            self.last_health[ene.tag] = ene.health
            
    def get_trail(self):
        # per unit the trail of its last 10 seconds positions 
        if self.frame % 24 == 12:
            trailnr = (self.frame // 24) % 10
            for unt in self.units:
                if unt.type_id != SCV:
                    if unt.tag in self.trail:
                        self.trail[unt.tag][trailnr] = unt.position
                    else:
                        self.trail[unt.tag] = [self.nowhere,self.nowhere,self.nowhere,self.nowhere,self.nowhere
                                             ,self.nowhere,self.nowhere,self.nowhere,self.nowhere,self.nowhere]

    def close_to_a_my_base(self,pos) -> bool:
        clos = False
        for tow in self.all_bases:
            clos = clos or self.near(tow.position,pos,20)
        return clos

    def locally_improved(self,place) -> Point2:
        # verhoog quality met 900 pogingen in de omgeving (maxdist 8)
        bestplace = place
        qual = self.quality_of_bc_position(place)
        for nx in range(-16,16):
            for ny in range(-16,16):
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
            if self.near(point,self.enemy_pos,110) and (not self.near(point,self.enemy_pos,90)):
                qual = 100
        elif self.attack_type == 'jumpy':
            #           bc.radius+bc.ground_range+hatchery.radius  estimate
            if self.near(point,self.target_loc,10):
                qual = 100
                for ene in self.enemy_structures:
                    if ene.type_id in self.antiair_detector:
                        if self.near(point,ene.position,11.5):
                            qual -= 10
                # bonus for a geyser in sight
                for gas in self.vespene_geyser:
                    if self.near(point,gas.position,7):
                        qual += 1
        return qual

    async def repair_bc(self):
        for bc in self.units(BATTLECRUISER):
            bct = bc.tag
            if self.emotion_of_unittag[bct] != 'recovering':
                torep = (self.emotion_of_unittag[bct] not in ['frozen','vulturing']) and (bc.health <= self.bc_fear)
                torep = torep or (bc.health < 100)
                if torep:
                    self.emotion_of_unittag[bct] = 'recovering'
                    await self.go_jumpormove(bc,self.shipyard)
                    self.bc_fear = max(150, self.bc_fear - 10)
            if self.emotion_of_unittag[bct] == 'recovering':
                # this emotion is partly a movement
                if self.no_move(bc,64):
                    # it should be repaired. Found anomality, thus next code
                    close = self.near(bc.position, self.shipyard, 15)
                    if not close:
                        await self.go_jumpormove(bc,self.shipyard)
                # keep the bc in the shipyard. Who is pulling it away?
                if self.near(bc.position,self.shipyard,12) and not self.near(bc.position,self.shipyard,2):
                    self.log_command('bc(AbilityId.MOVE_MOVE,self.shipyard)')
                    bc(AbilityId.MOVE_MOVE,self.shipyard)



    async def attack_with_bc(self):
        self.routine = 'attack_with_bc'
        if self.attack_type == 'jumpy':
            for bc in self.units(BATTLECRUISER):
                bct = bc.tag
                expo = self.expo_of_pos(bc.position)
                eneseen = False
                for ene in self.enemy_units_of_expo[expo]:
                    # todo not cloacked. Warning: is_visible means something else.
                    if self.near(ene.position, bc.position, 7):
                        eneseen = True
                for ene in self.enemy_structures_of_expo[expo]:
                    if self.near(ene.position, bc.position, 7):
                        eneseen = True
                antiairseen = False
                for ene in self.enemy_structures_of_expo[expo]:
                    if ene.type_id in self.antiair_detector:
                        antiairseen = True
                emotion = self.emotion_of_unittag[bct]
                # handle diverse possibilities
                if emotion == 'recovering':
                    pass # it will be repaired
                elif emotion == 'lazy':
                    qual = 0
                    while qual <= 50:
                        place = self.random_mappoint()
                        qual = self.quality_of_bc_position(place)
                    place = self.locally_improved(place)
                    await self.go_jumpormove(bc,place)
                    self.emotion_of_unittag[bct] = 'travels'
                elif emotion == 'travels':
                    # wait for the jump animation to finish, after that its position changes, and its vision returns
                    # or wait until it has flown ower.
                    if self.no_move_or_near(bc,100,1):
                        handable = True
                        for order in bc.orders:
                            if order.ability.id == AbilityId.EFFECT_TACTICALJUMP:
                                handable = False
                        if handable:
                            self.emotion_of_unittag[bct] = 'finetuning'
                            goal = self.locally_improved(bc.position)
                            self.go_move(bc,goal)
                            self.log_army('bc arrived, moving it a bit')
                elif emotion == 'finetuning':
                    if self.no_move(bc,64):
                        if antiairseen:
                            self.log_army('freezing bc there')
                            self.log_command('bc(AbilityId.HOLDPOSITION_BATTLECRUISER)')
                            bc(AbilityId.HOLDPOSITION_BATTLECRUISER)
                            self.emotion_of_unittag[bct] = 'frozen'
                        else:
                            self.log_army('vulturing')
                            self.emotion_of_unittag[bct] = 'vulturing'
                elif emotion == 'vulturing':
                    if (not eneseen) or (antiairseen):
                        self.log_army('stop vulture')
                        self.emotion_of_unittag[bct] = 'towander'
                elif emotion == 'frozen':
                    if (not eneseen):
                        self.log_army('unfreezing bc')
                        self.log_command('bc(AbilityId.STOP)')
                        bc(AbilityId.STOP)
                        self.emotion_of_unittag[bct] = 'towander'
                elif emotion == 'towander':
                    place = self.random_mappoint()
                    self.go_attack(bc,place)
                    self.emotion_of_unittag[bct] = 'wandering'
                elif emotion == 'wandering':
                    if self.no_move(bc,64):
                        self.emotion_of_unittag[bct] = 'towander'
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
            tp = self.target_loc
        elif self.attack_type == 'center':
            tp = self.army_center_point
        elif self.attack_type == 'centerpoint':
            tp = self.target_loc
        if (self.attack_type not in ['jumpy','arc']):
            for bc in self.units(BATTLECRUISER).idle:
                if self.emotion_of_unittag[bc.tag] != 'recovering':
                    if self.quality_of_bc_position(bc.position) <= 50:
                        self.log_command('bc.attack(tp)')
                        bc.attack(tp)
        #
        #       attack_type changes
        it_changed = False
        if self.attack_type == 'jumpy':
            frozen_or_wandering = 0
            for bct in self.emotion_of_unittag:
                if self.emotion_of_unittag[bct] in ['frozen','vulturing','wandering']:
                    frozen_or_wandering += 1
            if (self.cruisercount<self.lastcruisercount) or (frozen_or_wandering >= 3):
                self.attack_type = 'chaos'
                self.log_army('spreading the army')
                await self.log_attacktype('spreading the army')
                it_changed = True
                self.bestbc_dist_to_goal = 99999
                for bc in self.units(BATTLECRUISER):
                    if self.emotion_of_unittag[bc.tag] == 'frozen':
                        self.log_command('bc(AbilityId.STOP)')
                        bc(AbilityId.STOP)
                    if self.emotion_of_unittag[bc.tag] != 'recovering':
                        self.emotion_of_unittag[bc.tag] = 'lazy'
        elif self.attack_type == 'chaos':
            if self.supply_used > 190:
                change_the_type = True
                for bc in self.units(BATTLECRUISER):
                    if bc.tag == self.bestbctag:
                        sd = self.sdist(bc.position, self.target_loc)
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
                    sd = self.sdist(bc.position,self.target_loc)
                    if (sd > 9) and (sd <= self.bestbc_dist_to_goal):
                        self.bestbc_dist_to_goal = sd
                        change_the_type = False
            if change_the_type:
                self.attack_type = 'center'
                self.log_army('centering the army')
                await self.log_attacktype('centering the army')
                it_changed = True
                tp = self.random_mappoint()
                while self.near(tp,self.enemy_pos,90) or (not self.near(tp,self.enemy_pos,110)):
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
                    sd = self.sdist(bc.position,self.target_loc)
                    if (sd > 9) and (sd <= self.bestbc_dist_to_goal):
                        self.bestbc_dist_to_goal = sd
                        change_the_type = False
            if change_the_type:
                self.attack_type = 'jumpy'
                self.log_army('feeling jumpy')
                await self.log_attacktype('feeling jumpy')
                it_changed = True
        #
        #       if the attack_type changed, get a new target_loc
        if it_changed:
            self.log_army('attack_type changed, change target_loc')
            allloc = []
            for ene in self.enemy_structures.ready:
                if ene.type_id in self.hall_types:
                    allloc.append(ene.position)
            if len(allloc) == 0:
                for ene in self.enemy_structures:
                    allloc.append(ene.position)
            if len(allloc) == 0:
                self.target_loc = self.enemy_pos
            else:
                if self.random_chance(3):
                    self.target_loc = random.choice(allloc)
                elif self.random_chance(2):
                    # far from enemyclump
                    leastaa = 99999
                    for expo in range(0,self.expos):
                        aa = self.air_strength_of_expo[expo]
                        if aa < leastaa:
                            leastaa = aa
                            clumpexpo = expo
                    clumppos = self.pos_of_expo[clumpexpo]
                    maxsd = -99999
                    for pos in allloc:
                        sd = self.sdist(pos,clumppos)
                        if sd > maxsd:
                            maxsd = sd
                            self.target_loc = pos
                else:
                    # weakest antiair
                    maxaa = -99999
                    for pos in allloc:
                        expo = self.expo_of_pos(pos)
                        aa = self.air_strength_of_expo[expo]
                        if aa > maxaa:
                            maxaa = aa
                            self.target_loc = pos
            #
            self.init_vulture()


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
            if self.no_move_or_near(vik,56,5):
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
                    basp = self.loved_pos
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
        # marines individual move
        for mar in self.units(MARINE):
            if mar.tag not in self.special_tags | bunker_if.marinetags:
                tp = self.mineral_field.random.position  # mined out
                if (STIMPACK, self.nowhere) in self.birds:
                    if (mar.weapon_cooldown > 0):
                        if mar.health > 23:
                            if not mar.has_buff(BuffId.STIMPACK):
                                mar(AbilityId.EFFECT_STIM_MARINE)
                if mar.tag not in self.shame_of_unittag:
                    self.log_command('mar.attack(tp)')
                    self.go_attack(mar, tp)
                if mar.tag in self.last_health:
                    if mar.health != self.last_health[mar.tag]:
                        altpos = mar.position.towards(self.loved_pos, 0.4)
                        self.log_command('mar.move(altpos)')
                        mar.move(altpos)
                        self.detour_of_unittag[mar.tag] = True
                if self.no_move(mar, 20):
                    self.log_command('mar.attack(tp)')
                    self.go_attack(mar,tp)
        # marauders groupmove
        wantradius = 5
        groupcentre = self.nowhere
        n = 0
        sx = 0
        sy = 0
        for mar in self.units(MARAUDER):
            n += 1
            sx += mar.position.x
            sy += mar.position.y
        if n > 0:
            groupcentre = Point2((sx / n, sy / n))
            n = 0
            sx = 0
            sy = 0
            for mar in self.units(MARAUDER):
                if self.near(mar.position,groupcentre,wantradius*2):
                    n += 1
                    sx += mar.position.x
                    sy += mar.position.y
            if n > 0:
                groupcentre = Point2((sx / n, sy / n))
        reached = 0
        for mar in self.units(MARAUDER):
            if (STIMPACK, self.nowhere) in self.birds:
                if (mar.weapon_cooldown > 0):
                    if mar.health > 40:
                        if not mar.has_buff(BuffId.STIMPACKMARAUDER):
                            mar(AbilityId.EFFECT_STIM_MARAUDER)
            if mar.tag not in self.shame_of_unittag:
                self.log_command('mar.attack(self.marauder_goal)')
                self.go_attack(mar,self.marauder_goal)
            if mar.tag in self.last_health:
                if mar.health != self.last_health[mar.tag]:
                    altpos = mar.position.towards(self.loved_pos, 0.4)
                    self.log_command('mar.move(altpos)')
                    mar.move(altpos)
                    self.detour_of_unittag[mar.tag] = True
            if self.near(mar.position,groupcentre,wantradius*2):
                if not self.near(mar.position,groupcentre,wantradius):
                    mar.move(mar.position.towards(groupcentre,wantradius))
                    self.detour_of_unittag[mar.tag] = True
            if self.no_move(mar,40):
                reached += 1
        if self.opening_name in {'marauders','stimmed-marauders'}:
            if (reached >= 5):
                self.marauder_goal = self.mineral_field.random.position  # mined out
                allloc = []
                for ene in self.enemy_structures:
                    allloc.append(ene.position)
                if len(allloc) > 0:
                    self.marauder_goal = random.choice(allloc)
                self.log_army('marauder goal set')
                for mar in self.units(MARAUDER):
                    self.go_attack(mar, self.marauder_goal)
        else:
            if reached * 4 > 3 * len(self.units(MARAUDER)):
                self.marauder_goal = self.mineral_field.random.position # mined out
                if (self.random_chance(5)):
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
        tanks = len(self.units(SIEGETANK)) + len(self.units(SIEGETANKSIEGED))
        # tank duty: suppose no enemy units and kill the nearest enemy structure.
        #
        # is tank alive?
        todel = set()
        for tnktag in self.cleaning_tank_tags:
            seen = False
            for tnk in self.units(SIEGETANK) + self.units(SIEGETANKSIEGED):
                if tnk.tag == tnktag:
                    seen = True
            if not seen:
                todel.add(tnktag)
        self.cleaning_tank_tags -= todel # leave shotframe, siegepos, emotion
        # get a tank
        if len(self.cleaning_tank_tags) == 0:
            reserved = 0
            if SIEGETANK in self.buildseries_opening:
                reserved = 1
            if tanks > reserved:
                todo = 1
                for tnk in self.units(SIEGETANK):
                    if tnk.tag not in self.special_tags:
                        if tnk.tag not in self.cleaning_tank_tags:
                            if todo > 0:
                                todo -= 1
                                self.cleaning_tank_tags.add(tnk.tag)
                                self.special_tags.add(tnk.tag)
                                self.emotion_of_unittag[tnk.tag] = 'enthousiast'
                for tnk in self.units(SIEGETANKSIEGED):
                    if tnk.tag not in self.special_tags:
                        if tnk.tag not in self.cleaning_tank_tags:
                            if todo > 0:
                                todo -= 1
                                self.cleaning_tank_tags.add(tnk.tag)
                                self.special_tags.add(tnk.tag)
                                self.log_command('tnk(AbilityId.UNSIEGE_UNSIEGE)')
                                tnk(AbilityId.UNSIEGE_UNSIEGE)
                                self.emotion_of_unittag[tnk.tag] = 'enthousiast'
        if len(self.cleaning_tank_tags) > 0:
            # check cleaning_object
            if self.cleaning_object_found:
                seen = False
                for stru in self.enemy_structures:
                    if stru.tag == self.cleaning_object_tag:
                        seen = True
                        self.cleaning_object_pos = stru.position
                if not seen:
                    self.cleaning_object_found = False
            # get cleaning_object
            if not self.cleaning_object_found:
                atnkpos = self.loved_pos
                for tnk in self.units(SIEGETANK) + self.units(SIEGETANKSIEGED):
                    if tnk.tag in self.cleaning_tank_tags:
                        atnkpos = tnk.position
                minsd = 99999
                for stru in self.enemy_structures:
                    sd = self.sdist(stru.position, atnkpos)
                    if sd < minsd:
                        minsd = sd
                        self.cleaning_object_found = True
                        self.cleaning_object_pos = stru.position
                        self.cleaning_object_tag = stru.tag
            # cleaning tanks
            if self.cleaning_object_found:
                for tnk in self.units(SIEGETANK).idle:
                    if tnk.tag in self.cleaning_tank_tags:
                        if self.no_doubling(tnk.tag):
                            if self.emotion_of_unittag[tnk.tag] == 'hurt': # it has withdrawn
                                if tnk.health < self.last_health[tnk.tag]:
                                    trailnr = self.cleaning_tank_trailnr[tnk.tag]
                                    trailnr = (trailnr + 9) % 10 # -1
                                    self.cleaning_tank_trailnr[tnk.tag] = trailnr
                                    back = self.trail[tnk.tag][trailnr]
                                    self.log_command('tnk.move(back)')
                                    tnk.move(back)
                                else: # has been hurt
                                    self.log_command('tnk(AbilityId.SIEGEMODE_SIEGEMODE)')
                                    tnk(AbilityId.SIEGEMODE_SIEGEMODE)
                                    # start boredness timer
                                    self.cleaning_tank_shotframe[tnk.tag] = self.frame + 60 # some siegingtime
                                    self.emotion_of_unittag[tnk.tag] = 'sieged'
                            if self.emotion_of_unittag[tnk.tag] == 'enthousiast':
                                # get siegepos
                                around = self.cleaning_object_pos.towards(self.loved_pos,9)
                                siegepos = self.place_around(MISSILETURRET, around)
                                self.cleaning_tank_siegepos[tnk.tag] = siegepos
                                # Mark as used.
                                self.write_layout(MISSILETURRET, siegepos)
                                self.tankplaces.add(siegepos)
                                # go there
                                self.log_command('tnk.attack(siegepos)')
                                tnk.attack(siegepos)
                                self.emotion_of_unittag[tnk.tag] = 'approaching'
                            if self.emotion_of_unittag[tnk.tag] == 'approaching':
                                siegepos = self.cleaning_tank_siegepos[tnk.tag]
                                if self.near(tnk.position,siegepos,1):
                                    if tnk.weapon_cooldown == 0:
                                        self.log_command('tnk(AbilityId.SIEGEMODE_SIEGEMODE)')
                                        tnk(AbilityId.SIEGEMODE_SIEGEMODE)
                                        # start boreness timer
                                        self.cleaning_tank_shotframe[tnk.tag] = self.frame + 60 # some siegingtime
                                        self.emotion_of_unittag[tnk.tag] = 'sieged'
                                else: # it is idle but at wrong place
                                    self.log_command('tnk.attack(siegepos)')
                                    tnk.attack(siegepos)
                            if self.emotion_of_unittag[tnk.tag] == 'puzzled':
                                self.log_command('tnk.attack(self.cleaning_object_pos)')
                                tnk.attack(self.cleaning_object_pos)
                                self.emotion_of_unittag[tnk.tag] = 'searching'
                            if self.emotion_of_unittag[tnk.tag] == 'searching':
                                self.emotion_of_unittag[tnk.tag] = 'enthousiast'
                            if self.emotion_of_unittag[tnk.tag] == 'surprised':
                                self.log_command('tnk.attack(self.cleaning_object_pos)')
                                tnk.attack(self.cleaning_object_pos)
                                self.emotion_of_unittag[tnk.tag] = 'searching'
                for tnk in self.units(SIEGETANK):
                    if tnk.tag in self.cleaning_tank_tags:
                        # log
                        stri = 'a siegetank is '+self.emotion_of_unittag[tnk.tag]
                        for order in tnk.orders:
                            stri = stri + ' ' + str(order.ability.id)
                        self.log_success(stri)
                        # hurt
                        if tnk.tag in self.last_health:
                            if tnk.health < self.last_health[tnk.tag]:
                                if self.emotion_of_unittag[tnk.tag] != 'hurt':
                                    self.emotion_of_unittag[tnk.tag] = 'hurt'
                                    trailnr = (self.frame // 24) % 10
                                    trailnr = (trailnr + 9) % 10 # -1
                                    self.cleaning_tank_trailnr[tnk.tag] = trailnr
                                    back = self.trail[tnk.tag][trailnr]
                                    self.log_command('tnk.stop()')
                                    tnk.stop()
                                    self.log_command('tnk.move(back)')
                                    tnk.move(back)
                        if self.emotion_of_unittag[tnk.tag] in {'approaching','searching'}:
                            if tnk.weapon_cooldown > 0:
                                self.emotion_of_unittag[tnk.tag] = 'surprised'
                                trailnr = (self.frame // 24) % 10
                                trailnr = (trailnr + 9) % 10  # -1
                                back = self.trail[tnk.tag][trailnr]
                                self.log_command('tnk.stop()')
                                tnk.stop()
                                self.log_command('tnk.move(back)')
                                tnk.move(back)
                for tnk in self.units(SIEGETANKSIEGED):
                    if tnk.tag in self.cleaning_tank_tags:
                        if self.emotion_of_unittag[tnk.tag] == 'sieged':
                            if tnk.weapon_cooldown > 0:
                                self.cleaning_tank_shotframe[tnk.tag] = self.frame
                            shotframe = self.cleaning_tank_shotframe[tnk.tag]
                            if shotframe + 150 < self.frame: # some 7 seconds no shot
                                self.log_command('tnk(AbilityId.UNSIEGE_UNSIEGE)')
                                tnk(AbilityId.UNSIEGE_UNSIEGE)
                                self.emotion_of_unittag[tnk.tag] = 'puzzled'
        #
        # siege tank at a random own base
        for tnk in self.units(SIEGETANK) + self.units(SIEGETANKSIEGED):
            if tnk.tag not in self.special_tags:
                tnkt = tnk.tag
                expo = self.expo_of_pos(tnk.position)
                if tnkt not in self.emotion_of_unittag:
                    if (self.opening_name == 'liberator-tank'):
                        self.emotion_of_unittag[tnkt] = 'waiting'
                        self.shame_of_unittag[tnkt] = 0
                    else:
                        self.emotion_of_unittag[tnkt] = 'new'
                elif self.emotion_of_unittag[tnkt] == 'waiting':
                    self.shame_of_unittag[tnkt] += self.chosen_game_step
                    if (len(self.units(LIBERATORAG)) > 0) \
                            or (self.shame_of_unittag[tnkt] >= 800)  or (len(self.units(BATTLECRUISER)) > 0):
                        self.emotion_of_unittag[tnkt] = 'new'
                elif self.emotion_of_unittag[tnkt] == 'new':
                    # get a good tank siege position
                    aproxy = self.nowhere
                    for struc in self.structures:
                        pos = self.position_of_building(struc)
                        if self.proxy(pos):
                            aproxy = pos.towards(self.loved_pos, 3)
                    for bun in self.structures(BUNKER):
                        if self.proxy(bun.position):
                            aproxy = bun.position.towards(self.loved_pos, 3)
                    for lib in self.units(LIBERATORAG):
                        if self.proxy(lib.position):
                            aproxy = lib.position.towards(self.loved_pos, 3)
                    if (aproxy != self.nowhere) and (self.random_chance(2)):
                        goal = aproxy
                    elif (aproxy != self.nowhere) and (tanks <= 1):
                        goal = aproxy
                    elif len(self.all_bases) == 0:
                        goal = self.loved_pos
                    else:
                        tow = random.choice(self.all_bases)
                        # halfheartedly prevent all tanks in startbase
                        if tow.position == self.loved_pos:
                            tow = random.choice(self.all_bases)
                        # at first base, protect wall, at other bases, protect the tank
                        if tow.position == self.loved_pos:
                            goal = self.homeramp_pos.towards(self.loved_pos, 12)
                        else:
                            goal = tow.position.towards(self.game_info.map_center, -3)
                    place = self.place_around(MISSILETURRET,goal)
                    # Mark as used.
                    self.write_layout(MISSILETURRET, place)
                    self.tankplaces.add(place)
                    self.go_attack(tnk, place)
                    self.emotion_of_unittag[tnkt] = 'moving'
                elif self.emotion_of_unittag[tnkt] == 'moving':
                    if self.no_move_or_near(tnk,280,0.01): # yes there is a map with detour
                        self.log_command('tnk(AbilityId.SIEGEMODE_SIEGEMODE)')
                        tnk(AbilityId.SIEGEMODE_SIEGEMODE)
                        self.emotion_of_unittag[tnkt] = 'sieged'
                elif self.emotion_of_unittag[tnkt] == 'sieged':
                    hasbase = False
                    for cc in self.all_bases:
                        if self.near(tnk.position, cc.position, self.miner_bound):
                            hasbase = True
                    hasmins = False
                    for mim in self.minerals_of_expo[expo]:
                        if self.near(tnk.position, mim.position, 16):
                            hasmins = True
                    hasbunkers = 0
                    for bu in self.structures_of_expo[expo]:
                        if bu.type_id in [BUNKER]:
                            if self.near(tnk.position, bu.position, 8):
                                hasbunkers += 1
                    if not (hasbase and hasmins):
                        if hasbunkers < 2:
                            if not self.proxy(tnk.position):
                                self.log_command('tnk(AbilityId.UNSIEGE_UNSIEGE)')
                                tnk(AbilityId.UNSIEGE_UNSIEGE)
                                self.emotion_of_unittag[tnkt] = 'unsieging'
                elif self.emotion_of_unittag[tnkt] == 'unsieging':
                    if tnk in self.units(SIEGETANK):
                        self.emotion_of_unittag[tnkt] = 'new'



    async def use_mine(self):
        self.routine = 'use_mine'
        for wm in self.units(WIDOWMINE).ready:
            wmt = wm.tag
            if wmt not in self.special_tags:
                expo = self.expo_of_pos(wm.position)
                if wmt in self.goal_of_unittag:
                    nearenemies = False
                    for ene in self.enemy_units_of_expo[expo]:
                        if ene.can_attack_ground:
                            if self.ground_strength(ene) > 15: # worker strength
                                if self.near(ene.position, wm.position, 8):
                                    nearenemies = True
                    if self.no_move_or_near(wm,80,1) or (wm.health < self.maxhealth[wm.type_id]) or nearenemies:
                        self.log_command('wm(AbilityId.BURROWDOWN_WIDOWMINE)')
                        wm(AbilityId.BURROWDOWN_WIDOWMINE)
                        # solve a blockade
                        if (wm.health == self.maxhealth[wm.type_id]) and (not nearenemies):
                            if not self.near(wm.position,self.goal_of_unittag[wmt],5):
                                for dep in self.structures(SUPPLYDEPOT):
                                    if self.near(dep.position,wm.position,5):
                                        self.log_command('dep(AbilityId.MORPH_SUPPLYDEPOT_LOWER)')
                                        dep(AbilityId.MORPH_SUPPLYDEPOT_LOWER)
                                        self.log_success('lowering around blocked widowmine')
                                for tnk in self.units(SIEGETANKSIEGED):
                                    if self.near(tnk.position, wm.position, 5):
                                        self.log_success('Move tank around blocked widowmine')
                                        self.log_command('tnk(AbilityId.UNSIEGE_UNSIEGE)')
                                        tnk(AbilityId.UNSIEGE_UNSIEGE)
                                        if self.find_tobuildwalk_a_place(MISSILETURRET):
                                            goal = self.function_result_Point2
                                            self.go_move(tnk, goal)
                                            self.emotion_of_unittag[tnk.tag] = 'moving'
                                            self.tankplaces.add(goal)
                else: # find a goal
                    points = set()
                    for point in self.expansion_locations_list:
                        if self.proxy(point):
                            expo = self.expo_of_pos(point)
                            if self.ground_strength_of_expo[expo] >= 0:
                                haswm = False
                                for unt in self.units_of_expo[expo]:
                                    if unt.type_id == WIDOWMINEBURROWED:
                                        haswm = True
                                if not haswm:
                                    if self.check_layout(COMMANDCENTER, point):
                                        points.add(point)
                    if len(points) == 0:
                        for mim in self.mineral_field:
                            if self.proxy(mim.position):
                                point = mim.position.towards(self.loved_pos, -1)
                                points.add(point)
                    if len(points) == 0:
                        for mim in self.mineral_field:
                            point = mim.position.towards(self.game_info.map_center, -1)
                            points.add(point)
                    if len(points) == 0:
                        points.add(self.random_mappoint())
                    # try to avoid cannons and spores
                    tries = 0
                    goodpoint = False
                    while (not goodpoint) and (tries < 20):
                        tries += 1
                        point = random.choice(tuple(points))
                        goodpoint = True
                        for ene in self.enemy_structures:
                            if ene.type_id in self.antiair_detector:
                                if self.near(point,ene.position,8):
                                    goodpoint = False
                        nearmines = 0
                        for own in self.units(WIDOWMINEBURROWED):
                            if self.near(own.position,point,10):
                                nearmines +=1
                        if nearmines >= 2:
                            goodpoint = False
                    self.go_move(wm,point)                

    async def bc_micro(self):
        self.routine = 'bc_micro'
        for bc in self.units(BATTLECRUISER).ready:
            expo = self.expo_of_pos(bc.position)
            emotion = self.emotion_of_unittag[bc.tag]
            if emotion not in ['recovering','travels','finetuning']:
                # get targets and dangersum
                hatemax = 0
                dangersum = 0
                targets = set()
                for ene in self.enemy_units_of_expo[expo]:
                    kind = ene.type_id
                    if kind in self.bcenemies:
                        hate = self.hate_of_bcenemy[kind]
                        danger = self.danger_of_bcenemy[kind]
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
                for myn in self.units_of_expo[expo]:
                    if self.near(bc.position, myn.position, 10):
                        my_power += self.unit_power(myn.type_id)
                for myn in self.structures_of_expo[expo]:
                    kind = myn.type_id
                    if kind in [PLANETARYFORTRESS, MISSILETURRET, BUNKER]:
                        if self.near(bc.position, myn.position, 10):
                            my_power += self.unit_power(myn.type_id)
                myfactor = my_power / self.unit_power(BATTLECRUISER)
                dangersum = dangersum / myfactor
                # choose target, prefer lasttarget
                if hatemax > 0:
                    target = random.choice(tuple(targets))
                    if bc.tag in self.lasttargettag_of_bctag:
                        for tar in targets:
                            if tar.tag == self.lasttargettag_of_bctag[bc.tag]:
                                target = tar
                # if too dangerous, move away from adanger
                if (dangersum >= 100):
                    away = Point2((1.5*bc.position.x-0.5*adanger.x, 1.5*bc.position.y-0.5*adanger.y))
                    self.log_command('bc.move(away)')
                    bc.move(away)
                    self.detour_of_unittag[bc.tag] = True
                # maybe shoot
                if (hatemax > 0) and (dangersum < 100):
                    alreadyshooting = False
                    if bc.tag in self.lasttargettag_of_bctag:
                        if target.tag == self.lasttargettag_of_bctag[bc.tag]:
                            alreadyshooting = True
                    if not alreadyshooting:
                        if (self.attack_type != 'jumpy'):
                            self.log_command('bc(AbilityId.SMART, target)')
                            bc(AbilityId.SMART, target)
                            self.detour_of_unittag[bc.tag] = True
                # set lasttarget
                if hatemax > 0:
                    self.lasttargettag_of_bctag[bc.tag] = target.tag
                # yamato
                if (hatemax >= 4) and (dangersum < 200):
                    yama = True
                    if target.tag in self.yamatoed:
                        if (self.frame < self.yamatoed[target.tag] + 75):
                            yama = False
                    if yama:
                        abilities = (await self.get_available_abilities([bc]))[0]
                        if AbilityId.YAMATO_YAMATOGUN in abilities:
                            self.log_command('bc(AbilityId.YAMATO_YAMATOGUN,'+target.name+')')
                            bc(AbilityId.YAMATO_YAMATOGUN, target)
                            self.yamatoed[target.tag] = self.frame
                            # the yamato stops the movement, so mark detour.
                            self.detour_of_unittag[bc.tag] = True


    def yamato_admin(self):
        # To be executed rarely. Cleans up superfluous admin.
        todel = set()
        for enetag in self.yamatoed:
            if self.yamatoed[enetag] < self.frame - 75:
                todel.add(enetag)
        for enetag in todel:
            del self.yamatoed[enetag]


    async def raven_micro(self):
        self.routine = 'raven_micro'
        for ra in self.units(RAVEN).ready:
            expo = self.expo_of_pos(ra.position)
            found = False
            for ene in self.enemy_units_of_expo[expo]:
                kind = ene.type_id
                if kind in self.bcenemies:
                    if self.hate_of_bcenemy[kind] >= 4:
                        if self.near(ene.position,ra.position,10):
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

    def liberator(self):
        for lib in self.units(LIBERATOR):
            expo = self.expo_of_pos(lib.position)
            if lib.tag in self.libspot:
                spot = self.libspot[lib.tag]
                if self.no_move(lib, 8):
                    # check for antiair near the tail
                    tail = Point2((2*spot[2].x-spot[1].x, 2*spot[2].y-spot[1].y))
                    taildanger = 0
                    for ene in self.enemy_units_of_expo[expo]:
                        if self.near(ene.position,tail,10):
                            enetype = ene.type_id
                            if (enetype in self.bcenemies):
                                taildanger += self.danger_of_bcenemy[enetype]
                    if taildanger > 0:
                        oldname = spot[0]
                        while spot[0] == oldname:
                            spot = random.choice(tuple(self.liberator_spots))
                        self.libspot[lib.tag] = spot
                        self.go_move(lib, spot[2])
                    else: # no taildanger
                        lib(AbilityId.MORPH_LIBERATORAGMODE,spot[1])
                        # fly factory out
                        if self.opening_name in ['liberator-cc','liberator-bc']:
                            for fac in self.structures(FACTORY).ready + self.structures(FACTORYFLYING):
                                if fac.tag == self.lib_factory_tag:
                                    self.goal_of_flying_struct[fac.tag] = self.cheese_factory_pos
                                    # now, will it move there?
                                    if fac in self.structures(FACTORY):
                                        self.landings_of_flying_struct[fac.tag] = 0
                                        self.log_success('up FACTORY')
                                        self.log_command('fac(AbilityId.LIFT')
                                        fac(AbilityId.LIFT)
            else: # get spot
                spot = random.choice(tuple(self.liberator_spots))
                if (self.opening_name in {'liberator-bc','liberator-cc'}):
                    if (self.enemy_race != Race.Zerg) and (self.firstlib):
                        while (spot[0] != 'contain1'):
                            spot = random.choice(tuple(self.liberator_spots))
                if (self.opening_name == 'two liberators'):
                    if (self.firstlib):
                        while (spot[0] != 'mim1'):
                            spot = random.choice(tuple(self.liberator_spots))
                    if (self.secondlib):
                        while (spot[0] != 'mim2'):
                            spot = random.choice(tuple(self.liberator_spots))
                self.libspot[lib.tag] = spot
                self.go_move(lib,spot[2])
                if self.firstlib:
                    self.firstlib = False
                    self.secondlib = True
                elif self.secondlib:
                    self.secondlib = False
        if self.opening_name in ['liberator-cc', 'liberator-bc']:
            # fly proxy factory in
            flightdura = 1 + self.circledist(self.cheese_factory_pos,self.cheese_landing_pos) / 1.3
            for (martype,bartype,pos,dura) in self.eggs:
                if (martype == LIBERATOR) and (dura < flightdura):
                    for fac in self.structures(FACTORY).ready:
                        if fac.position == self.cheese_factory_pos:
                            self.lib_factory_tag = fac.tag
                            self.goal_of_flying_struct[fac.tag] = self.cheese_landing_pos
                            self.landings_of_flying_struct[fac.tag] = 0
                            self.log_success('up FACTORY')
                            self.log_command('fac(AbilityId.LIFT')
                            fac(AbilityId.LIFT)
        if self.opening_name == 'liberator-tank':
            for (martype,bartype,pos,dura) in self.eggs:
                if (martype == LIBERATOR) and (dura < 8):
                    for scv in self.units(SCV):
                        if scv.tag == self.scout1_tag:
                            self.promote(scv,'idler')
                            scv.move(self.cheese_landing_pos)
                            self.throw_at_spot(BUNKER,self.cheese_landing_pos,'liberator-tank',1)
        sieged = False
        for lib in self.units(LIBERATORAG):
            sieged = True
        if sieged:
            if self.lib_turpos == self.nowhere:
                self.lib_turpos = lib.position.towards(self.loved_pos, 2)
                self.lib_turpos = self.place_around(MISSILETURRET, self.lib_turpos)
            if self.lib_turret_tries > 0:
                if not self.we_started_at(self.lib_turpos,MISSILETURRET):
                    thrown = False
                    for tps in self.throwspots:
                        (th, po, status, ow, pri) = tps
                        if ow == 'liberator':
                            thrown = True
                    if not thrown:
                        self.throw_at_spot(MISSILETURRET,self.lib_turpos,'liberator',1)
                        self.lib_turret_tries -= 1
            # redirect attack to natural if any
            for (martype, bartype, pos, dura) in self.eggs:
                if (martype == BATTLECRUISER) and (dura < 10):
                    nat_used = False
                    for ene in self.enemy_structures:
                        if ene.position == self.enemynatural_pos:
                            nat_used = True
                    if nat_used:
                        if self.target_loc != self.enemynatural_pos:
                            self.log_army('change target_loc to enemy natural')
                            self.target_loc = self.enemynatural_pos
                            self.init_vulture()
        else: # not sieged
            todel = set()
            for tps in self.throwspots:
                (th, po, status, ow, pri) = tps
                if ow == 'liberator':
                    todel.add(tps)
            for tps in todel:
                del self.throwspots[self.throwspots.index(tps)]
        # if the factory flies home for repair, leave it there
        for fac in self.structures(FACTORY).ready + self.structures(FACTORYFLYING):
            if fac.tag == self.lib_factory_tag:
                if not self.proxy(fac.position):
                    if self.goal_of_flying_struct[fac.tag] == self.cheese_factory_pos:
                        if self.find_tobuildwalk_a_place(FACTORY):
                            spot = self.function_result_Point2
                            self.goal_of_flying_struct[fac.tag] = spot
                            self.write_layout(FACTORY,spot)


    def do_rally(self):
        # effect the rallys planned in set_rally
        todel = set()
        for (buipos,ralpos) in self.set_rally:
            for bui in self.structures.ready:
                if bui.position == buipos:
                    bui(AbilityId.RALLY_BUILDING,ralpos)
                    todel.add((buipos,ralpos))
        self.set_rally -= todel

    def unit_power(self,thing) -> int:
        # estimate of fighting power
        cost = self.get_total_cost(thing)
        power = cost.minerals+2*cost.vespene
        return power

    async def worker_defence(self):
        self.routine = 'worker_defence'
        for tow in self.all_bases:
            if tow.tag not in self.special_tags:
                expo = self.expo_of_pos(tow.position)
                # calc enemies and enemy_power
                enemies = []
                enemy_power = 0
                cx = 0
                cy = 0
                n_enemies = 0
                for ene in self.enemy_units_of_expo[expo]:
                    if not ene.is_flying:
                        enemies.append(ene)
                        enemy_power += self.unit_power(ene.type_id)
                        cx = cx + ene.position.x
                        cy = cy + ene.position.y
                        n_enemies += 1
                for ene in self.enemy_structures_of_expo[expo]:
                    if not ene.is_flying:
                        enemies.append(ene)
                        enemy_power += self.unit_power(ene.type_id)
                        cx = cx + ene.position.x
                        cy = cy + ene.position.y
                        n_enemies += 1
                all_enemytags = {ene.tag for ene in enemies}
                if n_enemies > 0:
                    center_enemies = Point2((cx / n_enemies, cy / n_enemies))
                    # use 1 frame lookahead
                    if not self.near(center_enemies, self.last_center_enemies,2):
                        self.last_center_enemies = center_enemies
                    next_center_enemies = Point2(((2*center_enemies.x-self.last_center_enemies.x), (2*center_enemies.y-self.last_center_enemies.y)))
                    self.last_center_enemies = center_enemies
                # calc my_power
                my_power = 0
                for myn in self.units_of_expo[expo]:
                    my_power += self.unit_power(myn.type_id)
                for myn in self.structures_of_expo[expo]:
                    if myn.type_id in [PLANETARYFORTRESS,MISSILETURRET,BUNKER]:
                        my_power += self.unit_power(myn.type_id)
                if my_power * 3 < enemy_power * 2:
                    # no hope
                    self.log_success('eeeeek!!!')
                    away = Point2((2*tow.position.x-next_center_enemies.x, 2*tow.position.y-next_center_enemies.y))
                    for myscv in self.scvs_of_expo[expo]:
                        job = self.job_of_scvt[myscv.tag]
                        if (job in self.bad_jobs + self.no_jobs) and (job not in {'inshock','fleeer'}):
                            self.promote(myscv,'inshock')
                            self.log_command('my_scv.move(away)')
                            myscv.move(away)
                else: #defend
                    if len(enemies) > 0:
                        wished_defenders = enemy_power/50 + 2
                    else:
                        wished_defenders = 0
                    # calc defenders
                    defenders = set()
                    for myscv in self.scvs_of_expo[expo]:
                        scvt = myscv.tag
                        job = self.job_of_scvt[scvt]
                        if (job == 'defender'):
                            defenders.add(myscv)
                    if len(defenders) > 0:
                        # dismiss veterans
                        veterans = set()
                        for myscv in defenders:
                            if myscv.health < 12:
                                veterans.add(myscv)
                                self.promote(myscv,'fleeer') # includes move
                        defenders -= veterans
                    if len(enemies) > 0:
                        # get new defenders
                        toget = wished_defenders - len(defenders)
                        if toget > 0:
                            candidates = set()
                            for myscv in self.scvs_of_expo[expo]:
                                if myscv.health >= 12:
                                    scvt = myscv.tag
                                    job = self.job_of_scvt[scvt]
                                    if job in (self.bad_jobs + self.no_jobs):
                                        candidates.add(myscv)
                            while (toget > 0) and (len(candidates) > 0):
                                bestsd = 99999
                                for myscv in candidates:
                                    sd = self.sdist(myscv.position,next_center_enemies)
                                    if sd < bestsd:
                                        bestscv = myscv
                                        bestsd = sd
                                myscv = bestscv
                                scvt = myscv.tag
                                candidates.remove(myscv)
                                # promote to defender and let idle
                                toget -= 1
                                self.promote(myscv,'defender')
                    if (len(defenders) > wished_defenders) or (len(enemies) == 0):
                        # dismiss some defenders
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
                            if self.near(next_center_enemies,ene.position,3):
                                grouped = True
                        if grouped:
                            # group attack
                            for myscv in defenders:
                                self.log_command('myscv.attack(next_center_enemies)')
                                myscv.attack(next_center_enemies)
                        else:
                            # individual attack
                            for myscv in defenders:
                                if myscv.tag in self.targettag_of_defendertag:
                                    targettag = self.targettag_of_defendertag[myscv.tag]
                                    if targettag not in all_enemytags:
                                       del self.targettag_of_defendertag[myscv.tag] 
                                if myscv.tag not in self.targettag_of_defendertag:
                                    target = random.choice(enemies)
                                    self.targettag_of_defendertag[myscv.tag] = target.tag
                                    self.log_command('myscv.attack(target)')
                                    myscv.attack(target)


    async def cheese_army(self):
        self.routine = 'cheese_army'
        if self.cheese_marine_count < 4:
            thing = MARINE
            if (self.cheese_phase >= 'B') and (self.cheese_phase < 'Z'):
                for ba in self.structures(BARRACKS).ready.idle:
                    if self.cheese_barracks_tag == ba.tag:
                        if self.can_pay(thing):
                            if self.supply_check(thing):
                                self.log_command('ba.train(thing)')
                                ba.train(thing)
                                self.cheese_marine_count += 1
        if self.cheese_tank_count < 1:
            thing = SIEGETANK
            if (self.cheese_phase >= 'K') and (self.cheese_phase < 'Z'):
                for fac in self.structures(FACTORY).ready.idle:
                    if self.cheese_factory_tag == fac.tag:
                        if self.can_pay(thing):
                            if self.supply_check(thing):
                                self.log_command('fac.train(thing)')
                                fac.train(thing)
                                self.cheese_tank_count += 1
        if self.cheese_mine_count < 2:
            thing = WIDOWMINE
            if (self.cheese_phase >= 'N') and (self.cheese_phase < 'Z'):
                for fac in self.structures(FACTORY).ready.idle:
                    if self.cheese_factory_tag == fac.tag:
                        if self.can_pay(thing):
                            if self.supply_check(thing):
                                self.log_command('fac.train(thing)')
                                fac.train(thing)
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
                    self.cheese_bunker_tag = bunk.tag
                    startedbuildings += 1
            if startedbuildings == 0:
                self.cheese_phase = 'Y cleanup'
        # follow a large series of phases
        if self.cheese_phase == 'Anobunker':
            if self.cheese_scv_tag == self.notag:
                self.cheese_phase = 'Y cleanup'
            elif self.add_thought(BUNKER, self.cheese_bunker_pos,'bunkercheese'):
                self.cheese_phase = 'Athought'
        elif self.cheese_phase == 'Athought':
            if await self.build_thing_tobuildwalk(self.cheese_scv_tag, BUNKER, self.cheese_bunker_pos,'bunkercheese'):
                self.cheese_phase = 'A'
        elif self.cheese_phase == 'A':
            for barra in self.structures(BARRACKS):
                if barra.position == self.cheese_barracks_pos:
                    self.cheese_barracks_tag = barra.tag
                    self.special_tags.add(barra.tag)
            # wait for landed barracks and building bunker
            startedbuildings = 0
            for barra in self.structures(BARRACKS).ready:
                if barra.position != self.cheese_barracks_pos:
                    if self.near(barra.position,self.cheese_landing_pos,7):
                        startedbuildings += 1
            for bunk in self.structures(BUNKER):
                if bunk.position == self.cheese_bunker_pos:
                    self.cheese_bunker_tag = bunk.tag
                    startedbuildings += 1
            if startedbuildings == 2:
                for anscv in self.units(SCV):
                    scvt = anscv.tag
                    if scvt in self.goal_of_trabu_scvt:
                        if self.goal_of_trabu_scvt[scvt] == self.cheese_bunker_pos:
                            self.promote(anscv,'cheeser')
                            self.cheese_scv_tag = anscv.tag
                            self.special_tags.add(self.cheese_scv_tag)
                self.cheese_marine_count = 0
                self.cheese_tank_count = 0
                self.cheese_phase = 'B'
        elif self.cheese_phase == 'B':
            for ba in self.structures(BARRACKS):
                if ba.tag == self.cheese_barracks_tag:
                    self.log_command('ba(AbilityId.RALLY_BUILDING,self.cheese_prison_pos)')
                    ba(AbilityId.RALLY_BUILDING,self.cheese_prison_pos)
                    self.cheese_phase = 'C'
        elif self.cheese_phase == 'C':
            # wait for bunker ready
            # check for a lost cause
            for bun in self.structures(BUNKER):
                if bun.tag == self.cheese_bunker_tag:
                    if bun.tag in self.last_health:
                        if bun.health < 0.67 * self.last_health[bun.tag]:
                            # execute bunkercheese before destroyed
                            # cancel the build
                            bun(AbilityId.CANCEL)
                            self.cheese_phase = 'Anobunker'
                            # execute bunkercheese before make_planning_exe
                            self.but_i_had_structures = 0
                    # first, try back-to-track
                    if (self.cheese_scv_tag not in self.all_scvtags) and (self.scout1_tag != self.notag):
                        # promote scout to cheese_scv
                        for scv in self.units(SCV):
                            if scv.tag == self.scout1_tag:
                                if self.near(scv.position,self.cheese_prison_pos,20):
                                    self.cheese_scv_tag = scv.tag
                                    self.special_tags.add(self.cheese_scv_tag)
                                    self.scout1_tag = self.notag
                                    self.promote(scv,'cheeser')
                                    self.log_command('scv(AbilityId.SMART,bun)')
                                    scv(AbilityId.SMART,bun)
                    if bun in self.structures(BUNKER).ready:
                        # rally and load
                        for ba in self.structures(BARRACKS):
                            if ba.tag == self.cheese_barracks_tag:
                                for scv in self.units(SCV):
                                    if scv.tag == self.cheese_scv_tag:
                                        self.log_command('ba(AbilityId.RALLY_BUILDING,bun)')
                                        ba(AbilityId.RALLY_BUILDING,bun)
                                        self.log_command('bun(AbilityId.RALLY_BUILDING,self.cheese_prison_pos)')
                                        bun(AbilityId.RALLY_BUILDING,self.cheese_prison_pos)
                                        # warning: scv inside the bunker is not in self.units(SCV)
                                        self.log_command('bun(AbilityId.LOAD_BUNKER,scv)')
                                        bun(AbilityId.LOAD_BUNKER,scv)
                                        self.cheese_phase = 'D'
            if self.cheese_bunker_tag not in self.all_bunkertags:
                if self.cheese_scv_tag in self.all_scvt:
                    self.cheese_phase = 'Anobunker'
        elif self.cheese_phase == 'D':
            # temporarily load some marines to make place for the scv
            self.cheese_marine_tags = set()
            for mari in self.units(MARINE):
                if self.near(mari.position, self.cheese_landing_pos, 7):
                    self.cheese_marine_tags.add(mari.tag)
            for mari in self.units(MARINE):
                if mari.tag in self.cheese_marine_tags:
                    for bun in self.structures(BUNKER):
                        if bun.tag == self.cheese_bunker_tag:
                            if len(bun.passengers) < 4:
                                self.log_command('bun(AbilityId.LOAD_BUNKER,mari)')
                                bun(AbilityId.LOAD_BUNKER,mari)
            self.cheese_phase = 'E'
        elif self.cheese_phase == 'E':
            # we want to unload the cheese_scv, but it is said only unloadall works
            for bun in self.structures(BUNKER):
                if bun.tag == self.cheese_bunker_tag:
                    self.log_command('bun(AbilityId.UNLOADALL_BUNKER)')
                    bun(AbilityId.UNLOADALL_BUNKER)
                    self.cheese_frames = 0
                    self.cheese_phase = 'F'
        elif self.cheese_phase == 'F':
            # The scv sometimes does not come out. Maybe if a marine goes out and starts shooting?
            self.cheese_frames += self.chosen_game_step
            if self.cheese_frames == 24:
                self.cheese_phase = 'G'
        elif self.cheese_phase == 'G':
            self.cheese_marine_tags = set()
            for mari in self.units(MARINE):
                if self.near(mari.position, self.cheese_landing_pos, 7):
                    self.cheese_marine_tags.add(mari.tag)
            for mari in self.units(MARINE):
                if mari.tag in self.cheese_marine_tags:
                    for bun in self.structures(BUNKER):
                        if bun.tag == self.cheese_bunker_tag:
                            if len(bun.passengers) < 4:
                                self.log_command('bun(AbilityId.LOAD_BUNKER,mari)')
                                bun(AbilityId.LOAD_BUNKER,mari)
            self.cheese_phase = 'H'
            if self.cheese_scv_tag not in self.all_scvt: # cheese_scv is still inside the bunker
                self.cheese_phase = 'E'
        elif self.cheese_phase == 'H':
            # repeat the load command as it is seen to be disobeyed
            self.cheese_marine_tags = set()
            for mari in self.units(MARINE):
                if self.near(mari.position, self.cheese_landing_pos, 7):
                    self.cheese_marine_tags.add(mari.tag)
            for mari in self.units(MARINE):
                if mari.tag in self.cheese_marine_tags:
                    for bun in self.structures(BUNKER):
                        if bun.tag == self.cheese_bunker_tag:
                            if len(bun.passengers) < 4:
                                self.log_command('bun(AbilityId.LOAD_BUNKER,mari)')
                                bun(AbilityId.LOAD_BUNKER,mari)
            # wait for the factory and rally it
            for facta in self.structures(FACTORY).ready:
                if facta.position == self.cheese_factory_pos:
                    self.cheese_factory_tag = facta.tag
                    point = self.cheese_tank_pos
                    self.log_command('facta(AbilityId.RALLY_BUILDING, point)')
                    facta(AbilityId.RALLY_BUILDING, point)
                    self.cheese_phase = 'I'
        elif self.cheese_phase == 'I':
            # make a lab
            for fac in self.structures(FACTORY).ready:
                if fac.position == self.cheese_factory_pos:
                    if self.can_pay(FACTORYTECHLAB):
                        self.log_command('fac.train(FACTORYTECHLAB)')
                        fac.train(FACTORYTECHLAB)
                        self.cheese_phase = 'J'
        elif self.cheese_phase == 'J':
            for tl in self.structures(FACTORYTECHLAB).ready:
                self.cheese_phase = 'K'
        elif self.cheese_phase == 'K':
            # wait for tank to be made
            if self.cheese_tank_count == 1:
                for st in self.units(SIEGETANK).ready:
                    if self.near(st.position,self.cheese_factory_pos,7):
                        self.cheese_tank_tag = st.tag
                        self.special_tags.add(self.cheese_tank_tag)
                        # toward cheese_tank_pos
                        self.log_command('st.attack(self.cheese_tank_pos)')
                        st.attack(self.cheese_tank_pos)
                        # fly the factory in
                        for fac in self.structures(FACTORY).ready:
                            if fac.tag == self.cheese_factory_tag:
                                self.goal_of_flying_struct[fac.tag] = self.cheese_landing_pos
                                self.landings_of_flying_struct[fac.tag] = 0
                                self.log_success('up FACTORY')
                                self.log_command('fac(AbilityId.LIFT')
                                fac(AbilityId.LIFT)
                                # next phase
                                self.cheese_phase = 'L'
        elif self.cheese_phase == 'L':
            # wait for tank to arrive, then siege it
            for st in self.units(SIEGETANK).idle:
                if st.tag == self.cheese_tank_tag:
                    self.log_command('st(AbilityId.SIEGEMODE_SIEGEMODE)')
                    st(AbilityId.SIEGEMODE_SIEGEMODE)
                    self.cheese_phase = 'M'
        elif self.cheese_phase == 'M':
            # fly the barracks out
            for ba in self.structures(BARRACKS):
                if ba.tag == self.cheese_barracks_tag:
                    self.goal_of_flying_struct[ba.tag] = self.cheese_factory_pos
                    self.landings_of_flying_struct[ba.tag] = 0
                    self.log_success('up BARRACKS')
                    self.log_command('ba(AbilityId.LIFT')
                    ba(AbilityId.LIFT)
                    self.cheese_phase = 'N'
        elif self.cheese_phase == 'N':
            # wait for landing of factory and rally it
            for fac in self.structures(FACTORY).ready:
                if fac.tag == self.cheese_factory_tag:
                    for bun in self.structures(BUNKER):
                        if bun.tag == self.cheese_bunker_tag:
                            point = bun.position.towards(self.enemy_pos,2)
                            self.log_command('fac(AbilityId.RALLY_BUILDING, point)')
                            fac(AbilityId.RALLY_BUILDING, point)
                            self.cheese_phase = 'O'
        elif self.cheese_phase == 'O':
            # wait for 2 cheese_mines
            for wm in self.units(WIDOWMINE).ready:
                wmt = wm.tag
                if self.near(wm.position,self.cheese_landing_pos,7):
                    if wmt not in self.cheese_mine_tags:
                        self.cheese_mine_tags.add(wmt)
                        self.special_tags.add(wmt)
                        found = False
                        while not found:
                            mim = self.mineral_field.random
                            if self.near(mim.position, self.enemy_pos, self.miner_bound):
                                goal = mim.position.towards(self.loved_pos,-2)
                                found = True
                        self.burrowpos_of_wmt[wmt] = goal
                        pole = self.get_near_pole(goal)
                        self.homepole_of_wmt[wmt] = pole
                        pole = self.get_near_pole(wm.position)
                        pole = (pole + 1) % len(self.scout1_pos)
                        self.pole_of_wmt[wmt] = pole
                        self.phase_of_wmt[wmt] = 'flee'
                        if len(self.cheese_mine_tags) < 2:
                            self.log_command('wm(AbilityId.BURROWDOWN_WIDOWMINE)')
                            wm(AbilityId.BURROWDOWN_WIDOWMINE)
            if len(self.cheese_mine_tags) == 2:
                for wm in self.units(WIDOWMINE) + self.units(WIDOWMINEBURROWED):
                    if wm.tag in self.cheese_mine_tags:
                        wmt = wm.tag
                        if (wm in self.units(WIDOWMINEBURROWED)):
                            self.log_command('wm(AbilityId.BURROWUP_WIDOWMINE)')
                            wm(AbilityId.BURROWUP_WIDOWMINE)
                        pole = self.pole_of_wmt[wmt]
                        goal = self.scout1_pos[pole]
                        self.go_move(wm,goal)
                        self.cheese_phase = 'P'
        elif self.cheese_phase == 'P':
            # manage cheesemines
            for wm in self.units(WIDOWMINE) + self.units(WIDOWMINEBURROWED):
                if wm.tag in self.cheese_mine_tags:
                    wmt = wm.tag
                    if self.phase_of_wmt[wmt] == 'attack':
                        if (wm in self.units(WIDOWMINE)):
                            if self.no_move_or_near(wm,32,0.1):
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
                                pole = (pole + 1) % len(self.scout1_pos)
                                self.pole_of_wmt[wmt] = pole
                                goal = self.scout1_pos[pole]
                                self.go_move(wm,goal)
                    if self.phase_of_wmt[wmt] == 'flee':
                        pole = self.pole_of_wmt[wmt]
                        goal = self.scout1_pos[pole]
                        if self.no_move_or_near(wm,32,4):
                            pole = (pole + 1) % len(self.scout1_pos)
                            if pole == self.homepole_of_wmt[wmt]:
                                goal = self.burrowpos_of_wmt[wmt]
                                self.phase_of_wmt[wmt] = 'attack'
                            else:
                                goal = self.scout1_pos[pole]
                            self.pole_of_wmt[wmt] = pole
                            self.go_move(wm,goal)
            if len(self.cheese_mine_tags) == 0: #todo living
                self.cheese_phase = 'Y cleanup'
        elif self.cheese_phase == 'Y cleanup':
            # clean up
            for scv in self.units(SCV):
                if scv.tag == self.cheese_scv_tag:
                    self.special_tags.remove(self.cheese_scv_tag)
                    self.promote(scv,'idler')
            self.cheese_scv_tag = self.notag
            for st in self.units(SIEGETANKSIEGED):
                if st.tag == self.cheese_tank_tag:
                    self.log_command('st(AbilityId.UNSIEGE_UNSIEGE)')
                    st(AbilityId.UNSIEGE_UNSIEGE)
                    self.log_command('st.attack(self.shipyard)')
                    st.attack(self.shipyard)
            if self.cheese_tank_tag in self.special_tags:
                self.special_tags.remove(self.cheese_tank_tag)
            self.cheese_tank_tag = self.notag
            for ba in self.structures(BARRACKS):
                if ba.tag == self.cheese_barracks_tag:
                    if ba.tag in self.special_tags:
                        self.special_tags.remove(ba.tag)
                    self.log_command('bu(AbilityId.CANCEL)')
                    ba(AbilityId.CANCEL)
                    self.goal_of_flying_struct[ba.tag] = self.wall_barracks_pos
                    self.landings_of_flying_struct[ba.tag] = 0
                    self.log_success('up CHEESE_BARRACKS')
                    self.log_command('ba(AbilityId.LIFT')
                    ba(AbilityId.LIFT)
            self.cheese_barracks_tag = self.notag
            self.special_tags -= self.cheese_mine_tags
            self.cheese_mine_tags = set()
            self.log_success('ending the bunkercheese')
            self.cheese_phase = 'Z'
        #
        self.log_cheese()

    ################ cheese2 ########################

    async def bunker_handling(self):
        self.routine = 'bunker_handling'
        # hiding_spot
        if bunker_if.hiding_spot is None:
            place = self.random_mappoint()
            while self.proxy(place) or self.near(place, self.loved_pos, 60):
                place = self.random_mappoint()
            bunker_if.hiding_spot = place
        if not (self.game_choice[2] or self.game_choice[3] or self.game_choice[6]):  # tight openings TODO special_tags
            for bu in self.structures(BUNKER):
                # give some time to others to make it special
                if bu.build_progress > 0.25:
                    if bu.tag not in self.special_tags:
                        bunker_if.bunkertags.add(bu.tag)
            if len(bunker_if.marinetags) < self.wished_marines_per_bunker * len(bunker_if.bunkertags):
                todo = 1
                for mar in self.units(MARINE):
                    if mar.tag not in bunker_if.marinetags:
                        if todo > 0:
                            todo -= 1
                            bunker_if.marinetags.add(mar.tag)
                # and to prevent problems with direct load:
                for bu in self.structures(BUNKER):
                    if bu.tag in bunker_if.bunkertags:
                        for mar in bu.passengers:
                            if mar.type_id == MARINE:
                                if mar.tag not in bunker_if.marinetags:
                                    if todo > 0:
                                        todo -= 1
                                        bunker_if.marinetags.add(mar.tag)
            if len(bunker_if.bunkertags) > 0:
                if len(bunker_if.scvtags) < 2:
                    scvt = self.get_near_scvt_to_goodjob(self.loved_pos)
                    for scv in self.units(SCV):
                        if scv.tag == scvt:
                            self.promote(scv, 'cheeser')
                            bunker_if.scvtags.add(scv.tag)
            # salvage bunker
            for tow in self.expansion_locations_list:
                expo = self.expo_of_pos(tow)
                # calc static my_power
                my_power = 0
                for myn in self.units_of_expo[expo]:
                    if myn.type_id in [SIEGETANKSIEGED, WIDOWMINEBURROWED]:
                        my_power += self.unit_power(myn.type_id)
                for myn in self.structures_of_expo[expo]:
                    if myn.type_id in [PLANETARYFORTRESS]:
                        my_power += self.unit_power(myn.type_id)
                if my_power > 200:
                    for bun in self.structures_of_expo[expo]:
                        if bun.type_id in [BUNKER]:
                            if not self.proxy(bun.position): # cheese exception
                                if bun.tag in bunker_if.bunkertags:
                                    # salvage
                                    await bunker_if.salvage(bun)
            if self.supply_used > 190:
                # bunkers not useful any more
                mintag = self.notag
                first = True
                for bun in self.structures(BUNKER):
                    if bun.tag in bunker_if.bunkertags:
                        if first:
                            mintag = bun.tag
                            first = False
                        mintag = min(bun.tag, mintag)
                for bun in self.structures(BUNKER):
                    if bun.tag in bunker_if.bunkertags:
                        if bun.tag == mintag:
                            # salvage
                            await bunker_if.salvage(bun)
            if len(bunker_if.bunkertags) == 0:
                if not self.we_started_a(BUNKER):
                    # release scvs and marines
                    for scv in self.units(SCV):
                        if scv.tag in bunker_if.scvtags:
                            self.promote(scv, 'idler')
                    bunker_if.scvtags = set()
                    bunker_if.marinetags = set()




    async def bunkercheese2(self):
        self.routine = 'bunkercheese2'
        if self.game_choice[50]:
            if not self.rushopening: # that would be a bad combination
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


    ################ cheese3 ########################


    async def cheese3_internals(self):
        # bunker has started
        # name cheesebunker
        for bu in self.structures(BUNKER):
            if bu.position == self.cheese3_bunker_pos:
                self.cheese3_bunker_tag = bu.tag
            if bu.position == self.cheese3_bunker2_pos:
                self.cheese3_bunker2_tag = bu.tag
        # rebuild bunker
        if not self.we_started_at(BUNKER, self.cheese3_bunker_pos):
            self.throw_at_spot_if_rich(BUNKER, self.cheese3_bunker_pos, 'cheese3_internals',1)
        if self.cheese3_bunker2_pos != self.nowhere:
            if not self.we_started_at(BUNKER, self.cheese3_bunker2_pos):
                self.throw_at_spot_if_rich(BUNKER, self.cheese3_bunker2_pos, 'cheese3_internals',1)


    async def do_pf_rush(self):
        self.routine = 'do_pf_rush'
        if self.opening_name == 'pf-rush':
            if self.cheese3_phase == 'A':
                # while (nothing)
                # continue
                for ba in self.structures(BARRACKS):
                    if ba.position == self.cheese3_barracks_pos:
                        # init (barracks is constructing)
                        self.special_tags.add(ba.tag)
                        self.cheese3_barracks_tag = ba.tag
                        self.cheese3_phase = 'B'
            elif self.cheese3_phase == 'B':
                # while (barracks is constructing)
                #clean
                if self.cheese3_barracks_tag not in (ba.tag for ba in self.structures(BARRACKS)):
                    self.cheese3_phase = 'Y'
                # continue
                for bu in self.structures(BUNKER):
                    if bu.position == self.cheese3_bunker_pos:
                        # init (bunker is constructing)
                        self.cheese3_bunker_tag = bu.tag
                        self.cheese3_phase = 'C'
            elif self.cheese3_phase == 'C':
                # while (bunker is constructing)
                await self.cheese3_internals()
                #clean
                if self.cheese3_barracks_tag not in (ba.tag for ba in self.structures(BARRACKS)):
                    self.cheese3_phase = 'Y'
                # continue
                for bu in self.structures(BUNKER).ready:
                    if bu.tag == self.cheese3_bunker_tag:
                        # init (bunker ready)
                        for ba in self.structures(BARRACKS):
                            if ba.tag == self.cheese3_barracks_tag:
                                ba(AbilityId.RALLY_BUILDING,bu)
                        self.cheese3_phase = 'D'
            elif self.cheese3_phase == 'D':
                # while (bunker ready)
                await self.cheese3_internals()
                #clean
                if self.cheese3_barracks_tag not in (ba.tag for ba in self.structures(BARRACKS)):
                    self.cheese3_phase = 'Y'
                # continue
                for cc in self.structures(COMMANDCENTER):
                    if cc.position == self.cheese3_cc_pos:
                        # init (cc constructing)
                        self.special_tags.add(cc.tag)
                        self.cheese3_cc_tag = cc.tag
                        self.cheese3_phase = 'E'
            elif self.cheese3_phase == 'E':
                # while (cc constructing)
                await self.cheese3_internals()
                # chosen is no redo if the cc-build is interrupted
                #clean
                if self.cheese3_barracks_tag not in (ba.tag for ba in self.structures(BARRACKS)):
                    self.cheese3_phase = 'Y'
                if self.cheese3_cc_tag not in (cc.tag for cc in self.structures(COMMANDCENTER)):
                    self.cheese3_phase = 'Y'
                # continue
                for cc in self.structures(COMMANDCENTER).ready:
                    if cc.tag == self.cheese3_cc_tag:
                        # init (cc ready)
                        self.goal_of_flying_struct[cc.tag] = self.cheese3_landing_pos
                        self.landings_of_flying_struct[cc.tag] = 0
                        self.log_success('up cheese COMMANDCENTER')
                        self.log_command('cc(AbilityId.LIFT')
                        cc(AbilityId.LIFT)
                        self.cheese3_phase = 'F'
            elif self.cheese3_phase == 'F':
                # while (cc flies)
                await self.cheese3_internals()
                #clean
                if self.cheese3_barracks_tag not in (ba.tag for ba in self.structures(BARRACKS)):
                    self.cheese3_phase = 'Y'
                if self.cheese3_cc_tag not in (cc.tag for cc in self.structures(COMMANDCENTER)):
                    if self.cheese3_cc_tag not in (cc.tag for cc in self.structures(COMMANDCENTERFLYING)):
                        self.cheese3_phase = 'Y'
                # continue
                for cc in self.structures(COMMANDCENTER).ready:
                    if (cc.tag == self.cheese3_cc_tag) and (cc.position != self.cheese3_cc_pos):
                        # init (cc landed)
                        cc(AbilityId.RALLY_BUILDING,self.cheese3_prison_pos)
                        self.throw_at_spot(PLANETARYFORTRESS,cc.position,'do_pf_rush',1)
                        self.cheese3_phase = 'G'
            elif self.cheese3_phase == 'G':
                # while (cc landed)
                await self.cheese3_internals()
                #clean
                if self.cheese3_cc_tag not in (cc.tag for cc in self.structures(COMMANDCENTER)):
                    if self.cheese3_cc_tag not in (cc.tag for cc in self.structures(COMMANDCENTERFLYING)):
                        self.cheese3_phase = 'Y'
                # continue
                if (self.cheese3_cc_tag in (cc.tag for cc in self.structures(PLANETARYFORTRESS).ready)):
                    # init (pf ready)
                    self.cheese3_phase = 'H'
            elif self.cheese3_phase == 'H':
                # while (pf ready)
                await self.cheese3_internals()
                #clean
                if self.cheese3_cc_tag not in (cc.tag for cc in self.structures(PLANETARYFORTRESS)):
                    self.cheese3_phase = 'Y'
                # make
                for cc in self.structures(PLANETARYFORTRESS).ready.idle:
                    if cc.tag == self.cheese3_cc_tag:
                        if self.wantscv():
                            if self.can_pay(SCV):
                                cc.train(SCV)
                # continue
            elif self.cheese3_phase == 'Y':
                # clean up the cheese
                for ba in self.structures(BARRACKS):
                    if ba.tag == self.cheese3_barracks_tag:
                        if ba not in self.structures(BARRACKS).ready:
                            self.log_command('ba(AbilityId.CANCEL)')
                            ba(AbilityId.CANCEL)
                        if ba in self.structures(BARRACKS).ready:
                            if self.find_tobuildwalk_a_place(BARRACKS):
                                goal = self.function_result_Point2
                                self.write_layout(BARRACKS, goal)
                                if not ba.is_idle:
                                    self.log_command('ba(AbilityId.CANCEL)')
                                    ba(AbilityId.CANCEL)
                                self.goal_of_flying_struct[ba.tag] = goal
                                self.landings_of_flying_struct[ba.tag] = 0
                                self.log_success('move cheese BARRACKS')
                                self.log_command('ba(AbilityId.LIFT')
                                ba(AbilityId.LIFT)
                for ba in self.structures(BARRACKSFLYING):
                    if ba.tag == self.cheese3_barracks_tag:
                        if self.find_tobuildwalk_a_place(BARRACKS):
                            goal = self.function_result_Point2
                            self.write_layout(BARRACKS, goal)
                            self.goal_of_flying_struct[ba.tag] = goal
                            self.landings_of_flying_struct[ba.tag] = 0
                            self.log_success('move cheese BARRACKS')
                for cc in self.structures(COMMANDCENTER):
                    if cc.tag == self.cheese3_cc_tag:
                        if cc not in self.structures(COMMANDCENTER).ready:
                            self.log_command('cc(AbilityId.CANCEL)')
                            cc(AbilityId.CANCEL)
                    if cc in self.structures(COMMANDCENTER).ready:
                        if self.find_tobuildwalk_a_place(COMMANDCENTER):
                            goal = self.function_result_Point2
                            self.write_layout(COMMANDCENTER, goal)
                            if not cc.is_idle:
                                self.log_command('cc(AbilityId.CANCEL)')
                                cc(AbilityId.CANCEL)
                            self.goal_of_flying_struct[cc.tag] = goal
                            self.landings_of_flying_struct[cc.tag] = 0
                            self.log_success('move cheese COMMANDCENTER')
                            self.log_command('cc(AbilityId.LIFT')
                            cc(AbilityId.LIFT)
                for cc in self.structures(COMMANDCENTERFLYING):
                    if cc.tag == self.cheese3_cc_tag:
                        if self.find_tobuildwalk_a_place(COMMANDCENTER):
                            goal = self.function_result_Point2
                            self.write_layout(COMMANDCENTER, goal)
                            if not cc.is_idle:
                                self.log_command('cc(AbilityId.CANCEL)')
                                cc(AbilityId.CANCEL)
                            self.goal_of_flying_struct[cc.tag] = goal
                            self.landings_of_flying_struct[cc.tag] = 0
                            self.log_success('move cheese COMMANDCENTER')
                self.cheese3_bunker_tag = self.notag
                self.cheese3_barracks_tag = self.notag
                self.cheese3_cc_tag = self.notag
                self.cheese3_phase = 'Z'

    ################### reapers

    def init_reaper_attack(self, expa):
        self.reaper_center = expa


    def reaper_focus_qual(self, point) -> int:
        qual = 0
        relevant = False
        for mim in self.mineral_field:
            if self.near(mim.position, point, 6):
                relevant = True
        if relevant:
            qual += 100
        # could shun spines
        return qual

    def get_terrain_force(self, point):
        # -> self.forcex, self.forcey
        # forcefield method
        # neglect individual forces under 0.01
        fx = 0
        fy = 0
        # objects
        # pylon radius 1.5, touch power 100, at d=2.5 power=1, at d=4 power=0.16
        for ene in self.enemy_structures:
            if self.near(ene.position, point, 10):  # restrict work
                dist = max(0.1, self.circledist(ene.position, point) - ene.radius)  # minimum distance 0.1
                unit_power = 1 / (dist * dist)  # max 100
                fx = fx + (point.x - ene.position.x) * unit_power
                fy = fy + (point.y - ene.position.y) * unit_power
        # edge
        # touch power 25, radius 0.5
        # at d=1.5 power=1.56
        # at d=4 power=0.09
        aroundx = round(point.x)
        aroundy = round(point.y)
        for x in range(aroundx-10,aroundx+10):
            for y in range(aroundy-10,aroundy+10):
                if self.read_layout(x,y) not in [0,2]:
                    square = Point2((x + 0.5,y + 0.5))
                    dist = max(0.2, self.circledist(square, point) - 0.7)  # minimum distance 0.2
                    unit_power = 1 / (dist * dist)  # max 25
                    fx = (point.x - fx + square.x) * unit_power
                    fy = (point.y - fy + square.y) * unit_power
        self.forcex = fx
        self.forcey = fy

    def terrain_signature(self) -> int:
        sig = 0
        for tag in self.enemy_buidings_permanent:
            sig += tag
        return sig

    def get_terrain_compensator(self, point):
        # -> self.compensatorx, self.compensatory
        # Free oval
        # The reaper should be able to move around reaper_center freely
        # At each angle, somewhere between 3 and 9 should be a point without perpendicular force
        # Find the minimum perpedicular force component over that linesegment and compensate it.
        # (could use angle to look up a precomputed value as long as the near buildings did not change)
        d = self.circledist(point, self.reaper_center)
        perpx = (point.y - self.reaper_center.y) / d # x and y mix is correct
        perpy = - (point.x - self.reaper_center.x) / d # x and y mix is correct
        vecx = (point.x - self.reaper_center.x) / d
        vecy = (point.y - self.reaper_center.y) / d
        signature = self.terrain_signature()
        if vecy >= 0:
            alfa = acos(vecx)
        else: # 0 <= alfa < 2*pi
            alfa = 2 * pi - acos(vecx)
        remembered = False    
        alfasegment = round(alfa * 32) # 0 <= alfasegment < 202
        if alfasegment in self.remember_terrain:
            (compx, compy, sig) = self.remember_terrain[alfasegment]
            if sig == signature:
                remembered = True
                self.compensatorx = compx
                self.compensatory = compy
        if not remembered:    
            best_perppart = 99999
            for pog in range(0,30):
                newdist = self.reaper_ideal_dist + 6 * pog / 30 - 3
                segmentpointx = self.reaper_center.x + newdist * vecx
                segmentpointy = self.reaper_center.y + newdist * vecy
                segmentpoint = Point2((segmentpointx,segmentpointy))
                self.get_terrain_force(segmentpoint)
                inproduct = self.forcex * perpx + self.forcey * perpy
                perppart = inproduct * inproduct
                if perppart < best_perppart:
                    best_perppart = perppart
                    best_inproduct = inproduct
            self.compensatorx = - perpx * best_inproduct
            self.compensatory = - perpy * best_inproduct
            self.remember_terrain[alfasegment] = (self.compensatorx, self.compensatory, signature)

    def get_reaper_micro_advice(self, reaper):
        # -> self.advice_text: 'run'
        # -> self.advice_goal: Point2
        mypoint = reaper.position
        self.get_terrain_compensator(mypoint) # beware, this overwrites self.forcex
        self.get_terrain_force(mypoint)
        fx = self.forcex + self.compensatorx
        fy = self.forcey + self.compensatory
        # units
        # Stalker has dps=10. Stalker at d=10 has power 0.63.
        # Stalker in range has power 1000 (x 4 frames)
        # Drone has dps=4.67. Drone at d=4 has power 0.31
        # 10 drones at d=7 have power 0.95 (x 4 frames)
        for ene in self.enemy_units:
            if ene.can_attack_ground:
                if self.near(ene.position,mypoint,30): # restrict work
                    lastpos = ene.position
                    if ene.tag in self.last_enemies:
                        lastpos = self.last_enemies[ene.tag]
                    ene_jump = Point2((ene.position.x - lastpos.x, ene.position.y - lastpos.y))
                    ene_step = Point2((ene_jump.x / self.chosen_game_step, ene_jump.y / self.chosen_game_step))
                    for ahead in range(0, 4):  # Amount of frames in the future.
                        futureenepos = Point2((ene.position.x + ahead * ene_step.x, ene.position.y + ahead * ene_step.y))
                        dist = max(0.1,self.circledist(futureenepos,mypoint)-ene.ground_range) # minimum distance 0.1
                        unit_power = ene.ground_dps / (dist*dist)
                        fx = fx + (mypoint.x - futureenepos.x) * unit_power
                        fy = fy + (mypoint.y - futureenepos.y) * unit_power
        #
        d = self.circledist(mypoint, self.reaper_center)
        perpx = (mypoint.y - self.reaper_center.y) / d # x and y mix is correct
        perpy = - (mypoint.x - self.reaper_center.x) / d # x and y mix is correct
        vecx = (mypoint.x - self.reaper_center.x) / d
        vecy = (mypoint.y - self.reaper_center.y) / d
        # At cdist=reaper_ideal_dist, power=0
        # At cdist=reaper_ideal_dist+1, draw in 0.5
        # at cdist=reaper_ideal_dist-3, push out 13.5
        # At cdis=reaper_ideal_dist+3, draw in 13.5
        dist = self.reaper_ideal_dist - self.circledist(self.reaper_center, mypoint)
        unit_power = 0.5 * (dist * dist)
        fx = fx + vecx * unit_power * dist
        fy = fy + vecy * unit_power * dist
        # add a wish to circle
        # circlepower 0.5
        unit_power = 0.5
        fx = fx + perpx * unit_power
        fy = fy + perpy * unit_power
        # get a point dist 2*reaperstep*game_step in the force direction from mypoint
        norm = sqrt(fx * fx + fy * fy)
        wishnorm = 2 * self.reaper_step * self.chosen_game_step
        px = mypoint.x + fx * wishnorm / norm
        py = mypoint.y + fy * wishnorm / norm
        self.advice_goal = Point2((px,py))
        self.advice_text = 'run'


    def get_reaper_hit_advice(self, reaper):
        # -> self.advice_text   sometimes changed to 'hit'
        # -> self.advice_hit  is the enemy to hit then
        mypoint = reaper.position
        minlife = 99999
        for ahead in range(0,5): # Amount of frames in the future.
            futurecooldown = reaper.weapon_cooldown - ahead
            for ene in self.enemy_units:
                lastpos = ene.position
                if ene.tag in self.last_enemies:
                    lastpos = self.last_enemies[ene.tag]
                ene_jump = Point2((ene.position.x - lastpos.x, ene.position.y - lastpos.y))
                ene_step = Point2((ene_jump.x / self.chosen_game_step, ene_jump.y / self.chosen_game_step))
                futureenepos = Point2((ene.position.x + ahead * ene_step.x, ene.position.y + ahead * ene_step.y))
                if futurecooldown <= 0:
                    if ahead < 5: # a good chance of hitting
                        if self.near(mypoint, futureenepos, 5):  # official range
                            life = ene.shield + ene.health
                            if life < minlife:
                                if (not ene.is_flying):
                                    self.advice_hit = ene
                                    minlife = life
            ahead += 1
        if minlife < 99999:
            # expecting the reaper to be faster
            ene = self.advice_hit
            lastpos = ene.position
            if ene.tag in self.last_enemies:
                lastpos = self.last_enemies[ene.tag]
            ene_jump = Point2((ene.position.x - lastpos.x, ene.position.y - lastpos.y))
            ene_step = Point2((ene_jump.x / self.chosen_game_step, ene_jump.y / self.chosen_game_step))
            # get dist to estimate the ahead for a hit
            enepositionestimate = ene.position
            for improve in range(0,3):
                dist = max(0,self.circledist(mypoint,enepositionestimate) - 5)
                aheadestimate = dist / self.reaper_step
                enepositionestimate = Point2((ene.position.x + aheadestimate * ene_step.x, ene.position.y + aheadestimate * ene_step.y))
            if reaper.weapon_cooldown <= aheadestimate:
                self.advice_text = 'hit'


    def do_reaper(self):
        self.routine = 'do_reaper'
        if self.opening_name == 'reapers':
            if len(self.units(REAPER)) > 0:
                #self.slowed_down()
                # scvs building bunkers
                if len(self.structures(BUNKER)) > 0:
                    for anscv in self.units(SCV):
                        scvt = anscv.tag
                        if scvt in self.goal_of_trabu_scvt:
                            if self.goal_of_trabu_scvt[scvt] in [self.reaper_bunker1_pos,self.reaper_bunker2_pos]:
                                self.promote(anscv,'cheeser')
                                self.special_tags.add(anscv.tag)
                # reaper_focus
                old_reaper_focus = self.reaper_focus
                #
                if self.reaper_focus == self.nowhere:
                    self.reaper_focus = self.reaper_center  # self.reaper_prison_pos
                bestqual = self.reaper_focus_qual(self.reaper_focus)
                for pog in range(0,20):
                    ok = False
                    while not ok:
                        point = self.random_mappoint()
                        ok = self.near(point,self.enemy_pos, self.miner_bound)
                    qual = self.reaper_focus_qual(point)
                    if qual > bestqual:
                        bestqual = qual
                        self.reaper_focus = point
                for ene in self.enemy_units:
                    # todo if not cloacked
                    if self.near(ene.position,self.reaper_prison_pos,8):
                        self.reaper_focus = self.reaper_center #self.reaper_prison_pos
                # change focus of entering reapers
                if self.reaper_focus != old_reaper_focus:
                    for re in self.units(REAPER):
                        if re.tag in self.reaper_status:
                            if self.reaper_status[re.tag] != 'fleeing':
                                self.reaper_status[re.tag] = 'relaxing'
                # fleepos
                fleepos = self.game_info.map_center
                bestsd = self.sdist(self.reaper_focus,fleepos)
                for bun in self.structures(BUNKER).ready:
                    if len(bun.passengers) < 4:
                        sd = self.sdist(bun.position,self.reaper_focus)
                        if sd < bestsd:
                            bestsd = sd
                            fleepos = bun.position
                # steer each reaper
                for re in self.units(REAPER):
                    if re.tag not in self.reaper_status:
                        self.reaper_status[re.tag] = 'relaxing'
                    status = self.reaper_status[re.tag]
                    if re.health < self.maxhealth[re.type_id] / 4:
                        status = 'fleeing'
                        re.move(fleepos)
                    if status == 'fleeing':
                        if re.health >= 3 * self.maxhealth[re.type_id] / 4:
                            status = 'entering'
                            re.move(self.reaper_focus)
                    if status == 'hitting':
                        if re.weapon_cooldown > 6:
                            status = 'entering'
                            re.move(self.reaper_focus)
                    elif not self.near(re.position,self.reaper_center,25):
                        status = 'entering'
                        re.move(self.reaper_focus)
                    else:
                        self.get_reaper_micro_advice(re)
                        self.get_reaper_hit_advice(re)
                        if self.advice_text == 'hit':
                            re.attack(self.advice_hit)
                            status = 'hitting'
                        elif self.advice_text == 'run':
                            re.move(self.advice_goal)
                            status = 'running'
                    self.reaper_status[re.tag] = status
                    # logging:
                    self.log_success('reaper '+str(re.tag)+self.txt(re.position)+' health '+str(re.health)+' '+status+' '+str(re.weapon_cooldown))


    async def do_cocoon(self):
        self.routine = 'do_cocoon'
        if self.opening_name == 'cocoon':
            if self.cheese3_phase == 'A':
                # while (nothing)
                # continue
                for ba in self.structures(BARRACKS):
                    if ba.position == self.cheese3_barracks_pos:
                        # init (barracks is constructing)
                        self.cheese3_barracks_tag = ba.tag
                        self.special_tags.add(ba.tag)
                        ba(AbilityId.RALLY_BUILDING, self.cheese3_prison_pos)
                        self.cheese3_phase = 'B'
                    if ba.position == self.cheese3_barracks2_pos:
                        # init (barracks is constructing)
                        self.cheese3_barracks2_tag = ba.tag
                        self.special_tags.add(ba.tag)
                        ba(AbilityId.RALLY_BUILDING, self.cheese3_prison_pos)
                        self.cheese3_phase = 'C'
            elif self.cheese3_phase == 'B':
                # while (nothing)
                # continue
                for ba in self.structures(BARRACKS):
                    if ba.position == self.cheese3_barracks2_pos:
                        # init (barracks is constructing)
                        self.cheese3_barracks2_tag = ba.tag
                        self.special_tags.add(ba.tag)
                        ba(AbilityId.RALLY_BUILDING, self.cheese3_prison_pos)
                        self.cheese3_phase = 'D'
            elif self.cheese3_phase == 'C':
                # while (nothing)
                # continue
                for ba in self.structures(BARRACKS):
                    if ba.position == self.cheese3_barracks_pos:
                        # init (barracks is constructing)
                        self.cheese3_barracks_tag = ba.tag
                        self.special_tags.add(ba.tag)
                        ba(AbilityId.RALLY_BUILDING, self.cheese3_prison_pos)
                        self.cheese3_phase = 'D'
            elif self.cheese3_phase == 'D':
                # while (barracks is constructing)
                #clean
                if self.cheese3_barracks_tag not in (ba.tag for ba in self.structures(BARRACKS)):
                    self.cheese3_phase = 'Y'
                if self.cheese3_barracks2_tag not in (ba.tag for ba in self.structures(BARRACKS)):
                    self.cheese3_phase = 'Y'
                # continue
                if len(self.structures(BUNKER).ready) >= 2:
                    self.cheese3_phase = 'E'
            elif self.cheese3_phase == 'E':
                # while (emptying barracks)
                # clean
                # continue
                for ba in self.structures(BARRACKS).ready.idle:
                    if ba.tag == self.cheese3_barracks_tag:
                        if self.find_tobuildwalk_a_place(BARRACKS):
                            goal = self.function_result_Point2
                            self.write_layout(BARRACKS, goal)
                            self.goal_of_flying_struct[ba.tag] = goal
                            self.landings_of_flying_struct[ba.tag] = 0
                            self.log_success('move cheese BARRACKS')
                            self.log_command('ba(AbilityId.LIFT')
                            ba(AbilityId.LIFT)
                            self.cheese3_barracks_tag = self.notag
                            self.cheese3_phase = 'F'
            elif self.cheese3_phase == 'F':
                # while (factory, tank constructing)
                # clean
                if len(self.structures(BUNKER).ready) == 0:
                    self.cheese3_phase = 'Y'
                # continue
                if len(self.units(SIEGETANK)) > 0:
                    # init (siegetank going)
                    for tnk in self.units(SIEGETANK):
                        self.special_tags.add(tnk.tag)
                        self.go_attack(tnk,self.cheese3_prison_pos)
                    self.cheese3_phase = 'G'
            elif self.cheese3_phase == 'G':
                # while (siegetank going)
                # clean
                if len(self.structures(BUNKER).ready) == 0:
                    self.cheese3_phase = 'Y'
                # continue
                for tnk in self.units(SIEGETANK):
                    if tnk.tag in self.special_tags:
                        if self.no_move(tnk,32):
                            self.log_command('tnk(AbilityId.SIEGEMODE_SIEGEMODE)')
                            tnk(AbilityId.SIEGEMODE_SIEGEMODE)
                            self.cheese3_phase = 'Y'
            elif self.cheese3_phase == 'Y':
                # clean up the cheese
                for scv in self.units(SCV):
                    scvt = scv.tag
                    if self.job_of_scvt[scvt] == 'cheeser':
                        self.promote(scv,'fleeer') # includes move
                for ba in self.structures(BARRACKS):
                    if ba.tag in [self.cheese3_barracks_tag,self.cheese3_barracks2_tag]:
                        if ba not in self.structures(BARRACKS).ready:
                            self.log_command('ba(AbilityId.CANCEL)')
                            ba(AbilityId.CANCEL)
                        if ba in self.structures(BARRACKS).ready:
                            if self.find_tobuildwalk_a_place(BARRACKS):
                                goal = self.function_result_Point2
                                self.write_layout(BARRACKS, goal)
                                if not ba.is_idle:
                                    self.log_command('ba(AbilityId.CANCEL)')
                                    ba(AbilityId.CANCEL)
                                self.goal_of_flying_struct[ba.tag] = goal
                                self.landings_of_flying_struct[ba.tag] = 0
                                self.log_success('move cheese BARRACKS')
                                self.log_command('ba(AbilityId.LIFT')
                                ba(AbilityId.LIFT)
                for ba in self.structures(BARRACKSFLYING):
                    if ba.tag in [self.cheese3_barracks_tag,self.cheese3_barracks2_tag]:
                        if self.find_tobuildwalk_a_place(BARRACKS):
                            goal = self.function_result_Point2
                            self.write_layout(BARRACKS, goal)
                            self.goal_of_flying_struct[ba.tag] = goal
                            self.landings_of_flying_struct[ba.tag] = 0
                            self.log_success('move cheese BARRACKS')
                self.cheese3_bunker_tag = self.notag
                self.cheese3_barracks_tag = self.notag
                self.cheese3_bunker2_tag = self.notag
                self.cheese3_barracks2_tag = self.notag
                self.cheese3_phase = 'Z'




    def get_shield_pos(self):
        self.routine = 'get_shield_pos'
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
                                self.chosenplaces.append((INFESTEDBUNKER, goodpoint))
                                self.write_layout(BUNKER, goodpoint)
                                keep.append(goodpoint)
                                found += 1
        self.erase_layout(BUNKER,self.cheese_bunker_pos)
        self.erase_layout(ARMORY,self.cheese_landing_pos)
        self.erase_layout(BUNKER,keep[0])
        self.erase_layout(BUNKER,keep[1])

    #*********************************************************************************************************************
    def place_around(self, building, anchor) -> Point2:
        altpoint = self.put_on_the_grid(building, anchor)
        ok = self.check_layout(building, altpoint)
        tries = 0
        radius = 0
        around = altpoint
        while (not ok):
            if tries == radius * radius:
                radius += 1
            tries += 1
            x = around.x + random.randrange(-radius, radius)
            y = around.y + random.randrange(-radius, radius)
            altpoint = Point2((x, y))
            ok = self.check_layout(building, altpoint)
        return altpoint

    async def lift(self):
#       attacked buildings can fly, survive, be repaired, and land back.
        self.routine = 'lift'
        for srt in self.landable:
            basekind = self.basekind_of(srt)
            for bu in self.structures(srt).ready.idle:
                if bu.health >= self.maxhealth[bu.type_id]-100:
                    goal = self.goal_of_flying_struct[bu.tag]
                    # unburrow widowines
                    if self.near(bu.position, goal, 9):
                        for wm in self.units(WIDOWMINEBURROWED):
                            if self.near(wm.position, goal, 3):
                                self.log_command('wm(AbilityId.BURROWUP_WIDOWMINE)')
                                wm(AbilityId.BURROWUP_WIDOWMINE)
                                self.goal_of_unittag[wm.tag] = wm.position.towards(self.loved_pos, 4)
                    # land (or move to landing spot)
                    if self.near(bu.position,goal,4):
                        # land
                        if self.landings_of_flying_struct[bu.tag] > 5:
                            # try another landing place
                            self.landings_of_flying_struct[bu.tag] = 0
                            newpoint = self.place_around(basekind,goal)
                            self.goal_of_flying_struct[bu.tag] = newpoint
                        self.log_success('down '+srt.name)
                        self.log_command('bu(AbilityId.LAND,self.goal_of_flying_struct[bu.tag])')
                        bu(AbilityId.LAND,self.goal_of_flying_struct[bu.tag])
                        self.landings_of_flying_struct[bu.tag] += 1
                    else: # not near goal
                        bu.move(self.goal_of_flying_struct[bu.tag])
                elif not self.near(self.shipyard,bu.position,7):
                    self.log_command('bu(AbilityId.MOVE_MOVE,self.shipyard)')
                    bu(AbilityId.MOVE_MOVE,self.shipyard)
        for srt in self.liftable:
            for bu in self.structures(srt).ready:
                # early goal makes goal overwritable before lifting
                if bu.tag not in self.goal_of_flying_struct:
                    self.goal_of_flying_struct[bu.tag] = bu.position 
                if bu.health < 500:
                    if bu.tag not in self.special_tags:
                        if not bu.is_idle:
                            self.log_command('bu(AbilityId.CANCEL)')
                            bu(AbilityId.CANCEL)
                        self.landings_of_flying_struct[bu.tag] = 0
                        self.log_success('up '+srt.name)
                        self.log_command('bu(AbilityId.LIFT')
                        bu(AbilityId.LIFT)
        #       fly in the cheese
        if self.opening_name in ['cheese-bc','cheese-expand','cheese-bunk']:
            for ba in self.structures(BARRACKS).ready:
                if ba.position == self.cheese_barracks_pos:
                    self.goal_of_flying_struct[ba.tag] = self.cheese_landing_pos
                    self.landings_of_flying_struct[ba.tag] = 0
                    self.log_success('up cheese-BARRACKS')
                    self.log_command('ba(AbilityId.LIFT)')
                    ba(AbilityId.LIFT)
                    # it will try to land itself


    async def manage_the_wall(self):
        self.routine = 'manage_the_wall'
        havehome = False
        for cc in self.all_bases:
            if cc.position == self.loved_pos:
                havehome = True
        if self.wall == set():
            self.wall.add((BARRACKS, self.wall_barracks_pos))
            self.wall.add((SUPPLYDEPOT, self.wall_depot0_pos))
            self.wall.add((SUPPLYDEPOT, self.wall_depot1_pos))
        if havehome:
            for (struc_type,position) in self.wall:
                seen = False
                for struc in self.structures(struc_type) + self.structures(SUPPLYDEPOTLOWERED):
                    if (struc.position == position):
                        seen = True
                        self.special_tags.add(struc.tag)
                if not seen:
                    if (struc_type, position) not in self.chosenplaces:
                        self.chosenplaces.append((struc_type, position))
        # up down depots
        for sd in self.structures(SUPPLYDEPOTLOWERED).ready + self.structures(SUPPLYDEPOT).ready:
            if (SUPPLYDEPOT,sd.position) in self.wall:
                danger = False
                for ene in self.enemy_units:
                    if self.near(ene.position,sd.position,5):
                        if not ene.is_flying:
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
                if danger:
                    for ba in self.structures(BARRACKS):
                        if ba.position == self.wall_barracks_pos:
                            if ba.tag in self.idle_structure_tags:
                                if self.can_pay(MARINE):
                                    if self.supply_check(MARINE):
                                        self.log_command('ba.train(MARINE)')
                                        ba.train(MARINE)
                                        self.idle_structure_tags.remove(ba.tag)


    def lower_some_depots(self):
        for sd in self.structures(SUPPLYDEPOT):
            expo = self.expo_of_pos(sd.position)
            near = False
            for mim in self.minerals_of_expo[expo]:
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


    async def destroyed(self):
        self.routine = 'destroyed'
        for stru in self.structures:
            if stru.tag in self.last_health:
                if stru.health < 0.67 * self.last_health[stru.tag]:
                    stru(AbilityId.CANCEL)


    async def deserted(self):
        self.routine = 'deserted'
        for s in self.structures_without_construction_SCVs():
            place = s.position
            if not self.proxy(place):
                if s.health < 0.5 * self.maxhealth[s.type_id]:
                    self.log_command(s.name+'(AbilityId.CANCEL)')
                    s(AbilityId.CANCEL)
                else:
                    if self.frame % 71 == 70:
                        scvt = self.get_near_scvt_to_goodjob(place)
                        for scv in self.units(SCV):
                            if scv.tag == scvt:
                                if self.near(scv.position,place,15):
                                    self.promote(scv,'builder')
                                    self.log_command('scv(AbilityId.SMART,s)')
                                    scv(AbilityId.SMART,s)
                                    self.structure_of_trabu_scvt[scvt] = s.type_id
                                    self.goal_of_trabu_scvt[scvt] = place



#*********************************************************************************************************************
# worker routines

    def wantscv(self) -> bool:
        wa = True
        flyingccs = len(self.structures(COMMANDCENTERFLYING)) + len(self.structures(ORBITALCOMMANDFLYING))
        if self.count_of_job['idler']  + self.count_of_job['volunteer'] >= 11 + 16 * flyingccs:
            wa = False
        if len(self.all_scvt) - self.count_of_job['suicider'] >= 100 - ((self.vespene + self.minerals) / 150):
            wa = False
        return wa

    def hatescv(self) -> bool:
        ha = False
        if self.count_of_job['idler']  + self.count_of_job['volunteer'] >= 21:
            ha = True
        if len(self.all_scvt) - self.count_of_job['suicider'] >= 110 - ((self.vespene + self.minerals) / 150):
            ha = True
        return ha

    def reserve_for_orbitals(self) -> bool:
        toreserve = 0
        orbitals = True
        for bu in self.buildseries_exe:
            if bu == ORBITALCOMMAND:
                if orbitals:
                    toreserve += 150
            else:
                orbitals = False
        return self.minerals >= toreserve + 50


    async def build_worker(self,amount):
        self.routine = 'build_worker'
        # ignore self.already_pending(SCV) as it is slow
        if self.count_of_job['idler'] + self.count_of_job['volunteer'] > 1: # allow new scv temporary idler
            # try oc first
            todo = 1
            for cc in self.structures(COMMANDCENTER):
                if cc.tag in self.idle_structure_tags:
                    if cc.position in self.cc_destiny:
                        if self.cc_destiny[cc.position] == 'oc':
                            if self.can_pay(ORBITALCOMMAND):
                                if todo > 0:
                                    todo -= 1
                                    self.throw_at_spot(ORBITALCOMMAND, cc.position, 'build_worker', 1)
        # new scv
        todo = amount - self.units(SCV).amount
        todo = min(todo,self.supply_left)
        if todo > 0:
            todo = 1 # max 1 per frame
            if self.wantscv():
                pause = False
                for (th, am, bu, bam) in self.production_pause:
                    if th == SCV:
                        if self.we_finished_amount(bu) < bam:
                            if self.we_started_amount(th) >= am:
                                pause = True
                if not pause:
                    for cc in self.all_bases:
                        if cc.tag in self.idle_structure_tags: # skipping gym
                            if cc.tag not in (self.ambition_of_strt.keys() | self.gym_of_strt.keys()):
                                # always urgent
                                if self.can_pay(SCV):
                                    if cc.tag in self.last_health:
                                        if cc.health >= self.last_health[cc.tag]:
                                            if self.reserve_for_orbitals():
                                                if todo > 0:
                                                    if self.no_doubling(cc.tag):
                                                        todo -= 1
                                                        self.log_workers('')
                                                        self.log_command('cc.train(SCV)')
                                                        dummy = cc.train(SCV)
                                                        self.idle_structure_tags.remove(cc.tag)


    #######################################################################################

    async def mules(self):
        for oc in self.structures(ORBITALCOMMAND).ready:
            if oc.energy >= 50:
                if len(self.mineral_field) > 0:
                    bestqual = -99999
                    pog = 0
                    while (pog < 80):
                        pog += 1
                        mim = random.choice(self.mineral_field)
                        itssd = 99999
                        for kind in [COMMANDCENTER,ORBITALCOMMAND,PLANETARYFORTRESS]:
                            for cc in self.structures(kind).ready:
                                sd = self.sdist(cc.position,mim.position)
                                itssd = min(itssd,sd)
                        itsqual = self.simpledist(mim.position,self.loved_pos) - itssd
                        if itsqual > bestqual:
                            bestqual = itsqual
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
        self.job_of_scvt[scvt] = new_job
        self.log_workers('promoted ' + old_job + ' to ' + new_job + ' ' + self.name(scvt))
        if new_job == 'fleeer':
            place = self.random_mappoint()
            self.log_command('scv(AbilityId.MOVE_MOVE,place)')
            scv(AbilityId.MOVE_MOVE, place)
        # for other new_job, code elsewhere


    def do_repair(self):
        self.routine = 'do_repair'
        # If something needs repair, promote someone to repairer
        if len(self.thingtag_of_repairertag) * 2 < len(self.units(SCV)) - 6:
            low_qual = 1.0
            wreck = self.notag
            for strtype in self.all_repairable_shooters:
                for s in self.structures(strtype).ready + self.units(strtype):
                    handable = True
                    if (strtype == BATTLECRUISER):
                        for order in s.orders:
                            if order.ability.id == AbilityId.EFFECT_TACTICALJUMP:
                                handable = False
                    if handable:
                        qual = s.health / self.maxhealth[s.type_id]
                        if qual < low_qual:
                            expo = self.expo_of_pos(s.position)
                            hasrepairers = 0
                            for reptag in self.thingtag_of_repairertag:
                                thitag = self.thingtag_of_repairertag[reptag]
                                if thitag == s.tag:
                                    hasrepairers += 1
                            couldhaverep = False
                            for scv in self.scvs_of_expo[expo]:
                                scvt = scv.tag
                                job = self.job_of_scvt[scvt]
                                if (job in (self.bad_jobs + self.no_jobs)) or (job == 'cheeser'):
                                    if scvt not in self.thingtag_of_repairertag:
                                        couldhaverep = True
                            if (hasrepairers < 5) and (couldhaverep):
                                low_qual = qual
                                wreck = s
                                wreckexpo = expo
            # if no wreck then repair a simple building
            if low_qual == 1.0:
                for s in self.structures.ready:
                    if s.type_id not in self.all_repairable_shooters:
                        if s.type_id != BARRACKSFLYING:
                            qual = s.health / self.maxhealth[s.type_id]
                            if qual < low_qual:
                                expo = self.expo_of_pos(s.position)
                                hasrepairers = 0
                                for reptag in self.thingtag_of_repairertag:
                                    thitag = self.thingtag_of_repairertag[reptag]
                                    if thitag == s.tag:
                                        hasrepairers += 1
                                couldhaverep = False
                                for scv in self.scvs_of_expo[expo]:
                                    scvt = scv.tag
                                    job = self.job_of_scvt[scvt]
                                    if (job in (self.bad_jobs + self.no_jobs)) or (job == 'cheeser'):
                                        if scvt not in self.thingtag_of_repairertag:
                                            couldhaverep = True
                                if (hasrepairers < 1) and (couldhaverep):
                                    low_qual = qual
                                    wreck = s
                                    wreckexpo = expo
            if low_qual < 0.99:
                # We have a wreck needing repair. Assign one repairer.
                scvt = self.get_near_scvt_to_goodjob(wreck.position)
                for scv in self.scvs_of_expo[wreckexpo]:
                    cheesertag = scv.tag
                    if self.job_of_scvt[cheesertag] == 'cheeser':
                        if not scv.is_constructing_scv:
                            if cheesertag not in self.thingtag_of_repairertag:
                                scvt = cheesertag
                for scv in self.scvs_of_expo[wreckexpo]:
                    if scv.tag == scvt:
                        if self.job_of_scvt[scvt] != 'cheeser':
                            self.promote(scv,'repairer')
                        self.thingtag_of_repairertag[scv.tag] = wreck.tag
                        #self.log_command('scv.repair('+wreck.name+')')
                        #scv.repair(wreck)
                        scv(AbilityId.EFFECT_REPAIR_SCV,wreck)
                        # do not have repairers trailing vikings
                        if wreck in self.units:
                            wreck.move(scv.position)
        # logging
        count_of_thing = {}
        for reptag in self.thingtag_of_repairertag:
            thitag = self.thingtag_of_repairertag[reptag]
            if thitag in count_of_thing:
                count_of_thing[thitag] += 1
            else:
                count_of_thing[thitag] = 1
        for s in self.structures.ready + self.units:
            if s.tag in count_of_thing:
                self.log_success('repairing a '+s.type_id.name+' with '+str(count_of_thing[s.tag]))


    async def manage_workers(self):
        self.routine = 'manage_workers'
        # heaven
        heaven = set()
        maxsafety = -99999
        for expo in range(0,self.expos):
            safety = self.ground_strength_of_expo[expo]
            if safety > maxsafety:
                heaven = {expo}
                maxsafety = safety
            elif safety == maxsafety:
                heaven.add(expo)
        #
        #  applicant was walking to a cc with a problem
        for scvt in self.all_scvt:
            if self.job_of_scvt[scvt] == 'applicant':
                if scvt not in self.vision_of_scvt:
                    for scv in self.units(SCV):
                        if scv.tag == scvt:
                            self.promote(scv,'idler')
        #
        for scv in self.units(SCV):
            scvt = scv.tag
            job = self.job_of_scvt[scvt]
            # panic
            if job in ['gasminer','mimminer']:
                panic = True
                for tow in self.all_bases:
                    if self.near(scv.position,tow.position,self.miner_bound):
                        panic = False
                if panic:
                    self.promote(scv,'fleeer') # includes move
            # builders start to mine after building a geyser
            if job == 'builder':
                if scv.is_collecting:
                    gast = self.get_near_gast_free(scv.position)
                    for gas in self.all_refineries:
                        if gas.tag == gast:
                            self.promote(scv,'gasminer')
                            await self.be_gasminer(scv,gas)
            # not lazy
            if scvt in self.lazyness_of_scvt:
                if not scv.is_idle:
                    del self.lazyness_of_scvt[scvt]
        #
        # idle scvs:
        for scv in self.units(SCV).idle:
            scvt = scv.tag
            job = self.job_of_scvt[scvt]
            expo = self.expo_of_pos(scv.position)
            # fleeer runs to heaven
            if job == 'fleeer':
                if expo not in heaven:
                    place = self.random_mappoint()
                    while self.expo_of_pos(place) not in heaven:
                        place = self.random_mappoint()
                    self.log_command('scv(AbilityId.MOVE_MOVE,place)')
                    scv(AbilityId.MOVE_MOVE, place)
            # may not idle
            if job not in self.jobs_may_idle:
                if scvt in self.lazyness_of_scvt:
                    self.lazyness_of_scvt[scvt] += self.chosen_game_step
                    if self.lazyness_of_scvt[scvt] >= self.gracetime:
                        if job == 'inshock':
                            self.promote(scv,'fleeer') # includes move
                        else:
                            self.promote(scv,'idler')
                else:
                    self.lazyness_of_scvt[scvt] = self.chosen_game_step
            if job == 'traveller':
                if not self.near(scv.position,self.goal_of_trabu_scvt[scvt],3):
                    # the traveller has been blocked
                    self.log_command('scv(AbilityId.MOVE_MOVE,self.goal_of_trabu_scvt[scvt])')
                    scv(AbilityId.MOVE_MOVE,self.goal_of_trabu_scvt[scvt])
            if job == 'applicant':
                cct = self.vision_of_scvt[scvt]
                for cc in self.all_bases:
                    if cc.tag == cct:
                        employment = cc.position.towards(self.game_info.map_center, -3)
                        if not self.near(scv.position,employment,3):
                            # the applicant has been blocked
                            self.log_command('scv(AbilityId.MOVE_MOVE,employment)')
                            scv(AbilityId.MOVE_MOVE,employment)
            if job == 'gasper':
                self.promote(scv, 'idler')
        #
        #
        # scout1 please
        if (self.scout1_tag == self.notag) and (len(self.structures) >= 3):
            scvt = self.get_near_scvt_to_goodjob(self.enemy_pos)
            for scv in self.units(SCV):
                if scv.tag == scvt:
                    self.promote(scv,'scout')
                    # mark it and start running around
                    self.scout1_tag = scvt
                    self.scout1_pole = 0
                    self.go_move(scv,self.scout1_pos[0])
        # scout2 please
        if (self.scout2_tag == self.notag) and (len(self.structures) >= 8):
            scvt = self.get_near_scvt_to_goodjob(self.loved_pos)
            for scv in self.units(SCV):
                if scv.tag == scvt:
                    self.promote(scv,'scout')
                    # mark it and start running around
                    self.scout2_tag = scvt
                    self.scout2_pole = 0
                    self.go_move(scv,self.scout2_pos[0])
        # expansionblocker
        if self.game_choice[51]:
            if not self.rushopening: # that would be a bad combination
                if (self.blocker_tag == self.notag):
                    self.blocker_tag = self.get_near_scvt_to_goodjob(self.enemy_pos)
                    for scv in self.units(SCV):
                        if scv.tag == self.blocker_tag:
                            self.promote(scv, 'scout')
                            self.blocker_pole = 0
                            scv.move(self.blocker_pos[0])


    def blocker(self):
        if self.game_choice[51]:
            for scv in self.units(SCV):
                if scv.tag == self.blocker_tag:
                    self.blocker_pole = (self.blocker_pole + self.chosen_game_step) % len(self.blocker_pos)
                    goal = self.blocker_pos[self.blocker_pole]
                    # high APM command not logged
                    scv.move(goal)
                    if self.blocker_pole < self.chosen_game_step:
                        for ene in self.enemy_structures:
                            if self.near(ene.position,self.enemy_expand_pos,5):
                                self.next_blocker()

    def init_blocker(self):
        self.enemy_expansions = []
        self.enemy_expand_pos = self.enemy_pos
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
        self.make_circle(96)
        for point in self.circle:
            self.blocker_pos.append(Point2((self.enemy_expand_pos.x+4*point.x,self.enemy_expand_pos.y+4*point.y)))


    def search_applicants(self):
        self.routine = 'search_applicants'
        candidates = set()
        for scv in self.units(SCV):
            scvt = scv.tag
            job = self.job_of_scvt[scvt]
            if (job in self.no_jobs):
                candidates.add(scv)
        total_wish = 0
        for cc in self.all_bases:
            total_wish = total_wish + self.wanted_of_cct[cc.tag]
        if total_wish < len(candidates):
            for cc in self.all_bases:
                employment = cc.position.towards(self.game_info.map_center,-3)
                while self.wanted_of_cct[cc.tag] > 0:
                    self.wanted_of_cct[cc.tag] -= 1
                    scvt = self.get_near_scvt_nojob(employment)
                    for scv in self.units(SCV):
                        if scv.tag == scvt:
                            self.promote(scv,'applicant')
                            self.log_command('scv(AbilityId.MOVE_MOVE,employment)')
                            scv(AbilityId.MOVE_MOVE,employment)
                            self.vision_of_scvt[scvt] = cc.tag
        else:
            for scv in candidates:
                scvt = scv.tag
                cct = self.get_near_cct_wanted(scv.position)
                for cc in self.all_bases:
                    if cc.tag == cct:
                        employment = cc.position.towards(self.game_info.map_center, -3)
                        self.wanted_of_cct[cc.tag] -= 1
                        self.promote(scv,'applicant')
                        self.log_command('scv(AbilityId.MOVE_MOVE,employment)')
                        scv(AbilityId.MOVE_MOVE,employment)
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
            candidates = set()
            for scv in self.units(SCV):
                scvt = scv.tag
                job = self.job_of_scvt[scvt]
                if (job in self.no_jobs) or (job == 'applicant'):
                    candidates.add(scv)
            if vacatures < len(candidates):
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
                for scv in candidates:
                    scvt = scv.tag
                    gast = self.get_near_gast_free(scv.position)
                    for gas in self.all_refineries:
                        if gas.tag == gast:
                            if self.near(scv.position,gas.position,self.miner_bound):
                                self.promote(scv,'gasminer')
                                await self.be_gasminer(scv,gas)
        self.log_gasminer()
        # after we tried local miner hiring, want applicants
        if self.mimminer_vacatures()+self.gasminer_vacatures() > len(self.vision_of_scvt):
            self.wanted_of_cct = {}
            for cc in self.all_bases:
                self.wanted_of_cct[cc.tag] = 0
                expo = self.expo_of_pos(cc.position)
                # per gast: 3 - existing workers
                for gas in self.vespene_of_expo[expo]:
                    gast = gas.tag
                    if gast in self.all_gast:
                        self.wanted_of_cct[cc.tag] += (3 - self.count_of_gast[gast])
            # decrease self.wanted_of_cct for walking applicants
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
            # new mim-mineral connections
            candidates = set()
            for scv in self.units(SCV):
                scvt = scv.tag
                job = self.job_of_scvt[scvt]
                if (job in self.no_jobs) or (job == 'applicant'):
                    candidates.add(scv)
            if vacatures < len(candidates):
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
                for scv in candidates:
                    scvt = scv.tag
                    mimt = self.get_near_mimt_free(scv.position)
                    for mim in self.mineral_field:
                        if mim.tag == mimt:
                            if self.near(scv.position,mim.position,self.miner_bound):
                                self.promote(scv,'mimminer')
                                await self.be_mimminer(scv,mim)
        # after we tried local miner hiring, want applicants
        if self.mimminer_vacatures()+self.gasminer_vacatures() > len(self.vision_of_scvt):
            self.wanted_of_cct = {}
            for cc in self.all_bases:
                self.wanted_of_cct[cc.tag] = 0
                expo = self.expo_of_pos(cc.position)
                # per mimt: 2 - existing workers
                for mim in self.minerals_of_expo[expo]:
                    mimt = mim.tag
                    if mimt in self.all_mimt:
                        self.wanted_of_cct[cc.tag] += (2 - self.count_of_mimt[mimt])
            # decrease self.wanted_of_cct for walking applicants
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
        #
        #  max idle workers
        if self.hatescv():
            todo = 1
            for scv in self.units(SCV):
                scvt = scv.tag
                if scvt in self.all_scvt:
                    if self.job_of_scvt[scvt] in self.no_jobs:
                        if todo > 0:
                            todo -= 1
                            self.promote(scv,'suicider')
                            self.log_command('scv.attack(self.enemy_pos)')
                            scv.attack(self.enemy_pos)
            for scv in self.units(SCV):
                scvt = scv.tag
                if scvt in self.all_scvt:
                    if self.job_of_scvt[scvt] in self.bad_jobs:
                        if todo > 0:
                            todo -= 1
                            self.promote(scv, 'suicider')
                            self.log_command('scv.attack(self.enemy_pos)')
                            scv.attack(self.enemy_pos)
        # mimminer or gasminer
        if (self.count_of_job['idler'] + self.count_of_job['volunteer'] == 0):
            if self.vespene < 1000: # new, promote gas.
                await self.more_gas()
            elif self.minerals > self.vespene + 1000:
                await self.more_gas()
            elif self.vespene > self.minerals + 1000:
                await self.more_minerals()
        #       stop escorters lured to their death
        for scvt in self.all_scvt:
            if (self.job_of_scvt[scvt] == 'escorter'):
                for scv in self.units(SCV):
                    if scvt == scv.tag:
                        if self.proxy(scv.position):
                            self.promote(scv,'idler')
                            self.log_workers('Enemy fear stops escorter '+self.name(scvt))
                            self.log_command('scv(AbilityId.STOP)') # stop moving
                            scv(AbilityId.STOP)
        # scouts
        for scv in self.units(SCV):
            if scv.tag == self.scout1_tag:
                if self.no_move_or_near(scv,32,4):
                    self.scout1_pole = (self.scout1_pole+1) % len(self.scout1_pos)
                    goal = self.scout1_pos[self.scout1_pole]
                    self.go_move(scv,goal)
            if scv.tag == self.scout2_tag:
                if self.no_move_or_near(scv, 32, 1):
                    self.scout2_pole = (self.scout2_pole + self.scout2_direction) % len(self.scout2_pos)
                    goal = self.scout2_pos[self.scout2_pole]
                    self.go_move(scv, goal)
        # idler leisure walks
        for scv in self.units(SCV):
            scvt = scv.tag
            if self.job_of_scvt[scvt] == 'idler':
                # get a point, not too far
                sd = 99999
                while sd > 70 * 70:
                    tp = self.random_mappoint()
                    sd = self.sdist(tp, self.loved_pos)
                if self.near(scv.position,self.loved_pos,80):
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
            expo = self.expo_of_pos(scv.position)
            if self.job_of_scvt[scvt] == 'mimminer':
                assigned_mimt = self.mimt_of_scvt[scvt]
                for mim in self.minerals_of_expo[expo]:
                    if mim.tag == assigned_mimt:
                        if scvt in self.minedirection_of_scvt:
                            if scv.is_returning and (self.minedirection_of_scvt[scvt] == 'G'):
                                # it is turning round towards the base
                                if not self.near(mim.position,scv.position,2):
                                    self.log_boss('Hey a shifted mimminer '+self.name(scvt)+' should mine '+str(assigned_mimt))
                                    # find closest mineralpatch. In equal cases promote one with less miners.
                                    best_sdist = 80000
                                    best_mimt = self.notag
                                    for mim in self.minerals_of_expo[expo]:
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
                        mim = self.mineral_field.random  # contains nonempty
                        tries = 0
                        while (mim.tag in self.all_mimt) and (tries<100):
                            tries += 1
                            mim = self.mineral_field.random
                        for scv in self.units(SCV):
                            if scv.tag == scvt:
                                self.promote(scv,'volunteer')
                                scv.gather(mim)

    def hop_cc(self):
        self.routine = 'hop_cc'
        tomove = set() # of cc
        moveto = set() # of ccpos
        cancelable = {AbilityId.COMMANDCENTERTRAIN_SCV}
        # tomove (cc)
        for cc in self.structures(COMMANDCENTER).ready + self.structures(ORBITALCOMMAND).ready:
            if cc.tag not in self.special_tags:
                movable = True
                for order in cc.orders:
                    if order not in cancelable:
                        movable = False
                if movable:        
                    expo = self.expo_of_pos(cc.position)
                    # move reason: low minerals
                    patches = 0
                    for mim in self.minerals_of_expo[expo]:
                        patches +=1
                    if patches < 5:
                        tomove.add(cc)
                    # move reason: enemies
                    if self.ground_strength_of_expo[expo] < -50: # about 3 marines
                        tomove.add(cc)
        # moveto (cc_pos)
        if len(tomove) > 0:
            for ccpos in self.expansion_locations_list:
                expo = self.expo_of_pos(ccpos)
                patches = 0
                for mim in self.minerals_of_expo[expo]:
                    patches += 1
                if patches >= 5:
                    if self.check_layout(COMMANDCENTER,ccpos):
                        moveto.add(ccpos)
        # do 1 move
        if (len(tomove) > 0) and (len(moveto) > 0):
            if len(tomove) > len(moveto):
                moveto_choice = random.choice(tuple(moveto))
                minsd = 99999
                for cc in tomove:
                    sd = self.sdist(cc.position,moveto_choice)
                    if sd < minsd:
                        tomove_choice = cc
                        minsd = sd
            else: # len(tomove <= len(moveto)
                tomove_choice = random.choice(tuple(tomove))
                minsd = 99999
                for ccpos in moveto:
                    sd = self.sdist(ccpos, tomove_choice.position)
                    if sd < minsd:
                        moveto_choice = ccpos
                        minsd = sd
            # hop tomove_choice to moveto_choice
            self.write_layout(COMMANDCENTER,moveto_choice)
            for order in tomove_choice.orders:
                if order in cancelable:
                    self.log_command('tomove_choice(AbilityId.CANCEL)')
                    tomove_choice(AbilityId.CANCEL)
            self.goal_of_flying_struct[tomove_choice.tag] = moveto_choice
            self.landings_of_flying_struct[tomove_choice.tag] = 0
            self.log_success('up base')
            self.log_command('tomove_choice(AbilityId.LIFT')
            tomove_choice(AbilityId.LIFT)
            # give a hopped cc a destiny
            if tomove_choice in self.structures(COMMANDCENTER):
                self.cc_destiny[moveto_choice] = 'pf'

    #*********************************************************************************************************************

    def clean_layout(self):
        self.routine = 'clean_layout'
        # erase layout buildings that are in designs, but neither existing there nor thought
        #
        # if vision, delete from enemy_buidings_permanent
        todel = set()
        for tag in self.enemy_buidings_permanent:
            pos = self.enemy_buidings_permanent[tag]
            if self.is_visible(pos):
                seen = False
                for ene in self.enemy_structures:
                    if (ene.tag == tag) and (ene.position == pos):
                        seen = True
                if not seen:
                    todel.add(tag)
        for tag in todel: # we neglect that it can exist at another position           
            del self.enemy_buidings_permanent[tag]
        # designs: add tag to realized plans
        newdesigns = set()
        for (struc,place,tag) in self.designs:
            if tag == self.notag:
                for astruc in self.structures:
                    # the cc could have become a pf already, accept flying
                    if self.position_of_building(astruc) == place:
                        tag = astruc.tag
            newdesigns.add((struc,place,tag))
        self.designs = newdesigns.copy()
        # designs: erase if neither tag nor plan is found
        erase = set()
        for (struc,place,tag) in self.designs:
            seen = False
            if tag in self.all_structuretags:
                seen = True
            for scvt in self.goal_of_trabu_scvt:
                if place == self.goal_of_trabu_scvt[scvt]:
                    seen = True
            for (exething,exeplace,status) in self.buildorder_exe:
                if place == exeplace:
                    seen = True
            for (exething,exeplace) in self.chosenplaces:
                if place == exeplace:
                    seen = True
            if place in self.possible_cc_positions:
                if struc == MAINCELLBLOCK:
                    seen = True
            if place in self.tankplaces:
                seen = True
            if place in self.goal_of_flying_struct.values():
                seen = True
            for enetag in self.enemy_buidings_permanent:
                enepos = self.enemy_buidings_permanent[enetag]
                if place == enepos:
                    seen = True
            for (th, po, status, ow, pri) in self.throwspots:
                if place == po:
                    seen = True
            if not seen:
                erase.add((struc,place,tag))
        for (struc,place,tag) in erase:
            self.log_success('(clean_layout of a '+struc.name+')')
            self.erase_layout(struc,place)


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
        #radio_nr = 23
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


#*********************************************************************************************************************

    def get_nuke_target(self, ghostpos):
        # -> self.nuke_target
        nuke_targets = set()
        bestquality = -99999
        for ene in self.enemy_structures:
            expo = self.expo_of_pos(ene.position)
            quality = - self.circledist(ene.position,ghostpos)
            for are in self.enemy_structures_of_expo[expo]:
                if self.near(ene.position,are.position,4):
                    quality += 20
            if quality > bestquality:
                bestquality = quality
                nuke_targets = {ene.position}
            elif quality == bestquality:
                nuke_targets.add(ene.position)
        if len(nuke_targets) == 0:
            self.nuke_target = self.enemy_pos
        elif self.nuke_target not in nuke_targets:
            bestsd = 99999
            for nt in nuke_targets:
                sd = self.sdist(ghostpos,nt)
                if sd < bestsd:
                    bestsd = sd
                    self.nuke_target = nt


    async def ghost_fun(self):
        self.routine = 'ghost_fun'
        if self.ghost_phase > 'A':
            self.log_success('ghost_phase '+self.ghost_phase)
        self.ghost_calmdown = max(0,self.ghost_calmdown - self.chosen_game_step)
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
                    self.ghost_calmdown = 80
            else:
                done += 1
            if self.we_started_amount(BARRACKS) < 2:
                if self.ghost_calmdown == 0:
                    self.throw_if_rich(BARRACKS, 'ghost_fun', 1)
                    self.ghost_calmdown = 80
            else:
                done += 1
            if self.we_started_amount(BARRACKSTECHLAB) < 1:
                self.throw_if_rich(BARRACKSTECHLAB, 'ghost_fun', 1)
            else:
                done += 1
            if self.we_started_amount(FACTORY) < 1:
                if self.ghost_calmdown == 0:
                    self.throw_if_rich(FACTORY, 'ghost_fun', 1)
                    self.ghost_calmdown = 80
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
                    self.ghost_calmdown = 80
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
            for (martype, bartype, pos, dura) in self.eggs:
                if (martype == NUKESILONOVA) and (dura > 20):
                    done -= 1
            if done >= 2:
                self.ghost_phase = 'E'
                # init
                self.get_nuke_target(self.shipyard)
        elif self.ghost_phase == 'E':
            # there are ghosts and nukes and a target
            # if none close to nuking place, go there
            close = False
            for ghost in self.units(GHOST):
                if self.near(ghost.position,self.nuke_target,13):
                    close = True
            if close:
                self.ghost_phase = 'G'
            else:
                target = self.nuke_target
                radius = 13
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
                            if self.near(goal, ene.position, 11.5):
                                tooclose = True
                for ghost in self.units(GHOST):
                    self.go_move(ghost,goal)
                self.ghost_phase = 'F'
        elif self.ghost_phase == 'F':
            # moving to goals
            for ghost in self.units(GHOST):
                if self.near(ghost.position,self.nuke_target,70):
                    if AbilityId.BEHAVIOR_CLOAKON_GHOST in await self.get_available_abilities(ghost):
                        ghost(AbilityId.BEHAVIOR_CLOAKON_GHOST)
                if ghost.tag in self.goal_of_unittag: # dont ask me, it occurred
                    if self.no_move(ghost,64):
                        self.get_nuke_target(ghost.position)
                        self.ghost_phase = 'E'
        elif self.ghost_phase == 'G':
            # goal reached
            # call nuke
            done = 0
            for ghost in self.units(GHOST):
                if self.near(ghost.position,self.nuke_target,13):
                    if AbilityId.TACNUKESTRIKE_NUKECALLDOWN in await self.get_available_abilities(ghost):
                        ghost(AbilityId.TACNUKESTRIKE_NUKECALLDOWN, self.nuke_target)
                        done += 1
            # continue
            if done >= 1:
                self.ghost_calmdown = 80
                self.ghost_phase = 'H'
        elif self.ghost_phase == 'H':
            # waiting for strike
            if self.ghost_calmdown == 0:
                self.ghost_phase = 'I'
                # init
                for ghost in self.units(GHOST):
                    self.go_move(ghost,self.shipyard)
        elif self.ghost_phase == 'I':
            # walking home
            done = 0
            for ghost in self.units(GHOST):
                if not self.near(ghost.position,self.nuke_target,70):
                    if AbilityId.BEHAVIOR_CLOAKOFF_GHOST in await self.get_available_abilities(ghost):
                        ghost(AbilityId.BEHAVIOR_CLOAKOFF_GHOST)
                if not self.no_move(ghost,64):
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
    all_maps = ['IceandChromeLE','PillarsofGoldLE','EternalEmpireLE','SubmarineLE','DeathauraLE','GoldenWallLE','EverDreamLE']
    map = random.choice(all_maps)
    # TO TEST use next line
    #map = 'PillarsofGoldLE'
    opponentspecies = random.choice([Race.Terran,Race.Zerg,Race.Protoss])
    # TO TEST use next line
    #opponentspecies = Race.Terran
    # Easy/Medium/Hard/VeryHard
    run_game(maps.get(map), [
        Bot(Race.Terran, Chaosbot()),
        Computer(opponentspecies, Difficulty.VeryHard)
        ], realtime = False)

if __name__ == "__main__":
    main()
