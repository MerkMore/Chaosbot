# Merkbot.py containing Chaosbot
# author: MerkMore
# version: see chat
# built on the Burnysc2 layer.
# origin: C:\Users\Wout\AppData\Local\Programs\Python\projects\bot
#
import sc2
from sc2 import run_game, Race, Difficulty, maps
from sc2.player import Bot, Computer
from sc2.ids.ability_id import AbilityId
from sc2.ids.unit_typeid import UnitTypeId
from sc2.ids.upgrade_id import UpgradeId
from sc2.ids.effect_id import EffectId
from sc2.ids.buff_id import BuffId
from sc2.position import Point2
from sc2.game_data import Cost
from sc2.constants import TARGET_AIR, TARGET_GROUND
import random
import time
from math import sqrt,cos,sin,pi,acos
from sc2.game_info import GameInfo
from layout_if_py import layout_if
from rocks_if_py import rocks_if
from bunker_if_py import bunker_if
from plot_if_py import plot_if
# from sc2.constants import *
from sc2.ids.unit_typeid import SCV
from sc2.ids.unit_typeid import RAVEN
from sc2.ids.unit_typeid import STARPORT
from sc2.ids.unit_typeid import VIKINGFIGHTER
from sc2.ids.unit_typeid import VIKINGASSAULT
from sc2.ids.unit_typeid import MARINE
from sc2.ids.unit_typeid import BARRACKS
from sc2.ids.unit_typeid import BUNKER
from sc2.ids.unit_typeid import MARAUDER
from sc2.ids.unit_typeid import REAPER
from sc2.ids.unit_typeid import MEDIVAC
from sc2.ids.unit_typeid import SIEGETANK
from sc2.ids.unit_typeid import HELLION
from sc2.ids.unit_typeid import HELLIONTANK
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
from sc2.ids.upgrade_id import SHIELDWALL
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
from sc2.ids.upgrade_id import DRILLCLAWS
from sc2.ids.upgrade_id import BANSHEECLOAK
from sc2.ids.unit_typeid import ENGINEERINGBAY
from sc2.ids.upgrade_id import TERRANINFANTRYWEAPONSLEVEL1
from sc2.ids.upgrade_id import TERRANINFANTRYWEAPONSLEVEL2
from sc2.ids.upgrade_id import TERRANINFANTRYWEAPONSLEVEL3
from sc2.ids.upgrade_id import TERRANINFANTRYARMORSLEVEL1
from sc2.ids.upgrade_id import TERRANINFANTRYARMORSLEVEL2
from sc2.ids.upgrade_id import TERRANINFANTRYARMORSLEVEL3
from sc2.ids.upgrade_id import CYCLONELOCKONDAMAGEUPGRADE
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
from sc2.ids.unit_typeid import AUTOTURRET
# with INFESTED is meant "close to the enemy".
from sc2.ids.unit_typeid import INFESTEDBARRACKS
from sc2.ids.unit_typeid import INFESTEDBUNKER
from sc2.ids.unit_typeid import INFESTEDFACTORY
from sc2.ids.unit_typeid import INFESTEDSTARPORT
from sc2.ids.unit_typeid import INFESTEDCOCOON
# mark possible expansions:
from sc2.ids.unit_typeid import MAINCELLBLOCK
# protoss
from sc2.ids.unit_typeid import MOTHERSHIP
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
from sc2.ids.unit_typeid import CREEPTUMORBURROWED
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
from sc2.ids.unit_typeid import OVERSEER
from sc2.ids.unit_typeid import BROODLORD
from sc2.ids.unit_typeid import HATCHERY
from sc2.ids.unit_typeid import LAIR
from sc2.ids.unit_typeid import HIVE
from sc2.ids.unit_typeid import BROODLING
from sc2.ids.unit_typeid import LARVA
from sc2.ids.unit_typeid import EGG
from sc2.ids.unit_typeid import ZERGLING

class Chaosbot(sc2.BotAI):
    #   ############### CHANGE VALUE AD LIB
    do_slowdown = False
    slowdown_frames = 99999 # 5*60*22.4
    slowness = 0.05 # realtime is around 0.05
    there_is_a_new_opening = True
    do_funchat = False
    do_selfhate = True
    do_log_success = False
    do_log_bird_history = False
    do_log_fail = False
    do_log_command = False
    do_log_attacktype = False
    do_log_workers = False
    do_log_population = False
    do_log_fighters = False
    do_log_armysize = False
    do_log_army = False
    do_log_cc = False
    do_log_purpose = False
    do_log_swaps = False
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
    do_log_dreams = False
    do_log_thoughts = False
    do_log_preps = False
    do_log_eggs = False
    do_log_birds = False
    do_log_buildstate = False
    do_log_throw = False
    do_log_bunker = False
    do_log_earn = False
    do_log_orders = False
    do_log_unitorder = False
    do_log_buildorder = False
    do_log_speedmining = False
    do_log_buildsource = False
    #   ############### CONSTANT ######################################
    #   constant over the frames after frame 0:
    chosen_game_step = 2 # the amount of frames between program-step-runs
    frame = 0 # will have even numbers if chosen_game_step=2
    frames_per_second = 22.4 # a gameclient property
    expansion_locations = [] # expansion_locations_list debugged
    #
    botnames = {}
    errortexts = []
    reaper_speed_official = 5.25
    scv_speed_official = 3.94
    # The circledistance a unit travels per second.
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
    patience = 200 # amount of frames to retry building etc.
    detection_range = 11.5
    all_structures = []
    all_structures_tobuildwalk = []
    all_army = []
    all_labarmy = []
    all_workertypes = []
    all_upgrades = []
    all_labs = [] # for labs, with place, always its motherbuilding place will be used.
    all_techlabs = []
    all_reactors = []
    standalone_labs = [] # TECHLAB, REACTOR
    all_pfoc = []
    basekind_of_kind = {}
    antiair_detector = [] # PHOTONCANNON, SPORECRAWLER, MISSILETURRET
    supply_of_army = {}
    airground_of_unit = {} # 'air'/'ground'
    builddura_of_thing = {}
    category_of_thing = {}
    size_of_structure = {}
    species_of_structure = {}
    liftable = []
    techtree = []
    all_species_things = set()
    cradle = []
    viking_targets = []
    hall_types = []
    landable = []
    all_repairable_shooters = set()
    thingtag_of_repairertag = {} # for repairers
    upgrade_benefitter = set() # of (upgrade,benefitter)
    hometop = set() # empty squares near start, inside the wall, inside ramps
    homeramp_pos = None
    homenatural_pos = None
    homenaturalchoke_pos = None
    enemytop = set() # empty squares near enemy_pos
    enemyramp_pos = None
    enemynatural_pos = None
    enemythird_pos = None
    enemynaturalchoke_pos = None
    hisleft = None
    hisright = None
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
    map_center = None
    #
    flee_circle = []
    opponent = '' # opponent_id on ladder, else enemy_species
    enemy_species = '' # Zerg/Terran/Protoss/Random
    #
    maxhealth = {}  # per unittype the health_max
    #
    #   ############### variables by expo ######################################
    maptile_width = 10
    maptile_half = maptile_width // 2
    maptile_amount = (200+maptile_half) // maptile_width
    maptiles = maptile_amount * maptile_amount
    nine = {} # the 9 maptiles around a maptile
    enemies_of_tile = {} # the enemy units and structures per tile
    goodguys_of_tile = {} # the own units and structures per tile
    expos = 0 # expansionlocations
    expo_of_maptile = {}
    pos_of_expo = {}
    # a postag is a kind of tag based on position. The position can have halves and is in 0,200 x 0,200.
    # an enemy building or mineralpatch has no stable tag, because of fog-of-war.
    minerals_of_expo = {} # all_minerals, not mined-out. Per expo: (mimpos,postag)
    vespene_of_expo = {} # all gasgeysers, not mined-out. Per expo: (gaspos,postag)
    units_of_expo = {} # units
    scvs_of_expo = {} # units(SCV)
    structures_of_expo = {} # structures
    enemy_units_of_expo = {} # enemy_units
    enemy_structureinfo_of_expo = {} # per expo: set of structureinfo = tp = (typ,pos) last seen
    # strength = dps * health
    ground_strength_hist = set() # of (thing,float)
    air_strength_hist = set() # of (thing,float)
    ground_strength_of_expo = {} # strength of me minus enemy
    air_strength_of_expo = {} # strength of me minus enemy
    worth_of_expo = {} # positive, only buildings: mineralcost + 2*gascost
    #
    #   ############### GAMESTATE ##################################################
    #   gamestate values constant in this frame after gamestate:
    all_bases = [] # including at odd positions
    all_mine_bases = [] # at expansion_locations
    army_supply = 0
    all_scvtags = set() # simple, no limbo like in all_scvt
    all_mine_basetags = set()
    all_structuretags = set() # simple
    all_unittags = set()
    all_bunkertags = set() # simple
    all_minerals = set() # mineral_field but with a stable tag. (mimpos,mimt). Not mined-out.
    all_vespene = set() # vespene_geyser but with a stable tag. (gaspos,gast). Not mined-out.
    mineral_field_hash = 0 # to skip computing all_minerals
    supply_rate = 0.17
    enoughworkers = 0 # about 80 but reduced when floating minerals
    reached_max_supply_once = False
    # some average counts related to supply:
    good_worker_supply = 0
    good_army_supply = 0
    good_bases = 0
    good_armybuildings = 0
    good_upgradebuildings = 0
    good_upgrades = 0
    good_plans = set()
    last_good_plans = set()
    notechlab = set() # of (thingtype,pos), to prevent building a techlab there.
    #   ############### REST ##############################################################
    focus = {} # per unittag the enemy to attack tag advice
    queuefocus = {} # if a queued attack is wanted, take this.
    fightpos = {} # per tag, a good fighting position, or self.nowhere.
    attackmove_state = {} # per tag a text. Indicates if the unit uses my attackmove.
    attackmove_goal = {} # per tag a point
    attackmove_fightgoal = {} # in a fight, a point to move to.
    attackmove_goalreached = {} # per tag a boolean.
    attackmove_goaltried = {} # amount of move commands given.
    attackmove_enetag = {} # per tag a enemytag (enemyunit or structure)
    attackmove_queue_enetag = {} # per tag a enemytag (enemyunit or structure)
    attackmove_hangout = {} # per tag a number. The distance it may float before being called back to goal.
    #
    free_normal_basepositions = set()
    #
    enemy_count = {} # per enemy unittype the max amount simultaneously seen
    #
    all_categories = set() # grouping for structures and units
    purpose = {} # for bases: 'scv'/'wishtofly' etc
    circle = []
    # dream -> thought -> prep -> egg -> bird
    preps = set() # (martype,bartype,pos,dura,owner) or (thingtype,scv,buildpos,dura,owner)
    eggs = set() # (martype,bartype,buildingpos,dura) or (thingtype,scv,buildpos,dura)
    birds = set() # (thingtype,pos)
    #
    bird_am_history = {} # for log_bird_history
    # for different constructionwish subsystems to interact
    # Systems must first put a thought in "thoughts" before they can build_thing.
    # The (thingtype,pos) must be unique
    # Sometimes you cannot add because of maxam.
    thoughts = [] # multiset (thingtype,pos,owner)
    unthinkable = set() # (thingtype,pos)
    dreams = [] # multiset (thingtype,pos,owner)
    #   stored tips
    tips = []
    tips_used = set()
    #   coding problem
    function_result_Point2 = None
    doubling_frame = {}
    idles = set() # idle at least 10 frames
    idles_start = {}
    readies = set() # ready at least 20 frames
    readies_start = {}
    readies_delayed = {} # to delay readyness of a building landing.
    neighbours = set()
    chosenplaces = []
    #   ############### ARMY AND STRUCTURE MANAGEMENT
    # corrosive biles
    biles = set()
    bile_landframe = set()
    #
    throw_history_set = set()
    # medivacs:
    victim_of_medivac = {} # per medivac the marine it follows
    thechosen = None # a unit. Only valid this frame, functionresult.
    # ravens:
    lostframe_of_raven = {} # the followed bc jumped
    victim_of_raven = {} # per raven the bc it follows
    # vikings:
    viking_air_range = 9
    viking_min_health = 35
    viking_good_health = 120
    viking_last_att_pos = nowhere # last attacked enemy hall position
    normalsquadrons = set() # of identification number
    all_squadrons = {-2,-1} # -1 for looking, vik repair, -2 for landharass
    squadron_of_viktag = {}
    size_of_squadron = {} # amount
    pos_of_squadron = {} # pos
    goal_of_squadron = {} # pos, if no victim
    victim_of_squadron = {} # ene.tag, or notag
    victimpos_of_squadron = {} # pos
    victimlastpos_of_squadron = {} # pos
    bestdist_of_squadron = {} # number
    movepos_of_viking = {} # for a moving viking: pos
    # emotion_of_unittag[vik.tag] 'patrolling'/'attacking'/'moving'
    forgotten_vikings = {} # per vik.tag the frame it was seen idle in repair
    #
    idiot_plan = []
    idiot_busy = set()  # of (thing,finishframe) being built
    rushopening = False
    opening_create = set() # of (unittype,amount)
    opening_create_units = 0 # sum of the above amounts
    opening_create_hadmax = {} # per kind a number
    opening_create_slack = 99 # means do opening_buildseries first
    marine_gathered = False
    marine_attacked = False
    marine_opening_bases = 0
    marine_gatherframe = 0
    marine_goal = nowhere
    marine_gather_time = 0
    marine_attack_estimate = [0,4.2,6.3,7.5,8.4,9.2,9.6] # 0 1 2 3 4 5 6 bases, attacktime in minutes
    flown_in = set() # to fly in just once
    liberator_spots = set() # of [name,siegeattack,siegeship]
    libspot = {} # per liberatortag: [name,siegeattack,siegeship]
    spotlove = {} # per spotname: int
    lib_factory_tag = notag
    lib_turret_tries = 7
    lib_turpos = nowhere
    firstlib = True
    secondlib = False
    #
    vulture_pole = 0
    last_vulture_frame = 0
    vulture_pos = []
    #
    enemy_real_structures = set() # enemy_structures without the snapshots
    enemy_structureinfo = set() # of (type,pos) having last seen info
    last_enemy_structureinfo = set() # of last programframerun
    enemy_structureinfo_plus = set() # of (type,pos,finishframe) having last seen info
    # neglects structures flying directly above another structure
    #
    last_enemies = set() # of (type,position,tag) Only enemy units.
    #
    # wa_ is worker attack administration
    wa_ihitted = 0 # total hit count
    wa_iwashit = 0 # total being hit count
    wa_repair = 0 # total own hp repair
    wa_hitframe = {} # per worker, estimated frame of the last hit dealt
    wa_lastscvs = set() # set of own scv (tag,position,health)
    wa_lastene = set() # set of enemy worker (tag,position,canhit)
    #
    yamatoed = {} # per enemytag the shootframe. To prevent a group of bcs overkilling the same target.
    #
    # cluster is a number, 0<=cluster<100. It groups widowmines, burried and bare.
    clusters = set() # of each cluster with size>0 (and some with size 0)
    goal_of_cluster = {} # per cluster a Point2
    cluster_of_mine = {} # per widowminetag (or burried) the cluster it is in.
    size_of_cluster = {} # per cluster the amount of mines in it.
    #
    cleaners = set() # escorters clean enemy structures near home
    escorter_of_builder = {} # per threatened buildertag a escortertag
    #
    last_health = {}
    #
    #   army coodination
    goal_of_unittag = {} # control of unit movement
    last_sd_of_unittag = {} # control of unit movement
    shame_of_unittag = {} # control of unit movement
    detour_of_unittag = {} # control of unit movement
    side_of_unittag = {} # some units have L/R
    victimtag_of_unittag = {} # cyclones have a victim
    unlockframe_of_cyclonetag = {}
    energy_of_unittag = {} # control of spend energy
    wait_of_unittag = {} # control of spend energy
    #
    speciality_of_tag = {} # wall/cheese1/ opening_name
    bunker_marines = set()
    cleaning_tank_tags = set()
    cleaning_object_found = False
    cleaning_object_pos = nowhere
    cleaning_tank_siegepos = {} # intended siege position
    cleaning_tank_shotframe = {} # to know whether it is shooting
    cleaning_tank_thinkframe = {} # to wait a second after being surprised
    cleaning_tank_back = {} # move one step back if falling in a fight
    #
    emotion_of_unittag = {} # jumpy bc emotion "lazy","repair", etc. Also for tanks, and for widowmines, rushworkers.
    burrowpos_of_wmt = {}
    eneunitsseen = {} # per vulture a timer
    attack_type = 'jumpy'
    cruisercount = 0
    lastcruisercount = 0
    goal_of_flying_struct = {} # initially its own position
    subgoal_of_flying_struct = {} # can be used to fly not in a straight line
    landings_of_flying_struct = {}
    bestbctag = notag
    bestbc_dist_to_goal = 99999
    bc_fear = 250
    demanded_groupup = False # for bc to speed groupup getting the slowest ones
    lasttargettag_of_bctag = {}
    homepole_of_wmt = {} # for cheesemines a scoutplace near goal
    pole_of_wmt = {} # for cheesemines a next scoutplace
    phase_of_wmt = {} # for cheesemines attack or flee
    marauder_goal = Point2((100,100))
    marauder_restpoint = Point2((100,100))
    marauder_retreat = True
    marauder_pf_phase = 0
    marauder_pf_spot = nowhere
    mine_shot = {} # the frame a cheese1_mine did shoot
    mine_burried = {} # the frame a mine burried
    #
    trail = {} # per unittag, of the last 10 movements, the position. Not workers.
    trailpo = {} # per unittag, the index of the newest trail value
    trailtarget = {} # per unittag, its goalposition (if it has one). Also used to init trail.
    trailtargetframe = {} # per unittag, the frame it got this goal.
    preferred_trailnr = {} # to move back along the trail if attacked
    #
    waitframe_of_tag = {} # a future framenumber to continue action
    #
    tankplaces = set()
    airport_of_expo = {} # some place to repair airships
    employment_of_expo = {} # some place to gather applicants (miners)
    ambition_of_strt = {} # ambition contains labs, pfoc  just before actual build
    gym = [] # (structuretype,structuretag,trainee,owner) to soon train trainee (upgrade or army)
    ambitiondura = 10 # less than scv_build_time 12
    gymdura = 8 # less than ambitiondura, so upgrade cc works
    owner_of_ambistrt = {}
    army_center_point = None
    # The lab progress bug demands extra administation
    labprogress_buildframes = set() # of (cradletag,cradlepos,startframe)
    #   (struc,place,tag) for tobuildwalk plans with a layout. Administrate to enable erasing.
    designs = set()
    # wall
    wall_barracks_pos = None
    wall_depot0_pos = None
    wall_depot1_pos = None
    wall = set() # ((SUPPLYDEPOT, point), ...)
    #
    funchat_linenr = 0
    funchat_lines = []
    #
    selfhate_frame = 99999
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
    # standard reaper:
    reaper_goal = nowhere
    #
    banshee_right = {} # per bansheetag a bool
    fearframe_of_banshee = {} # per bansheetag a framenumber
    detect = set()  # set of positions of enemy detector buildings
    detect_hash = 0 # to notice changes in detect
    detect_old_hash = 0 # to notice changes in detect
    detect_improve = nowhere # if not self.flystraight(), the position further from an enemy detector building
    #
    #   A barracks close to the enemy has to fly from build position to attack position
    cheese1_barracks_pos = nowhere # startposition
    cheese1_factory_pos = nowhere
    cheese1_starport_pos = nowhere
    cheese1_landing_pos = nowhere
    cheese1_bunker_pos = nowhere
    cheese1_prison_pos = nowhere
    cheese1_tank_pos = nowhere
    cheese1_phase = 'A'
    cheese1_barracks_tag = notag
    cheese1_factory_tag = notag
    cheese1_starport_tag = notag
    cheese1_bunker_tag = notag
    cheese1_scv_tag = notag
    cheese1_marine_tags = set()
    cheese1_marine_buildcount = 0
    cheese1_tank_buildcount = 0
    cheese1_mine_buildcount = 0
    cheese1_tank_tag = notag
    cheese1_mine_tags = set()
    cheese1_frames = 0
    # cheese2
    cheese2_bunkspots = set()
    cheese2_triedexp = set()
    wished_marines_per_bunker = 2
    # cheese3
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
    cheese3_bunkersites = set()
    cheese3_tanktags = set()
    # for workerrush:
    followers = nowhere # for a large runaround circle
    fleefear = {} # to continue through bushes: per scvtag a number
    fleepole = {} # for circling scvs: per scvtag a number 0/1/.../15
    fleepolepos = [] # 16 points of a circle in a corner
    enemymelee = set() # of tag of reachable enemy workers and zerglings
    hisrampmimtag = 0
    hismidmimtag = 0
    hisfarmimtag = 0
    homemimtag = 0
    sidemimtag = 0
    hisrampmim = None
    hismidmim = None
    hisfarmim = None
    homemim = None
    sidemim = None
    turningpoint = nowhere
    startworkerrushers = 0
    workerrushstartframe = 250 # 250
    workerrushmayfleeframe = 1800 # 1800
    workerrushstopframe = 4500 # 4500
    healthybound = 40.5
    rushrepairs = set()  # of (repairer_tag,reparee_tag) No double repairer_tag.
    rushrepairers = set()  # of repairer_tag
    workerrushstate = 'tobe' # tobe/busy/ended
    workerback = set() # of tag of worker moving back, trying to stack.
    stackphase = 'A'
    stacktag = notag # a reference worker
    stack_at_dist = 50 # moment for stacking
    turndistance = 1.04 # when to turn while stacking
    turndistance2 = 0.50 # when to turn while stacking
    bitebound = 1.0 # melee worker attack clash
    rushvictim = None # this iteration, result of subroutine
    rushdamage = 0
    last_weapon_cooldown = {} # for rushdamage
    last_sd_of_scv = {} # to move to a goal, when started with a jump
    repairsite_emotions = set()
    towardsmineral = {}
    known_hit_by_enemy = {} # for enemy workers, the frame he hit me (very likely).
    wait_of_scv = {} # for cooling some frames
    nuke_ghosts = set()
    army_ghosts = set()
    rush_ghosts = set()
    ghost_requests = [] # 'nuke_ghost'/'army_ghost'/'rush_ghost'  if you want one
    ghostmove_last_energy = {} # per ghosttag a number
    ghostmove_snipeend = {} # per ghosttag the frame a snipe will end
    ghostmove_state = {} # per ghosttag a text
    ghostmove_fightgoal = {} # per ghosttag a position
    ghostmove_goal = {} # per ghosttag a position
    ghostmove_goalreached = {} # per ghosttag a bool
    ghostmove_goaltried = {} # count move commandos
    ghostmove_hangout = {} # tolerance after reaching goal
    rushghost_phase = 'A'
    rushghost_sp = nowhere # the starport position
    rushghost_frame = 0 # to timeseparate phases
    rushghost_toemp = notag # one of the ghosts
    rushghost_tonuke = notag # one of the ghosts
    rushghost_bunker = True
    rushghost_scvs = set() # the nukerush scvs
    rushghost_retired = set() # some ghosts
    rushghost_droppos = nowhere # for the medivac
    rushghost_callpos = nowhere # for the nuking ghost
    rushghost_shootpos = nowhere # to stand in the enemy mineralline
    rushghost_bunkerpos = nowhere # for a distraction bunker
    medivac_speedframe = {} # per medivac the frame it started its speed boost.
    platoons = [] # of set of scvtag
    platooncenters = [] # of Point2
    platoonenemies = [] # of set of workertag
    platoonenemycenters = [] # of Point2
    platoonmight = [] # of float. Positive means I am stronger.
    platoonplans = [] # 'neutral'/'agressive'/'defensive'/'flee'
    platoongoals = [] # of Point2
    lastpos_of_unittag = {} # Point2 for enemy and own workers
    nextpos_of_unittag = {} # Point2 for enemy and own workers
    # after the workerrush:
    fleecirclers = set()
    #
    do211_phase = 0
    do211_mar = set()
    do211_med = set()
    do211_scv = set()
    do211_plane = {} # the preferred medivac of the passenger
    do211_goal = nowhere
    do211_goals = []
    do211_hallsgoaled = set()
    do211_delay_attack = False
    #
    # to swap starport on techlab:
    couldswap = set() # of (buildingtype,position)
    willswap = set() # of (buildingtype,position) from decision (maybe still egg) to lift-off
    didswap = set() # of (buildingtype,position): the old position of a swapped building
    swapplans = set() # of (frompos,topos) Contains also old plans
    barracks_techlab_advice = nowhere
    #
    ghost_phase = 'A'
    ghost_calmdown = 0
    nuke_target = None
    #
    cc_destiny_rush = False
    cc_destiny = {} # [pos] = 'oc'/'pf'/not_in
    #
    # painted on the layout, so as not to build other things there. Yet can place cc there.
    possible_cc_positions = set()
    #
    #   ############### SCV MANAGEMENT
    #   traveller -> settler -> fencer -> builder  scvs have a goal
    #   traveller, settler, fencer and builder scvs have a structure to build
    goal_of_trabu_scvt = {}
    structure_of_trabu_scvt = {}
    owner_of_trabu_scvt = {}
    arrivals = set() # of (scvtag, goal, building, startframe, maxarrivalframe) for travellers
    #   scv management:
    #   The tag of existing own scvs, in this frame. scvs in limbo included.
    all_scvt = []
    #   The existing refineries where we want to mine from, in this frame
    all_gas_to_mine = set() # of (gaspos,gast) with gast a postag
    #   The existing minerals where we want to mine from, in this frame
    all_mim_to_mine = set() # of (gaspos,gast) with gast a postag
    #   job_of_scvt dictionary
    good_jobs = ('builder','settler','fencer','traveller','repairer','fighter','escorter'
                 ,'scout','cheeser','pilot','sacrifice')
    bad_jobs = ('gasminer','mimminer','candidate','carrier','applicant','reporter')
    no_jobs = ('idler','suicider','volunteer','inshock','fleeer')
    #
    jobs_may_idle = ('mimminer','fencer','settler','scout','fighter','cheeser','applicant'
                     ,'idler','pilot','sacrifice')
    #
    expected_orders = set()
    #
    job_of_scvt = {}
    count_of_job = {}
    #   applicants,candidates,carriers have a vision, a tag of a base to walk to
    vision_of_scvt = {}
    #   recalculated each frame:
    wanted_of_cct = {}
    #   gas harvesting assignments
    gas_of_minert = {} # gas=(gaspo,gast), gast is a postag
    nminers_of_gast = {}
    #   mineral harvesting assignments
    mim_of_minert = {} # mim=(mimpos,mimt), mimt is a postag.
    nminers_of_mimt = {}
    mulestart_of_ptag = {} # the frame a mule was dropped here
    # speedmining.
    # No deceleration when having a queued command at minerals. No deceleration when avoiding collisions. 
    phase_of_minert = {}
    patchpoint_of_mimt = {}
    lastppdist_of_minert = {} # distance to patchpoint last programloop
    lastspeed_of_minert = {} # log
    basepos_hash = 0 # to avoid recalculating basepos_of_mimt
    basepos_of_mimt = {} # per mimt the closest own landed base
    miningframe_of_minert = {} # per scvtag the frame it neared decidepoint (patchpoint + 3).
    hint_patch_of_scvt = {} # Hints are never cleaned, and remember a last connection to skip calculations.
    start_to_speed = 54 # othertime to start to speed from either pp=3 or standstill at waitpoint
    #
    # a reporter for an attacked builder
    reporter_of_scvt = {}
    #
    #   fighters attack somewhere
    last_center_enemies = nowhere
    home_of_fighter = {} # per tag of scv job fighter, the position of its hall.
    fighter_phase = {} # per tag of scv job fighter, a text for its phase
    fighternurse = {} # per tag of scv job fighter phase nurse, the tag of her patient.
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
    last_blocker_frame = 0
    # checks
    minedirection_of_scvt = {}
    #   ############### PLAY CHOICES
    game_phase = 'init'
    #   the planning_of_buildorder routine
    # bagofthings is a list of things, that we want to be made. No infected.
    # bagofcradle is a bagofthings, now also the cradle demand is met; flying is not sufficient.
    # bagoftree is a bagofcradle including still needed techtree demands. No infected.
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
    transformable = {} # for hoopy
    bagofthings_exe = []
    bagoftree_exe = []
    bagofcradle_exe = []
    buildseries_exe = []
    buildorder_exe = [] # like buildorder, but extra field: status='dream'/'thought'/'prep'
    planning_exe = []
    #
    buildseries_opening = []
    buildseries_old = [] # used when remaking a series
    techsequence = [] # use with self.throw_techsequence()
    techsequence_starter = SUPPLYDEPOT # when this thing is started (egg or bird), the techsequence will start
    #
    all_future_basepos = set() # used when making buildorder
    #
    throwspots = [] # (thing spot status='dream'/'thought'/'prep' owner     (thing,spot) will be unique
    #                 Also accept 'somewhere' for army and upgrades, to be actualized only when a cradle is idle.
    amount_usable = {} # per buildingtype eg barracks, count of barracks (finished or half-built), 
                       # minus count of marines etc in throwspots or eggs. Marge 12 seconds (about ambitiondura).
    amount_usable_teched = {}
    #
    but_i_had_structures = 0 # amount of own structures, excl bunkers
    but_i_had_flying = 0 # make new plans if a weak building lifted
    #
    # next structures are to retry when stopped by mappart occupied
    buildandretry = [] # (scvt, building, goal, frame) for tobuildwalk buildings
    growandretry = [] # (oldbuildingtag, newbuilding, frame) for labs and pfoc
    trainandretry = [] # (cradletype, cradletag, unitupgrade, frame) for armyunit, scv or upgrade
    purse = Cost(0,0) # to reserve the cost for the retry.
    bought_admin = [] # fills the purse a few frames, when the game is given a spend command.
    commandgiven = {} # to distinguish idles -> ordergiven -> orderaccepted
    #
    missing = '' # a string to explain a wait situation
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
    production_pause_finish = set() # of (thing, amount, building, bam). Postpone adlib thing production at amount, until bam buildings are finished.
    production_pause_egg = set() # of (thing, amount, building, bam). Postpone adlib thing production at amount, until bam buildings are in eggs or birds.
    # to abort plans
    buildorderdelay = 0
    crad_places = set()
    bui_min_lab = {}
    bui_of_pos = {}
    happy_made = set()
    strategy = [] # for some opponents, per gamechoice, the chance to make this choice.
    strategy_oppi = [] # opponent_id, to pair on stratline with strategy
    stratline = 0 # which line in strategy 
    game_choice = []
    radio_choices = 47
    game_choices = 62
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
    earn_show = False
    #
    tag_sent = False
    win_ignore = set()
    #
    # *********************************************************************************************************************
    async def on_start(self):
        self._client.game_step = self.chosen_game_step

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
        if self.frame % 23 == 22:
            await self.funchat()
        await self.act_on_errors()
        await self.gamestate1()
        self.init_step_expo()
        self.init_enemies_of_tile()
        self.init_goodguys_of_tile()
        await self.gamestate2()
        await self.get_birds()
        self.get_eggs() # after get_birds
        self.get_preps() # after get_eggs
        self.log_dreams()
        self.log_thoughts() # there is no get_thoughts()
        self.do_bought_admin()
        self.log_resource()
        self.log_armysize()
        self.log_fighters()
        self.log_purpose()
        self.log_bcs()
        self.log_orders()
        self.log_bird_history()
        self.loadcc()
        await self.manage_workers() # before planning
        if (self.frame % 5 == 4):
            self.housecleaning()
            self.escort_builders()
        if self.minerals < self.vespene:
            await self.manage_minerals()
            await self.manage_gas()
        else:
            await self.manage_gas()
            await self.manage_minerals()
        await self.get_applicants()
        await self.manage_rest()
        self.speedmining()
        self.fighters()
        await self.bunker_handling()
        await self.bunkercheese1()
        await self.bunkercheese2()
        if (self.frame % 5 == 4):
            self.idiot()
            self.implementing_buildorder_exe()
            self.make_planning_exe()
            self.follow_planning_exe()
            self.protection()
        await self.build_worker(100-self.minerals//100)
        await self.throw_advance()
        await self.start_construction()
        # army
        self.focusfire()
        self.calc_fightpos()
        self.do_attackmove()
        self.do_ghostmove()
        if (self.frame % 5 == 4):
            await self.siege_tanks()
        self.use_cluster()
        self.use_widowmine()
        await self.bc_micro()
        await self.raven_micro()
        await self.dodge_bile()
        self.liberator()
        self.destroyed()
        self.deserted()
        await self.repair_bc()
        if (self.frame % 7 == 6):
            self.maxout_sacrifice()
            self.do_repair()
            self.urgent_supplydepots_adlib()
            self.refineries_adlib()
            self.build_minima()
            self.armybuildings_adlib()
            self.techlabs_adlib()
            self.upgradebuildings_adlib()
            self.upgrades_adlib()
            self.army_adlib()
            self.pfoc_cc_adlib()
            self.urgent_ocs()
            self.turrets1_adlib()
            self.chaosbases_adlib()
            self.turrets6_adlib()
            self.lift()
            self.land()
            self.do_rally()
            self.opening_create_cut()
            self.log_buildsource()
        self.manage_the_wall()
        await self.cheese1_army()
        await self.attack_with_bc()
        await self.attack_with_rest()
        await self.worker_defence()
        await self.scv_endgame()
        if (self.frame % 11 == 10):
            await self.gasminer_boss()
            self.count_enemy()
        if (self.frame % 31 == 30):
            self.manage_layout()
            self.clean_doubling()
            self.lower_some_depots()
            self.hop_cc()
            self.yamato_admin()
            self.cluster_the_mines()
            self.manage_production_pause()
            self.lefttarget_righttarget()
            await self.send_tag()
        await self.mules()
        if (self.frame % 3 == 2):
            await self.do_buildandretry()
        await self.do_growandretry()
        await self.do_trainandretry()
        await self.do_pf_rush()
        self.do_cocoon()
        self.do_workerrush()
        await self.do211_steps()
        await self.do_banshees()
        self.handle_ghost_requests()
        await self.do_rush_ghosts()
        self.do_reaper()
        await self.catch_a_bug()
        self.blocker()
        self.continue_fleecircle()
        await self.nuke_fun()
        bunker_if.step()
        self.vulture()
        await self.marine_fun()
        await self.marauder_fun()
        await self.selfhate()
        await self.win_loss()
        #
        # preparation for next step
        self.write_enemy_structures()
        self.get_last_enemies()
        self.get_last_health()
        self.make_trail()
        self.post_idles()
        #if self.frame < 4000:
        #    self.wa_step()
        #



    # *********************************************************************************************************************
    async def my_init(self):
        self.log_success('##############################################################################')
        random.seed()
        #
        self.map_left = self.game_info.playable_area.x
        self.map_right = self.game_info.playable_area.width+self.game_info.playable_area.x
        self.map_bottom = self.game_info.playable_area.y
        self.map_top = self.game_info.playable_area.height+self.game_info.playable_area.y
        self.map_center = self.game_info.map_center
        #
        self.expansion_locations = self.expansion_locations_list.copy()
        # mapspecific
        if self.family(self.game_info.map_name) == 'atmospheres':
            mispoint = Point2((67.5, 130.5))
            correctpoint = Point2((66.5, 131.5))
            del self.expansion_locations[self.expansion_locations.index(mispoint)]
            self.expansion_locations.append(correctpoint)
            mispoint = Point2((156.5, 73.5))
            correctpoint = Point2((157.5, 72.5))
            del self.expansion_locations[self.expansion_locations.index(mispoint)]
            self.expansion_locations.append(correctpoint)
        #
        self.init_all_minerals()
        self.init_all_vespene()
        self.init_expo()
        self.init_step_expo()
        self.all_categories = {'worker','army','base','armybuilding','upgradebuilding','upgrade'
            ,'otherbuilding','lab','e'}
        # expected_order
        self.init_expected_order('mimminer', AbilityId.HARVEST_RETURN)
        self.init_expected_order('mimminer', AbilityId.HARVEST_GATHER)
        self.init_expected_order('mimminer', AbilityId.MOVE)
        self.init_expected_order('gasminer', AbilityId.HARVEST_RETURN)
        self.init_expected_order('gasminer', AbilityId.HARVEST_GATHER)
        self.init_expected_order('volunteer', AbilityId.HARVEST_RETURN)
        self.init_expected_order('volunteer', AbilityId.HARVEST_GATHER)
        self.init_expected_order('inshock', AbilityId.MOVE)
        self.init_expected_order('fleeer', AbilityId.MOVE)
        self.init_expected_order('traveller', AbilityId.MOVE)
        self.init_expected_order('traveller', AbilityId.HARVEST_GATHER) # mineralwalking
        self.init_expected_order('settler', AbilityId.MOVE)
        self.init_expected_order('fencer', AbilityId.MOVE)
        self.init_expected_order('escorter', AbilityId.ATTACK)
        self.init_expected_order('reporter', AbilityId.ATTACK)
        self.init_expected_order('applicant', AbilityId.MOVE)
        self.init_expected_order('carrier', AbilityId.HARVEST_RETURN)
        self.init_expected_order('scout', AbilityId.MOVE)
        self.init_expected_order('cheeser', AbilityId.MOVE)
        self.init_expected_order('cheeser', AbilityId.HARVEST_GATHER) # mineralwalking
        self.init_expected_order('suicider', AbilityId.ATTACK)
        self.init_expected_order('fighter', AbilityId.ATTACK)
        self.init_expected_order('fighter', AbilityId.HARVEST_GATHER) # mineralwalking
        self.init_expected_order('fighter',AbilityId.EFFECT_REPAIR)
        self.init_expected_order('fighter', AbilityId.MOVE)
        self.init_expected_order('repairer',AbilityId.EFFECT_REPAIR)
        self.init_expected_order('sacrifice', AbilityId.ATTACK)
        self.init_expected_order('suicider', AbilityId.ATTACK)
        #
        self.win_ignore = {SPORECRAWLER,SPINECRAWLER,AUTOTURRET,CREEPTUMOR,CREEPTUMORBURROWED}
        # liftable
        self.liftable = [BARRACKS,FACTORY,STARPORT,COMMANDCENTER,ORBITALCOMMAND]
        self.landable = [BARRACKSFLYING,FACTORYFLYING,STARPORTFLYING,COMMANDCENTERFLYING,ORBITALCOMMANDFLYING]
        # enemy air with weak air defence, and fighters
        self.viking_targets = [BANSHEE,LIBERATOR,LIBERATORAG,ORACLE,BROODLORD,OVERLORD,OBSERVER,BATTLECRUISER,
                               CORRUPTOR,MUTALISK,TEMPEST,VIPER, VIKINGFIGHTER,PHOENIX,OVERSEER]
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
        if self.enemy_species != 'zerg':
            self.init_bcenemy(BATTLECRUISER, 50, 3)
            self.init_bcenemy(VIKINGFIGHTER, 35, 5)
            self.init_bcenemy(MISSILETURRET, 60, 6)
            self.init_bcenemy(THOR, 40, 3)
            self.init_bcenemy(PHOENIX, 35, 5)
            self.init_bcenemy(RAVEN, 30, 5)
            self.init_bcenemy(MARINE, 10, 2)
            self.init_bcenemy(SCV, 0, 1)
        self.init_bcenemy(HYDRALISK, 20, 3)
        self.init_bcenemy(VIPER, 30, 4)
        self.init_bcenemy(VOIDRAY, 35, 5)
        self.init_bcenemy(RAVAGER, 20, 2)
        self.init_bcenemy(CYCLONE, 50, 5)
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
        self.all_techlabs = [BARRACKSTECHLAB,FACTORYTECHLAB,STARPORTTECHLAB,TECHLAB]
        self.all_reactors = [BARRACKSREACTOR,FACTORYREACTOR,STARPORTREACTOR,REACTOR]
        self.standalone_labs = [TECHLAB,REACTOR]
        self.all_pfoc = [PLANETARYFORTRESS,ORBITALCOMMAND]
        self.all_workertypes = [SCV,PROBE,DRONE]
        # list of structures, with species, category,builddura, size. Can be flying, can be lowered.
        self.init_structures('T','otherbuilding',SUPPLYDEPOT, 21, 2)
        self.init_structures('T','otherbuilding',SUPPLYDEPOTLOWERED, 21, 2)
        self.init_structures('T','armybuilding',BARRACKS, 46, 3)
        self.init_structures('T','armybuilding',BARRACKSFLYING, 46, 3)
        self.init_structures('T','otherbuilding',REFINERY, 21, 3)
        self.init_structures('T','lab',BARRACKSTECHLAB, 18, 2)
        self.init_structures('T','armybuilding',FACTORY, 43, 3)
        self.init_structures('T','armybuilding',FACTORYFLYING, 43, 3)
        self.init_structures('T','lab',FACTORYTECHLAB, 18, 2)
        self.init_structures('T','armybuilding',STARPORT, 36, 3)
        self.init_structures('T','armybuilding',STARPORTFLYING, 36, 3)
        self.init_structures('T','lab',STARPORTTECHLAB, 18, 2)
        self.init_structures('T','lab',TECHLAB, 18, 2)
        self.init_structures('T','upgradebuilding',FUSIONCORE,46, 3)
        self.init_structures('T','base',COMMANDCENTER, 71, 5)
        self.init_structures('T','base',COMMANDCENTERFLYING, 71, 5)
        self.init_structures('T','base',PLANETARYFORTRESS, 36, 5)
        self.init_structures('T','base',ORBITALCOMMAND, 25, 5)
        self.init_structures('T','base',ORBITALCOMMANDFLYING, 25, 5)
        self.init_structures('T','upgradebuilding',ENGINEERINGBAY, 25, 3)
        self.init_structures('T','otherbuilding',MISSILETURRET,18, 2)
        self.init_structures('T','upgradebuilding',ARMORY, 46, 3)
        self.init_structures('T','otherbuilding',BUNKER, 29, 3)
        self.init_structures('T','otherbuilding',SENSORTOWER, 18, 2)
        self.init_structures('T','upgradebuilding',GHOSTACADEMY, 20, 3)
        self.init_structures('T','lab',BARRACKSREACTOR, 36, 2)
        self.init_structures('T','lab',FACTORYREACTOR, 36, 2)
        self.init_structures('T','lab',STARPORTREACTOR, 36, 2)
        self.init_structures('T','lab',REACTOR, 36, 2)
        self.init_structures('T','otherbuilding',AUTOTURRET, 0, 2)
        # protoss added for layout
        self.init_structures('P','e',NEXUS, 71, 5)
        self.init_structures('P','e',PYLON, 18, 2)
        self.init_structures('P','e',ASSIMILATOR, 21, 3)
        self.init_structures('P','e',GATEWAY, 46, 3)
        self.init_structures('P','e',FORGE, 32, 3)
        self.init_structures('P','e',PHOTONCANNON, 29, 2)
        self.init_structures('P','e',SHIELDBATTERY, 29, 2)
        self.init_structures('P','e',WARPGATE, 7, 3)
        self.init_structures('P','e',CYBERNETICSCORE, 36, 3)
        self.init_structures('P','e',TWILIGHTCOUNCIL, 36, 3)
        self.init_structures('P','e',ROBOTICSFACILITY, 46, 3)
        self.init_structures('P','e',STARGATE, 43, 3)
        self.init_structures('P','e',TEMPLARARCHIVE, 36, 3)
        self.init_structures('P','e',DARKSHRINE, 71, 2)
        self.init_structures('P','e',ROBOTICSBAY, 46, 3)
        self.init_structures('P','e',FLEETBEACON, 43, 3)
        self.init_structures('P','e',ORACLESTASISTRAP, 11, 1)
        # zerg
        self.init_structures('Z','e',HATCHERY, 71, 5)
        self.init_structures('Z','e',LAIR, 57, 5)
        self.init_structures('Z','e',HIVE, 71, 5)
        self.init_structures('Z','e',EXTRACTOR, 21, 3)
        self.init_structures('Z','e',SPAWNINGPOOL, 46, 3)
        self.init_structures('Z','e',SPINECRAWLER, 36, 2)
        self.init_structures('Z','e',SPORECRAWLER, 21, 2)
        self.init_structures('Z','e',EVOLUTIONCHAMBER, 25, 3)
        self.init_structures('Z','e',ROACHWARREN, 39, 3)
        self.init_structures('Z','e',BANELINGNEST, 43, 3)
        self.init_structures('Z','e',HYDRALISKDEN, 29, 3)
        self.init_structures('Z','e',LURKERDEN, 57, 3)
        self.init_structures('Z','e',SPIRE, 71, 3)
        self.init_structures('Z','e',GREATERSPIRE, 71, 3)
        self.init_structures('Z','e',NYDUSNETWORK, 36, 3)
        self.init_structures('Z','e',NYDUSCANAL, 14, 3)
        self.init_structures('Z','e',INFESTATIONPIT, 36, 3)
        self.init_structures('Z','e',ULTRALISKCAVERN, 46, 3)
        self.init_structures('Z','e',CREEPTUMOR, 11, 1)
        self.init_structures('Z','e',CREEPTUMORBURROWED, 11, 1)
        # add for cheese with barracks and bunker
        # warning: this complicated much. Restrict to buildseries and placement.txt
        self.init_structures('T','armybuilding',INFESTEDBARRACKS, 46, 3)
        self.init_structures('T','armybuilding',INFESTEDBUNKER, 29, 3)
        self.init_structures('T','armybuilding',INFESTEDFACTORY, 43, 3)
        self.init_structures('T','armybuilding',INFESTEDSTARPORT, 36, 3)
        self.init_structures('T','otherbuilding',INFESTEDCOCOON, 50, 8)
        self.init_structures('T','otherbuilding',MAINCELLBLOCK, 0, 5)
        # scv
        self.builddura_of_thing[SCV] = 12
        self.airground_of_unit[SCV] = 'ground'
        self.category_of_thing[SCV] = 'worker'
        # mule
        self.category_of_thing[MULE] = 'worker'
        self.airground_of_unit[MULE] = 'ground'
        self.builddura_of_thing[MULE] = 0
        # army, builddura, supply, is air/ground
        self.init_army(MARINE,18,1,'ground')
        self.init_army(MARAUDER,21,2,'ground')
        self.init_army(REAPER,32,1,'ground')
        self.init_army(HELLION,21,2,'ground')
        self.init_army(HELLIONTANK,21,2,'ground')
        self.init_army(CYCLONE,32,3,'ground')
        self.init_army(WIDOWMINE,21,2,'ground')
        self.init_army(WIDOWMINEBURROWED,21,2,'ground')
        self.init_army(SIEGETANK,32,3,'ground')
        self.init_army(SIEGETANKSIEGED,32,3,'ground')
        self.init_army(VIKINGFIGHTER,30,2,'air')
        self.init_army(VIKINGASSAULT,30,2,'ground')
        self.init_army(MEDIVAC,30,2,'air')
        self.init_army(RAVEN,43,2,'air')
        self.init_army(LIBERATOR,43,3,'air')
        self.init_army(LIBERATORAG,43,3,'air')
        self.init_army(BANSHEE,43,2,'air')
        self.init_army(BATTLECRUISER,64,6,'air')
        self.init_army(GHOST,29,2,'ground')
        self.init_army(NUKESILONOVA,43,0,'ground')
        # upgrade, builddura
        self.init_upgrade(PUNISHERGRENADES, 43, MARAUDER)
        self.init_upgrade(STIMPACK, 100, MARINE)
        self.init_upgrade(SHIELDWALL, 79, MARINE)
        self.init_upgrade(TERRANSHIPWEAPONSLEVEL1, 114, BATTLECRUISER)
        self.init_upgrade(TERRANSHIPWEAPONSLEVEL2, 136, BATTLECRUISER)
        self.init_upgrade(TERRANSHIPWEAPONSLEVEL3, 157, BATTLECRUISER)
        self.init_upgrade(TERRANVEHICLEANDSHIPARMORSLEVEL1, 114, BATTLECRUISER)
        self.init_upgrade(TERRANVEHICLEANDSHIPARMORSLEVEL2, 136, BATTLECRUISER)
        self.init_upgrade(TERRANVEHICLEANDSHIPARMORSLEVEL3, 157, BATTLECRUISER)
        self.init_upgrade(TERRANBUILDINGARMOR, 100, PLANETARYFORTRESS)
        self.init_upgrade(HISECAUTOTRACKING,57, MISSILETURRET)
        self.init_upgrade(TERRANINFANTRYWEAPONSLEVEL1, 114, MARINE)
        self.init_upgrade(TERRANINFANTRYWEAPONSLEVEL2, 136, MARINE)
        self.init_upgrade(TERRANINFANTRYWEAPONSLEVEL3, 157, MARINE)
        self.init_upgrade(TERRANINFANTRYARMORSLEVEL1, 114, MARINE)
        self.init_upgrade(TERRANINFANTRYARMORSLEVEL2, 136, MARINE)
        self.init_upgrade(TERRANINFANTRYARMORSLEVEL3, 157, MARINE)
        self.init_upgrade(BATTLECRUISERENABLESPECIALIZATIONS, 100, BATTLECRUISER)
        self.init_upgrade(PERSONALCLOAKING, 86, GHOST)
        self.init_upgrade(DRILLCLAWS, 79, WIDOWMINEBURROWED)
        self.init_upgrade(CYCLONELOCKONDAMAGEUPGRADE, 100, CYCLONE)
        self.init_upgrade(BANSHEECLOAK, 79, BANSHEE)
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
        self.init_cradle(HELLIONTANK,FACTORY)
        self.init_cradle(BATTLECRUISER,STARPORT)
        self.init_cradle(BARRACKSTECHLAB,BARRACKS)
        self.init_cradle(FACTORYTECHLAB,FACTORY)
        self.init_cradle(STARPORTTECHLAB,STARPORT)
        self.init_cradle(BARRACKSREACTOR,BARRACKS)
        self.init_cradle(FACTORYREACTOR,FACTORY)
        self.init_cradle(STARPORTREACTOR,STARPORT)
        self.init_cradle(PUNISHERGRENADES,BARRACKSTECHLAB)
        self.init_cradle(STIMPACK,BARRACKSTECHLAB)
        self.init_cradle(SHIELDWALL,BARRACKSTECHLAB)
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
        self.init_cradle(DRILLCLAWS,FACTORYTECHLAB)
        self.init_cradle(BANSHEECLOAK,STARPORTTECHLAB)
        self.init_cradle(CYCLONELOCKONDAMAGEUPGRADE,FACTORYTECHLAB)
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
        self.init_techtree(AUTOTURRET,RAVEN)
        self.init_techtree(GHOSTACADEMY,BARRACKS)
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
        self.init_techtree(HELLIONTANK,ARMORY)
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
        self.init_techtree(DRILLCLAWS,ARMORY)
        #
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
        self.init_maxhealth(CREEPTUMORBURROWED, 50)
        self.init_maxhealth(INFESTEDBARRACKS, 1000)
        self.init_maxhealth(INFESTEDBUNKER, 400)
        self.init_maxhealth(INFESTEDFACTORY, 1250)
        self.init_maxhealth(INFESTEDSTARPORT, 1300)
        self.init_maxhealth(INFESTEDCOCOON, 0)
        self.init_maxhealth(MAINCELLBLOCK, 0)
        self.init_maxhealth(SCV, 45)
        self.init_maxhealth(MARINE, 45)
        self.init_maxhealth(MARAUDER, 125)
        self.init_maxhealth(REAPER, 60)
        self.init_maxhealth(HELLION, 90)
        self.init_maxhealth(HELLIONTANK, 135)
        self.init_maxhealth(CYCLONE, 120)
        self.init_maxhealth(WIDOWMINE, 90)
        self.init_maxhealth(WIDOWMINEBURROWED, 90)
        self.init_maxhealth(SIEGETANK, 175)
        self.init_maxhealth(SIEGETANKSIEGED, 175)
        self.init_maxhealth(VIKINGFIGHTER, 125)
        self.init_maxhealth(VIKINGASSAULT, 125)
        self.init_maxhealth(MEDIVAC, 150)
        self.init_maxhealth(RAVEN, 140)
        self.init_maxhealth(LIBERATOR, 180)
        self.init_maxhealth(LIBERATORAG, 180)
        self.init_maxhealth(BANSHEE, 140)
        self.init_maxhealth(BATTLECRUISER, 550)
        self.init_maxhealth(GHOST, 100)
        self.init_maxhealth(NUKESILONOVA, 0)
        self.init_maxhealth(AUTOTURRET, 150)
        #
        self.init_nine()
        #
        # enemy_species
        if self.enemy_race == Race.Zerg:
            self.enemy_species = 'zerg'
        elif self.enemy_race == Race.Terran:
            self.enemy_species = 'terran'
        elif self.enemy_race == Race.Protoss:
            self.enemy_species = 'protoss'
        else:
            self.enemy_species = 'someone'
        # opponent
        self.opponent = self.opponent_id
        if self.opponent is None:
            self.opponent = self.enemy_species
        #
        self.enemy_pos = self.enemy_start_locations[0].position
        self.lefttarget = self.enemy_pos
        self.righttarget = self.enemy_pos
        self.loved_pos = self.start_location.position
        self.loved_expo = self.expo_of_pos(self.loved_pos)
        self.cheese2_triedexp.add(self.enemy_pos)
        self.target_loc = self.enemy_pos
        self.cc_destiny[self.loved_pos] = 'oc'
        #
        self.ground_strength_hist.add((SPINECRAWLER,63.67))
        self.air_strength_hist.add((SPORECRAWLER,83.49))
        self.ground_strength_hist.add((PHOTONCANNON,69.29))
        self.air_strength_hist.add((PHOTONCANNON,69.29))
        self.air_strength_hist.add((MISSILETURRET, 83.49))
        self.ground_strength_hist.add((PLANETARYFORTRESS, 173.21))
        #
        if self.enemy_species == 'zerg':
            self.enemy_structureinfo.add((HATCHERY,self.enemy_pos))
            self.enemy_structureinfo_plus.add((HATCHERY,self.enemy_pos,0))
        elif self.enemy_species == 'protoss':
            self.enemy_structureinfo.add((NEXUS, self.enemy_pos))
            self.enemy_structureinfo_plus.add((NEXUS, self.enemy_pos,0))
        else: # random or terran
            self.enemy_structureinfo.add((COMMANDCENTER, self.enemy_pos))
            self.enemy_structureinfo_plus.add((COMMANDCENTER, self.enemy_pos,0))
        #
        # botnames
        pl = open('data/botnames.txt','r')
        lines = pl.read().splitlines()
        pl.close()
        self.botnames = {}
        for line in lines:
            words = line.split()
            code = words[0]
            human = words[1]
            self.botnames[code] = human
            #print('bot '+code+' = '+human)
        #
        # vulture
        self.init_vulture()
        # all_repairable_shooters for repair priority
        self.all_repairable_shooters = {PLANETARYFORTRESS, MISSILETURRET, BUNKER}
        for ut in self.all_army:
            if ut not in [MARINE,MARAUDER,REAPER,GHOST]: # bio
                self.all_repairable_shooters.add(ut)
        # strategy choices
        await self.init_strategy()
        #
        # hisleft, hisright are mapcorners on different sides of the enemy.
        bestsd = 99999
        for corner in [(self.map_left,self.map_top),(self.map_right,self.map_bottom),(self.map_right,self.map_top),(self.map_left,self.map_bottom)]:
            pos = Point2(corner)
            sd = self.sdist(pos,self.enemy_pos)
            if sd < bestsd:
                bestsd = sd
                enemycorner = pos
        bestsd = 99999
        for corner in [(self.map_left,self.map_top),(self.map_right,self.map_bottom),(self.map_right,self.map_top),(self.map_left,self.map_bottom)]:
            pos = Point2(corner)
            if pos != enemycorner:
                sd = self.sdist(pos,enemycorner)
                if sd < bestsd:
                    bestsd = sd
                    self.hisleft = pos
        bestsd = 99999
        for corner in [(self.map_left,self.map_top),(self.map_right,self.map_bottom),(self.map_right,self.map_top),(self.map_left,self.map_bottom)]:
            pos = Point2(corner)
            if pos not in {enemycorner,self.hisleft}:
                sd = self.sdist(pos,enemycorner)
                if sd < bestsd:
                    bestsd = sd
                    self.hisright = pos
        # layout
        self.get_layout()
        # append base positions to layout.txt for placer.py to compute placement tips
        for pos in self.expansion_locations:
            self.write_layout(COMMANDCENTER,pos)
        #
        layout_if.mapname = self.family(self.game_info.map_name)
        layout_if.startx = self.loved_pos.x
        layout_if.starty = self.loved_pos.y
        layout_if.enemyx = self.enemy_pos.x
        layout_if.enemyy = self.enemy_pos.y
        #
        layout_if.save_layout() # saves as data\layout.txt for placer.py
        # now we use layout ourselves too
        #
        for pos in self.expansion_locations:
            self.erase_layout(COMMANDCENTER,pos)
        # possible_cc_positions, layout MAINCELLBLOCK to prevent future misuse
        self.possible_cc_positions = set()
        for pos in self.expansion_locations:
            self.add_possible_cc_position(pos)
        #
        self.write_layout(COMMANDCENTER,self.loved_pos)
        self.write_layout(COMMANDCENTER,self.enemy_pos)
        self.init_airports()
        #
        for cc in self.structures(COMMANDCENTER):
            self.readies_start[cc.tag] = -99999
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
                self.cheese1_prison_pos = Point2((float(woord[2]), float(woord[3])))
            elif (woord[0] == 'position') and (woord[1] == 'INFESTEDBARRACKS'):
                self.cheese1_barracks_pos = Point2((float(woord[2]), float(woord[3])))
            elif (woord[0] == 'position') and (woord[1] == 'INFESTEDFACTORY'):
                self.cheese1_factory_pos = Point2((float(woord[2]), float(woord[3])))
            elif (woord[0] == 'position') and (woord[1] == 'INFESTEDLANDING'):
                self.cheese1_landing_pos = Point2((float(woord[2]), float(woord[3])))
            elif (woord[0] == 'position') and (woord[1] == 'INFESTEDBUNKER'):
                self.cheese1_bunker_pos = Point2((float(woord[2]), float(woord[3])))
            elif (woord[0] == 'position') and (woord[1] == 'INFESTEDTANK'):
                self.cheese1_tank_pos = Point2((float(woord[2]), float(woord[3])))
            elif (woord[0] == 'position') and (woord[1] == 'INFESTEDSTARPORT'):
                self.cheese1_starport_pos = Point2((float(woord[2]), float(woord[3])))
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
            elif (woord[0] == 'position') and (woord[1] == 'HOMENATURAL'):
                self.homenatural_pos = Point2((float(woord[2]), float(woord[3])))
            elif (woord[0] == 'position') and (woord[1] == 'HOMENATURALCHOKE'):
                self.homenaturalchoke_pos = Point2((float(woord[2]), float(woord[3])))
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
            elif (woord[0] == 'position') and (woord[1] == 'EXTRACC'):
                ccpos = Point2((float(woord[2]), float(woord[3])))
                self.add_possible_cc_position(ccpos)
            elif (woord[0] == 'position') and (woord[1] == 'FOLLOWERS'):
                self.followers = Point2((float(woord[2]), float(woord[3])))
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
        # INFESTEDCOCOON is sometimes not in placement.txt, init it here
        if self.cheese3_cocoon_pos == self.nowhere:
            self.cheese3_cocoon_pos = self.init_cheese_position(self.enemynaturalchoke_pos,35,45,INFESTEDCOCOON)
        self.erase_layout(INFESTEDCOCOON,self.cheese3_cocoon_pos)
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
        for pos in self.expansion_locations:
            if pos != self.enemy_pos:
                if self.proxy(pos):
                    visit.append(pos.towards(self.map_center, 4))
                    visit.append(pos.towards(self.map_center, 6))
                else:
                    visit.append(pos.towards(self.map_center, -1))
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
        if self.family(self.game_info.map_name) == 'goldenwall':
            self.miner_bound = 18
            if self.loved_pos.x > 100:
                viewpos = Point2((165,45))
            else:
                viewpos = Point2((43,45))
            self.chosenplaces.append((SUPPLYDEPOT, viewpos))
        #
        # reassign wall_barracks_pos tile to loved_pos expo
        # this should help to repair the wall
        maptile = self.maptile_of_pos(self.loved_pos)
        chosen_expo = self.expo_of_maptile[maptile]
        maptile = self.maptile_of_pos(self.wall_barracks_pos)
        self.expo_of_maptile[maptile] = chosen_expo
        #
        # idiot_plan to be used when floating minerals
        block = [COMMANDCENTER, SCV,SCV,SCV,SCV,SCV,SCV,SCV,SCV, REFINERY, SCV,SCV,SCV, SCV, REFINERY,
                 SUPPLYDEPOT, STARPORT, SCV, SCV, SCV, SCV, STARPORTTECHLAB, BATTLECRUISER]
        self.idiot_plan = [COMMANDCENTER, SCV, SCV, SCV, SCV, SCV, SCV, SCV, SCV, SUPPLYDEPOT, BARRACKS, MARINE, MARINE,
                            SCV, SCV, SCV, SCV, ORBITALCOMMAND, COMMANDCENTER, BARRACKS, REFINERY,
                            MARINE, MARINE, FACTORY, REFINERY, ENGINEERINGBAY, PLANETARYFORTRESS,
                            STARPORT, BANSHEE, SCV, SCV, SCV, SCV, MARINE, MARINE, SUPPLYDEPOT, REFINERY,
                            FACTORYTECHLAB, STARPORTTECHLAB, SIEGETANK, FUSIONCORE, BATTLECRUISER,
                            ARMORY, TERRANSHIPWEAPONSLEVEL1]
        self.idiot_plan += block + block + block + [RAVEN, BATTLECRUISER, BATTLECRUISER]

        # standard reaper_goal
        self.reaper_goal = self.enemynatural_pos.towards(self.enemy_pos,-3)
        #
        self.init_liberator_spots()
        # opening
        cocoon_series = [SUPPLYDEPOT, BARRACKS, BARRACKS, SUPPLYDEPOT, MARINE, BUNKER, MARINE, BUNKER, MARINE, MARINE, MARINE]
        banshee_series = [SUPPLYDEPOT, REFINERY, BARRACKS, FACTORY, SUPPLYDEPOT, REFINERY,
                                    STARPORT, STARPORT, BARRACKSTECHLAB, SUPPLYDEPOT, FACTORYTECHLAB]
        if self.game_choice[0]:
            self.opening_name = 'twobase-bc'
            self.buildseries_opening = [SUPPLYDEPOT, REFINERY, BARRACKS, SUPPLYDEPOT, MARINE, REFINERY, FACTORY, MARINE,
                                       STARPORT, COMMANDCENTER, FUSIONCORE, STARPORTTECHLAB, BATTLECRUISER]
        elif self.game_choice[1]:
            self.opening_name = 'elementary'
            self.buildseries_opening = [SUPPLYDEPOT, REFINERY, BARRACKS, SUPPLYDEPOT, MARINE, ORBITALCOMMAND]
        elif self.game_choice[2]:
            self.opening_name = 'cheese-expand'
            self.buildseries_opening = [SUPPLYDEPOT, INFESTEDBARRACKS, REFINERY, INFESTEDBUNKER, SUPPLYDEPOT, INFESTEDFACTORY,
                                        BARRACKS, REFINERY, COMMANDCENTER]
        elif self.game_choice[3]:
            self.opening_name = 'cheese-bc'
            self.buildseries_opening = [SUPPLYDEPOT, INFESTEDBARRACKS, REFINERY, INFESTEDBUNKER,
                                        SUPPLYDEPOT, INFESTEDFACTORY, BARRACKS, REFINERY,
                                        STARPORT, SUPPLYDEPOT, FUSIONCORE, STARPORTTECHLAB, SUPPLYDEPOT, BATTLECRUISER]
        elif self.game_choice[4]:
            self.opening_name = 'expand'
            self.buildseries_opening = [SUPPLYDEPOT, COMMANDCENTER, BARRACKS, SUPPLYDEPOT]
        elif self.game_choice[5]:
            self.opening_name = 'double-expand'
            self.buildseries_opening = [SUPPLYDEPOT, COMMANDCENTER, COMMANDCENTER, BARRACKS, REFINERY, ENGINEERINGBAY,
                                        PLANETARYFORTRESS]
        elif self.game_choice[6]:
            self.opening_name = 'cheese-bunk'
            self.buildseries_opening = [SUPPLYDEPOT, INFESTEDBARRACKS, INFESTEDBUNKER, INFESTEDBUNKER,
                                        INFESTEDBUNKER, SUPPLYDEPOT, REFINERY, INFESTEDFACTORY, BARRACKS, REFINERY]
            self.get_shield_pos()
        elif self.game_choice[7]:
            self.opening_name = 'rush-bc'
            self.rushopening = True
            self.buildseries_opening = [SUPPLYDEPOT, REFINERY, BARRACKS, SUPPLYDEPOT, MARINE, FACTORY, REFINERY, MARINE,
                                       STARPORT, FUSIONCORE, STARPORTTECHLAB, BATTLECRUISER, COMMANDCENTER]
        elif self.game_choice[8]:
            self.opening_name = 'defence'
            self.buildseries_opening = [SUPPLYDEPOT, REFINERY, BARRACKS, SUPPLYDEPOT, MARINE, FACTORY, MARINE,
                                        FACTORYTECHLAB, MARINE, SUPPLYDEPOT, SIEGETANK, ENGINEERINGBAY]
        elif self.game_choice[9]:
            self.opening_name = 'pf-rush'
            self.rushopening = True
            self.cc_destiny_rush = True # fast oc
            self.buildseries_opening = [SUPPLYDEPOT, BARRACKS, BUNKER, MARINE, COMMANDCENTER, REFINERY,
                                        MARINE, SUPPLYDEPOT, ENGINEERINGBAY, MARINE, REFINERY,
                                        MARINE, FACTORY, TERRANBUILDINGARMOR]
            self.init_pf_rush()
        elif self.game_choice[10]:
            self.opening_name = 'expa-ma'
            self.buildseries_opening = [SUPPLYDEPOT, COMMANDCENTER, BARRACKS, SUPPLYDEPOT, REFINERY, COMMANDCENTER,
                                        BARRACKS, BARRACKS, FACTORY, COMMANDCENTER, FACTORYTECHLAB,SIEGETANK]
            self.opening_create = {(MARINE,15)}
            self.rushopening = True
            self.cc_destiny_rush = True
        elif self.game_choice[11]:
            self.opening_name = 'cocoon'
            self.rushopening = True
            self.buildseries_opening = cocoon_series + [REFINERY, INFESTEDFACTORY, MARINE, COMMANDCENTER, MARINE, FACTORYTECHLAB, SIEGETANK]
            self.init_cocoon()
        elif self.game_choice[12]:
            self.opening_name = 'triple-expand'
            self.buildseries_opening = [SUPPLYDEPOT, COMMANDCENTER, COMMANDCENTER, BARRACKS, SUPPLYDEPOT, COMMANDCENTER, MARINE, ENGINEERINGBAY]
        elif self.game_choice[13]:
            self.opening_name = 'liberator-cc'
            self.rushopening = True
            self.cc_destiny_rush = True
            self.buildseries_opening = [SUPPLYDEPOT, REFINERY, BARRACKS, MARINE, INFESTEDFACTORY, REFINERY,
                                        STARPORT, LIBERATOR, COMMANDCENTER]
            self.place_proxy(STARPORT, 60)
        elif self.game_choice[14]:
            self.opening_name = 'liberator-bc'
            self.rushopening = True
            self.cc_destiny_rush = True
            self.buildseries_opening = [SUPPLYDEPOT, REFINERY, BARRACKS, MARINE, INFESTEDFACTORY, REFINERY,
                                        STARPORT, LIBERATOR, FUSIONCORE, STARPORTTECHLAB, BATTLECRUISER, COMMANDCENTER]
            self.place_proxy(STARPORT,60)
        elif self.game_choice[15]:
            self.opening_name = 'liberator-tank'
            self.rushopening = True
            self.buildseries_opening = [SUPPLYDEPOT, REFINERY, BARRACKS, SUPPLYDEPOT, MARINE, FACTORY, REFINERY,
                                        STARPORT, FACTORYTECHLAB, LIBERATOR, SIEGETANK, LIBERATOR]
            self.place_proxy(STARPORT, 60)
            self.place_proxy(FACTORY, 60)
        elif self.game_choice[16]:
            self.opening_name = 'reapers'
            self.buildseries_opening = [SUPPLYDEPOT, REFINERY, BARRACKS, REAPER, SUPPLYDEPOT, REAPER, BUNKER, BUNKER,
                                        BARRACKS, REFINERY]
            self.init_reapers()
            self.opening_create = {(REAPER,3)}
        elif self.game_choice[17]:
            self.opening_name = 'two liberators'
            self.rushopening = True
            self.buildseries_opening = [SUPPLYDEPOT, REFINERY, BARRACKS, SUPPLYDEPOT, REFINERY, FACTORY, MARINE,
                                        STARPORT, STARPORT, LIBERATOR, LIBERATOR]
            self.place_proxy(STARPORT,45)
            self.place_proxy(STARPORT, 40)
        elif self.game_choice[18]:
            self.opening_name = 'marauders'
            self.rushopening = True
            self.buildseries_opening = [SUPPLYDEPOT, BARRACKS, REFINERY, SUPPLYDEPOT,
                                        INFESTEDBARRACKS, INFESTEDBUNKER, INFESTEDBARRACKS, ORBITALCOMMAND,
                                        BARRACKSTECHLAB, BARRACKSTECHLAB, BARRACKSTECHLAB,
                                        MARAUDER, MARAUDER, MARAUDER, PUNISHERGRENADES]
            for (lab,pos) in self.unthinkable:
                if lab == BARRACKSTECHLAB:
                    del self.buildseries_opening[self.buildseries_opening.index(BARRACKSTECHLAB)]
                    del self.buildseries_opening[self.buildseries_opening.index(MARAUDER)]
            self.init_marauders()
            self.opening_create = {(MARAUDER,12)}
            self.production_pause_finish.add((SCV,18,BARRACKS,2))
        elif self.game_choice[19]:
            self.opening_name = 'stimmed-marauders'
            self.rushopening = True
            self.buildseries_opening = [SUPPLYDEPOT, BARRACKS, REFINERY, SUPPLYDEPOT,
                                        INFESTEDBARRACKS, INFESTEDBUNKER, INFESTEDBARRACKS, MARINE,
                                        ORBITALCOMMAND, BARRACKSTECHLAB, BARRACKSTECHLAB, BARRACKSTECHLAB,
                                        STIMPACK, MARAUDER, MARAUDER, MARAUDER, PUNISHERGRENADES]
            for (lab,pos) in self.unthinkable:
                if lab == BARRACKSTECHLAB:
                    del self.buildseries_opening[self.buildseries_opening.index(BARRACKSTECHLAB)]
                    del self.buildseries_opening[self.buildseries_opening.index(MARAUDER)]
            self.init_marauders()
            self.opening_create = {(MARAUDER,20)}
        elif self.game_choice[20]:
            self.opening_name = 'marine-1'
            self.init_marine_opening(1)
        elif self.game_choice[21]:
            self.opening_name = 'marine-2'
            self.init_marine_opening(2)
        elif self.game_choice[22]:
            self.opening_name = 'marine-3'
            self.init_marine_opening(3)
        elif self.game_choice[23]:
            self.opening_name = 'marine-4'
            self.init_marine_opening(4)
        elif self.game_choice[24]:
            self.opening_name = 'marine-5'
            self.init_marine_opening(5)
        elif self.game_choice[25]:
            self.opening_name = 'marine-6'
            self.init_marine_opening(6)
        elif self.game_choice[26]:
            self.opening_name = 'cocoon-marine-3'
            self.rushopening = True
            self.buildseries_opening = cocoon_series
            self.init_cocoon()
            self.init_marine_opening(3)
        elif self.game_choice[27]:
            self.opening_name = 'cocoon-marine-4'
            self.rushopening = True
            self.buildseries_opening = cocoon_series
            self.init_cocoon()
            self.init_marine_opening(4)
        elif self.game_choice[28]:
            self.opening_name = 'cocoon-marine-5'
            self.rushopening = True
            self.buildseries_opening = cocoon_series
            self.init_cocoon()
            self.init_marine_opening(5)
        elif self.game_choice[29]:
            self.opening_name = 'cocoon-widowmine'
            self.rushopening = True
            self.buildseries_opening = cocoon_series + [ORBITALCOMMAND, REFINERY, COMMANDCENTER, FACTORY, FACTORY, ORBITALCOMMAND]
            self.init_cocoon()
            self.opening_create = {(WIDOWMINE,8)}
            self.production_pause_finish.add((REFINERY, 1, FACTORY, 1))
            # factories random placing
            facs = 0
            while facs < 3:
                around = self.random_mappoint()
                while self.proxy(around) or (not self.near(around,self.map_center,60)):
                    around = self.random_mappoint()
                place = self.place_around(FACTORY, around)
                nearminerals = False
                for (mimpos,mimt) in self.all_minerals:
                    if self.near(place,mimpos,4):
                        nearminerals = True
                if not nearminerals:
                    self.chosenplaces.append((FACTORY, place))
                    facs += 1
        elif self.game_choice[30]:
            self.opening_name = 'cocoon-bc'
            self.rushopening = True
            self.buildseries_opening = cocoon_series + [REFINERY, ORBITALCOMMAND, FACTORY, REFINERY,
                                        STARPORT, COMMANDCENTER, FUSIONCORE, STARPORTTECHLAB, BATTLECRUISER]
            self.init_cocoon()
        elif self.game_choice[31]:
            self.opening_name = 'cocoon-3bc'
            self.rushopening = True
            self.buildseries_opening = cocoon_series + [REFINERY, INFESTEDFACTORY, COMMANDCENTER, REFINERY,
                                        FACTORYTECHLAB, SIEGETANK, ORBITALCOMMAND, COMMANDCENTER,
                                        STARPORT, ORBITALCOMMAND, FUSIONCORE, STARPORT, STARPORT,
                                       STARPORTTECHLAB, STARPORTTECHLAB, STARPORTTECHLAB,
                                       BATTLECRUISER, BATTLECRUISER, BATTLECRUISER]
            self.init_cocoon()
            self.production_pause_finish.add((REFINERY, 1, STARPORT, 1))
        elif self.game_choice[32]:
            self.opening_name = 'banshees'
            self.rush_opening = True
            self.buildseries_opening = banshee_series
            self.opening_create = {(BANSHEE,2)}
            self.init_banshee_spots()
        elif self.game_choice[33]:
            self.opening_name = 'workerrush-trans'
            self.rushopening = True
            self.startworkerrushers = 9 # 9
            self.buildseries_opening = [SUPPLYDEPOT, BARRACKS, MARINE, BUNKER, MARINE]
            if (self.enemy_species == 'zerg'):
                bunker_raw_pos = self.cheese3_cocoon_pos
            else:
                bunker_raw_pos = self.enemynatural_pos.towards(self.enemynaturalchoke_pos,3)
            bunker_pos = self.init_cheese_position(bunker_raw_pos, 0, 20, BUNKER)
            barracks_pos = self.init_cheese_position(self.enemythird_pos, 7, 17, BARRACKS)
            self.chosenplaces.insert(0, (BARRACKS, barracks_pos))
            self.chosenplaces.append((BUNKER, bunker_pos))
            self.wished_marines_per_bunker = 3
        elif self.game_choice[34]:
            self.opening_name = 'workerrush-banshees'
            self.rushopening = True
            self.startworkerrushers = 10 # 10
            self.buildseries_opening = banshee_series
            self.opening_create = {(BANSHEE,2)}
            self.init_banshee_spots()
        elif self.game_choice[35]:
            self.opening_name = 'workerrush-bc'
            self.rushopening = True
            self.startworkerrushers = 11 # 11
            # style twobase-bc
            self.buildseries_opening = [SUPPLYDEPOT, BARRACKS, REFINERY, SUPPLYDEPOT, MARINE, REFINERY, FACTORY, MARINE,
                                       STARPORT, COMMANDCENTER, FUSIONCORE, STARPORTTECHLAB, BATTLECRUISER]
        elif self.game_choice[36]:
            self.opening_name = 'workerrush-marine-1'
            self.rushopening = True
            self.startworkerrushers = 12 # 12
            self.workerrushstartframe = 300  # 300
            self.init_marine_opening(1)
        elif self.game_choice[37]:
            self.opening_name = 'workerrush-13-marine-2'
            self.rushopening = True
            self.startworkerrushers = 13 # 13
            self.workerrushstartframe = 390  # 390
            self.init_marine_opening(2)
        elif self.game_choice[38]:
            self.opening_name = 'workerrush-late'
            self.rushopening = True
            self.startworkerrushers = 11 # 11
            self.workerrushstartframe = 370  # 370
            self.buildseries_opening = [SUPPLYDEPOT, BARRACKS, REFINERY, MARINE, ORBITALCOMMAND]
        elif self.game_choice[39]:
            self.opening_name = 'cocoon-banshees'
            self.rushopening = True
            self.buildseries_opening = cocoon_series + [COMMANDCENTER] + banshee_series
            self.opening_create = {(BANSHEE,2)}
            self.init_banshee_spots()
            self.init_cocoon()
        elif self.game_choice[40]:
            self.opening_name = 'viking'
            self.rushopening = True
            self.buildseries_opening = [SUPPLYDEPOT, REFINERY, BARRACKS, SUPPLYDEPOT, REFINERY, FACTORY,
                                        STARPORT, FACTORYTECHLAB, VIKINGFIGHTER, SIEGETANK]
            self.place_proxy(STARPORT,45)
        elif self.game_choice[41]: # this was a test
            self.opening_name = 'immediate_fight'
            self.rushopening = True
            self.buildseries_opening = [SUPPLYDEPOT, BARRACKS, MARINE, BUNKER]
            if self.enemy_species == 'zerg':
                bunkerpos = self.init_cheese_position(self.enemyramp_pos, 7, 17, BUNKER)
            else:
                bunkerpos = self.init_cheese_position(self.enemy_pos, 79, 79, BUNKER)
            self.chosenplaces.append((BUNKER, bunkerpos))
        elif self.game_choice[42]:
            self.opening_name = 'banshee_flock'
            self.buildseries_opening = [SUPPLYDEPOT, COMMANDCENTER, BARRACKS, REFINERY, REFINERY, BUNKER,
                                        MARINE, FACTORY, SUPPLYDEPOT, ORBITALCOMMAND, MARINE, REFINERY,
                                        STARPORT, STARPORT, STARPORT, MARINE,
                                        STARPORTTECHLAB,STARPORTTECHLAB,STARPORTTECHLAB,BANSHEECLOAK]
            self.chosenplaces.append((COMMANDCENTER, self.homenatural_pos))
            self.natural_bunker()
            self.opening_create = {(BANSHEE,6)}
        elif self.game_choice[43]:
            self.opening_name = 'marauder-3'
            self.rushopening = True
            self.cc_destiny_rush = True
            self.buildseries_opening = [SUPPLYDEPOT, COMMANDCENTER, BARRACKS,COMMANDCENTER,REFINERY,
                                        BUNKER, ENGINEERINGBAY, REFINERY,
                                        BARRACKS,BARRACKS,BARRACKS,BARRACKS,BARRACKS,BARRACKS,BARRACKS,
                                        BARRACKS, REFINERY,
                                        BARRACKSTECHLAB,BARRACKSTECHLAB,BARRACKSTECHLAB,BARRACKSTECHLAB,
                                        BARRACKSTECHLAB,BARRACKSTECHLAB,BARRACKSTECHLAB,BARRACKSTECHLAB,
                                        GHOSTACADEMY,REFINERY]
            # marauder_restpoint, marauder_goal
            self.marauder_pf_spot = self.place_around(COMMANDCENTER, self.map_center)
            self.marauder_restpoint = self.marauder_pf_spot.towards(self.loved_pos,3)
            self.marauder_goal = self.marauder_restpoint
            self.natural_bunker()
            # barracks random placing
            bars = 1
            while bars < 8:
                barpos = self.choose_place_random()
                self.chosenplaces.append((BARRACKS, barpos))
                self.write_layout(BARRACKS, barpos)
                bars += 1
            self.production_pause_finish.add((SUPPLYDEPOT, 1, ORBITALCOMMAND, 1))
            self.production_pause_finish.add((REFINERY, 0, FACTORY, 1))
            self.opening_create = {(MARAUDER,48),(GHOST,5)}
            self.ghost_requests.append('army_ghost')
            self.ghost_requests.append('army_ghost')
            self.ghost_requests.append('army_ghost')
            self.ghost_requests.append('army_ghost')
            self.ghost_requests.append('army_ghost')
            self.supply_rate = 0.26
        elif self.game_choice[44]:
            self.opening_name = 'nukerush'
            self.rushopening = True
            self.buildseries_opening = [SUPPLYDEPOT, REFINERY, BARRACKS, ORBITALCOMMAND,
                                    MARINE, BUNKER, GHOSTACADEMY, REFINERY, FACTORY, BARRACKSTECHLAB,
                                    PERSONALCLOAKING, GHOST,
                                    STARPORT,GHOST, NUKESILONOVA,MEDIVAC]
            self.natural_bunker()
            self.ghost_requests.append('rush_ghost')
            self.ghost_requests.append('rush_ghost')
            for (lab,pos) in self.unthinkable:
                if lab == BARRACKSTECHLAB:
                    barpos = self.homenaturalchoke_pos
                    barpos = self.place_around(BARRACKS, barpos)
                    self.chosenplaces.insert(0,(BARRACKS, barpos))
                    self.write_layout(BARRACKS, barpos)
        elif self.game_choice[45]:
            self.opening_name = '2-1-1'
            self.rushopening = True
            self.buildseries_opening = [SUPPLYDEPOT,BARRACKS,REFINERY,REAPER,ORBITALCOMMAND,COMMANDCENTER,
                                        BARRACKS,SUPPLYDEPOT,BARRACKSREACTOR,REFINERY,FACTORY,BARRACKSTECHLAB,
                                        ORBITALCOMMAND,STIMPACK,STARPORT,FACTORYREACTOR]
            # no scout1
            self.scout1_tag = -2
            # full marines after barrackstechlab, 2 medivacs after starportreactor
            self.opening_create = {(MARINE,24),(MEDIVAC,2)}
            self.production_pause_finish.add((MARINE, 0, BARRACKSTECHLAB, 1))
            self.opening_create_slack = 2 # means not all opening_buildseries first
            self.production_pause_finish.add((MEDIVAC, 0, STARPORTREACTOR, 1))
            # swap starport to factoryreactor
            around = self.loved_pos.towards(self.map_center,7)
            facpos = self.place_around(FACTORY, around)
            self.chosenplaces.append((FACTORY, facpos))
            self.write_layout(FACTORY, facpos)
            self.notechlab.add((FACTORY,facpos))
            sppos = self.init_cheese_position(facpos, 3, 20, STARPORT) # does write layout
            self.chosenplaces.append((STARPORT, sppos))
            self.notechlab.add((STARPORT,sppos))
            self.swapplans.add((sppos,facpos))
            # placement for dumb walls
            for (lab,pos) in self.unthinkable:
                if lab == BARRACKSTECHLAB:
                    # find 2 barracks spots
                    barpos = self.homenaturalchoke_pos.towards(self.homenatural_pos,3)
                    barpos = self.place_around(BARRACKS, barpos)
                    self.chosenplaces.insert(0,(BARRACKS, barpos))
                    self.write_layout(BARRACKS, barpos)
                    barpos = self.homenaturalchoke_pos.towards(self.homenatural_pos, 3)
                    barpos = self.place_around(BARRACKS, barpos)
                    self.chosenplaces.insert(0, (BARRACKS, barpos))
                    self.write_layout(BARRACKS, barpos)
            self.do211_init()
        elif self.game_choice[46]:
            self.opening_name = 'reaper-rauder'
            self.rushopening = True
            self.buildseries_opening = [SUPPLYDEPOT,BARRACKS,REFINERY,REAPER,ORBITALCOMMAND,COMMANDCENTER,
                                        BARRACKS,SUPPLYDEPOT,BARRACKSREACTOR,BARRACKSTECHLAB,REFINERY,
                                        ORBITALCOMMAND,PUNISHERGRENADES, ENGINEERINGBAY, REFINERY, TERRANINFANTRYARMORSLEVEL1,
                                        FACTORY,COMMANDCENTER,STARPORT,FUSIONCORE,STARPORTTECHLAB,BATTLECRUISER]
            self.opening_create = {(REAPER,10),(MARAUDER,15)}
            #for agh in range(0,5):
            #    self.ghost_requests.append('army_ghost')
            self.opening_create_slack = 2 # means not all opening_buildseries first
            self.reaper_goal = self.enemy_pos.towards(self.map_center,-5)
            self.marauder_goal = self.reaper_goal
            self.production_pause_egg.add((MARINE, 0, BARRACKSTECHLAB, 1))
            # placement for dumb walls
            for (lab,pos) in self.unthinkable:
                if lab == BARRACKSTECHLAB:
                    # find 2 barracks spots
                    for times in [1,2]:
                        barpos = self.map_center
                        while not self.hoxy(barpos):
                            barpos = self.random_mappoint()
                        barpos = self.place_around(BARRACKS, barpos)
                        self.chosenplaces.insert(0,(BARRACKS, barpos))
                        self.write_layout(BARRACKS, barpos)
        # radio_choices = 47
        self.log_success('OPENING: '+self.opening_name)
        #
        for (kind,am) in self.opening_create:
            self.opening_create_units += am
            self.opening_create_hadmax[kind] = 0
        #
        self.init_cheese1()
        self.init_workerrush()
        #
        # init gather
        for (mimpos,mimt) in self.all_minerals:
            self.nminers_of_mimt[mimt] = 0
        for miner in self.units(SCV):
            minert = miner.tag
            if minert not in self.speciality_of_tag:
                self.job_of_scvt[minert] = 'mimminer'
                best_sd = 99999
                bestmim = (self.nowhere,self.notag)
                for (mimpos,mimt) in self.all_minerals:
                    if self.nminers_of_mimt[mimt] < 2:
                        sd = self.sdist(miner.position,mimpos) + 30 * self.nminers_of_mimt[mimt]
                        if sd < best_sd:
                            best_sd = sd
                            bestmim = (mimpos,mimt)
                (mimpos,mimt) = bestmim
                self.mim_of_minert[minert] = bestmim
                self.nminers_of_mimt[mimt] += 1
        # gather (unless second)
        for miner in self.units(SCV):
            minert = miner.tag
            if minert in self.mim_of_minert:
                gogather = True
                mim = self.mim_of_minert[minert]
                (mimpos,mimt) = mim
                if self.nminers_of_mimt[mimt] == 2:
                    # smallest tag will mine first
                    for otherminert in self.mim_of_minert:
                        if self.mim_of_minert[otherminert] == mim:
                            if otherminert < minert:
                                gogather = False
                if gogather:
                    self.go_gather_mim(miner,mim)
                    self.phase_of_minert[minert] = 'G'
                else: # needs move to prevent automatic mining
                    startpoint = self.loved_pos.towards(mimpos,3)
                    miner.move(startpoint)
                    self.phase_of_minert[minert] = 'W'
        self.fix_count_of_job()
        #
        #  preparing midgame
        self.midgame_things = []
        # The midgame really needs a battlecruiser, or the core is too late
        # This routine is called in the init phase, you cannot depend on e.g. amount of barracks
        self.midgame(BATTLECRUISER,1)
        if self.game_choice[50]:
            self.midgame(VIKINGFIGHTER,1)
        if self.game_choice[51]:
            self.midgame(SIEGETANK,1)
        if self.game_choice[52]:
            self.midgame(SIEGETANK,2)
        if self.game_choice[53]:
            self.midgame(MARINE, 2)
        else:
            self.midgame(MARINE, 5)
        if self.game_choice[54]:
            self.midgame(COMMANDCENTER,2)
            self.midgame(STARPORT,2)
            self.midgame(STARPORTTECHLAB,2)
        if self.game_choice[55]:
            self.midgame(ENGINEERINGBAY,1)
            self.midgame(MISSILETURRET,1)
            self.midgame(PLANETARYFORTRESS,1)
        if self.game_choice[56]:
            self.midgame(LIBERATOR,1)
        if self.game_choice[57]:
            self.midgame(CYCLONE,1)
        # made self.midgame_things
        # circle
        self.make_circle(10)
        self.flee_circle = self.circle.copy()
        # blocker
        self.init_blocker()
        # rally the first cc
        for cc in self.structures(COMMANDCENTER):
            cc(AbilityId.RALLY_BUILDING,self.loved_pos.towards(self.map_center,-3))
        # get hometop, enemytop
        self.get_hometop()
        self.get_enemytop()
        # name_of_scvt: fun translation of scvt to english boy name
        pl = open('data/names.txt','r')
        self.all_names = pl.read().splitlines()
        pl.close()
        # fleepolepos
        self.make_circle(16)
        self.fleepolepos = []
        for point in self.circle:
            # use 8.5 instead of 8, as the towards-points are outside of the walked circle.
            cpoint = Point2((self.followers.x + 8.5 * point.x, self.followers.y + 8.5 * point.y))
            self.fleepolepos.append(cpoint)
        #
        # from s2clientprotocol/error.proto:
        self.errortexts = ['0', # 0
        'Success', # 1
        'NotSupported', # 2;
        'Error', # 3;
        'CantQueueThatOrder', # 4;
        'Retry', # 5;
        'Cooldown', # 6;
        'QueueIsFull', # 7;
        'RallyQueueIsFull', # 8;
        'NotEnoughMinerals', # 9;
        'NotEnoughVespene', # 10;
        'NotEnoughTerrazine', # 11;
        'NotEnoughCustom', # 12;
        'NotEnoughFood', # 13;
        'FoodUsageImpossible', # 14;
        'NotEnoughLife', # 15;
        'NotEnoughShields', # 16;
        'NotEnoughEnergy', # 17;
        'LifeSuppressed', # 18;
        'ShieldsSuppressed', # 19;
        'EnergySuppressed', # 20;
        'NotEnoughCharges', # 21;
        'CantAddMoreCharges', # 22;
        'TooMuchMinerals', # 23;
        'TooMuchVespene', # 24;
        'TooMuchTerrazine', # 25;
        'TooMuchCustom', # 26;
        'TooMuchFood', # 27;
        'TooMuchLife', # 28;
        'TooMuchShields', # 29;
        'TooMuchEnergy', # 30;
        'MustTargetUnitWithLife', # 31;
        'MustTargetUnitWithShields', # 32;
        'MustTargetUnitWithEnergy', # 33;
        'CantTrade', # 34;
        'CantSpend', # 35;
        'CantTargetThatUnit', # 36;
        'CouldntAllocateUnit', # 37;
        'UnitCantMove', # 38;
        'TransportIsHoldingPosition', # 39;
        'BuildTechRequirementsNotMet', # 40;
        'CantFindPlacementLocation', # 41;
        'CantBuildOnThat', # 42;
        'CantBuildTooCloseToDropOff', # 43;
        'CantBuildLocationInvalid', # 44;
        'CantSeeBuildLocation', # 45;
        'CantBuildTooCloseToCreepSource', # 46;
        'CantBuildTooCloseToResources', # 47;
        'CantBuildTooFarFromWater', # 48;
        'CantBuildTooFarFromCreepSource', # 49;
        'CantBuildTooFarFromBuildPowerSource', # 50;
        'CantBuildOnDenseTerrain', # 51;
        'CantTrainTooFarFromTrainPowerSource', # 52;
        'CantLandLocationInvalid', # 53;
        'CantSeeLandLocation', # 54;
        'CantLandTooCloseToCreepSource', # 55;
        'CantLandTooCloseToResources', # 56;
        'CantLandTooFarFromWater', # 57;
        'CantLandTooFarFromCreepSource', # 58;
        'CantLandTooFarFromBuildPowerSource', # 59;
        'CantLandTooFarFromTrainPowerSource', # 60;
        'CantLandOnDenseTerrain', # 61;
        'AddOnTooFarFromBuilding', # 62;
        'MustBuildRefineryFirst', # 63;
        'BuildingIsUnderConstruction', # 64;
        'CantFindDropOff', # 65;
        'CantLoadOtherPlayersUnits', # 66;
        'NotEnoughRoomToLoadUnit', # 67;
        'CantUnloadUnitsThere', # 68;
        'CantWarpInUnitsThere', # 69;
        'CantLoadImmobileUnits', # 70;
        'CantRechargeImmobileUnits', # 71;
        'CantRechargeUnderConstructionUnits', # 72;
        'CantLoadThatUnit', # 73;
        'NoCargoToUnload', # 74;
        'LoadAllNoTargetsFound', # 75;
        'NotWhileOccupied', # 76;
        'CantAttackWithoutAmmo', # 77;
        'CantHoldAnyMoreAmmo', # 78;
        'TechRequirementsNotMet', # 79;
        'MustLockdownUnitFirst', # 80;
        'MustTargetUnit', # 81;
        'MustTargetInventory', # 82;
        'MustTargetVisibleUnit', # 83;
        'MustTargetVisibleLocation', # 84;
        'MustTargetWalkableLocation', # 85;
        'MustTargetPawnableUnit', # 86;
        'YouCantControlThatUnit', # 87;
        'YouCantIssueCommandsToThatUnit', # 88;
        'MustTargetResources', # 89;
        'RequiresHealTarget', # 90;
        'RequiresRepairTarget', # 91;
        'NoItemsToDrop', # 92;
        'CantHoldAnyMoreItems', # 93;
        'CantHoldThat', # 94;
        'TargetHasNoInventory', # 95;
        'CantDropThisItem', # 96;
        'CantMoveThisItem', # 97;
        'CantPawnThisUnit', # 98;
        'MustTargetCaster', # 99;
        'CantTargetCaster', # 100;
        'MustTargetOuter', # 101;
        'CantTargetOuter', # 102;
        'MustTargetYourOwnUnits', # 103;
        'CantTargetYourOwnUnits', # 104;
        'MustTargetFriendlyUnits', # 105;
        'CantTargetFriendlyUnits', # 106;
        'MustTargetNeutralUnits', # 107;
        'CantTargetNeutralUnits', # 108;
        'MustTargetEnemyUnits', # 109;
        'CantTargetEnemyUnits', # 110;
        'MustTargetAirUnits', # 111;
        'CantTargetAirUnits', # 112;
        'MustTargetGroundUnits', # 113;
        'CantTargetGroundUnits', # 114;
        'MustTargetStructures', # 115;
        'CantTargetStructures', # 116;
        'MustTargetLightUnits', # 117;
        'CantTargetLightUnits', # 118;
        'MustTargetArmoredUnits', # 119;
        'CantTargetArmoredUnits', # 120;
        'MustTargetBiologicalUnits', # 121;
        'CantTargetBiologicalUnits', # 122;
        'MustTargetHeroicUnits', # 123;
        'CantTargetHeroicUnits', # 124;
        'MustTargetRoboticUnits', # 125;
        'CantTargetRoboticUnits', # 126;
        'MustTargetMechanicalUnits', # 127;
        'CantTargetMechanicalUnits', # 128;
        'MustTargetPsionicUnits', # 129;
        'CantTargetPsionicUnits', # 130;
        'MustTargetMassiveUnits', # 131;
        'CantTargetMassiveUnits', # 132;
        'MustTargetMissile', # 133;
        'CantTargetMissile', # 134;
        'MustTargetWorkerUnits', # 135;
        'CantTargetWorkerUnits', # 136;
        'MustTargetEnergyCapableUnits', # 137;
        'CantTargetEnergyCapableUnits', # 138;
        'MustTargetShieldCapableUnits', # 139;
        'CantTargetShieldCapableUnits', # 140;
        'MustTargetFlyers', # 141;
        'CantTargetFlyers', # 142;
        'MustTargetBuriedUnits', # 143;
        'CantTargetBuriedUnits', # 144;
        'MustTargetCloakedUnits', # 145;
        'CantTargetCloakedUnits', # 146;
        'MustTargetUnitsInAStasisField', # 147;
        'CantTargetUnitsInAStasisField', # 148;
        'MustTargetUnderConstructionUnits', # 149;
        'CantTargetUnderConstructionUnits', # 150;
        'MustTargetDeadUnits', # 151;
        'CantTargetDeadUnits', # 152;
        'MustTargetRevivableUnits', # 153;
        'CantTargetRevivableUnits', # 154;
        'MustTargetHiddenUnits', # 155;
        'CantTargetHiddenUnits', # 156;
        'CantRechargeOtherPlayersUnits', # 157;
        'MustTargetHallucinations', # 158;
        'CantTargetHallucinations', # 159;
        'MustTargetInvulnerableUnits', # 160;
        'CantTargetInvulnerableUnits', # 161;
        'MustTargetDetectedUnits', # 162;
        'CantTargetDetectedUnits', # 163;
        'CantTargetUnitWithEnergy', # 164;
        'CantTargetUnitWithShields', # 165;
        'MustTargetUncommandableUnits', # 166;
        'CantTargetUncommandableUnits', # 167;
        'MustTargetPreventDefeatUnits', # 168;
        'CantTargetPreventDefeatUnits', # 169;
        'MustTargetPreventRevealUnits', # 170;
        'CantTargetPreventRevealUnits', # 171;
        'MustTargetPassiveUnits', # 172;
        'CantTargetPassiveUnits', # 173;
        'MustTargetStunnedUnits', # 174;
        'CantTargetStunnedUnits', # 175;
        'MustTargetSummonedUnits', # 176;
        'CantTargetSummonedUnits', # 177;
        'MustTargetUser1', # 178;
        'CantTargetUser1', # 179;
        'MustTargetUnstoppableUnits', # 180;
        'CantTargetUnstoppableUnits', # 181;
        'MustTargetResistantUnits', # 182;
        'CantTargetResistantUnits', # 183;
        'MustTargetDazedUnits', # 184;
        'CantTargetDazedUnits', # 185;
        'CantLockdown', # 186;
        'CantMindControl', # 187;
        'MustTargetDestructibles', # 188;
        'CantTargetDestructibles', # 189;
        'MustTargetItems', # 190;
        'CantTargetItems', # 191;
        'NoCalldownAvailable', # 192;
        'WaypointListFull', # 193;
        'MustTargetRace', # 194;
        'CantTargetRace', # 195;
        'MustTargetSimilarUnits', # 196;
        'CantTargetSimilarUnits', # 197;
        'CantFindEnoughTargets', # 198;
        'AlreadySpawningLarva', # 199;
        'CantTargetExhaustedResources', # 200;
        'CantUseMinimap', # 201;
        'CantUseInfoPanel', # 202;
        'OrderQueueIsFull', # 203;
        'CantHarvestThatResource', # 204;
        'HarvestersNotRequired', # 205;
        'AlreadyTargeted', # 206;
        'CantAttackWeaponsDisabled', # 207;
        'CouldntReachTarget', # 208;
        'TargetIsOutOfRange', # 209;
        'TargetIsTooClose', # 210;
        'TargetIsOutOfArc', # 211;
        'CantFindTeleportLocation', # 212;
        'InvalidItemClass', # 213;
        'CantFindCancelOrder', # 214;
        ]
        # chat
        await self._client.chat_send('Chaosbot version 6 dec 2021, made by MerkMore', team_only=False)
        code = self.opponent[0:8]
        if code in self.botnames:
            human = self.botnames[code]
        else:
            human = code
        await self._client.chat_send('Good luck and have fun, '+human, team_only=False)
        await self._client.chat_send('Tag:'+code, team_only=False)
        #
        #layout_if.photo_layout()

    async def send_tag(self):
        if self.frame > 1000:
            if not self.tag_sent:
                await self._client.chat_send('Tag:'+self.opening_name, team_only=True)
                self.tag_sent = True

    def postag(self,pos) -> int:    
        return round(400*pos.x+2*pos.y)

    def postag_of_patch(self, patch) -> int:
        return self.postag(patch.position)
        
    def init_all_minerals(self):
        if len(self.mineral_field) != self.mineral_field_hash:
            self.mineral_field_hash = len(self.mineral_field)
            self.all_minerals = {(patch.position,self.postag_of_patch(patch)) for patch in self.mineral_field}

    def init_all_vespene(self):
        self.all_vespene = {(gey.position,self.postag(gey.position)) for gey in self.vespene_geyser}
        # i hope this means not empty

    def go_gather_gas(self, scv, gas):
        (gaspos,gast) = gas
        for ref in self.structures(REFINERY)+self.structures(REFINERYRICH):
            if ref.position == gaspos:
                self.log_command('scv.gather(ref)')
                scv.gather(ref)

    def go_gather_mim(self, scv, mim):
        (mimpos,mimt) = mim
        # about 4/sec
        scvt = scv.tag
        done = False
        if scvt in self.hint_patch_of_scvt:
            patch = self.hint_patch_of_scvt[scvt]
            if patch in self.mineral_field:
                if self.postag_of_patch(patch) == mimt:
                    self.log_command('scv.gather(patch)')
                    scv.gather(patch)
                    done = True
        if not done:
            #print('* ',str(self.frame))    about 1/second
            for patch in self.mineral_field:
                if self.postag_of_patch(patch) == mimt:
                    self.log_command('scv.gather(patch)')
                    scv.gather(patch)
                    self.hint_patch_of_scvt[scvt] = patch

    def loadcc(self):
        # flee when unhealthy
        for cc in self.structures(COMMANDCENTER):
            if cc.tag in self.readies:
                if cc.health < 800: # or other reasons
                    if self.purpose[cc.tag] == 'scv':
                        self.purpose[cc.tag] = 'wishtofly'
                        self.log_cc('Commandcenter '+str(cc.tag)+' '+self.txt(cc.position)+' wishes to fly because of low health.')
                        if len(self.all_bases) < 2:
                            place = random.choice(self.expansion_locations)
                            self.goal_of_flying_struct[cc.tag] = place
                            self.landings_of_flying_struct[cc.tag] = 0
        for cc in self.structures(ORBITALCOMMAND):
            if cc.health < 800: # or other reasons
                if self.purpose[cc.tag] == 'scv':
                    self.purpose[cc.tag] = 'fly'
                    self.log_cc('Orbitalcommand '+str(cc.tag)+' '+self.txt(cc.position)+' wishes to fly because of low health.')
                    if len(self.all_bases) < 2:
                        place = random.choice(self.expansion_locations)
                        self.goal_of_flying_struct[cc.tag] = place
                        self.landings_of_flying_struct[cc.tag] = 0
        #
        for cc in self.structures(COMMANDCENTER):
            if cc.tag in self.readies:
                if self.purpose[cc.tag] == 'wishtofly':
                    self.log_cc('Commandcenter '+str(cc.tag)+' '+self.txt(cc.position)+' will cancel and load.')
                    self.purpose[cc.tag] = 'load'
                    if cc.tag not in self.idles:
                        self.log_command('cc(AbilityId.CANCEL_QUEUECANCELTOSELECTION)')  # build worker
                        cc(AbilityId.CANCEL_QUEUECANCELTOSELECTION)
                elif self.purpose[cc.tag] == 'load':
                    somerun = False
                    seats = 5 - len(cc.passengers)
                    for scv in self.units(SCV):
                        if self.near(scv.position, cc.position, 8):
                            if self.job_of_scvt[scv.tag] in {'escorter','pilot'}:
                                seats -= 1
                    for scv in self.units(SCV):
                        if self.near(scv.position, cc.position, 8):
                            if self.job_of_scvt[scv.tag] not in {'repairer', 'escorter', 'pilot'}:
                                if seats > 0:
                                    seats -= 1
                                    self.promote(scv, 'escorter')
                                    scv.move(cc.position)
                                    somerun = True
                            if self.job_of_scvt[scv.tag] == 'escorter':
                                somerun = True
                                if len(scv.orders) == 0:
                                    self.promote(scv, 'pilot')
                    if not somerun:
                        cc(AbilityId.LOADALL_COMMANDCENTER)
                        self.purpose[cc.tag] = 'closethedoors'
                elif self.purpose[cc.tag] == 'closethedoors':
                    passe = len(cc.passengers)
                    self.log_cc('Commandcenter '+str(cc.tag)+' '+self.txt(cc.position)+' closes its doors with '+str(passe)+' passengers.')
                    self.purpose[cc.tag] = 'fly'
                    for scv in self.units(SCV):
                        if self.near(scv.position, cc.position, 9):
                            if self.job_of_scvt[scv.tag] == 'pilot':
                                self.promote(scv,'idler')


    def max25_around(self, around) -> Point2:
        ok = False
        while not ok:
            ok = True
            place = self.random_mappoint()
            if (not self.near(around, place, 25)):
                ok = False
            place = self.place_around(BARRACKS, place)
            for (mimpos,mimt) in self.all_minerals:
                if self.near(place, mimpos, 4):
                    ok = False
        return place

    def choose_place_random(self) -> Point2:
        ok = False
        while not ok:
            ok = True
            around = self.random_mappoint()
            if self.proxy(around):
                ok = False
            #if (not self.near(around, self.map_center, 60)):
            if not self.near(around,self.hisright,35):
                ok = False
            place = self.place_around(BARRACKS, around)
            for (mimpos,mimt) in self.all_minerals:
                if self.near(place, mimpos, 4):
                    ok = False
        return place

    def natural_bunker(self):
        bunkerplace = self.homenaturalchoke_pos.towards(self.homenatural_pos, 2)
        bunkerplace = self.place_around(BUNKER, bunkerplace)
        bunker_if.hiding_spot = bunkerplace.towards(self.homenatural_pos, 3)
        self.chosenplaces.append((BUNKER, bunkerplace))
        self.write_layout(BUNKER, bunkerplace)


    def init_marine_opening(self, nbases):
        # 1 <= nbases <= 6
        # can also be the second part of an opening
        self.marine_opening_bases = nbases
        self.rushopening = True
        self.cc_destiny_rush = True
        ccs = 1
        if len(self.buildseries_opening) > 0:
            # suppose barracks included
            for thing in self.buildseries_opening:
                if thing == COMMANDCENTER:
                    ccs += 1
        elif nbases == 1:
            self.buildseries_opening = [SUPPLYDEPOT, BARRACKS]
        else:    
            self.buildseries_opening = [SUPPLYDEPOT, COMMANDCENTER, BARRACKS]
            ccs = 2
        while (ccs < nbases):
            self.buildseries_opening.append(COMMANDCENTER)
            ccs += 1
        # start gas
        if nbases >= 2: # first gas
            self.buildseries_opening.append(REFINERY)
        if nbases >= 3: # second gas
            self.buildseries_opening.append(REFINERY)
        # barracks (in the opening, so scvs can travel in advance)
        bars = 1
        while bars < 4 * nbases:
            self.buildseries_opening.append(BARRACKS)
            bars += 1
        # barracks random placing
        bars = 1
        while bars < 4 * nbases:
            barpos = self.choose_place_random()
            self.chosenplaces.append((BARRACKS, barpos))
            self.write_layout(BARRACKS, barpos)
            bars += 1
        # bunker code deleted because of interaction with cocoon
        self.production_pause_finish.add((SUPPLYDEPOT, 1, ORBITALCOMMAND, 1))
        self.production_pause_finish.add((SCV, 16 + nbases, ORBITALCOMMAND, 1))
        self.production_pause_finish.add((REFINERY, 0, FACTORY, 1))
        self.opening_create = {(MARINE,nbases * 28)} # 4 barracks * 7 marines/barracks
        self.marine_gather_time = nbases * 4 # 4 barracks * 1 marines/barracks
        self.supply_rate = 0.12 + 0.04 * nbases

    #*********************************************************************************************************************
    #   logging

    async def catch_a_bug(self):
        abug = False
        # put detectioncondition under here
        # put detectioncondition above here
        if abug:
            await self._client.chat_send('catch a bug ', team_only=False)
            self.slowdown_frames = 30
            please_breakpoint_this_line = True

    def log_buildsource(self):
        if self.do_log_buildsource:
            stri = 'buildorder:'
            for (th, po, status) in self.buildorder_exe:
                stri = stri + '   ' + th.name + ' ' + status[0]
            print(stri)
            stri = 'throwspots:'
            for (thing, pos, status, owner) in self.throwspots:
                stri = stri + '   ' + thing.name + ' ' + status[0]
            print(stri)

    def log_speedmining(self, stri):
        if self.do_log_speedmining:
            print(' On '+str(self.frame)+' speedmining '+stri)

    def log_fail(self,bol,stri):
        if self.do_log_fail:
            if not bol:
                print(' On '+str(self.frame)+' fail '+stri)

    def log_success(self,stri):
        if self.do_log_success:
            print(' On '+str(self.frame)+' success '+stri)

    def log_bunker(self,stri):
        if self.do_log_bunker:
            print(' On '+str(self.frame)+' bunker '+stri)

    def log_swaps(self):
        if self.do_log_swaps:
            for (thing, pos) in self.couldswap:
                print('could swap ' + thing.name + ' ' + self.txt(pos))
            for (frompos, topos) in self.swapplans:
                print('plan ' + self.txt(frompos) + ' ' + self.txt(topos))
            for (thing, pos) in self.willswap:
                print('will swap ' + thing.name + ' ' + self.txt(pos))
            for (thing, pos) in self.didswap:
                print('did swap ' + thing.name + ' ' + self.txt(pos))

    def log_army(self,stri):
        if self.do_log_army:
            print(' On '+str(self.frame)+' army '+stri)

    def log_cc(self,stri):
        if self.do_log_cc:
            print(' On '+str(self.frame)+' cc '+stri)

    def log_purpose(self):
        if self.do_log_purpose:
            print(' ')
            for cctag in self.purpose:
                for stru in self.structures:
                    if stru.tag == cctag:
                        print(stru.type_id.name + ' ' + str(cctag) + ' ' + self.purpose[cctag])

    def log_fighters(self):
        if self.do_log_fighters:
            print('----------')
            for scv in self.units(SCV):
                scvt = scv.tag
                if self.job_of_scvt[scvt] == 'fighter':
                    mypos = scv.position
                    nearenemydist = 99999
                    if scvt in self.victimtag_of_unittag:
                        victimtag = self.victimtag_of_unittag[scvt]
                        for ene in self.enemy_units:
                            if ene.tag == victimtag:
                                nearenemydist = self.circledist(mypos,ene.position) - ene.radius
                    if scvt in self.fighter_phase:
                        phase = self.fighter_phase[scvt]
                    else:
                        phase = 'free'
                    print('fighter ' + self.name(scvt) + ' '+ phase + ' ' + str(nearenemydist))
                    if scvt in self.fighternurse:
                        otherscvt = self.fighternurse[scvt]
                        print('fighter ' + self.name(scvt) + ' repairs ' + self.name(otherscvt))
                    orders = ""
                    for order in scv.orders:
                        if type(order.target) == int:
                            orders = orders + '    ' + str(order.ability.id) + ', ' + str(order.target) + ', ' + str(
                                order.progress)
                        else:
                            orders = orders + '   ' + str(order.ability.id) + ', ' + self.txt(order.target) + ', ' + str(
                                order.progress)
                    print('fighter orders ' + orders)

    def log_bcs(self):
        if self.do_log_bcs:
            atty = self.attack_type
            inrep = 0
            for bc in self.units(BATTLECRUISER):
                if self.emotion_of_unittag[bc.tag] == 'bcrecovering':
                    inrep +=1
            print(' On '+str(self.frame)+' attacktype '+atty+', in rep '+str(inrep))
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
            print(' On '+str(self.frame)+' attacktype '+stri)

    def log_workers(self,stri):
        if self.do_log_workers:
            print(' On '+str(self.frame)+' workers '+stri)

    def log_layout(self,stri):
        if self.do_log_layout:
            print(' On '+str(self.frame)+' layout '+stri)

    def log_placing(self,stri):
        if self.do_log_placing:
            print(' On '+str(self.frame)+' placing '+stri)

    def log_command(self,stri):
        if self.do_log_command:
            print(' On '+str(self.frame)+' commands '+stri)

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
            stro = ''
            for (thing, pos, status, owner) in self.throwspots:
                stro = stro + thing.name + ' ' + self.txt(pos) + ' ' + owner + '   '
            print(' On '+str(self.frame)+' throw '+stro+stri)

    def txt(self, point) -> str:
        return str(point.x)+','+str(point.y)

    def log_boss(self,stri):
        if self.do_log_boss:
            print(' On '+str(self.frame)+' boss '+stri)

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
            for gas in self.all_gas_to_mine:
                (gaspos,gast) = gas
                print('gas '+str(gast)+': ')
                for scvt in self.gas_of_minert: 
                    if self.gas_of_minert[scvt] == gas:
                        print(str(scvt))
            for scvt in self.all_scvt:
                if self.job_of_scvt[scvt] == 'gasminer':
                    if scvt not in self.gas_of_minert:
                        print('gasminer without assignment '+self.name(scvt)) 
            for scvt in self.gas_of_minert:
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
            if self.cheese1_phase != 'Z':
                print(' On '+str(self.frame)+' cheese1_phase '+self.cheese1_phase
                      +'   cheese3_phase '+self.cheese3_phase)

    def family(self, mapname):
        mapfamily = ''
        for ch in mapname.replace('LE', '').replace('AIE', ''):
            if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
                mapfamily += ch.lower()
        return mapfamily


    def slowed_down(self):
        if self.do_slowdown:
            if self.slowdown_frames > 0:
                self.slowdown_frames -= self.chosen_game_step
                time.sleep(self.slowness)

    async def funchat(self):
        if self.do_funchat:
            if len(self.funchat_lines) == 0:
                pl = open('data/funchat.txt', 'r')
                self.funchat_lines = pl.read().splitlines()
                pl.close()
                self.funchat_linenr = random.randrange(0, len(self.funchat_lines))
            if self.funchat_linenr < len(self.funchat_lines):
                line = self.funchat_lines[self.funchat_linenr]
                await self._client.chat_send(line, team_only=False)
                self.funchat_linenr = (self.funchat_linenr + 1) % len(self.funchat_lines)

    async def act_on_errors(self):
        for err in self.state.action_errors:
            abiid = err.ability_id
            unittag = err.unit_tag
            res = err.result
            abiname = sc2.AbilityId(abiid).name
            self.log_fail(False,'Error trying '+abiname+' '+self.errortexts[res])
            # anti burrowed ling code
            if res == 44: # 'CantBuildLocationInvalid'
                for items in self.buildandretry:
                    (scvt, building, goal, startframe) = items
                    if (building == COMMANDCENTER) and (scvt == unittag):
                        # trow turret
                        turpos = goal.towards(self.map_center,-3)
                        turpos = self.place_around(MISSILETURRET,turpos)
                        self.throw_at_spot(MISSILETURRET,turpos,'act_on_errors')
            #await self._client.chat_send('on_error '+abiname+' '+self.errortexts[res], team_only=False)


    def position_of_building(self, bui) -> Point2:
        if bui.type_id in self.all_labs:
            pos = Point2((bui.position.x - 2.5, bui.position.y + 0.5))
        else:
            pos = bui.position
        return pos


    def init_expected_order(self, job, abil):
        self.expected_orders.add((job,abil))

    def init_cheese_position(self, anchor,good_sdist,max_sdist,building) -> Point2:
        # to prevent some bugged placement: do not place higher than anchor.
        maxheight = self.get_height(anchor)
        besttry = 99999
        found_spot = self.nowhere
        estimate = anchor.towards(self.map_center,sqrt(good_sdist))
        estimate = self.put_on_the_grid(building, estimate)
        for dx in range(-20, 20):
            for dy in range(-20, 20):
                maypos = Point2((estimate.x + dx, estimate.y + dy))
                if self.check_layout(building, maypos):
                    mayheight = self.get_height(maypos)
                    if mayheight <= maxheight:
                        sd = self.sdist(anchor, maypos)
                        if sd < max_sdist:
                            try0 = (sd - good_sdist)*(sd-good_sdist) + self.circledist(maypos,self.map_center)
                            if try0 < besttry:
                                found_spot = maypos
                                besttry = try0
        if found_spot != self.nowhere:
            self.write_layout(building,found_spot)
        return found_spot

    def init_cheese1(self):
        if self.opening_name.find('cheese') >= 0:
            self.set_rally.add((self.cheese1_landing_pos, self.cheese1_prison_pos))
            self.set_rally.add((self.cheese1_bunker_pos, self.cheese1_prison_pos))
            self.set_rally.add((self.cheese1_factory_pos, self.cheese1_tank_pos))
            self.rushopening = True
            self.production_pause_finish.add((SCV, 12, SUPPLYDEPOT, 1))

    def init_pf_rush(self):
        # fun placement of barracks, bunker, commandcenter, planetaryfortress
        self.write_layout(COMMANDCENTER,self.enemynatural_pos)
        planpos = self.enemynatural_pos.towards(self.enemynaturalchoke_pos,10)
        self.cheese3_landing_pos = self.init_cheese_position(planpos,1,20,COMMANDCENTER)
        self.cheese3_bunker_pos = self.init_cheese_position(self.cheese3_landing_pos,66,66,BUNKER)
        self.cheese3_barracks_pos = self.init_cheese_position(self.enemynaturalchoke_pos,21,41,ARMORY) # BARRACKS nolab
        self.cheese3_cc_pos = self.init_cheese_position(self.cheese3_barracks_pos,28,28,COMMANDCENTER)
        self.cheese3_prison_pos = self.init_cheese_position(self.cheese3_bunker_pos,12,22,MISSILETURRET)
        bunker_if.hiding_spot = self.init_cheese_position(self.cheese3_bunker_pos,50,50,MISSILETURRET)
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
        self.production_pause_finish.add((SCV,20,ENGINEERINGBAY,1))
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
        for (mimpos,mimt) in self.all_minerals:
            if self.near(mimpos,base,self.miner_bound):
                sumx += mimpos.x
                sumy += mimpos.y
                n += 1
        if n > 0:
            mimcenter = Point2((sumx/n,sumy/n))
            where = Point2((1.3*mimcenter.x-0.3*base.x, 1.3*mimcenter.y-0.3*base.y))
            self.add_spot(name,where,base)

    def init_banshee_spots(self):
        x = (2 * self.hisright.x + self.enemy_pos.x + self.loved_pos.x) / 4
        y = (2 * self.hisright.y + self.enemy_pos.y + self.loved_pos.y) / 4
        around = Point2((x, y))
        barpos = self.max25_around(around)
        self.chosenplaces.insert(0, (BARRACKS, barpos))
        self.write_layout(BARRACKS, barpos)
        self.barracks_techlab_advice = barpos
        x = (3 * self.hisleft.x + 2 * self.enemy_pos.x + self.loved_pos.x) / 6
        y = (3 * self.hisleft.y + 2 * self.enemy_pos.y + self.loved_pos.y) / 6
        around = Point2((x, y))
        facpos = self.max25_around(around)
        self.chosenplaces.append((FACTORY, facpos))
        self.write_layout(FACTORY, facpos)
        pos = self.init_cheese_position(barpos, 3, 20, STARPORT)
        self.chosenplaces.append((STARPORT, pos))
        self.notechlab.add((STARPORT, pos))
        pos = self.init_cheese_position(facpos, 3, 20, STARPORT)
        self.chosenplaces.append((STARPORT, pos))
        self.notechlab.add((STARPORT, pos))

    def init_liberator_spots(self):
        self.add_spot('contain1',self.enemyramp_pos,self.enemy_pos)
        self.add_spot('contain2',self.enemynaturalchoke_pos,self.enemynatural_pos)
        self.add_spot('base1',self.enemy_pos,self.enemyramp_pos)
        self.add_spot('base2',self.enemynatural_pos,self.enemyramp_pos)
        self.add_mineral_spot('mim1',self.enemy_pos)
        self.add_mineral_spot('mim2',self.enemynatural_pos)

    def init_reapers(self):
        if self.reaper_bunker1_pos == self.nowhere:
            self.reaper_bunker1_pos = self.init_cheese_position(self.enemynatural_pos, 79, 99, BUNKER)
        if self.reaper_bunker2_pos == self.nowhere:
            self.reaper_bunker2_pos = self.init_cheese_position(self.enemynatural_pos, 200, 300, BUNKER)
        self.chosenplaces.append((BUNKER,self.reaper_bunker1_pos))
        self.chosenplaces.append((BUNKER,self.reaper_bunker2_pos))
        self.chosenplaces.insert(0,(BARRACKS,self.reaper_barracks_pos))
        self.init_reaper_attack(self.enemy_pos)

    def init_cocoon(self):
        # funny placement of barracks, bunker, barracks,bunker
        self.cheese3_bunker_pos = Point2((self.cheese3_cocoon_pos.x+2.5,self.cheese3_cocoon_pos.y-0.5))
        self.cheese3_bunker2_pos = Point2((self.cheese3_cocoon_pos.x+0.5,self.cheese3_cocoon_pos.y+2.5))
        self.cheese3_barracks_pos = Point2((self.cheese3_cocoon_pos.x-2.5,self.cheese3_cocoon_pos.y+0.5))
        self.cheese3_barracks2_pos = Point2((self.cheese3_cocoon_pos.x-0.5,self.cheese3_cocoon_pos.y-2.5))
        self.cheese3_prison_pos = self.cheese3_cocoon_pos
        # use all
        self.chosenplaces.insert(0,(BARRACKS,self.cheese3_barracks_pos))
        self.chosenplaces.append((BUNKER,self.cheese3_bunker_pos))
        self.chosenplaces.insert(0,(BARRACKS,self.cheese3_barracks2_pos))
        self.chosenplaces.append((BUNKER,self.cheese3_bunker2_pos))
        #
        self.set_rally.add((self.cheese3_barracks_pos, self.cheese3_prison_pos))
        self.set_rally.add((self.cheese3_barracks2_pos, self.cheese3_prison_pos))
        self.wished_marines_per_bunker = 4
        self.production_pause_egg.add((SCV, 16, BUNKER, 1))


    def init_marauders(self):
        bar1_pos = self.init_cheese_position(self.enemythird_pos,200,300,BARRACKS)
        bar2_pos = self.init_cheese_position(bar1_pos,1,30,BARRACKS)
        bun_pos = self.init_cheese_position(bar1_pos,1,30,BUNKER)
        self.chosenplaces.append((INFESTEDBARRACKS,bar1_pos))
        self.chosenplaces.append((INFESTEDBARRACKS,bar2_pos))
        self.chosenplaces.append((INFESTEDBUNKER,bun_pos))
        self.marauder_goal = bun_pos
        self.production_pause_finish.add((SCV,23,FACTORY,1))
        self.production_pause_finish.add((REFINERY,1,FACTORY,1))
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

    def log_bird_history(self):
        if self.do_log_bird_history:
            # count the birds
            new_bird_am = {}
            am = 0
            for reftype in {REFINERY,REFINERYRICH}:
                for ref in self.structures(reftype):
                    am += len(ref.passengers)
            new_bird_am[SCV] = am
            for (thing,pos) in self.birds:
                if thing in new_bird_am:
                    new_bird_am[thing] += 1
                else:
                    new_bird_am[thing] = 1
            # compare to self.bird_am_history
            for thing in new_bird_am:
                am = new_bird_am[thing]
                if thing in self.bird_am_history:
                    am -= self.bird_am_history[thing]
                if am == 1:
                    print('created a '+thing.name)
                elif am > 0:
                    print('created '+str(am)+' '+thing.name)
            for thing in self.bird_am_history:
                am = self.bird_am_history[thing]
                if thing in new_bird_am:
                    am -= new_bird_am[thing]
                if am == 1:
                    print('lost a ' + thing.name)
                elif am > 0:
                    print('lost ' + str(am) + ' ' + thing.name)
            # set bird_am_history
            self.bird_am_history = new_bird_am


    def log_thoughts(self):
        if self.do_log_thoughts:
            for (thingtype,pos,owner) in self.thoughts:
                print(' On '+str(self.frame)+' ' + owner + ' is thinking of ' + thingtype.name + ' at ' + self.txt(pos))
            for (thingtype,pos) in self.unthinkable:
                print('Unthinkable is a ' + thingtype.name + ' at ' + self.txt(pos))

    def log_dreams(self):
        if self.do_log_dreams:
            for (thingtype,pos,owner) in self.dreams:
                print(' On '+str(self.frame)+' ' + owner + ' is dreaming of ' + thingtype.name + ' at ' + self.txt(pos))

    def log_buildorder(self, stri):
        if self.do_log_buildorder:
            print(' On ' + str(self.frame) + ' buildorder ' + stri)

    def log_unitorder(self, unt, instri):
        if self.do_log_unitorder:
            mytile = self.maptile_of_pos(unt.position)
            stri = unt.type_id.name + ' ' + instri
            for order in unt.orders:
                stri = stri + ' ' +str(unt.tag) + ' ' + str(order.ability.id)
                if order.ability.id == AbilityId.ATTACK:
                    if type(order.target) == int:
                        text = ' thing'
                        for tile in self.nine[mytile]:
                            for ene in self.enemies_of_tile[tile]:
                                if ene.tag == order.target:
                                    text = ' ' + ene.name
                        if text == ' thing':
                            for ene in self.enemy_units | self.enemy_real_structures:
                                if ene.tag == order.target:
                                    text = ' ' + ene.name
                        stri = stri + text
                    else:
                        stri = stri + ' place'
            print(' On '+str(self.frame)+' unitorder                        ' + stri)

    def log_orders(self):
        # order 0 will be executed first
        # a bump can insert a move
        # attack point but see enemy can insert attack enemy
        if self.do_log_orders:
            for scv in self.units(SCV):
                normal = False
                job = self.job_of_scvt[scv.tag]
                if len(scv.orders) == 2:
                    if job == 'fighter':
                        if scv.orders[0].ability.id == AbilityId.ATTACK:
                            if scv.orders[1].ability.id == AbilityId.ATTACK:
                                normal = True
                    if job == 'mimminer':
                        if scv.orders[0].ability.id == AbilityId.MOVE:
                            if scv.orders[1].ability.id == AbilityId.HARVEST_GATHER:
                                normal = True
                if (len(scv.orders) == 1):
                    if (job,scv.orders[0].ability.id) in self.expected_orders:
                        normal = True
                    if job in ('fencer','builder'):
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


    async def debug(self, unt):
        stri = 'debug ' + str(unt.tag) + ' ' + str(unt.weapon_cooldown) + ' '
        if unt.tag in self.emotion_of_unittag:
            stri += self.emotion_of_unittag[unt.tag]
        if unt in self.units(SCV):
            stri += self.job_of_scvt[unt.tag] + ' ' + self.name(unt.tag)
        for order in unt.orders:
            if type(order.target) == int:
                stri = stri + '    ' + str(order.ability.id) + ', ' + str(order.target) + ', ' + str(order.progress)
            else:
                stri = stri + '   ' + str(order.ability.id) + ', ' + self.txt(order.target) + ', ' + str(order.progress)
        print(stri)
        #stri = 'debug '
        #abilities = (await self.get_available_abilities([unt]))[0]
        #for abi in abilities:
        #    stri = stri + ' ' + abi.name
        #print(stri)


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

    def read_layout_ignore_creep(self, vakx,vaky) -> int:
        if (self.map_left <= vakx) and (vakx < self.map_right) and (self.map_bottom <= vaky) and (vaky < self.map_top):
            point = Point2((vakx,vaky))
            return layout_if.layout[vakx][vaky]
        else:
            return 3

    def read_height(self, vakx,vaky) -> int:
        if (self.map_left <= vakx) and (vakx < self.map_right) and (self.map_bottom <= vaky) and (vaky < self.map_top):
            return layout_if.height[vakx][vaky]
        else:
            return 99999

    def get_height(self,point) -> int:
        return self.read_height(round(point.x),round(point.y))

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
        # struc in all_structures_tobuildwalk or enemy structuretype
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
            # the add-on could still be there


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
            elif struc == INFESTEDCOCOON:
                for vakx in range(round(x - siz / 2), round(x + siz / 2)):
                    for vaky in range(round(y - siz / 2), round(y + siz / 2)):
                        dx = abs(vakx-x)
                        dy = abs(vaky-y)
                        if (dx <= 2) or (dy <= 2):
                            placable = placable and (self.read_layout(vakx, vaky) == mustbecolor)
            elif struc == AUTOTURRET:
                for vakx in range(round(x - siz / 2), round(x + siz / 2)):
                    for vaky in range(round(y - siz / 2), round(y + siz / 2)):
                        placable = placable and (self.read_layout_ignore_creep(vakx, vaky) == mustbecolor)
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
            if struc in [COMMANDCENTER,ORBITALCOMMAND,MAINCELLBLOCK]:
                # can not be placed close to a geyser or mineral
                siz = 9
                for vakx in range(round(x - siz / 2), round(x + siz / 2)):
                    for vaky in range(round(y - siz / 2), round(y + siz / 2)):
                        placable = placable and (self.read_layout(vakx,vaky) != 1)
                sizx = 11
                sizy = 5
                for vakx in range(round(x - sizx / 2), round(x + sizx / 2)):
                    for vaky in range(round(y - sizy / 2), round(y + sizy / 2)):
                        placable = placable and (self.read_layout(vakx, vaky) != 1)
                sizx = 5
                sizy = 11
                for vakx in range(round(x - sizx / 2), round(x + sizx / 2)):
                    for vaky in range(round(y - sizy / 2), round(y + sizy / 2)):
                        placable = placable and (self.read_layout(vakx, vaky) != 1)
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
        maxam = 200
        if thing in self.all_structures_tobuildwalk:
            if thing in [ARMORY,FUSIONCORE,ENGINEERINGBAY,GHOSTACADEMY]:
                maxam = 2
            if thing == FACTORY:
                maxam = 4
            if thing == STARPORT:
                maxam = 9
            if thing == MISSILETURRET:
                maxam = len(self.all_bases)*6
        elif thing in self.all_structures:
            pass
        elif thing in self.all_upgrades:
            maxam = 1
        else:
            # army
            if thing in [RAVEN]:
                maxam = 3
            if thing in [SIEGETANK,WIDOWMINE,REAPER]:
                maxam = 15
            if thing == LIBERATOR:
                maxam = 5
        return maxam

    def future_maxam_of_thing(self,thing) -> int:
        self.get_all_future_basepos()
        maxam = 200
        if thing in self.all_structures_tobuildwalk:
            if thing in [ARMORY,FUSIONCORE,ENGINEERINGBAY,GHOSTACADEMY]:
                maxam = 2
            if thing == FACTORY:
                maxam = 4
            if thing == STARPORT:
                maxam = 9
            if thing == MISSILETURRET:
                maxam = len(self.all_future_basepos)*6
        elif thing in self.all_structures:
            pass
        elif thing in self.all_upgrades:
            maxam = 1
        else:
            # army
            if thing in [RAVEN]:
                maxam = 3
            if thing in [SIEGETANK,WIDOWMINE,REAPER]:
                maxam = 15
            if thing == LIBERATOR:
                maxam = 5
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


    # a nine is a set of usually 9 tiles near a tile
    #
    # to get all enemies at dist<10 of pos:
    #     mytile = self.maptile_of_pos(pos)
    #     for tile in self.nine[mytile]:
    #         for ene in self.enemies_of_tile[tile]:
    #             if self.near(pos,ene.position,10):
    #
    def init_nine(self):
        self.nine = {}
        for maptile in range(0, self.maptiles):
            self.nine[maptile] = set()
        for maptile in range(0, self.maptiles):
            pos = self.pos_of_maptile(maptile)
            for dx in [-self.maptile_width,0,self.maptile_width]:
                for dy in [-self.maptile_width, 0, self.maptile_width]:
                    altpos = Point2((pos.x+dx,pos.y+dy))
                    altpos = self.into_map(altpos)
                    alttile = self.maptile_of_pos(altpos)
                    self.nine[maptile].add(alttile)

    def init_enemies_of_tile(self):
        self.enemies_of_tile = {}
        for maptile in range(0, self.maptiles):
            self.enemies_of_tile[maptile] = set()
        for ene in self.enemy_units | self.enemy_real_structures:
            # we need the structure itself, and do not care for out-of-vision, so use not enemy_structureinfo
            maptile = self.maptile_of_pos(ene.position)
            self.enemies_of_tile[maptile].add(ene)

    def init_goodguys_of_tile(self):
        self.goodguys_of_tile = {}
        for maptile in range(0, self.maptiles):
            self.goodguys_of_tile[maptile] = set()
        for myn in self.units:
            maptile = self.maptile_of_pos(myn.position)
            self.goodguys_of_tile[maptile].add(myn)
        for myn in self.structures:
            maptile = self.maptile_of_pos(myn.position)
            self.goodguys_of_tile[maptile].add(myn)


    # a expo is a group of maptiles, roughly around an expansion
    def init_expo(self):
        self.expos = len(self.expansion_locations)
        self.pos_of_expo = {}
        for expo in range(0, self.expos):
            self.pos_of_expo[expo] = self.expansion_locations[expo]
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
        # later the homeramp tile will be forced to loved_pos expansion

    def expo_of_pos(self, pos: Point2) -> int:
        return self.expo_of_maptile[self.maptile_of_pos(pos)]

    def ground_strength(self, one) -> float:
        # e.g. Stalker 39
        return sqrt(one.ground_dps * (one.health + one.shield))

    def air_strength(self, one) -> float:
        return sqrt(one.air_dps * (one.health + one.shield))

    def ground_strength_of_type(self, typ) -> float:
        strength = 0.0
        for (thing,stre) in self.ground_strength_hist:
            if thing == typ:
                strength = stre
        return strength

    def air_strength_of_type(self, typ) -> float:
        strength = 0.0
        for (thing,stre) in self.air_strength_hist:
            if thing == typ:
                strength = stre
        return strength

    def init_step_expo(self):
        self.minerals_of_expo = {}
        self.vespene_of_expo = {}
        self.scvs_of_expo = {}
        self.units_of_expo = {}
        self.structures_of_expo = {}
        self.enemy_units_of_expo = {}
        self.enemy_structureinfo_of_expo = {}
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
            self.enemy_structureinfo_of_expo[expo] = set()
            self.air_strength_of_expo[expo] = 0
            self.worth_of_expo[expo] = 0
        #
        for (onepos,onet) in self.all_minerals:
            expo = self.expo_of_pos(onepos)
            self.minerals_of_expo[expo].add((onepos,onet))
        for (onepos,onet) in self.all_vespene:
            expo = self.expo_of_pos(onepos)
            self.vespene_of_expo[expo].add((onepos,onet))
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
            self.worth_of_expo[expo] += self.worth_of_thing(kind)
        for tp in self.enemy_structureinfo:
            (typ,pos) = tp
            expo = self.expo_of_pos(pos)
            self.enemy_structureinfo_of_expo[expo].add(tp)
            self.ground_strength_of_expo[expo] -= self.ground_strength_of_type(typ)
            self.air_strength_of_expo[expo] -= self.air_strength_of_type(typ)
            self.worth_of_expo[expo] += self.worth_of_thing(typ)
        #

    #*********************************************************************************************************************

    #   techtree
    def init_structures(self,species,category,barra,builddura, size):
        self.log_fail((species in {'T','P','Z'}),'')
        self.log_fail((type(barra) == UnitTypeId),'')
        self.log_fail((category in self.all_categories),'')
        self.all_structures.append(barra)
        self.builddura_of_thing[barra] = builddura
        self.category_of_thing[barra] = category
        self.size_of_structure[barra] = size
        self.species_of_structure[barra] = species
        if species == 'T':
            if barra not in self.all_pfoc:
                if barra not in self.all_labs:
                    if barra not in self.landable:
                        self.all_structures_tobuildwalk.append(barra)

    def init_techtree(self,facto,barra):
        self.log_fail((type(facto) in [UpgradeId,UnitTypeId]),'first arg')
        self.log_fail((type(barra) in [UpgradeId,UnitTypeId]),'second arg')
        self.techtree.append( (facto,barra) )

    def init_cradle(self,mari,barra):
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
        cando = True
        self.missing = ''
        sepa = '('
        for pair in self.techtree:
            if pair[0] == facto:
                if not self.we_finished_a(pair[1]):
                    cando = False
                    self.missing += sepa + pair[1].name
                    sepa = ','
        self.missing += ')'
        return cando

    def check_nearly_techtree(self,facto,secs) -> bool:
        cando = True
        for pair in self.techtree:
            if pair[0] == facto:
                cando = cando and self.we_nearly_finished_a(pair[1],secs)
        return cando

    def check_future_techtree(self,facto) -> bool:
        cando = True
        for pair in self.techtree:
            if pair[0] == facto:
                cando = cando and self.we_started_a(pair[1])
        return cando

    def init_maxhealth(self, thing, maxh):
        self.maxhealth[thing] = maxh

    def init_bcenemy(self, thing, danger, hate):
        # shoot at most hated
        # flee at dangersum 100
        self.bcenemies.add(thing)
        self.danger_of_bcenemy[thing] = danger
        self.hate_of_bcenemy[thing] = hate

    def init_army(self,thing,dura,supply,airground):
        self.all_army.append(thing)
        self.supply_of_army[thing] = supply
        self.builddura_of_thing[thing] = dura
        self.airground_of_unit[thing] = airground
        self.category_of_thing[thing] = 'army'

    def init_labarmy(self):
        for thing in self.all_army:
            needstechlab = False
            for pair in self.techtree:
                if pair[0] == thing:
                    if pair[1] in self.all_techlabs:
                        needstechlab = True
            if needstechlab:
                self.all_labarmy.append(thing)

    def init_upgrade(self,upg,time, benefitter):
        self.all_upgrades.append(upg)
        self.builddura_of_thing[upg] = time
        self.upgrade_benefitter.add((upg,benefitter))
        self.category_of_thing[upg] = 'upgrade'

    def we_finished_a(self,barra) -> bool:
        have = False
        for (thing,pos) in self.birds:
            have = have or (thing == barra)
        return have

    def we_nearly_finished_a(self,barra,secs) -> bool:
        have = False
        for (thing,pos) in self.birds:
            have = have or (thing == barra)
        for (marty,bartype,pos,dura) in self.eggs:
            have = have or ((marty == barra) and (dura <= secs))
        return have

    def eggorbird(self,barra) -> bool:
        have = False
        for (thing,pos) in self.birds:
            have = have or (thing == barra)
        for (marty,bartype,pos,dura) in self.eggs:
            have = have or (marty == barra)
        return have

    def eggorbird_amount(self,barra) -> int:
        have = 0
        for (thing,pos) in self.birds:
            if (thing == barra):
                have += 1
        for (marty,bartype,pos,dura) in self.eggs:
            if (marty == barra):
                have += 1
        return have

    def we_finished_amount(self, barra) -> int:
        have = 0
        for (thing,pos) in self.birds:
            if (thing == barra):
                have += 1
        return have

    def we_started_a(self,barra) -> bool:
        have = False
        for (thing,pos) in self.birds:
            have = have or (thing == barra)
        for (marty,bartype,pos,dura) in self.eggs:
            have = have or (marty == barra)
        for (marty,bartype,pos,dura,owner) in self.preps:
            have = have or (marty == barra)
        for (thing,pos,owner) in self.thoughts:
            have = have or (thing == barra)
        for (thing,pos,owner) in self.dreams:
            have = have or (thing == barra)
        return have

    def we_started_at(self,barra,atpos) -> bool:
        have = False
        for (thing,pos) in self.birds:
            have = have or ((thing == barra) and (pos == atpos))
        for (marty,bartype,pos,dura) in self.eggs:
            have = have or ((marty == barra) and (pos == atpos))
        for (marty,bartype,pos,dura,owner) in self.preps:
            have = have or ((marty == barra) and (pos == atpos))
        for (thing,pos,owner) in self.thoughts:
            have = have or ((thing == barra) and (pos == atpos))
        for (thing,pos,owner) in self.dreams:
            have = have or ((thing == barra) and (pos == atpos))
        return have

    def we_started_hall_at(self, atpos) -> bool:
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
        for (thing,pos,owner) in self.dreams:
            have = have or ((pos == atpos) and (thing in kinds))
        return have

    def we_started_amount(self,barra) -> int:
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
        for (thing,pos,owner) in self.dreams:
            if (thing == barra):
                have += 1
        return have

    def we_thoughtetc_at(self,barra,atpos) -> bool:
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

    def we_thoughtetc_amount(self,barra) -> int:
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

    def we_preppedetc_amount(self,barra) -> int:
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
        return have

    def has_finished_reactor(self,spot) -> bool:
        has = False
        for (thing,pos) in self.birds:
            if thing in self.all_reactors:
                if pos == spot:
                    has = True
        return has


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

    def prevent_doubling(self, tag):
        self.doubling_frame[tag] = self.frame

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

    def worth_of_thing(self,thing) -> int:
        cost = self.get_total_cost(thing)
        worth = cost.minerals + 2 * cost.vespene
        return worth

    def allow_throw(self, thing) -> bool:
        # throw max 2 parallel per category (army 8)
        # also admit waitfree throws
        allow = False
        if self.check_techtree(thing):
            if self.game_phase != 'opening':
                category = self.category_of_thing[thing]
                parallel = 0
                for (th, pos, status, owner) in self.throwspots:
                    if self.category_of_thing[th] == category:
                        parallel += 1
                for (th,po,status) in self.buildorder_exe:
                    if self.category_of_thing[th] == category:
                        parallel += 1
                if category == 'army':
                    allow = (parallel < 8)
                else:
                    allow = (parallel < 2)
                # waitfree throws:
                if self.can_pay(thing):
                    if thing in self.all_structures_tobuildwalk:
                        allow = True
                        # please do not ask for more than you want
                    elif thing in self.all_labarmy:
                        crad = self.cradle_of_thing(thing)
                        if self.amount_usable_teched[crad] > 0:
                            allow = True
                    else:
                        crad = self.cradle_of_thing(thing)
                        if crad in {BARRACKS,FACTORY,STARPORT,ARMORY,ENGINEERINGBAY}:
                            if self.amount_usable[crad] > 0:
                                allow = True
                        else:
                            allow = True
        return allow

    def add_purse(self,thing):
        cost = self.get_added_cost(thing)
        self.purse.minerals += cost.minerals
        self.purse.vespene += cost.vespene

    def del_purse(self,thing):
        cost = self.get_added_cost(thing)
        self.purse.minerals -= cost.minerals
        self.purse.vespene -= cost.vespene

    def in_purse(self,thing) -> bool:
        ok = True
        cost = self.get_added_cost(thing)
        ok = ok and (self.purse.minerals >= cost.minerals)
        ok = ok and (self.purse.vespene >= cost.vespene)
        return ok

    def can_pay(self,thing) -> bool:
        # purse contains a small amount for max self.patience frames
        cost = self.get_added_cost(thing)
        mis_min = cost.minerals + self.purse.minerals - self.minerals
        mis_gas = cost.vespene + self.purse.vespene - self.vespene
        self.missing = ''
        sepa = '('
        if mis_min > 0:
            self.missing += sepa + str(mis_min)+' minerals'
            sepa = ','
        if mis_gas > 0:
            self.missing += sepa + str(mis_gas) + ' gas'
            sepa = ','
        self.missing += ')'
        return (mis_min <= 0) and (mis_gas <= 0)

    def can_nearly_pay(self,thing,secs) -> bool:
        # purse contains a small amount for max self.patience frames
        cost = self.get_added_cost(thing)
        mimmers = self.count_of_job['mimminer'] + 6 * len(self.structures(ORBITALCOMMAND))
        gassers = self.count_of_job['gasminer']
        future_minerals = self.minerals + secs * (mimmers * self.mim_speed)
        future_vespene = self.vespene + secs * (gassers * self.gas_speed)
        return (future_minerals >= self.purse.minerals + cost.minerals) and (future_vespene >= self.purse.vespene + cost.vespene)


    def bug_can_pay(self,upg) -> bool:
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

    def create_rockblock(self, pos,measure):
        # Integer pos. Called with odd as well as with even measure.
        disx = measure[0] - (measure[0] // 2)
        disy = measure[1] - (measure[1] // 2)
        for tx in range(0,measure[0]):
            px = round(pos.x + tx - disx)
            for ty in range(0,measure[1]):
                py = round(pos.y + ty - disy)
                layout_if.layout[px][py] = 1

    def create_unbuildable(self,pos):
        for tx in range(0,2):
            px = round(pos.x + tx -1)
            for ty in range(0,2):
                py = round(pos.y + ty -1)
                layout_if.layout[px][py] = 2 # unbuildable

    def create_block(self, pos,measure):
        # Call with half-pos when measure is odd.
        disx = measure[0] / 2
        disy = measure[1] / 2
        for tx in range(0,measure[0]):
            px = round(pos.x + tx - disx)
            for ty in range(0,measure[1]):
                py = round(pos.y + ty - disy)
                layout_if.layout[px][py] = 1

    def get_layout(self):
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
        for (mimpos,mimt) in self.all_minerals:
            # mimpos always x whole, y half
            layout_if.layout[round(mimpos.x-1)][round(mimpos.y-0.5)] = 1
            layout_if.layout[round(mimpos.x+0)][round(mimpos.y-0.5)] = 1
        for gas in self.vespene_geyser:
            self.create_block(gas.position,(3,3))
        for tow in self.watchtowers:
            self.create_block(tow.position, (2, 2))
        for rock in self.destructables:  # copied from Sharpy
            rock_type = rock.type_id
            if rock.name == "MineralField450":
                # Attempts to solve the issue with sc2 linux 4.10 vs Windows 4.11
                self.create_rockblock(rock.position, (2, 1))
            elif rock_type in rocks_if.unbuildable_rocks:
                self.create_unbuildable(rock.position)
            elif rock_type in rocks_if.breakable_rocks_2x2:
                self.create_rockblock(rock.position, (2, 2))
            elif rock_type in rocks_if.breakable_rocks_4x4:
                self.create_rockblock(rock.position, (4, 3))
                self.create_rockblock(rock.position, (3, 4))
            elif rock_type in rocks_if.breakable_rocks_6x6:
                self.create_rockblock(rock.position, (6, 4))
                self.create_rockblock(rock.position, (5, 5))
                self.create_rockblock(rock.position, (4, 6))
            elif rock_type in rocks_if.breakable_rocks_4x2:
                self.create_rockblock(rock.position, (4, 2))
            elif rock_type in rocks_if.breakable_rocks_2x4:
                self.create_rockblock(rock.position, (2, 4))
            elif rock_type in rocks_if.breakable_rocks_6x2:
                self.create_rockblock(rock.position, (6, 2))
            elif rock_type in rocks_if.breakable_rocks_2x6:
                self.create_rockblock(rock.position, (2, 6))
            elif rock_type in rocks_if.breakable_rocks_diag_BLUR:
                for y in range(-4, 6):
                    if y == -4:
                        self.create_rockblock(rock.position + Point2((y + 2, y)), (1, 1))
                    elif y == 5:
                        self.create_rockblock(rock.position + Point2((y - 2, y)), (1, 1))
                    elif y == -3:
                        self.create_rockblock(rock.position + Point2((y - 1, y)), (3, 1))
                    elif y == 4:
                        self.create_rockblock(rock.position + Point2((y + 1, y)), (3, 1))
                    else:
                        self.create_rockblock(rock.position + Point2((y, y)), (5, 1))
            elif rock_type in rocks_if.breakable_rocks_diag_ULBR:
                for y in range(-4, 6):
                    if y == -4:
                        self.create_rockblock(rock.position + Point2((-y - 2, y)), (1, 1))
                    elif y == 5:
                        self.create_rockblock(rock.position + Point2((-y + 2, y)), (1, 1))
                    elif y == -3:
                        self.create_rockblock(rock.position + Point2((-y + 1, y)), (3, 1))
                    elif y == 4:
                        self.create_rockblock(rock.position + Point2((-y - 1, y)), (3, 1))
                    else:
                        self.create_rockblock(rock.position + Point2((-y, y)), (5, 1))

    # *********************************************************************************************************************

    def get_dock(self, point) -> Point2:
        bestpos = self.hisleft
        bestsd = 99999
        for base in self.all_mine_bases:
            expo = self.expo_of_pos(base.position)
            if len(self.scvs_of_expo[expo]) >= 3:
                pos = self.airport_of_expo[expo]
                sd = self.sdist(pos,point)
                if sd < bestsd:
                    bestsd = sd
                    bestpos = pos
        return bestpos

    #*********************************************************************************************************************

    #   fix secondary information
    #   call just before using count_of_job when precize numbers are important
    def fix_count_of_job(self):
        #       count_of_job
        for j in (self.good_jobs + self.bad_jobs + self.no_jobs):
            self.count_of_job[j] = 0
        for scvt in self.job_of_scvt:
            j = self.job_of_scvt[scvt]
            self.count_of_job[j] += 1

    def fix_nminers_of_mimt(self):
        # calculate the amount of gatherers on each mineral, using mim_of_minert
        self.nminers_of_mimt = {}
        for mim in self.all_mim_to_mine:
            (mimpos,mimt) = mim
            self.nminers_of_mimt[mimt] = 0
        for scvt in self.mim_of_minert:
            mim = self.mim_of_minert[scvt]
            if mim in self.all_mim_to_mine:
                (mimpos, mimt) = mim
                self.nminers_of_mimt[mimt] += 1

    def fix_nminers_of_gast(self):
        # calculate the amount of gatherers on each gas, using gas_of_minert
        self.nminers_of_gast = {}
        for gas in self.all_gas_to_mine:
            (gaspos, gast) = gas
            self.nminers_of_gast[gast] = 0
        for scvt in self.gas_of_minert:
            gas = self.gas_of_minert[scvt]
            if gas in self.all_gas_to_mine:
                (gaspos,gast) = gas
                self.nminers_of_gast[gast] += 1

    def mimminer_vacatures(self) -> int:
        return len(self.all_mim_to_mine) * 2 - len(self.mim_of_minert)

    def gasminer_vacatures(self) -> int:
        return len(self.all_gas_to_mine) * 3 - len(self.gas_of_minert)

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
        square = (round(self.loved_pos.x+2.5),round(self.loved_pos.y-0.5))
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
                    job = self.job_of_scvt[scvt]
                    if job in (self.bad_jobs + self.no_jobs):
                        if (job != 'suicider'):
                            hope = True
                            sd = self.sdist(scv.position,point)
                            #  accept idler if 1.7 times as far
                            if job in self.no_jobs:
                                sd /= 3
                            #   accept mimminer if 1.4 times as far
                            if job in ['applicant','candidate','carrier','mimminer']:
                                sd /= 2
                            if (sd < best_sdist) and (sd > 0.5*0.5): # dont select an scv to repair itself
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
        # suggestion: call    if self.count_of_job['idler'] > 0;
        best_sdist = 99999
        best_scvt = self.notag
        for scv in self.units(SCV):
            scvt = scv.tag
            job = self.job_of_scvt[scvt]
            if (job in self.no_jobs) and (job != 'suicider'):
                sd = self.sdist(scv.position,point)
                if sd < best_sdist:
                    best_sdist = sd
                    best_scvt = scvt
        scvt = best_scvt
        self.log_fail((best_sdist < 99999),'no idler found.')
        return scvt        

    def get_near_cct_wanted(self,point) -> int:
        best_sdist = 80000
        best_cct = self.notag
        for cc in self.all_mine_bases:
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

    def hoxy(self,point) -> bool:
        return self.near(point,self.loved_pos,63)

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
        # the buildings are ready for a second, so really usable
        self.birds = set()
        for kind in self.all_structures:
            for stru in self.structures(kind):
                if stru.tag in self.readies:
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
        # lowerbound for the amount of nukes-in-silo, misses e.g. if academy is upgrading
        for ga in self.structures(GHOSTACADEMY):
            if ga.tag in self.readies:
                if ga.tag in self.idles:
                    if self.can_pay(NUKESILONOVA):
                        if self.check_techtree(NUKESILONOVA):
                            abilities = (await self.get_available_abilities([ga]))[0]
                            if AbilityId.BUILD_NUKE not in abilities:
                                self.birds.add((NUKESILONOVA,ga.position))
        self.log_birds()

    def get_eggs(self):
        # overview of things currently being made
        self.eggs = set()
        for scv in self.units(SCV):
            scvt = scv.tag
            if scvt in self.goal_of_trabu_scvt:
                if self.job_of_scvt[scvt] in {'fencer','builder'}:
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
                if martype in self.all_reactors:
                    abi = AbilityId.BUILD_REACTOR
                else:
                    abi = AbilityId.BUILD_TECHLAB
            elif martype == NUKESILONOVA:
                abi = AbilityId.BUILD_NUKE
            else:
                abi = sc2.dicts.unit_train_build_abilities.TRAIN_INFO[bartype][martype]['ability']
            for bar in self.structures(bartype):
                if bar.tag in self.readies:
                    if bar.is_using_ability(abi):
                        for order in bar.orders:
                            # bug if making viking and medivac
                            progress = order.progress
                            # the LAB,PFOC progress bugs. Thus extra own administration.
                            # (this implementation fails if a lab is being destroyed while building and is rebuilt)
                            if martype in self.all_labs + self.all_pfoc:
                                seconds = self.builddura_of_thing[martype]
                                seen = False
                                for (tag,startpos,startframe) in self.labprogress_buildframes:
                                    if (tag == bar.tag) and (startpos == bar.position):
                                        seen = True
                                        progress = (self.frame - startframe) / (seconds * self.frames_per_second)
                                        if progress > 1.2:
                                            seen = False
                                            progress = 0
                                        progress = min(1, progress)
                                if not seen:
                                    self.labprogress_buildframes.add((bar.tag,bar.position,self.frame))
                            # Prevent double with birds. Paranoid?
                            inbirds = False
                            for (birdthing,birdpos) in self.birds:
                                if (birdthing == martype) and (birdpos == bar.position):
                                    inbirds = True
                            if not inbirds:
                                restdura = dura * (1.0 - progress)
                                pos = self.position_of_building(bar)
                                self.eggs.add((martype,bartype,pos,restdura))
        martype = SCV
        abi = AbilityId.COMMANDCENTERTRAIN_SCV
        for bartype in [COMMANDCENTER,ORBITALCOMMAND,PLANETARYFORTRESS]:
            for bar in self.structures(bartype):
                if bar.tag in self.readies:
                    if bar.is_using_ability(abi):
                        dura = self.builddura_of_thing[martype]
                        progress = bar.orders[0].progress
                        restdura = dura * (1.0 - progress)
                        pos = bar.position
                        self.eggs.add((martype,bartype,pos,restdura))
        for kind in self.all_structures:
            for stru in self.structures(kind).ready:
                if stru.tag not in self.readies:
                    basekind = self.basekind_of(kind)
                    bartype = self.cradle_of_thing(basekind)
                    if bartype is None:
                        bartype = SCV
                    pos = self.position_of_building(stru)
                    restdura = 0.5
                    isthere = False
                    for (ma,ba,po,du) in self.eggs:
                        if (ma == basekind) and (ba == bartype) and (po == pos):
                            isthere = True
                    if not isthere:
                        self.eggs.add((basekind,bartype,pos,restdura))
        self.log_eggs()

    def get_preps(self):
        # overview of things currently being prepaired
        self.preps = set()
        for scv in self.units(SCV):
            scvt = scv.tag
            if scvt in self.goal_of_trabu_scvt:
                if self.job_of_scvt[scvt] in ('traveller','settler'):
                    goal = self.goal_of_trabu_scvt[scvt]
                    thing = self.structure_of_trabu_scvt[scvt]
                    owner = self.owner_of_trabu_scvt[scvt]
                    pos = scv.position
                    restdura = self.walk_duration(pos,goal)
                    self.preps.add((thing, scv, goal, restdura, owner))
        for strt in self.ambition_of_strt: # pfoc, labs
            martype = self.ambition_of_strt[strt]
            owner = self.owner_of_ambistrt[strt]
            dura = self.ambitiondura
            for abar in self.structures:
                if abar.tag == strt:
                    bar = abar
                    pos = self.position_of_building(abar)
            for (othermartype,otherbartype,otherpos,otherdura) in self.eggs: # calc eggs first
                if (otherbartype == bar.type_id) and (otherpos == pos):
                    dura = otherdura
            self.preps.add((martype, bar.type_id, pos, dura, owner))
        for (strtype,strtag,martype,owner) in self.gym: # upgr, army
            dura = self.gymdura
            for abar in self.structures(strtype):
                if abar.tag == strtag:
                    bar = abar
                    pos = self.position_of_building(abar)
            for (othermartype,otherbartype,otherpos,otherdura) in self.eggs: # calc eggs first
                if (otherbartype == bar.type_id) and (otherpos == pos):
                    dura = otherdura
            self.preps.add((martype, bar.type_id, pos, dura, owner))
        # prevent double with eggs
        # de code die bv ambition_of_strt corrigeert is elders.
        todel = set()
        for mbpdo in self.preps:
            (martype,bartype,pos,dura,owner) = mbpdo
            for (othermartype,otherbartype,otherpos,otherdura) in self.eggs: # calc eggs first
                if (martype == othermartype) and (pos == otherpos) and (otherdura > self.ambitiondura):
                    todel.add(mbpdo)
        self.preps -= todel
        self.log_preps()

    # *********************************************************************************************************************
    #  bagofthings, bagoftree, bagofcradle, buildseries

    def get_all_future_basepos(self):
        afb = set()
        for cc in self.all_mine_bases:
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
        

    def find_tobuildwalk_a_place(self, building, actual) -> bool:
        # actual: 'plan'/'now'
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
            self.get_all_future_basepos()
            tried = 0
            found = False
            while (not found) and (tried < 20):
                place = random.choice(self.expansion_locations)
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
                            for cc in self.all_mine_bases:
                                if self.near(place, cc.position, self.miner_bound):
                                    seen = True
                            if seen:
                                places.append(place)
            if len(places) > 0:
                place = random.choice(places)
                found = True
            # Then with future bases.
            if not found:
                if actual == 'plan':
                    self.get_all_future_basepos()
                    places = []
                    for gey in self.vespene_geyser:
                        place = gey.position
                        if self.check_layout(building, place):
                            if not self.we_started_at(building, place):
                                if place not in [pl for (th, pl) in self.buildorder]:
                                    seen = False
                                    for ccpos in self.all_future_basepos:
                                        if self.near(place, ccpos, self.miner_bound):
                                            seen = True
                                    if seen:
                                        places.append(place)
                if len(places) > 0:
                    place = random.choice(places)
                    found = True
        elif (building in self.all_structures_tobuildwalk) and (not found):
            # normal building
            if len(self.all_mine_bases) > 0:
                if actual == 'plan':
                    self.get_all_future_basepos()
                    ccpos = random.choice(tuple(self.all_future_basepos))
                else:
                    cc = random.choice(self.all_mine_bases)
                    ccpos = cc.position
                dist = 6
                if building == MISSILETURRET:
                    dist = random.randrange(-10, 10)
                fixplace = ccpos.towards(self.map_center, dist)
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

    def bagofcradle_of_bagofthings(self):
        # Add cradle parents. Flying is not good enough.
        # Accept buildings beyond the bag: prep egg bird
        # For 2 bcs and 2 starporttechlabs, cradle about 2 starports.
        # For 3 marines, cradle about 1 barracks.
        stri = 'bagofthings: '
        for thing in self.bagofthings:
            stri = stri + thing.name + ' '
        self.log_success(stri)
        #
        # for army, sometimes extra cradles to build parallel.
        needed_dura = {}
        needed_onedura = {}
        for thing in self.bagofthings:
            if thing not in self.all_structures_tobuildwalk:
                dura = self.builddura_of_thing[thing]
                barra = self.cradle_of_thing(thing)
                if barra in needed_dura:
                    needed_dura[barra] += dura
                    needed_onedura[barra] = max(dura,needed_onedura[barra])
                else:
                    needed_dura[barra] = dura
                    needed_onedura[barra] = dura
        # For transformations, an integer amount is needed.
        am = {}
        for thing in [BARRACKS,FACTORY,STARPORT,COMMANDCENTER]:
            am[thing] = 0
        for thing in self.bagofthings:
            if thing in self.all_labs + self.all_pfoc:
                if thing not in self.standalone_labs:
                    barra = self.cradle_of_thing(thing)
                    am[barra] += 1
        # needed
        needed = [] # multiset
        for barra in needed_dura:
            dura = needed_dura[barra]
            onedura = needed_onedura[barra]
            floatamount = dura / onedura
            # round up
            amount = 0
            while floatamount > 0:
                amount += 1
                floatamount -= 1
            # max with am
            if barra in am:
                amount = max(amount,am[barra])
            # put in needed
            while amount > 0:
                needed.append(barra)
                amount -= 1
        # have
        have = []
        for (thing, pos) in self.birds:
            have.append(thing)
            if thing in self.all_pfoc:
                have.append(COMMANDCENTER)
        for (thing, bartype, pos, dura) in self.eggs:
            have.append(thing)
            if thing in self.all_pfoc:
                have.append(COMMANDCENTER)
        for (thing,scv,pos,dura,owner) in self.preps:
            have.append(thing)
        # used
        used = []
        for (thing, pos) in self.birds:
            if thing in self.all_labs + self.all_pfoc:
                if thing not in self.standalone_labs:
                    barra = self.cradle_of_thing(thing)
                    used.append(barra)
        for (thing, bartype, pos, dura) in self.eggs:
            if thing in self.all_labs + self.all_pfoc:
                if thing not in self.standalone_labs:
                    barra = self.cradle_of_thing(thing)
                    used.append(barra)
        for (thing,scv,pos,dura,owner) in self.preps:
            if thing in self.all_labs + self.all_pfoc:
                if thing not in self.standalone_labs:
                    barra = self.cradle_of_thing(thing)
                    used.append(barra)
        # free = have - used
        free = have
        for thing in used:
            if thing in free:
                del free[free.index(thing)]
            else:
                print('explain this ?! ' + thing.name)
                for th in have:
                    print('have ' + th.name)
                for th in used:
                    print('used ' + th.name)
                for (th, pos) in self.birds:
                    print('bird ' + th.name)
                for (th, bartype, pos, dura) in self.eggs:
                    print('egg ' + th.name)
                for (th, scv, pos, dura, owner) in self.preps:
                    print('prep ' + th.name)
                # exit pgm     saw egg starporttechlab too much
                del free[free.index(thing)]
        # needed = needed - free
        for thing in free:
            if thing in needed:
                del needed[needed.index(thing)]
        # needed = needed - bagofthings
        for thing in self.bagofthings:
            if thing in needed:
                del needed[needed.index(thing)]
        # append needed
        self.bagofcradle = self.bagofthings + needed
        # show
        stri = 'bagofcradle: '
        for th in self.bagofcradle:
            stri = stri + th.name + ' '
        self.log_success(stri)

    def bagoftree_of_bagofcradle(self):
        # add techtree parents
        bag = self.bagofcradle.copy()
        stable = False
        while not stable:
            stable = True
            extra = set()
            for th in bag:
                for pair in self.techtree:
                    if pair[0] == th:
                        otherth = pair[1]
                        haveit = (otherth in bag)
                        for (marty, bartype, pos, dura) in self.eggs:
                            haveit = haveit or (marty == otherth)
                        for (thing,pos) in self.birds:
                            haveit = haveit or (thing == otherth)
                        if haveit:
                            self.log_success('need tree ' + otherth.name + ' already satisfied')
                        else:
                            self.log_success('need tree ' + otherth.name)
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
        # sort until executable
        # May use buildseries_old as an example. In the end refresh buildseries_old
        # 1) CHECK WHETHER ALL CAN BE PUT
        self.hoopy_get_sit()
        toput = self.bagoftree.copy()
        while len(toput) > 0:
            # There should always be one in toput that you can do. Get one
            stri = 'can put'
            cando = []
            for th in toput:
                if self.hoopy_can_add(th):
                    cando.append(th)
                    stri = stri + ' ' + th.name
            if len(cando) > 0:
                candoone = cando[0]
                self.hoopy_add(candoone)
                self.log_success(stri + ', putting ' + candoone.name)
                del toput[toput.index(candoone)]
            else:
                for th in toput:
                    self.log_success('BUG cannot put all; not ' + th.name)
                candoone = cando[0] # quit
        # 2) NEEDS TREE
        self.hoopy_get_sit()
        needs = set()
        for thing in self.bagoftree:
            for pair in self.techtree:
                if pair[0] == thing:
                    need = pair[1]
                    if need not in self.hoopy_made:
                        needs.add((thing,need))
        # 3) EST (earliest start time). Consider preps to be made.
        est = {}
        changed = True
        while changed:
            changed = False
            for thing in self.bagoftree:
                if thing not in est:
                    calculable = True
                    myest = 0
                    for pair in needs:
                        if pair[0] == thing:
                            need = pair[1]
                            if need in est:
                                itsest = est[need]
                                itsend = itsest + self.builddura_of_thing[need]
                                myest = max(myest, itsend)
                            else:
                                calculable = False
                    if calculable:
                        est[thing] = myest
                        changed = True
        # 4) ETOC (endtime of chain).
        etoc = {}
        changed = True
        while changed:
            changed = False
            for thing in self.bagoftree:
                if thing not in etoc:
                    calculable = True
                    myetoc = est[thing] + self.builddura_of_thing[thing]
                    for pair in needs:
                        if pair[1] == thing:
                            depender = pair[0]
                            if depender in etoc:
                                itsetoc = etoc[depender]
                                myetoc = max(myetoc, itsetoc)
                            else:
                                calculable = False
                    if calculable:
                        etoc[thing] = myetoc
                        changed = True
        # 5)
        self.hoopy_get_sit()
        toput = self.bagoftree.copy()
        series = []
        oldidea = self.buildseries_old
        while len(toput) > 0:
            # There should always be one in toput that you can do. Get one
            cando = []
            for th in toput:
                if self.hoopy_can_add(th):
                    cando.append(th)
            # get one you can do
            bestix = 99999
            for one in cando:
                if one in oldidea:
                    ix = oldidea.index(one)
                else:
                    ix = 99999 - etoc[one]
                if ix < bestix:
                    bestix = ix
                    candoone = one
            self.hoopy_add(candoone)
            series.append(candoone)
            del toput[toput.index(candoone)]
            if candoone in oldidea:
                del oldidea[oldidea.index(candoone)]
        self.buildseries = series
        self.buildseries_old = series
        stri = 'buildseries: '
        for th in self.buildseries:
            stri = stri + th.name + ' '
        self.log_success(stri)


    def crad_places_for_thing(self, thing):
        # thing is labs, pfoc, upgr, or army. It has a unique cradle.
        crad = self.cradle_of_thing(thing)
        # needstechlab ?/n/y
        needstechlab = '?'
        if thing in self.all_labs + self.all_pfoc:
            needstechlab = 'n'
        for pair in self.techtree:
            if pair[0] == thing:
                if (pair[1] in self.all_techlabs) and (pair[1] != crad):
                    # stimpack is upgraded IN a lab, but that lab does not need a lab.
                    needstechlab = 'y'
        # Everything has a cradle
        # crad could exist, or be ordered, or be in the buildorder
        self.crad_places = set()
        for stru in self.structures(crad):
            if stru.tag in self.readies:
                pos = self.position_of_building(stru)
                if pos in self.bui_min_lab:
                    if (self.bui_min_lab[pos] == 1) and (needstechlab != 'y'):
                        self.crad_places.add(pos)
                    if (self.bui_min_lab[pos] == 0) and (needstechlab != 'n'):
                        self.crad_places.add(pos)
                elif needstechlab == '?':
                    self.crad_places.add(pos)
        for scvt in self.goal_of_trabu_scvt:
            if self.structure_of_trabu_scvt[scvt] == crad:
                pos = self.goal_of_trabu_scvt[scvt]
                if pos in self.bui_min_lab:
                    if (self.bui_min_lab[pos] == 1) and (needstechlab != 'y'):
                        self.crad_places.add(pos)
                    if (self.bui_min_lab[pos] == 0) and (needstechlab != 'n'):
                        self.crad_places.add(pos)
                elif needstechlab == '?':
                    self.crad_places.add(pos)
        for (otherthing, pos) in self.buildorder:
            if otherthing == crad:
                if pos in self.bui_min_lab:
                    if (self.bui_min_lab[pos] == 1) and (needstechlab != 'y'):
                        self.crad_places.add(pos)
                    if (self.bui_min_lab[pos] == 0) and (needstechlab != 'n'):
                        self.crad_places.add(pos)
                elif (needstechlab == '?') or (pos == self.somewhere):
                    self.crad_places.add(pos)


    def buildorder_of_buildseries(self):
        # buildorder = buildseries + place
        # also: change infested to normal
        # if skipping, some of the rest maybe cannot be built. Hoopy checks this.
        # Happy is used for bui_min_lab, used in crad_places_for_thing
        self.buildorder = []
        self.hoopy_get_sit()
        self.happy_get_sit()
        for infathing in self.buildseries:
            thing = self.basekind_of(infathing)
            if self.hoopy_can_add(thing):
                place = self.nowhere
                if thing in self.all_structures_tobuildwalk:
                    if place == self.nowhere:
                        if self.find_tobuildwalk_a_place(infathing,'plan'):
                            place = self.function_result_Point2
                    if place == self.nowhere:
                        self.log_success('skipping a '+infathing.name+' because I found no position!')
                        # if skipping, some of the rest maybe cannot be built. Hoopy checks this.
                    else:
                        self.buildorder.append((thing, place))
                        self.write_layout(thing, place)
                        self.hoopy_add(thing)
                        self.happy_add(thing,place)
                else: # army, labs, upgr, pfoc
                    if place == self.nowhere:
                        self.crad_places_for_thing(thing)
                        # get a random cradle place
                        if len(self.crad_places)==0:
                            self.log_success('Can not place '+thing.name)
                        else:
                            #place = random.choice(tuple(self.crad_places))
                            place = self.somewhere
                            # exception for the swap techlab
                            if thing == BARRACKSTECHLAB:
                                if self.barracks_techlab_advice != self.nowhere:
                                    place = self.barracks_techlab_advice
                                    self.barracks_techlab_advice = self.nowhere
                    if place != self.nowhere:
                        self.buildorder.append((thing, place))
                        self.hoopy_add(thing)
                        self.happy_add(thing,place)


    # *********************************************************************************************************************


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
        # prep_buildorder will have an is_prepped field.
        # e.g. two medivacs are in the buildorder, one is prepped.
        prep_buildorder = []
        for (beautiful_thing,beautiful_place) in self.buildorder:
            prep_buildorder.append((beautiful_thing,beautiful_place,False))
        todel = []
        for buildplan in current_walking:
            (th, scvt, pos, sr, sc, fi) = buildplan
            if (th,pos,False) in prep_buildorder:
                prep_buildorder[prep_buildorder.index((th,pos,False))] = (th,pos,True)
            elif (th,self.somewhere, False) in prep_buildorder:
                prep_buildorder[prep_buildorder.index((th,self.somewhere,False))] = (th,self.somewhere,True)
        for trainplan in current_ambition | current_gym:
            (th, ata, pos, sr, sc, fi) = trainplan
            if (th,pos,False) in prep_buildorder:
                prep_buildorder[prep_buildorder.index((th,pos,False))] = (th,pos,True)
            elif (th,self.somewhere, False) in prep_buildorder:
                prep_buildorder[prep_buildorder.index((th,self.somewhere,False))] = (th,self.somewhere,True)
        #
        plannable = True
        toskip = set()
        for (beautiful_thing,beautiful_place, is_prepped) in prep_buildorder:
            if plannable:
                self.log_planning('Planning a ' + beautiful_thing.name)
                # MAKE A BEAUTIFUL_BUILDPLAN, PLAN_MOMENT AND EVENTS, AND APPEND BP TO PLANNING
                beautiful_cradle = self.cradle_of_thing(beautiful_thing)
                tocalculate = not is_prepped
                if is_prepped:
                    for buildplan in current_walking:
                        (th, scvt, pos, sr, sc, fi) = buildplan
                        if (th == beautiful_thing):
                            if (pos == beautiful_place) or (beautiful_place == self.somewhere):
                                if buildplan not in self.planning:
                                    beautiful_buildplan = buildplan
                                    self.planning.append(beautiful_buildplan)
                                    plan_moment = sc
                    for trainplan in current_ambition | current_gym:
                        (th, ata, pos, sr, sc, fi) = trainplan
                        if (th == beautiful_thing):
                            if (pos == beautiful_place) or (beautiful_place == self.somewhere):
                                buildplan = (th, self.notag, pos, sr, sc, fi)
                                if buildplan not in self.planning:
                                    beautiful_buildplan = buildplan
                                    self.planning.append(beautiful_buildplan)
                                    plan_moment = sc
                if tocalculate:
                    # fix_somewhere, but in the current situation
                    # choose a specific cradle if the choice was delayed with 'somewhere'
                    if (beautiful_place == self.somewhere):
                        # beautiful_thing is labs, pfoc, upgr, or army. It has a unique cradle.
                        # needstechlab ?/n/y
                        # needsreactor ?/n/y
                        if beautiful_thing == BARRACKSTECHLAB:
                            lookatme = True
                        needstechlab = '?'
                        needsreactor = '?'
                        if beautiful_thing in self.all_labs + self.all_pfoc:
                            needstechlab = 'n'
                            needsreactor = 'n'
                        for pair in self.techtree:
                            if pair[0] == beautiful_thing:
                                if (pair[1] in self.all_techlabs) and (pair[1] != beautiful_cradle):
                                    needstechlab = 'y'
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
                                slots = 1
                                hastechlab = 'n'
                                hasreactor = 'n'
                                for (otherthing, otherx, othery) in current_buildings_and_parts:
                                    if (otherthing != thing) and (otherx == x) and (othery == y):
                                        if (otherthing in self.all_techlabs + self.all_pfoc):
                                            hastechlab = 'y'
                                        elif otherthing in self.all_reactors:
                                            hasreactor = 'y'
                                            slots = 2
                                minfinish = 99999
                                slotsused = 0
                                for (thi, ata, goal, sg, start, finish) in current_growing | current_training:
                                    if (goal == cradle_place) and (ata == beautiful_cradle):
                                        minfinish = min(finish,minfinish)
                                        slotsused += 1
                                if slotsused < slots:
                                    minfinish = current_moment
                                if minfinish < 99999:
                                    maxfinish = max(minfinish,maxfinish)
                                cradle_dura = maxfinish - current_moment
                                if (needstechlab == '?') or (needstechlab == hastechlab):
                                    if (needsreactor == '?') or (needsreactor == hasreactor):
                                        exception = ((beautiful_thing,cradle_place) in self.unthinkable)
                                        if not exception:
                                            cradles.add((cradle_place,cradle_dura))
                        # check
                        if len(cradles) == 0:
                            self.log_success('Skipping, I have nowhere to build a '+beautiful_thing.name)
                            # maybe some other routine already built the starporttechlab
                            tocalculate = False
                            plan_moment = -1
                            toskip.add((beautiful_thing,beautiful_place))
                        # get earliest
                        bestdura = 99999
                        bestplace = self.nowhere
                        for (place,dura) in cradles:
                            if dura < bestdura:
                                bestdura = dura
                                bestplace = place
                        beautiful_place = bestplace
                if tocalculate:
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
                                could_arrive_quality = could_arrive + 0.20*walk_dura
                            else:
                                could_arrive_quality = could_arrive + 0.16*walk_dura
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
                    # cradle could be in use
                    slots = 1
                    for (thing,x,y) in current_buildings_and_parts:
                        if thing in self.all_reactors:
                            if (x == beautiful_place.x) and (y == beautiful_place.y):
                                slots = 2
                    minfinish = 99999
                    slotsused = 0
                    for (thi, ata, goal, sg, start, finish) in current_growing | current_training:
                        if (goal == beautiful_place) and (ata == beautiful_cradle):
                            minfinish = min(finish,minfinish)
                            slotsused += 1
                    if slotsused < slots:
                        minfinish = current_moment
                    if minfinish < 99999:
                        maxfinish = max(minfinish,maxfinish)
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
        # toskip
        for (thing,place) in toskip:
            self.log_success('I have to skip a '+thing.name)
            self.remove_from_planning_etc(thing,place)



#*********************************************************************************************************************

    async def gamestate1(self):
        # things to do before tile and expo
        #
        # enemy_real_structures
        # enemy_structures without the snapshots
        self.enemy_real_structures = set()
        for ene in self.enemy_structures:
            if not ene.is_snapshot:
                self.enemy_real_structures.add(ene)
        #
        # enemy_structureinfo
        itchanged = False
        todel = set()
        todelplus = set()
        for ene in self.enemy_real_structures:
            goodtp = (ene.type_id,ene.position)
            if goodtp not in self.enemy_structureinfo:
                itchanged = True
                # delete outdated info
                for tp in self.enemy_structureinfo:
                    (typ,pos) = tp
                    if self.near(pos,ene.position,1.0):
                        todel.add(tp)
                # add new info
                self.enemy_structureinfo.add(goodtp)
                # plus finishframe
                if ene.build_progress == 1:
                    finishframe = self.frame
                else:
                    if ene.type_id in self.builddura_of_thing:
                        dura = self.builddura_of_thing[ene.type_id]
                    else:
                        dura = 50
                    finishframe = self.frame + (1 - ene.build_progress) * dura * self.frames_per_second
                tpplus = (ene.type_id,ene.position,finishframe)
                self.enemy_structureinfo_plus.add(tpplus)
        if itchanged:
            # delete from tpplus
            if len(todel) > 0:
                for tpplus in self.enemy_structureinfo_plus:
                    (typ, pos, finishframe) = tpplus
                    if (typ, pos) in todel:
                        todelplus.add(tpplus)
            self.enemy_structureinfo -= todel
            self.enemy_structureinfo_plus -= todelplus
            self.init_undetect()
        #  
        # All idle structures and units. Idle for at least 10 frames.
        self.idles = set()
        for one in self.structures | self.units:
            if one.tag not in self.idles_start:
                self.idles_start[one.tag] = 999999
            if len(one.orders) == 0:
                if self.frame >= self.idles_start[one.tag] + 10:
                    self.idles.add(one.tag)
                elif self.idles_start[one.tag] == 999999:
                    self.idles_start[one.tag] = self.frame
            else:
                self.idles_start[one.tag] = 999999
        #
        # All ready structures. Ready for at least 20 frames.
        self.readies = set()
        for one in self.structures:
            if one.tag not in self.readies_start:
                self.readies_start[one.tag] = 999999
            if one in self.structures.ready:
                if self.frame >= self.readies_start[one.tag] + 20:
                    self.readies.add(one.tag)
                elif self.readies_start[one.tag] == 999999:
                    self.readies_start[one.tag] = self.frame
            else:
                self.readies_start[one.tag] = 999999
            # readies_delayed
            for tag in self.readies_delayed:
                tilframe = self.readies_delayed[tag]
                if self.frame < tilframe:
                    if tag in self.readies:
                        self.readies.remove(tag)
            # administration
            if self.frame % 43 == 42:
                todel = set()
                for tag in self.readies_delayed:
                    tilframe = self.readies_delayed[tag]
                    if self.frame >= tilframe:
                        todel.add(tag)
                for tag in todel:
                    del self.readies_delayed[tag]


    def post_idles(self):
        # when self.idles.remove(tag) has been done, update idles_start
        for tag in self.idles_start:
            if self.frame >= self.idles_start[tag] + 10: # has been put in idles
                if tag not in self.idles:
                    self.idles_start[tag] = 999999

    async def gamestate2(self):
        #
        #
        #   All existing not-flying ready commandcenters and orbitalcommands and all planetary fortresses
        #       pf and oc morphing from cc are included
        #       (the pluscharacter appends lists)
        self.all_bases = []
        for cc in self.structures(COMMANDCENTER)+self.structures(ORBITALCOMMAND)+self.structures(PLANETARYFORTRESS):
            if cc.tag in self.readies:
                if cc.tag != self.cheese3_cc_tag: # exclude a cc for pf-rush
                    self.all_bases.append(cc)
        # ccs in construction nearly finished are included
        for cc in self.structures(COMMANDCENTER):
            if cc.build_progress > 0.85:
                if cc not in self.all_bases:
                    if not self.proxy(cc.position):
                        self.all_bases.append(cc)
        #
        self.all_mine_bases = []
        for cc in self.structures(COMMANDCENTER)+self.structures(ORBITALCOMMAND)+self.structures(PLANETARYFORTRESS):
            if cc.tag in self.readies:
                if cc.tag != self.cheese3_cc_tag: # exclude a cc for pf-rush
                    if cc.position in self.expansion_locations:
                        self.all_mine_bases.append(cc)
        #   ccs in construction nearly finished are included
        for cc in self.structures(COMMANDCENTER):
            if cc.build_progress > 0.85:
                if not self.proxy(cc.position):
                    if cc.position in self.expansion_locations:
                        if cc not in self.all_mine_bases:
                            self.all_mine_bases.append(cc)
        # purpose
        for cc in self.structures(COMMANDCENTER)+self.structures(ORBITALCOMMAND)+self.structures(PLANETARYFORTRESS):
            if cc.tag not in self.purpose:
                self.purpose[cc.tag] = 'scv'
        #
        self.all_scvtags = {scv.tag for scv in self.units(SCV)}
        self.all_mine_basetags = {cc.tag for cc in self.all_mine_bases}
        self.all_structuretags = {struc.tag for struc in self.structures}
        self.all_unittags = {mar.tag for mar in self.units}
        for carriertype in [MEDIVAC,BUNKER,COMMANDCENTER,PLANETARYFORTRESS]:
            for car in self.units(carriertype):
                for pas in car.passengers:
                    self.all_unittags.add(pas.tag)
        self.all_bunkertags = {bun.tag for bun in self.structures(BUNKER)}
        self.init_all_minerals()
        self.init_all_vespene()
        #
        #   in the jump lost battlecruisers increase bc_fear
        #       uses old emotion_of_unittag info!
        living = 0
        for bc in self.units(BATTLECRUISER):
            if (bc.tag in self.emotion_of_unittag):
                if self.emotion_of_unittag[bc.tag] == 'bcrecovering':
                    living += 1
        past = 0
        for bct in self.emotion_of_unittag:
            if self.emotion_of_unittag[bct] == 'bcrecovering':
                past += 1
        if past > living:
            self.bc_fear = min(500,self.bc_fear+40)
        #
        # emotion_of_unittags is used for many units, even for units that are passengers.
        new_emotion_of_unittag = {}
        for tag in self.emotion_of_unittag:
            if tag in self.all_unittags:
                new_emotion_of_unittag[tag] = self.emotion_of_unittag[tag]
        # for battlecruisers, emotion_of_unittag contains tags of all living; unhealthy if repairing
        for bc in self.units(BATTLECRUISER):
            if (bc.tag in new_emotion_of_unittag):
                if (new_emotion_of_unittag[bc.tag] == 'bcrecovering'):
                    if (bc.health == self.maxhealth[bc.type_id]):
                        new_emotion_of_unittag[bc.tag] = 'lazy'
            else:
                new_emotion_of_unittag[bc.tag] = 'lazy'
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
        #   ambition_of_strt contains tags of living commandcenters, barracks etc. May be not ready.
        new_ambition_of_strt = {}
        for cc in self.structures:
            if cc.tag in self.ambition_of_strt:
                new_ambition_of_strt[cc.tag] = self.ambition_of_strt[cc.tag]
        self.ambition_of_strt = new_ambition_of_strt
        #
        #   gym contains tags of living commandcenters, barracks etc. May be not ready.
        new_gym = []
        for (strtype,strtag,trainee,owner) in self.gym:
            for stru in self.structures(strtype):
                if stru.tag == strtag:
                    new_gym.append((strtype,strtag,trainee,owner))
        self.gym = new_gym
        # owner_of_ambistrt may have outdated info
        #
        #   Count battlecruisers
        self.lastcruisercount = self.cruisercount
        self.cruisercount = self.units(BATTLECRUISER).amount
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
                    if scvt not in self.structure_of_trabu_scvt:
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
        self.all_gas_to_mine = set()
        for ref in self.structures(REFINERY)+self.structures(REFINERYRICH):
            if ref.tag in self.readies:
                gaspos = ref.position
                gast = self.postag(gaspos)
                gas = (gaspos,gast)
                for tow in self.all_mine_bases:
                    expo = self.expo_of_pos(tow.position)
                    if self.ground_strength_of_expo[expo] >= 0:
                        if self.near(gaspos, tow.position, self.miner_bound):
                            if ref.vespene_contents > 0:
                                self.all_gas_to_mine.add(gas)
        #   The tag of existing minerals where we want to mine from, in this frame
        self.all_mim_to_mine = set()
        for tow in self.all_mine_bases:
            expo = self.expo_of_pos(tow.position)
            if self.ground_strength_of_expo[expo] >= 0:
                for mim in self.minerals_of_expo[expo]:
                    self.all_mim_to_mine.add(mim)
        #   job_of_scvt contains the tag of all living scvs
        new_job_of_scvt = {}
        for scvt in self.all_scvt:
            if scvt in self.job_of_scvt:
                new_job_of_scvt[scvt] = self.job_of_scvt[scvt]
            elif scvt == self.cheese1_scv_tag:
                new_job_of_scvt[scvt] = 'cheeser'
                self.log_workers('cheeser came out of bunker'+self.name(scvt))
            else:
                new_job_of_scvt[scvt] = 'idler'
                self.log_workers('had no job, now is idler '+self.name(scvt))
        self.job_of_scvt = new_job_of_scvt
        #   count_of_job
        self.fix_count_of_job()
        self.log_population()
        #   restrict mim_of_minert to existing worker and mineral
        new_mim_of_minert = {}
        for scvt in self.mim_of_minert:
            if scvt in self.all_scvt:
                mim = self.mim_of_minert[scvt]
                if mim in self.all_mim_to_mine:
                    new_mim_of_minert[scvt] = mim
        for scvt in set(self.mim_of_minert) - set(new_mim_of_minert):
            self.log_workers('from mim_of_minert gone is mim_of_'+str(scvt))
        self.mim_of_minert = new_mim_of_minert
        self.fix_nminers_of_mimt()
        #   restrict gas_of_minert to existing worker and mineral
        new_gas_of_minert = {}
        for scvt in self.gas_of_minert:
            if scvt in self.all_scvt:
                gas = self.gas_of_minert[scvt]
                if gas in self.all_gas_to_mine:
                    new_gas_of_minert[scvt] = gas
        for scvt in set(self.gas_of_minert) - set(new_gas_of_minert):
            self.log_workers('from gas_of_minert gone is gast_of_'+str(scvt))
        self.gas_of_minert = new_gas_of_minert
        self.fix_nminers_of_gast()
        #   check consistency
        for scvt in self.mim_of_minert:
            job = self.job_of_scvt[scvt]
            name = self.name(scvt)
            if (job != 'mimminer'):
                self.log_success('not a mimminer, yet in mim_of_minert '+job+' '+name)
        for scvt in self.gas_of_minert:
            job = self.job_of_scvt[scvt]
            name = self.name(scvt)
            if (job != 'gasminer'):
                self.log_success('not a gasminer, yet in gas_of_minert ' + job + ' ' + name)
        for scv in self.units(SCV):
            if scv.tag in self.all_scvt:
                job = self.job_of_scvt[scv.tag]
                name = self.name(scv.tag)
                if scv.is_collecting:
                    if (job not in ['mimminer','carrier','gasminer','builder','volunteer','cheeser','traveller']):
                        self.log_success('collecting but wrong job ' + job + ' ' + name)
                else: # not collecting
                    if (job in ['gasminer','volunteer']):
                        self.log_success('not collecting but job ' + job + ' ' + name)
        # vision_of_scvt contains the tag of living applicants/candidates/carriers and existing bases
        new_vision_of_scvt = {}
        for scvt in self.all_scvt:
            if self.job_of_scvt[scvt] in {'applicant','candidate','carrier'}:
                cct = self.vision_of_scvt[scvt]
                if cct in self.all_mine_basetags:
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
        #   arrivals are only for travellers
        new_arrivals = set()
        for sgbsf in self.arrivals:
            (scvt, agoal, abuilding, sframe, aframe) = sgbsf
            if scvt in self.job_of_scvt:
                if self.job_of_scvt[scvt] == 'traveller':
                    new_arrivals.add(sgbsf)
        self.arrivals = new_arrivals
        # goal_of_flying_struct, structure exists
        new_goal_of_flying_struct = {}
        for structag in self.goal_of_flying_struct:
            goal = self.goal_of_flying_struct[structag]
            if structag in self.all_structuretags:
                new_goal_of_flying_struct[structag] = goal
        self.goal_of_flying_struct = new_goal_of_flying_struct
        # subgoal_of_flying_struct, structure exists
        new_subgoal_of_flying_struct = {}
        for structag in self.subgoal_of_flying_struct:
            subgoal = self.subgoal_of_flying_struct[structag]
            if structag in self.all_structuretags:
                new_subgoal_of_flying_struct[structag] = subgoal
        self.subgoal_of_flying_struct = new_subgoal_of_flying_struct
        # owner_of_trabu_scvt may have outdated info
        #
        # check for ready finished buildings
        todel = set()
        for scvt in self.structure_of_trabu_scvt:
            if self.job_of_scvt[scvt] == 'builder':
                struc = self.structure_of_trabu_scvt[scvt]
                goal = self.goal_of_trabu_scvt[scvt]
                for st in self.structures(struc):
                    if st.tag in self.readies:
                        if self.position_of_building(st) == goal:
                            todel.add(scvt)
        # The scv will become idler.
        for scvt in todel:
            del self.structure_of_trabu_scvt[scvt]
            del self.goal_of_trabu_scvt[scvt]
            for scv in self.units(SCV):
                if scv.tag == scvt:
                    self.promote(scv,'idler')
        #
        # scout2 died
        if self.scout2_tag != self.notag:
            if self.scout2_tag not in self.all_scvt:
                self.scout2_tag = self.notag
                self.scout2_direction = len(self.scout2_pos) - self.scout2_direction
        # army_supply
        self.army_supply = 0
        for marty in self.all_army: # birds
            self.army_supply = self.army_supply + self.supply_of_army[marty] * len(self.units(marty))
        for (marty,bartype,pos,dura) in self.eggs:
            if (marty in self.all_army):
                self.army_supply += self.supply_of_army[marty]
        for (marty,bartype,pos,dura,owner) in self.preps:
            if (marty in self.all_army):
                self.army_supply += self.supply_of_army[marty]
        for (marty, pos, owner) in self.thoughts:
            if (marty in self.all_army):
                self.army_supply += self.supply_of_army[marty]
        for (marty, pos, owner) in self.dreams:
            if (marty in self.all_army):
                self.army_supply += self.supply_of_army[marty]
        #
        # for every supply, a good mix of things:
        self.enoughworkers = max(10, 90 - self.minerals / 100)
        self.good_worker_supply = round(min(self.supply_used / 3 + 10, self.enoughworkers))
        if self.reached_max_supply_once:
            self.good_worker_supply = len(self.units(SCV))
        self.good_army_supply = round(self.supply_used - self.good_worker_supply)
        self.good_bases = round(1 + self.supply_used / 30)
        self.good_armybuildings = round(6 + self.supply_used / 6)
        self.good_upgradebuildings = round((self.supply_used - 10) / 50)
        self.good_upgrades = round((self.supply_used - 20) / 20)
        #
        armybuildings = self.we_started_amount(BARRACKS)
        armybuildings += 3 * self.we_started_amount(FACTORY)
        armybuildings += 5 * self.we_started_amount(STARPORT)
        upgradebuildings = self.we_started_amount(ARMORY)
        upgradebuildings += self.we_started_amount(ENGINEERINGBAY)
        upgradebuildings += self.we_started_amount(GHOSTACADEMY)
        upgradebuildings += self.we_started_amount(FUSIONCORE)
        ccs = self.we_started_amount(COMMANDCENTER)
        ccs += self.structures(ORBITALCOMMAND).amount + self.structures(PLANETARYFORTRESS).amount
        upgrades = 0
        for upg in self.all_upgrades:
            if self.we_started_a(upg):
                upgrades += 1  
        #
        self.good_plans = set()
        # supply-based
        if ccs < self.good_bases:
            self.good_plans.add('base')
        if (upgradebuildings < self.good_upgradebuildings):
            self.good_plans.add('upgradebuilding')
        if upgrades < self.good_upgrades:
            self.good_plans.add('upgrade')
        if self.supply_used < 200:
            if self.army_supply < self.good_army_supply:
                self.good_plans.add('army')
            if armybuildings < self.good_armybuildings:
                self.good_plans.add('armybuilding')
            # ambition
            if len(self.good_plans) == 0:
                self.good_plans.add('army')
        else: # max supply
            self.good_plans.add('base')
            self.good_plans.add('upgradebuilding')
            self.good_plans.add('upgrade')
        # moneysurplus-based
        if (self.minerals > 1200) and (self.vespene > 600):
            self.good_plans.add('base')
            self.good_plans.add('upgradebuilding')
            self.good_plans.add('army')
            self.good_plans.add('armybuilding')
            self.good_plans.add('upgrade')
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
        #
        # amount usable of barracks (at least half-built), minus count of marines etc in throwspots
        # used to cut ideas in throw_anywhere
        for kind in {BARRACKS,FACTORY,STARPORT,ARMORY,ENGINEERINGBAY}:
            self.amount_usable[kind] = 0
            for bar in self.structures(kind):
                if bar.tag in self.readies:
                    self.amount_usable[kind] += 1
                    if self.has_finished_reactor(bar.position):
                        self.amount_usable[kind] += 1
            for (marty,bartype,pos,dura) in self.eggs:
                if (marty == kind) and (dura < 12):
                    self.amount_usable[kind] += 1
            for (thing, pos, status, owner) in self.throwspots:
                if self.cradle_of_thing(thing) == kind:
                    self.amount_usable[kind] -= 1
            for (marty,bartype,pos,dura) in self.eggs:
                if (bartype == kind) and (dura >= 12):
                    self.amount_usable[kind] -= 1
        # amount_usable_teched
        for kind in {BARRACKS,FACTORY,STARPORT}:
            spots = set()
            self.amount_usable_teched[kind] = 0
            for bar in self.structures(kind):
                if bar.tag in self.readies:
                    if bar.has_techlab:
                        self.amount_usable_teched[kind] += 1
                        spots.add(bar.position)
            for (marty,bartype,pos,dura) in self.eggs:
                if (bartype == kind) and (marty in self.all_techlabs) and (dura < 12):
                    self.amount_usable_teched[kind] += 1
            for (thing, pos, status, owner) in self.throwspots:
                if self.cradle_of_thing(thing) == kind:
                    if pos in spots:
                        self.amount_usable_teched[kind] -= 1
            for (marty,bartype,pos,dura) in self.eggs:
                if (bartype == kind) and (dura >= 12):
                    if pos in spots:
                        self.amount_usable[kind] -= 1



    #*********************************************************************************************************************

    def build_minima(self):
        # advice on stuck amount=0 situations
        ccs = self.we_started_amount(COMMANDCENTER) + self.structures(PLANETARYFORTRESS).amount \
              + self.structures(ORBITALCOMMAND).amount
        bcs = self.we_started_amount(BATTLECRUISER)
        if self.allow_throw(COMMANDCENTER):
            if (ccs == 0):
                self.throw_anywhere(COMMANDCENTER,'build_minima')
        if self.allow_throw(SUPPLYDEPOT):
            if (not self.we_started_a(SUPPLYDEPOT)):
                self.throw_anywhere(SUPPLYDEPOT,'build_minima')
        if self.allow_throw(BARRACKS):
            if (not self.we_started_a(BARRACKS)):
                self.throw_anywhere(BARRACKS,'build_minima')
        if self.allow_throw(REFINERY):
            if (not self.we_started_a(REFINERY)):
                if self.workerrushstate != 'busy': # exception
                    if self.opening_name.find('marine-1') < 0: # exception
                        self.throw_anywhere(REFINERY,'build_minima')
        if self.allow_throw(ENGINEERINGBAY):
            if (not self.we_started_a(ENGINEERINGBAY)) and (ccs >= 2):
                self.throw_anywhere(ENGINEERINGBAY,'build_minima')
        if self.allow_throw(FACTORY):
            if (not self.we_started_a(FACTORY)) and (ccs >= 2):
                self.throw_anywhere(FACTORY,'build_minima')
        if self.allow_throw(MISSILETURRET):
            if (not self.we_started_a(MISSILETURRET)) and (ccs >= 2):
                self.throw_anywhere(MISSILETURRET, 'build_minima')
        if self.allow_throw(STARPORT):
            if (not self.we_started_a(STARPORT)) and (ccs >= 2):
                self.throw_anywhere(STARPORT,'build_minima')
        if self.allow_throw(FUSIONCORE):
            if (not self.we_started_a(FUSIONCORE)) and (ccs >= 2):
                self.throw_anywhere(FUSIONCORE,'build_minima')
        if self.allow_throw(ARMORY):
            if (not self.we_started_a(ARMORY)) and (ccs >= 4):
                self.throw_anywhere(ARMORY,'build_minima')
        if self.allow_throw(RAVEN):
            if (not self.we_started_a(RAVEN)) and (bcs >= 2):
                self.throw_anywhere(RAVEN,'build_minima')
        if self.allow_throw(BARRACKSTECHLAB):
            if (not self.we_started_a(BARRACKSTECHLAB)):
                self.throw_anywhere(BARRACKSTECHLAB,'build_minima')
        if self.allow_throw(FACTORYTECHLAB):
            if (not self.we_started_a(FACTORYTECHLAB)):
                self.throw_anywhere(FACTORYTECHLAB,'build_minima')
        if self.allow_throw(STARPORTTECHLAB):
            if (not self.we_started_a(STARPORTTECHLAB)):
                self.throw_anywhere(STARPORTTECHLAB,'build_minima')


    def lategame(self):
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
        for sp in self.structures(FACTORY):
            if sp.tag in self.readies:
                if not sp.has_add_on:
                    self.blunt_to_bagofthings(FACTORYTECHLAB)
        for sp in self.structures(STARPORT):
            if sp.tag in self.readies:
                if not sp.has_add_on:
                    self.blunt_to_bagofthings(STARPORTTECHLAB)
        # army
        if ('army' in self.good_plans):
            factoriesready = False
            for fa in self.structures(FACTORY):
                if fa.tag in self.readies:
                    if fa.tag in self.idles:
                        factoriesready = True
            if core:
                starportsready = False
                for sp in self.structures(STARPORT):
                    if sp.tag in self.readies:
                        if sp.tag in self.idles:
                            starportsready = True
                if starportsready:
                    self.blunt_to_bagofthings(BATTLECRUISER)
                else:
                    self.blunt_to_bagofthings(STARPORT)
            elif factoriesready:
                self.blunt_to_bagofthings(SIEGETANK)
            else:
                self.blunt_to_bagofthings(MARINE)
            if (wms < 5) and (ccs > 1) and (factoriesready):
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
        for kind in self.enemy_count:
            if (kind in self.viking_targets):
                vikings += 1.2 * self.enemy_count[kind]
        vikings -= self.we_started_amount(VIKINGFIGHTER)
        while vikings > 0:
            self.blunt_to_bagofthings(VIKINGFIGHTER)
            vikings -= 1
        # log
        stri = 'lategame added bagofthings: '
        for th in self.bagofthings:
            stri = stri + th.name + ' '
        self.log_success(stri)


    def midgame(self,thing,amount):
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
    #        consider preps and eggs to be completed, do not accept unordered thoughts
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
            # When the oc is in eggs, in birds that cc is ...
            if thing in self.all_pfoc:
                self.transformable[COMMANDCENTER] += 1
        for (thing,scv,pos,dura,owner) in self.preps:
            self.hoopy_add(thing)


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
        self.bui_min_lab = {}
        self.bui_of_pos = {}
        self.happy_made = set()
        for (thing,pos) in self.birds:
            self.happy_add(thing,pos)
            if thing in self.all_pfoc: # a cc is hidden under each pfoc
                self.bui_min_lab[pos] = 0
        for (thing,bartype,pos,dura) in self.eggs:
            self.happy_add(thing, pos)
        for (thing,scv,pos,dura,owner) in self.preps:
            self.happy_add(thing, pos)

    def happy_buildorder(self) -> bool:
        # DEMANDS done is self.happy_get_sit()
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
        have = self.we_started_amount(thing)
        for th in self.bagofthings:
            if th == thing:
                have += 1
        if have < 1:
            self.bagofthings.append(thing)

    def blunt_to_bagofthings(self,thing):
        have = self.we_started_amount(thing)
        for th in self.bagofthings:
            if th == thing:
                have += 1
        if have < self.maxam_of_thing(thing):
            self.bagofthings.append(thing)

    def buildseries_of_bagofthings(self):
        self.delete_all_thrown_thoughts_and_dreams() # this should make the checks easier, and should be remade automatic.
        self.bagofcradle_of_bagofthings()
        self.bagofcradle_exe = self.bagofcradle.copy()
        self.bagoftree_of_bagofcradle()
        self.bagoftree_exe = self.bagoftree.copy()
        self.buildseries_of_bagoftree()

    def make_planning_exe(self):
        # first make buildseries
        if ((len(self.buildorder_exe) == 0)) and ((self.opening_create_units <= 0) or (self.game_phase != 'opening')):
            # phase
            if self.game_phase == 'init':
                self.game_phase = 'opening'
                #await self._client.chat_send('opening', team_only=False)
                self.log_success('============================================================ opening =========')
                self.log_buildseries('game_phase')
            elif self.game_phase == 'opening':
                self.game_phase = 'midgame'
                #await self._client.chat_send('midgame', team_only=False)
                self.log_buildseries('game_phase')
                self.log_success('============================================================ midgame ======')
            elif self.game_phase == 'midgame':
                self.game_phase = 'lategame'
                #await self._client.chat_send('lategame', team_only=False)
                self.log_buildseries('game_phase')
                self.log_success('============================================================ lategame =======')
            elif self.game_phase == 'lategame':
                self.game_phase = 'endgame'
                #await self._client.chat_send('endgame', team_only=False)
                self.log_buildseries('game_phase')
                self.log_success('============================================================ endgame =======')
            # make optimized buildseries
            if (self.game_phase == 'opening'):
                self.buildseries = self.buildseries_opening
                self.buildseries_old = self.buildseries_opening
                # make the simpler bags
                self.bagofthings = []
                for infa_th in self.buildseries:
                    th = self.basekind_of(infa_th)
                    self.bagofthings.append(th)
                self.bagofcradle_of_bagofthings()
                self.bagoftree_of_bagofcradle()
            elif (self.game_phase == 'midgame'):
                self.bagofthings = []
                for thing in self.midgame_things:
                    self.blunt_to_bagofthings(thing)
                self.shrink_bagofthings_have()
                # bagofthings is made. Build up from here.
                self.buildseries_of_bagofthings()
            elif (self.game_phase == 'lategame'):
                self.bagofthings = []
                self.lategame()
                self.buildseries_of_bagofthings()
            elif (self.game_phase == 'endgame'):
                # make only thrown things, not ordered things
                self.bagofthings = []
                self.buildseries_of_bagofthings()
            # buildseries is made
            # Keep old places for reuse.
            for (th,po,status) in self.buildorder_exe:
                if not self.proxy(po):
                    if po != self.somewhere:
                        self.chosenplaces.append((th,po))
            self.buildorder_of_buildseries()
            # make _exe variants
            self.bagofthings_exe = self.bagofthings.copy()
            self.bagoftree_exe = self.bagoftree.copy()
            self.bagofcradle_exe = self.bagofcradle.copy()
            self.buildseries_exe = self.buildseries.copy()
            for (th,po,status) in self.buildorder_exe:
                if status == 'dream':
                    del self.dreams[self.dreams.index((th,po,'follow_planning_exe'))]
            self.buildorder_exe = []
            for (th,pl) in self.buildorder:
                self.buildorder_exe.append((th,pl,'dream'))
                self.dreams.append((th,pl,'follow_planning_exe'))
        # buildorder_exe is made
        # cut off a productionline at the loss of a structure
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
            for thing in self.bagofthings_exe:
                self.log_success('I will remember to make a '+thing.name)
            # Keep old places for reuse.
            for (th, pos, status) in self.buildorder_exe:
                if not self.proxy(pos):
                    if pos != self.somewhere:
                        self.log_success('I will remember to put a '+th.name+' at '+self.txt(pos))
                        self.chosenplaces.append((th, pos))
            # empty the store beyond self.bagofthings_exe and before eggs
            self.bagoftree_exe = []
            self.bagofcradle_exe = []
            self.buildseries_exe = []
            self.buildorder_exe = []
            self.planning = []
            self.throwspots = []
            self.thoughts = []
            self.dreams = []
            self.ambition_of_strt = {}
            self.gym = []
            self.owner_of_ambistrt = {}
            for scv in self.units(SCV):
                scvt = scv.tag
                if self.job_of_scvt[scvt] not in ['mimminer','gasminer','builder']:
                    self.promote(scv,'idler')
                    scv.move(scv.position.towards(self.loved_pos,1))
                    if scvt in self.goal_of_trabu_scvt:
                        del self.goal_of_trabu_scvt[scvt]
                        del self.structure_of_trabu_scvt[scvt]
            self.vision_of_scvt = {}
            # this changes preps and eggs
            self.get_eggs()
            self.get_preps()  # after get_eggs
            # remake plans
            self.bagofthings = self.bagofthings_exe.copy()
            self.buildseries_of_bagofthings()
            self.buildorder_of_buildseries()
            self.buildorder_exe = []
            for (th, pl) in self.buildorder:
                self.buildorder_exe.append((th, pl, 'dream'))
                self.dreams.append((th,pl,'follow_planning_exe'))
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

    def idiot(self):
        # build something when minerals explode
        if self.minerals >= 1000:
            wanted = {}
            todo = 1
            minimum_minerals = 1000
            todel = set()
            for (thing,finishframe) in self.idiot_busy:
                if self.frame < finishframe:
                    cost = self.get_added_cost(thing)
                    minimum_minerals += cost.minerals
                    if thing in wanted:
                        wanted[thing] -= 1
                    else:
                        wanted[thing] = -1
                else:
                    todel.add((thing,finishframe))
            self.idiot_busy -= todel
            if self.minerals >= minimum_minerals:
                for thing in self.idiot_plan:
                    if todo > 0:
                        if thing in wanted:
                            wanted[thing] += 1
                        else:
                            wanted[thing] = 1
                        amount = wanted[thing]
                        if self.we_preppedetc_amount(thing) < amount:
                            if self.can_pay(thing):
                                if self.check_techtree(thing):
                                    if self.check_supply(thing):
                                        if self.check_cradleidle(thing):
                                            self.oknowbuildthething(thing)
                                            todo -= 1

    def oknowbuildthething(self,thing):
        if thing == SCV:
            for cradle_type in {COMMANDCENTER, ORBITALCOMMAND, PLANETARYFORTRESS}:
                for dock in self.structures(cradle_type):
                    if dock.tag in self.readies:
                        if dock.tag in self.idles:
                            self.idiot_busy.add((thing, self.frame + 100))
                            dock.train(SCV)
                            self.bought(SCV)
        elif thing == COMMANDCENTER:
            place = random.choice(self.expansion_locations)
            if self.check_layout(thing,place):
                self.write_layout(thing,place)
                self.idiot_busy.add((thing, self.frame + 500))
                scvt = self.get_near_scvt_to_goodjob(place)
                self.thoughts.append((thing, place, 'idiot'))
                self.build_thing_tobuildwalk(scvt,thing,place,'idiot')
        elif thing == REFINERY:
            # closest empty geyser, and close geysers
            geysers = set()
            minsd = 99999
            closest = self.nowhere
            for cradle_type in {COMMANDCENTER, ORBITALCOMMAND, PLANETARYFORTRESS}:
                for dock in self.structures(cradle_type):
                    for gey in self.vespene_geyser:
                        if self.near(dock.position,gey.position,10):
                            geysers.add(gey.position)
                        sd = self.sdist(dock.position,gey.position)
                        if sd < minsd:
                            closest = gey.position
                            minsd = sd
            geysers.add(closest)
            place = random.choice(tuple(geysers))
            if self.check_layout(thing,place):
                self.write_layout(thing,place)
                self.idiot_busy.add((thing, self.frame + 500))
                scvt = self.get_near_scvt_to_goodjob(place)
                self.thoughts.append((thing, place, 'idiot'))
                self.build_thing_tobuildwalk(scvt, thing, place, 'idiot')
        elif thing in self.all_structures_tobuildwalk:
            place = self.random_mappoint()
            while self.proxy(place):
                place = self.random_mappoint()
            place = self.place_around(thing,place)
            if self.check_layout(thing,place):
                self.write_layout(thing,place)
                self.idiot_busy.add((thing, self.frame + 500))
                scvt = self.get_near_scvt_to_goodjob(place)
                self.thoughts.append((thing, place, 'idiot'))
                self.build_thing_tobuildwalk(scvt,thing,place,'idiot')
        else:
            self.idiot_busy.add((thing, self.frame + 100))
            self.thoughts.append((thing, self.somewhere, 'idiot'))
            self.build_thing(thing,self.somewhere,'idiot')
                        
    
    def remove_from_planning_etc(self, thing, place):
        # from planning_exe the first one
        todel = set()
        first = True
        for bp in self.planning_exe:
            (th, sv, pl, sr, sc, fi) = bp
            if first and (th == thing) and (pl == place):
                todel.add(bp)
                first = False
        for bp in todel:
            del self.planning_exe[self.planning_exe.index(bp)]
        # from buildorder_exe the first one
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
        if self.proxy(place):
            if thing == BUNKER:
                infa_thing = INFESTEDBUNKER
            elif thing == FACTORY:
                infa_thing = INFESTEDFACTORY
            elif thing == BARRACKS:
                infa_thing = INFESTEDBARRACKS
            elif thing == STARPORT:
                infa_thing = INFESTEDSTARPORT
        # from buildseries_exe and the bags
        if infa_thing in self.buildseries_exe:
            del self.buildseries_exe[self.buildseries_exe.index(infa_thing)]
        # no infested in the bags
        if thing in self.bagofcradle_exe:
            del self.bagofcradle_exe[self.bagofcradle_exe.index(thing)]
        if thing in self.bagoftree_exe:
            del self.bagoftree_exe[self.bagoftree_exe.index(thing)]
        if thing in self.bagofthings_exe:
            del self.bagofthings_exe[self.bagofthings_exe.index(thing)]
        # dreams thoughts
        if (thing,place,'follow_planning_exe') in self.dreams:
            del self.dreams[self.dreams.index((thing,place,'follow_planning_exe'))]
        if (thing,place,'follow_planning_exe') in self.thoughts:
            del self.thoughts[self.thoughts.index((thing,place,'follow_planning_exe'))]


    def implementing_buildorder_exe(self):
        # dream to thought
        for nr in range(0,len(self.buildorder_exe)):
            (thing,place,status) = self.buildorder_exe[nr]
            if status == 'dream':
                donow = True
                for (th, po, ow) in self.thoughts:
                    if (th == thing) and (place == po) and (ow != 'follow_planning_exe'):
                        donow = False
                        self.log_success('In thoughts ' + ow + ' already put a ' + thing.name + ' ' + self.txt(place))
                # delay walking to a buildingsite during workerrush
                if (self.workerrushstate == 'tobe'):
                    if self.opening_name.find('workerrush') >= 0:
                        donow = False
                        self.log_success('buildorder delay because of workerrush')
                elif (self.workerrushstate == 'busy'):
                    if (self.opening_name == 'immediate_fight'):
                        donow = False
                        self.log_success('buildorder delay because of workerrush')
                    elif (self.opening_name == 'workerrush-trans'):
                        pass
                    elif (self.opening_name == 'workerrush-late'):
                        if thing != SUPPLYDEPOT:
                            donow = False
                            self.log_success('buildorder delay because of workerrush')
                    elif self.opening_name.find('workerrush') >= 0:
                        donow = False
                        self.log_success('buildorder delay because of workerrush')
                # delay on low miners
                if self.count_of_job['mimminer'] < 5:
                    donow = False
                    self.log_success('buildorder delay because of too few mimminers')
                if donow:
                    if self.add_thought(thing, place, 'follow_planning_exe'):
                        self.buildorder_exe[nr] = (thing,place,'thought')
                        self.log_success('dream to thought ' + thing.name + ' at ' + self.txt(place))
                        del self.dreams[self.dreams.index((thing,place,'follow_planning_exe'))]
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
            self.log_success('I have done a '+thing.name)
            self.remove_from_planning_etc(thing,place)


    def follow_planning_exe(self):
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
        owner = 'follow_planning_exe'
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
                                    if self.build_thing_tobuildwalk(scvt,thing, place, owner):
                                        del self.thoughts[self.thoughts.index((thing, pl, owner))]
                                        self.buildorder_exe[nr] = (th,place,'prep')
                        elif thing in self.all_pfoc + self.all_labs:
                            if sr <= 0:
                                uses = 0
                                for abar in self.structures:
                                    if self.position_of_building(abar) == place:
                                        if abar.tag in (self.ambition_of_strt.keys()):
                                            uses = 99999
                                        for (strtype,strtag,trainee,ow) in self.gym:
                                            if abar.tag == strtag:
                                                uses += 1
                                if uses < 1:
                                    if self.build_thing(thing, place, owner):
                                        del self.thoughts[self.thoughts.index((thing, pl, owner))]
                                        self.buildorder_exe[nr] = (th, place, 'prep')
                        else: # upgr, army
                            if sr <= 0:
                                maxuses = 1
                                uses = 0
                                for abar in self.structures:
                                    if self.position_of_building(abar) == place:
                                        if self.has_finished_reactor(abar.position):
                                            maxuses = 2
                                        if abar.tag in (self.ambition_of_strt.keys()):
                                            uses = 99999
                                        for (strtype,strtag,trainee,ow) in self.gym:
                                            if abar.tag == strtag:
                                                uses += 1
                                if uses < maxuses:
                                    if self.build_thing(thing, place, owner):
                                        del self.thoughts[self.thoughts.index((thing, pl, owner))]
                                        self.buildorder_exe[nr] = (th, place, 'prep')

    def throw_history(self,th,po):
        # make unthinkable to throw a building more than 3 times at the same spot
        if th in self.all_structures_tobuildwalk:
            nr = 0
            for (hth,hpo,hnr) in self.throw_history_set:
                if (hth == th) and (hpo == po):
                    nr = hnr
            if nr > 0:
                self.throw_history_set.remove((th,po,nr))
            nr += 1
            self.throw_history_set.add((th,po,nr))
            if nr == 3:
                self.log_success('This is the third and the last time I build a '+th.name+' here!')
                self.make_unthinkable(th,po)

    def throw_at_spot(self, th, po, ow):
        # append to throwspots
        # respecting unique (th,po), respect unthinkable.
        # ignore to throw if the thing is in buildorder_exe
        # also write_layout
        self.log_throw(th.name)
        cradle = self.cradle_of_thing(th)
        sta = 'dream'
        approve = True
        # enough cradles?
        for kind in {BARRACKS,FACTORY,STARPORT,ARMORY,ENGINEERINGBAY}:
            if cradle == kind:
                if self.amount_usable[kind] <= 0:
                    approve = False
                    self.log_success('Thrown but not enough cradles for ' + th.name + ' by ' + ow)
        # enough cradles with techlab?
        needstechlab = False
        for (thi, need) in self.techtree:
            if thi == th:
                if (need in self.all_techlabs) and (need != cradle):
                   needstechlab = True
        if needstechlab:
            for kind in {BARRACKS,FACTORY,STARPORT}:
                if cradle == kind:
                    if self.amount_usable_teched[kind] <= 0:
                        approve = False
                        self.log_success('Thrown but not enough teched cradles for ' + th.name + ' by ' + ow)
        same = 0
        for (thing, pos, status, owner) in self.throwspots:
            if (thing == th) and (pos == po):
                same += 1
        if same > 0:
            maxsame = 1
            for (kind,place) in self.birds:
                if place == pos:
                    if kind in self.all_reactors:
                        maxsame = 2
            if same >= maxsame:
                approve = False
                self.log_success('Thrown but it was thrown already: ' + th.name + ' there by ' + ow)
        if (th,po) in self.unthinkable:
            approve = False
            self.log_success('Thrown but unthinkable: '+th.name+' there by ' + ow)
        for (exething, exeplace, status) in self.buildorder_exe:
            if exething == th:
                approve = False
                self.log_success('Thrown but in buildorder_exe: '+th.name + ' by ' + ow)
        if approve:
            self.throwspots.append((th, po, sta, ow))
            self.throw_history(th,po)
            if th in self.all_structures_tobuildwalk:
                self.write_layout(th, po)
            if th in self.all_army:
                self.army_supply += self.supply_of_army[th]
            self.dreams.append((th,po,ow))
            self.log_success('New dream: ' + th.name + ' at ' + self.txt(po))

    def make_unthinkable(self, thing,pos):
        # called only when there is no such pair in preps
        self.unthinkable.add((thing,pos))
        # remove from throwspots and chosenplaces too
        todel = []
        for tps in self.throwspots:
            (th, po, status, ow) = tps
            if (th == thing) and (po == pos):
                todel.append(tps)
                while (th, po, ow) in self.dreams:
                    del self.dreams[self.dreams.index((th,po,ow))]
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
        ok = True
        badpos = False
        badthing = False
        todel = set()
        if self.we_thoughtetc_at(thing,pos):
            if (thing in self.all_army) or (pos == self.somewhere):
                ok = True
            else:
                ok = False
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
                                (th_, po_, status_, ow_) = tps
                                if (th == th_) and (po == po_) and (ow == ow_) and (status_ == 'thought'):
                                    todel_.append(tps)
                            for tps in todel_:
                                del self.throwspots[self.throwspots.index(tps)]
        if self.we_thoughtetc_amount(thing) >= self.future_maxam_of_thing(thing):
            ok = False
            badthing = True
            self.log_success('Add_thought halted by future maximum a ' + thing.name + ' by ' + owner)
        # no restrictions on e.g. minerals, free cradle, as those can become ok later
        if not self.check_future_techtree(thing):
            ok = False
            self.log_success('Add_thought halted by future techtree a '+thing.name+' by '+owner)
        if thing == REFINERY:
            # This code forbids gas-stealing. Could have to change later.
            expa = self.nowhere
            for ccpos in self.expansion_locations:
                if self.near(pos,ccpos,self.miner_bound):
                    expa = ccpos
            if not self.we_started_hall_at(expa):
                ok = False
                self.log_success('Add_thought halted a hallless refinery by '+owner)
        if (thing,pos) in self.unthinkable:
            ok = False
            badpos = True
            self.log_success('Add_thought halted unthinkable ' + thing.name +' at ' + self.txt(pos) + ' by ' + owner)
        if ok:
            self.thoughts.append((thing,pos,owner))
            for tpo in todel:
                del self.thoughts[self.thoughts.index(tpo)]
        if badpos:
            # remove this from new throwspots, dreams and chosenplaces
            todel = []
            for tps in self.throwspots:
                (th, po, status, ow) = tps
                if (th == thing) and (po == pos) and (ow == owner) and (status == 'dream'):
                    todel.append(tps)
                    while (th,po,ow) in self.dreams:
                        del self.dreams[self.dreams.index((th,po,ow))]
            for tps in todel:
                del self.throwspots[self.throwspots.index(tps)]
            todel = []
            for tps in self.chosenplaces:
                (th, po) = tps
                if (th == thing) and (po == pos) and ('follow_planning_exe' == owner):
                    todel.append(tps)
            for tps in todel:
                del self.chosenplaces[self.chosenplaces.index(tps)]
        if badthing:
            # remove this from new throwspots, dreams and chosenplaces
            todel = []
            for tps in self.throwspots:
                (th, po, status, ow) = tps
                if (th == thing) and (status == 'dream'):
                    todel.append(tps)
            for tps in todel:
                del self.throwspots[self.throwspots.index(tps)]
            todel = []
            for tps in self.dreams:
                (th, po, ow) = tps
                if (th == thing):
                    todel.append(tps)
            for tps in todel:
                del self.dreams[self.dreams.index(tps)]
            todel = []
            for tps in self.chosenplaces:
                (th, po) = tps
                if (th == thing):
                    todel.append(tps)
            for tps in todel:
                del self.chosenplaces[self.chosenplaces.index(tps)]
        return ok

    def movetothefront(self, thing, owner):
        found = False
        found_tps = (None, None, None, None)
        for tps in self.throwspots:
            (th, po, status, ow) = tps
            if (th == thing) and (ow == owner):
                found = True
                found_tps = tps
        if found:
            del self.throwspots[self.throwspots.index(found_tps)]
            self.throwspots.insert(0,found_tps)

    def throw_treeno(self, thing, owner):
        if not self.we_started_a(thing):
            self.throw_tree(thing,owner)

    def throw_tree(self, thing, owner):
        # throw if   ok techtree   and   not in throwspots
        seenthrown = False
        for (th, pos, status, ow) in self.throwspots:
            if (th == thing):
                seenthrown = True
        if not seenthrown:
            if self.check_techtree(thing):
                self.throw_anywhere(thing, owner)
                self.movetothefront(thing,owner)

    def throw_anywhere(self, thing, owner):
        # if owner threw this thing already, and it is not yet egged, do nothing
        # find or reuse a place, store it in throwspots
        # also write_layout
        # if not found, do nothing
        self.log_throw(owner + ' throws somewhere a ' + thing.name)
        tisarepeat = False
        for (th,po,status, ow) in self.throwspots:
            if (th == thing) and (ow == owner):
                tisarepeat = True
        bar = self.cradle_of_thing(thing)
        if bar in {BARRACKS,FACTORY,STARPORT}: # repeat may be no problem
            tisarepeat = False
        if tisarepeat:
            self.log_success('Repeated throw_anywhere of a '+thing.name+' by '+owner)
        else:
            foundplace = False
            place = self.nowhere
            if thing in self.all_structures_tobuildwalk:
                if self.find_tobuildwalk_a_place(thing,'now'):
                    place = self.function_result_Point2
                    if (thing,place) not in self.unthinkable:
                        foundplace = True
            elif thing in self.all_pfoc:
                for cc in self.structures(COMMANDCENTER):
                    if cc.tag in self.readies:
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
                for aba in self.structures(bar):
                    if aba.tag in self.readies:
                        if aba.tag not in self.ambition_of_strt:
                            growing = False
                            for (martype,bartype,pos,dura) in self.eggs:
                                if (bartype == bar) and (pos == aba.position):
                                    if martype in self.all_labs:
                                        growing = True
                            if not growing:
                                if not aba.has_add_on:
                                    if not self.proxy(aba.position):
                                        if thing in self.all_techlabs:
                                            if (bar,aba.position) not in self.notechlab:
                                                sps.append(aba)
                                        else: # reactor
                                            sps.append(aba)
                if len(sps) > 0:
                    sp = random.choice(sps)
                    place = self.position_of_building(sp)
                    if (thing, place) not in self.unthinkable:
                        foundplace = True
            else: # army, upgr
                bar = self.cradle_of_thing(thing)
                havebar = True
                if bar in {BARRACKS, FACTORY, STARPORT,ARMORY,ENGINEERINGBAY}:
                    if self.amount_usable[bar] <= 0:
                        havebar = False
                        self.log_success('Thrown but not enough cradles for ' + thing.name + ' by ' + owner)
                if havebar:
                    needstechlab = False
                    for (thi, need) in self.techtree:
                        if thi == thing:
                            if (need in self.all_techlabs) and (need != bar):
                                needstechlab = True
                    if needstechlab:
                        sps = []
                        for sp in self.structures(bar):
                            if sp.tag in self.readies:
                                if sp.has_techlab:
                                    sps.append(sp)
                    else:
                        sps = []
                        for sp in self.structures(bar):
                            if sp.tag in self.readies:
                                sps.append(sp)
                    if len(sps) > 0:
                        sp = random.choice(sps)
                        example_place = self.position_of_building(sp)
                        if (thing, example_place) not in self.unthinkable:
                            foundplace = True
                            place = self.somewhere
            if foundplace:
                self.throw_at_spot(thing,place,owner)

    async def throw_advance(self):
        # push throwspots into thought
        nr = 0
        while nr < len(self.throwspots): # a throwspot can be deleted in the loop
            tps = self.throwspots[nr]
            (thing, place, status, ow) = tps
            if (status == 'dream'):
                if self.add_thought(thing, place, ow):
                    newtps = (thing, place, 'thought', ow)
                    self.log_success('dream to thought a thrown ' + thing.name + ' at ' + self.txt(place))
                    self.throwspots[self.throwspots.index(tps)] = newtps
                    del self.dreams[self.dreams.index((thing, place, ow))]
            nr += 1
        # build things into prep
        # save_throw_max_mineralgas to prevent the cc in throwspots[0] waiting.
        # do not hinder buildorder_exe or create_units (except for supplydepot and refinery)
        save_bo_sum_minerals = 0
        save_bo_sum_vespene = 0
        save_opening_minerals = 0
        save_opening_vespene = 0
        save_throw_max_minerals = 0
        save_throw_max_vespene = 0
        if self.opening_create_units > 0:
            for (kind,am) in self.opening_create:
                cost = self.get_added_cost(kind)
                save_bo_sum_minerals += cost.minerals * am
                save_bo_sum_vespene += cost.vespene * am
                save_opening_minerals += cost.minerals * am
                save_opening_vespene += cost.vespene * am
        for (thing, place, status) in self.buildorder_exe:
            cost = self.get_added_cost(thing)
            save_bo_sum_minerals += cost.minerals
            save_bo_sum_vespene += cost.vespene
            if self.game_phase == 'opening':
                save_opening_minerals += cost.minerals
                save_opening_vespene += cost.vespene
        for (thing,place,status, ow) in self.throwspots:
            if (status == 'prep'):
                cost = self.get_added_cost(thing)
                save_throw_max_minerals = max(cost.minerals, save_throw_max_minerals)
                save_throw_max_vespene = max(cost.vespene, save_throw_max_vespene)
        nr = 0
        while nr < len(self.throwspots): # a throwspot can be deleted in the loop
            tps = self.throwspots[nr]
            (thing,place,status, ow) = tps
            if (status == 'thought'):
                doitnow = False
                mycost = self.get_added_cost(thing)
                if (self.minerals >= save_bo_sum_minerals + save_throw_max_minerals + mycost.minerals):
                    if mycost.vespene == 0:
                        doitnow = True
                    elif (self.vespene >= save_bo_sum_vespene + save_throw_max_vespene + mycost.vespene):
                        doitnow = True
                if thing in {SUPPLYDEPOT}: # urgent
                    doitnow = True
                if thing in {REFINERY,COMMANDCENTER}: # ratherurgent
                    if (self.minerals >= save_opening_minerals):
                        doitnow = True
                # some buildorder_exe parts that are thrown:
                for (kind, am) in self.opening_create:
                    if (thing == kind) and (self.game_phase == 'opening'):
                        doitnow = True
                if (ow in {'marine_fun','do_cocoon','do_banshees','urgent_ocs','bunkercheese1',
                           'marauder_fun','do_pf_rush','cheese3_internals','do_rush_ghosts',
                           'throw_techsequence'}):
                    doitnow = True
                if doitnow:
                    if thing in self.all_structures_tobuildwalk:
                        scvt = self.get_near_scvt_to_goodjob(place)
                        if self.build_thing_tobuildwalk(scvt, thing, place, ow):
                            newtps = (thing, place, 'prep', ow)
                            self.log_success('thought to prep a thrown ' + thing.name + ' for ' + ow)
                            self.throwspots[self.throwspots.index(tps)] = newtps
                            del self.thoughts[self.thoughts.index((thing, place, ow))]
                    else: # labs, pfoc, army, upgr
                        if self.build_thing(thing, place, ow):
                            newtps = (thing, place, 'prep', ow)
                            self.log_success('thought to prep a thrown ' + thing.name + ' for ' + ow)
                            self.throwspots[self.throwspots.index(tps)] = newtps
                            del self.thoughts[self.thoughts.index((thing, place, ow))]
                            # place can be 'somewhere' while in prep it is chosen
                cost = self.get_added_cost(thing)
                save_throw_max_minerals = max(cost.minerals, save_throw_max_minerals)
                save_throw_max_vespene = max(cost.vespene, save_throw_max_vespene)
            nr += 1

    def manage_production_pause(self):
        todel = set()
        for el in self.production_pause_finish:
            (th, am, bu, bam) = el
            if self.we_finished_amount(bu) >= bam:
                todel.add(el)
        self.production_pause_finish -= todel
        todel = set()
        for el in self.production_pause_egg:
            (th, am, bu, bam) = el
            if self.eggorbird_amount(bu) >= bam:
                todel.add(el)
        self.production_pause_egg -= todel
        if (self.game_phase not in {'init','opening'}):
            self.production_pause_finish = set()
            self.production_pause_egg = set()

    def production_no_pause(self,thing) -> bool:
        pause = False
        for (th, am, bu, bam) in self.production_pause_finish:
            if th == thing:
                if self.we_finished_amount(bu) < bam:
                    if self.we_started_amount(th) >= am:
                        pause = True
        for (th, am, bu, bam) in self.production_pause_egg:
            if th == thing:
                if self.eggorbird_amount(bu) < bam:
                    if self.we_started_amount(th) >= am:
                        pause = True
        return (not pause)

    def urgent_supplydepots_adlib(self):
        if self.production_no_pause(SUPPLYDEPOT):
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
                for (th, pl, st, ow) in self.throwspots:
                    if th == SUPPLYDEPOT:
                        satisfied = True
                if not satisfied:
                    npiped = 0
                    for (martype,bartype,pos,dura) in self.eggs:
                        if martype == SUPPLYDEPOT:
                            npiped += 1
                    if (npiped < wanteddepots):
                        self.throw_anywhere(SUPPLYDEPOT,'urgent_supplydepots_adlib')

    def refineries_adlib(self):
        if self.production_no_pause(REFINERY):
            pause = False
            if (self.workerrushstate == 'busy'):
                pause = True
                self.log_success('refineries workerrush pause')
            if self.opening_name.find('marine-1') >= 0: # no refineries for this opening.
                if (self.game_phase in {'init','opening'}):
                    pause = True
                    self.log_success('refineries marine rush pause')
            if not pause:
                satisfied = False
                if self.frame < 2700: # 2 minutes
                    satisfied = True
                    self.log_success('refineries 2 minutes')
                for (exething, exeplace, status) in self.buildorder_exe:
                    if exething == REFINERY:
                        satisfied = True
                        self.log_success('refineries in buildorder')
                for (th, pl, st, ow) in self.throwspots:
                    if th == REFINERY:
                        satisfied = True
                        self.log_success('refineries in throwspots')
                if not satisfied:
                    ratherurgent = len(self.all_mine_bases) + 1
                    if (self.we_started_amount(REFINERY) < ratherurgent):
                        self.throw_anywhere(REFINERY,'refineries_adlib')
                    elif self.allow_throw(REFINERY):
                        self.throw_anywhere(REFINERY,'refineries_adlib')

    def opening_create_cut(self):
        # stop with opening_create_units when heavy losses
        if self.opening_create_units > 0:
            todel = set()
            for (kind, am) in self.opening_create:
                have = len(self.units(kind))
                if have > self.opening_create_hadmax[kind]:
                    self.opening_create_hadmax[kind] = have
                if am + have < self.opening_create_hadmax[kind]:
                    todel.add((kind,am))
                    self.opening_create_units -= am
            self.opening_create -= todel


    def techlabs_adlib(self):
        # ensure a free factory with a techlab.
        todo = 1
        for (lab_type,bui_type) in self.cradle:
            if lab_type in self.all_techlabs:
                has_idle = False
                for bui in self.structures(bui_type):
                    if bui.has_techlab and (bui.tag in self.idles):
                        has_idle = True
                if not has_idle:
                    # need one more
                    canlab = self.eggorbird_amount(bui_type)
                    for (a_lab_type, a_bui_type) in self.cradle:
                        if a_bui_type == bui_type:
                            if a_lab_type in self.all_labs:
                                canlab -= self.we_started_amount(a_lab_type)
                    if canlab > 0:
                        if self.allow_throw(lab_type):
                            self.throw_anywhere(lab_type,'techlabs_adlib')
                            todo = 0


    def armybuildings_adlib(self):
        if ('armybuilding' in self.good_plans):
            todo = 1
            if todo == 1:
                if self.we_finished_a(FACTORY) and (self.we_started_amount(STARPORT) < self.maxam_of_thing(STARPORT)):
                    self.throw_anywhere(STARPORT, 'armybuildings_adlib')
                elif self.we_finished_a(BARRACKS) and (self.we_started_amount(FACTORY) < self.maxam_of_thing(FACTORY)):
                    self.throw_anywhere(FACTORY, 'armybuildings_adlib')
                elif self.we_finished_a(SUPPLYDEPOT) and (self.we_started_amount(BARRACKS) < self.maxam_of_thing(BARRACKS)):
                    self.throw_anywhere(BARRACKS, 'armybuildings_adlib')

    def upgradebuildings_adlib(self):
        if ('upgradebuilding' in self.good_plans):
            # armory to hide widowmines
            # techlab for drilling claws
            loved = len(self.units(WIDOWMINE)) + len(self.units(WIDOWMINEBURROWED))
            if loved >= 6:
                if self.allow_throw(ARMORY):
                    if not self.we_started_a(ARMORY):
                        self.throw_anywhere(ARMORY,'upgradebuildings_adlib')
                if self.allow_throw(FACTORYTECHLAB):
                    if not self.we_started_a(FACTORYTECHLAB):
                        self.throw_anywhere(FACTORYTECHLAB,'upgradebuildings_adlib')
            # second armory
            if self.allow_throw(ARMORY):
                if (self.we_started_amount(ARMORY) < 2):
                    self.throw_anywhere(ARMORY, 'upgradebuildings_adlib')
            if self.allow_throw(ENGINEERINGBAY):
                if (self.we_started_amount(ENGINEERINGBAY) < 2):
                    self.throw_anywhere(ENGINEERINGBAY, 'upgradebuildings_adlib')

    def upgrades_adlib(self):
        if ('upgrade' in self.good_plans):
            todo = 1
            for beneficialminimum in [1200,800,400]:
                for (upg,benefitter) in self.upgrade_benefitter:
                    if self.allow_throw(upg):
                        benes = len(self.units(benefitter)) + len(self.structures(benefitter))
                        benes *= self.worth_of_thing(benefitter)
                        if (benes >= beneficialminimum):
                            cradtype = self.cradle_of_thing(upg)
                            freecrad = True
                            if cradtype in {ARMORY,ENGINEERINGBAY}:
                                if self.amount_usable[cradtype] <= 0:
                                    freecrad = False
                            if freecrad:
                                if upg != NUKESILONOVA:
                                    if self.check_techtree(upg):
                                        if not self.we_started_a(upg):
                                            if todo > 0:
                                                todo -= 1
                                                self.throw_anywhere(upg,'upgrades_adlib')


    def enough_for_buildorder_exe(self) -> bool:
        # guarantee the first part of buildorder, length self.opening_create_slack
        mim = 0
        gas = 0
        nr = 0
        for (item, goal, status) in self.buildorder_exe:
            if nr < self.opening_create_slack:
                basekind = self.basekind_of(item)
                cost = self.get_added_cost(basekind)
                mim += cost.minerals
                gas += cost.vespene
            nr += 1
        enough = (self.minerals >= mim) and (self.vespene >= gas)
        return enough

    def army_adlib(self):
        # medivacs at any phase
        if self.supply_used < 190:
            helees = 0
            for kind in {MARINE,MARAUDER,HELLIONTANK}:
                helees += len(self.units(kind))
            medivacs = helees // 7
            medivacs -= self.we_started_amount(MEDIVAC)
            if medivacs > 0:
                if self.check_techtree(MEDIVAC):
                    if self.production_no_pause(MEDIVAC):
                        starportsready = False
                        for sp in self.structures(STARPORT):
                            if sp.tag in self.readies:
                                if sp.tag in self.idles:
                                    starportsready = True
                        if starportsready:
                            self.throw_anywhere(MEDIVAC, 'army_adlib')
        # monobattle openings
        if self.opening_create_units > 0:
            can_pay_all_kinds = True
            for (kind,am) in self.opening_create:
                if not self.can_pay(kind):
                    can_pay_all_kinds = False
            if can_pay_all_kinds:
                possible = set()
                for (kind,am) in self.opening_create:
                    if self.check_techtree(kind):
                        cradtype = self.cradle_of_thing(kind)
                        if self.amount_usable[cradtype] > 0:
                            possible.add((kind,am))
                if len(possible) > 0:
                    (kind,am) = random.choice(tuple(possible))
                    if self.production_no_pause(kind):
                        cradtype = self.cradle_of_thing(kind)
                        units_todo = am
                        for tps in self.throwspots:
                            (th, goal, status, ow) = tps
                            if th == kind: # a marine is being made already
                                units_todo -= 1
                        for bar in self.structures(cradtype):
                            if bar.tag in self.readies:
                                spots = 0
                                if (bar.tag in self.idles):
                                    spots = 1
                                if self.has_finished_reactor(bar.position):
                                    spots = 2 - len(bar.orders)
                                # this barracks may want a lab
                                for (item, goal, status) in self.buildorder_exe:
                                    if cradtype == self.cradle_of_thing(item):
                                        if goal == bar.position:
                                            spots -= 1
                                # this barracks has planned a marine already
                                for tps in self.throwspots:
                                    (th, goal, status, ow) = tps
                                    if goal == bar.position:
                                        spots -= 1
                                if spots > 0:
                                    if self.enough_for_buildorder_exe():
                                        usable = True
                                        if bar.tag in self.speciality_of_tag: # barracks in a cocoon
                                            if self.speciality_of_tag[bar.tag] != 'wall': # wall barracks is ok
                                                usable = False
                                        if usable:
                                            if bar.has_techlab or (kind not in self.all_labarmy):
                                                if units_todo > 0:
                                                    self.throw_at_spot(kind, bar.position, 'army_adlib')
                                                    units_todo -= 1
        else: # normal
            if ('army' in self.good_plans):
                # do not interfere with opening
                goahead = True
                if self.game_phase == 'opening':
                    for (item, goal, status) in self.buildorder_exe:
                        if item in self.all_army:
                            goahead = False
                if goahead:
                    # supply ghost+raven = 4; fill to 196
                    if self.supply_used < 190:
                        vikings = 0
                        for kind in self.enemy_count:
                            if (kind in self.viking_targets):
                                vikings += 1.5 * self.enemy_count[kind]
                        #
                        if self.allow_throw(BATTLECRUISER):
                            self.throw_anywhere(BATTLECRUISER, 'army_adlib')
                        if self.allow_throw(BANSHEE):
                            if self.we_started_amount(BANSHEE) < 2:
                                flyingdetector = False
                                for det in {OVERSEER,OBSERVER,RAVEN}:
                                    if det in self.enemy_count:
                                        flyingdetector = True
                                if not flyingdetector:
                                    self.throw_anywhere(BANSHEE, 'army_adlib')
                        if self.allow_throw(RAVEN):
                            if self.we_started_amount(RAVEN) < 3:
                                if self.we_started_amount(BATTLECRUISER) > self.we_started_amount(RAVEN):
                                    self.throw_anywhere(RAVEN, 'army_adlib')
                        if self.allow_throw(VIKINGFIGHTER):
                            if self.we_started_amount(VIKINGFIGHTER) < vikings:
                                self.throw_anywhere(VIKINGFIGHTER, 'army_adlib')
                        if self.allow_throw(SIEGETANK):
                            self.throw_anywhere(SIEGETANK, 'army_adlib')
                        if self.allow_throw(WIDOWMINE):
                            self.throw_anywhere(WIDOWMINE, 'army_adlib')
                        if self.allow_throw(MARAUDER):
                            self.throw_anywhere(MARAUDER, 'army_adlib')
                        if self.allow_throw(CYCLONE):
                            if self.we_started_amount(CYCLONE) < 4:
                                self.throw_anywhere(CYCLONE, 'army_adlib')
                        if self.allow_throw(MARINE):
                            self.throw_anywhere(MARINE, 'army_adlib')
                    elif self.supply_used == 190:
                        # last bc
                        if self.allow_throw(BATTLECRUISER):
                            self.throw_anywhere(BATTLECRUISER, 'army_adlib')
                    elif self.supply_used <= 198:
                        # ghost, raven
                        if self.allow_throw(RAVEN):
                            if self.we_started_amount(RAVEN) == 0:
                                self.throw_anywhere(RAVEN, 'army_adlib')
                        elif self.allow_throw(GHOST):
                            if self.we_started_amount(GHOST) == 0:
                                self.throw_anywhere(GHOST, 'army_adlib')


    def calc_free_normal_basepositions(self):
        self.free_normal_basepositions = set()
        for normalpos in self.expansion_locations:
            free = True
            for stru in self.structures:
                pos = stru.position
                if self.near(pos, normalpos, 10):
                    free = False
            for (kind, pos) in self.enemy_structureinfo:
                if self.near(pos, normalpos, 10):
                    free = False
            for (th, pos, status, ow) in self.throwspots:
                if th == COMMANDCENTER:
                    if self.near(pos, normalpos, 10):
                        free = False
            if free:
                self.free_normal_basepositions.add(normalpos)

    def urgent_ocs(self):
        if self.cc_destiny_rush:
            if self.game_phase == 'opening':
                if self.check_techtree(ORBITALCOMMAND):
                    for cc in self.structures(COMMANDCENTER):
                        if cc.position in self.cc_destiny:
                            if self.cc_destiny[cc.position] == 'oc':
                                done = False
                                for (th, pos, status, ow) in self.throwspots:
                                    if (th == ORBITALCOMMAND) and (pos == cc.position):
                                        done = True
                                for (th,scv,pos,dura) in self.eggs:
                                    if (th == ORBITALCOMMAND) and (pos == cc.position):
                                        done = True
                                if not done:
                                    self.throw_at_spot(ORBITALCOMMAND,cc.position,'urgent_ocs')

    def pfoc_cc_adlib(self):
        if ('base' in self.good_plans):
            todo = 1
            for cc in self.structures(COMMANDCENTER):
                if cc.tag in self.readies:
                    if todo > 0:
                        if cc.position in self.cc_destiny:
                            if self.cc_destiny[cc.position] == 'pf':
                                if not self.we_started_at(PLANETARYFORTRESS, cc.position):
                                    if self.allow_throw(PLANETARYFORTRESS):
                                        self.throw_at_spot(PLANETARYFORTRESS, cc.position, 'pfoc_cc_adlib')
                                        todo -= 1
                            if self.cc_destiny[cc.position] == 'oc':
                                if not self.we_started_at(ORBITALCOMMAND, cc.position):
                                    if self.allow_throw(ORBITALCOMMAND):
                                        self.throw_at_spot(ORBITALCOMMAND, cc.position, 'pfoc_cc_adlib')
                                        todo -= 1
                        else: # strange, choose an oc
                            if not self.we_started_at(ORBITALCOMMAND, cc.position):
                                if self.allow_throw(ORBITALCOMMAND):
                                    self.throw_at_spot(ORBITALCOMMAND, cc.position, 'pfoc_cc_adlib')
                                    todo -= 1
            if todo > 0:
                if self.allow_throw(COMMANDCENTER):
                    self.calc_free_normal_basepositions()
                    if len(self.free_normal_basepositions) > 0:
                        ccpos = random.choice(tuple(self.free_normal_basepositions))
                        self.throw_at_spot(COMMANDCENTER, ccpos, 'pfoc_cc_adlib')

    def chaosbases_adlib(self):
        # try to control open area
        todo = 0
        if ('base' in self.good_plans):
            if self.allow_throw(COMMANDCENTER):
                self.calc_free_normal_basepositions()
                if len(self.free_normal_basepositions) < 4:
                    maybe_stuck = 0
                    for cc in self.all_bases:
                        if cc.position in self.cc_destiny:
                            if self.cc_destiny[cc.position] == 'pf':
                                maybe_stuck += 1
                    if self.we_started_amount(COMMANDCENTER) < 3 + maybe_stuck:
                        todo = 1
        if todo > 0:
            pos = random.choice(tuple(self.possible_cc_positions))
            if self.check_layout(COMMANDCENTER, pos):
                has_enemy_bam = False
                for tp in self.enemy_structureinfo:
                    (kind, pfpos) = tp
                    if (kind == PLANETARYFORTRESS) and self.near(pfpos,pos,12):
                        has_enemy_bam = True
                    elif (kind == PHOTONCANNON) and self.near(pfpos, pos, 10):
                        has_enemy_bam = True
                    elif (kind == SPINECRAWLER) and self.near(pfpos, pos, 10):
                        has_enemy_bam = True
                if not has_enemy_bam:
                    self.throw_at_spot(COMMANDCENTER, pos, 'chaosbases_adlib')

    def turrets1_adlib(self):
        if self.we_finished_a(ENGINEERINGBAY):
            ccs = self.we_started_amount(COMMANDCENTER) + self.structures(PLANETARYFORTRESS).amount \
                  + self.structures(ORBITALCOMMAND).amount
            mts = self.we_started_amount(MISSILETURRET)
            if (mts < ccs):
                if self.allow_throw(MISSILETURRET):
                    self.throw_anywhere(MISSILETURRET,'turrets1_adlib')

    def turrets6_adlib(self):
        if self.we_finished_a(ENGINEERINGBAY):
            ccs = self.we_started_amount(COMMANDCENTER) + self.structures(PLANETARYFORTRESS).amount \
                  + self.structures(ORBITALCOMMAND).amount
            mts = self.we_started_amount(MISSILETURRET)
            if self.supply_used > 190:
                if (mts < ccs * 6):
                    if self.allow_throw(MISSILETURRET):
                        self.throw_anywhere(MISSILETURRET,'turrets6_adlib')


    #*********************************************************************************************************************

    def fix_somewhere(self, beautiful_thing) -> bool:
        # Choose a specific cradle. The choice was delayed with 'somewhere'.
        # beautiful_thing is labs, pfoc, upgr, or army.
        # calculates self.fixed_somewhere
        beautiful_cradle = self.cradle_of_thing(beautiful_thing)
        # needstechlab ?/n/y
        needstechlab = '?'
        if beautiful_thing in self.all_labs + self.all_pfoc:
            needstechlab = 'n'
        for pair in self.techtree:
            if pair[0] == beautiful_thing:
                if (pair[1] in self.all_techlabs) and (pair[1] != beautiful_cradle):
                    needstechlab = 'y'
        cradles = set()
        # finished cradles
        for (thing,cradle_place) in self.birds:
            if thing == beautiful_cradle:
                cradle_dura = 0
                # cradle has finished lab
                hastechlab = 'n'
                for (otherthing,otherplace) in self.birds:
                    if (otherplace == cradle_place) and (otherthing != thing):
                        if (otherthing in self.all_techlabs + self.all_pfoc):
                            hastechlab = 'y'
                # cradle has unfinished lab
                for (otherthing, bartype, otherplace, dura) in self.eggs:
                    if (otherplace == cradle_place) and (otherthing != thing):
                        if (otherthing in self.all_techlabs + self.all_pfoc):
                            hastechlab = 'y'
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
                    if (needstechlab == '?') or (needstechlab == hastechlab):
                        exception = ((beautiful_thing, cradle_place) in self.unthinkable)
                        if not exception:
                            cradles.add((cradle_place, cradle_dura))
        # unfinished cradles
        for (cradle_thing,dummy,cradle_place,cradle_dura) in self.eggs:
            if cradle_thing == beautiful_cradle:
                # cradle has finished lab
                hastechlab = 'n'
                for (otherthing,otherplace) in self.birds:
                    if (otherplace == cradle_place) and (otherthing != cradle_thing):
                        if (otherthing in self.all_techlabs + self.all_pfoc):
                            hastechlab = 'y'
                # cradle is reserved
                free = True
                for (martype,bartype,pos,dura,owner) in self.preps:
                    if (bartype == cradle_thing) and (pos == cradle_place):
                        free = False
                if free:
                    if (needstechlab == '?') or (needstechlab == hastechlab):
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
        # find thingsowner in preps
        thingsowner = 'eh'
        matched = False
        for (martype,bartype,pos,dura,owner) in self.preps:
            if (martype == thing) and (pos == goal):
                matched = True
                thingsowner = owner
        if not matched:
            md = False
            self.log_success('Delay of creating a '+thing.name+' because it is not prepaired.')
        if thingsowner == 'follow_planning_exe':
            found = False
            thingcost = self.get_added_cost(thing)
            headcost = Cost(0,0)
            headcradles = set()
            for (bu, go, status) in self.buildorder_exe:
                if not found:
                    if (thing == bu):
                        found = True
                        if goal != go:
                            self.log_success('May egg in exchange of another ' + thing.name)
                        if (self.minerals < headcost.minerals):
                            md = False
                        if (thingcost.vespene > 0) and (self.vespene < headcost.vespene):
                            md = False
                        if self.cradle_of_thing(thing) in headcradles:
                            md = False
                    else:
                        headcost += self.get_added_cost(bu)
                        headcradles.add(self.cradle_of_thing(bu))
            if (not md):
                self.log_success('Delay of creating a ' + thing.name + ' because of buildorder_exe')
            # delay for something urgent
            me_urgent = (thingsowner.find('urgent') >= 0)
            some_urgent = False
            urgent_thing = None
            for (martype,bartype,pos,dura,owner) in self.preps:
                if owner.find('urgent') >= 0:
                    some_urgent = True
                    urgent_thing = martype
            if some_urgent and not me_urgent:
                md = False
                self.log_success('Delay of egging because of an urgent '+urgent_thing.name)
        return md

    def build_thing_tobuildwalk(self,scvt,thing,place,owner) -> bool:
        self.log_success('trying to prep '+thing.name+' at '+self.txt(place)+' for '+owner)
        didit = False
        if (thing,place,owner) in self.thoughts:
            if thing == COMMANDCENTER:
                self.build_commandcenter(scvt,place,owner)
                didit = True
            elif thing == REFINERY:
                # no refinery before its commandcenter
                expa = self.nowhere
                for ccpos in self.expansion_locations:
                    if self.near(place, ccpos, self.miner_bound):
                        expa = ccpos
                canbuild = False
                for (th,po) in self.birds:
                    if (po == expa) and (th in [COMMANDCENTER,ORBITALCOMMAND,PLANETARYFORTRESS]):
                        canbuild = True
                if expa in self.goal_of_trabu_scvt.values():
                    canbuild = True
                if canbuild:
                    didit = self.build_building(scvt,thing,place,owner)
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
                            (th, po, status, ow) = tps
                            if (th == thing) and (po == place):
                                todel.add(tps)
                        for tps in todel:
                            del self.throwspots[self.throwspots.index(tps)]
            elif thing in self.all_structures_tobuildwalk:
                didit = self.build_building(scvt,thing,place,owner)
        else: # not in thoughts
            self.log_success('BUG trying to build '+thing.name+' by '+owner+' but it is not in thoughts.')
            self.log_thoughts()
        if didit:
            self.log_success('thought to prep ' + thing.name + ' at ' + self.txt(place))
            dura = 1
            self.preps.add((thing, scvt, place, dura, owner))
        return didit

    def check_supply(self,ship) -> bool:
        ok = True
        if ship == SCV:
            ok = (self.supply_left >= 1)
        elif ship in self.all_army:
            ok = (self.supply_left >= self.supply_of_army[ship])
        return ok

    def check_cradleidle(self,ship) -> bool:
        if (ship in self.all_structures_tobuildwalk):
            ok = True
        elif ship == SCV:
            ok = False
            for cradle_type in {COMMANDCENTER,ORBITALCOMMAND,PLANETARYFORTRESS}:
                for dock in self.structures(cradle_type):
                    if dock.tag in self.readies:
                        if dock.tag in self.idles:
                            ok = True
        else:    
            ok = False
            cradle_type = self.cradle_of_thing(ship)
            for dock in self.structures(cradle_type):
                if dock.tag in self.readies:
                    if dock.tag in self.idles:
                        ok = True
        return ok      

    def prepped_to_egg(self,  martype, bartype, pos):
        self.log_success('succeeded prep to egg ' + martype.name + ' at ' + self.txt(pos))
        # count opening_create_units
        if self.opening_create_units > 0:
            todel = set()
            toadd = set()
            for (kind,am) in self.opening_create:
                if kind == martype:
                    self.log_success('Ha another ' + martype.name + '!')
                    self.opening_create_units -= 1
                    todel.add((kind,am))
                    if am > 1:
                        toadd.add((kind,am-1))
            self.opening_create -= todel
            self.opening_create = self.opening_create | toadd
        # del preps
        todel = set()
        for tps in self.preps:
            (ma, ba, po, dura, owner) = tps
            if (ma == martype):
                if (po == pos) or (po == self.somewhere):
                    todel.add(tps)
        self.preps -= todel
        # del throw
        throwtodel = set()
        for tps in self.throwspots:
            (th, po, status, ow) = tps
            if (th == martype):
                if (po == pos) or (po == self.somewhere):
                    throwtodel.add(tps)
        for tps in throwtodel:
            del self.throwspots[self.throwspots.index(tps)]
        # del buildorder_exe etc
        self.log_success('I finished prepping a '+martype.name)
        self.remove_from_planning_etc(martype, pos)

    def bought(self, thing):
        # after the can_pay check a thing is bought.
        # this administration fills the purse for 10 frames, to prevent overspending.
        self.add_purse(thing)
        self.bought_admin.append((thing,self.frame))

    def do_bought_admin(self):
        todel = []
        for (thing,boughtframe) in self.bought_admin:
            if self.frame > boughtframe + 10:
                todel.append((thing,boughtframe))
        for (thing,boughtframe) in todel:
            self.del_purse(thing)
            del self.bought_admin[self.bought_admin.index((thing,boughtframe))]


    async def do_buildandretry(self):
        # all is ready to start building a tobuildwalk. But sometimes the build command fails.
        todel = []
        for items in self.buildandretry:
            (scvt, building, goal, startframe) = items
            if scvt not in self.commandgiven: # init
                self.commandgiven[scvt] = -99999
            if (self.frame<startframe+self.patience):
                if (scvt in self.all_scvt):
                    for scv in self.units(SCV):
                        if scv.tag == scvt:
                            if self.job_of_scvt[scvt] == 'fencer':
                                if self.frame >= self.commandgiven[scvt] + 20: # accept a new command
                                    # there we go (or go again)
                                    if building == REFINERY:
                                        for gey in self.vespene_geyser:
                                            if gey.position == goal:
                                                self.log_command('scv.build_gas(gey)')
                                                dummy = scv.build_gas(gey)
                                    else:
                                        self.log_command('scv.build(' + building.name + ',goal)')
                                        dummy = scv.build(building, goal)
                                    self.commandgiven[scvt] = self.frame
                                else: # working on a command
                                    if self.frame >= self.commandgiven[scvt] + 10: # command should have landed
                                        is_building_it = False
                                        for (eggthing,eggscv,eggpos,eggdura) in self.eggs:
                                            if (eggscv == scv) and (eggthing == building) and (eggpos == goal):
                                                is_building_it = True
                                        if is_building_it:
                                            # believe it is doing the right thing
                                            self.promote(scv,'builder')
                                            todel.append(items)
                                            self.prepped_to_egg(building, scv, goal)
                                            if building in {BARRACKS,FACTORY}:
                                                self.set_rallypoint(goal)
                                            self.commandgiven[scvt] = -99999 # command is handled
            else: # failed to build
                todel.append(items)
                for scv in self.units(SCV):
                    if scv.tag == scvt:
                        self.promote(scv, 'idler')
                        self.log_success('In buildandretry we discarded a ' + building.name)
                        if self.we_started_amount(building) <= 1:
                            self.throw_anywhere(building,'do_buildandretry')
        for items in todel:
            (scvt, building, goal, startframe) = items
            self.del_purse(building)
            del self.buildandretry[self.buildandretry.index(items)]

    async def do_trainandretry(self):
        # all is ready to start training a armyunit, scv or upgrade. But sometimes the command fails.
        todel = []
        for items in self.trainandretry:
            (cradletype, cradletag, unitupgrade, startframe) = items
            if cradletag not in self.commandgiven: # init
                self.commandgiven[cradletag] = -99999
            if (self.frame < startframe + self.patience):
                for cradle in self.structures(cradletype):
                    if cradle.tag == cradletag:
                        #if unitupgrade == MEDIVAC:
                        #    lookatme = True
                        slots = 1
                        if self.has_finished_reactor(self.position_of_building(cradle)):
                            slots = 2
                        eggcount = 0
                        for (martype, bartype, pos, dura) in self.eggs:
                            if (bartype == cradletype) and (pos == self.position_of_building(cradle)):
                                eggcount += 1
                                if martype in self.all_labs:
                                    eggcount = 99999  # you cannot make a marine now
                        if self.frame >= self.commandgiven[cradletag] + 20: # accept a new command
                            if eggcount < slots:
                                # there we go (or go again)
                                self.log_command(cradle.name + '.train(' + unitupgrade.name + ')')
                                if unitupgrade in self.all_upgrades:
                                    await self.do_upgrade(unitupgrade, self.position_of_building(cradle))
                                elif unitupgrade == NUKESILONOVA:
                                    cradle(AbilityId.BUILD_NUKE)
                                else:
                                    cradle.train(unitupgrade)
                                self.commandgiven[cradletag] = self.frame
                        else: # working on a command
                            if self.frame >= self.commandgiven[cradletag] + 10: # command should have landed
                                if eggcount > 0:
                                    is_training_it = False
                                    for (eggmartype, eggbartype, eggpos, eggdura) in self.eggs:
                                        if (eggmartype == unitupgrade) and (eggbartype == cradletype) and (eggpos == cradle.position):
                                            is_training_it = True
                                    if is_training_it:
                                        # believe it is doing the right thing
                                        place = self.position_of_building(cradle)
                                        self.prepped_to_egg(unitupgrade, cradle.type_id, place)
                                        todel.append(items)
                                        # mark the command as "handled"
                                        self.commandgiven[cradletag] = -99999  # command is handled
            else:
                todel.append(items)
                self.log_success('In trainandretry we discarded a ' + unitupgrade.name)
        for items in todel:
            (cradletype, cradletag, unitupgrade, startframe) = items
            del self.trainandretry[self.trainandretry.index(items)]
            self.del_purse(unitupgrade)
            delgym = set()
            for (strtype,strtag,trainee,owner) in self.gym:
                if (strtag == cradletag) and (unitupgrade == trainee):
                    delgym.add((strtype,strtag,trainee,owner))
            for sto in delgym:
                del self.gym[self.gym.index(sto)]

    async def do_growandretry(self):
        # all is ready to start growing a pfoc or lab. But sometimes the lab command fails.
        todel = []
        for items in self.growandretry:
            (oldbuildingtag, newbuilding, startframe) = items
            if oldbuildingtag not in self.commandgiven: # init
                self.commandgiven[oldbuildingtag] = 0
            if (self.frame < startframe + self.patience):
                for oldbuilding in self.structures:
                    if oldbuilding.tag == oldbuildingtag:
                        place = oldbuilding.position
                        if oldbuildingtag in self.idles:
                            if self.frame >= self.commandgiven[oldbuildingtag] + 20:
                                # there we go (or go again)
                                self.log_command(oldbuilding.name + '.grow(' + newbuilding.name + ')')
                                if newbuilding == BARRACKSTECHLAB:
                                    lookatme = True
                                oldbuilding.train(newbuilding)
                                self.commandgiven[oldbuildingtag] = self.frame
                        else: # it does something
                            if self.frame >= self.commandgiven[oldbuildingtag] + 10:
                                if self.frame < self.commandgiven[oldbuildingtag] + 30:
                                    is_growing_it = False
                                    for (eggmartype, eggbartype, eggpos, eggdura) in self.eggs:
                                        if (eggmartype == newbuilding) and (eggbartype == oldbuilding.type_id) and (eggpos == place):
                                            is_growing_it = True
                                    if is_growing_it:
                                        # believe it is doing the right thing
                                        self.prepped_to_egg(newbuilding, oldbuilding.type_id, place)
                                        todel.append(items)
                                        self.commandgiven[oldbuildingtag] = -99999  # command is handled
            else:
                todel.append(items)
                self.log_success('In growandretry we discarded a ' + newbuilding.name)
        for items in todel:
            (oldbuildingtag, newbuilding, startframe) = items
            del self.growandretry[self.growandretry.index(items)]
            self.del_purse(newbuilding)
            if oldbuildingtag in self.ambition_of_strt: # it could e.g. be killed
                del self.ambition_of_strt[oldbuildingtag]

    async def start_construction(self):
        # max 1 per frame to protect can_pay
        for scvt in self.goal_of_trabu_scvt:
            if self.job_of_scvt[scvt] == 'traveller':
                goal = self.goal_of_trabu_scvt[scvt]
                building = self.structure_of_trabu_scvt[scvt]
                for scv in self.units(SCV):
                    if scv.tag == scvt:
                        for (atag, agoal, abuilding, sframe, aframe) in self.arrivals:
                            if (atag == scvt) and (agoal == goal) and (abuilding == building):
                                # check the traveller
                                ok = True
                                if self.frame > aframe:
                                    self.log_success('Traveller is over time!')
                                    ok = False
                                    self.promote(scv, 'idler')
                                    # expect the absense of traveller to delete the rest
                                    # accept few of these timeouts
                                    self.throw_history(building, goal)
                                elif self.frame > sframe + 6: # allow startup frames
                                    if (len(scv.orders) == 0):
                                        ok = False
                                        self.log_success('Traveller idle')
                                    else:
                                        for order in scv.orders:
                                            if order.ability.id == AbilityId.HARVEST_GATHER:
                                                if self.near(scv.position,goal,15):
                                                    ok = False
                                                    self.log_success('Traveller gathers near goal')
                                            elif order.ability.id != AbilityId.MOVE:
                                                ok = False
                                                self.log_success('Traveller doesnt move but ')
                                                #print(order.ability.id)
                                            elif type(order.target) == int:
                                                ok = False
                                                self.log_success('Traveller moves to thing')
                                            elif (order.target.x != goal.x) or (order.target.y != goal.y): # fails as one condition
                                                ok = False
                                                self.log_success('Traveller moves not to goal')
                                if not ok:
                                    self.log_success('Traveller ' + self.name(scvt) + ' went astray, rerouted')
                                    scv.move(goal)
                                if self.near(scv.position, goal, 12):
                                    self.clear_from_mines(goal)
                                # settling
                                if self.near(scv.position, goal, 3):
                                    self.log_success('build site of a '+building.name+' reached')
                                    self.promote(scv,'settler')
        for scvt in self.goal_of_trabu_scvt:
            if self.job_of_scvt[scvt] == 'settler':
                goal = self.goal_of_trabu_scvt[scvt]
                building = self.structure_of_trabu_scvt[scvt]
                if self.may_egg_now(building, goal):
                    self.log_success('trying to egg ' + building.name)
                    if self.check_techtree(building):
                        if self.can_pay(building):
                            for scv in self.units(SCV):
                                if scv.tag == scvt:
                                    if not scv.is_constructing_scv:
                                        if self.near(scv.position,goal,3):
                                            self.promote(scv,'fencer') # prevents repeat
                                            self.log_workers('fencing '+building.name+' '+self.name(scvt))
                                            self.add_purse(building)
                                            self.buildandretry.append((scv.tag, building, goal, self.frame))
                                        else:
                                            self.log_success('not near')
                                            # try back-to-track
                                            scv.move(goal)
                                    else:
                                        self.log_success('still building')
                        else:
                            self.log_success('no pay ' + self.missing)
                    else:
                        self.log_success('no techtree ' + self.missing)
        # also, realize an ambition: pfoc, labs
        for oldbuilding in self.structures:
            if oldbuilding.tag in self.readies:
                if oldbuilding.tag in self.idles:  # not in eggs
                    if oldbuilding.tag in self.ambition_of_strt:
                        newbuilding = self.ambition_of_strt[oldbuilding.tag]
                        pos = self.position_of_building(oldbuilding)
                        inretry = False
                        for (obt, bui, fra) in self.growandretry:
                            if (bui == newbuilding) and (obt == oldbuilding.tag):
                                inretry = True
                        if not inretry:
                            if self.may_egg_now(newbuilding,pos):
                                self.log_success('trying to egg ' + newbuilding.name)
                                if self.check_techtree(newbuilding):
                                    if self.can_pay(newbuilding):
                                        self.add_purse(newbuilding)
                                        self.growandretry.append((oldbuilding.tag, newbuilding, self.frame))
                                    else:
                                        self.log_success('no pay ' + self.missing)
                                else:
                                    self.log_success('no techtree ' + self.missing)
        # also, realize a gym: upgr, army
        for (strtype,strtag,trainee,owner) in self.gym:
            for cradle in self.structures(strtype):
                if cradle.tag in self.readies:
                    if cradle.tag == strtag:
                        slots = 1
                        if self.has_finished_reactor(self.position_of_building(cradle)):
                            slots = 2
                        eggcount = 0
                        for (martype, bartype, pos, dura) in self.eggs:
                            if (bartype == strtype) and (pos == self.position_of_building(cradle)):
                                eggcount += 1
                                if martype in self.all_labs:
                                    eggcount = 99999 # you cannot make a marine now
                        for (oby, obt, uu, fra) in self.trainandretry:
                            if (uu == trainee) and (obt == cradle.tag):
                                eggcount += 1
                        if eggcount < slots:
                            pos = self.position_of_building(cradle)
                            if self.may_egg_now(trainee, pos):
                                self.log_success('trying to egg ' + trainee.name)
                                if self.check_techtree(trainee):
                                    if self.can_pay(trainee):
                                        if self.check_supply(trainee):
                                            self.add_purse(trainee)
                                            self.trainandretry.append((strtype,strtag, trainee, self.frame))
                                        else:
                                            self.log_success('no supply')
                                    else:
                                        self.log_success('no pay ' + self.missing)
                                else:
                                    self.log_success('no techtree ' + self.missing)

    def speedmove(self,scv,goal):
        if self.near(scv.position,goal,15):
            self.log_command('scv.move(goal)')
            scv.move(goal)
        else:
            minsd = 99999
            for mim in self.all_minerals:
                (mimpos,mimt) = mim
                sd = self.sdist(mimpos,goal)
                if sd < minsd:
                    minsd = sd
                    bestmim = mim
            if minsd >= 15*15:
                self.log_command('scv.move(goal)')
                scv.move(goal)
            else:
                self.go_gather_mim(scv,bestmim)

    def build_building(self,scvt,building,goal,owner) -> bool:
        # for tobuildwalk buildings except COMMANDCENTER
        didit = False
        # you do not have to wait for minerals and techtree
        if (self.check_future_techtree(building)) or (self.game_phase == 'opening'):
            for scv in self.units(SCV):
                if scv.tag == scvt:
                    self.promote(scv,'traveller')
                    self.goal_of_trabu_scvt[scvt] = goal
                    self.structure_of_trabu_scvt[scvt] = building
                    self.owner_of_trabu_scvt[scvt] = owner
                    self.log_workers('ordered  '+building.name+' '+self.name(scvt))
                    self.speedmove(scv,goal)
                    didit = True
                    # add to preps for restcode in this step
                    restdura = self.walk_duration(scv.position,goal)
                    self.preps.add((building, scv, goal, restdura, owner))
                    maxdura = 2 * restdura + 2
                    self.arrivals.add((scv.tag,goal,building,self.frame,self.frame+self.frames_per_second*maxdura))
        return didit

    def build_commandcenter(self,trabu_scvt,goal,owner):
        building = COMMANDCENTER
        # you do not have to wait for minerals and techtree
        if self.frame >= 2000:
            scvt = self.get_near_scvt_to_goodjob(goal)
            for scv in self.units(SCV):
                if scv.tag == scvt:
                    self.promote(scv,'escorter')
                    self.log_command('scv.attack(goal)')
                    scv.attack(goal)
        toget = 1
        for mar in self.units(MARINE):
            if mar.tag not in self.speciality_of_tag:
                if mar.tag not in bunker_if.marinetags:
                    if toget > 0:
                        toget -= 1
                        self.log_command('mar.attack(goal)')
                        mar.attack(goal)
        scvt = trabu_scvt
        for scv in self.units(SCV):
            if scv.tag == scvt:
                self.goal_of_trabu_scvt[scvt] = goal
                self.structure_of_trabu_scvt[scvt] = building
                self.owner_of_trabu_scvt[scvt] = owner
                self.promote(scv,'traveller')
                self.speedmove(scv, goal)
                # add to preps for restcode in this step
                restdura = self.walk_duration(scv.position, goal)
                self.preps.add((building, scv, goal, restdura, owner))
                maxdura = 2 * restdura + 2
                self.arrivals.add((scv.tag,goal,building,self.frame,self.frame + self.frames_per_second * maxdura))
        # give the cc a cc_destiny
        if goal in self.expansion_locations:
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
        # reserve place to repair ships

    def delete_all_thrown_thoughts_and_dreams(self):
        # excluding supplydepots. Nonsense? Shouldnt that be rethought?
        todel = set()
        for tpo in self.thoughts:
            (thing,place,owner) = tpo
            if owner != 'follow_planning_exe':
                if thing != SUPPLYDEPOT:
                    todel.add(tpo)
        for tpo in todel:
            self.thoughts.remove(tpo)
        todel = set()
        for tpo in self.dreams:
            (thing, place, owner) = tpo
            if owner != 'follow_planning_exe':
                if thing != SUPPLYDEPOT:
                    todel.add(tpo)
        for tpo in todel:
            del self.dreams[self.dreams.index(tpo)]
        todel = []
        for tps in self.throwspots:
            (th, po, status, ow) = tps
            if (status in {'dream','thought'}):
                if th != SUPPLYDEPOT:
                    todel.append(tps)
                    if th in self.all_structures_tobuildwalk:
                        self.erase_layout(th, po)
                    if th in self.all_army:
                        self.army_supply -= self.supply_of_army[th]
                    if po != self.somewhere:
                        self.chosenplaces.append((th, po))
        for tps in todel:
            del self.throwspots[self.throwspots.index(tps)]

    def disappeared_building(self, goneplace):
        # we tried to use a building but it is gone. Is this code reachable?
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
            (th, po, status, ow) = tps
            if po == goneplace:
                todel.append(tps)
                while (th, po, ow) in self.dreams:
                    del self.dreams[self.dreams.index((th, po, ow))]
        for tps in todel:
            del self.throwspots[self.throwspots.index(tps)]
        # ambition and gym are pruned to existing buildings in gamestate

    def nearly_ready(self, cc,cctype, secs) -> bool:
        ok = (cc.tag in self.readies)
        if not ok:
            for (thing,scv,pos,dura) in self.eggs:
                if (thing == cctype) and (pos == cc.position):
                    ok = (dura <= secs)
        return ok

    def nearly_free(self, cc,cctype, secs) -> bool:
        chances = 1
        if self.has_finished_reactor(cc.position):
            chances = 2
        for (martype, bartype, pos, dura) in self.eggs:
            if (bartype == cctype) and (pos == cc.position) and (dura >= secs):
                chances -= 1
        return (chances > 0)

    def build_thing(self,ambition,place,owner) -> bool:
        # labs, pfoc, upgr, army
        # puts a building in ambition_of_strt, then it will become idle, then be transformed
        # or in gym, when it is idle it will start training that army or upgrade
        # all checks must be met or nearly met.
        # fixes place==somewhere. This is sometimes done in planning.
        self.log_success('trying to prep '+ambition.name+' at '+self.txt(place)+' for '+owner)
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
                if self.check_nearly_techtree(ambition,10):
                    if self.can_nearly_pay(ambition,10):
                        seen = False
                        for cc in self.structures(cradle_type):
                            if self.position_of_building(cc) == fixplace:
                                seen = True
                                if self.nearly_ready(cc,cradle_type,10):
                                    if self.nearly_free(cc, cradle_type, 10):
                                        if cc.tag not in self.ambition_of_strt:
                                            ingym = False
                                            for (strtype,strtag,trainee,ow) in self.gym:
                                                if cc.tag == strtag:
                                                    ingym = True
                                            if not ingym:
                                                if self.check_supply(ambition):
                                                    if (ambition in self.all_labs):
                                                        if not cc.has_add_on:
                                                            self.ambition_of_strt[cc.tag] = ambition
                                                            self.owner_of_ambistrt[cc.tag] = owner
                                                            didit = True
                                                    else: # pfoc
                                                        self.ambition_of_strt[cc.tag] = ambition
                                                        self.owner_of_ambistrt[cc.tag] = owner
                                                        didit = True
                        if not seen:
                            self.log_success('That building is gone')
                            self.disappeared_building(fixplace)
            else: # not in thoughts
                self.log_success('BUG trying to build '+ambition.name+' by '+owner+' but it is not in thoughts.')
                self.log_thoughts()
            if didit:
                self.log_success('thought to prep ' + ambition.name + ' at ' + self.txt(place))
                dura = 1
                self.preps.add((ambition, cradle_type, fixplace, dura, owner))
        else: # army, upgr
            trainee = ambition
            if ((trainee, place, owner) in self.thoughts) or ((trainee, self.somewhere, owner) in self.thoughts):
                if self.check_nearly_techtree(trainee,8):
                    if self.can_nearly_pay(trainee,8):
                        seen = False
                        for cc in self.structures(cradle_type):
                            if self.position_of_building(cc) == fixplace:
                                seen = True
                                if self.nearly_ready(cc,cradle_type,8):
                                    if self.nearly_free(cc, cradle_type, 8):
                                        if cc.tag not in self.ambition_of_strt:
                                            maxamgym = 1
                                            if self.has_finished_reactor(cc.position):
                                                maxamgym = 2
                                            amgym = 0
                                            for (strtype,strtag,tr,ow) in self.gym:
                                                if strtag == cc.tag:
                                                    amgym += 1
                                            if amgym < maxamgym:
                                                if self.check_supply(trainee):
                                                    self.gym.append((cradle_type,cc.tag,trainee,owner))
                                                    didit = True
                        if not seen:
                            self.log_success('That building is gone')
                            self.disappeared_building(fixplace)
            else:  # not in thoughts
                self.log_success('BUG trying to train ' + trainee.name + ' by ' + owner + ' but it is not in thoughts.')
                self.log_thoughts()
            if didit:
                self.log_success('thought to prep '+ambition.name + ' at ' + self.txt(place))
                dura = 1
                self.preps.add((trainee, cradle_type, fixplace, dura, owner))
        return didit

    async def do_upgrade(self,upg,place):
        if upg in self.all_upgrades:
            if self.already_pending_upgrade(upg) == 0:
                if self.check_techtree(upg):
                    cra = self.cradle_of_thing(upg)
                    for ar in self.structures(cra):
                        if ar.tag in self.readies:
                            if (self.position_of_building(ar) == place):
                                if (ar.tag in self.idles):
                                    if self.in_purse(upg):
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


#*********************************************************************************************************************
#   army movement routines

    def focusfire(self):
        # self.focus: per unittag a preferred victimtag
        # prefer kills, else weak opponents, else lower tags
        # ignores overkill, eggs, larvae
        grounddamage = {}
        groundattacks = {}
        for myn in self.units:
            mydamage = 0
            myattacks = 0
            for weapon in myn._weapons:
                if myn.weapon_cooldown < 5:
                    if weapon.type in TARGET_GROUND:
                        mydamage += weapon.damage
                        myattacks = weapon.attacks
            grounddamage[myn.tag] = mydamage + myn.attack_upgrade_level
            groundattacks[myn.tag] = myattacks
        airdamage = {}
        airattacks = {}
        for myn in self.units:
            mydamage = 0
            myattacks = 0
            for weapon in myn._weapons:
                if myn.weapon_cooldown < 5:
                    if weapon.type in TARGET_AIR:
                        mydamage += weapon.damage
                        myatacks = weapon.attacks
            airdamage[myn.tag] = mydamage + myn.attack_upgrade_level
            airattacks[myn.tag] = myattacks
        # damagemax, couldfocus
        damagemax = {}
        couldfocus = {}
        for ene in self.enemy_units | self.enemy_real_structures:
            if ene.type_id not in {EGG, LARVA, AUTOTURRET}:
                damagemax[ene.tag] = 0
        for myn in self.units:
            couldfocus[myn.tag] = []
            mypos = myn.position
            mytile = self.maptile_of_pos(mypos)
            for tile in self.nine[mytile]:
                for ene in self.enemies_of_tile[tile]:
                    if ene.type_id not in {EGG,LARVA, AUTOTURRET}:
                        enepos = ene.position
                        armor = ene.armor + ene.armor_upgrade_level
                        if ene.is_flying:
                            if self.near(mypos,enepos,myn.air_range+myn.radius+ene.radius+0.25):
                                if airdamage[myn.tag] > 0:
                                    couldfocus[myn.tag].append(ene.tag)
                            if self.near(mypos, enepos, myn.air_range+myn.radius+ene.radius):
                                if myn.weapon_cooldown == 0:
                                    damagemax[ene.tag] += (airdamage[myn.tag] - armor) * airattacks[myn.tag]
                        else:
                            if self.near(mypos, enepos, myn.ground_range+myn.radius+ene.radius+0.25):
                                if grounddamage[myn.tag] > 0:
                                    couldfocus[myn.tag].append(ene.tag)
                            if self.near(mypos, enepos, myn.ground_range+myn.radius+ene.radius):
                                if myn.weapon_cooldown == 0:
                                    damagemax[ene.tag] += (grounddamage[myn.tag] - armor) * groundattacks[myn.tag]
        focusplus = []
        for ene in self.enemy_units | self.enemy_real_structures:
            if ene.type_id not in {EGG, LARVA, AUTOTURRET}:
                if damagemax[ene.tag] > ene.health+ene.shield:
                    focusplus.append((0,ene.health+ene.shield,ene.tag))
                else:
                    focusplus.append((1,ene.health+ene.shield,ene.tag))
        focusplus.sort()
        focussolo = []
        for (alive,size,enetag) in focusplus:
            focussolo.append(enetag)
        self.focus = {}
        self.queuefocus = {}
        for myntag in couldfocus:
            minix = 99999
            bestenetag = self.notag
            for enetag in couldfocus[myntag]:
                ix = focussolo.index(enetag)
                if ix < minix:
                    minix = ix
                    bestenetag = enetag
            if bestenetag != self.notag:
                self.focus[myntag] = bestenetag
            skiptag = bestenetag
            minix = 99999
            bestenetag = self.notag
            for enetag in couldfocus[myntag]:
                if enetag != skiptag:
                    ix = focussolo.index(enetag)
                    if ix < minix:
                        minix = ix
                        bestenetag = enetag
            if bestenetag != self.notag:
                self.queuefocus[myntag] = bestenetag

    def calc_fightpos(self):
        # fightposition hint dependant on nearest enemy
        self.fightpos = {}
        for myn in self.units:
            self.fightpos[myn.tag] = self.nowhere
            mypos = myn.position
            minsd = 10*10 # do not react on enemies further away
            i_can_hit_air = False
            i_can_hit_ground = False
            for weapon in myn._weapons:
                if weapon.type in TARGET_GROUND:
                    i_can_hit_ground = True
                if weapon.type in TARGET_AIR:
                    i_can_hit_air = True
            mytile = self.maptile_of_pos(mypos)
            for tile in self.nine[mytile]:
                for ene in self.enemies_of_tile[tile]:
                    if ene.type_id not in {EGG,LARVA,AUTOTURRET}:
                        enepos = ene.position
                        sd = self.sdist(mypos,enepos)
                        if sd < minsd:
                            # this is your enemy unit. Make a plan.
                            it_can_hit_air = False
                            it_can_hit_ground = False
                            for weapon in ene._weapons:
                                if weapon.type in TARGET_GROUND:
                                    it_can_hit_ground = True
                                if weapon.type in TARGET_AIR:
                                    it_can_hit_air = True
                            i_can_hit_it = False
                            it_can_hit_me = False
                            if ene.is_flying:
                                if i_can_hit_air:
                                    i_can_hit_it = True
                                    myrange = myn.air_range
                            else:
                                if i_can_hit_ground:
                                    i_can_hit_it = True
                                    myrange = myn.ground_range
                            if myn.is_flying:
                                if it_can_hit_air:
                                    it_can_hit_me = True
                                    itsrange = ene.air_range
                            else:
                                if it_can_hit_ground:
                                    it_can_hit_me = True
                                    itsrange = ene.ground_range
                            # plandist
                            if i_can_hit_it and it_can_hit_me:
                                if myrange > itsrange:
                                    plandist = max(0.5*myrange+0.5*itsrange, myrange - 1) + myn.radius + ene.radius
                                else:
                                    plandist = (myrange - 1) + myn.radius + ene.radius
                            elif it_can_hit_me:
                                plandist = (itsrange + 1) + myn.radius + ene.radius
                            elif i_can_hit_it:
                                plandist = (myrange - 1) + myn.radius + ene.radius
                            if i_can_hit_it or it_can_hit_me:
                                minsd = sd
                                self.fightpos[myn.tag] = enepos.towards(mypos,plandist)

    def attackmove(self,tag,goal,hangout):
        # makes my unit move to goal, attacking enemies in range.
        # hangout is the size of the area it can hang out after the goal is reached.
        self.attackmove_state[tag] = 'rest'
        self.attackmove_goal[tag] = goal
        self.attackmove_goalreached[tag] = False
        self.attackmove_enetag[tag] = self.notag
        self.attackmove_queue_enetag[tag] = self.notag
        self.attackmove_hangout[tag] = hangout
        self.attackmove_fightgoal[tag] = self.nowhere
        self.attackmove_goaltried[tag] = 0
        for unt in self.units:
            if unt.tag == tag:
                if len(unt.orders) > 0:
                    unt(AbilityId.STOP)

    def end_attackmove(self,tag):
        if tag in self.attackmove_state:
            del self.attackmove_state[tag]
            del self.attackmove_goal[tag]
            del self.attackmove_goalreached[tag]
            del self.attackmove_enetag[tag]
            del self.attackmove_queue_enetag[tag]
            del self.attackmove_hangout[tag]
            del self.attackmove_fightgoal[tag]
            del self.attackmove_goaltried[tag]

    def do_attackmove(self):
        # cleanup
        if self.frame % 29 == 28:
            todel = set()
            for tag in self.attackmove_state:
                if tag not in self.all_unittags:
                    todel.add(tag)
            for tag in todel:
                del self.attackmove_state[tag]
        #
        for mar in self.units:
            martag = mar.tag
            if martag in self.attackmove_state:
                state = self.attackmove_state[martag]
                goal = self.attackmove_goal[martag]
                goalreached = self.attackmove_goalreached[martag]
                enetag = self.attackmove_enetag[martag]
                hangout = self.attackmove_hangout[martag]
                fightgoal = self.attackmove_fightgoal[martag]
                goaltried = self.attackmove_goaltried[martag]
                if goalreached:
                    tolerance = hangout
                else:
                    tolerance = 1
                if state == 'attack':
                    if martag in self.focus:
                        if enetag != self.focus[martag]:
                            enetag = self.focus[martag]
                            self.attackmove_enetag[martag] = enetag
                            for ene in self.enemy_units | self.enemy_real_structures:
                                if ene.tag == enetag:
                                    mar.attack(ene)
                            if martag in self.queuefocus:
                                queue_enetag = self.queuefocus[martag]
                                self.attackmove_queue_enetag[martag] = queue_enetag
                                for ene in self.enemy_units | self.enemy_real_structures:
                                    if ene.tag == queue_enetag:
                                        mar.attack(ene,queue=True)
                    else:
                        state = 'rest'
                else: # state != 'attack'
                    if martag in self.focus:
                        state = 'attack'
                        enetag = self.focus[martag]
                        self.attackmove_enetag[martag] = enetag
                        for ene in self.enemy_units | self.enemy_real_structures:
                            if ene.tag == enetag:
                                mar.attack(ene)
                        if martag in self.queuefocus:
                            queue_enetag = self.queuefocus[martag]
                            self.attackmove_queue_enetag[martag] = queue_enetag
                            for ene in self.enemy_units | self.enemy_real_structures:
                                if ene.tag == queue_enetag:
                                    mar.attack(ene, queue=True)
                if state != 'attack':
                    fpos = self.fightpos[martag]
                    if fpos == self.nowhere:
                        if state == 'approach':
                            state = 'rest'
                    else: # take fightpos
                        if not self.near(fpos,fightgoal,0.5):
                            mar.move(fpos)
                            self.attackmove_fightgoal[martag] = fpos
                        state = 'approach'
                if state == 'rest':
                    if self.near(mar.position, goal, tolerance):
                        self.attackmove_goalreached[martag] = True
                    else:
                        state = 'move'
                if state == 'move':
                    if self.near(mar.position, goal, tolerance):
                        state = 'rest'
                    elif martag in self.idles:
                        mar.move(goal)
                        self.attackmove_goaltried[martag] += 1
                        if self.attackmove_goaltried[martag] >= 4:
                            self.attackmove_goalreached[martag] = True
                if state != 'approach':
                    self.attackmove_fightgoal[martag] = self.nowhere
                self.attackmove_state[martag] = state

    def init_undetect(self):
        # called if enemy_structureinfo changed
        # all detector buildings have sight 11
        detectors = set() # set of positions of enemy detector buildings
        hash = 0
        for tpplus in self.enemy_structureinfo_plus:
            (typ, pos, finish) = tpplus
            if typ in self.antiair_detector:
                if finish < self.frame + 200: # finished, or within 8 sec
                    detectors.add(pos)
                    hash += pos.x
        if self.detect_hash != hash:
            self.detect_hash = hash
            self.detect = detectors
            self.lefttarget_righttarget()

    def undetect_ok(self, point) -> bool:
        ok = True
        for det in self.detect:
            if self.near(det, point, self.detection_range):
                ok = False
        return ok

    def undetect_point(self, around) -> Point2:
        # get a point near 'around' but probably without detection, probably in the map
        goal = around
        if (not self.undetect_ok(goal)):
            away = self.random_mappoint()
            while (not self.undetect_ok(away)):
                away = self.random_mappoint()
            tries = 0
            while (not self.undetect_ok(goal)) and (tries < 7):
                tries += 1
                for det in self.detect:
                    if self.near(det, goal, 1):
                        goal = goal.towards(away,1)
                    elif self.near(det, goal, self.detection_range):
                        goal = det.towards(goal,self.detection_range)
                        goal = self.into_map(goal)
            while (not self.undetect_ok(goal)) and (tries < 77):
                tries += 1
                goal = goal.towards(away,1)
            self.log_success('undetect pointimprovement was '+ self.txt(around)+' became '+self.txt(goal))
        return goal

    def kill_a_base(self, pos):
        # put a bunker near very weak bases
        around = pos.towards(self.map_center, -7)
        place = self.place_around(BUNKER, around)
        self.throw_at_spot(BUNKER,place,'kill_a_base')

    def init_vulture(self):
        # needs target_loc
        circleframes = 337
        self.vulture_pos = []
        self.make_circle(circleframes)
        for point in self.circle:
            self.vulture_pos.append(Point2((self.target_loc.x + 7 * point.x, self.target_loc.y + 7 * point.y)))

    def vulture(self):
        # needs init_vulture
        circleframes = 337
        if self.frame >= self.last_vulture_frame + 7:
            self.last_vulture_frame = self.frame
            self.vulture_pole = self.frame % circleframes
            goal = self.vulture_pos[self.vulture_pole]
            for bc in self.units(BATTLECRUISER):
                # gamestate gives emotion_of_unittag
                if self.emotion_of_unittag[bc.tag] == 'vulturing':
                    # high APM command not logged
                    bc.move(goal)

    def get_goal(self) -> Point2:
        # for marines
        allloc = []
        for tp in self.enemy_structureinfo:
            (typ,pos) = tp
            if typ in self.hall_types:
                allloc.append(pos)
        if len(allloc) == 0:
            for tp in self.enemy_structureinfo:
                (typ, pos) = tp
                allloc.append(pos)
        if len(allloc) == 0:
            goal = self.enemy_pos
        else:
            goal = random.choice(allloc)
        return goal


    async def marine_fun(self):
        if self.opening_name.find('marine') >= 0:
            # stimpack
            self.techsequence_starter = STIMPACK
            if self.marine_opening_bases >= 2:
                self.throw_treeno(BARRACKSTECHLAB, 'marine_fun')
                self.throw_treeno(STIMPACK, 'marine_fun')
            # marine weapon
            self.techsequence_starter = TERRANINFANTRYWEAPONSLEVEL1
            if self.marine_opening_bases >= 3:
                if self.vespene > 10:
                    self.throw_treeno(ENGINEERINGBAY, 'marine_fun')
                if self.we_started_a(ENGINEERINGBAY):
                    self.throw_treeno(TERRANINFANTRYWEAPONSLEVEL1, 'marine_fun')
            # combatshield
            self.techsequence_starter = SHIELDWALL
            if self.marine_opening_bases >= 4:
                self.throw_treeno(SHIELDWALL, 'marine_fun')
            # marine armor
            self.techsequence_starter = TERRANINFANTRYARMORSLEVEL1
            if self.marine_opening_bases >= 5:
                if self.we_started_a(ENGINEERINGBAY):
                    self.throw_treeno(TERRANINFANTRYARMORSLEVEL1, 'marine_fun')
            # tech-up after stimpack if surplus money
            self.techsequence = [REFINERY,REFINERY,FACTORY,STARPORT,FUSIONCORE,STARPORTTECHLAB,BATTLECRUISER]
            self.throw_techsequence()
            # start the attack
            if (self.opening_create_units <= self.marine_gather_time) or (self.supply_used >= 190):
                if not self.marine_gathered:
                    self.marine_gathered = True
                    self.marine_gatherframe = self.frame
                    # find an army gather point
                    self.marine_goal = self.loved_pos
                    while not self.near(self.marine_goal, self.map_center, 15):
                        around = self.random_mappoint()
                        self.marine_goal = self.place_around(ARMORY,around)
                    for mar in self.units(MARINE):
                        self.speciality_of_tag[mar.tag] = self.opening_name
                        self.attackmove(mar.tag,self.marine_goal,8)
                    # try agressive bunkers
                    for tp in self.enemy_structureinfo:
                        (typ, pos) = tp
                        if typ in self.hall_types:
                            self.kill_a_base(pos)
                    # keep some barracks
                    for bar in self.structures(BARRACKS):
                        if self.random_chance(4):
                            self.flown_in.add(bar.tag)
            # 60 sec of new marines are sent in too
            # builddura of a marine is 18 sec
            if self.frame % 7 == 6:
                if self.frame < self.marine_gatherframe + self.frames_per_second * 60:
                    for mar in self.units(MARINE):
                        if mar.tag not in self.speciality_of_tag:
                            self.attackmove(mar.tag, self.marine_goal, 8)
                            self.speciality_of_tag[mar.tag] = self.opening_name
            # set a new goal
            if self.frame % 19 == 18:
                reached = 0
                total = 0
                for mar in self.units(MARINE):
                    if mar.tag in self.speciality_of_tag:
                        total += 1
                        if self.near(mar.position,self.marine_goal,5):
                            reached += 1
                if reached * 6 > 5 * total:
                    self.marine_goal = self.get_goal()
                    for mar in self.units(MARINE):
                        if mar.tag in self.speciality_of_tag:
                            self.attackmove(mar.tag, self.marine_goal, 8)
                    if not self.marine_attacked:
                        self.marine_attacked = True
                        attackseconds = self.frame / self.frames_per_second
                        attacktime = str(round(attackseconds // 60))+':'+str(round(attackseconds % 60))
                        await self._client.chat_send('Attacktime ' + attacktime, team_only=True)
            # fly the barracks in
            if self.marine_gathered:
                for bar in self.structures(BARRACKS):
                    if bar.tag in self.readies:
                        if bar.tag in self.idles:
                            if not bar.has_add_on:
                                if bar.tag not in self.flown_in:
                                    self.flown_in.add(bar.tag)
                                    newplace = self.place_around(BARRACKS,self.enemy_pos)
                                    self.goal_of_flying_struct[bar.tag] = newplace
                                    self.write_layout(BARRACKS,newplace)
                                    self.landings_of_flying_struct[bar.tag] = 0
                                    self.log_success('up BARRACKS')
                                    self.log_command('bar(AbilityId.LIFT')
                                    bar(AbilityId.LIFT)

    def throw_techsequence(self):
        if self.frame % 13 == 12:
            former = self.techsequence_starter
            seqhad = []
            amseqhad = 0
            allformerdone = self.eggorbird(former)
            for next in self.techsequence:
                formerdone = (self.eggorbird_amount(former) >= amseqhad)
                allformerdone = allformerdone and formerdone
                if allformerdone:
                    # count next in seqhad
                    amseqhad = 0
                    for thing in seqhad:
                        if thing == next:
                            amseqhad += 1
                    if self.we_started_amount(next) < amseqhad+1:
                        self.throw_tree(next,'throw_techsequence')
                        print('                 throw_tree '+next.name)
                seqhad.append(next)
                amseqhad += 1
                former = next

    async def marauder_fun(self):
        if self.opening_name == 'marauder-3':
            self.techsequence_starter = ORBITALCOMMAND
            self.techsequence = [ENGINEERINGBAY,TERRANINFANTRYARMORSLEVEL1,STIMPACK,
                            PUNISHERGRENADES,TERRANINFANTRYWEAPONSLEVEL1,
                            ENGINEERINGBAY,ARMORY,TERRANINFANTRYARMORSLEVEL2,
                            FACTORY,TERRANINFANTRYWEAPONSLEVEL2,STARPORT,FUSIONCORE]
            self.throw_techsequence()
            # fly some barracks in
            if not self.marauder_retreat:
                if len(self.structures(BARRACKSFLYING)) == 0:
                    barsready = []
                    for bar in self.structures(BARRACKS):
                        if bar.tag in self.readies:
                            if bar.tag in self.idles:
                                barsready.append(bar.tag)
                    if len(barsready) > 0:
                        thisbar = random.choice(barsready)
                        for bar in self.structures(BARRACKS):
                            if bar.tag in self.readies:
                                if bar.tag == thisbar:
                                    newplace = self.place_around(BARRACKS,self.marauder_goal)
                                    self.goal_of_flying_struct[bar.tag] = newplace
                                    self.write_layout(BARRACKS,newplace)
                                    self.landings_of_flying_struct[bar.tag] = 0
                                    self.log_success('up BARRACKS')
                                    self.log_command('bar(AbilityId.LIFT')
                                    bar(AbilityId.LIFT)
            # a pf in the middle
            if self.we_started_a(PUNISHERGRENADES):
                if self.marauder_pf_phase == 0:
                    self.throw_at_spot(COMMANDCENTER,self.marauder_pf_spot,'marauder_fun')
                    self.marauder_pf_phase += 1
                elif self.marauder_pf_phase == 1:
                    for cc in self.structures(COMMANDCENTER):
                        if cc.position == self.marauder_pf_spot:
                            self.speciality_of_tag[cc.tag] = 'marauder_fun'
                            self.cc_destiny[cc.position] = 'pf'
                            self.marauder_pf_phase += 1
                elif self.marauder_pf_phase == 2:
                    for cc in self.structures(COMMANDCENTER):
                        if cc.tag in self.readies:
                            if cc.position == self.marauder_pf_spot:
                                if self.allow_throw(PLANETARYFORTRESS):
                                    self.throw_at_spot(PLANETARYFORTRESS, cc.position, 'marauder_fun')
                                    self.marauder_pf_phase += 1

    def random_mappoint(self) -> Point2:
        return Point2((random.randrange(self.map_left, self.map_right), random.randrange(self.map_bottom, self.map_top)))

    def into_map(self, rawpoint) -> Point2:
        x = rawpoint.x
        y = rawpoint.y
        if x < self.map_left:
            x = self.map_left
        if x >= self.map_right:
            x = self.map_right
        if y < self.map_bottom:
            y = self.map_bottom
        if y >= self.map_top:
            y = self.map_top
        return Point2((x,y))


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

    async def go_jump(self, bc,goal):
        bct = bc.tag
        self.goal_of_unittag[bct] = goal
        self.last_sd_of_unittag[bct] = 0
        self.shame_of_unittag[bct] = 0
        self.detour_of_unittag[bct] = False
        jumping = False
        close = self.near(bc.position,goal,75)
        veryclose = self.near(bc.position,goal,25)
        abilities = (await self.get_available_abilities([bc]))[0]
        if (AbilityId.EFFECT_TACTICALJUMP in abilities):
            if not veryclose:
                if (not close) or (bc.health < 150):
                    self.log_command('bc(AbilityId.EFFECT_TACTICALJUMP,goal)')
                    bc(AbilityId.EFFECT_TACTICALJUMP, goal)
                    jumping = True
                    self.log_army('jumping a bc')
        if not jumping:
            bc.move(goal)

    def no_move(self, bc,maxshame) -> bool:
        nomo = False
        tag = bc.tag
        goal = self.goal_of_unittag[tag]
        sd = self.sdist(bc.position, goal)
        if sd < self.last_sd_of_unittag[tag]:
            self.shame_of_unittag[tag] = max(0, self.shame_of_unittag[tag] - self.chosen_game_step)
        elif self.shame_of_unittag[tag] < maxshame:
            self.shame_of_unittag[tag] += self.chosen_game_step
        elif self.detour_of_unittag[tag]:
            if bc.tag in self.idles:
                self.log_command('bc.move(goal)')
                bc.move(goal)
                self.detour_of_unittag[tag] = False
                self.shame_of_unittag[tag] = 0
        else:
            nomo = True
        self.last_sd_of_unittag[tag] = sd
        return nomo

    def no_move_or_near(self, unt, maxshame, nearity) -> bool:
        # min nearity 0.001
        nomo = False
        tag = unt.tag
        goal = self.goal_of_unittag[tag]
        sd = self.sdist(unt.position, goal)
        if sd < nearity*nearity:
            nomo = True
        elif sd < self.last_sd_of_unittag[tag]:
            self.shame_of_unittag[tag] = max(0, self.shame_of_unittag[tag] - self.chosen_game_step)
        elif self.shame_of_unittag[tag] < maxshame:
            self.shame_of_unittag[tag] += self.chosen_game_step
        elif self.detour_of_unittag[tag]:
            if tag in self.idles:
                self.log_command('unt.move(goal)')
                unt.move(goal)
                self.detour_of_unittag[tag] = False
                self.shame_of_unittag[tag] = 0
        else:
            nomo = True
        self.last_sd_of_unittag[tag] = sd
        return nomo


    def write_enemy_structures(self):
        for tp in self.enemy_structureinfo:
            (typ,pos) = tp
            if tp not in self.last_enemy_structureinfo:
                self.write_layout(typ,pos)
        self.last_enemy_structureinfo = set()
        for tp in self.enemy_structureinfo:
            self.last_enemy_structureinfo.add(tp)

    def get_last_enemies(self):
        # collect positions for next step
        self.last_enemies = set()
        for ene in self.enemy_units: # actual visible
            self.last_enemies.add((ene.type_id,ene.position,ene.tag))

    def get_last_health(self):
        # collect health for next step
        for myn in self.units:
            self.last_health[myn.tag] = myn.health
        for myn in self.structures:
            self.last_health[myn.tag] = myn.health

    def make_trail(self):
        # per unit the trail of its last 10 movements positions 
        if self.frame % 13 == 12: # mark trail per half second
            for unt in self.units:
                if unt.type_id != SCV:
                    # init
                    if unt.tag not in self.trailtarget:
                        self.trailtarget[unt.tag] = self.nowhere
                        self.trailtargetframe[unt.tag] = self.frame
                        pos = unt.position
                        self.trailpo[unt.tag] = 0
                        self.trail[unt.tag] = [pos, pos, pos, pos, pos, pos, pos, pos, pos, pos]
                    # same order?
                    same_order = False
                    if len(unt.orders) == 1:
                        order = unt.orders[0]
                        if order.ability.id in {AbilityId.MOVE,AbilityId.ATTACK}:
                            if type(order.target) != int:
                                if self.trailtarget[unt.tag] == order.target:
                                    same_order = True
                    if same_order:
                        # skip first 3 seconds
                        if self.trailtargetframe[unt.tag] + 60 < self.frame:
                            trailpo = self.trailpo[unt.tag]
                            trailpo = (trailpo + 1) % 10
                            self.trail[unt.tag][trailpo] = unt.position
                            self.trailpo[unt.tag] = trailpo
                    else:
                        self.trailtarget[unt.tag] = self.nowhere
                        self.trailtargetframe[unt.tag] = self.frame
                        if len(unt.orders) == 1:
                            order = unt.orders[0]
                            if order.ability.id in {AbilityId.MOVE,AbilityId.ATTACK}:
                                if type(order.target) != int:
                                    self.trailtarget[unt.tag] = order.target
                                    self.trailtargetframe[unt.tag] = self.frame


    def close_to_a_my_base(self,pos) -> bool:
        clos = False
        for tow in self.all_bases:
            clos = clos or self.near(tow.position,pos,20)
        return clos

    def locally_improved(self,place) -> Point2:
        # verhoog quality met 1600 pogingen in de omgeving (maxdist 10)
        bestplace = place
        qual = self.quality_of_bc_position(place)
        for nx in range(-20,20):
            for ny in range(-20,20):
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
        # 0=bad, 1000= very good, >500 is acceptable
        # should be working blind too
        qual = 0
        if self.attack_type == 'center':
            if self.near(point,self.army_center_point,10):
                qual = 1000
        elif self.attack_type == 'arc':
            if self.near(point,self.enemy_pos,110) and (not self.near(point,self.enemy_pos,90)):
                qual = 1000
        elif self.attack_type == 'jumpy':
            # bc.radius+bc.ground_range+hatchery.radius  estimate
            if self.near(point,self.target_loc,10):
                qual = 1000
                for tpplus in self.enemy_structureinfo_plus:
                    (typ, pos, finish) = tpplus
                    if type in self.antiair_detector:
                        if self.near(point, pos, self.detection_range):
                            if finish < self.frame + 200: # finished or within 8 sec
                                qual -= 100
        return qual

    async def repair_bc(self):
        for bc in self.units(BATTLECRUISER):
            bct = bc.tag
            if self.emotion_of_unittag[bct] != 'bcrecovering':
                torep = (self.emotion_of_unittag[bct] not in ['frozen','vulturing']) and (bc.health <= self.bc_fear)
                torep = torep or (bc.health < 100)
                if torep:
                    dock = self.get_dock(bc.position)
                    if dock != self.hisleft:
                        self.emotion_of_unittag[bct] = 'bcrecovering'
                        await self.go_jump(bc,dock)
                        self.bc_fear = max(150, self.bc_fear - 10)
            if self.emotion_of_unittag[bct] == 'bcrecovering':
                # this emotion is partly a movement
                dock = self.goal_of_unittag[bct]
                if self.no_move(bc,64):
                    # it should be repaired. Found anomality, thus next code
                    close = self.near(bc.position, dock, 15)
                    if not close:
                        self.go_move(bc,dock)
                # keep the bc in the dock. Who is pulling it away?
                if self.near(bc.position,dock,12) and not self.near(bc.position,dock,3):
                    self.log_command('bc(AbilityId.MOVE_MOVE,dock)')
                    bc(AbilityId.MOVE_MOVE,dock)
                # redocking if few scvs near
                if self.near(bc.position,dock,3):
                    expo = self.expo_of_pos(dock)
                    if len(self.scvs_of_expo[expo]) < 3:
                        betterdock = self.get_dock(bc.position)
                        if betterdock != self.hisleft:
                            if betterdock != dock:
                                self.go_move(bc, betterdock)

    def arc_now(self):
        for bc in self.units(BATTLECRUISER):
            if self.quality_of_bc_position(bc.position) <= 500:
                bct = bc.tag
                if self.emotion_of_unittag[bct] != 'bcrecovering':
                    bestsd = 99999
                    for tries in range(0, 3):
                        tp = self.random_mappoint()
                        while self.quality_of_bc_position(tp) <= 500:
                            tp = self.random_mappoint()
                        sd = self.sdist(bc.position, tp)
                        if sd < bestsd:
                            bestsd = sd
                            besttp = tp
                    tp = besttp
                    self.log_command('bc.move(tp)')
                    bc.move(tp)

    def center_now(self):
        for bc in self.units(BATTLECRUISER):
            if self.quality_of_bc_position(bc.position) <= 500:
                bct = bc.tag
                if self.emotion_of_unittag[bct] != 'bcrecovering':
                    tp = self.army_center_point
                    self.log_command('bc.move(tp)')
                    bc.move(tp)

    async def attack_with_bc(self):
        if self.attack_type == 'jumpy':
            for bc in self.units(BATTLECRUISER):
                bct = bc.tag
                mytile = self.maptile_of_pos(bc.position)
                if bct not in self.eneunitsseen:
                    self.eneunitsseen[bct] = 200
                eneseen = False
                eunitsseen = False
                for tile in self.nine[mytile]:
                    for ene in self.enemies_of_tile[tile]:
                        if ene.type_id not in {LARVA,EGG,AUTOTURRET}:
                            # todo not cloacked. Warning: is_visible means something else.
                            if self.near(ene.position, bc.position, 7):
                                eneseen = True
                                if ene in self.enemy_units: # actual visible
                                    eunitsseen = True
                if eunitsseen:
                    self.eneunitsseen[bct] = 200 # satisfied for 10 seconds
                else:
                    self.eneunitsseen[bct] -= self.chosen_game_step
                antiairseen = False
                for tile in self.nine[mytile]:
                    for ene in self.enemies_of_tile[tile]:
                        if ene.type_id in self.antiair_detector:
                            antiairseen = True
                emotion = self.emotion_of_unittag[bct]
                self.log_unitorder(bc,emotion)
                # handle diverse possibilities
                if emotion == 'bcrecovering':
                    pass # it will be repaired
                elif emotion == 'lazy':
                    qual = 0
                    while qual <= 500:
                        place = self.random_mappoint()
                        qual = self.quality_of_bc_position(place)
                    place = self.locally_improved(place)
                    await self.go_jump(bc,place)
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
                    if self.eneunitsseen[bct] <= 0:
                        betterplaceseen = False
                        for tp in self.enemy_structureinfo:
                            (typ, pos) = tp
                            if typ in self.hall_types:
                                if not self.near(pos, bc.position, 10):
                                    betterplaceseen = True
                                    betterplace = pos
                        if betterplaceseen:
                            place = self.locally_improved(betterplace)
                            self.go_move(bc,place)
                            self.emotion_of_unittag[bct] = 'travels'
                    if not eneseen:
                        self.log_army('stop vulture, wander')
                        self.emotion_of_unittag[bct] = 'towander'
                    if antiairseen:
                        self.log_army('stop vulture, freeze')
                        self.log_command('bc(AbilityId.HOLDPOSITION_BATTLECRUISER)')
                        bc(AbilityId.HOLDPOSITION_BATTLECRUISER)
                        self.emotion_of_unittag[bct] = 'frozen'
                elif emotion == 'frozen':
                    if self.eneunitsseen[bct] <= 0:
                        betterplaceseen = False
                        for tp in self.enemy_structureinfo:
                            (typ, pos) = tp
                            if typ in self.hall_types:
                                if not self.near(pos, bc.position, 10):
                                    betterplaceseen = True
                                    betterplace = pos
                        if betterplaceseen:
                            place = self.locally_improved(betterplace)
                            self.go_move(bc,place)
                            self.emotion_of_unittag[bct] = 'travels'
                    if not eneseen:
                        self.log_army('unfreezing bc')
                        self.log_command('bc(AbilityId.STOP)')
                        bc(AbilityId.STOP)
                        self.emotion_of_unittag[bct] = 'towander'
                elif emotion == 'towander':
                    place = self.random_mappoint()
                    for tp in self.enemy_structureinfo:
                        (typ, pos) = tp
                        if typ in self.hall_types:
                            if not self.near(pos,bc.position,10):
                                place = pos
                    self.go_attack(bc,place)
                    self.emotion_of_unittag[bct] = 'wandering'
                elif emotion == 'wandering':
                    if self.no_move(bc,64):
                        self.emotion_of_unittag[bct] = 'towander'
        elif self.attack_type == 'chaos':
            tp = self.random_mappoint() # 3/5
            if self.random_chance(5): # 1/5
                if len(self.enemy_structureinfo) > 0:
                    (type, pos) = random.choice(tuple(self.enemy_structureinfo))
                    tp = pos
            elif self.random_chance(4): # 1/5
                stru = random.choice(tuple(self.structures))
                tp = stru.position
        elif self.attack_type == 'arc':
            for bc in self.units(BATTLECRUISER):
                if bc.tag in self.idles:
                    if self.quality_of_bc_position(bc.position) <= 500:
                        bestsd = 99999
                        for tries in range(0,3):
                            tp = self.random_mappoint()
                            while self.quality_of_bc_position(tp) <= 500:
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
            for bc in self.units(BATTLECRUISER):
                if bc.tag in self.idles:
                    if self.emotion_of_unittag[bc.tag] != 'bcrecovering':
                        if self.quality_of_bc_position(bc.position) <= 500:
                            self.log_command('bc.attack(tp)')
                            bc.attack(tp)
        #
        # attack_type changes
        it_changed = False
        if self.attack_type == 'jumpy':
            frozen_vulture_wander = 0
            for bct in self.emotion_of_unittag:
                if self.emotion_of_unittag[bct] in ['frozen','vulturing','wandering']:
                    frozen_vulture_wander += 1
            if (self.cruisercount<self.lastcruisercount) or (frozen_vulture_wander >= 4): # 3
                self.attack_type = 'chaos'
                self.log_army('spreading the army')
                await self.log_attacktype('spreading the army')
                it_changed = True
                self.bestbc_dist_to_goal = 99999
                for bc in self.units(BATTLECRUISER):
                    if self.emotion_of_unittag[bc.tag] == 'frozen':
                        self.log_command('bc(AbilityId.STOP)')
                        bc(AbilityId.STOP)
                    if self.emotion_of_unittag[bc.tag] != 'bcrecovering':
                        self.emotion_of_unittag[bc.tag] = 'lazy'
        elif self.attack_type == 'chaos':
            if self.supply_used >= 190:
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
                    self.demanded_groupup = False
        elif self.attack_type == 'arc':
            reached = 0
            total = 0
            for ar in self.units(BATTLECRUISER):
                total += 1
                if self.quality_of_bc_position(ar.position) > 500:
                    if ar in self.units(BATTLECRUISER):
                        if ar.tag in self.idles:
                            reached += 1
            if reached*2 > total:
                if not self.demanded_groupup:
                    self.arc_now()
                    self.demanded_groupup = True
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
                self.demanded_groupup = False
        elif self.attack_type == 'center':
            reached = 0
            total = 0
            for ar in self.units(BATTLECRUISER):
                total += 1
                if self.quality_of_bc_position(ar.position) > 500:
                    if ar in self.units(BATTLECRUISER):
                        if ar.tag in self.idles:
                            reached += 1
            if reached*2 > total:
                if not self.demanded_groupup:
                    self.center_now()
                    self.demanded_groupup = True
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
            for tp in self.enemy_structureinfo:
                (typ, pos) = tp
                if typ in self.hall_types:
                    allloc.append(pos)
            if len(allloc) == 0:
                for tp in self.enemy_structureinfo:
                    (typ, pos) = tp
                    allloc.append(pos)
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

    def lefttarget_righttarget(self):
        self.lefttarget = self.enemy_pos
        leftsd = 99999
        self.righttarget = self.enemy_pos
        rightsd = 99999
        for (typ, pos) in self.enemy_structureinfo:
            if typ in self.hall_types:
                sd = self.sdist(pos, self.hisleft)
                if sd < leftsd:
                    leftsd = sd
                    self.lefttarget = pos
                sd = self.sdist(pos, self.hisright)
                if sd < rightsd:
                    rightsd = sd
                    self.righttarget = pos
        # if no enemy hall known, attack enemy buildings
        if leftsd == 99999: # no enemy hall known
            for (typ, pos) in self.enemy_structureinfo:
                sd = self.sdist(pos, self.hisleft)
                if sd < leftsd:
                    leftsd = sd
                    self.lefttarget = pos
                sd = self.sdist(pos, self.hisright)
                if sd < rightsd:
                    rightsd = sd
                    self.righttarget = pos
        self.lefttarget = self.undetect_point(self.lefttarget)
        self.righttarget = self.undetect_point(self.righttarget)

    def sneakymid(self, comefrom,togoto) -> Point2:
        if self.near(comefrom, togoto, 5):
            mid = togoto
        else:
            dist = self.circledist(comefrom, togoto)
            mid = Point2((comefrom.x / 2 + togoto.x / 2, comefrom.y / 2 + togoto.y / 2))
            mid = mid.towards(self.map_center, -dist / 5)
            mid = self.into_map(mid)
            mid = self.undetect_point(mid)
            tries = 0
            while (tries < 17) and (not self.flystraight(comefrom,mid)):
                tries += 1
                mid = self.detect_improve
        return mid

    # viking squadrons

    def set_new_goal_for_squadron(self, squadron):
        if len(self.all_bases) > 0:
            bas = random.choice(self.all_bases)
            basp = bas.position
        else: # no base
            basp = self.loved_pos
        goal = Point2((basp.x + random.randrange(-20, 20), basp.y + random.randrange(-20, 20)))
        self.goal_of_squadron[squadron] = goal
        for vik in self.units(VIKINGFIGHTER):
            if self.squadron_of_viktag[vik.tag] == squadron:
                self.log_command('vik.attack(goal)')
                self.go_attack(vik, goal)
                self.emotion_of_unittag[vik.tag] = 'patrolling'

    def squadronize_vikings(self):
        # a squadron of vikings has an identification number, a position, a goalposition, a victimtag, a size
        # every viking has an emotion
        # a viking is (repairing or looking, with squadron -1)
        #          or (it is in a squadron >= 0)
        #          or (it is in squadron -2, the harasslanders).
        #
        # init size_of_squadron
        for squadron in {-2,-1}:
            if squadron not in self.size_of_squadron:
                self.size_of_squadron[squadron] = 0
        # new vikings
        for vik in self.units(VIKINGFIGHTER) + self.units(VIKINGASSAULT):
            if vik.tag not in self.emotion_of_unittag:
                self.emotion_of_unittag[vik.tag] = 'looking'
                self.squadron_of_viktag[vik.tag] = -1
                self.size_of_squadron[-1] += 1
                # wait 2 seconds, so a different  viking routine can pick it up
                self.waitframe_of_tag[vik.tag] = self.frame + 40
        # died vikings
        if self.frame % 19 == 18:
            squadronviks = 0
            for squadron in self.all_squadrons:
                squadronviks += self.size_of_squadron[squadron]
            viks = 0
            for vik in self.units(VIKINGFIGHTER) + self.units(VIKINGASSAULT):
                viks += 1
            if viks < squadronviks:
                todel = set()
                for squadron in self.all_squadrons:
                    size = 0
                    for vik in self.units(VIKINGFIGHTER) + self.units(VIKINGASSAULT):
                        if self.squadron_of_viktag[vik.tag] == squadron:
                            size += 1
                    self.size_of_squadron[squadron] = size
                    if (size == 0) and (squadron >= 0):
                        todel.add(squadron)
                self.all_squadrons -= todel
                self.normalsquadrons -= todel

    def landed_viking(self):
        # early harass
        # hijack one that is 'looking'.
        todo = 1 - self.size_of_squadron[-2]
        for vik in self.units(VIKINGFIGHTER) + self.units(VIKINGASSAULT):
            if self.emotion_of_unittag[vik.tag] == 'looking': # so squadron -1
                if todo > 0:
                    todo -= 1
                    self.squadron_of_viktag[vik.tag] = -2
                    self.size_of_squadron[-1] -= 1
                    self.size_of_squadron[-2] += 1
                    self.emotion_of_unittag[vik.tag] = 'start'
        for vik in self.units(VIKINGFIGHTER) + self.units(VIKINGASSAULT):
            if self.squadron_of_viktag[vik.tag] == -2:
                emotion = self.emotion_of_unittag[vik.tag]
                if emotion == 'start':
                    if vik in self.units(VIKINGASSAULT):
                        vik(AbilityId.MORPH_VIKINGFIGHTERMODE)
                        emotion = 'takeoff'
                        self.waitframe_of_tag[vik.tag] = self.frame + 45 # 2 sec
                    else:
                        emotion = 'targetting'
                elif emotion == 'takeoff':
                    if self.frame > self.waitframe_of_tag[vik.tag]:
                        emotion = 'targetting'
                elif emotion == 'targetting':
                    # find a position behind enemy lines
                    minsd = 99999
                    bestgoal = self.enemy_pos.towards(self.map_center,-8)
                    bestpos = self.enemy_pos
                    for tp in self.enemy_structureinfo:
                        (typ, pos) = tp
                        if pos != self.viking_last_att_pos:
                            if typ in self.hall_types:
                                goal = pos.towards(self.map_center,-8)
                                sd = self.sdist(vik.position,goal)
                                if sd < minsd:
                                    minsd = sd
                                    bestgoal = goal
                                    bestpos = pos
                    vik.move(bestgoal)
                    self.goal_of_unittag[vik.tag] = bestgoal
                    self.viking_last_att_pos = bestpos
                    emotion = 'inflying'
                elif emotion == 'inflying':
                    # finetuning
                    goal = self.goal_of_unittag[vik.tag]
                    if self.near(vik.position,goal,3):
                        goal = self.place_around(AUTOTURRET,goal) # can be on creep
                        self.goal_of_unittag[vik.tag] = goal
                        vik.move(goal)
                        emotion = 'positioning'
                elif emotion == 'positioning':
                    # start landing
                    goal = self.goal_of_unittag[vik.tag]
                    if vik in self.units(VIKINGFIGHTER):
                        if vik.tag in self.idles:
                            vik(AbilityId.MORPH_VIKINGASSAULTMODE)
                            emotion = 'landing'
                elif emotion == 'landing':
                    # end landing
                    if vik in self.units(VIKINGASSAULT):
                        emotion = 'landed'
                        self.waitframe_of_tag[vik.tag] = self.frame + 160 # 7 sec
                elif emotion == 'landed':
                    # stand or flee or bored
                    flee = False
                    if vik.tag in self.last_health:
                        if vik.health < self.last_health[vik.tag] - 11:
                            # being hit from afar or a building or 3 workers
                            flee = True
                    for ene in self.enemy_units:
                        dist = self.circledist(vik.position,ene.position)
                        if ene.type_id not in self.all_workertypes:
                            if ene.can_attack_ground:
                                if ene.ground_range > dist - 2:
                                    flee = True
                                    away = vik.position.towards(ene.position,-7)
                                    away = self.into_map(away)
                                    self.goal_of_unittag[vik.tag] = away
                    if flee:
                        vik(AbilityId.MORPH_VIKINGFIGHTERMODE)
                        emotion = 'fleetakeoff'
                        self.waitframe_of_tag[vik.tag] = self.frame + 45 # 2 sec
                    # bored?
                    elif vik.weapon_cooldown > 0:
                        self.waitframe_of_tag[vik.tag] = self.frame + 160 # 7 sec
                    elif self.frame >= self.waitframe_of_tag[vik.tag]:
                        emotion = 'boredtakeoff'
                        self.waitframe_of_tag[vik.tag] = self.frame + 45 # 2 sec
                elif emotion == 'boredtakeoff':
                    if self.frame >= self.waitframe_of_tag[vik.tag]:
                        emotion = 'targetting'
                elif emotion == 'fleetakeoff':
                    if self.frame >= self.waitframe_of_tag[vik.tag]:
                        emotion = 'flee'
                elif emotion == 'flee':
                    # run away
                    away = self.goal_of_unittag[vik.tag]
                    vik.move(away)
                    emotion = 'relax'
                    self.waitframe_of_tag[vik.tag] = self.frame + 160 # 7 sec
                elif emotion == 'relax':
                    # wait, if needed flee further
                    if vik in self.units(VIKINGFIGHTER):
                        if vik.tag in self.idles:
                            flee = False
                            for ene in self.enemy_units:
                                dist = self.circledist(vik.position,ene.position)
                                if ene.can_attack_air:
                                    if ene.air_range > dist - 2:
                                        flee = True
                                        away = vik.position.towards(ene.position,-7)
                                        away = self.into_map(away)
                            if flee:
                                vik.move(away)
                                self.waitframe_of_tag[vik.tag] = self.frame + 160 # 7 sec
                    if self.frame >= self.waitframe_of_tag[vik.tag]:
                        emotion = 'targetting'
                self.emotion_of_unittag[vik.tag] = emotion

    def fly_viking(self):
        # new viking gets a squadron; stop looking
        for vik in self.units(VIKINGFIGHTER):
            if self.emotion_of_unittag[vik.tag] == 'looking': # so squadron -1
                if self.frame >= self.waitframe_of_tag[vik.tag]:
                    bestsquadron = -1 # not a squadron
                    closest = 99999
                    for squadron in self.normalsquadrons:
                        sd = self.sdist(vik.position,self.pos_of_squadron[squadron])
                        if sd < closest:
                            closest = sd
                            bestsquadron = squadron
                    if closest < 80*80:
                        squadron = bestsquadron
                        self.squadron_of_viktag[vik.tag] = squadron
                        self.size_of_squadron[-1] -= 1
                        self.size_of_squadron[squadron] += 1
                        # init vik move
                        if self.victim_of_squadron[squadron] == self.notag:
                            goal = self.goal_of_squadron[squadron]
                            self.log_command('vik.attack(goal)')
                            self.go_attack(vik, goal)
                            self.emotion_of_unittag[vik.tag] = 'patrolling'
                        else: # has victim
                            self.emotion_of_unittag[vik.tag] = 'attacking'
                            for ene in self.enemy_units:  # actual visible
                                if ene.tag == self.victim_of_squadron[squadron]:
                                    self.log_command('vik.attack(ene)')
                                    vik.attack(ene)
                    else: # no squadron close
                        # new squadron
                        squadron = 0
                        while squadron in self.normalsquadrons:
                            squadron += 1
                        self.normalsquadrons.add(squadron)
                        self.all_squadrons.add(squadron)
                        self.squadron_of_viktag[vik.tag] = squadron
                        self.pos_of_squadron[squadron] = vik.position
                        self.victim_of_squadron[squadron] = self.notag
                        self.size_of_squadron[squadron] = 1
                        self.size_of_squadron[-1] -= 1
                        self.set_new_goal_for_squadron(squadron)
        # repaired viking
        if self.frame % 31 == 30:
            for vik in self.units(VIKINGFIGHTER):
                if self.squadron_of_viktag[vik.tag] == -1:
                    if self.emotion_of_unittag[vik.tag] == 'vik repairing':
                        if vik.health >= self.viking_good_health:
                            self.emotion_of_unittag[vik.tag] = 'looking'
                            self.waitframe_of_tag[vik.tag] = self.frame + 40
        # unhealthy vikings go repair
        for vik in self.units(VIKINGFIGHTER):
            if self.squadron_of_viktag[vik.tag] >= 0:
                if vik.health < self.viking_min_health:
                    self.emotion_of_unittag[vik.tag] = 'vik repairing'
                    squadron = self.squadron_of_viktag[vik.tag]
                    self.squadron_of_viktag[vik.tag] = -1
                    self.size_of_squadron[squadron] -= 1
                    self.size_of_squadron[-1] += 1
                    if self.size_of_squadron[squadron] == 0:
                        self.normalsquadrons.remove(squadron)
                        self.all_squadrons.remove(squadron)
                    dock = self.get_dock(vik.position)
                    self.log_command('vik.move(dock)')
                    vik.move(dock)
                    # and hope it will be repaired
        # forgotten vikings
        if self.frame % 11 == 10:
            for vik in self.units(VIKINGFIGHTER):
                if vik.tag in self.idles:
                    if self.squadron_of_viktag[vik.tag] == -1:
                        if self.emotion_of_unittag[vik.tag] == 'vik repairing':
                            if vik.tag in self.forgotten_vikings:
                                moment = self.forgotten_vikings[vik.tag]
                                if moment + 150 < self.frame:
                                    del self.forgotten_vikings[vik.tag]
                                    dock = self.get_dock(vik.position)
                                    self.log_command('vik.move(dock)')
                                    vik.move(dock)
                            else:
                                self.forgotten_vikings[vik.tag] = self.frame
        # pos_of_squadron
        if self.frame % 41 == 40:
            for squadron in self.normalsquadrons:
                px = 0
                py = 0
                n = 0
                for vik in self.units(VIKINGFIGHTER):
                    if self.squadron_of_viktag[vik.tag] == squadron:
                        px += vik.position.x
                        py += vik.position.y
                        n += 1
                if n > 0:
                    self.pos_of_squadron[squadron] = Point2((px / n, py / n))
        # new squadron goal
        if self.frame % 23 == 22:
            for squadron in self.normalsquadrons:
                if self.victim_of_squadron[squadron] == self.notag:
                    goal = self.goal_of_squadron[squadron]
                    size = self.size_of_squadron[squadron]
                    reached = 0
                    for vik in self.units(VIKINGFIGHTER):
                        if self.squadron_of_viktag[vik.tag] == squadron:
                            if self.no_move_or_near(vik,22,8):
                                reached += 1
                    if reached * 4 > 3 * size:
                        self.set_new_goal_for_squadron(squadron)
        # squadron victim cleaning
        if self.frame % 13 == 12:
            for squadron in self.normalsquadrons:
                if self.victim_of_squadron[squadron] != self.notag:
                    enetag = self.victim_of_squadron[squadron]
                    eneseen = False
                    for ene in self.enemy_units: # actual visible
                        if ene.tag == enetag:
                            eneseen = True
                    if not eneseen:
                        self.victim_of_squadron[squadron] = self.notag
                        self.set_new_goal_for_squadron(squadron)
        # squadron victim
        if self.frame % 11 == 10:
            for ene in self.enemy_units: # actual visible
                if ene.type_id in self.viking_targets:
                    if ene.tag not in self.victim_of_squadron:
                        bestsquadron = -1
                        closest = 99999
                        for squadron in self.normalsquadrons:
                            if self.victim_of_squadron[squadron] == self.notag:
                                sd = self.sdist(ene.position, self.pos_of_squadron[squadron])
                                if sd < closest:
                                    closest = sd
                                    bestsquadron = squadron
                        if closest < 120*120: # 100*100
                            # attack this enemy
                            squadron = bestsquadron
                            self.victim_of_squadron[squadron] = ene.tag
                            # bestdist_of_squadron
                            if ene.can_attack_air:
                                if ene.air_range < self.viking_air_range:
                                    self.bestdist_of_squadron[squadron] = (ene.air_range + self.viking_air_range) / 2
                                else:
                                    self.bestdist_of_squadron[squadron] = 0
                            else:
                                self.bestdist_of_squadron[squadron] = 0
                            self.victimpos_of_squadron[squadron] = ene.position
                            self.victimlastpos_of_squadron[squadron] = ene.position
                            # init attack
                            for vik in self.units(VIKINGFIGHTER):
                                if self.squadron_of_viktag[vik.tag] == squadron:
                                    self.log_command('vik.attack(ene)')
                                    vik.attack(ene)
                                    self.emotion_of_unittag[vik.tag] = 'attacking'
        # enemy tracking
        for squadron in self.normalsquadrons:
            if self.victim_of_squadron[squadron] != self.notag:
                ene_tag = self.victim_of_squadron[squadron]
                for ene in self.enemy_units:  # actual visible
                    if ene.tag == ene_tag:
                        self.victimlastpos_of_squadron[squadron] = self.victimpos_of_squadron[squadron]
                        self.victimpos_of_squadron[squadron] = ene.position
        # viking cooldown
        for vik in self.units(VIKINGFIGHTER):
            if self.emotion_of_unittag[vik.tag] == 'attacking':
                if vik.weapon_cooldown >= 5: # it shot
                    squadron = self.squadron_of_viktag[vik.tag]
                    if self.victim_of_squadron[squadron] != self.notag:
                        # go move
                        bestdist = self.bestdist_of_squadron[squadron]
                        ene_pos = self.victimpos_of_squadron[squadron]
                        ene_lastpos = self.victimlastpos_of_squadron[squadron]
                        ene_speedx = (ene_pos.x - ene_lastpos.x) / self.chosen_game_step
                        ene_speedy = (ene_pos.y - ene_lastpos.y) / self.chosen_game_step
                        ene_futpos = Point2((ene_pos.x + vik.weapon_cooldown * ene_speedx, ene_pos.y + vik.weapon_cooldown * ene_speedy))
                        self.emotion_of_unittag[vik.tag] = 'moving'
                        movepos = ene_futpos.towards(vik.position,bestdist)
                        movepos = self.undetect_point(movepos)
                        self.log_command('vik.move(movepos)')
                        vik.move(movepos)
                        self.movepos_of_viking[vik.tag] = movepos
            elif self.emotion_of_unittag[vik.tag] == 'moving':
                if vik.weapon_cooldown < 5: # can shoot
                    squadron = self.squadron_of_viktag[vik.tag]
                    ene_tag = self.victim_of_squadron[squadron]
                    if ene_tag == self.notag:
                        goal = self.goal_of_squadron[squadron]
                        self.log_command('vik.attack(goal)')
                        self.go_attack(vik, goal)
                        self.emotion_of_unittag[vik.tag] = 'patrolling'
                    else: # victim
                        for ene in self.enemy_units:  # actual visible
                            if ene.tag == ene_tag:
                                vik.attack(ene)
                                self.emotion_of_unittag[vik.tag] = 'attacking'
                else: # recalc movepos
                    squadron = self.squadron_of_viktag[vik.tag]
                    if self.victim_of_squadron[squadron] != self.notag:
                        # go move
                        bestdist = self.bestdist_of_squadron[squadron]
                        ene_pos = self.victimpos_of_squadron[squadron]
                        ene_lastpos = self.victimlastpos_of_squadron[squadron]
                        ene_speedx = (ene_pos.x - ene_lastpos.x) / self.chosen_game_step
                        ene_speedy = (ene_pos.y - ene_lastpos.y) / self.chosen_game_step
                        ene_futpos = Point2((ene_pos.x + vik.weapon_cooldown * ene_speedx, ene_pos.y + vik.weapon_cooldown * ene_speedy))
                        movepos = self.movepos_of_viking[vik.tag]
                        dist = self.circledist(ene_futpos,movepos)
                        if (dist < bestdist - 0.5) or (dist > bestdist + 0.5):
                            movepos = ene_futpos.towards(vik.position,bestdist)
                            self.log_command('vik.move(movepos)')
                            vik.move(movepos)
                            self.movepos_of_viking[vik.tag] = movepos

    def heal_bio(self, pos) -> bool:
        # self.thechosen will be a marine close to pos
        # only usable this frame
        found = False
        for kind in {MARINE,MARAUDER,GHOST,HELLIONTANK}:
            if not found:
                minsd = 99999
                for mar in self.units(kind):
                    sd = self.sdist(mar.position,pos)
                    if sd < minsd:
                        if mar.tag not in self.victim_of_medivac.values():
                            minsd = sd
                            self.thechosen = mar
                            found = True
        return found

    def support_a_bc(self,pos) -> bool:
        # self.thechosen will be a bc close to pos
        # only usable this frame
        found = False
        minsd = 99999
        for bc in self.units(BATTLECRUISER):
            sd = self.sdist(bc.position,pos)
            if sd < minsd:
                if bc.tag not in self.victim_of_raven.values():
                    minsd = sd
                    self.thechosen = bc
                    found = True
        return found

    async def attack_with_rest(self):
        self.standard_reapers()
        # ravens should follow(attack) a battlecruiser
        for rv in self.units(RAVEN):
            if rv.tag in self.idles:
                if rv.tag in self.thingtag_of_repairertag.values():
                    pass
                elif rv.tag not in self.victim_of_raven:
                    if self.support_a_bc(rv.position):
                        self.victim_of_raven[rv.tag] = self.thechosen.tag
                        rv.attack(self.thechosen)
                        self.log_army('raven will follow a bc')
                else:
                    problemtag = self.victim_of_raven[rv.tag]
                    # It jumped? It died? I did a turret?
                    seen = False
                    for bc in self.units(BATTLECRUISER):
                        if bc.tag == problemtag:
                            seen = True
                            rv.attack(bc)
                    if not seen:
                        # wait, then find a new victim.
                        if rv.tag in self.lostframe_of_raven:
                            lostframe = self.lostframe_of_raven[rv.tag]
                            if self.frame > lostframe + 60:
                                if self.support_a_bc(rv.position):
                                    self.victim_of_raven[rv.tag] = self.thechosen.tag
                                    rv.attack(self.thechosen)
                                    self.log_army('raven will follow a bc')
                        else:
                            self.lostframe_of_raven[rv.tag] = self.frame
        # medivacs should follow(attack) a marine
        for med in self.units(MEDIVAC):
            if med.tag not in self.speciality_of_tag:
                if med.tag in self.idles:
                    if med.tag in self.thingtag_of_repairertag.values():
                        pass
                    elif med.tag not in self.victim_of_medivac:
                        if self.heal_bio(med.position):
                            self.victim_of_medivac[med.tag] = self.thechosen.tag
                            med.attack(self.thechosen)
                            self.log_army('medivac will follow a marine')
                    else:
                        problemtag = self.victim_of_medivac[med.tag]
                        # died? entered a bunker? transformed to hellion? entered a medivac?
                        if self.heal_bio(med.position):
                            self.victim_of_medivac[med.tag] = self.thechosen.tag
                            med.attack(self.thechosen)
                            self.log_army('medivac will follow a marine')
        # vikings
        self.squadronize_vikings()
        self.fly_viking()
        self.landed_viking()
        # suicider scvs
        if self.count_of_job['suicider'] > 0:
            for scv in self.units(SCV):
                scvt = scv.tag
                if scvt in self.idles:
                    if self.job_of_scvt[scvt] == 'suicider':
                        place = self.random_mappoint()
                        self.log_command('scv.attack(place)')
                        scv.attack(place)
        # marines individual move
        for mar in self.units(MARINE):
            if mar.tag not in self.speciality_of_tag:
                if mar.tag not in bunker_if.marinetags:
                    tp = self.random_mappoint()
                    if (STIMPACK, self.nowhere) in self.birds:
                        if (mar.weapon_cooldown > 0):
                            if mar.health > 30: # 1.5(x-10)=x
                                if not mar.has_buff(BuffId.STIMPACK):
                                    mar(AbilityId.EFFECT_STIM_MARINE)
                    if mar.tag in self.idles:
                        self.attackmove(mar.tag, tp, 7)
                    if mar.tag in self.last_health:
                        if mar.health != self.last_health[mar.tag]:
                            altpos = mar.position.towards(self.loved_pos, 0.4)
                            self.log_command('mar.move(altpos)')
                            mar.move(altpos)
        # marine step forward if blocking another marine
        if self.frame % 11 == 10:
            for mar in self.units(MARINE):
                if (mar.weapon_cooldown > 0): # mar shot
                    mieppos = self.nowhere
                    expo = self.expo_of_pos(mar.position)
                    for miep in self.units_of_expo[expo]:
                        if miep.type_id == MARINE:
                            if self.near(miep.position,mar.position,1.5):
                                if miep.weapon_cooldown == 0: # miep didnt shoot
                                    mieppos = miep.position
                    if mieppos != self.nowhere:
                        togo = mar.position.towards(mieppos, -0.7)
                        mar.move(togo)
        # marauders groupmove
        if self.opening_name == 'marauder-3':
            wantradius = 10
        else:
            wantradius = 5
        # stim
        for mar in self.units(MARAUDER):
            if (STIMPACK, self.nowhere) in self.birds:
                if (mar.weapon_cooldown > 0):
                    if mar.health > 60: # 1.5(x-20)=x
                        if not mar.has_buff(BuffId.STIMPACKMARAUDER):
                            mar(AbilityId.EFFECT_STIM_MARAUDER)
        for mar in self.units(GHOST):
            if mar.tag in self.army_ghosts:
                if mar.tag not in self.ghostmove_state: # new army_ghost
                    self.ghostmove(mar.tag, self.marauder_goal, wantradius)
        reached = 0
        for mar in self.units(MARAUDER):
            if mar.tag not in self.attackmove_state: # new marauder
                self.attackmove(mar.tag,self.marauder_goal,wantradius)
            if self.near(mar.position,self.marauder_goal,wantradius):
                reached += 1
        if self.opening_name.find('marauders') >= 0:
            if (reached >= 3):
                for bun in self.structures(BUNKER):
                    if len(bun.passengers) > 0:
                        self.log_command('bun(AbilityId.UNLOADALL_BUNKER)')
                        bun(AbilityId.UNLOADALL_BUNKER)
                    else:
                        bun(AbilityId.EFFECT_SALVAGE)
            if (reached >= 5):
                self.marauder_goal = self.random_mappoint()
                allloc = []
                for tp in self.enemy_structureinfo:
                    (typ, pos) = tp
                    allloc.append(pos)
                if len(allloc) > 0:
                    self.marauder_goal = random.choice(allloc)
                self.log_army('marauder goal set')
                for mar in self.units(MARAUDER):
                    self.attackmove(mar.tag, self.marauder_goal,wantradius)
                for mar in self.units(MARINE):
                    self.attackmove(mar.tag, self.marauder_goal,wantradius)
        else: # general marauder action
            if reached * 4 > 3 * self.we_preppedetc_amount(MARAUDER):
                # new goal
                self.marauder_retreat = not self.marauder_retreat
                if self.marauder_retreat:
                    self.marauder_goal = self.marauder_restpoint
                else:
                    self.marauder_goal = self.random_mappoint()
                    if (self.random_chance(5)) or (reached >= 7):
                        allloc = []
                        for tp in self.enemy_structureinfo:
                            (typ, pos) = tp
                            allloc.append(pos)
                        if len(allloc) > 0:
                            self.marauder_goal = random.choice(allloc)
                self.log_army('marauder goal set')
                for mar in self.units(MARAUDER):
                    self.attackmove(mar.tag, self.marauder_goal,wantradius)
                for mar in self.units(GHOST):
                    if mar.tag in self.army_ghosts:
                        self.ghostmove(mar.tag, self.marauder_goal, wantradius)
        # cyclones
        # NOT ACTION-MINIMIZED
        for cyc in self.units(CYCLONE):
            cyct = cyc.tag
            if cyct not in self.emotion_of_unittag:
                self.emotion_of_unittag[cyct] = 'resting'
                await self._client.toggle_autocast([cyc],AbilityId.LOCKON_LOCKON)
                self.unlockframe_of_cyclonetag[cyct] = 0
        # cyclones have side L or R
        sidecount = {}
        sidecount['L'] = 0
        sidecount['R'] = 0
        for cyc in self.units(CYCLONE):
            cyct = cyc.tag
            if cyct in self.side_of_unittag:
                sidecount[self.side_of_unittag[cyct]] += 1
        for cyc in self.units(CYCLONE):
            cyct = cyc.tag
            if cyct not in self.side_of_unittag:
                if sidecount['L'] < sidecount['R']:
                    self.side_of_unittag[cyct] = 'L'
                    sidecount['L'] += 1
                elif sidecount['L'] == sidecount['R']:
                    if self.random_chance(2):
                        self.side_of_unittag[cyct] = 'L'
                        sidecount['L'] += 1
                    else:
                        self.side_of_unittag[cyct] = 'R'
                        sidecount['R'] += 1
                else:
                    self.side_of_unittag[cyct] = 'R'
                    sidecount['R'] += 1
        # left_building_target and right_building_target
        left_building_exists = False
        left_building_target_pos = self.enemy_pos
        bestsd = 99999
        for tp in self.enemy_structureinfo:
            (typ,pos) = tp
            sd = self.sdist(pos,self.hisleft)
            if sd < bestsd:
                bestsd = sd
                left_building_target_pos = pos
                left_building_exists = True
        right_building_exists = False
        right_building_target_pos = self.enemy_pos
        bestsd = 99999
        for tp in self.enemy_structureinfo:
            (typ,pos) = tp
            sd = self.sdist(pos,self.hisright)
            if sd < bestsd:
                bestsd = sd
                right_building_target_pos = pos
                right_building_exists = True
        #
        for cyc in self.units(CYCLONE):
            cyct = cyc.tag
            #await self.debug(cyc)
            if self.no_doubling(cyct):
                if self.emotion_of_unittag[cyct] == 'resting':
                    side = self.side_of_unittag[cyct]
                    if side == 'L':
                        exists = left_building_exists
                        target_pos = left_building_target_pos
                    else:
                        exists = right_building_exists
                        target_pos = right_building_target_pos
                    if exists:
                        self.go_attack(cyc,target_pos)
                        self.emotion_of_unittag[cyct] = 'attacking'
                elif self.emotion_of_unittag[cyct] == 'attacking':
                    if self.no_move(cyc,120):
                        self.emotion_of_unittag[cyct] = 'resting'
                    if cyc.weapon_cooldown > 0: # it shot
                        if self.frame >= self.unlockframe_of_cyclonetag[cyct] + 100: # cooldown of lock
                            mytile = self.maptile_of_pos(cyc.position)
                            tolock = None
                            max_power = 0
                            for tile in self.nine[mytile]:
                                for ene in self.enemies_of_tile[tile]:
                                    if ene.type_id not in self.all_workertypes:
                                        if self.near(cyc.position, ene.position, 10):
                                            power = self.unit_power(ene.type_id)
                                            #print('cyclone sees '+ene.type_id.name+' power '+str(power))
                                            if power > max_power:
                                                tolock = ene
                                                max_power = power
                            if max_power > 0:
                                self.log_success('locking a '+tolock.type_id.name)
                                self.victimtag_of_unittag[cyct] = tolock.tag
                                bestpos = tolock.position.towards(cyc.position,10)
                                if cyct in self.trail:
                                    bestdist = 99999
                                    for tp in range(0, 10):
                                        pos = self.trail[cyct][tp]
                                        dist = abs(self.circledist(pos, tolock.position) - 10)
                                        if dist < bestdist:
                                            bestdist = dist
                                            bestpos = pos
                                cyc.move(bestpos) # run away
                                cyc(AbilityId.LOCKON_LOCKON,tolock) # start lockon
                                self.emotion_of_unittag[cyct] = 'locking'
                                #self.slowdown_frames = 30
                            else: # no enemy in sight
                                self.emotion_of_unittag[cyct] = 'retreating'
                                self.go_move(cyc, cyc.position.towards(self.loved_pos, 6))
                        else: # in cooldown
                            self.emotion_of_unittag[cyct] = 'retreating'
                            self.go_move(cyc,cyc.position.towards(self.loved_pos, 6))
                elif self.emotion_of_unittag[cyct] == 'retreating':
                    if (cyc.health < self.last_health[cyct]) or (cyc.weapon_cooldown > 0):
                        self.go_move(cyc, cyc.position.towards(self.loved_pos, 6))
                    if self.no_move(cyc,40):
                        self.emotion_of_unittag[cyct] = 'resting'
                elif self.emotion_of_unittag[cyct] == 'locking':
                    abilities = (await self.get_available_abilities([cyc]))[0]
                    if AbilityId.CANCEL_LOCKON in abilities:
                        self.emotion_of_unittag[cyct] = 'locked'
                    if AbilityId.LOCKON_LOCKON in abilities:
                        # how did the lockon fail?
                        self.emotion_of_unittag[cyct] = 'resting'
                elif self.emotion_of_unittag[cyct] == 'locked':
                    self.unlockframe_of_cyclonetag[cyct] = self.frame
                    mytile = self.maptile_of_pos(cyc.position)
                    abilities = (await self.get_available_abilities([cyc]))[0]
                    if AbilityId.CANCEL_LOCKON not in abilities:
                        self.emotion_of_unittag[cyct] = 'resting'
                    enepos = self.nowhere
                    enethreat = False
                    for tile in self.nine[mytile]:
                        for ene in self.enemies_of_tile[tile]:
                            if ene.tag == self.victimtag_of_unittag[cyct]:
                                enepos = ene.position
                            if self.near(ene.position,cyc.position,7):
                                enethreat = True
                                threatpos = ene.position
                    calc_pos = cyc.position
                    if enepos != self.nowhere:
                        calc_pos = enepos.towards(cyc.position, 10)
                    if enethreat:
                        calc_pos = cyc.position.towards(threatpos,-3)
                    bestsd = 99999
                    bestpos = calc_pos
                    if cyct in self.trail:
                        for tp in range(0,10):
                            pos = self.trail[cyct][tp]
                            sd = self.sdist(pos,calc_pos)
                            if sd < bestsd:
                                bestsd = sd
                                bestpos = pos
                    if bestpos != cyc.position:
                        cyc.move(bestpos)
        # banshees
        if len(self.banshee_right) > len(self.units(BANSHEE)):
            # cleanup lost banshees
            todel = set()
            for tag in self.banshee_right:
                seen = False
                for ban in self.units(BANSHEE):
                    if ban.tag == tag:
                        seen = True
                if not seen:
                    todel.add(tag)
            for tag in todel:
                del self.banshee_right[tag]
                del self.fearframe_of_banshee[tag]
        # per banshee
        if len(self.biles) == 0: # else the dodging will be done by other code
            for ban in self.units(BANSHEE):
                banpos = ban.position
                if ban.tag not in self.fearframe_of_banshee:
                    # init
                    self.lefttarget_righttarget()
                    self.emotion_of_unittag[ban.tag] = 'resting'
                    leftminusright = 0
                    for rba in self.banshee_right:
                        if rba:
                            leftminusright -= 1
                        else:
                            leftminusright += 1
                    if leftminusright < 0:
                        self.banshee_right[ban.tag] = False
                    elif leftminusright > 0:
                        self.banshee_right[ban.tag] = True
                    else:
                        if self.sdist(banpos,self.hisleft) < self.sdist(banpos,self.hisright):
                            self.banshee_right[ban.tag] = False
                        else:
                            self.banshee_right[ban.tag] = True
                    self.fearframe_of_banshee[ban.tag] = 0
                # goal
                if self.banshee_right[ban.tag]:
                    goal = self.righttarget
                else:
                    goal = self.lefttarget
                if self.detect_hash != self.detect_old_hash:
                    self.detect_old_hash = self.detect_hash
                    goal = self.undetect_point(goal)
                emo = self.emotion_of_unittag[ban.tag]
                mytile = self.maptile_of_pos(banpos)
                # cloack and uncloack
                for tile in self.nine[mytile]:
                    for ene in self.enemies_of_tile[tile]:
                        if self.air_strength(ene) > 0:
                            if self.near(ene.position,banpos,10):
                                self.fearframe_of_banshee[ban.tag] = self.frame
                if ban.tag in self.last_health:
                    if ban.health < self.last_health[ban.tag]:
                        self.fearframe_of_banshee[ban.tag] = self.frame
                if ban.is_cloaked:
                    if self.fearframe_of_banshee[ban.tag] + 300 < self.frame:
                        ban(AbilityId.BEHAVIOR_CLOAKOFF_BANSHEE)
                else:
                    if self.fearframe_of_banshee[ban.tag] + 50 >= self.frame:
                        if ban.energy >= 40:
                            if self.we_finished_a(BANSHEECLOAK):
                                ban(AbilityId.BEHAVIOR_CLOAKON_BANSHEE)
                #
                # being scanned
                for effect in self.state.effects:
                    if effect.id == EffectId.SCANNERSWEEP:
                        for effectpos in effect.positions:
                            if self.near(effectpos,banpos,13.5): # scanrange + 0.5
                                if self.banshee_right[ban.tag]:
                                    ban.move(self.hisright)
                                else:
                                    ban.move(self.hisleft)
                                emo = 'fleeing' # banshee
                                self.shame_of_unittag[ban.tag] = 100
                #
                if emo == 'resting':
                    start = True
                    if self.we_started_a(BANSHEECLOAK):
                        start = False
                    for (thing,pos) in self.birds:
                        if thing == BANSHEECLOAK:
                            start = True
                    for (thing,bartype,pos,upgdura) in self.eggs:
                        if thing == BANSHEECLOAK:
                            flightdura = 0.17 * (self.circledist(banpos,goal) - 10)
                            if upgdura < flightdura:
                                start = True
                    for (kind,am) in self.opening_create:
                        if (kind == BANSHEE):
                            start = False
                    for (thing,bartype,pos,upgdura) in self.eggs:
                        if thing == BANSHEE:
                            start = False
                    if start:
                        mid = self.sneakymid(banpos,goal)
                        self.go_move(ban, mid)
                        emo = 'approaching'
                elif emo == 'approaching':
                    if self.no_move_or_near(ban, 8, 4):
                        if self.near(banpos,goal,1):
                            emo = 'near'
                            ban.move(goal)
                        else:
                            mid = self.sneakymid(banpos, goal)
                            self.go_move(ban, mid)
                elif emo == 'near':
                    if self.near(banpos,goal,0.5):
                        emo = 'reached'
                        ban(AbilityId.HOLDPOSITION)
                elif emo == 'reached':
                    if not self.near(banpos,goal,0.5):
                        ban.move(goal)
                    if ban.energy < 15: # cloack runs low
                        if self.fearframe_of_banshee[ban.tag] + 200 >= self.frame: # if it has fear
                            if self.banshee_right[ban.tag]:
                                ban.move(self.hisright)
                            else:
                                ban.move(self.hisleft)
                            emo = 'refresh'
                elif emo == 'refresh':
                    flightdura = 0.17 * (self.circledist(banpos, goal) - 10)
                    if ban.energy + flightdura >= 70:
                        emo = 'resting'
                elif emo == 'fleeing': # banshee
                    if ban.energy < 15:
                        # cloack runs low
                        if self.banshee_right[ban.tag]:
                            ban.move(self.hisright)
                        else:
                            ban.move(self.hisleft)
                        emo = 'refresh'
                    elif self.shame_of_unittag[ban.tag] <= 0:
                        emo = 'resting'
                    else:
                        self.shame_of_unittag[ban.tag] -= self.chosen_game_step
                self.emotion_of_unittag[ban.tag] = emo



    def back_first_step(self, tag) -> Point2:
        if tag in self.trailpo:  # and thus in trail
            trailpo = self.trailpo[tag]
            po = (10 + trailpo - 1) % 10
            self.preferred_trailnr[tag] = po
            back = self.trail[tag][po]
        else:
            back = self.loved_pos
            self.preferred_trailnr[tag] = 0
        return back

    def back_step(self, tag) -> Point2:
        trailnr = self.preferred_trailnr[tag]  # exists per hurt cleaning_tank
        trailnr = (10 + trailnr - 1) % 10
        self.preferred_trailnr[tag] = trailnr
        if tag in self.trailpo:  # and thus in trail
            back = self.trail[tag][trailnr]
        else:
            back = self.loved_pos
        return back

    async def siege_tanks(self):
        tanks = len(self.units(SIEGETANK)) + len(self.units(SIEGETANKSIEGED))
        # cleaning_tank duty: suppose no enemy units and kill the nearest enemy structure.
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
        if len(self.cleaning_tank_tags) < 2:
            if tanks > len(self.cleaning_tank_tags) + 1: # reserve 1 tank for other plans
                todo = 1
                for tnk in self.units(SIEGETANK):
                    tnkt = tnk.tag
                    if tnkt not in self.speciality_of_tag:
                        if todo > 0:
                            todo -= 1
                            self.cleaning_tank_tags.add(tnkt)
                            self.speciality_of_tag[tnkt] = 'cleaner'
                            self.emotion_of_unittag[tnkt] = 'enthousiast'
                            self.prevent_doubling(tnkt)
                for tnk in self.units(SIEGETANKSIEGED):
                    tnkt = tnk.tag
                    if tnkt not in self.speciality_of_tag:
                        if todo > 0:
                            todo -= 1
                            self.cleaning_tank_tags.add(tnkt)
                            self.speciality_of_tag[tnkt] = 'cleaner'
                            self.log_command('tnk(AbilityId.UNSIEGE_UNSIEGE)')
                            tnk(AbilityId.UNSIEGE_UNSIEGE)
                            self.emotion_of_unittag[tnkt] = 'enthousiast'
                            self.prevent_doubling(tnkt)
        if len(self.cleaning_tank_tags) > 0:
            # check cleaning_object
            if self.cleaning_object_found:
                seen = False
                for tp in self.enemy_structureinfo:
                    (typ, pos) = tp
                    if pos == self.cleaning_object_pos:
                        seen = True
                if not seen:
                    self.cleaning_object_found = False
            # get cleaning_object
            if not self.cleaning_object_found:
                atnkpos = self.loved_pos
                for tnk in self.units(SIEGETANK) + self.units(SIEGETANKSIEGED):
                    if tnk.tag in self.cleaning_tank_tags:
                        atnkpos = tnk.position
                minsd = 99999
                for tp in self.enemy_structureinfo:
                    (typ, pos) = tp
                    sd = self.sdist(pos, atnkpos)
                    if sd < minsd:
                        minsd = sd
                        self.cleaning_object_found = True
                        self.cleaning_object_pos = pos
            # cleaning tanks
            if self.cleaning_object_found:
                for tnk in self.units(SIEGETANK):
                    tnkt = tnk.tag
                    if tnkt in self.idles:
                        if tnkt in self.cleaning_tank_tags:
                            if self.emotion_of_unittag[tnkt] == 'fighting':
                                if (tnk.health < self.last_health[tnkt]) or (tnk.weapon_cooldown > 0):
                                    self.cleaning_tank_back[tnkt] = self.back_step(tnkt)
                                    backpoint = tnk.position.towards(self.cleaning_tank_back[tnkt],2)
                                    self.log_command('tnk.move(backpoint)')
                                    tnk.move(backpoint)
                                else: # stopped fighting
                                    self.log_command('tnk(AbilityId.SIEGEMODE_SIEGEMODE)')
                                    tnk(AbilityId.SIEGEMODE_SIEGEMODE)
                                    # start boredness timer
                                    self.cleaning_tank_shotframe[tnkt] = self.frame + 60 # some siegingtime
                                    self.emotion_of_unittag[tnkt] = 'sieged'
                            if self.emotion_of_unittag[tnkt] == 'enthousiast':
                                # get siegepos
                                around = self.cleaning_object_pos.towards(self.loved_pos,10)
                                siegepos = self.place_around(AUTOTURRET, around)
                                self.cleaning_tank_siegepos[tnkt] = siegepos
                                # Mark as used.
                                self.write_layout(MISSILETURRET, siegepos)
                                self.tankplaces.add(siegepos)
                                # go there
                                self.log_command('tnk.attack(siegepos)')
                                self.go_attack(tnk, siegepos)
                                self.emotion_of_unittag[tnkt] = 'approaching'
                            if self.emotion_of_unittag[tnkt] == 'approaching':
                                if self.no_move_or_near(tnk, 280, 0.1):
                                    if tnk.weapon_cooldown == 0:
                                        self.log_command('tnk(AbilityId.SIEGEMODE_SIEGEMODE)')
                                        tnk(AbilityId.SIEGEMODE_SIEGEMODE)
                                        # start boreness timer
                                        self.cleaning_tank_shotframe[tnkt] = self.frame + 60 # some siegingtime
                                        self.emotion_of_unittag[tnkt] = 'sieged'
                for tnk in self.units(SIEGETANK):
                    tnkt = tnk.tag
                    if tnkt in self.cleaning_tank_tags:
                        # log
                        #stri = self.emotion_of_unittag[tnkt]
                        #self.log_unitorder(tnk,stri)
                        # starting a fight
                        if tnkt in self.last_health:
                            if (tnk.health < self.last_health[tnkt]) or (tnk.weapon_cooldown > 0):
                                self.emotion_of_unittag[tnkt] = 'backabit'
                                self.cleaning_tank_back[tnkt] = self.back_first_step(tnkt)
                                backpoint = tnk.position.towards(self.cleaning_tank_back[tnkt], 2)
                                self.log_command('tnk.move(backpoint)')
                                tnk.move(backpoint)
                                self.prevent_doubling(tnkt)
                        if self.emotion_of_unittag[tnkt] == 'backabit':
                            moves = 0
                            for order in tnk.orders:
                                if order.ability.id == AbilityId.MOVE:
                                    moves += 1
                                else:
                                    moves = 99999
                            if moves == 1:
                                self.emotion_of_unittag[tnkt] = 'fighting'
                for tnk in self.units(SIEGETANKSIEGED):
                    tnkt = tnk.tag
                    if tnkt in self.cleaning_tank_tags:
                        #stri = self.emotion_of_unittag[tnkt]
                        #self.log_unitorder(tnk,stri)
                        if self.emotion_of_unittag[tnkt] == 'sieged':
                            if tnk.weapon_cooldown > 0:
                                self.cleaning_tank_shotframe[tnkt] = self.frame
                            shotframe = self.cleaning_tank_shotframe[tnkt]
                            if shotframe + 222 < self.frame: # some 10 seconds no shot
                                self.log_command('tnk(AbilityId.UNSIEGE_UNSIEGE)')
                                tnk(AbilityId.UNSIEGE_UNSIEGE)
                                self.emotion_of_unittag[tnkt] = 'enthousiast'
        #
        # siege tank at a random own base
        for tnk in self.units(SIEGETANK) + self.units(SIEGETANKSIEGED):
            if tnk.tag not in self.speciality_of_tag:
                tnkt = tnk.tag
                expo = self.expo_of_pos(tnk.position)
                if tnkt not in self.emotion_of_unittag:
                    if (self.opening_name == 'liberator-tank'):
                        self.emotion_of_unittag[tnkt] = 'waiting'
                        self.shame_of_unittag[tnkt] = 0
                    else:
                        self.emotion_of_unittag[tnkt] = 'dream'
                elif self.emotion_of_unittag[tnkt] == 'waiting':
                    self.shame_of_unittag[tnkt] += self.chosen_game_step
                    if (len(self.units(LIBERATORAG)) > 0) \
                            or (self.shame_of_unittag[tnkt] >= 800)  or (len(self.units(BATTLECRUISER)) > 0):
                        self.emotion_of_unittag[tnkt] = 'dream'
                elif self.emotion_of_unittag[tnkt] == 'dream':
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
                    elif len(self.all_mine_bases) == 0:
                        goal = self.loved_pos
                    else:
                        tow = random.choice(self.all_mine_bases)
                        # halfheartedly prevent all tanks in startbase
                        if tow.position == self.loved_pos:
                            tow = random.choice(self.all_mine_bases)
                        # at first base, protect wall, at other bases, protect the tank
                        if tow.position == self.loved_pos:
                            goal = self.homeramp_pos.towards(self.loved_pos, 12)
                        else:
                            goal = tow.position.towards(self.map_center, -3)
                    place = self.place_around(AUTOTURRET,goal)
                    # Mark as used.
                    self.write_layout(AUTOTURRET, place)
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
                    for cc in self.all_mine_bases:
                        if self.near(tnk.position, cc.position, self.miner_bound):
                            hasbase = True
                    hasmins = False
                    for (mimpos,mimt) in self.minerals_of_expo[expo]:
                        if self.near(tnk.position, mimpos, 16):
                            hasmins = True
                    if not (hasbase and hasmins):
                        if not self.proxy(tnk.position):
                            self.log_command('tnk(AbilityId.UNSIEGE_UNSIEGE)')
                            tnk(AbilityId.UNSIEGE_UNSIEGE)
                            self.emotion_of_unittag[tnkt] = 'unsieging'
                elif self.emotion_of_unittag[tnkt] == 'unsieging':
                    if tnk in self.units(SIEGETANK):
                        self.emotion_of_unittag[tnkt] = 'dream'

    def cluster_the_mines(self):
        mines = len(self.units(WIDOWMINE)) + len(self.units(WIDOWMINEBURROWED))
        wantclussize = round(0.7 * sqrt(mines))
        # mines   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
        # cluss   0 1 1 1 1 2 2 2 2 2  2  2  2  3  3  3  3  3  3  3  3
        clustered = 0
        for cluster in self.clusters:
            clustered += self.size_of_cluster[cluster]
        # lost and new mines:
        if mines != clustered:
            toplace = set()
            for cluster in self.clusters:
                self.size_of_cluster[cluster] = 0
            for wm in self.units(WIDOWMINE) | self.units(WIDOWMINEBURROWED):
                wmt = wm.tag
                if wmt in self.cluster_of_mine:
                    cluster = self.cluster_of_mine[wmt]
                    self.size_of_cluster[cluster] += 1
                else:
                    toplace.add(wmt)
            for cluster in self.clusters:
                while (self.size_of_cluster[cluster] < wantclussize) and (len(toplace) > 0):
                    wmt = toplace.pop()
                    self.cluster_of_mine[wmt] = cluster
                    self.size_of_cluster[cluster] += 1
            while (len(toplace) > 0):
                cluster = 0
                while cluster in self.clusters:
                    cluster = random.randrange(0,100)
                self.clusters.add(cluster)
                self.size_of_cluster[cluster] = 0
                while (self.size_of_cluster[cluster] < wantclussize) and (len(toplace) > 0):
                    wmt = toplace.pop()
                    self.cluster_of_mine[wmt] = cluster
                    self.size_of_cluster[cluster] += 1
            todel = set()
            for cluster in self.clusters:
                if self.size_of_cluster[cluster] == 0:
                    todel.add(cluster)
            self.clusters -= todel


    def use_cluster(self):
        for cluster in self.clusters:
            if cluster in self.goal_of_cluster:
                # maybe move the cluster
                clugoal = self.goal_of_cluster[cluster]
                owning = False
                for cc in self.all_mine_bases:
                    if self.near(cc.position,clugoal,2):
                        owning = True
                if owning:
                    del self.goal_of_cluster[cluster]
            if cluster not in self.goal_of_cluster:
                points = set()
                for expopoint in self.expansion_locations:
                    point = expopoint.towards(self.map_center, -1)
                    if self.proxy(point):
                        expo = self.expo_of_pos(point)
                        owning = False
                        for cc in self.all_mine_bases:
                            if self.near(cc.position,point,2):
                                owning = True
                        if not owning:
                            hasclu = False
                            for clu in self.clusters:
                                if clu in self.goal_of_cluster:
                                    clugoal = self.goal_of_cluster[clu]
                                    if expo == self.expo_of_pos(clugoal):
                                        hasclu = True
                            if not hasclu:
                                points.add(point)
                if len(points) == 0:
                    for (mimpos,mimt) in self.all_minerals:
                        if self.proxy(mimpos):
                            point = mimpos.towards(self.map_center, -1)
                            points.add(point)
                if len(points) == 0:
                    for (mimpos,mimt) in self.all_minerals:
                        point = mimpos.towards(self.map_center, -1)
                        points.add(point)
                if len(points) == 0:
                    points.add(self.random_mappoint())
                # try to avoid cannons and spores
                bestquality = -99999
                tries = 0
                while (tries < 20):
                    tries += 1
                    point = random.choice(tuple(points))
                    quality = 1000
                    for tp in self.enemy_structureinfo_plus:
                        (typ, pos, finish) = tp
                        if typ in self.antiair_detector:
                            if finish < self.frame + 200: # finished or within 8 sec
                                if self.near(point,pos,7): # hit
                                    quality -= 100
                                if self.near(point,pos,11): # see
                                    quality -= 10
                    for clu in self.clusters:
                        if clu in self.goal_of_cluster:
                            clugoal = self.goal_of_cluster[clu]
                            if self.near(clugoal,point,7):
                                quality -=1
                    if quality > bestquality:
                        bestquality = quality
                        bestpoint = point
                self.goal_of_cluster[cluster] = bestpoint


    def use_widowmine(self):
        for wm in self.units(WIDOWMINE):
            wmt = wm.tag
            if wmt not in self.speciality_of_tag:
                mytile = self.maptile_of_pos(wm.position)
                nearenemies = False
                for tile in self.nine[mytile]:
                    for ene in self.enemies_of_tile[tile]:
                        if ene.can_attack_ground:
                            if self.ground_strength(ene) > 15:  # worker strength
                                if self.near(ene.position, wm.position, 8):
                                    nearenemies = True
                #
                if wmt not in self.emotion_of_unittag:
                    self.emotion_of_unittag[wmt] = 'lazy'
                if self.emotion_of_unittag[wmt] == 'lazy':
                    if wmt in self.cluster_of_mine:
                        cluster = self.cluster_of_mine[wmt]
                        if cluster in self.goal_of_cluster:
                            goal = self.goal_of_cluster[cluster]
                            self.go_move(wm,goal)
                            self.emotion_of_unittag[wmt] = 'marching'
                if self.emotion_of_unittag[wmt] == 'marching':
                    dying = False
                    if wmt in self.last_health:
                        if (wm.health < self.last_health[wmt]):
                            dying = True
                    if dying or nearenemies:
                        self.emotion_of_unittag[wmt] = 'scared'
                        back = self.back_first_step(wmt)
                        backpoint = wm.position.towards(back, 3)
                        self.go_move(wm,backpoint)
                    if self.no_move_or_near(wm, 100, 1):
                        self.log_command('wm(AbilityId.BURROWDOWN_WIDOWMINE)')
                        wm(AbilityId.BURROWDOWN_WIDOWMINE)
                        self.emotion_of_unittag[wmt] = 'settled'
                        self.mine_burried[wmt] = self.frame
                        if self.near(wm.position,self.goal_of_unittag[wmt],5):
                            self.emotion_of_unittag[wmt] = 'settled'
                        else:
                            self.emotion_of_unittag[wmt] = 'lodging'
                            self.solve_blockade(wm.position)
                if self.emotion_of_unittag[wmt] == 'scared':
                    if self.no_move_or_near(wm, 100, 1):
                        self.log_command('wm(AbilityId.BURROWDOWN_WIDOWMINE)')
                        wm(AbilityId.BURROWDOWN_WIDOWMINE)
                        self.emotion_of_unittag[wmt] = 'lodging'
                        self.mine_burried[wmt] = self.frame
        for wm in self.units(WIDOWMINEBURROWED):
            wmt = wm.tag
            if wmt not in self.speciality_of_tag:
                mytile = self.maptile_of_pos(wm.position)
                nearenemies = False
                for tile in self.nine[mytile]:
                    for ene in self.enemies_of_tile[tile]:
                        if ene.can_attack_ground:
                            if self.ground_strength(ene) > 15:  # worker strength
                                if self.near(ene.position, wm.position, 8):
                                    nearenemies = True
                #
                if wmt not in self.emotion_of_unittag:
                    self.emotion_of_unittag[wmt] = 'lodging'
                    self.mine_burried[wmt] = self.frame
                if self.emotion_of_unittag[wmt] == 'lodging':
                    if self.frame > self.mine_burried[wmt] + 350: # some 15 sec
                        if wmt in self.idles:
                            if not nearenemies:
                                static_stopper = False
                                for tp in self.enemy_structureinfo: # remembered info
                                    (typ, pos) = tp
                                    if typ in {PLANETARYFORTRESS,PHOTONCANNON,SPINECRAWLER,BUNKER}:
                                        if self.near(pos,wm.position,11):
                                            static_stopper = True
                                if not static_stopper:
                                   self.log_command('wm(AbilityId.BURROWUP_WIDOWMINE)')
                                   wm(AbilityId.BURROWUP_WIDOWMINE)
                                   self.emotion_of_unittag[wmt] = 'lazy'
                if self.emotion_of_unittag[wmt] == 'settled':
                    # changing clustergoals
                    if wmt in self.cluster_of_mine:
                        cluster = self.cluster_of_mine[wmt]
                        if cluster in self.goal_of_cluster:
                            clustergoal = self.goal_of_cluster[cluster]
                            minegoal = self.goal_of_unittag[wmt]
                            if minegoal != clustergoal:
                                if wmt in self.idles:
                                    if not nearenemies:
                                        self.log_command('wm(AbilityId.BURROWUP_WIDOWMINE)')
                                        wm(AbilityId.BURROWUP_WIDOWMINE)
                                        self.emotion_of_unittag[wmt] = 'lazy'



    def solve_blockade(self, position):
        for dep in self.structures(SUPPLYDEPOT):
            if self.near(dep.position,position,5):
                self.log_command('dep(AbilityId.MORPH_SUPPLYDEPOT_LOWER)')
                dep(AbilityId.MORPH_SUPPLYDEPOT_LOWER)
                self.log_success('lowering around blockade')
        for tnk in self.units(SIEGETANKSIEGED):
            if self.near(tnk.position, position, 5):
                self.log_success('Move tank around blockade')
                self.log_command('tnk(AbilityId.UNSIEGE_UNSIEGE)')
                tnk(AbilityId.UNSIEGE_UNSIEGE)
                if self.find_tobuildwalk_a_place(MISSILETURRET,'now'):
                    goal = self.function_result_Point2
                    self.go_move(tnk, goal)
                    self.emotion_of_unittag[tnk.tag] = 'moving'
                    self.tankplaces.add(goal)


    async def bc_micro(self):
        for bc in self.units(BATTLECRUISER):
            expo = self.expo_of_pos(bc.position)
            mytile = self.maptile_of_pos(bc.position)
            emotion = self.emotion_of_unittag[bc.tag]
            if emotion not in ['bcrecovering','travels','finetuning']:
                # get targets and dangersum
                hatemax = 0
                dangersum = 0
                targets = set()
                for tile in self.nine[mytile]:
                    for ene in self.enemies_of_tile[tile]:
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
        for ra in self.units(RAVEN):
            poop = False
            if ra.tag in self.last_health:
                if self.last_health[ra.tag] > ra.health:
                    poop = True
                    pooppos = ra.position
            mytile = self.maptile_of_pos(ra.position)
            goodfound = False
            badfound = False
            for tile in self.nine[mytile]:
                for ene in self.enemies_of_tile[tile]:
                    badfound = True
                    badtarget = ene
                    kind = ene.type_id
                    if kind in self.bcenemies:
                        if self.hate_of_bcenemy[kind] >= 4:
                            if self.near(ene.position,ra.position,10):
                                target = ene
                                goodfound = True
                                poop = True
                                pooppos = target.position.towards(ra.position, 6)
            if (ra.energy > 190) and (not goodfound) and (badfound):
                poop = True
                pooppos = badtarget.position.towards(ra.position, 6)
            # but not if not yet dropped, unless 4 sec past
            if ra.tag in self.energy_of_unittag: # then it is also in wait-of_unittag
                if ra.energy > self.energy_of_unittag[ra.tag]: # turret not delivered
                    if self.frame < self.wait_of_unittag[ra.tag]: # valid only some seconds
                        poop = False
            if poop:
                pooppos = self.place_around(AUTOTURRET, pooppos)
                abilities = (await self.get_available_abilities([ra]))[0]
                if AbilityId.BUILDAUTOTURRET_AUTOTURRET in abilities:
                    self.log_command('ra(AbilityId.BUILDAUTOTURRET_AUTOTURRET, pooppos)')
                    ra(AbilityId.BUILDAUTOTURRET_AUTOTURRET, pooppos)
                    self.energy_of_unittag[ra.tag] = ra.energy - 10
                    self.wait_of_unittag[ra.tag] = self.frame + 100
                #if AbilityId.EFFECT_ANTIARMORMISSILE in abilities:
                #    self.log_command('ra(AbilityId.EFFECT_ANTIARMORMISSILE,'+target.name+')')
                #    ra(AbilityId.EFFECT_ANTIARMORMISSILE, target)


    async def dodge_bile(self):
        # delete old biles
        # ignore the possibility of multiple biles at the same spot
        todel = set()
        for (pos,landframe) in self.bile_landframe:
            if self.frame > landframe:
                todel.add((pos,landframe))
        for (pos,landframe) in todel:
            self.biles.remove(pos)
        self.bile_landframe -= todel
        # new biles
        for effect in self.state.effects:
            if effect.id == EffectId.RAVAGERCORROSIVEBILECP:
                for bileposition in effect.positions:
                    if bileposition not in self.biles:
                        self.biles.add(bileposition)
                        self.bile_landframe.add((bileposition,self.frame + 60))
        # dodge biles
        for bileposition in self.biles:
            for kind in self.all_army:
                if kind not in {SIEGETANKSIEGED,LIBERATORAG,WIDOWMINEBURROWED}:
                    for bc in self.units(kind):
                        mustflee = False
                        if self.near(bileposition,bc.position,3):
                            mustflee = True
                            abile = bileposition
                        if mustflee:
                            topoint = self.flee(bc.position,3.2)
                            while self.near(abile,topoint,3):
                                topoint = self.flee(bc.position, 3.2)
                            self.log_command('bc(AbilityId.MOVE_MOVE,topoint)')
                            bc(AbilityId.MOVE_MOVE,topoint)

    def eval_libspots(self):
        # sometimes check the spots for known dangers and usefulness
        for spot in self.liberator_spots:
            name = spot[0]
            tail = Point2((2 * spot[2].x - spot[1].x, 2 * spot[2].y - spot[1].y))
            tail = self.into_map(tail)
            nose = Point2((1.5 * spot[1].x - 0.5 * spot[2].x, 1.5 * spot[1].y - 0.5 * spot[2].y))
            nose = self.into_map(nose)
            tailtile = self.maptile_of_pos(tail)
            noseexpo = self.expo_of_pos(nose)
            taildanger = 0
            for tile in self.nine[tailtile]:
                for ene in self.enemies_of_tile[tile]:
                    if self.near(ene.position, tail, 10):
                        enetype = ene.type_id
                        if (enetype in self.bcenemies):
                            taildanger += self.danger_of_bcenemy[enetype]
            thisspotlove = 0
            for tp in self.enemy_structureinfo_of_expo[noseexpo]:
                (typ,pos) = tp
                if typ in self.hall_types:
                    thisspotlove += 100
            self.spotlove[name] = thisspotlove - taildanger

    def liberator(self):
        for lib in self.units(LIBERATOR):
            if lib.tag in self.libspot:
                spot = self.libspot[lib.tag]
                oldname = spot[0]
                if self.frame % 9 == 8:
                    self.eval_libspots()
                    bestlove = self.spotlove[oldname]
                    bestname = oldname
                    bestspot = spot
                    tries = 0
                    while (tries < 9):
                        tries += 1
                        spot = random.choice(tuple(self.liberator_spots))
                        name = spot[0]
                        love = self.spotlove[name]
                        if love > bestlove:
                            bestlove = love
                            bestname = name
                            bestspot = spot
                    if bestname != oldname:
                        spot = bestspot
                        self.libspot[lib.tag] = bestspot
                        mid = self.sneakymid(lib.position,bestspot[2])
                        self.go_move(lib, mid)
                if self.no_move_or_near(lib, 8, 0.1):
                    lspot = self.libspot[lib.tag]
                    if self.near(lib.position,lspot[2],2):
                        lib(AbilityId.MORPH_LIBERATORAGMODE,lspot[1])
                    else:
                        self.go_move(lib,lspot[2])
                    # fly factory out
                    if self.opening_name.find('liberator-') >= 0:
                        for fac in self.structures(FACTORY) + self.structures(FACTORYFLYING):
                            if fac.tag in self.readies:
                                if fac.tag == self.lib_factory_tag:
                                    self.goal_of_flying_struct[fac.tag] = self.cheese1_factory_pos
                                    # now, will it move there?
                                    if fac in self.structures(FACTORY):
                                        self.landings_of_flying_struct[fac.tag] = 0
                                        self.log_success('up FACTORY')
                                        self.log_command('fac(AbilityId.LIFT')
                                        fac(AbilityId.LIFT)
            else: # get spot
                self.eval_libspots()
                bestlove = -99999
                tries = 0
                while (tries < 9):
                    tries += 1
                    spot = random.choice(tuple(self.liberator_spots))
                    name = spot[0]
                    love = self.spotlove[name]
                    if love > bestlove:
                        bestlove = love
                        bestname = name
                        bestspot = spot
                spot = bestspot
                if self.opening_name.find('liberator-') >= 0:
                    if (self.enemy_species != 'zerg') and (self.firstlib):
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
                mid = self.sneakymid(lib.position,spot[2])
                self.go_move(lib, mid)
                if self.firstlib:
                    self.firstlib = False
                    self.secondlib = True
                elif self.secondlib:
                    self.secondlib = False
        if self.opening_name.find('liberator-') >= 0:
            # fly proxy factory in
            flightdura = 1 + self.circledist(self.cheese1_factory_pos,self.cheese1_landing_pos) / 1.3
            for (martype,bartype,pos,dura) in self.eggs:
                if (martype == LIBERATOR) and (dura < flightdura):
                    for fac in self.structures(FACTORY):
                        if fac.tag in self.readies:
                            if fac.position == self.cheese1_factory_pos:
                                self.lib_factory_tag = fac.tag
                                self.goal_of_flying_struct[fac.tag] = self.cheese1_landing_pos
                                self.landings_of_flying_struct[fac.tag] = 0
                                self.log_success('up FACTORY')
                                self.log_command('fac(AbilityId.LIFT')
                                fac(AbilityId.LIFT)
        if self.opening_name == 'liberator-tank':
            for (martype,bartype,pos,dura) in self.eggs:
                if (martype == LIBERATOR) and (dura < 8):
                    for scv in self.units(SCV):
                        if scv.tag == self.scout1_tag:
                            self.scout1_tag = -2 # prevent immediate reassign
                            self.promote(scv,'idler')
                            scv.move(self.cheese1_landing_pos)
                            self.throw_at_spot(BUNKER,self.cheese1_landing_pos,'liberator-tank')
        for lib in self.units(LIBERATORAG):
            if lib.tag in self.libspot:
                spot = self.libspot[lib.tag]
                oldname = spot[0]
                if self.frame % 107 == 106:
                    self.eval_libspots()
                    bestlove = self.spotlove[oldname]
                    bestname = oldname
                    bestspot = spot
                    tries = 0
                    while (tries < 9):
                        tries += 1
                        spot = random.choice(tuple(self.liberator_spots))
                        name = spot[0]
                        love = self.spotlove[name]
                        if love > bestlove:
                            bestlove = love
                            bestname = name
                            bestspot = spot
                    if bestname != oldname:
                        spot = bestspot
                        self.libspot[lib.tag] = bestspot
                        lib(AbilityId.MORPH_LIBERATORAAMODE)
        somesieged = False
        for lib in self.units(LIBERATORAG):
            somesieged = True
            if self.lib_turpos == self.nowhere:
                self.lib_turpos = lib.position.towards(self.loved_pos, 2)
                self.lib_turpos = self.place_around(MISSILETURRET, self.lib_turpos)
        if somesieged:
            if self.lib_turret_tries > 0:
                if not self.we_started_at(MISSILETURRET,self.lib_turpos):
                    thrown = False
                    for tps in self.throwspots:
                        (th, po, status, ow) = tps
                        if ow == 'liberator':
                            thrown = True
                    if not thrown:
                        self.throw_at_spot(MISSILETURRET,self.lib_turpos,'liberator')
                        self.lib_turret_tries -= 1
            # redirect attack to natural if any
            for (martype, bartype, pos, dura) in self.eggs:
                if (martype == BATTLECRUISER) and (dura < 10):
                    nat_used = False
                    for tp in self.enemy_structureinfo:
                        (typ, pos) = tp
                        if pos == self.enemynatural_pos:
                            nat_used = True
                    if nat_used:
                        if self.target_loc != self.enemynatural_pos:
                            self.log_army('change target_loc to enemy natural')
                            self.target_loc = self.enemynatural_pos
                            self.init_vulture()
        else: # none sieged
            # retract the plan of building a missileturret
            todel = set()
            for tps in self.throwspots:
                (th, po, status, ow) = tps
                if (ow == 'liberator'):
                    todel.add(tps)
                    while (th, po, ow) in self.dreams:
                        del self.dreams[self.dreams.index((th, po, ow))]
            for tps in todel:
                del self.throwspots[self.throwspots.index(tps)]
                # del evt trabu
                (th, po, status, ow) = tps
                if status == 'prep':
                    for scv in self.units(SCV):
                        scvt = scv.tag
                        if scvt in self.goal_of_trabu_scvt:
                            if (self.goal_of_trabu_scvt[scvt] == po) and (self.structure_of_trabu_scvt[scvt] == th):
                                if self.job_of_scvt[scvt] in {'traveller','settler'}:
                                    self.promote(scv, 'idler')
                                    del self.goal_of_trabu_scvt[scvt]
                                    del self.structure_of_trabu_scvt[scvt]
        # if the factory flies home for repair, leave it there
        for fac in self.structures(FACTORY) + self.structures(FACTORYFLYING):
            if fac.tag in self.readies:
                if fac.tag == self.lib_factory_tag:
                    if not self.proxy(fac.position):
                        if self.goal_of_flying_struct[fac.tag] == self.cheese1_factory_pos:
                            if self.find_tobuildwalk_a_place(FACTORY,'now'):
                                spot = self.function_result_Point2
                                self.goal_of_flying_struct[fac.tag] = spot
                                self.write_layout(FACTORY,spot)

    def set_rallypoint(self,goal):
        # give goal a rallypoint (if it doesnt have one)
        rally = goal.towards(self.map_center, 2)
        seen = False
        for (pos, ralpos) in self.set_rally:
            seen = seen or (pos == goal)
        if not seen:
            self.set_rally.add((goal, rally))

    def do_rally(self):
        # effect the rallys planned in set_rally as soon as the rallying building is ready
        todel = set()
        for (buipos,ralpos) in self.set_rally:
            for bui in self.structures:
                if bui.tag in self.readies:
                    if bui.position == buipos: # this excludes labs
                        if bui.type_id not in self.landable:
                            done = False
                            for tar in self.structures:
                                if tar.position == ralpos:
                                    bui(AbilityId.RALLY_BUILDING,tar)
                                    done = True
                            if not done:
                                bui(AbilityId.RALLY_BUILDING,ralpos)
                            todel.add((buipos,ralpos))
        self.set_rally -= todel

    def unit_power(self,thing) -> int:
        # estimate of fighting power
        cost = self.get_total_cost(thing)
        power = cost.minerals+2*cost.vespene
        return power

    def clean_speciality_of_tag(self, stri):
        todel =set()
        for tag in self.speciality_of_tag:
            if self.speciality_of_tag[tag] == stri:
                todel.add(tag)
        for tag in todel:
            del self.speciality_of_tag[tag]

    async def worker_defence(self):
        if self.opening_name == 'immediate_fight':
            if self.workerrushstate != 'ended':
                # test the 'fighter' job by a primitive workerrush
                # slow
                if (self.frame > 1500) and (self.frame < 1500 + 20):
                    self.slowdown_frames = self.workerrushstopframe - 1500
                # end
                if self.frame > self.workerrushstopframe:
                    self.workerrushstate = 'ended'
                    for scv in self.units(SCV):
                        scvt = scv.tag
                        if self.job_of_scvt[scvt] == 'fighter':
                            self.promote(scv,'idler')
                # start
                if self.workerrushstate == 'tobe':
                    if len(self.structures) > 1: # after starting depot
                        self.workerrushstate = 'busy'
                if self.workerrushstate == 'busy':
                    miners = 0
                    fighters = 0
                    for myscv in self.units(SCV):
                        scvt = myscv.tag
                        job = self.job_of_scvt[scvt]
                        if (job == 'mimminer'):
                            miners += 1
                        elif (job == 'fighter'):
                            fighters += 1
                    if (miners > 6) and (self.frame < self.workerrushstopframe - 1000):
                        todo = 1
                        for myscv in self.units(SCV):
                            scvt = myscv.tag
                            job = self.job_of_scvt[scvt]
                            if (job not in self.good_jobs):
                                if todo > 0:
                                    todo -= 1
                                    self.promote(myscv,'fighter')
                                    self.home_of_fighter[scvt] = self.loved_pos
        else: # normal
            for tow in self.all_mine_bases:
                if tow.tag not in self.speciality_of_tag:
                    expo = self.expo_of_pos(tow.position)
                    # calc enemies and enemy_power
                    enemies = set() # set of pos
                    enemy_power = 0
                    cx = 0
                    cy = 0
                    n_enemies = 0
                    for ene in self.enemy_units_of_expo[expo]:
                        if not ene.is_flying:
                            if (tow.position == self.loved_pos) or (self.near(ene.position,tow.position,12)):
                                enemies.add(ene.position)
                                enemy_power += self.unit_power(ene.type_id)
                                cx = cx + ene.position.x
                                cy = cy + ene.position.y
                                n_enemies += 1
                    for tp in self.enemy_structureinfo_of_expo[expo]:
                        (typ,pos) = tp
                        enemies.add(pos)
                        enemy_power += self.unit_power(typ)
                        cx = cx + pos.x
                        cy = cy + pos.y
                        n_enemies += 1
                    if n_enemies > 0:
                        center_enemies = Point2((cx / n_enemies, cy / n_enemies))
                        # use 1 gamestep lookahead
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
                        if self.purpose[tow.tag] == 'scv':
                            if tow.type_id in {ORBITALCOMMAND,COMMANDCENTER}:
                                self.log_cc('Hall '+str(tow.tag)+' '+ self.txt(tow.position) + ' wishes to fly because of many enemies.')
                                if tow in self.structures(ORBITALCOMMAND):
                                    self.purpose[tow.tag] = 'fly'
                                elif tow in self.structures(COMMANDCENTER):
                                    self.purpose[tow.tag] = 'wishtofly'
                                if len(self.all_bases) < 2:
                                    toplace = random.choice(self.expansion_locations)
                                    self.goal_of_flying_struct[tow.tag] = toplace
                                    self.landings_of_flying_struct[tow.tag] = 0
                    else: #defend
                        if len(enemies) == 1:
                            wished_fighters = enemy_power/50 + 1
                        elif len(enemies) > 0:
                            wished_fighters = enemy_power/50 + 2
                        else:
                            wished_fighters = 0
                        # calc fighters
                        fighters = set()
                        for myscv in self.scvs_of_expo[expo]:
                            scvt = myscv.tag
                            job = self.job_of_scvt[scvt]
                            if (job == 'fighter'):
                                fighters.add(myscv)
                        # get new fighters
                        toget = wished_fighters - len(fighters)
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
                                # promote to fighter and let idle
                                toget -= 1
                                self.promote(myscv,'fighter')
                                self.home_of_fighter[scvt] = tow.position
                        if (len(fighters) > wished_fighters) or (len(enemies) == 0):
                            # dismiss some fighters
                            todel = len(fighters) - wished_fighters
                            if len(enemies) == 0:
                                todel = len(fighters)
                            for myscv in fighters:
                                if (todel > 0):
                                    todel -= 1
                                    self.promote(myscv,'idler')
                                    self.log_command('myscv.move(tow.position)')
                                    myscv.move(tow.position)
                        # We have the fighters. Now what will they do? See self.fighters()

    def calc_outnumber(self, mypos) -> int:
        # (own units at dist < 2) - (hisunits at dist < 2)
        outnumber = 0
        mytile = self.maptile_of_pos(mypos)
        for tile in self.nine[mytile]:
            for myn in self.goodguys_of_tile[tile]:
                if self.near(mypos, myn.position, 2):
                    outnumber += 1
            for ene in self.enemies_of_tile[tile]:
                if self.near(mypos, ene.position, 2):
                    if not ene.is_flying:
                        if ene.type_id not in {LARVA,EGG,AUTOTURRET}:
                            if ene not in self.enemy_real_structures:
                                outnumber -= 1
        return outnumber

    def calculate_enecenter(self,mypos) -> Point2:
        # get close enemies
        enemies = set()
        mytile = self.maptile_of_pos(mypos)
        for tile in self.nine[mytile]:
            for ene in self.enemies_of_tile[tile]:
                if ene.type_id not in {LARVA, EGG, AUTOTURRET}:
                    if self.near(mypos, ene.position, 7):
                        if not ene.is_flying:
                            enemies.add(ene.position)
        # if no close enemies, get any enemies
        if len(enemies) == 0:
            for ene in self.enemy_units:
                if not ene.is_flying:
                    if ene.type_id not in {LARVA, EGG, AUTOTURRET}:
                        enemies.add(ene.position)
        # make sure there is something
        if len(enemies) == 0:
            enemies.add(self.enemy_pos)
        # calculate enemy center, weigh close ones extra
        weightsum = 0
        cx = 0
        cy = 0
        for enepos in enemies:
            sd = self.sdist(mypos, enepos)
            weight = 1 / (sd + 0.1)
            weightsum += weight
            cx += weight * enepos.x
            cy += weight * enepos.y
        enecenter = Point2((cx / weightsum, cy / weightsum))
        return enecenter

    def check_walk(self,mytag,mypos,topos):
        # topos should be dist 2 from mypos
        mid = Point2((0.5*mypos.x+0.5*topos.x,0.5*mypos.y+0.5*topos.y))
        can = self.canstandon(mid)
        mytile = self.maptile_of_pos(mid)
        for tile in self.nine[mytile]:
            for ene in self.enemies_of_tile[tile]:
                if self.near(mid, ene.position, 1):
                    if not ene.is_flying:
                        can = False
            for myn in self.goodguys_of_tile[tile]:
                if self.near(mid, myn.position, 1):
                    if myn.tag != mytag:
                        can = False
        return can

    def fighters(self):
        # for scvs with job 'fighter', sensible individual actions
        #
        homeexpos = set()
        for scv in self.units(SCV):
            scvt = scv.tag
            if self.job_of_scvt[scvt] == 'fighter':
                home = self.home_of_fighter[scvt]
                homeexpo = self.expo_of_pos(home)
                homeexpos.add(homeexpo)
        if len(homeexpos) > 0:
            # minerals to move towards: hismim, homemim
            hismim_exists = False
            hismim = (self.nowhere,self.notag)
            hisexpo = self.expo_of_pos(self.enemy_pos)
            minsd = 99999
            for mim in self.minerals_of_expo[hisexpo]:
                (mimpos,mimt) = mim
                if self.near(mimpos, self.enemy_pos, 8):
                    hismim_exists = True
                    sd = self.sdist(mimpos, self.hisleft)
                    if sd < minsd:
                        minsd = sd
                        hismim = mim
            # homemim
            homemim_exists = {} # per expo with fighters: does it have minerals?
            homemim = {} # per expo with fighters: a (mimpos,postag)
            for homeexpo in homeexpos:
                homemim_exists[homeexpo] = False
                minsd = 99999
                for mim in self.minerals_of_expo[homeexpo]:
                    (mimpos,mimt) = mim
                    if self.near(mimpos, self.pos_of_expo[homeexpo], 8):
                        homemim_exists[homeexpo] = True
                        sd = self.sdist(mimpos, self.hisleft)
                        if sd < minsd:
                            minsd = sd
                            homemim[homeexpo] = mim
            # fighter_phase, goal_of_scvt should exist
            for scv in self.units(SCV):
                scvt = scv.tag
                if self.job_of_scvt[scvt] == 'fighter':
                    if scvt not in self.fighter_phase:
                        self.fighter_phase[scvt] = 'free'
                    if scvt not in self.goal_of_unittag:
                        self.goal_of_unittag[scvt] = self.nowhere
                    self.log_unitorder(scv, self.fighter_phase[scvt])
            # self.fighternurse relevance
            todel = set() # of nurse
            for nurse in self.fighternurse:
                repairee = self.fighternurse[nurse]
                seen = 0
                for scv in self.units(SCV):
                    scvt = scv.tag
                    if self.job_of_scvt[scvt] == 'fighter':
                        if self.fighter_phase[scvt] == 'nurse':
                            if scvt == nurse:
                                seen += 1
                        if self.fighter_phase[scvt] in {'rest','nurse'}:
                            if scvt == repairee:
                                if scv.health < self.healthybound:
                                    seen += 1
                if seen < 2:
                    todel.add(nurse)
            for nurse in todel:
                del self.fighternurse[nurse]
            # new self.fighternurse
            for scv in self.units(SCV):
                scvt = scv.tag
                if self.job_of_scvt[scvt] == 'fighter':
                    mypos = scv.position
                    if self.fighter_phase[scvt] == 'rest':
                        enecenter = self.calculate_enecenter(mypos)
                        minsd = 99999
                        bestscvt = scvt
                        for otherscv in self.units(SCV):
                            otherscvt = otherscv.tag
                            if otherscvt != scvt:
                                if self.job_of_scvt[otherscvt] == 'fighter':
                                    if self.fighter_phase[otherscvt] == 'rest':
                                        otherpos = otherscv.position
                                        sd = self.sdist(mypos,otherpos)
                                        co = self.sdist(enecenter,otherpos)
                                        ce = self.sdist(enecenter,mypos)
                                        if sd < co + ce:
                                            if otherscv.health < self.healthybound:
                                                if sd < minsd:
                                                    minsd = sd
                                                    bestscvt = otherscvt
                        if minsd < 99999:
                            self.fighternurse[scvt] = bestscvt
            #
            for scv in self.units(SCV):
                scvt = scv.tag
                if self.job_of_scvt[scvt] == 'fighter':
                    home = self.home_of_fighter[scvt]
                    homeexpo = self.expo_of_pos(home)
                    mypos = scv.position
                    enecenter = self.calculate_enecenter(mypos)
                    # wanteddist
                    wanteddist = scv.weapon_cooldown / 12
                    awaypos = mypos.towards(enecenter, -2)
                    awaywalk = self.check_walk(scvt, mypos, awaypos)
                    towardspos = mypos.towards(enecenter, 2)
                    phase = self.fighter_phase[scvt]
                    # nearenemy
                    # first try only units, if they are further than 10, accept buildings
                    nearenemydist = 99999
                    nearenemy = None
                    mytile = self.maptile_of_pos(mypos)
                    for tile in self.nine[mytile]:
                        for ene in self.enemies_of_tile[tile]:
                            if ene.type_id not in {LARVA, EGG, AUTOTURRET}:
                                # radius is needed as buildings are included.
                                dist = self.circledist(ene.position, mypos) - ene.radius
                                # dist 0.575 is touching, dist 0.675 is canhit
                                if dist < nearenemydist:
                                    if ene not in self.enemy_real_structures:
                                        nearenemydist = dist
                                        nearenemy = ene
                    if nearenemydist >= 10:
                        # accept buildings
                        nearenemydist = 99999
                        nearenemy = None
                        mytile = self.maptile_of_pos(mypos)
                        for tile in self.nine[mytile]:
                            for ene in self.enemies_of_tile[tile]:
                                if ene.type_id not in {LARVA, EGG, AUTOTURRET}:
                                    # radius is needed as buildings are included.
                                    dist = self.circledist(ene.position, mypos) - ene.radius
                                    # dist 0.575 is touching, dist 0.675 is canhit
                                    if dist < nearenemydist:
                                        nearenemydist = dist
                                        nearenemy = ene
                    # phase changes
                    newphase = phase
                    if scv.weapon_cooldown > 16:
                        newphase = 'away'
                    elif (phase == 'nurse'):
                        if (scv.health >= self.healthybound):
                            newphase = 'towards'
                        elif nearenemydist < 3.5:
                            newphase = 'away'
                        elif scvt not in self.fighternurse:
                            newphase = 'rest'
                    elif (phase == 'rest'):
                        if (scv.health >= self.healthybound):
                            newphase = 'towards'
                        elif nearenemydist < 3.5:
                            newphase = 'away'
                        elif scvt in self.fighternurse:
                            newphase = 'nurse'
                        elif (scv.health >= 31):
                            newphase = 'towards'
                    elif (scv.health <= 10):
                        if nearenemydist > 5:
                            newphase = 'rest'
                        else:
                            newphase = 'away'
                    elif (nearenemydist < 2) and (self.calc_outnumber(mypos) < 0):
                        newphase = 'hesitate'
                    elif nearenemydist < 1:
                        newphase = 'closeattack'
                    elif (phase == 'towards'):
                        # like the built-in attack command
                        if nearenemydist < 5:
                            newphase = 'found'
                    elif (phase == 'hesitate'):
                        if self.calc_outnumber(mypos) >= 0:
                            newphase = 'towards'
                    elif (nearenemydist > wanteddist + 0.1):
                        newphase = 'towards'
                    elif (nearenemydist < wanteddist - 0.1):
                        newphase = 'away'
                    #    
                    # metaphases 'away' and 'towards'
                    if newphase == 'away':
                        if (hismim_exists and homemim_exists[homeexpo]):
                            hm = homemim[homeexpo]
                            (hmp,hmt) = hm
                            if awaywalk:
                                newphase = 'walkaway'
                            elif self.sdist(enecenter, hmp) > self.sdist(mypos, hmp):
                                newphase = 'homemim'
                            else:
                                newphase = 'hismim'
                        else:
                            newphase = 'walkaway'
                    elif newphase == 'towards':
                        # go towards enecenter
                        newphase = 'walktowards'
                        # we use an angle of 60 degrees max to use mineralwalking
                        if homemim_exists[homeexpo]:
                            hm = homemim[homeexpo]
                            (hmp,hmt) = hm
                            a = self.circledist(mypos,enecenter) / 2
                            c = self.circledist(mypos,hmp) - a
                            b = self.circledist(enecenter, hmp)
                            if b*b < 3*a*a + c*c:
                                newphase = 'homemim'
                        if hismim_exists:
                            hm = hismim
                            (hmp,hmt) = hm
                            a = self.circledist(mypos,enecenter) / 2
                            c = self.circledist(mypos,hmp) - a
                            b = self.circledist(enecenter, hmp)
                            if b*b < 3*a*a + c*c:
                                newphase = 'hismim'
                    # do action?
                    do_action = False
                    if newphase != phase:
                        do_action = True
                    goal = self.goal_of_unittag[scvt]
                    if self.near(mypos,goal,1):
                        do_action = True
                    if (phase == newphase):
                        if scvt in self.idles:
                            # e.g. repair while no minerals
                            if phase != 'rest':
                                do_action = True
                    if newphase in {'closeattack','found'}:
                        # target switching
                        if scv.tag in self.victimtag_of_unittag:
                            if self.victimtag_of_unittag[scv.tag] != nearenemy.tag:
                                do_action = True
                    if self.frame % 23 == 22:
                        # some hanging situations remained
                        do_action = True
                    # action
                    if do_action:
                        if newphase == 'hismim':
                            # must check hismim_exists, as this phase can be a left-over.
                            if hismim_exists:
                                (hmp, hmt) = hismim
                                self.go_gather_mim(scv,hismim)
                                self.goal_of_unittag[scvt] = hmp
                        elif newphase == 'homemim':
                            if homemim_exists[homeexpo]:
                                hm = homemim[homeexpo]
                                (hmp, hmt) = hm
                                self.go_gather_mim(scv,hm)
                                self.goal_of_unittag[scvt] = hmp
                        elif newphase == 'walkaway':
                            scv.move(awaypos)
                            self.goal_of_unittag[scvt] = awaypos
                        elif newphase == 'walktowards':
                            scv.move(towardspos)
                            self.goal_of_unittag[scvt] = towardspos
                        elif newphase == 'found':
                            scv.move(nearenemy.position)
                        elif newphase == 'closeattack':
                            scv.attack(nearenemy)
                            # i would like to add:
                            #scv.gather(homemim[homeexpo],queue=True)
                            #self.goal_of_unittag[scvt] = homemimpos[homeexpo]
                        elif newphase == 'rest':
                            self.log_command('scv(AbilityId.STOP)')  # stop moving
                            scv(AbilityId.STOP)
                        elif newphase == 'hesitate':
                            scv.move(awaypos)
                            self.goal_of_unittag[scvt] = awaypos
                        elif newphase == 'nurse':
                            otherscvt = self.fighternurse[scvt] # exists because nurse
                            for otherscv in self.units(SCV):
                                if otherscv.tag == otherscvt:
                                    scv.repair(otherscv)
                    # round
                    self.fighter_phase[scvt] = newphase
                    # victimtag_of_unittag
                    if nearenemy is None:
                        pass
                    else:
                        self.victimtag_of_unittag[scv.tag] = nearenemy.tag

    def escort_builders(self):
        # dismiss escorter
        todel = set()
        for buildert in self.escorter_of_builder:
            scvt = self.escorter_of_builder[buildert]
            seen = False
            for builder in self.units(SCV):
                if builder.tag == buildert:
                    if self.job_of_scvt[buildert] == 'builder':
                        seen = True
            if not seen:
                todel.add(buildert)
                for scv in self.units(SCV):
                    if scv.tag == scvt:
                        self.promote(scv, 'idler')
            # no action if the escorter is gone
        for buildert in todel:
            del self.escorter_of_builder[buildert]
        # get new escorter
        if self.count_of_job['mimminer'] > 7:
            for builder in self.units(SCV):
                buildert = builder.tag
                if self.job_of_scvt[buildert] == 'builder':
                    if buildert not in self.escorter_of_builder:
                        enemiesnear = False
                        mytile = self.maptile_of_pos(builder.position)
                        for tile in self.nine[mytile]:
                            for ene in self.enemies_of_tile[tile]:
                                if self.near(ene.position, builder.position,7):
                                    if ene.type_id in self.all_workertypes:
                                        enemiesnear = True
                        if enemiesnear:
                            scvt = self.get_near_scvt_to_goodjob(builder.position)
                            self.escorter_of_builder[buildert] = scvt
                            for scv in self.units(SCV):
                                if scv.tag == scvt:
                                    self.promote(scv, 'escorter')
                                    self.log_command('scv.attack(goal)')
                                    scv.attack(builder.position)

    def housecleaning(self):
        # an enemy placed a turret at my natural!
        if self.frame < 4000: # 3 minutes
            if self.count_of_job['mimminer'] > 7:
                for tp in self.enemy_structureinfo:
                    (typ, itspos) = tp
                    if self.hoxy(itspos):
                        if typ not in {BARRACKSFLYING}:
                            cleaners = 0
                            for (scvt,cleanpos) in self.cleaners:
                                if cleanpos == itspos:
                                    cleaners += 1
                            if cleaners < 4:
                                scvt = self.get_near_scvt_to_goodjob(itspos)
                                for scv in self.units(SCV):
                                    if scv.tag == scvt:
                                        self.promote(scv,'escorter')
                                        scv.attack(itspos)
                                        self.cleaners.add((scvt,itspos))
        # cleaners administration check
        todel = set()
        for (scvt,cleanpos) in self.cleaners:
            seen = False
            for scv in self.units(SCV):
                if scv.tag == scvt:
                    if self.job_of_scvt[scvt] == 'escorter':
                        seen = True
            if not seen:
                todel.add((scvt,cleanpos))
        self.cleaners -= todel
        # dismiss cleaners?



    async def cheese1_army(self):
        if self.cheese1_marine_buildcount < 4:
            thing = MARINE
            if (self.cheese1_phase >= 'B') and (self.cheese1_phase < 'Z'):
                for ba in self.structures(BARRACKS):
                    if ba.tag in self.readies:
                        if ba.tag in self.idles:
                            if self.cheese1_barracks_tag == ba.tag:
                                if self.can_pay(thing):
                                    if self.check_supply(thing):
                                        if self.no_doubling(ba.tag):
                                            self.log_command('ba.train(thing)')
                                            ba.train(thing)
                                            self.bought(thing)
                                            self.cheese1_marine_buildcount += 1
                                            self.prevent_doubling(ba.tag)
        if self.cheese1_tank_buildcount < 1:
            thing = SIEGETANK
            if (self.cheese1_phase >= 'K') and (self.cheese1_phase < 'Z'):
                for fac in self.structures(FACTORY):
                    if fac.tag in self.readies:
                        if fac.tag in self.idles:
                            if self.cheese1_factory_tag == fac.tag:
                                if self.can_pay(thing):
                                    if self.check_supply(thing):
                                        if self.no_doubling(fac.tag):
                                            self.log_command('fac.train(thing)')
                                            fac.train(thing)
                                            self.bought(thing)
                                            self.cheese1_tank_buildcount += 1
                                            self.prevent_doubling(fac.tag)
        if self.cheese1_mine_buildcount < 2:
            thing = WIDOWMINE
            if (self.cheese1_phase >= 'N') and (self.cheese1_phase < 'Z'):
                for fac in self.structures(FACTORY):
                    if fac.tag in self.readies:
                        if fac.tag in self.idles:
                            if self.cheese1_factory_tag == fac.tag:
                                if self.can_pay(thing):
                                    if self.check_supply(thing):
                                        if self.no_doubling(fac.tag):
                                            self.log_command('fac.train(thing)')
                                            fac.train(thing)
                                            self.bought(thing)
                                            self.cheese1_mine_buildcount += 1
                                            self.prevent_doubling(fac.tag)

    def cheese1_scv_is_in_prison(self) -> bool:
        inprison = False
        for scv in self.units(SCV):
            if scv.tag == self.cheese1_scv_tag:
                bound = self.circledist(self.cheese1_prison_pos, self.cheese1_bunker_pos)
                if self.near(scv.position, self.cheese1_prison_pos, bound):
                    inprison = True
        return inprison

    def marines_into_cheesebunker(self):
        # explicit repair
        for bu in self.structures(BUNKER):
            if bu.tag == self.cheese1_bunker_tag:
                if bu.health < self.maxhealth[BUNKER]:
                    if self.cheese1_scv_is_in_prison():
                        for scv in self.units(SCV):
                            if scv.tag == self.cheese1_scv_tag:
                                if scv.tag not in self.thingtag_of_repairertag:
                                    self.thingtag_of_repairertag[scv.tag] = bu.tag
                                    scv.repair(bu)
        # marines into bunker
        for bu in self.structures(BUNKER):
            if bu.tag == self.cheese1_bunker_tag:
                for mar in bu.passengers:
                    if mar.type_id == MARINE:
                        self.cheese1_marine_tags.add(mar.tag)
        for mari in self.units(MARINE):
            if self.near(mari.position, self.cheese1_landing_pos, 7):
                if len(self.cheese1_marine_tags) < 4:
                    self.cheese1_marine_tags.add(mari.tag)
        for bun in self.structures(BUNKER):
            if bun.tag == self.cheese1_bunker_tag:
                if self.cheese1_scv_is_in_prison():
                    freeplaces = 4 - len(bun.passengers)
                else:
                    freeplaces = 3 - len(bun.passengers)
                if (freeplaces > 0):
                    for mari in self.units(MARINE):
                        if mari.tag in self.cheese1_marine_tags:
                            if freeplaces > 0:
                                if self.no_doubling(bun.tag):
                                    self.prevent_doubling(bun.tag)
                                    self.log_command('bun(AbilityId.LOAD_BUNKER,mari)')
                                    bun(AbilityId.LOAD_BUNKER, mari)
                                    freeplaces -= 1


    async def bunkercheese1(self):
        # break off the cheese?
        if (self.cheese1_phase >= 'B') and (self.cheese1_phase < 'Z'):
            startedbuildings = 0
            for barra in self.structures(BARRACKS):
                if barra.tag in self.readies:
                    if barra.position != self.cheese1_barracks_pos:
                        if self.near(barra.position,self.cheese1_landing_pos,7):
                            startedbuildings += 1
            for bunk in self.structures(BUNKER):
                if bunk.position == self.cheese1_bunker_pos:
                    self.cheese1_bunker_tag = bunk.tag
                    startedbuildings += 1
            if startedbuildings == 0:
                self.cheese1_phase = 'Y cleanup'
        # fly in the cheese
        if self.opening_name.find('cheese') >= 0:
            for ba in self.structures(BARRACKS):
                if ba.tag in self.readies:
                    if ba.position == self.cheese1_barracks_pos:
                        #
                        self.goal_of_flying_struct[ba.tag] = self.cheese1_landing_pos
                        self.landings_of_flying_struct[ba.tag] = 0
                        self.log_success('up cheese-BARRACKS')
                        self.log_command('ba(AbilityId.LIFT)')
                        ba(AbilityId.LIFT)
                        # it will try to land itself
        # follow a large series of phases
        if self.cheese1_phase == 'Anobunker':
            if not self.we_started_at(BUNKER, self.cheese1_bunker_pos):
                self.erase_layout(BUNKER,self.cheese1_bunker_pos)
                self.throw_at_spot(BUNKER, self.cheese1_bunker_pos, 'bunkercheese1')
                for scv in self.units(SCV):
                    if scv.tag == self.cheese1_scv_tag:
                        self.promote(scv,'idler')
                        self.cheese1_scv_tag = self.notag
                self.cheese1_phase = 'A'
        elif self.cheese1_phase == 'A':
            # wait for landed barracks and building bunker
            startedbuildings = 0
            for barra in self.structures(BARRACKS):
                if barra.tag in self.readies:
                    if barra.position != self.cheese1_barracks_pos:
                        if self.near(barra.position,self.cheese1_landing_pos,7):
                            self.cheese1_barracks_tag = barra.tag
                            self.speciality_of_tag[barra.tag] = 'cheese1'
                            startedbuildings += 1
            for bunk in self.structures(BUNKER):
                if bunk.position == self.cheese1_bunker_pos:
                    self.cheese1_bunker_tag = bunk.tag
                    startedbuildings += 1
            if startedbuildings == 2:
                for anscv in self.units(SCV):
                    scvt = anscv.tag
                    if scvt in self.goal_of_trabu_scvt:
                        if self.goal_of_trabu_scvt[scvt] == self.cheese1_bunker_pos:
                            self.cheese1_scv_tag = anscv.tag
                            self.speciality_of_tag[anscv.tag] = 'cheese1'
                self.cheese1_phase = 'B'
        elif self.cheese1_phase == 'B':
            # barracks has landed and bunker is started
            # wait for bunker ready
            for bun in self.structures(BUNKER):
                if bun.tag == self.cheese1_bunker_tag:
                    if bun.tag in self.last_health:
                        if bun.health < 0.67 * self.last_health[bun.tag]:
                            # execute bunkercheese before destroyed
                            # cancel the build
                            bun(AbilityId.CANCEL_BUILDINPROGRESS)
                            self.cheese1_phase = 'Anobunker'
                    # first, try back-to-track
                    if (self.cheese1_scv_tag not in self.all_scvtags) and (self.scout1_tag != self.notag):
                        # promote scout to cheese1_scv
                        for scv in self.units(SCV):
                            if scv.tag == self.scout1_tag:
                                if self.near(scv.position,self.cheese1_prison_pos,20):
                                    self.cheese1_scv_tag = scv.tag
                                    self.speciality_of_tag[scv.tag] = 'cheese1'
                                    self.scout1_tag = self.notag # allow reassign
                                    self.promote(scv,'cheeser')
                                    self.log_command('scv(AbilityId.SMART,bun)')
                                    scv(AbilityId.SMART,bun)
                    if bun in self.structures(BUNKER):
                        if bun.tag in self.readies:
                            # rally and load-or-repair and promotion
                            for ba in self.structures(BARRACKS):
                                if ba.tag == self.cheese1_barracks_tag:
                                    self.set_rally.add((ba.position, self.cheese1_bunker_pos))
                                    for scv in self.units(SCV):
                                        if scv.tag == self.cheese1_scv_tag:
                                            self.promote(scv, 'cheeser')
                                            # warning: scv inside the bunker is not in self.units(SCV)
                                            if self.cheese1_scv_is_in_prison():
                                                self.cheese1_phase = 'G'
                                            elif (scv.health > self.maxhealth[SCV] / 2) and (bun.health < self.maxhealth[BUNKER] / 2):
                                                self.cheese1_phase = 'C'
                                                if scv.tag not in self.thingtag_of_repairertag:
                                                    self.thingtag_of_repairertag[scv.tag] = bun.tag
                                                    scv.repair(bun)
                                            else:
                                                self.log_command('bun(AbilityId.LOAD_BUNKER,scv)')
                                                bun(AbilityId.LOAD_BUNKER,scv)
                                                self.cheese1_phase = 'D'
            if self.cheese1_bunker_tag not in self.all_bunkertags:
                if self.cheese1_scv_tag in self.all_scvt:
                    self.cheese1_phase = 'Anobunker'
        elif self.cheese1_phase == 'C':
            # outerrepair
            self.marines_into_cheesebunker()
            for bun in self.structures(BUNKER):
                if bun.tag == self.cheese1_bunker_tag:
                    if bun.tag in self.last_health:
                        if bun.health < 0.67 * self.last_health[bun.tag]:
                            # execute bunkercheese before destroyed
                            # cancel the build
                            bun(AbilityId.CANCEL_BUILDINPROGRESS)
                            self.cheese1_phase = 'Anobunker'
                    for scv in self.units(SCV):
                        if scv.tag == self.cheese1_scv_tag:
                            if (scv.health < self.maxhealth[SCV] / 2) or (bun.health > self.maxhealth[BUNKER] / 2):
                                self.log_command('bun(AbilityId.LOAD_BUNKER,scv)')
                                bun(AbilityId.LOAD_BUNKER, scv)
                                del self.thingtag_of_repairertag[scv.tag]
                                self.cheese1_phase = 'D'
        elif self.cheese1_phase == 'D':
            # wait until the scv is in the bunker
            for bu in self.structures(BUNKER):
                if bu.tag == self.cheese1_bunker_tag:
                    for mar in bu.passengers:
                        if mar.type_id == SCV:
                            self.cheese1_phase = 'E'
        elif self.cheese1_phase == 'E':
            # we want to unload the cheese1_scv, but only unloadall works
            for bun in self.structures(BUNKER):
                if bun.tag == self.cheese1_bunker_tag:
                    self.log_command('bun(AbilityId.UNLOADALL_BUNKER)')
                    bun(AbilityId.UNLOADALL_BUNKER)
                    self.cheese1_frames = 0
                    self.cheese1_phase = 'F'
        elif self.cheese1_phase == 'F':
            # wait until the scv is out of the bunker
            for scv in self.units(SCV):
                if scv.tag == self.cheese1_scv_tag:
                    self.cheese1_phase = 'G'
        elif self.cheese1_phase == 'G':
            self.marines_into_cheesebunker()
            # wait until the marines are inside
            allin = True
            for mar in self.units(MARINE):
                if mar.tag in self.cheese1_marine_tags:
                    allin = False
            if allin:
                self.cheese1_phase = 'H'
        elif self.cheese1_phase == 'H':
            self.marines_into_cheesebunker()
            # if the bunker is killed, try again
            if self.cheese1_bunker_tag not in self.all_bunkertags:
                if self.cheese1_scv_tag in self.all_scvt:
                    self.cheese1_phase = 'Anobunker'
                    self.set_rally.add((self.cheese1_landing_pos, self.cheese1_prison_pos))
            # use the scout for an extra bunker
            if self.scout1_tag != self.notag:
                for scv in self.units(SCV):
                    if scv.tag == self.scout1_tag:
                        if self.near(scv.position, self.cheese1_bunker_pos, 10):
                            mytile = self.maptile_of_pos(scv.position)
                            tail = 0
                            for tile in self.nine[mytile]:
                                for ene in self.enemies_of_tile[tile]:
                                    if self.near(ene.position,scv.position,4):
                                        tail += 1
                            if tail < 2:
                                if self.can_pay(BUNKER):
                                    around = scv.position.towards(self.cheese1_bunker_pos,2)
                                    place = self.place_around(BUNKER,around)
                                    self.cheese1_scv_tag = scv.tag
                                    self.speciality_of_tag[scv.tag] = 'cheese1'
                                    self.scout1_tag = self.notag # allows reassign
                                    self.promote(scv, 'reporter')
                                    scv.move(place)
                                    self.throw_at_spot(BUNKER,place,'bunkercheese1')
            # wait for the factory and rally it
            for facta in self.structures(FACTORY):
                if facta.tag in self.readies:
                    if facta.position == self.cheese1_factory_pos:
                        self.cheese1_factory_tag = facta.tag
                        self.cheese1_phase = 'I'
        elif self.cheese1_phase == 'I':
            self.marines_into_cheesebunker()
            # make a lab
            for fac in self.structures(FACTORY):
                if facta.tag in self.readies:
                    if fac.position == self.cheese1_factory_pos:
                        if self.can_pay(FACTORYTECHLAB):
                            self.log_command('fac.train(FACTORYTECHLAB)')
                            fac.train(FACTORYTECHLAB)
                            self.bought(FACTORYTECHLAB)
                            self.cheese1_phase = 'J'
        elif self.cheese1_phase == 'J':
            self.marines_into_cheesebunker()
            for tl in self.structures(FACTORYTECHLAB):
                if tl.tag in self.readies:
                    self.cheese1_phase = 'K'
        elif self.cheese1_phase == 'K':
            self.marines_into_cheesebunker()
            # wait for tank to be made
            if self.cheese1_tank_buildcount == 1:
                if len(self.units(SIEGETANK)) + len(self.units(SIEGETANKSIEGED)) == 1:
                    # fly the factory in
                    for fac in self.structures(FACTORY):
                        if fac.tag in self.readies:
                            if fac.tag == self.cheese1_factory_tag:
                                self.goal_of_flying_struct[fac.tag] = self.cheese1_landing_pos
                                self.landings_of_flying_struct[fac.tag] = 0
                                self.log_success('up FACTORY')
                                self.log_command('fac(AbilityId.LIFT')
                                fac(AbilityId.LIFT)
                                # next phase M or L
                                self.cheese1_phase = 'M'
                    # for combination of cheese1 and cheese3, cheese3 gets the tank
                    if self.cheese3_phase == 'A':
                        for st in self.units(SIEGETANK):
                            self.cheese1_tank_tag = st.tag
                            self.speciality_of_tag[st.tag] = 'cheese1'
                            # toward cheese1_tank_pos
                            self.log_command('st.attack(self.cheese1_tank_pos)')
                            st.attack(self.cheese1_tank_pos)
                            # next phase
                            self.cheese1_phase = 'L'
        elif self.cheese1_phase == 'L':
            # wait for tank to arrive, then siege it
            for st in self.units(SIEGETANK):
                if st.tag in self.idles:
                    if st.tag == self.cheese1_tank_tag:
                        self.log_command('st(AbilityId.SIEGEMODE_SIEGEMODE)')
                        st(AbilityId.SIEGEMODE_SIEGEMODE)
                        self.cheese1_phase = 'M'
        elif self.cheese1_phase == 'M':
            # fly the barracks out
            for ba in self.structures(BARRACKS):
                if ba.tag == self.cheese1_barracks_tag:
                    self.goal_of_flying_struct[ba.tag] = self.cheese1_factory_pos
                    self.landings_of_flying_struct[ba.tag] = 0
                    self.log_success('up BARRACKS')
                    self.log_command('ba(AbilityId.LIFT')
                    ba(AbilityId.LIFT)
                    self.cheese1_phase = 'N'
        elif self.cheese1_phase == 'N':
            # wait for landing of factory and rally it
            for fac in self.structures(FACTORY):
                if fac.tag in self.readies:
                    if fac.tag == self.cheese1_factory_tag:
                        point = fac.position.towards(self.enemy_pos,2) # if bunker is gone
                        for bun in self.structures(BUNKER):
                            if bun.tag == self.cheese1_bunker_tag:
                                point = bun.position.towards(self.enemy_pos,2)
                        self.set_rally.add((fac.position,point))
                        self.cheese1_phase = 'O'
        elif self.cheese1_phase == 'O':
            # wait for 2 cheese1_mines
            for wm in self.units(WIDOWMINEBURROWED):
                if wm.tag in self.cheese1_mine_tags:
                    # cooldown: 29 sec * 22.4 frames/sec
                    if self.mine_shot[wm.tag] + 650 < self.frame:
                        abilities = (await self.get_available_abilities([wm]))[0]
                        if AbilityId.WIDOWMINEATTACK_WIDOWMINEATTACK not in abilities:
                            # it fired!
                            self.mine_shot[wm.tag] = self.frame
            for wm in self.units(WIDOWMINE):
                wmt = wm.tag
                if self.near(wm.position,self.cheese1_landing_pos,7):
                    if wmt not in self.cheese1_mine_tags:
                        self.cheese1_mine_tags.add(wmt)
                        self.speciality_of_tag[wmt] = 'cheese1'
                        self.mine_shot[wmt] = 0
                        found = False
                        while not found:
                            # cheese1 is expected to finish before the map is mined out.
                            (mimpos, tag) = random.choice(tuple(self.all_minerals))
                            if self.near(mimpos, self.enemy_pos, self.miner_bound):
                                goal = mimpos.towards(self.loved_pos,-2)
                                found = True
                        self.burrowpos_of_wmt[wmt] = goal
                        pole = self.get_near_pole(goal)
                        self.homepole_of_wmt[wmt] = pole
                        pole = self.get_near_pole(wm.position)
                        pole = (pole + 1) % len(self.scout1_pos)
                        self.pole_of_wmt[wmt] = pole
                        self.phase_of_wmt[wmt] = 'flee'
                        if len(self.cheese1_mine_tags) < 2:
                            self.log_command('wm(AbilityId.BURROWDOWN_WIDOWMINE)')
                            wm(AbilityId.BURROWDOWN_WIDOWMINE)
            if len(self.cheese1_mine_tags) == 2:
                for wm in self.units(WIDOWMINE) + self.units(WIDOWMINEBURROWED):
                    if wm.tag in self.cheese1_mine_tags:
                        wmt = wm.tag
                        if (wm in self.units(WIDOWMINEBURROWED)):
                            self.log_command('wm(AbilityId.BURROWUP_WIDOWMINE)')
                            wm(AbilityId.BURROWUP_WIDOWMINE)
                        pole = self.pole_of_wmt[wmt]
                        goal = self.scout1_pos[pole]
                        self.go_move(wm,goal)
                        self.cheese1_phase = 'P'
        elif self.cheese1_phase == 'P':
            # manage cheesemines
            for wm in self.units(WIDOWMINE) + self.units(WIDOWMINEBURROWED):
                if wm.tag in self.cheese1_mine_tags:
                    # a widowmine does not have weapon_cooldown, so we calculate mine_shot
                    wmt = wm.tag
                    if self.phase_of_wmt[wmt] == 'attack':
                        if (wm in self.units(WIDOWMINE)):
                            if self.no_move_or_near(wm,32,0.1):
                                self.log_command('wm(AbilityId.BURROWDOWN_WIDOWMINE)')
                                wm(AbilityId.BURROWDOWN_WIDOWMINE)
                        if (wm in self.units(WIDOWMINEBURROWED)):
                            # cooldown: 29 sec * 22.4 frames/sec = 650 frames
                            if self.mine_shot[wm.tag] + 650 < self.frame:
                                abilities = (await self.get_available_abilities([wm]))[0]
                                if AbilityId.WIDOWMINEATTACK_WIDOWMINEATTACK not in abilities:
                                    # it fired!
                                    self.mine_shot[wm.tag] = self.frame
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
            if len(self.cheese1_mine_tags) == 0: #todo living
                self.cheese1_phase = 'Y cleanup'
        elif self.cheese1_phase == 'Y cleanup':
            # clean up
            self.clean_speciality_of_tag('cheese1')
            for scv in self.units(SCV):
                if scv.tag == self.cheese1_scv_tag:
                    self.promote(scv,'idler')
            self.cheese1_scv_tag = self.notag
            for st in self.units(SIEGETANKSIEGED):
                if st.tag == self.cheese1_tank_tag:
                    self.log_command('st(AbilityId.UNSIEGE_UNSIEGE)')
                    st(AbilityId.UNSIEGE_UNSIEGE)
                    self.log_command('st.attack(self.loved_pos)')
                    st.attack(self.loved_pos)
            self.cheese1_tank_tag = self.notag
            for ba in self.structures(BARRACKS):
                if ba.tag == self.cheese1_barracks_tag:
                    self.log_command('ba(AbilityId.CANCEL_BUILDINPROGRESS)')
                    ba(AbilityId.CANCEL_BUILDINPROGRESS)
                    self.goal_of_flying_struct[ba.tag] = self.wall_barracks_pos
                    self.landings_of_flying_struct[ba.tag] = 0
                    self.log_success('up CHEESE_BARRACKS')
                    self.log_command('ba(AbilityId.LIFT')
                    ba(AbilityId.LIFT)
            self.cheese1_barracks_tag = self.notag
            self.cheese1_mine_tags = set()
            self.log_success('ending the bunkercheese')
            self.cheese1_phase = 'Z'
        #
        self.log_cheese()

    ################ cheese2 ########################

    async def bunker_handling(self):
        # hiding_spot
        if bunker_if.hiding_spot is None:
            if len(self.expansion_locations) > 0:
                place = random.choice(tuple(self.expansion_locations))
            else:
                place = self.random_mappoint()
            while self.proxy(place) or self.near(place, self.loved_pos, 60):
                place = self.random_mappoint()
            bunker_if.hiding_spot = place
        if self.opening_name.find('cheese') < 0: # not
            for bu in self.structures(BUNKER):
                # give some time to others to make it special
                if bu.build_progress > 0.25:
                    if bu.tag not in self.speciality_of_tag:
                        bunker_if.bunkertags.add(bu.tag)
                        if bu.tag not in bunker_if.door:
                            bunker_if.door[bu.tag] = bu.position.towards(self.loved_pos, 3)
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
            for tow in self.expansion_locations:
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
            if self.supply_used >= 190:
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
        if self.game_choice[60]:
            if not self.rushopening: # that would be a bad combination
                if (self.we_started_amount(BUNKER) < len(self.all_mine_bases) - 1) and (len(self.units(MARINE)) > 0):
                    todo = 1
                    for goal in self.expansion_locations:
                        if goal not in self.cheese2_triedexp:
                            if todo > 0:
                                todo -= 1
                                self.cheese2_triedexp.add(goal)
                                pos = self.init_cheese_position(goal,79,79,BUNKER)
                                self.throw_at_spot(BUNKER,pos,'bunkercheese2')
                                self.cheese2_bunkspots.add(pos)
                                self.throw_anywhere(MARINE,'bunkercheese2')


    ################ cheese3 ########################


    async def cheese3_internals(self):
        # bunker has started
        # name cheesebunker
        for bu in self.structures(BUNKER):
            if bu.position == self.cheese3_bunker_pos:
                self.cheese3_bunker_tag = bu.tag
            if bu.position == self.cheese3_bunker2_pos:
                self.cheese3_bunker2_tag = bu.tag
        # name cc
        for cc in self.structures(COMMANDCENTER):
            if cc.position == self.cheese3_cc_pos:
                self.cheese3_cc_tag = cc.tag
                self.speciality_of_tag[cc.tag] = self.opening_name
        # rebuild bunker
        if not self.we_started_at(BUNKER, self.cheese3_bunker_pos):
            if self.allow_throw(BUNKER):
                self.throw_at_spot(BUNKER, self.cheese3_bunker_pos, 'cheese3_internals')
                self.movetothefront(BUNKER,'cheese3_internals')
        # rebuild cc
        for bu in self.structures(BUNKER):
            if bu.tag in self.readies:
                if bu.tag == self.cheese3_bunker_tag:
                    if not self.we_started_at(COMMANDCENTER,self.cheese3_cc_pos):
                        if self.cheese3_phase <= 'E':
                            self.throw_at_spot(COMMANDCENTER,self.cheese3_cc_pos,'cheese3_internals')
                            self.movetothefront(COMMANDCENTER,'cheese3_internals')


    async def do_pf_rush(self):
        if self.opening_name == 'pf-rush':
            if self.cheese3_phase == 'A':
                # while (nothing)
                # continue
                for ba in self.structures(BARRACKS):
                    if ba.position == self.cheese3_barracks_pos:
                        # init (barracks is constructing)
                        self.speciality_of_tag[ba.tag] = self.opening_name
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
                for bu in self.structures(BUNKER):
                    if bu.tag in self.readies:
                        if bu.tag == self.cheese3_bunker_tag:
                            # init (bunker ready)
                            for ba in self.structures(BARRACKS):
                                if ba.tag == self.cheese3_barracks_tag:
                                    self.set_rally.add((ba.position,bu.position))
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
                        self.speciality_of_tag[cc.tag] = self.opening_name
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
                for cc in self.structures(COMMANDCENTER):
                    if cc.tag in self.readies:
                        if cc.tag == self.cheese3_cc_tag:
                            if self.enemy_species == 'zerg':
                                self.cheese3_phase = 'G1'
                            else:
                                self.cheese3_phase = 'F1'
                            self.waitframe_of_tag[cc.tag] = self.frame+20
            elif self.cheese3_phase == 'F1':
                # while (cooldown)
                await self.cheese3_internals()
                # continue
                if self.frame >= self.waitframe_of_tag[self.cheese3_cc_tag]:
                    self.cheese3_phase = 'F'
                    # init (cc ready)
                    for cc in self.structures(COMMANDCENTER):
                        if cc.tag == self.cheese3_cc_tag:
                            self.goal_of_flying_struct[cc.tag] = self.cheese3_landing_pos
                            self.landings_of_flying_struct[cc.tag] = 0
                            self.log_success('up cheese COMMANDCENTER')
                            self.log_command('cc(AbilityId.LIFT')
                            cc(AbilityId.LIFT)
                            self.cheese3_phase = 'F'
            elif self.cheese3_phase == 'F':
                # while (cc flies)
                await self.cheese3_internals()
                # clean
                if self.cheese3_barracks_tag not in (ba.tag for ba in self.structures(BARRACKS)):
                    self.cheese3_phase = 'Y'
                if self.cheese3_cc_tag not in (cc.tag for cc in self.structures(COMMANDCENTER)):
                    if self.cheese3_cc_tag not in (cc.tag for cc in self.structures(COMMANDCENTERFLYING)):
                        self.cheese3_phase = 'Y'
                # continue
                for cc in self.structures(COMMANDCENTER): # so it landed
                    if cc.tag in self.readies:
                        if (cc.tag == self.cheese3_cc_tag) and (cc.position != self.cheese3_cc_pos):
                            self.waitframe_of_tag[cc.tag] = self.frame + 20
                            self.cheese3_phase = 'G1'
            elif self.cheese3_phase == 'G1':
                # while (cooldown)
                await self.cheese3_internals()
                #clean
                if self.cheese3_cc_tag not in (cc.tag for cc in self.structures(COMMANDCENTER)):
                    if self.cheese3_cc_tag not in (cc.tag for cc in self.structures(COMMANDCENTERFLYING)):
                        self.cheese3_phase = 'Y'
                # continue
                if self.frame >= self.waitframe_of_tag[self.cheese3_cc_tag]:
                    # init (cc to pf)
                    for cc in self.structures(COMMANDCENTER):
                        if (cc.tag == self.cheese3_cc_tag):
                            self.set_rally.add((cc.position, self.cheese3_prison_pos))
                            self.throw_at_spot(PLANETARYFORTRESS,cc.position,'do_pf_rush')
                            self.cheese3_phase = 'G'
            elif self.cheese3_phase == 'G':
                # while (cc to pf)
                await self.cheese3_internals()
                #clean
                if self.cheese3_cc_tag not in (cc.tag for cc in self.structures(COMMANDCENTER)):
                    if self.cheese3_cc_tag not in (cc.tag for cc in self.structures(COMMANDCENTERFLYING)):
                        self.cheese3_phase = 'Y'
                # continue
                for cc in self.structures(PLANETARYFORTRESS):
                    if cc.tag in self.readies:
                        if (self.cheese3_cc_tag == cc.tag):
                            # init (pf ready)
                            self.cheese3_phase = 'H'
            elif self.cheese3_phase == 'H':
                # while (pf ready)
                await self.cheese3_internals()
                #clean
                seen = False
                for cc in self.structures(PLANETARYFORTRESS):
                    if cc.tag in self.readies:
                        if (self.cheese3_cc_tag == cc.tag):
                            seen = True
                if not seen:
                    self.cheese3_phase = 'Y'
                # make
                for cc in self.structures(PLANETARYFORTRESS):
                    if cc.tag in self.readies:
                        if cc.tag in self.idles:
                            if cc.tag == self.cheese3_cc_tag:
                                if self.wantscv():
                                    if self.can_pay(SCV):
                                        cc.train(SCV)
                                        self.bought(SCV)
                # continue
            elif self.cheese3_phase == 'Y':
                # clean up the cheese
                self.clean_speciality_of_tag(self.opening_name)
                for ba in self.structures(BARRACKS):
                    if ba.tag == self.cheese3_barracks_tag:
                        if ba.tag not in self.readies:
                            self.log_command('ba(AbilityId.CANCEL_BUILDINPROGRESS)')
                            ba(AbilityId.CANCEL_BUILDINPROGRESS)
                        if ba.tag in self.readies:
                            if self.find_tobuildwalk_a_place(BARRACKS,'now'):
                                goal = self.function_result_Point2
                                self.write_layout(BARRACKS, goal)
                                if ba.tag not in self.idles:
                                    self.log_command('ba(AbilityId.CANCEL_QUEUE5)') # build unit
                                    ba(AbilityId.CANCEL_QUEUE5)
                                self.goal_of_flying_struct[ba.tag] = goal
                                self.landings_of_flying_struct[ba.tag] = 0
                                self.log_success('move cheese BARRACKS')
                                self.log_command('ba(AbilityId.LIFT')
                                ba(AbilityId.LIFT)
                for ba in self.structures(BARRACKSFLYING):
                    if ba.tag == self.cheese3_barracks_tag:
                        if self.find_tobuildwalk_a_place(BARRACKS,'now'):
                            goal = self.function_result_Point2
                            self.write_layout(BARRACKS, goal)
                            self.goal_of_flying_struct[ba.tag] = goal
                            self.landings_of_flying_struct[ba.tag] = 0
                            self.log_success('move cheese BARRACKS')
                for cc in self.structures(COMMANDCENTER):
                    if cc.tag == self.cheese3_cc_tag:
                        if cc.tag not in self.readies:
                            self.log_command('cc(AbilityId.CANCEL_BUILDINPROGRESS)')
                            cc(AbilityId.CANCEL_BUILDINPROGRESS)
                        if cc.tag in self.readies:
                            if self.find_tobuildwalk_a_place(COMMANDCENTER,'now'):
                                goal = self.function_result_Point2
                                self.write_layout(COMMANDCENTER, goal)
                                if cc.tag not in self.idles:
                                    self.log_command('cc(AbilityId.CANCEL_QUEUECANCELTOSELECTION)') # build worker
                                    cc(AbilityId.CANCEL_QUEUECANCELTOSELECTION)
                                self.goal_of_flying_struct[cc.tag] = goal
                                self.landings_of_flying_struct[cc.tag] = 0
                                self.log_success('move cheese COMMANDCENTER')
                                self.log_command('cc(AbilityId.LIFT')
                                cc(AbilityId.LIFT)
                for cc in self.structures(COMMANDCENTERFLYING):
                    if cc.tag == self.cheese3_cc_tag:
                        if self.find_tobuildwalk_a_place(COMMANDCENTER,'now'):
                            goal = self.function_result_Point2
                            self.write_layout(COMMANDCENTER, goal)
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
        for (mimpos,mimt) in self.all_minerals:
            if self.near(mimpos, point, 6):
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
        for ene in self.enemy_real_structures:
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
        for (typ,pos) in self.enemy_structureinfo:
            sig += pos.x
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
        for ene in self.enemy_units: # actual visible
            if ene.can_attack_ground:
                if self.near(ene.position,mypoint,30): # restrict work
                    lastpos = ene.position
                    for (typ,pos,tag) in self.last_enemies:
                        if tag == ene.tag:
                            lastpos = pos
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
            for ene in self.enemy_units: # actual visible
                lastpos = ene.position
                for (typ, pos, tag) in self.last_enemies:
                    if tag == ene.tag:
                        lastpos = pos
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
            for (typ, pos, tag) in self.last_enemies:
                if tag == ene.tag:
                    lastpos = pos
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
        if self.opening_name == 'reapers':
            if len(self.units(REAPER)) > 0:
                # scvs building bunkers
                if len(self.structures(BUNKER)) > 0:
                    for anscv in self.units(SCV):
                        scvt = anscv.tag
                        if scvt in self.goal_of_trabu_scvt:
                            if self.goal_of_trabu_scvt[scvt] in [self.reaper_bunker1_pos,self.reaper_bunker2_pos]:
                                self.promote(anscv,'cheeser')
                                self.speciality_of_tag[anscv.tag] = self.opening_name
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
                for ene in self.enemy_units: # actual visible
                    # todo if not cloacked
                    if self.near(ene.position,self.reaper_prison_pos,8):
                        self.reaper_focus = self.reaper_center #self.reaper_prison_pos
                # change focus of entering reapers
                if self.reaper_focus != old_reaper_focus:
                    for re in self.units(REAPER):
                        if re.tag in self.reaper_status:
                            if self.reaper_status[re.tag] != 'fleeing': # reaper
                                self.reaper_status[re.tag] = 'relaxing'
                # fleepos
                fleepos = self.map_center
                bestsd = self.sdist(self.reaper_focus,fleepos)
                for bun in self.structures(BUNKER):
                    if bun.tag in self.readies:
                        if len(bun.passengers) < 4:
                            sd = self.sdist(bun.position,self.reaper_focus)
                            if sd < bestsd:
                                bestsd = sd
                                fleepos = bun.position
                # steer each reaper
                for re in self.units(REAPER):
                    if re.tag not in self.reaper_status:
                        self.reaper_status[re.tag] = 'relaxing'
                        self.speciality_of_tag[re.tag] = self.opening_name # prevent standard reaper code
                    status = self.reaper_status[re.tag]
                    if re.health < self.maxhealth[re.type_id] / 4:
                        status = 'fleeing' # reaper
                        re.move(fleepos)
                    if status == 'fleeing': # reaper
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

    async def swap_starports_to_techlab(self):
        # get starport and techlab
        if self.frame % 11 == 10:
            for (martype, bartype, pos, dura) in self.eggs:
                if (dura >= 6) and (dura < 12):
                    if martype == BARRACKSTECHLAB:
                        if (BARRACKS,pos) not in self.willswap:
                            self.couldswap.add((BARRACKS,pos))
                    elif martype == FACTORYTECHLAB:
                        if (FACTORY,pos) not in self.willswap:
                            self.couldswap.add((FACTORY, pos))
                    elif martype == STARPORT:
                        if (STARPORT,pos) not in self.willswap:
                            self.couldswap.add((STARPORT, pos))
            await self.swapping_actions()

    async def swap_starports_to_reactor(self):
        # get starport and reactor
        if self.frame % 11 == 10:
            for (martype, bartype, pos, dura) in self.eggs:
                if (dura >= 6) and (dura < 12):
                    if martype == BARRACKSREACTOR:
                        if (BARRACKS,pos) not in self.willswap:
                            self.couldswap.add((BARRACKS,pos))
                    elif martype == FACTORYREACTOR:
                        if (FACTORY,pos) not in self.willswap:
                            self.couldswap.add((FACTORY, pos))
                    elif martype == STARPORT:
                        if (STARPORT,pos) not in self.willswap:
                            self.couldswap.add((STARPORT, pos))
            await self.swapping_actions()

    async def swapping_actions(self):
        # administrate existing plans
        todel = set()
        for (frompos,topos) in self.swapplans:
            for (thing, pos) in self.couldswap:
                if (pos == frompos) or (pos == topos):
                    self.willswap.add((thing, pos))
                    todel.add((thing, pos))
        self.couldswap -= todel
        # make new plans; connect starport lab
        maycombis = set()
        for (thing1,pos1) in self.couldswap:
            if thing1 == STARPORT:
                for (thing2, pos2) in self.couldswap:
                    if thing2 in {BARRACKS,FACTORY}:
                        maycombis.add((pos1,pos2,self.sdist(pos1,pos2)))
        minsd = 99999
        for (frompos,topos,sd) in maycombis:
            if sd < minsd:
                combi = (frompos,topos)
                minsd = sd
        if minsd < 9*9:
            # use combi
            self.swapplans.add(combi)
        # lift
        todel = set()
        for (frompos,topos) in self.swapplans:
            amready = 0
            for (thingtype,pos) in self.willswap:
                if pos in {frompos,topos}:
                    for bu in self.structures(thingtype):
                        if bu.tag in self.readies:
                            if bu.tag in self.idles:
                                if bu.position == pos:
                                    if (thingtype == STARPORT) or (bu.has_add_on):
                                        amready += 1
            if amready == 2:
                goon = False
                for bu in self.structures(STARPORT):
                    if bu.position == frompos:
                        if bu.tag not in self.waitframe_of_tag:
                            self.waitframe_of_tag[bu.tag] = self.frame + 20
                        elif self.frame >= self.waitframe_of_tag[bu.tag]:
                            goon = True
                if goon:
                    for (thingtype,pos) in self.willswap:
                        if pos in {frompos, topos}:
                            for bu in self.structures(thingtype):
                                if bu.tag in self.readies:
                                    if bu.tag in self.idles:
                                        if bu.position == pos:
                                            if (thingtype == STARPORT) or (bu.has_add_on):
                                                todel.add((thingtype,pos))
                                                self.didswap.add((thingtype,pos))
                                                # lift
                                                goal = self.loved_pos
                                                if thingtype == BARRACKS:
                                                    goal = frompos
                                                    if self.we_started_amount(BARRACKS) == 1:
                                                        goal = self.wall_barracks_pos
                                                elif thingtype == FACTORY:
                                                    goal = frompos
                                                elif thingtype == STARPORT:
                                                    goal = topos
                                                self.goal_of_flying_struct[bu.tag] = goal
                                                self.landings_of_flying_struct[bu.tag] = 0
                                                # bu(AbilityId.LIFT) failed.
                                                #stri = 'debug '
                                                #abilities = (await self.get_available_abilities([bu]))[0]
                                                #for abi in abilities:
                                                #   stri = stri + ' ' + abi.name
                                                #print(stri)
                                                self.log_success('swap up ' + thingtype.name)
                                                if thingtype == BARRACKS:
                                                    bu(AbilityId.LIFT_BARRACKS)
                                                    self.log_command('bu(AbilityId.LIFT_BARRACKS')
                                                elif thingtype == FACTORY:
                                                    bu(AbilityId.LIFT_FACTORY)
                                                    self.log_command('bu(AbilityId.LIFT_FACTORY')
                                                elif thingtype == STARPORT:
                                                    bu(AbilityId.LIFT_STARPORT)
                                                    self.log_command('bu(AbilityId.LIFT_STARPORT')
        self.willswap -= todel
        self.log_swaps()

    async def do_banshees(self):
        if self.opening_name.find('banshees') >= 0:
            await self.swap_starports_to_techlab()
            # upgrade asap
            upg = BANSHEECLOAK
            for bu in self.structures(STARPORTTECHLAB):
                self.throw_treeno(upg, 'do_banshees')

    def standard_reapers(self):
        for rea in self.units(REAPER):
            tag = rea.tag
            if tag not in self.speciality_of_tag:
                if tag not in self.reaper_status:
                    self.reaper_status[tag] = 'home'
                status = self.reaper_status[tag]
                if status == 'home':
                    if rea.health >= 35:
                        status = 'out'
                        self.attackmove(tag,self.reaper_goal,2)
                elif status == 'out':
                    if tag in self.last_health:
                        if rea.health < 0.67 * self.last_health[tag]:
                            self.end_attackmove(tag)
                            rea.move(self.loved_pos)
                            status = 'home'
                self.reaper_status[tag] = status

    def do211_init(self):
        self.do211_goals = []
        # brute fly-in
        goal = self.enemy_pos.towards(self.map_center,4)
        goal = self.place_around(AUTOTURRET,goal)
        self.do211_goals.append(goal)
        # ramptop
        goal = self.enemyramp_pos.towards(self.enemy_pos,3)
        goal = self.place_around(AUTOTURRET,goal)
        self.do211_goals.append(goal)
        # rampbottom
        goal = self.enemyramp_pos.towards(self.enemy_pos,-3)
        goal = self.place_around(AUTOTURRET,goal)
        self.do211_goals.append(goal)
        # choke
        goal = self.enemynaturalchoke_pos.towards(self.map_center,4)
        goal = self.place_around(AUTOTURRET,goal)
        self.do211_goals.append(goal)
        # enemyhall.towards(center,-4) will be added later

    async def do211_steps(self):
        if self.opening_name == '2-1-1':
            # swap
            if self.game_phase == 'opening':
                await self.swap_starports_to_reactor()
            # alive
            if self.eggorbird(STARPORTREACTOR):
                self.do211_mar = self.do211_mar & self.all_unittags
                self.do211_scv = self.do211_scv & self.all_unittags
                self.do211_med = self.do211_med & self.all_unittags
            # phases
            if self.do211_phase == 0:
                # gather
                if self.eggorbird(STARPORTREACTOR):
                    goal = self.homenaturalchoke_pos.towards(self.homenatural_pos,2)
                    for mar in self.units(MARINE):
                        if len(self.do211_mar) < 14:
                            if mar.tag not in self.do211_mar:
                                self.do211_mar.add(mar.tag)
                                self.speciality_of_tag[mar.tag] = self.opening_name
                                self.emotion_of_unittag[mar.tag] = 'bored'
                                mar.move(goal)
                                if mar.tag in self.attackmove_state:
                                    self.end_attackmove(mar.tag)
                    while len(self.do211_scv) < 2:
                        scvt = self.get_near_scvt_to_goodjob(goal)
                        for scv in self.units(SCV):
                            if scv.tag == scvt:
                                if scv.tag not in self.do211_scv: # of course
                                    self.promote(scv,'cheeser')
                                    self.do211_scv.add(scv.tag)
                                    self.speciality_of_tag[scv.tag] = self.opening_name
                                    self.emotion_of_unittag[scv.tag] = 'bored'
                                    scv.move(goal)
                    for med in self.units(MEDIVAC):
                        if len(self.do211_med) < 2:
                            if med.tag not in self.do211_med:
                                self.do211_med.add(med.tag)
                                self.speciality_of_tag[med.tag] = self.opening_name
                                med.move(goal)
                    if len(self.do211_mar) + len(self.do211_scv) + len(self.do211_med) == 18:
                        self.do211_phase += 1
            elif self.do211_phase == 1:
                # choose a plane
                for med in self.units(MEDIVAC):
                    if med.tag in self.do211_med:
                        passengers = 0
                        for mar in self.units(MARINE):
                            if mar.tag in self.do211_mar:
                                if passengers < 8:
                                    if mar.tag not in self.do211_plane:
                                        self.do211_plane[mar.tag] = med.tag
                                        passengers += 1
                        for scv in self.units(SCV):
                            if scv.tag in self.do211_scv:
                                if passengers < 8:
                                    if scv.tag not in self.do211_plane:
                                        self.do211_plane[scv.tag] = med.tag
                                        passengers += 1
                self.do211_phase += 1
            elif self.do211_phase == 2:
                # load
                # can be entered from phase 9
                allpassengers = min(8 * len(self.do211_med), len(self.do211_mar) + len(self.do211_scv))
                loadedpassengers = 0
                for med in self.units(MEDIVAC):
                    if med.tag in self.do211_med:
                        loadedpassengers += len(med.passengers)
                        if med.tag in self.idles:
                            for unt in self.units:
                                if unt.tag in self.do211_scv | self.do211_mar:
                                    if self.do211_plane[unt.tag] == med.tag:
                                        self.emotion_of_unittag[unt.tag] = 'flying'
                                        med(AbilityId.LOAD_MEDIVAC, unt, queue=True)
                if loadedpassengers == allpassengers:
                    self.do211_phase += 1
            elif self.do211_phase == 3:
                # add enemy hall goals
                # can be entered from phase 5
                for (enetype, enepos) in self.enemy_structureinfo:
                    if enetype in self.hall_types:
                        if enepos not in self.do211_hallsgoaled:
                            self.do211_hallsgoaled.add(enepos)
                            goal = enepos.towards(self.map_center,-4)
                            goal = self.place_around(AUTOTURRET,goal)
                            self.do211_goals.append(goal)
                self.do211_phase += 1
            elif self.do211_phase == 4:
                # choose self.do211_goal
                his_agression = 0
                for ene in self.enemy_units:
                    if self.ground_strength(ene) > 15:  # worker strength
                        if self.hoxy(ene.position):
                            his_agression += self.ground_strength(ene)
                #
                hally = len(self.all_bases)
                for (enetype,enepos) in self.enemy_structureinfo:
                    if enetype in self.hall_types:
                        hally -= 1
                if hally < 0:
                    # agressive
                    goal = random.choice(self.do211_goals)
                    self.do211_delay_attack = False
                elif hally == 0:
                    # neutral
                    goal = random.choice(self.do211_goals)
                    self.do211_delay_attack = False
                elif hally > 0:
                    # defensive
                    if self.random_chance(2):
                        goal = Point2((self.enemy_pos.x,100))
                    else:
                        goal = Point2((100,self.enemy_pos.y))
                    self.do211_delay_attack = True
                if his_agression >= 80: # about 2 stalkers
                    self.do211_delay_attack = False
                    goal = random.choice(self.do211_goals)
                for med in self.units(MEDIVAC):
                    if med.tag in self.do211_med:
                        mid = self.sneakymid(med.position, goal)
                        self.go_move(med, mid)
                        self.emotion_of_unittag[med.tag] = 'flying'
                self.do211_goal = goal
                self.do211_phase += 1
            elif self.do211_phase == 5:
                # all fly
                #
                goal = self.do211_goal
                #
                danger = 0
                mytile = self.maptile_of_pos(goal)
                for tile in self.nine[mytile]:
                    for ene in self.enemies_of_tile[tile]:
                        if self.ground_strength(ene) > 15:  # worker strength
                            if self.near(ene.position, goal, 10):
                                danger += self.ground_strength(ene)
                if danger >= 80: # about 2 stalkers
                    self.do211_phase == 3 # back
                else:
                    somenear = False
                    for med in self.units(MEDIVAC):
                        if med.tag in self.do211_med:
                            if self.near(med.position,goal,3):
                                somenear = True
                                # unsure goal landable
                                goal = self.place_around(AUTOTURRET,goal)
                                self.do211_goal = goal
                    #
                    # boost
                    for med in self.units(MEDIVAC):
                        if med.tag in self.do211_med:
                            if med.tag not in self.medivac_speedframe:
                                self.medivac_speedframe[med.tag] = 0
                            dospeed = False
                            if self.near(med.position, goal, 40):
                                dospeed = True
                            if med.tag in self.last_health:
                                if med.health < self.last_health[med.tag]:
                                    dospeed = True
                            if dospeed:
                                if self.frame >= self.medivac_speedframe[med.tag]:  # canspeed
                                    med(AbilityId.EFFECT_MEDIVACIGNITEAFTERBURNERS)
                                    self.medivac_speedframe[med.tag] = self.frame + 414
                    #
                    for med in self.units(MEDIVAC):
                        if med.tag in self.do211_med:
                            if self.no_move_or_near(med, 8, 4):
                                if self.near(med.position, goal, 6):
                                    if self.goal_of_unittag[med.tag] != goal: # no redo go_move
                                        self.go_move(med,goal)
                                else:
                                    mid = self.sneakymid(med.position, goal)
                                    self.go_move(med, mid)
                    #
                    if somenear:
                        self.do211_phase += 1
            elif self.do211_phase == 6:
                # fly and unload
                goal = self.do211_goal
                #
                somefar = False
                somenear = False
                for med in self.units(MEDIVAC):
                    if med.tag in self.do211_med:
                        if self.near(med.position,goal,3):
                            somenear = True
                            if self.emotion_of_unittag[med.tag] == 'flying':
                                self.emotion_of_unittag[med.tag] = 'unloading'
                                med(AbilityId.UNLOADALLAT_MEDIVAC,self.do211_goal)
                        else:
                            somefar = True
                #
                for med in self.units(MEDIVAC):
                    if med.tag in self.do211_med:
                        if self.no_move_or_near(med, 8, 4):
                            if self.near(med.position, goal, 6):
                                if self.goal_of_unittag[med.tag] != goal: # no redo go_move
                                    self.go_move(med,goal)
                            else:
                                mid = self.sneakymid(med.position, goal)
                                self.go_move(med, mid)
                #
                if (somenear) and (not somefar):
                    self.do211_phase += 1
            elif self.do211_phase == 7:
                # unload
                haspassengers = False
                for med in self.units(MEDIVAC):
                    if med.tag in self.do211_med:
                        if len(med.passengers) > 0:
                            haspassengers = True
                            # sometimes the drop_all failed partly.
                            if med.tag in self.idles:
                                med(AbilityId.UNLOADALLAT_MEDIVAC,self.do211_goal)
                for mar in self.units(MARINE): # appeared
                    if mar.tag in self.do211_mar:
                        if self.emotion_of_unittag[mar.tag] == 'flying':
                            self.emotion_of_unittag[mar.tag] = 'falling'
                            self.waitframe_of_tag[mar.tag] = self.frame + 3 * self.frames_per_second # unload time
                for scv in self.units(SCV): # appeared
                    if scv.tag in self.do211_scv:
                        if self.emotion_of_unittag[scv.tag] == 'flying':
                            self.emotion_of_unittag[scv.tag] = 'falling'
                            self.waitframe_of_tag[scv.tag] = self.frame + 3 * self.frames_per_second # unload time
                if not haspassengers:
                    self.do211_phase += 1
            elif self.do211_phase == 8:
                # attack
                somewait = False
                for mar in self.units(MARINE):
                    if mar.tag in self.do211_mar:
                        if self.emotion_of_unittag[mar.tag] == 'falling':
                            if self.frame >= self.waitframe_of_tag[mar.tag]:
                                self.emotion_of_unittag[mar.tag] = 'landed'
                                if not self.do211_delay_attack:
                                    self.attackmove(mar.tag,self.enemy_pos,5)
                            else:
                                somewait = True
                for scv in self.units(SCV):
                    if scv.tag in self.do211_scv:
                        if self.emotion_of_unittag[scv.tag] == 'falling':
                            if self.frame >= self.waitframe_of_tag[scv.tag]:
                                self.emotion_of_unittag[scv.tag] = 'landed'
                                if not self.do211_delay_attack:
                                    self.promote(scv,'reporter')
                                    pos = self.place_around(BUNKER,scv.position)
                                    self.throw_at_spot(BUNKER,pos,'do211_steps')
                            else:
                                somewait = True
                if not somewait:
                    self.do211_phase += 1
            elif self.do211_phase == 9:
                # wait
                if self.do211_delay_attack:
                    his_agression = 0
                    for ene in self.enemy_units:
                        if self.ground_strength(ene) > 15:  # worker strength
                            if self.hoxy(ene.position):
                                his_agression += self.ground_strength(ene) 
                    if his_agression >= 80: # about 2 stalkers
                        self.do211_delay_attack = False
                        self.do211_phase = 2 # back
            elif self.do211_phase == 99:
                # normalize
                for mar in self.units(MARINE):
                    if mar.tag in self.do211_mar:
                        self.do211_mar.remove(mar.tag)
                        del self.speciality_of_tag[mar.tag]
                for scv in self.units(SCV):
                    if scv.tag in self.do211_scv:
                        self.do211_scv.remove(scv.tag)
                        self.promote(scv,'idler')
                        del self.speciality_of_tag[scv.tag]
                for med in self.units(MEDIVAC):
                    if med.tag in self.do211_med:
                        self.do211_med.remove(med.tag)
                        del self.speciality_of_tag[med.tag]
                if len(self.do211_med) + len(self.do211_mar) + len(self.do211_scv) == 0:
                    self.do211_phase += 1
            elif self.do211_phase == 100:
                pass
  


    ################################# ghosts #########################################

    # rush_ghosts
    def calculate_rushghost_points(self):
        nukepos = self.enemy_pos.towards(self.map_center, -3)
        height = self.get_height(self.enemy_pos)
        # rushghost_droppos
        oneside = Point2((self.enemy_pos.x,100))
        otherside = Point2((100,self.enemy_pos.y))
        if self.sdist(oneside,self.enemynatural_pos) < self.sdist(otherside,self.enemynatural_pos):
            toside = otherside
        else:
            toside = oneside
        dropheight = self.get_height(self.enemy_pos)
        dd = 0
        self.rushghost_droppos = self.enemy_pos
        while self.get_height(self.rushghost_droppos) == dropheight:
            dd += 1
            self.rushghost_droppos = self.enemy_pos.towards(toside, dd)
        dd -= 1
        self.rushghost_droppos = self.enemy_pos.towards(toside, dd)
        improved_pos = self.undetect_point(self.rushghost_droppos)
        if self.get_height(improved_pos) == height:
            self.rushghost_droppos = improved_pos
        self.rushghost_droppos = self.place_around_atheight(AUTOTURRET,self.rushghost_droppos)
        # rushghost_callpos
        self.rushghost_callpos = nukepos.towards(self.rushghost_droppos,11)
        improved_pos = self.undetect_point(self.rushghost_callpos)
        if self.get_height(improved_pos) == height:
            if self.near(self.rushghost_callpos,improved_pos,6):
                self.rushghost_callpos = improved_pos
        # rushghost_shootpos
        self.rushghost_shootpos = self.enemy_pos.towards(self.map_center, -10)
        improved_pos = self.undetect_point(self.rushghost_shootpos)
        if self.get_height(improved_pos) == height:
            self.rushghost_shootpos = improved_pos
        # rushghost_bunkerpos
        pos = self.enemy_pos.towards(self.enemyramp_pos,-5)
        self.rushghost_bunkerpos = self.place_around_atheight(BUNKER,pos)
        # try to improve
        pos = self.rushghost_bunkerpos
        dist = 0
        while self.near(pos, nukepos, 10):
            dist += 1
            pos = self.rushghost_bunkerpos.towards(self.enemyramp_pos, -dist)
        if self.get_height(pos) == height:
            selfrushghost_bunkerpos = self.place_around_atheight(BUNKER,pos)




    async def do_rush_ghosts(self):
        if self.opening_name == 'nukerush':
            # init new medivac and starportbuilder to get control.
            if self.rushghost_phase < 'K': # then it starts heal.
                if len(self.units(MEDIVAC)) == 1:
                    for med in self.units(MEDIVAC):
                        self.speciality_of_tag[med.tag] = self.opening_name
            # get a pilot
            if self.rushghost_phase < 'F': # then medivac load starts
                if len(self.rushghost_scvs) == 0:
                    for sp in self.structures(STARPORT):
                        for scv in self.units(SCV):
                            if self.near(scv.position,sp.position,7):
                                scvt = scv.tag
                                if self.job_of_scvt[scvt] not in self.good_jobs: # building
                                    self.promote(scv,'pilot')
                                    self.rushghost_scvs.add(scvt)
                                    scv.move(sp.position)
            # phases
            if self.frame >= self.rushghost_frame: # separates the phases
                phase = self.rushghost_phase
                if phase == 'A':
                    # store ghosts temporarily in the bunker
                    if len(self.structures(BUNKER)) > 0:
                        for bar in self.structures(BARRACKS):
                            for bun in self.structures(BUNKER):
                                self.set_rally.add((bar.position,bun.position))
                                phase = 'B'
                elif phase == 'B':
                    for sp in self.structures(STARPORT):
                        self.rushghost_sp = sp.position
                        for bun in self.structures(BUNKER):
                            hasghosts = False
                            for mar in bun.passengers:
                                if mar.type_id == GHOST:
                                    hasghosts = True
                            if hasghosts:
                                bun(AbilityId.UNLOADALL_BUNKER)
                        phase = 'C'
                        for bar in self.structures(BARRACKS):
                            door = bar.position.towards(self.map_center,3)
                            self.set_rally.add((bar.position,door))
                elif phase == 'C':
                    allthere = True
                    # energy for an emp vs terran
                    if self.enemy_species == 'terran':
                        allthere = False
                        for ghost in self.units(GHOST):
                            tag = ghost.tag
                            if tag in self.rush_ghosts:
                                if ghost.energy >= 150: # cloack+emp+50
                                    allthere = True
                    allthere = allthere and (len(self.units(MEDIVAC)) > 0)
                    allthere = allthere and self.we_nearly_finished_a(PERSONALCLOAKING,9)
                    allthere = allthere and self.we_nearly_finished_a(NUKESILONOVA,9)
                    for ghost in self.units(GHOST):
                        tag = ghost.tag
                        if tag in self.rush_ghosts:
                            if not self.near(ghost.position,self.rushghost_sp,5):
                                allthere = False
                                if tag in self.idles:
                                    ghost.move(self.rushghost_sp)
                    if allthere:
                        self.rushghost_passengers = set()
                        for ghost in self.units(GHOST):
                            tag = ghost.tag
                            if tag in self.rush_ghosts:
                                self.rushghost_passengers.add(tag)
                        todomax = 2
                        for scv in self.units(SCV):
                            if self.near(scv.position,self.rushghost_sp,5):
                                if todomax > 0:
                                    todomax -= 1
                                    self.rushghost_passengers.add(scv.tag)
                        phase = 'D'
                elif phase == 'D':
                    maxenergy = 0
                    for ghost in self.units(GHOST):
                        tag = ghost.tag
                        if tag in self.rush_ghosts:
                            maxenergy = max(ghost.energy,maxenergy)
                    for ghost in self.units(GHOST):
                        tag = ghost.tag
                        if tag in self.rush_ghosts:
                            ghost(AbilityId.BEHAVIOR_HOLDFIREON_GHOST)
                            if ghost.energy == maxenergy:
                                self.rushghost_tonuke = tag
                            else:
                                self.rushghost_toemp = tag
                            phase = 'E'
                elif phase == 'E':
                    for ghost in self.units(GHOST):
                        tag = ghost.tag
                        if tag in self.rush_ghosts:
                            abilities = (await self.get_available_abilities([ghost]))[0]
                            if AbilityId.BEHAVIOR_CLOAKON_GHOST in abilities:
                                ghost(AbilityId.BEHAVIOR_CLOAKON_GHOST)
                    phase = 'F'
                elif phase == 'F': # also entered from 'G'
                    for med in self.units(MEDIVAC):
                        if med.tag in self.idles:
                            todo = 1
                            for unt in self.units:
                                tag = unt.tag
                                if tag in self.rushghost_passengers:
                                    if todo > 0:
                                        todo -= 1
                                        med(AbilityId.LOAD_MEDIVAC,unt)
                                        phase = 'G'
                elif phase == 'G':
                    for med in self.units(MEDIVAC):
                        if med.tag in self.idles:
                            if len(med.passengers) < len(self.rushghost_passengers):
                                phase = 'F'
                            else:
                                phase = 'H'
                elif phase == 'H':
                    self.calculate_rushghost_points()
                    for med in self.units(MEDIVAC):
                        mid = self.sneakymid(med.position,self.rushghost_droppos)
                        self.go_move(med, mid)
                        phase = 'I'
                elif phase == 'I':
                    for med in self.units(MEDIVAC):
                        self.rushghost_droppos = self.place_around_atheight(AUTOTURRET,self.rushghost_droppos)
                        goal = self.rushghost_droppos
                        if med.tag not in self.medivac_speedframe:
                            self.medivac_speedframe[med.tag] = 0
                        dospeed = False
                        if self.near(med.position,goal,30):
                            dospeed = True
                        if med.tag in self.last_health:
                            if med.health < self.last_health[med.tag]:
                                dospeed = True
                        if dospeed:
                            if self.frame >= self.medivac_speedframe[med.tag]: # canspeed
                                med(AbilityId.EFFECT_MEDIVACIGNITEAFTERBURNERS)
                                self.medivac_speedframe[med.tag] = self.frame + 414
                        if self.no_move_or_near(med, 8, 4):
                            if self.near(med.position,goal,1):
                                med(AbilityId.UNLOADALLAT_MEDIVAC,self.rushghost_droppos)
                                phase = 'J'
                            elif self.near(med.position,goal,8):
                                med.move(goal)
                            else:
                                mid = self.sneakymid(med.position, goal)
                                self.go_move(med, mid)
                elif phase == 'J':
                    # reclaim dropped scvs. They land as idler and are misused immediately.
                    for scv in self.units(SCV):
                        scvt = scv.tag
                        if scvt in self.rushghost_scvs:
                            if self.job_of_scvt[scvt] != 'pilot':
                                self.promote(scv,'pilot')
                                self.log_command('scv(AbilityId.STOP)')  # stop moving
                                scv(AbilityId.STOP)
                    for med in self.units(MEDIVAC):
                        if len(med.passengers) == 0:
                            all_at_ease = True
                            for unt in self.units:
                                if unt.tag in self.rushghost_passengers:
                                    if unt.tag not in self.idles:
                                        all_at_ease = False
                            if all_at_ease:
                                phase = 'K'
                elif phase == 'K':
                    # allow medivac to heal normal
                    for med in self.units(MEDIVAC):
                        if med.tag in self.speciality_of_tag:
                            del self.speciality_of_tag[med.tag]
                    # build an offensive distraction bunker
                    for scv in self.units(SCV):
                        scvt = scv.tag
                        if scv.tag in self.rushghost_scvs:
                            self.promote(scv, 'reporter')
                            if self.rushghost_bunker:
                                self.rushghost_bunker = False
                                self.throw_at_spot(BUNKER, self.rushghost_bunkerpos, 'do_rush_ghosts')
                                scv.move(self.rushghost_bunkerpos)
                    # emp townhall
                    # goto nukepos
                    for ghost in self.units(GHOST):
                        tag = ghost.tag
                        if tag in self.rush_ghosts:
                            if self.enemy_species == 'terran':
                                if tag == self.rushghost_toemp:
                                    abilities = (await self.get_available_abilities([ghost]))[0]
                                    if AbilityId.EMP_EMP in abilities:
                                        pos = self.enemy_pos.towards(self.map_center,2)
                                        ghost(AbilityId.EMP_EMP, pos)
                            if tag == self.rushghost_tonuke:
                                ghost.move(self.rushghost_callpos)
                    phase = 'L'
                elif phase == 'L':
                    for ghost in self.units(GHOST):
                        tag = ghost.tag
                        if tag == self.rushghost_tonuke:
                            if self.near(ghost.position,self.rushghost_callpos,1):
                                abilities = (await self.get_available_abilities([ghost]))[0]
                                if AbilityId.TACNUKESTRIKE_NUKECALLDOWN in abilities:
                                    pos = self.enemy_pos.towards(self.map_center,-3)
                                    ghost(AbilityId.TACNUKESTRIKE_NUKECALLDOWN, pos)
                                    phase = 'M'
                        elif tag == self.rushghost_toemp:
                            if tag in self.idles:
                                ghost.move(self.rushghost_shootpos)
                elif phase == 'M':
                    # reuse ghosts when idle
                    for ghost in self.units(GHOST):
                        tag = ghost.tag
                        if tag in self.rush_ghosts:
                            if tag in self.rushghost_retired:
                                if tag in self.idles:
                                    ghost.move(self.loved_pos)
                                elif self.near(ghost.position,self.loved_pos,20):
                                    ghost(AbilityId.BEHAVIOR_HOLDFIREOFF_GHOST) # ought to be superfluous
                                    self.rush_ghosts.remove(tag)
                                    self.ghost_requests.append('army_ghost')
                            else: # there is one more thing we ask you, ghost.
                                if ghost.energy < 10:
                                    self.rushghost_retired.add(tag)
                                    ghost.move(self.loved_pos)
                                elif tag in self.idles:
                                    if self.near(self.rushghost_shootpos,ghost.position,1):
                                        ghost(AbilityId.BEHAVIOR_HOLDFIREOFF_GHOST)
                                        ghost(AbilityId.HOLDPOSITION)
                                    else:
                                        ghost.move(self.rushghost_shootpos)
                # enz
                if phase != self.rushghost_phase:
                    self.rushghost_frame = self.frame + 20
                    self.rushghost_phase = phase

    # army_ghosts
    def ghostmove(self,tag,goal,hangout):
        # makes my ghost unit move to goal, sniping enemies in range.
        # tag must be of an army_ghost.
        # hangout is the size of the area it can hang out after the goal is reached.
        self.ghostmove_state[tag] = 'rest'
        self.ghostmove_goal[tag] = goal
        self.ghostmove_goalreached[tag] = False
        self.ghostmove_hangout[tag] = hangout
        self.ghostmove_fightgoal[tag] = self.nowhere
        self.ghostmove_goaltried[tag] = 0
        self.ghostmove_last_energy[tag] = 0
        self.ghostmove_snipeend[tag] = 0

    def handle_ghost_requests(self):
        # For a new army_ghost, do:
        #    produce a ghost
        #    self.ghost_requests.append('army_ghost')
        # This procedure may assign it to army_ghosts, and call
        #    self.new_army_ghost(tag)
        #
        if len(self.ghost_requests) > 0:
            for ghost in self.units(GHOST):
                tag = ghost.tag
                if tag not in self.rush_ghosts:
                    if tag not in self.nuke_ghosts:
                        if tag not in self.army_ghosts:
                            # a new one
                            kind = self.ghost_requests[0]
                            if kind == 'nuke_ghost':
                                self.nuke_ghosts.add(tag)
                            elif kind == 'army_ghost':
                                self.army_ghosts.add(tag)
                            elif kind == 'rush_ghost':
                                self.rush_ghosts.add(tag)
                            del self.ghost_requests[0]

    def do_ghostmove(self):
        # states:
        #    rest       Not moving, e.g. goal reached
        #    approach   Seeing a target, going to snipe
        #    snipe      Carefully aiming
        #    move       Going in the direction of the goal
        #    role       Retreat on low energy
        #    home       Retreated
        #    host       Halted on seeing a threat
        if len(self.army_ghosts) > 0:
            # cleanup
            if self.frame % 29 == 28:
                todel = set()
                for tag in self.army_ghosts:
                    if tag not in self.all_unittags:
                        todel.add(tag)
                for tag in todel:
                    self.army_ghosts.remove(tag)
            # init ghostmove_* is done by the caller via ghostmove()
            if self.enemy_species == 'zerg':
                min_energy = 50 # snipe
            else:
                min_energy = 75 # emp
            # snipe biological, range 10, 32 frames, me no damage, do 170 damage
            for ghost in self.units(GHOST):
                tag = ghost.tag
                if tag in self.ghostmove_state: # implies army_ghosts
                    mypos = ghost.position
                    state = self.ghostmove_state[tag]
                    goal = self.ghostmove_goal[tag]
                    goalreached = self.ghostmove_goalreached[tag]
                    goaltried = self.ghostmove_goaltried[tag]
                    hangout = self.ghostmove_hangout[tag]
                    snipeend = self.ghostmove_snipeend[tag]
                    last_energy = self.ghostmove_last_energy[tag]
                    fightgoal = self.ghostmove_fightgoal[tag]
                    if goalreached:
                        tolerance = hangout
                    else:
                        tolerance = 1
                    if state in {'move','role','host'}:
                        it_can_hit_me = False
                        minsd = 10*10
                        mytile = self.maptile_of_pos(mypos)
                        for tile in self.nine[mytile]:
                            for ene in self.enemies_of_tile[tile]:
                                enepos = ene.position
                                sd = self.sdist(mypos, enepos)
                                if sd < minsd:
                                    for weapon in ene._weapons:
                                        if weapon.type in TARGET_GROUND:
                                            it_can_hit_me = True
                        if it_can_hit_me:
                            if state in {'move','role'}:
                                state = 'host'
                                ghost(AbilityId.STOP)
                        else:
                            if state == 'host':
                                state = 'rest'
                    if ghost.energy < min_energy:
                        if state in {'rest','move'}:
                            state = 'role' # retreat on low energy
                            ghost.move(self.loved_pos)
                    else: # enough energy
                        if state in {'role','home'}:
                            state = 'move'
                            ghost.move(goal)
                            goalreached = False
                            goaltried = 0
                            tolerance = 1
                        if state in {'rest','move','approach'}:
                            moveplan = self.nowhere
                            mytile = self.maptile_of_pos(mypos)
                            for tile in self.nine[mytile]:
                                for ene in self.enemies_of_tile[tile]:
                                    if ene.type_id not in {EGG, LARVA, AUTOTURRET}:
                                        enepos = ene.position
                                        if ene.health > 85:  # avoid workers, zerglings
                                            if ene.type_id in {SENTRY, HIGHTEMPLAR, PHOENIX, ORACLE, MOTHERSHIP,
                                                               SHIELDBATTERY, GHOST, MEDIVAC, RAVEN, BANSHEE, ORBITALCOMMAND}:
                                                if self.near(mypos, enepos, 10):  # demanded for emp
                                                    ghost(AbilityId.EMP_EMP, ene.position)
                                                    state = 'snipe'
                                                    snipeend = self.frame + 4
                                                    last_energy = ghost.energy
                                                else:
                                                    moveplan = enepos.towards(mypos, 9.5)
                                            elif ene.is_biological: # demanded for snipe
                                                if self.near(mypos,enepos,10): # demanded for snipe
                                                    ghost(AbilityId.EFFECT_GHOSTSNIPE,ene)
                                                    state = 'snipe'
                                                    snipeend = self.frame + 32
                                                    last_energy = ghost.energy
                                                else:
                                                    moveplan = enepos.towards(mypos,9.5)
                            if moveplan != self.nowhere:
                                if state in {'rest','move'}:
                                    state = 'approach'
                                    ghost.move(moveplan)
                                    fightgoal = moveplan
                    # interrupted snipe
                    if state == 'snipe': # implies last_energy
                        if ghost.energy > last_energy + 10:
                            # interrupted snipe
                            state = 'rest'
                        last_energy = ghost.energy
                    # succeeded snipe
                    if state == 'snipe': # implies snipeend
                        if self.frame > snipeend:
                            # ended snipe
                            state = 'rest'
                    # end approach
                    if state == 'approach': # implies fightgoal
                        if self.near(mypos,fightgoal,0.5):
                            state = 'rest'
                        if tag in self.idles:
                            state = 'rest'
                    #                 
                    if state == 'rest':
                        if self.near(mypos, goal, tolerance):
                            goalreached = True
                        else:
                            state = 'move'
                    if state == 'home':
                        if not self.near(mypos, self.loved_pos, 10):
                            state = 'role'
                    if state == 'move':
                        if self.near(mypos, goal, tolerance):
                            state = 'rest'
                        elif tag in self.idles:
                            ghost.move(goal)
                            goaltried += 1
                            if goaltried >= 4:
                                goalreached = True
                    if state == 'role': # retreat on low energy
                        if self.near(mypos, self.loved_pos, 10):
                            state = 'home'
                        elif tag in self.idles:
                            ghost.move(self.loved_pos)
                    #
                    #print('debug '+str(tag)+' '+state+' '+str(ghost.weapon_cooldown))
                    #
                    self.ghostmove_state[tag] = state
                    self.ghostmove_goal[tag] = goal
                    self.ghostmove_goalreached[tag] = goalreached
                    self.ghostmove_goaltried[tag] = goaltried
                    self.ghostmove_hangout[tag] = hangout
                    self.ghostmove_snipeend[tag] = snipeend
                    self.ghostmove_last_energy[tag] = last_energy
                    self.ghostmove_fightgoal[tag] = fightgoal
                    #

    # nuke_ghosts
    def get_nuke_target(self, ghostpos):
        # -> self.nuke_target
        nuke_targets = set()
        bestquality = -99999
        for tp in self.enemy_structureinfo:
            (typ, pos) = tp
            expo = self.expo_of_pos(pos)
            quality = - self.circledist(pos, ghostpos)
            for other_tp in self.enemy_structureinfo_of_expo[expo]:
                (other_typ, other_pos) = other_tp
                if self.near(pos, other_pos, 4):
                    quality += 20
            if quality > bestquality:
                bestquality = quality
                nuke_targets = {pos}
            elif quality == bestquality:
                nuke_targets.add(pos)
        if len(nuke_targets) == 0:
            self.nuke_target = self.enemy_pos
        elif self.nuke_target not in nuke_targets:
            bestsd = 99999
            for nt in nuke_targets:
                sd = self.sdist(ghostpos, nt)
                if sd < bestsd:
                    bestsd = sd
                    self.nuke_target = nt

    async def nuke_fun(self):
        # startup
        if self.ghost_phase == 'A':
            if (self.supply_used >= 180):
                self.ghost_phase = 'B'
        # fallback
        if self.ghost_phase > 'A':
            self.log_success('ghost_phase ' + self.ghost_phase)
            self.ghost_calmdown = max(0, self.ghost_calmdown - self.chosen_game_step)
            # phase fall back
            if self.we_started_amount(GHOSTACADEMY) < 1:
                self.ghost_phase = min('B', self.ghost_phase)
            if self.we_started_amount(BARRACKS) < 2:  # Force second barracks as the first sometimes cannot lab.
                self.ghost_phase = min('B', self.ghost_phase)
            if self.we_started_amount(BARRACKSTECHLAB) < 1:
                self.ghost_phase = min('B', self.ghost_phase)
            if self.we_started_amount(FACTORY) < 1:
                self.ghost_phase = min('B', self.ghost_phase)
            if len(self.nuke_ghosts) < 1:
                self.ghost_phase = min('C', self.ghost_phase)
            # nuke_ghosts alive
            todel = set()
            for ghost in self.units(GHOST):
                if ghost.tag not in self.nuke_ghosts:
                    todel.add(ghost.tag)
            self.nuke_ghosts -= todel
            # phases
            phase = self.ghost_phase
            if self.ghost_calmdown == 0:
                if phase == 'B':
                    # build buildings
                    done = 0
                    if self.we_started_amount(GHOSTACADEMY) < 1:
                        if self.allow_throw(GHOSTACADEMY):
                            self.throw_anywhere(GHOSTACADEMY, 'nuke_fun')
                    else:
                        done += 1
                    if self.we_started_amount(BARRACKS) < 2:
                        if self.allow_throw(BARRACKS):
                            self.throw_anywhere(BARRACKS, 'nuke_fun')
                    else:
                        done += 1
                    if self.we_started_amount(BARRACKSTECHLAB) < 1:
                        if self.allow_throw(BARRACKSTECHLAB):
                            self.throw_anywhere(BARRACKSTECHLAB, 'nuke_fun')
                    else:
                        done += 1
                    if self.we_started_amount(FACTORY) < 1:
                        if self.allow_throw(FACTORY):
                            self.throw_anywhere(FACTORY, 'nuke_fun')
                    else:
                        done += 1
                    # continue
                    if done >= 4:
                        phase = 'C'
                elif phase == 'C':
                    # buildings are started
                    # build cloack, ghosts, nukes
                    done = 0
                    if len(self.nuke_ghosts) > 0:
                        done += 1
                    else:
                        requested = 0
                        for req in self.ghost_requests:
                            if req == 'nuke_ghost':
                                requested += 1
                        if requested == 0:
                            self.ghost_requests.append('nuke_ghost')
                        if not self.we_started_a(GHOST):
                            if self.allow_throw(GHOST):
                                self.throw_anywhere(GHOST, 'nuke_fun')
                    if self.we_started_amount(PERSONALCLOAKING) < 1:
                        if self.allow_throw(PERSONALCLOAKING):
                            self.throw_anywhere(PERSONALCLOAKING, 'nuke_fun')
                    else:
                        done += 1
                    if self.we_started_amount(NUKESILONOVA) < 1:
                        if self.allow_throw(NUKESILONOVA):
                            for ga in self.structures(GHOSTACADEMY):
                                if ga.tag in self.readies:
                                    if ga.tag in self.idles:
                                        ga(AbilityId.BUILD_NUKE)
                    else:
                        done += 1
                    if done >= 3:
                        phase = 'D'
                elif phase == 'D':
                    # wait for ghost some energy, nuke, restdura max 20 sec
                    # continue
                    done = 0
                    for ghost in self.units(GHOST):
                        if ghost.tag not in self.army_ghosts:
                            done = 1 # there are nuke_ghosts
                            if len(self.nuke_ghosts) < 1:
                                self.nuke_ghosts.add(ghost.tag)
                    for ghost in self.units(GHOST):
                        if ghost.tag in self.nuke_ghosts:
                            if ghost.energy < 100:
                                done = 0 # there are nuke_ghosts with low energy
                    if self.we_started_amount(NUKESILONOVA) >= 1:
                        done += 1 # there are started nukes
                    for (martype, bartype, pos, dura) in self.eggs:
                        if (martype == NUKESILONOVA) and (dura > 20):
                            done -= 1 # there are child nukes
                    if done >= 2:
                        phase = 'E'
                        # init
                        for ghost in self.units(GHOST):
                            if ghost.tag in self.nuke_ghosts:
                                pos = ghost.position
                        self.get_nuke_target(pos)
                elif phase == 'E':
                    # there are ghosts and nukes and a target
                    # if none close to nuking place, go there
                    close = False
                    for ghost in self.units(GHOST):
                        if ghost.tag in self.nuke_ghosts:
                            if self.near(ghost.position, self.nuke_target, 13):
                                close = True
                    if close:
                        phase = 'G'
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
                            for tp in self.enemy_structureinfo_plus:
                                (typ, pos, finish) = tp
                                if typ in self.antiair_detector:
                                    if self.near(goal, pos, self.detection_range):
                                        if finish < self.frame + 200:  # finished or within 8 sec
                                            tooclose = True
                        for ghost in self.units(GHOST):
                            if ghost.tag in self.nuke_ghosts:
                                self.go_move(ghost, goal)
                        phase = 'F'
                elif phase == 'F':
                    # moving to goals
                    for ghost in self.units(GHOST):
                        if ghost.tag in self.nuke_ghosts:
                            if self.near(ghost.position, self.nuke_target, 70):
                                abilities = (await self.get_available_abilities([ghost]))[0]
                                if AbilityId.BEHAVIOR_CLOAKON_GHOST in abilities:
                                    ghost(AbilityId.BEHAVIOR_CLOAKON_GHOST)
                            if ghost.tag in self.goal_of_unittag:  # dont ask me, it occurred
                                if self.no_move(ghost, 64):
                                    self.get_nuke_target(ghost.position)
                                    phase = 'E'
                elif phase == 'G':
                    # goal reached
                    # call nuke
                    done = 0
                    for ghost in self.units(GHOST):
                        if ghost.tag in self.nuke_ghosts:
                            if self.near(ghost.position, self.nuke_target, 13):
                                abilities = (await self.get_available_abilities([ghost]))[0]
                                if AbilityId.TACNUKESTRIKE_NUKECALLDOWN in abilities:
                                    ghost(AbilityId.TACNUKESTRIKE_NUKECALLDOWN, self.nuke_target)
                                    fleepos = self.nuke_target.towards(ghost.position, 16)
                                    ghost.move(fleepos, queue=True)
                                    done += 1
                    # continue
                    if done >= 1:
                        phase = 'H'
                elif phase == 'H':
                    # waiting for strike
                    phase = 'I'
                    # init
                    for ghost in self.units(GHOST):
                        if ghost.tag in self.nuke_ghosts:
                            self.go_move(ghost, self.loved_pos)
                elif phase == 'I':
                    # walking home
                    done = 0
                    for ghost in self.units(GHOST):
                        if ghost.tag in self.nuke_ghosts:
                            if not self.near(ghost.position, self.nuke_target, 70):
                                abilities = (await self.get_available_abilities([ghost]))[0]
                                if AbilityId.BEHAVIOR_CLOAKOFF_GHOST in abilities:
                                    ghost(AbilityId.BEHAVIOR_CLOAKOFF_GHOST)
                            if not self.no_move(ghost, 64):
                                done -= 1
                    # continue
                    if done >= 0:
                        phase = 'C'
                        # init
                        for ghost in self.units(GHOST):
                            if ghost.tag in self.nuke_ghosts:
                                abilities = (await self.get_available_abilities([ghost]))[0]
                                if AbilityId.BEHAVIOR_CLOAKOFF_GHOST in abilities:
                                    ghost(AbilityId.BEHAVIOR_CLOAKOFF_GHOST)
            # write phase, cooldown
            if phase != self.ghost_phase:
                self.ghost_calmdown = 80
                self.ghost_phase = phase


    # workerfight administration wa_ ######################################################
    # As long as no other units are out,
    # this administration tries to grasp the worker-hits-worker counts.
    #
    # wa_ihitted   total hit count
    # wa_iwashit   total being hit count
    # wa_repair    total repair
    # wa_hitframe  per worker, estimated frame of the last hit dealt
    # wa_lastscvs  set of own scv (tag,position,health)
    # wa_lastene   set of enemy worker (tag,position,canhit)
    
    def wa_step(self):
        # log
        print('hitted '+str(self.wa_ihitted)+'   was hit '+str(self.wa_iwashit)+'   repaired '+str(self.wa_repair))
        for scv in self.units(SCV):
            for order in scv.orders:
                if order.ability.id == AbilityId.ATTACK:
                    if type(order.target) == int:
                        for ene in self.enemy_real_structures:
                            if ene.tag == order.target:
                                print('an scv attacks ' + ene.name)
        # init wa_hitframe
        for ene in self.enemy_units:  # actual visible
            if ene.type_id in {DRONE, SCV, PROBE}:
                if ene.tag not in self.wa_hitframe:
                    self.wa_hitframe[ene.tag] = -99999
        for scv in self.units(SCV):
            if scv.tag not in self.wa_hitframe:
                self.wa_hitframe[scv.tag] = -99999
        # repair
        for scv in self.units(SCV):
            for (scvt, lastscvpos, lastscvhealth) in self.wa_lastscvs:
                if scvt == scv.tag:
                    if scv.health > lastscvhealth:
                        self.wa_repair += (scv.health - lastscvhealth)
        # hitting
        for scv in self.units(SCV):
            for (scvt, lastscvpos, lastscvhealth) in self.wa_lastscvs:
                if scvt == scv.tag:
                    if scv.weapon_cooldown > 10:
                        hitworker = False
                        minsd = 99999
                        for (enetag, lastenepos,canhit) in self.wa_lastene:
                            if self.near(lastenepos, lastscvpos, 0.95):  # 0.85 theory
                                hitworker = True
                            minsd = min(minsd,self.sdist(lastenepos, lastscvpos))
                        estiframe = self.frame - (24 - scv.weapon_cooldown)
                        if estiframe > self.wa_hitframe[scvt] + 16:
                            self.wa_hitframe[scvt] = estiframe
                            if hitworker:
                                self.wa_ihitted += 1
                            else:
                                print('hit a brick? '+str(minsd))
        # being hit
        for scv in self.units(SCV):
            for (scvt, lastscvpos, lastscvhealth) in self.wa_lastscvs:
                if scvt == scv.tag:
                    if scv.health < lastscvhealth:
                        # I was bitten
                        bites = round((lastscvhealth - scv.health)/5)
                        self.wa_iwashit += bites
                        crulpits = set()
                        for (enetag, lastenepos,canhit) in self.wa_lastene:
                            if canhit:
                                if self.near(lastenepos, lastscvpos, 0.95):  # 0.85 theory
                                    crulpits.add(enetag)
                        if len(crulpits) <= bites:
                            for crulpittag in crulpits:
                                self.wa_hitframe[crulpittag] = self.frame - 2
        # being hit to death
        for (scvt,lastscvpos,lastscvhealth) in self.wa_lastscvs:
            living = False
            for scv in self.units(SCV):
                if scv.tag == scvt:
                    living = True
            if not living:
                bites = 0
                mishealth = lastscvhealth
                while mishealth > 0:
                    mishealth -= 5
                    bites += 1
                crulpits = set()
                # actual visible does not work after death
                for (enetag,lastenepos,canhit) in self.wa_lastene:
                    if canhit:
                        if self.near(lastenepos, lastscvpos, 0.95):  # 0.85 theory
                            crulpits.add(enetag)
                # the scv could have gone into gas, or could have been bitten to death
                if len(crulpits) >= bites:
                    self.wa_iwashit += bites
                    if len(crulpits) <= bites:
                        for crulpittag in crulpits:
                            self.wa_hitframe[crulpittag] = self.frame - 2
        # wa_lastscvs
        self.wa_lastscvs = set()
        for scv in self.units(SCV):
            self.wa_lastscvs.add((scv.tag,scv.position,scv.health))
        # wa_lastene
        self.wa_lastene = set()
        for ene in self.enemy_units:  # actual visible
            if ene.type_id in {DRONE, SCV, PROBE}:
                canhit = (self.wa_hitframe[ene.tag] < self.frame - 16)
                self.wa_lastene.add((ene.tag,ene.position,canhit))

    # workerrush ###########################################################################

    def fleecirclemove(self, scv):
        mypole = self.fleepole[scv.tag]
        topos = self.fleepolepos[mypole]
        if not self.near(scv.position, self.followers, 10):
            scv.move(topos)
        elif self.near(scv.position, topos, 3):
            self.fleepole[scv.tag] = (self.fleepole[scv.tag] + 1) % 16
            mypole = self.fleepole[scv.tag]
            topos = self.fleepolepos[mypole]
            scv.move(topos)
        elif len(scv.orders) == 0:
            scv.move(topos)

    def calculate_nextpos(self):
        # calculate nextpos for all units.
        # This handles the delay of orders, whatever the gamestep.
        # Only useful for close encounters
        for unt in self.units | self.enemy_units:
            if unt.tag in self.lastpos_of_unittag:
                last = self.lastpos_of_unittag[unt.tag]
                next = Point2((2 * unt.position.x - last.x, 2 * unt.position.y - last.y))
                self.nextpos_of_unittag[unt.tag] = next
            else:
                self.nextpos_of_unittag[unt.tag] = unt.position
            self.lastpos_of_unittag[unt.tag] = unt.position

    def groupmight(self, listofhealth) -> float:
        might = 0
        loh = listofhealth.copy()
        n = len(loh)
        while n > 0:
            minhealth = 99999
            for health in loh:
                minhealth = min(health,minhealth)
            might += minhealth * n
            del loh[loh.index(minhealth)]
            n -= 1
        return might

    def replatoon(self):
        # self.platoons
        self.platoons = []
        torank = set()
        for scv in self.units(SCV):
            if scv.tag in self.speciality_of_tag:
                if self.speciality_of_tag[scv.tag] == 'workerrush':
                    torank.add(scv.tag)
        while len(torank) > 0:
            # in torank none addable to an existing platoon
            platoon = set()
            for scv in self.units(SCV):
                if scv.tag in torank:
                    bestscv = scv
            platoon.add(bestscv.tag)
            torank.remove(bestscv.tag)
            for onescv in self.units(SCV):
                if onescv.tag in torank:
                    mayadd = False
                    for platoonscv in self.units(SCV):
                        if platoonscv.tag in platoon:
                            if self.near(onescv.position,platoonscv.position,2):
                                mayadd = True
                    if mayadd:
                        platoon.add(onescv.tag)
                        torank.remove(onescv.tag)
            self.platoons.append(platoon)
        # self.platooncenters
        self.platooncenters = []
        for platoon in self.platoons:
            n = 0
            sx = 0
            sy = 0
            for scv in self.units(SCV):
                if scv.tag in platoon:
                    n += 1
                    sx += scv.position.x
                    sy += scv.position.y
            center = Point2((sx/n,sy/n))
            self.platooncenters.append(center)
        # self.platoonenemies
        self.platoonenemies = []
        for platoon in self.platoons:
            self.platoonenemies.append(set())
        for ene in self.enemy_units: # actual visible
            if ene.tag in self.enemymelee:
                bestsd = 99999
                nr = -1
                for center in self.platooncenters:
                    nr += 1
                    sd = self.sdist(ene.position, center)
                    if sd < bestsd:
                        bestsd = sd
                        bestnr = nr
                if bestsd < 4*4:
                    self.platoonenemies[nr].add(ene.tag)
        # self.platoonenemycenters
        self.platoonenemycenters = []
        for platoonenemy in self.platoonenemies:
            n = 0
            sx = 0
            sy = 0
            for ene in self.enemy_units: # actual visible
                if ene.tag in platoonenemy:
                    n += 1
                    sx += ene.position.x
                    sy += ene.position.y
            if n == 0:
                center = self.nowhere
            else:
                center = Point2((sx/n,sy/n))
            self.platoonenemycenters.append(center)
        # self.platoonmight
        self.platoonmight = []
        for pid in range(0,len(self.platoons)):
            platoon = self.platoons[pid]
            platoonenemy = self.platoonenemies[pid]
            loh = []
            for scv in self.units(SCV):
                if scv.tag in platoon:
                    loh.append(scv.health)
            might = self.groupmight(loh)
            loh = []
            for ene in self.enemy_units: # actual visible
                if ene.tag in platoonenemy:
                    loh.append(ene.health+ene.shield)
            might -= self.groupmight(loh)
            self.platoonmight.append(might)
        # platoonplans
        self.platoonplans = []
        stri = 'platoonplans:'
        for pid in range(0,len(self.platoons)):
            platoon = self.platoons[pid]
            platoonenemy = self.platoonenemies[pid]
            might = self.platoonmight[pid]
            if len(platoonenemy) == 0:
                plan = 'neutral'
            elif might > 0:
                plan = 'agressive'
            elif might < -100:
                plan = 'flee'
            else:
                plan = 'defensive'
            self.platoonplans.append(plan)
            stri = stri + ' ' + plan
        self.log_success(stri)
        # platoongoals
        self.platoongoals = []
        for pid in range(0,len(self.platoons)):
            platoon = self.platoons[pid]
            me = self.platooncenters[pid]
            her = self.platoonenemycenters[pid]
            plan = self.platoonplans[pid]
            if plan == 'neutral':
                goal = self.enemy_pos.towards(self.map_center,-3)
            elif plan == 'agressive':
                goal = her
            elif plan == 'defensive':
                goal = Point2((3 * me.x - 2 * her.x, 3 * me.y - 2 * her.y))
            elif plan == 'flee':
                goal = self.loved_pos.towards(self.map_center,-3)
            self.platoongoals.append(goal)
        #

    def get_rushvictims(self,myposition,bound) -> int:
        reachable = 0
        for ene in self.enemy_units: # actual visible
            if ene.tag in self.enemymelee:
                if self.near(self.nextpos_of_unittag[ene.tag], myposition, bound):
                    if reachable == 0:
                        self.rushvictim = ene
                    reachable += 1
                    if ene.health < self.rushvictim.health:
                        self.rushvictim = ene
                    elif ene.health == self.rushvictim.health:
                        if ene.tag < self.rushvictim.tag:
                            self.rushvictim = ene
        return reachable

    def init_workerrush(self):
        if (self.opening_name.find('workerrush') >= 0):
            # minerals to move towards: hisrampmim, hisfarmim, hismidmim, homemim, sidemim
            hisexpo = self.expo_of_pos(self.enemy_pos)
            leftsd = 99999
            rightsd = 99999
            for (mimpos,mimt) in self.minerals_of_expo[hisexpo]:
                if self.near(mimpos, self.enemy_pos, 8):
                    sd = self.sdist(mimpos, self.hisleft)
                    if sd < leftsd:
                        leftsd = sd
                        hisleftmim = (mimpos,mimt)
                        hisleftmimpos = mimpos
                    sd = self.sdist(mimpos, self.hisright)
                    if sd < rightsd:
                        rightsd = sd
                        hisrightmim = (mimpos,mimt)
                        hisrightmimpos = mimpos
            if self.sdist(hisleftmimpos, self.enemyramp_pos) < self.sdist(hisrightmimpos,self.enemyramp_pos):
                self.hisrampmim = hisleftmim
                self.hisfarmim = hisrightmim
            else:
                self.hisrampmim = hisrightmim
                self.hisfarmim = hisleftmim
            # hismidmim
            lowestq = 99999
            for (mimpos,mimt) in self.minerals_of_expo[hisexpo]:
                if self.near(mimpos, self.enemy_pos, 8):
                    q = self.sdist(mimpos, hisleftmimpos) + self.sdist(mimpos,hisrightmimpos)
                    if q < lowestq:
                        lowestq = q
                        self.hismidmim = (mimpos,mimt)
            # homemim
            homeexpo = self.expo_of_pos(self.loved_pos)
            minsd = 99999
            for (mimpos,mimt) in self.minerals_of_expo[homeexpo]:
                sd = self.sdist(mimpos, self.hisleft)
                if sd < minsd:
                    minsd = sd
                    self.homemim = (mimpos,mimt)
            # sidemim
            bestsd = 99999
            for (mimpos,mimt) in self.all_minerals:
                sd = self.sdist(mimpos,self.hisleft)
                if sd < bestsd:
                    bestsd = sd
                    self.sidemim = (mimpos,mimt)
            # turningpoint
            (mimpos,mimt) = self.hisrampmim
            self.turningpoint = self.enemy_pos.towards(mimpos,-3)


    def do_workerrush(self):
        if (self.opening_name.find('workerrush') >= 0) and (self.workerrushstate != 'ended'):
            # slow
            if (self.frame > 1100) and (self.frame < 1100 + 20):
                self.slowdown_frames =  self.workerrushstopframe - 1100
            # emotions:
            agressive = {'brave','jumping','biting','bouncing','afraid','looting'}
            defensive = {'fleeing','firstaid','inrepair','circling','teasing'}
            neutral = {'ingoing'}
            #
            # brave: mineralwalking to hisrampmim or hisfarmim. Cooled (<7). Near enemy minerals.
            # looting: like brave, far from enemies, attacking a structure.
            # jumping: near an enemy. Cooled. Mineralwalking, sometimes walking.
            # biting: close to an enemy. Cooled.
            # bouncing: a few frames of mineralwalking back. After biting or if very threatened.
            # afraid: after bouncing, trying to get distance to the enemy.
            # firstaid: ready to repair.
            # fleeing: mineralwalking to some mineral. Often low health, will not bite.
            # circling: walking around in a corner of the map
            # inrepair: Going to an own scv or repairing one. May be repaired.
            # ingoing: mineralwalking to hisrampmim or hisfarmim. Ready to bite. Not near enemy minerals.
            # teasing: being followed by many opponents
            #
            #
            self.calculate_nextpos()
            #
            if self.workerrushstate == 'tobe':
                if (self.frame > self.workerrushstartframe):
                    self.workerrushstate = 'busy'
                    # reserved 45 minerals for repair
                    self.purse.minerals += 45
                    todo = self.startworkerrushers
                    for scv in self.units(SCV):
                        job = self.job_of_scvt[scv.tag]
                        if job in self.bad_jobs + self.no_jobs:
                            if todo > 0:
                                todo -= 1
                                self.promote(scv,'cheeser')
                                self.speciality_of_tag[scv.tag] = 'workerrush'
                                self.go_gather_mim(scv,self.hisrampmim)
                                self.emotion_of_unittag[scv.tag] = 'ingoing'
                                self.wait_of_scv[scv.tag] = 0 # for emotions
                                self.last_sd_of_scv[scv.tag] = 99999
                            else:
                                # give fresh mining place, especially on golden wall
                                self.promote(scv,'escorter')
                                scv.attack(self.loved_pos.towards(self.map_center,-3))
            elif self.workerrushstate == 'busy':
                rushers = 0
                for scv in self.units(SCV):
                    if scv.tag in self.speciality_of_tag:
                        if self.speciality_of_tag[scv.tag] == 'workerrush':
                            rushers += 1
                enemyarmy = 0
                for ene in self.enemy_units: # actual visible
                    if ene.type_id not in {EGG, LARVA, OVERLORD, OVERSEER, DRONE, SCV, PROBE, ZERGLING}:
                        enemyarmy += 1
                mustgoon = False
                if self.frame >= self.workerrushstopframe:
                    mustgoon = True
                if rushers < 4:
                    mustgoon = True
                if enemyarmy > 0:
                    mustgoon = True
                if mustgoon:
                    self.workerrushstate = 'ended'
                    # reserved 45 minerals for repair
                    self.purse.minerals -= 45
                    self.rushrepairs = set()
                    self.rushrepairers = set()
                    for scv in self.units(SCV):
                        if scv.tag in self.speciality_of_tag:
                            if self.speciality_of_tag[scv.tag] == 'workerrush':
                                del self.speciality_of_tag[scv.tag]
                                if self.emotion_of_unittag[scv.tag] == 'circling':
                                    # circle forever
                                    self.promote(scv,'scout')
                                    self.fleecirclers.add(scv.tag)
                                else:
                                    self.promote(scv,'idler')
            # stacking while moving forward
            back = self.homemim
            (backpos,backt) = back
            forward = self.hisrampmim
            if self.stackphase == 'A':
                # get a stacktag
                for scv in self.units(SCV):
                    if scv.tag in self.speciality_of_tag:
                        if self.speciality_of_tag[scv.tag] == 'workerrush':
                            self.stacktag = scv.tag
                            self.stackphase = 'B'
            elif self.stackphase == 'B':
                # wait till going
                for scv in self.units(SCV):
                    if scv.tag == self.stacktag:
                        dist = self.circledist(scv.position, backpos)
                        if dist > self.stack_at_dist:
                            self.stackphase = 'C'
            elif self.stackphase == 'C':
                # slowest is stacktag
                mindist = 99999
                for scv in self.units(SCV):
                    if scv.tag in self.speciality_of_tag:
                        if self.speciality_of_tag[scv.tag] == 'workerrush':
                            dist = self.circledist(scv.position,backpos)
                            if (dist > self.stack_at_dist - 20): # neglect late arrivers
                                if dist < mindist:
                                    mindist = dist
                                    self.stacktag = scv.tag
                # turn fast ones around
                self.workerback = set()
                for scv in self.units(SCV):
                    if scv.tag in self.speciality_of_tag:
                        if self.speciality_of_tag[scv.tag] == 'workerrush':
                            dist = self.circledist(scv.position, backpos)
                            if dist > mindist + self.turndistance:
                                self.go_gather_mim(scv,back)
                                self.workerback.add(scv.tag)
                self.stackphase = 'D'
            elif self.stackphase == 'D':
                # go forward at the right moment
                for scv in self.units(SCV):
                    if scv.tag == self.stacktag:
                        mindist = self.circledist(scv.position, backpos)
                if len(self.workerback) > 0:
                    for scv in self.units(SCV):
                        if scv.tag in self.workerback:
                            dist = self.circledist(scv.position, backpos)
                            if dist < mindist + self.turndistance:
                                self.go_gather_mim(scv,forward)
                                self.workerback.remove(scv.tag)
                if len(self.workerback) == 0:
                    self.stackphase = 'E'
                    self.stack_at_dist += 3
            elif self.stackphase == 'E':
                # wait till going
                for scv in self.units(SCV):
                    if scv.tag == self.stacktag:
                        dist = self.circledist(scv.position, backpos)
                        if dist > self.stack_at_dist:
                            self.stackphase = 'F'
            elif self.stackphase == 'F':
                # slowest is stacktag
                mindist = 99999
                maxdist = -99999
                for scv in self.units(SCV):
                    if scv.tag in self.speciality_of_tag:
                        if self.speciality_of_tag[scv.tag] == 'workerrush':
                            dist = self.circledist(scv.position,backpos)
                            if (dist > self.stack_at_dist - 20): # neglect late arrivers
                                maxdist = max(dist, maxdist)
                                if dist < mindist:
                                    mindist = dist
                                    self.stacktag = scv.tag
                # ready?
                if maxdist < mindist + self.turndistance2:
                    self.stackphase = 'H'
                    self.log_success('Fully stacked!')
                # turn fast ones around
                self.workerback = set()
                for scv in self.units(SCV):
                    if scv.tag in self.speciality_of_tag:
                        if self.speciality_of_tag[scv.tag] == 'workerrush':
                            dist = self.circledist(scv.position, backpos)
                            if dist > mindist + self.turndistance2:
                                self.go_gather_mim(scv,back)
                                self.workerback.add(scv.tag)
                self.stackphase = 'G'
            elif self.stackphase == 'G':
                # next programrun go forward
                if len(self.workerback) > 0:
                    for scv in self.units(SCV):
                        if scv.tag in self.workerback:
                            self.go_gather_mim(scv,forward)
                            self.workerback.remove(scv.tag)
                if len(self.workerback) == 0:
                    self.stackphase = 'E'
                    self.stack_at_dist += 3
            #
            # re_move
            re_move_set = set() # of scvtag
            # add scv's tag if its move must be given.
            #
            # to remember emotion
            last_emotion = {}
            for scv in self.units(SCV):
                if scv.tag in self.speciality_of_tag:
                    if self.speciality_of_tag[scv.tag] == 'workerrush':
                        last_emotion[scv.tag] = self.emotion_of_unittag[scv.tag]
            # rushscore
            # per hit +5, per enemy hit -5, own healthrepeair.
            rushhealth = - self.startworkerrushers * 45
            for scv in self.units(SCV):
                if scv.tag in self.speciality_of_tag:
                    if self.speciality_of_tag[scv.tag] == 'workerrush':
                        rushhealth += scv.health
                        if scv.tag in self.last_weapon_cooldown:
                            if scv.weapon_cooldown > self.last_weapon_cooldown[scv.tag]:
                                self.rushdamage += 5
                        self.last_weapon_cooldown[scv.tag] = scv.weapon_cooldown
            rushscore = rushhealth + self.rushdamage
            # logging
            self.log_success('rushscore '+str(rushscore))
            for scv in self.units(SCV):
                if scv.tag in self.speciality_of_tag:
                    if self.speciality_of_tag[scv.tag] == 'workerrush':
                        emotion = self.emotion_of_unittag[scv.tag]
                        orders = ""
                        for order in scv.orders:
                            if type(order.target) == int:
                                orders = orders + '   ' + str(order.ability.id) + ', ' + str(order.target)
                            else:
                                orders = orders + '   ' + str(order.ability.id) + ', ' + self.txt(order.target)
                        # dte = dist to (nearest) enemy
                        dte = 99999
                        for ene in self.enemy_units: # actual visible
                            if ene.tag in self.enemymelee:
                                dist = self.circledist(self.nextpos_of_unittag[scv.tag],self.nextpos_of_unittag[ene.tag])
                                dte = min(dte,dist)
                        wai = self.wait_of_scv[scv.tag]
                        self.log_success(self.name(scv.tag) + ' ' + str(scv.health) + ' ' + emotion
                                         + ' ' + str(scv.weapon_cooldown) + ' ' + str(dte) + ' ' + str(wai) + orders)
            #
            # delete rushrepair
            todel1 = set()
            todel2 = set()
            for (repairer_tag,repairee_tag) in self.rushrepairs:
                repairerfound = False
                for may_repairer in self.units(SCV):
                    if may_repairer.tag == repairer_tag:
                        if self.emotion_of_unittag[repairer_tag] == 'inrepair':
                            repairerfound = True
                            repairer = may_repairer
                if repairerfound:
                    repaireefound = False
                    for repairee in self.units(SCV):
                        if repairee.tag == repairee_tag:
                            if self.emotion_of_unittag[repairee.tag] == 'inrepair':
                                repaireefound = True
                                if repairee.health >= self.healthybound:
                                    # cured
                                    todel1.add(repairer_tag)
                                    todel2.add((repairer_tag,repairee_tag))
                    if not repaireefound:
                        todel1.add(repairer_tag)
                        todel2.add((repairer_tag, repairee_tag))
                else: # repairer not found
                    todel1.add(repairer_tag)
                    todel2.add((repairer_tag, repairee_tag))
            self.rushrepairers -= todel1
            self.rushrepairs -= todel2
            for (repairer_tag,repairee_tag) in todel2:
                self.log_success(self.name(repairer_tag)+' ended repairing '+self.name(repairee_tag))
            for (repairer_tag,repairee_tag) in self.rushrepairs:
                self.log_success(self.name(repairer_tag)+' is repairing '+self.name(repairee_tag))
            # counts
            agressivecount = 0
            defensivecount = 0
            neutralcount = 0
            for scv in self.units(SCV):
                if scv.tag in self.speciality_of_tag:
                    if self.speciality_of_tag[scv.tag] == 'workerrush':
                        emotion = self.emotion_of_unittag[scv.tag]
                        if emotion in agressive:
                            agressivecount += 1
                        elif emotion in neutral:
                            neutralcount += 1
                        elif emotion in defensive:
                            defensivecount += 1
            # enemymelee: tag of reachable enemy workers
            # not overlord, not inside a building structure
            self.enemymelee = set()
            for ene in self.enemy_units: # actual visible
                if ene.type_id in {DRONE, SCV, PROBE, ZERGLING}:
                    outside = True
                    for stru in self.enemy_real_structures:
                        if self.near(ene.position,stru.position,stru.radius - 0.25):
                            outside = False
                    if outside:
                        self.enemymelee.add(ene.tag)
            # known_hit_by_enemy: frame that that worker hit me
            for ene in self.enemy_units: # actual visible
                if ene.tag in self.enemymelee:
                    if ene.tag not in self.known_hit_by_enemy:
                        self.known_hit_by_enemy[ene.tag] = -99999
            for scv in self.units(SCV):
                if scv.tag in self.last_health:
                    if scv.health < self.last_health[scv.tag]:
                        # I was bitten
                        nnear = 0
                        for ene in self.enemy_units: # actual visible
                            if ene.tag in self.enemymelee:
                                if self.near(self.nextpos_of_unittag[ene.tag],self.nextpos_of_unittag[scv.tag],0.95): # 0.85 theory
                                    if self.known_hit_by_enemy[ene.tag] < self.frame - 20:
                                        nnear += 1
                                        crulpittag = ene.tag
                        if nnear == 1:
                            self.known_hit_by_enemy[crulpittag] = self.frame
            #
            # emotion changes
            #
            # end of repair
            for scv in self.units(SCV):
                if scv.tag in self.speciality_of_tag:
                    if self.speciality_of_tag[scv.tag] == 'workerrush':
                        emotion = self.emotion_of_unittag[scv.tag]
                        if emotion == 'inrepair':
                            seen = False
                            for (aider_tag, aidee_tag) in self.rushrepairs:
                                if (aider_tag == scv.tag) or (aidee_tag == scv.tag):
                                    seen = True
                            if not seen:
                                self.emotion_of_unittag[scv.tag] = 'firstaid'
                                re_move_set.add(scv.tag)
            # platoons
            if self.frame % 29 == 28:
                if self.frame > self.workerrushmayfleeframe:
                    self.replatoon()
                    for pid in range(0,len(self.platoons)):
                        platoon = self.platoons[pid]
                        plan = self.platoonplans[pid]
                        goal = self.platoongoals[pid]
                        center = self.platooncenters[pid]
                        if plan == 'flee':
                            self.log_success(' Platoon flee '+str(len(platoon)))
                        for scv in self.units(SCV):
                            if scv.tag in platoon:
                                if plan == 'flee':
                                    self.emotion_of_unittag[scv.tag] = 'fleeing'
                                    (mimpos,mimt) = self.hisfarmim
                                    if self.near(center,mimpos,5):
                                        self.towardsmineral[scv.tag] = self.hisfarmim
                                    else:
                                        self.towardsmineral[scv.tag] = self.homemim
            # per scv
            for scv in self.units(SCV):
                if scv.tag in self.speciality_of_tag:
                    if self.speciality_of_tag[scv.tag] == 'workerrush':
                        emotion = self.emotion_of_unittag[scv.tag]
                        # jumpbound
                        # 2.0 for health 41, 1.0 for health 0
                        jumpbound = 1.0 + scv.health / 41
                        # awaymim
                        enemies_behind_you = 99999
                        for mim in {self.hisfarmim,self.hisrampmim,self.homemim}:
                            (mimpos,mimt) = mim
                            enem = 0
                            safetycenter = scv.position.towards(mimpos,4)
                            for ene in self.enemy_units: # actual visible
                                if ene.tag in self.enemymelee:
                                    if self.near(ene.position, safetycenter, 4):
                                        enem += 1
                            if enem < enemies_behind_you:
                                enemies_behind_you = enem
                                awaymim = mim
                        (mimpos,mimt) = awaymim        
                        if self.near(scv.position,mimpos,2):
                            awaymim = self.homemim
                        # bittencount
                        bittencount = 0
                        for ene in self.enemy_units: # actual visible
                            if ene.tag in self.enemymelee:
                                if self.near(self.nextpos_of_unittag[ene.tag], self.nextpos_of_unittag[scv.tag], self.bitebound):
                                    if self.known_hit_by_enemy[ene.tag] < self.frame - 20:
                                        bittencount += 1
                        # sd_to_enemy
                        sd_to_enemy = 99999
                        for ene in self.enemy_units: # actual visible
                            if ene.tag in self.enemymelee:
                                sd = self.sdist(self.nextpos_of_unittag[scv.tag],self.nextpos_of_unittag[ene.tag])
                                sd_to_enemy = min(sd,sd_to_enemy)
                        #
                        # minority means running away when followed by many enemies
                        minority = 0 # enemies - 1.5 * ours
                        for anscv in self.units(SCV):
                            if self.near(anscv.position, scv.position, 5):
                                minority -= 1.5
                        for (typ, pos, tag) in self.last_enemies:
                            if self.near(pos, scv.position, 10):
                                for ene in self.enemy_units(typ):  # actual visible
                                    if ene.tag == tag:
                                        # if approaches
                                        if self.sdist(ene.position, scv.position) < self.sdist(pos, scv.position):
                                            minority += 1
                        #
                        self.wait_of_scv[scv.tag] -= self.chosen_game_step
                        # timed: bouncing, jumping, biting
                        #
                        # emotion state changes
                        #
                        if (bittencount >= 2):
                            emotion = 'bouncing'
                            re_move_set.add(scv.tag)
                        # go flee
                        minhealthbound = 5.5 + enemies_behind_you * 5
                        minhealthbound = min(20.5,minhealthbound)
                        if (scv.health < minhealthbound):
                            if emotion in agressive:
                                emotion = 'fleeing'
                                self.towardsmineral[scv.tag] = awaymim
                                self.last_sd_of_scv[scv.tag] = 99999
                                re_move_set.add(scv.tag)
                        if emotion in {'firstaid','inrepair'}:
                            if sd_to_enemy < 2*2:
                                emotion = 'fleeing'
                                self.towardsmineral[scv.tag] = awaymim
                                self.last_sd_of_scv[scv.tag] = 99999
                                re_move_set.add(scv.tag)
                        #
                        if (emotion in {'firstaid', 'inrepair'}) and (scv.weapon_cooldown < 7):
                            # and close and a bit healed
                            for tt in [0, 1, 2, 3, 4, 5, 6, 7]:
                                # (1.5, 5.5), (2.0, 10.5), ..., (5.0, 40.5)
                                dist = 1.5 + tt / 2
                                bound = 5.5 + tt * 5
                                if (sd_to_enemy < dist * dist) and (scv.health >= bound):
                                    if (len(self.rushrepairs) == 0) or (self.minerals < 40) or (agressivecount >= 2):
                                        emotion = 'brave'
                                        re_move_set.add(scv.tag)
                            # next run self.rushrepairs will be adapted
                        #
                        if emotion == 'fleeing':
                            if sd_to_enemy > 5*5:
                                emotion = 'firstaid'
                            elif (not self.near(scv.position,self.enemy_pos,20)):
                                groupcount = 0
                                for anscv in self.units(SCV):
                                    if self.near(anscv.position,scv.position,7):
                                        groupcount += 1
                                for ene in self.enemy_units: # actual visible
                                    if self.near(ene.position, scv.position, 7):
                                        groupcount -= 1
                                if groupcount < 0:
                                    emotion = 'circling'
                                    self.fleepole[scv.tag] = 0
                                    self.fleefear[scv.tag] = 10 # programruns
                        elif emotion == 'circling':
                            groupcount = 0
                            for anscv in self.units(SCV):
                                if self.near(anscv.position, scv.position, 7):
                                    groupcount += 1
                            for ene in self.enemy_units: # actual visible
                                if self.near(ene.position, scv.position, 7):
                                    groupcount -= 1
                            if groupcount > 0:
                                self.fleefear[scv.tag] -= 1
                            else:
                                self.fleefear[scv.tag] = 10 # programruns
                            if self.fleefear[scv.tag] < 0:
                                emotion = 'firstaid'
                        elif scv.weapon_cooldown >= 18: # I bit
                            if emotion != 'looting':
                                emotion = 'bouncing'
                        elif (self.get_rushvictims(self.nextpos_of_unittag[scv.tag],self.bitebound) > 0) and (scv.weapon_cooldown < 5):
                            if self.near(self.nextpos_of_unittag[scv.tag],self.nextpos_of_unittag[self.rushvictim.tag],0.95):
                                emotion = 'biting'
                            elif emotion != 'jumping':
                                emotion = 'biting'
                        elif (self.get_rushvictims(self.nextpos_of_unittag[scv.tag], jumpbound) > 0) and (scv.weapon_cooldown < 10):
                            emotion = 'jumping'
                        elif emotion == 'brave':
                            if (sd_to_enemy == 99999):
                                emotion = 'looting'
                        elif emotion == 'looting':
                            if (sd_to_enemy < 99999):
                                emotion = 'brave'
                            elif scv.tag in self.idles:
                                re_move_set.add(scv.tag)
                        elif emotion == 'ingoing':
                            if minority >= 0:
                                emotion = 'teasing'
                            elif self.near(scv.position, self.hisfarmim[0], 8):
                                emotion = 'brave'
                            elif self.near(scv.position, self.hisrampmim[0], 8):
                                emotion = 'brave'
                        elif emotion == 'teasing':
                            if minority < 0:
                                emotion = 'ingoing'
                            elif (not self.near(scv.position, self.enemy_pos, 20)):
                                emotion = 'circling'
                                self.fleepole[scv.tag] = 0
                                self.fleefear[scv.tag] = 10  # programruns
                        elif emotion == 'afraid':
                            if sd_to_enemy >= 1.5*1.5:
                                emotion = 'firstaid'
                        # try to repair
                        if emotion in {'firstaid','inrepair'}:
                            if self.minerals >= 20:
                                minsd = 99999
                                for otherscv in self.units(SCV):
                                    if otherscv.tag != scv.tag:
                                        if otherscv.tag in self.speciality_of_tag:
                                            if self.speciality_of_tag[otherscv.tag] == 'workerrush':
                                                if self.emotion_of_unittag[otherscv.tag] in {'firstaid','inrepair'}:
                                                    if otherscv.health < self.healthybound:
                                                        sd = self.sdist(scv.position,otherscv.position)
                                                        if sd < minsd:
                                                            minsd = sd
                                                            bestscv = otherscv
                                if (sd_to_enemy == 99999):
                                    emotion = 'looting'
                                elif (scv.health >= self.healthybound) and (scv.weapon_cooldown < 7):
                                    emotion = 'ingoing'
                                elif minsd < 99999:
                                    if (minsd < 5*5) or (self.frame % 53 == 52):
                                        if scv.tag not in self.rushrepairers:
                                            emotion = 'inrepair'
                                            self.emotion_of_unittag[bestscv.tag] = 'inrepair'
                                            self.rushrepairs.add((scv.tag, bestscv.tag))
                                            self.rushrepairers.add(scv.tag)
                                            re_move_set.add(scv.tag)
                        #
                        #
                        # workerrush timeouts
                        if emotion == last_emotion[scv.tag]:
                            if emotion in {'jumping', 'biting'}:
                                if self.wait_of_scv[scv.tag] <= 0:
                                    emotion = 'bouncing'
                                    re_move_set.add(scv.tag)
                            elif emotion == 'bouncing':
                                if self.wait_of_scv[scv.tag] <= 0:
                                    if scv.health < self.healthybound:
                                        emotion = 'afraid'
                                        re_move_set.add(scv.tag)
                                    else:
                                        emotion = 'brave'
                                        re_move_set.add(scv.tag)
                        #
                        # workerrush wait
                        if emotion != last_emotion[scv.tag]:
                            if emotion == 'bouncing':
                                self.wait_of_scv[scv.tag] = 8.5 - scv.health / 7
                                # health 45 -> wait 2.1
                                # health 5 -> wait 7.8
                            elif emotion in {'jumping','biting'}:
                                self.wait_of_scv[scv.tag] = 9
                        #
                        self.emotion_of_unittag[scv.tag] = emotion
                        #
                        # calculated
                        if emotion == 'ingoing':
                            if self.sdist(scv.position, self.hisfarmim[0]) > 20:
                                tomim = self.hisrampmim
                            elif self.sdist(scv.position, self.hisfarmim[0]) > \
                                    self.sdist(scv.position,self.hisrampmim[0]):
                                tomim = self.hisrampmim
                            else:
                                tomim = self.hisfarmim
                            self.towardsmineral[scv.tag] = tomim
                        #
                        # workerrush move
                        re_move = False
                        if emotion != last_emotion[scv.tag]:
                            self.log_success('For ' + self.name(scv.tag) + ' ' + last_emotion[scv.tag] + ' became ' + emotion)
                            re_move = True
                        elif self.near(scv.position, self.hisfarmim[0], 2):
                            re_move = True
                        elif self.near(scv.position, self.hisrampmim[0], 2):
                            re_move = True
                        elif self.near(scv.position, self.turningpoint, 2):
                            re_move = True
                        elif self.near(scv.position,self.followers,10):
                            re_move = True
                        elif scv.tag in re_move_set:
                            re_move = True
                        if re_move:
                            if emotion == 'biting':
                                scv.attack(self.rushvictim)
                            elif emotion == 'jumping':
                                maxcool = -99999
                                for mim in {self.homemim, self.hismidmim, self.hisrampmim, self.hisfarmim}:
                                    (mimpos,mimt) = mim
                                    cool = self.circledist(scv.position, mimpos) - self.circledist(
                                        self.rushvictim.position, mimpos)
                                    if cool > maxcool:
                                        maxcool = cool
                                        bestmim = mim
                                if maxcool > 0.8 * self.circledist(scv.position, self.rushvictim.position):
                                    self.go_gather_mim(scv,bestmim)
                                else:
                                    scv.attack(self.rushvictim)
                            elif emotion == 'brave':
                                if self.near(scv.position, self.hisfarmim[0], 2):
                                    self.towardsmineral[scv.tag] = self.hisrampmim
                                elif self.near(scv.position, self.hisrampmim[0], 2):
                                    self.towardsmineral[scv.tag] = self.hisfarmim
                                if self.towardsmineral[scv.tag] not in {self.hisrampmim,self.hisfarmim}:
                                    self.towardsmineral[scv.tag] = self.hisfarmim
                                self.go_gather_mim(scv,self.towardsmineral[scv.tag])
                            elif emotion == 'bouncing':
                                self.go_gather_mim(scv,awaymim)
                            elif emotion in {'fleeing','teasing'}:
                                if self.near(scv.position, self.hisfarmim[0], 2):
                                    self.towardsmineral[scv.tag] = self.homemim
                                    scv.move(self.turningpoint)
                                elif self.near(scv.position,self.turningpoint,2):
                                    self.towardsmineral[scv.tag] = self.homemim
                                    self.go_gather_mim(scv,self.towardsmineral[scv.tag])
                                elif self.near(scv.position, self.hisrampmim[0], 2):
                                    self.towardsmineral[scv.tag] = self.homemim
                                    self.go_gather_mim(scv,self.towardsmineral[scv.tag])
                                else:
                                    self.go_gather_mim(scv,self.towardsmineral[scv.tag])
                            elif emotion == 'firstaid':
                                scv.move(scv.position.towards(self.loved_pos,0.1)) # is it a bug to go to own position?
                            elif emotion == 'circling':
                                self.fleecirclemove(scv)
                            elif emotion == 'afraid':
                                if self.near(scv.position, self.hisrampmim[0], 2):
                                    self.go_gather_mim(scv,self.homemim)
                                else:
                                    self.go_gather_mim(scv,self.hisrampmim)
                            elif emotion == 'inrepair':
                                itisarepairer = False
                                itisarepairee = False
                                for (repairer_tag, repairee_tag) in self.rushrepairs:
                                    # find one of the partners
                                    if scv.tag == repairee_tag:
                                        itisarepairee = True
                                        for other in self.units(SCV):
                                            if other.tag == repairer_tag:
                                                partner = other # multiple
                                    elif scv.tag == repairer_tag:
                                        itisarepairer = True
                                        for other in self.units(SCV):
                                            if other.tag == repairee_tag:
                                                partner = other # unique
                                                repairee = other
                                halfway = Point2(((scv.position.x + partner.position.x) / 2,
                                                  (scv.position.y + partner.position.y) / 2))
                                if self.minerals >= 20:
                                    if itisarepairer:
                                        scv.repair(repairee)
                                    else:
                                        scv.move(halfway)
                                else:
                                    scv.move(halfway)
                            elif emotion == 'ingoing':
                                tomim = self.towardsmineral[scv.tag]
                                self.go_gather_mim(scv,tomim)
                            elif emotion == 'looting':
                                minh = 99999
                                for stru in self.enemy_real_structures:
                                    if stru.health < minh:
                                        minh = stru.health
                                        victimstru = stru
                                if minh < 99999:
                                    scv.attack(victimstru)
                        #
            # starved repair
            if self.minerals >= 20:
                for (repairer_tag,repairee_tag) in self.rushrepairs:
                    if repairer_tag in self.idles:
                        # re-repair
                        for repairer in self.units(SCV):
                            if repairer.tag == repairer_tag:
                                for repairee in self.units(SCV):
                                    if repairee.tag == repairee_tag:
                                        repairer.repair(repairee)


    def do_cocoon(self):
        if self.opening_name.find('cocoon') >= 0:
            if self.cheese3_phase == 'A':
                # while (nothing)
                # continue
                for ba in self.structures(BARRACKS):
                    if ba.position == self.cheese3_barracks_pos:
                        # init (barracks is constructing)
                        self.cheese3_barracks_tag = ba.tag
                        self.speciality_of_tag[ba.tag] = self.opening_name
                        self.cheese3_phase = 'B'
                    if ba.position == self.cheese3_barracks2_pos:
                        # init (barracks is constructing)
                        self.cheese3_barracks2_tag = ba.tag
                        self.speciality_of_tag[ba.tag] = self.opening_name
                        self.cheese3_phase = 'C'
            elif self.cheese3_phase == 'B':
                # while (nothing)
                # continue
                for ba in self.structures(BARRACKS):
                    if ba.position == self.cheese3_barracks2_pos:
                        # init (barracks is constructing)
                        self.cheese3_barracks2_tag = ba.tag
                        self.speciality_of_tag[ba.tag] = self.opening_name
                        self.cheese3_phase = 'D'
            elif self.cheese3_phase == 'C':
                # while (nothing)
                # continue
                for ba in self.structures(BARRACKS):
                    if ba.position == self.cheese3_barracks_pos:
                        # init (barracks is constructing)
                        self.cheese3_barracks_tag = ba.tag
                        self.speciality_of_tag[ba.tag] = self.opening_name
                        self.cheese3_phase = 'D'
            elif self.cheese3_phase == 'D':
                # while (barracks, bunkers constructing)
                for bunpos in {self.cheese3_bunker_pos,self.cheese3_bunker2_pos}:
                    if not self.we_started_at(BUNKER,bunpos):
                        self.throw_at_spot(BUNKER,bunpos,'do_cocoon')
                for bu in self.structures(BUNKER):
                    if bu.tag not in bunker_if.door:
                        bunker_if.door[bu.tag] = self.cheese3_prison_pos
                #clean
                if self.cheese3_barracks_tag not in (ba.tag for ba in self.structures(BARRACKS)):
                    self.cheese3_phase = 'Y'
                if self.cheese3_barracks2_tag not in (ba.tag for ba in self.structures(BARRACKS)):
                    self.cheese3_phase = 'Y'
                # continue
                seen = 0
                for bu in self.structures(BUNKER):
                    if bu.tag in self.readies:
                        seen += 1
                if seen >= 2:
                    self.cheese3_phase = 'E'
            elif self.cheese3_phase == 'E':
                # while (emptying barracks 1)
                # clean
                # continue
                todo = 1
                for ba in self.structures(BARRACKS):
                    if ba.tag in self.readies:
                        if ba.tag in self.idles:
                            if ba.tag in {self.cheese3_barracks_tag,self.cheese3_barracks2_tag}:
                                if todo > 0:
                                    todo -= 1
                                    # other cheese!
                                    self.set_rally.add((self.cheese1_landing_pos, self.cheese1_prison_pos))
                                    self.set_rally.add((self.cheese1_bunker_pos, self.cheese1_prison_pos))
                                    goal = self.cheese1_landing_pos
                                    self.write_layout(BARRACKS, goal)
                                    self.goal_of_flying_struct[ba.tag] = goal
                                    self.subgoal_of_flying_struct[ba.tag] = goal.towards(self.map_center, 10)
                                    self.landings_of_flying_struct[ba.tag] = 0
                                    self.log_success('move cheese BARRACKS')
                                    self.log_command('ba(AbilityId.LIFT')
                                    ba(AbilityId.LIFT)
                                    if ba.tag == self.cheese3_barracks_tag:
                                        self.cheese3_barracks_tag = self.notag
                                    else:
                                        self.cheese3_barracks2_tag = self.notag
                                    self.cheese3_phase = 'F'
            elif self.cheese3_phase == 'F':
                # while (emptying barracks 2)
                # clean
                # continue
                for ba in self.structures(BARRACKS):
                    if ba.tag in self.readies:
                        if ba.tag in self.idles:
                            if ba.tag in {self.cheese3_barracks_tag, self.cheese3_barracks2_tag}:
                                if self.find_tobuildwalk_a_place(BARRACKS,'now'):
                                    goal = self.function_result_Point2
                                    self.write_layout(BARRACKS, goal)
                                    self.goal_of_flying_struct[ba.tag] = goal
                                    self.landings_of_flying_struct[ba.tag] = 0
                                    self.log_success('move cheese BARRACKS')
                                    self.log_command('ba(AbilityId.LIFT')
                                    ba(AbilityId.LIFT)
                                    self.cheese3_barracks_tag = self.notag
                                    self.cheese3_phase = 'G'
            elif self.cheese3_phase == 'G':
                # while (factory or tank constructing, barracks flying)
                # clean
                seen = False
                for bu in self.structures(BUNKER):
                    if bu.tag in self.readies:
                        seen = True
                if not seen:
                    self.cheese3_phase = 'Y'
                # other cheese
                for ba in self.structures(BARRACKS):
                    if ba.position == self.cheese1_landing_pos:
                        self.throw_at_spot(MARINE, ba.position, 'do_cocoon')
                        for scv in self.units(SCV):
                            if scv.tag == self.scout1_tag:
                                self.promote(scv, 'idler')
                                self.scout1_tag = -2 # notag, but notag would rerecruite it
                        self.throw_at_spot(BUNKER, self.cheese1_bunker_pos, 'do_cocoon')
                        self.cheese3_phase = 'Galt'
                        # if the bunker starts building, cheese1 will start.
                # continue
                if len(self.units(SIEGETANK)) > 0:
                    # init (siegetank going)
                    for tnk in self.units(SIEGETANK):
                        self.speciality_of_tag[tnk.tag] = self.opening_name
                        goal = self.cheese3_bunker_pos.towards(self.loved_pos,2.2)
                        goal = self.place_around(AUTOTURRET,goal)
                        self.write_layout(AUTOTURRET, goal)
                        self.tankplaces.add(goal)
                        self.go_attack(tnk, goal)
                    self.cheese3_phase = 'H'
            elif self.cheese3_phase == 'Galt':
                # while (factory or tank constructing)
                # clean
                seen = False
                for bu in self.structures(BUNKER):
                    if bu.tag in self.readies:
                        seen = True
                if not seen:
                    self.cheese3_phase = 'Y'
                # continue
                if len(self.units(SIEGETANK)) > 0:
                    # init (siegetank going)
                    for tnk in self.units(SIEGETANK):
                        self.speciality_of_tag[tnk.tag] = self.opening_name
                        self.cheese3_tanktags.add(tnk.tag)
                        goal = self.cheese3_bunker_pos.towards(self.loved_pos,2.2)
                        goal = self.place_around(AUTOTURRET,goal)
                        self.write_layout(AUTOTURRET, goal)
                        self.tankplaces.add(goal)
                        self.go_attack(tnk, goal)
                    self.cheese3_phase = 'H'
            elif self.cheese3_phase == 'H':
                # while (siegetank going)
                # clean
                seen = False
                for bu in self.structures(BUNKER):
                    if bu.tag in self.readies:
                        seen = True
                if not seen:
                    self.cheese3_phase = 'Y'
                # continue
                for tnk in self.units(SIEGETANK):
                    if tnk.tag in self.cheese3_tanktags:
                        if self.no_move(tnk,32):
                            self.log_command('tnk(AbilityId.SIEGEMODE_SIEGEMODE)')
                            tnk(AbilityId.SIEGEMODE_SIEGEMODE)
                            self.cheese3_phase = 'I'
            elif self.cheese3_phase == 'I':
                # while (wait for engibay)
                # clean
                seen = False
                for bu in self.structures(BUNKER):
                    if bu.tag in self.readies:
                        seen = True
                if not seen:
                    self.cheese3_phase = 'Y'
                # continue
                if self.we_finished_a(ENGINEERINGBAY):
                    goal = self.cheese3_bunker2_pos.towards(self.loved_pos, 2.2)
                    goal = self.place_around(MISSILETURRET, goal)
                    self.throw_at_spot(MISSILETURRET,goal,'do_cocoon')
                    self.cheese3_phase = 'J'
            elif self.cheese3_phase == 'Y':
                # clean up the cheese
                self.clean_speciality_of_tag(self.opening_name)
                for scv in self.units(SCV):
                    scvt = scv.tag
                    if self.job_of_scvt[scvt] == 'cheeser':
                        self.promote(scv,'fleeer') # includes move
                for ba in self.structures(BARRACKS):
                    if ba.tag in [self.cheese3_barracks_tag,self.cheese3_barracks2_tag]:
                        if ba.tag not in self.readies:
                            self.log_command('ba(AbilityId.CANCEL_BUILDINPROGRESS)')
                            ba(AbilityId.CANCEL_BUILDINPROGRESS)
                        if ba.tag in self.readies:
                            if self.find_tobuildwalk_a_place(BARRACKS,'now'):
                                goal = self.function_result_Point2
                                self.write_layout(BARRACKS, goal)
                                if ba.tag not in self.idles:
                                    self.log_command('ba(AbilityId.CANCEL_QUEUE5)') # build unit
                                    ba(AbilityId.CANCEL_QUEUE5)
                                self.goal_of_flying_struct[ba.tag] = goal
                                self.landings_of_flying_struct[ba.tag] = 0
                                self.log_success('move cheese BARRACKS')
                                self.log_command('ba(AbilityId.LIFT')
                                ba(AbilityId.LIFT)
                for ba in self.structures(BARRACKSFLYING):
                    if ba.tag in [self.cheese3_barracks_tag,self.cheese3_barracks2_tag]:
                        if self.find_tobuildwalk_a_place(BARRACKS,'now'):
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
        self.write_layout(BUNKER,self.cheese1_bunker_pos)
        self.write_layout(ARMORY,self.cheese1_landing_pos)
        keep = []
        found = 0
        for r in range(1,15):
            if found < 2:
                for x in range(-r,r):
                    for y in range(-r,r):
                        if abs(x)+abs(y)+max(abs(x),abs(y)) == r:
                            point = Point2((self.cheese1_bunker_pos.x+x,self.cheese1_bunker_pos.y+y))
                            if self.check_layout(BUNKER,point):
                                goodpoint = point
                                self.chosenplaces.append((INFESTEDBUNKER, goodpoint))
                                self.write_layout(BUNKER, goodpoint)
                                keep.append(goodpoint)
                                found += 1
        self.erase_layout(BUNKER,self.cheese1_bunker_pos)
        self.erase_layout(ARMORY,self.cheese1_landing_pos)
        self.erase_layout(BUNKER,keep[0])
        self.erase_layout(BUNKER,keep[1])

    #*********************************************************************************************************************
    def clear_from_mines(self, goal):
        # goal is an expansion_location that may have own widowmines
        for wm in self.units(WIDOWMINEBURROWED):
            if self.near(wm.position, goal, 3):
                self.log_command('wm(AbilityId.BURROWUP_WIDOWMINE)')
                wm(AbilityId.BURROWUP_WIDOWMINE)
                point = wm.position.towards(self.loved_pos, 4)
                self.go_move(wm, point)
                self.emotion_of_unittag[wm.tag] = 'marching'
        for cluster in self.clusters:
            if cluster in self.goal_of_cluster:
                if self.goal_of_cluster[cluster] == goal:
                    del self.goal_of_cluster[cluster]

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

    def place_around_atheight(self, building, anchor) -> Point2:
        altpoint = self.put_on_the_grid(building, anchor)
        height = self.get_height(altpoint)
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
            ok = ok and (height == self.get_height(altpoint))
        return altpoint

    def init_airports(self):
        for expo in range(0,self.expos):
            ccpos = self.pos_of_expo[expo]
            # reserve airport place
            around = ccpos.towards(self.map_center, 5)
            place = self.place_around(ARMORY, around)
            self.write_layout(ARMORY, place)
            self.airport_of_expo[expo] = place
            # also reserve an employment office
            around = ccpos.towards(self.map_center, -4)
            place = self.place_around(SUPPLYDEPOT, around)
            self.write_layout(SUPPLYDEPOT, place)
            self.employment_of_expo[expo] = place

    def lift(self):
        # attacked buildings can fly, survive, be repaired, and land back.
        for srt in self.liftable:
            for bu in self.structures(srt):
                if bu.tag in self.readies:
                    # goal overwritable before lifting
                    if bu.tag not in self.goal_of_flying_struct:
                        self.goal_of_flying_struct[bu.tag] = bu.position
                    if bu in self.all_bases:
                        if self.purpose[bu.tag] == 'fly':
                            self.log_cc(srt.name + ' '+str(bu.tag)+' ' + self.txt(bu.position) + ' takes off to fly.')
                            self.landings_of_flying_struct[bu.tag] = 0
                            self.log_success('up ' + srt.name)
                            self.log_command('bu(AbilityId.LIFT')
                            bu(AbilityId.LIFT)
                            self.purpose[bu.tag] = 'float'
                    elif bu.health < 500:
                        if bu.tag not in self.speciality_of_tag:
                            if bu.type_id not in {COMMANDCENTER,ORBITALCOMMAND}: # those have code elsewhere
                                if bu.tag not in self.idles:
                                    self.log_command('bu(AbilityId.CANCEL_QUEUE5)') # build unit
                                    bu(AbilityId.CANCEL_QUEUE5)
                                self.landings_of_flying_struct[bu.tag] = 0
                                self.log_success('up '+srt.name)
                                self.log_command('bu(AbilityId.LIFT')
                                bu(AbilityId.LIFT)

    def land(self):
        # attacked buildings can fly, survive, be repaired, and land back.
        for srt in self.landable:
            basekind = self.basekind_of(srt)
            for bu in self.structures(srt):
                if bu.tag in self.readies:
                    if bu.tag in self.idles:
                        if bu.health >= self.maxhealth[bu.type_id]-100:
                            self.log_success('a sound '+srt.name+' should land')
                            goal = self.goal_of_flying_struct[bu.tag]
                            # unburrow widowines
                            if self.near(bu.position, goal, 8):
                                self.clear_from_mines(goal)
                            if self.near(bu.position,goal,4):
                                self.log_success('it is close.')
                                # land
                                if basekind in self.hall_types:
                                    self.log_cc(srt.name + ' '+str(bu.tag)+' ' + self.txt(bu.position) + ' lands.')
                                    self.purpose[bu.tag] = 'land'
                                    self.waitframe_of_tag[bu.tag] = self.frame + 20
                                # maybe wait
                                mustwait = False
                                # maybe wait for willswap
                                for (block,blockpos) in self.willswap:
                                    if blockpos == goal:
                                        mustwait = True
                                        self.log_success('can not land on '+block.name)
                                # maybe wait for enemies
                                if basekind in self.hall_types:
                                    mytile = self.maptile_of_pos(bu.position)
                                    for tile in self.nine[mytile]:
                                        for ene in self.enemies_of_tile[tile]:
                                            if self.near(ene.position,bu.position,7):
                                                if not ene.is_flying:
                                                    mustwait = True
                                if not mustwait:
                                    self.log_success('down '+srt.name)
                                    self.log_command('bu(AbilityId.LAND,self.goal_of_flying_struct[bu.tag])')
                                    bu(AbilityId.LAND,self.goal_of_flying_struct[bu.tag])
                                    self.readies_delayed[bu.tag] = self.frame + 8 * self.frames_per_second
                                    self.landings_of_flying_struct[bu.tag] += 1
                                    if self.landings_of_flying_struct[bu.tag] > 5:
                                        # try another landing place
                                        self.landings_of_flying_struct[bu.tag] = 0
                                        newpoint = self.place_around(basekind,goal)
                                        self.goal_of_flying_struct[bu.tag] = newpoint
                            else: # not near goal
                                if bu.tag in self.subgoal_of_flying_struct:
                                    subgoal = self.subgoal_of_flying_struct[bu.tag]
                                    if self.near(bu.position, subgoal, 4):
                                        self.log_success('it is near the subgoal.')
                                        del self.subgoal_of_flying_struct[bu.tag]
                                        bu.move(self.goal_of_flying_struct[bu.tag])
                                    else:
                                        self.log_success('it is far.')
                                        bu.move(subgoal)
                                else:
                                    self.log_success('it is far.')
                                    bu.move(self.goal_of_flying_struct[bu.tag])
                        else: # it is broken
                            self.log_success('a broken '+srt.name+' should land')
                            if (srt == BARRACKSFLYING) and (self.opening_create_units == 0):
                                # wander chaotic
                                if bu.tag not in self.speciality_of_tag:
                                    self.log_success('flying barracks may randomwalk')
                                    goal = self.random_mappoint()
                                    self.goal_of_flying_struct[bu.tag] = goal
                                    self.landings_of_flying_struct[bu.tag] = 0
                                    bu(AbilityId.MOVE_MOVE, goal)
                            else: # not barracksflying
                                # be repaired at dock
                                dock = self.get_dock(bu.position)
                                if self.near(dock,bu.position,7):
                                    self.log_success('i hope it is being repaired')
                                    if len (self.all_mine_bases) == 0:
                                        if srt in [COMMANDCENTERFLYING,ORBITALCOMMANDFLYING]:
                                            self.log_success('down ' + srt.name)
                                            self.log_command('bu(AbilityId.LAND,self.goal_of_flying_struct[bu.tag])')
                                            bu(AbilityId.LAND, self.goal_of_flying_struct[bu.tag])
                                            self.readies_delayed[bu.tag] = self.frame + 8 * self.frames_per_second
                                            self.landings_of_flying_struct[bu.tag] += 1
                                else: # not at destination
                                    self.log_success('move it to a dock')
                                    self.log_command('bu(AbilityId.MOVE_MOVE,dock)')
                                    bu(AbilityId.MOVE_MOVE,dock)
        # cc landed
        for kind in {COMMANDCENTER,ORBITALCOMMAND}:
            for cc in self.structures(kind):
                if self.purpose[cc.tag] == 'land':
                    if self.frame >= self.waitframe_of_tag[cc.tag]:
                        safety = True
                        for ene in self.enemy_units: # actual visible
                            if ene.type_id not in {OVERLORD,OVERSEER}:
                                if self.near(ene.position,cc.position,9):
                                    safety = False
                        if safety:
                            if kind == COMMANDCENTER:
                                if len(cc.passengers) > 0:
                                    cc(AbilityId.UNLOADALL_COMMANDCENTER)
                            self.purpose[cc.tag] = 'scv'
                            self.log_cc(kind.name + ' '+str(cc.tag)+' ' + self.txt(cc.position) + ' landed safe.')
                        else:
                            self.log_cc(kind.name + ' '+str(cc.tag)+' ' + self.txt(cc.position) + ' landed unsafe.')
                            # set purpose to scv, so it can be moved again
                            self.purpose[cc.tag] = 'scv'


    def manage_the_wall(self):
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
                        self.speciality_of_tag[struc.tag] = 'wall'
                if not seen:
                    if not self.we_started_at(struc_type, position):
                        if (struc_type, position) not in self.chosenplaces:
                            if self.frame > 10*22:
                                if (struc_type, position) not in self.unthinkable:
                                    self.chosenplaces.append((struc_type, position))
        # up down depots
        for sd in self.structures(SUPPLYDEPOTLOWERED) + self.structures(SUPPLYDEPOT):
            if sd.tag in self.readies:
                if (SUPPLYDEPOT,sd.position) in self.wall:
                    danger = False
                    mytile = self.maptile_of_pos(sd.position)
                    for tile in self.nine[mytile]:
                        for ene in self.enemies_of_tile[tile]:
                            if self.near(ene.position,sd.position,5):
                                if not ene.is_flying:
                                    danger = True
                    # close
                    if (danger) and (sd in self.structures(SUPPLYDEPOTLOWERED)):
                        self.log_command('sd(AbilityId.MORPH_SUPPLYDEPOT_RAISE)')
                        sd(AbilityId.MORPH_SUPPLYDEPOT_RAISE)
                        self.log_success('raising')
                    # open
                    if (not danger) and (sd in self.structures(SUPPLYDEPOT)):
                        self.log_command('sd(AbilityId.MORPH_SUPPLYDEPOT_LOWER)')
                        sd(AbilityId.MORPH_SUPPLYDEPOT_LOWER)
                        self.log_success('lowering')
                    # do not idle on the depot
                    for scv in self.units(SCV):
                        if scv.tag in self.idles:
                            if self.near(scv.position,sd.position,1.5):
                                whereto = self.flee(sd.position,2)
                                self.log_command('scv.move(whereto)')
                                scv.move(whereto)
                    # marine
                    if danger:
                        for ba in self.structures(BARRACKS):
                            if ba.position == self.wall_barracks_pos:
                                if ba.tag in self.idles:
                                    if self.can_pay(MARINE):
                                        if self.check_supply(MARINE):
                                            self.log_command('ba.train(MARINE)')
                                            ba.train(MARINE)
                                            self.bought(MARINE)
                                            self.idles.remove(ba.tag)

    def lower_some_depots(self):
        for sd in self.structures(SUPPLYDEPOT):
            expo = self.expo_of_pos(sd.position)
            near = False
            for (mimpos,mimt) in self.minerals_of_expo[expo]:
                if self.near(sd.position,mimpos,5):
                    near = True
            for gas in self.vespene_geyser:
                if self.near(sd.position,gas.position,5):
                    near = True
            if near:
                self.log_command('sd(AbilityId.MORPH_SUPPLYDEPOT_LOWER)')
                sd(AbilityId.MORPH_SUPPLYDEPOT_LOWER)
                self.log_success('lowering')


    def destroyed(self):
        for stru in self.structures:
            if stru.tag in self.last_health:
                if stru.health < 0.67 * self.last_health[stru.tag]:
                    stru(AbilityId.CANCEL_BUILDINPROGRESS)


    def deserted(self):
        for s in self.structures_without_construction_SCVs():
            place = s.position
            if self.proxy(place):
                scvt = self.get_near_scvt_to_goodjob(place)
                for scv in self.units(SCV):
                    if scv.tag == scvt:
                        self.promote(scv, 'builder')
                        self.log_command('scv(AbilityId.SMART,s)')
                        scv(AbilityId.SMART, s)
                        self.structure_of_trabu_scvt[scvt] = s.type_id
                        self.goal_of_trabu_scvt[scvt] = place
            else:
                if s.health < 0.5 * self.maxhealth[s.type_id]:
                    self.log_command(s.name+'(AbilityId.CANCEL_BUILDINPROGRESS)')
                    s(AbilityId.CANCEL_BUILDINPROGRESS)
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

    def count_enemy(self):
        #     enemy_count = {} # per enemy unittype the max amount simultaneously seen
        kinds = set()
        for ene in self.enemy_units: # actual visible
            kinds.add(ene.type_id)
        for kind in kinds:
            amount = len(self.enemy_units(kind)) # actual visible
            if kind in self.enemy_count:
                self.enemy_count[kind] = max(amount,self.enemy_count[kind])
            else:
                self.enemy_count[kind] = amount


#*********************************************************************************************************************
# worker routines

    def wantscv(self) -> bool:
        wa = True
        flyingccs = len(self.structures(COMMANDCENTERFLYING)) + len(self.structures(ORBITALCOMMANDFLYING))
        if self.count_of_job['idler']  + self.count_of_job['volunteer'] >= 11 + 16 * flyingccs:
            wa = False
        if len(self.all_scvt) - self.count_of_job['suicider'] >= self.enoughworkers:
            wa = False
        return wa

    def hatescv(self) -> bool:
        ha = False
        flyingccs = len(self.structures(COMMANDCENTERFLYING)) + len(self.structures(ORBITALCOMMANDFLYING))
        if self.count_of_job['idler']  + self.count_of_job['volunteer'] >= 21 + 16 * flyingccs:
            ha = True
        if len(self.all_scvt) - self.count_of_job['suicider'] >= self.enoughworkers + 10:
            ha = True
        return ha

    def maxout_sacrifice(self):
        # sacrifice some mimminers to make an extra bc
        if self.supply_used >= 190:
            self.reached_max_supply_once = True
        # turn idle sacrifices against eachother
        if self.count_of_job['sacrifice'] > 1:
            victimtag = self.notag
            victim = None
            for scv in self.units(SCV):
                scvt = scv.tag
                if scvt in self.idles:
                    job = self.job_of_scvt[scvt]
                    if job == 'sacrifice':
                        if victimtag == self.notag:
                            victimtag = scvt
                            victim = scv
                        else:
                            scv.attack(victim)
        # turn lone sacrifice to suicider
        if self.count_of_job['sacrifice'] == 1:
            for scv in self.units(SCV):
                scvt = scv.tag
                job = self.job_of_scvt[scvt]
                if job == 'sacrifice':
                    self.promote(scv,'suicider')
        # sacrifice 8 mimminers.
        if self.supply_used - self.count_of_job['sacrifice'] >= 194:
            if (self.minerals >= 500) and (self.vespene >= 400):
                if self.count_of_job['mimminer'] >= 16:
                    if len(self.units(BATTLECRUISER)) > 0:
                        # sacrifice 8 workers (one will remain)
                        for pair in range(0,4):
                            onescv = None
                            onescvtag = self.notag
                            otherscv = None
                            otherscvtag = self.notag
                            for scv in self.units(SCV):
                                scvt = scv.tag
                                if self.job_of_scvt[scvt] == 'mimminer':
                                    if onescvtag == self.notag:
                                        onescvtag = scvt
                                        onescv = scv
                                    elif otherscvtag == self.notag:
                                        otherscvtag = scvt
                                        otherscv = scv
                                        bestsd = self.sdist(onescv.position,otherscv.position)
                                    else:
                                        onesd = self.sdist(scv.position,onescv.position)
                                        if onesd < bestsd:
                                            bestsd = onesd
                                            otherscvtag = scvt
                                            otherscv = scv
                                        else:
                                            othersd = self.sdist(scv.position,otherscv.position)
                                            if othersd < bestsd:
                                                bestsd = othersd
                                                onescvtag = scvt
                                                onescv = scv
                            self.promote(onescv,'sacrifice')
                            self.promote(otherscv,'sacrifice')
                            onescv.attack(otherscv)
                            otherscv.attack(onescv)

    def reserve_for_orbitals(self) -> bool:
        toreserve = 0
        orbitals_first = True
        for bu in self.buildseries_exe:
            if bu == ORBITALCOMMAND:
                if orbitals_first:
                    toreserve += 150
            else:
                orbitals_first = False
        return self.minerals >= toreserve + 50

    async def build_worker(self,amount):
        # ignore self.already_pending(SCV) as it is slow
        if self.count_of_job['idler'] + self.count_of_job['volunteer'] > 1: # allow new scv temporary idler
            # try oc first
            todo = 1
            for cc in self.structures(COMMANDCENTER):
                if cc.tag in self.readies:
                    if cc.tag in self.idles:
                        if cc.position in self.cc_destiny:
                            if self.cc_destiny[cc.position] == 'oc':
                                if self.can_pay(ORBITALCOMMAND):
                                    if todo > 0:
                                        todo -= 1
                                        self.throw_at_spot(ORBITALCOMMAND, cc.position, 'build_worker')
        # new scv
        todo = amount - self.units(SCV).amount
        todo = min(todo,self.supply_left)
        if self.reached_max_supply_once:
            todo = 0
        if todo > 0:
            todo = 1 # max 1 per frame
            if self.wantscv():
                if self.production_no_pause(SCV):
                    for cc in self.all_bases:
                        nearfree = False
                        if cc.tag in self.idles: # skipping gym
                            nearfree = True
                        for (martype, bartype, pos, dura) in self.eggs:
                            if (pos == cc.position) and (dura < 2):
                                nearfree = True
                        if len(cc.orders) > 1:
                            nearfree = False
                        if nearfree:
                            if cc.tag not in (self.ambition_of_strt.keys()):
                                if self.purpose[cc.tag] == 'scv':
                                    # always urgent
                                    if self.can_pay(SCV):
                                        if self.supply_left > 0:
                                            if cc.tag in self.last_health:
                                                if cc.health >= self.last_health[cc.tag]:
                                                    if self.reserve_for_orbitals():
                                                        if todo > 0:
                                                            if self.no_doubling(cc.tag):
                                                                todo -= 1
                                                                self.log_workers('training a new scv')
                                                                self.log_command('cc.train(SCV)')
                                                                cc.train(SCV)
                                                                self.bought(SCV)
                                                                if cc.tag in self.idles:
                                                                    self.idles.remove(cc.tag)


    #######################################################################################

    async def mules(self):
        for oc in self.structures(ORBITALCOMMAND):
            if oc.tag in self.readies:
                if oc.energy >= 50:
                    if len(self.all_minerals) > 0:
                        bestqual = -99999
                        pog = 0
                        while (pog < 80):
                            pog += 1
                            patch = random.choice(self.mineral_field)
                            ok = True
                            ptag = self.postag(patch.position)
                            if ptag in self.mulestart_of_ptag:
                                if self.mulestart_of_ptag[ptag] + 1450 > self.frame:
                                    ok = False
                            if ok:
                                itssd = 99999
                                for kind in [COMMANDCENTER,ORBITALCOMMAND,PLANETARYFORTRESS]:
                                    for cc in self.structures(kind):
                                        if cc.tag in self.readies:
                                            sd = self.sdist(cc.position,patch.position)
                                            itssd = min(itssd,sd)
                                itsqual = self.simpledist(patch.position,self.loved_pos) - itssd
                                if itsqual > bestqual:
                                    bestqual = itsqual
                                    bestpatch = patch
                        if bestqual > -99999:
                            patch = bestpatch
                            oc(AbilityId.CALLDOWNMULE_CALLDOWNMULE, patch)
                            ptag = self.postag(patch.position)
                            self.mulestart_of_ptag[ptag] = self.frame


    def be_gasminer(self,scv,gas):
        (gaspos,gast) = gas
        self.go_gather_gas(scv,gas)
        self.gas_of_minert[scv.tag] = gas
        self.nminers_of_gast[gast] += 1

    def be_mimminer(self,scv,mim):
        (mimpos,mimt) = mim
        if self.nminers_of_mimt[mimt] == 0: # first miner
            self.go_gather_mim(scv,mim)
        self.mim_of_minert[scv.tag] = mim
        (mimpos,mimt) = mim
        self.nminers_of_mimt[mimt] += 1

    def promote(self, scv,new_job):
        scvt = scv.tag
        old_job = self.job_of_scvt[scvt]
        if old_job == 'gasminer':
            if scvt in self.gas_of_minert:
                gas = self.gas_of_minert[scvt]
                (gaspos,gast) = gas 
                self.nminers_of_gast[gast] -= 1
                del self.gas_of_minert[scvt]
        elif old_job == 'mimminer':
            if scvt in self.mim_of_minert:
                mim = self.mim_of_minert[scvt]
                (mimpos, mimt) = mim
                self.nminers_of_mimt[mimt] -= 1
                del self.mim_of_minert[scvt]
        self.count_of_job[old_job] -= 1
        self.count_of_job[new_job] += 1
        self.job_of_scvt[scvt] = new_job
        self.log_workers('promoted ' + old_job + ' to ' + new_job + ' ' + self.name(scvt))
        if new_job == 'fleeer':
            place = self.random_mappoint()
            self.log_command('scv(AbilityId.MOVE_MOVE,place)')
            scv(AbilityId.MOVE_MOVE, place)
        # for other new_job, code elsewhere
        # stop the scv from being repaired
        for reptag in self.thingtag_of_repairertag:
            if self.thingtag_of_repairertag[reptag] == scv.tag:
                for rep in self.units(SCV):
                    if rep.tag == reptag:
                        # promote repairing one to idler
                        old_job = self.job_of_scvt[rep.tag]
                        new_job = 'idler'
                        self.count_of_job[old_job] -= 1
                        self.count_of_job[new_job] += 1
                        self.job_of_scvt[rep.tag] = new_job
                        rep.move(rep.position.towards(self.loved_pos,0.1))
                        # thingtag_of_repairertag will notice next runstep

    def do_repair(self):
        if (self.workerrushstate != 'busy') and (self.minerals >= 70):
            # If something needs repair, promote someone to repairer
            if len(self.thingtag_of_repairertag) * 2 < len(self.units(SCV)) - 6:
                low_qual = 1.0
                wreck = self.notag
                for strtype in self.all_repairable_shooters:
                    for s in self.structures(strtype) + self.units(strtype):
                        if (s.tag in self.readies) or (s in self.units(strtype)):
                            handable = True
                            if (strtype == BATTLECRUISER):
                                for order in s.orders:
                                    if order.ability.id == AbilityId.EFFECT_TACTICALJUMP:
                                        handable = False
                            if s.tag in self.speciality_of_tag:
                                if (strtype == MEDIVAC): # repair drew this off track
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
                    for s in self.structures:
                        if s.tag in self.readies:
                            if s.type_id not in self.all_repairable_shooters:
                                if (s.type_id == BARRACKSFLYING) and (self.game_phase != 'opening'):
                                    pass # flying funnier than repair
                                else: # may repair
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
                # if no wreck then repair an scv
                if low_qual == 1.0:
                    for s in self.units(SCV):
                        if s.tag in self.job_of_scvt:
                            job = self.job_of_scvt[s.tag]
                            if (job in self.bad_jobs):
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
                                                if scvt != s.tag:
                                                    couldhaverep = True
                                    if (hasrepairers < 1) and (couldhaverep):
                                        low_qual = qual
                                        wreck = s
                                        wreckexpo = expo
                # repair
                if low_qual < 1.0:
                    # We have a wreck needing repair. Assign one repairer.
                    scvt = self.get_near_scvt_to_goodjob(wreck.position)
                    for scv in self.scvs_of_expo[wreckexpo]:
                        cheesertag = scv.tag
                        if self.job_of_scvt[cheesertag] == 'cheeser':
                            if not scv.is_constructing_scv:
                                if cheesertag not in self.thingtag_of_repairertag:
                                    if scv.tag != wreck.tag:
                                        scvt = cheesertag
                    for scv in self.scvs_of_expo[wreckexpo]:
                        if scv.tag == scvt:
                            if self.job_of_scvt[scvt] != 'cheeser':
                                self.promote(scv,'repairer')
                            self.thingtag_of_repairertag[scv.tag] = wreck.tag
                            #self.log_command('scv.repair('+wreck.name+')')
                            #scv.repair(wreck)
                            scv(AbilityId.EFFECT_REPAIR_SCV,wreck)
                            self.prevent_doubling(scvt)
                            # do not have repairers trailing vikings
                            if wreck in self.units:
                                if wreck.type_id != SCV:
                                    wreck.move(scv.position)
                # sometimes a cheeser or repairer forgets he was repairing, e.g. when no minerals
                for scvt in self.thingtag_of_repairertag:
                    for scv in self.units(SCV):
                        if scv.tag == scvt:
                            seen = False
                            for order in scv.orders:
                                if order.ability.id == AbilityId.EFFECT_REPAIR:
                                    seen = True
                            if not seen:
                                if self.no_doubling(scvt):
                                    for s in self.structures + self.units:
                                        if s.tag == self.thingtag_of_repairertag[scvt]:
                                            scv(AbilityId.EFFECT_REPAIR_SCV,s)
                # logging
                count_of_thing = {}
                for reptag in self.thingtag_of_repairertag:
                    thitag = self.thingtag_of_repairertag[reptag]
                    if thitag in count_of_thing:
                        count_of_thing[thitag] += 1
                    else:
                        count_of_thing[thitag] = 1
                for s in self.structures + self.units:
                    if s.tag in count_of_thing:
                        self.log_success('repairing a '+s.type_id.name+' with '+str(count_of_thing[s.tag]))

    async def manage_workers(self):
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
            if self.job_of_scvt[scvt] in {'applicant','candidate','carrier'}:
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
                    self.log_success('a miner in panic!')
                    self.promote(scv,'fleeer') # includes move
            # builders start to mine after building a geyser
            # sometimes we can fit him in.
            if job == 'builder':
                if scv.is_collecting:
                    best_sdist = 99999
                    best_gas = (self.nowhere, self.notag)
                    for gas in self.all_gas_to_mine:
                        (gaspos, gast) = gas
                        sd = self.sdist(gaspos, scv.position)
                        if sd < best_sdist:
                            best_sdist = sd
                            best_gas = gas
                    gas = best_gas
                    (gaspos,gast) = gas
                    if gast in self.nminers_of_gast:
                        if self.nminers_of_gast[gast] < 3:
                            self.promote(scv,'gasminer')
                            self.be_gasminer(scv,gas)
        #
        # idle scvs:
        for scv in self.units(SCV):
            scvt = scv.tag
            if scvt in self.idles:
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
                    if job == 'inshock':
                        self.promote(scv,'fleeer') # includes move
                    else:
                        self.promote(scv,'idler')
                if job == 'traveller':
                    if not self.near(scv.position,self.goal_of_trabu_scvt[scvt],3):
                        # the traveller has been blocked
                        self.log_command('scv(AbilityId.MOVE_MOVE,self.goal_of_trabu_scvt[scvt])')
                        scv(AbilityId.MOVE_MOVE,self.goal_of_trabu_scvt[scvt])
                        self.solve_blockade(scv.position)
                if job == 'applicant':
                    cct = self.vision_of_scvt[scvt]
                    for cc in self.all_mine_bases:
                        if cc.tag == cct:
                            expo = self.expo_of_pos(cc.position)
                            employment = self.employment_of_expo[expo]
                            if self.near(scv.position, employment, 3):
                                if scv.is_carrying_minerals or scv.is_carrying_vespene:
                                    self.promote(scv, 'carrier')  # deliver first
                                    scv(AbilityId.SMART,cc)
                                else:
                                    self.promote(scv, 'candidate')  # can become miner
                            else: # the applicant has been blocked
                                self.log_command('scv(AbilityId.MOVE_MOVE,employment)')
                                scv(AbilityId.MOVE_MOVE,employment)
        #
        #
        # scout1 please
        if (self.scout1_tag == self.notag) and (len(self.structures) >= 3) and (len(self.units) >= 10):
            scvt = self.get_near_scvt_to_goodjob(self.enemy_pos)
            for scv in self.units(SCV):
                if scv.tag == scvt:
                    self.promote(scv,'scout')
                    # mark it and start running around
                    self.scout1_tag = scvt
                    self.scout1_pole = 0
                    self.go_move(scv,self.scout1_pos[0])
        # scout2 please
        if (self.scout2_tag == self.notag) and (len(self.structures) >= 8) and (len(self.units) >= 10):
            scvt = self.get_near_scvt_to_goodjob(self.loved_pos)
            for scv in self.units(SCV):
                if scv.tag == scvt:
                    self.promote(scv,'scout')
                    # mark it and start running around
                    self.scout2_tag = scvt
                    self.scout2_pole = 0
                    self.go_move(scv,self.scout2_pos[0])
        # expansionblocker
        if self.game_choice[61]:
            if not self.rushopening: # that would be a bad combination
                if (self.blocker_tag == self.notag):
                    self.blocker_tag = self.get_near_scvt_to_goodjob(self.enemy_pos)
                    for scv in self.units(SCV):
                        if scv.tag == self.blocker_tag:
                            self.promote(scv,'scout')
                            self.blocker_pole = 0
                            scv.move(self.blocker_pos[0])


    def protection(self):
        # reporter for an attacked builder
        if len(self.units(SCV)) > 7:
            for bui in self.units(SCV):
                if self.job_of_scvt[bui.tag] == 'builder':
                    if bui.health < self.last_health[bui.tag]:
                        if bui.tag not in self.reporter_of_scvt:
                            repo_tag = self.get_near_scvt_to_goodjob(bui.position)
                            for repo in self.units(SCV):
                                if repo.tag == repo_tag:
                                    self.reporter_of_scvt[bui.tag] = repo.tag
                                    self.promote(repo,'reporter')
                                    repo.attack(bui.position)
        todel = set()
        for bui_tag in self.reporter_of_scvt:
            if self.job_of_scvt[bui.tag] != 'builder':
                todel.add(bui_tag)
        for bui_tag in todel:
            del self.reporter_of_scvt[bui_tag]

    def blocker(self):
        if self.game_choice[61]:
            if self.frame >= self.last_blocker_frame + 5:
                circleframes = 96
                self.last_blocker_frame = self.frame
                self.blocker_pole = self.frame % circleframes
                for scv in self.units(SCV):
                    if scv.tag == self.blocker_tag:
                        goal = self.blocker_pos[self.blocker_pole]
                        # high APM command not logged
                        scv.move(goal)
                        if self.blocker_pole < 5:
                            for tp in self.enemy_structureinfo:
                                (typ,pos) = tp
                                if self.near(pos,self.enemy_expand_pos,5):
                                    self.next_blocker()

    def init_blocker(self):
        self.enemy_expansions = []
        self.enemy_expand_pos = self.enemy_pos
        self.next_blocker()

    def next_blocker(self):
        circleframes = 96
        self.enemy_expansions.append(self.enemy_expand_pos)
        bestsd = 99999
        for pos in self.expansion_locations:
            if pos not in self.enemy_expansions:
                sd = self.sdist(pos,self.enemyramp_pos)
                if sd < bestsd:
                    self.enemy_expand_pos = pos
                    bestsd = sd
        self.blocker_pos = []
        self.make_circle(circleframes)
        for point in self.circle:
            self.blocker_pos.append(Point2((self.enemy_expand_pos.x+4*point.x,self.enemy_expand_pos.y+4*point.y)))

    def continue_fleecircle(self):
        if len(self.fleecirclers) > 0:
            seenene = False
            for ene in self.enemy_units: # actual visible
                if self.near(ene.position,self.followers,10):
                    seenene = True
            if seenene:
                for scv in self.units(SCV):
                    if scv.tag in self.fleecirclers:
                        self.fleecirclemove(scv)
            else: # no enemies
                for scv in self.units(SCV):
                    if scv.tag in self.fleecirclers:
                        self.promote(scv,'idler')
                self.fleecirclers = set()

    async def get_applicants(self):
        # after we tried local miner hiring, want applicants
        if self.mimminer_vacatures()+self.gasminer_vacatures() > len(self.vision_of_scvt):
            self.wanted_of_cct = {}
            for cc in self.all_mine_bases:
                cct = cc.tag
                self.wanted_of_cct[cct] = 0
                expo = self.expo_of_pos(cc.position)
                # per mimt: 2 - existing workers
                for mim in self.minerals_of_expo[expo]:
                    if mim in self.all_mim_to_mine:
                        (mimpos, mimt) = mim
                        self.wanted_of_cct[cct] += (2 - self.nminers_of_mimt[mimt])
                # per gast: 3 - existing workers
                for gas in self.vespene_of_expo[expo]:
                    if gas in self.all_gas_to_mine:
                        (gaspos,gast) = gas
                        self.wanted_of_cct[cct] += (3 - self.nminers_of_gast[gast])
            # decrease self.wanted_of_cct for walking applicants,carriers,candidates
            for scvt in self.vision_of_scvt:
                cct = self.vision_of_scvt[scvt]
                self.wanted_of_cct[cct] -= 1
            # search applicants
            candidates = set()
            for scv in self.units(SCV):
                scvt = scv.tag
                job = self.job_of_scvt[scvt]
                if (job in self.no_jobs) and (job != 'suicider'):
                    candidates.add(scv)
            total_wish = 0
            for cc in self.all_mine_bases:
                total_wish += self.wanted_of_cct[cc.tag]
            if total_wish < len(candidates):
                for cc in self.all_mine_bases:
                    expo = self.expo_of_pos(cc.position)
                    employment = self.employment_of_expo[expo]
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
                    for cc in self.all_mine_bases:
                        if cc.tag == cct:
                            expo = self.expo_of_pos(cc.position)
                            employment = self.employment_of_expo[expo]
                            self.wanted_of_cct[cc.tag] -= 1
                            self.promote(scv,'applicant')
                            self.log_command('scv(AbilityId.MOVE_MOVE,employment)')
                            scv(AbilityId.MOVE_MOVE,employment)
                            self.vision_of_scvt[scvt] = cc.tag

    async def manage_gas(self):
        self.log_gasminer()
        # not mining any more
        for scvt in self.all_scvt:
            if self.job_of_scvt[scvt] == 'gasminer':
                if scvt not in self.gas_of_minert:
                    for scv in self.units(SCV):
                        if scv.tag == scvt:
                            self.promote(scv,'idler')
        self.fix_count_of_job()
        # candidate to gasminer
        if self.count_of_job['candidate'] > 0:
            for scv in self.units(SCV):
                scvt = scv.tag
                job = self.job_of_scvt[scvt]
                if (job == 'candidate'):
                    cct = self.vision_of_scvt[scvt]
                    for cc in self.all_mine_bases:
                        if cc.tag == cct:
                            expo = self.expo_of_pos(cc.position)
                            for gas in self.vespene_of_expo[expo]:
                                if gas in self.all_gas_to_mine:
                                    (gaspos,gast) = gas
                                    if self.nminers_of_gast[gast] < 3:
                                        self.promote(scv, 'gasminer')
                                        self.be_gasminer(scv,gas)
        self.log_gasminer()

    async def manage_minerals(self):
        # carriers are carrying
        for scv in self.units(SCV):
            scvt = scv.tag
            if self.job_of_scvt[scvt] == 'carrier':
                if not (scv.is_carrying_minerals or scv.is_carrying_vespene):
                    scv(AbilityId.STOP)
                    self.promote(scv,'candidate')
        # not mining any more
        for scvt in self.all_scvt:
            if self.job_of_scvt[scvt] == 'mimminer':
                if scvt not in self.mim_of_minert:
                    for scv in self.units(SCV):
                        if scv.tag == scvt:
                            self.promote(scv,'idler')
        self.fix_count_of_job()
        # candidate to mimminer
        if self.count_of_job['candidate'] > 0:
            for scv in self.units(SCV):
                scvt = scv.tag
                job = self.job_of_scvt[scvt]
                if (job == 'candidate'):
                    cct = self.vision_of_scvt[scvt]
                    for cc in self.all_mine_bases:
                        if cc.tag == cct:
                            expo = self.expo_of_pos(cc.position)
                            for mim in self.minerals_of_expo[expo]:
                                if mim in self.all_mim_to_mine:
                                    (mimpos,mimt) = mim
                                    if self.nminers_of_mimt[mimt] < 2:
                                        self.promote(scv, 'mimminer')
                                        self.be_mimminer(scv,mim)


    async def more_gas(self):
        # try to swap a mimminer to gasminer
        todo = 1
        self.fix_nminers_of_gast()
        if self.gasminer_vacatures() > 0:
            gas = (self.nowhere,self.notag)
            for maybegas in self.all_gas_to_mine:
                (gaspos, gast) = maybegas
                if self.nminers_of_gast[gast] < 3:
                    gas = maybegas
            (gaspos, gast) = gas
            for scv in self.units(SCV):
                scvt = scv.tag
                if self.job_of_scvt[scvt] == 'mimminer':
                    if self.near(scv.position, gaspos, self.miner_bound):
                        if todo>0:
                            todo -= 1
                            self.promote(scv,'gasminer')
                            self.be_gasminer(scv,gas)

    async def more_minerals(self):
        # try to swap a gasminer to mimminer
        todo = 1
        self.fix_nminers_of_mimt()
        if self.mimminer_vacatures() > 0:
            thismimt = self.notag
            for mim in self.all_mim_to_mine:
                (mimpos, mimt) = mim
                if self.nminers_of_mimt[mimt] < 2:
                    thismimt = mimt
            for mim in self.all_minerals:
                (mimpos,mimt) = mim
                if mimt == thismimt:
                    for scv in self.units(SCV):
                        scvt = scv.tag
                        if self.job_of_scvt[scvt] == 'gasminer':
                            if self.near(scv.position, mimpos, self.miner_bound):
                                if todo>0:
                                    todo -= 1
                                    self.promote(scv,'mimminer')
                                    self.be_mimminer(scv,mim)

    async def manage_rest(self):
        self.fix_count_of_job()
        #       
        #
        #  max idle workers
        if self.hatescv():
            todo = 1
            for scv in self.units(SCV):
                scvt = scv.tag
                if scvt in self.all_scvt:
                    job = self.job_of_scvt[scvt]
                    if (job in self.no_jobs) and (job != 'suicider'):
                        if todo > 0:
                            todo -= 1
                            self.promote(scv,'suicider')
                            self.log_command('scv.attack(self.enemy_pos)')
                            scv.attack(self.enemy_pos)
            for scv in self.units(SCV):
                scvt = scv.tag
                if scvt in self.all_scvt:
                    job = self.job_of_scvt[scvt]
                    if job in self.bad_jobs:
                        if todo > 0:
                            todo -= 1
                            self.promote(scv, 'suicider')
                            self.log_command('scv.attack(self.enemy_pos)')
                            scv.attack(self.enemy_pos)
        # mimminer or gasminer
        if (self.count_of_job['idler'] + self.count_of_job['volunteer'] == 0):
            if self.vespene < 1000: # new, promote gas.
                await self.more_gas()
            elif self.minerals >= self.vespene + 1000:
                await self.more_gas()
            elif self.vespene >= self.minerals + 1000:
                await self.more_minerals()
        # stop escorters lured to their death
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
                tp = self.random_mappoint()
                while not self.hoxy(tp):
                    tp = self.random_mappoint()
                if self.hoxy(scv.position):
                    if scvt in self.idles:
                        self.log_command('scv.attack(tp)')
                        scv.attack(tp)
                else: # too far
                    self.log_command('scv.move(tp)')
                    scv.move(tp)


    async def gasminer_boss(self):
        # gasminers can shift off their assigned patch.
        # the boss will see this, and correct the administration.
        for scv in self.units(SCV):
            scvt = scv.tag
            if self.job_of_scvt[scvt] == 'gasminer':
                assigned_gas = self.gas_of_minert[scvt]
                (assigned_gaspos, assigned_gast) = assigned_gas
                if scvt in self.minedirection_of_scvt:
                    if scv.is_returning and (self.minedirection_of_scvt[scvt] == 'G'):
                        # it is turning round towards the base
                        if not self.near(assigned_gaspos, scv.position, 6):
                            self.log_boss('Hey a shifted gasminer ' + self.name(scvt) + ' should mine ' + str(assigned_gast))
                            # find closest vespenepatch. In equal cases promote one with less miners.
                            best_sdist = 99999
                            best_gas = (self.nowhere,self.notag)
                            for gas in self.all_gas_to_mine:
                                (gaspos, gast) = gas
                                sd = self.sdist(gaspos, scv.position)
                                sd = sd + self.nminers_of_gast[gast]
                                if sd < best_sdist:
                                    best_sdist = sd
                                    best_gas = gas
                            gas = best_gas
                            (gaspos, gast) = gas
                            if best_sdist == 99999:
                                self.log_boss('Hey no vespene found.')
                            else:
                                self.log_boss('He appears to mine ' + str(gast))
                                self.gas_of_minert[scvt] = gas
                                self.nminers_of_gast[gast] += 1
                                self.nminers_of_gast[assigned_gast] -= 1
                                if self.nminers_of_gast[gast] > 3:
                                    self.log_boss('Now I have a patch with ' + str(self.nminers_of_gast[gast]))
                    if scv.is_gathering and (self.minedirection_of_scvt[scvt] == 'R'):
                        # miner just starts from base to patch
                        gas = (self.nowhere,self.notag)
                        for ref in self.structures(REFINERY) + self.structures(REFINERYRICH):
                            if ref.tag in self.readies:
                                if ref.tag == scv.order_target:
                                    gaspos = ref.position
                                    gast = self.postag(gaspos)
                                    gas = (gaspos, gast)
                        if gas != assigned_gas:
                            (gaspos,gast) = gas
                            self.log_boss((self.name(scvt) + ' he says ' + str(gast) + ' but administrated is ' + str(assigned_gast)))
                            if gast in self.nminers_of_gast:
                                self.log_boss('I reassign him.')
                                self.gas_of_minert[scvt] = gas
                                self.nminers_of_gast[gast] += 1
                                self.nminers_of_gast[assigned_gast] -= 1
                                if self.nminers_of_gast[gast] > 3:
                                    self.log_boss('Now I have a patch with ' + str(self.nminers_of_gast[gast]))
                # correct the minedirection administration for the next look.
                if scv.is_returning:
                    self.minedirection_of_scvt[scvt] = 'R'
                if scv.is_gathering:
                    self.minedirection_of_scvt[scvt] = 'G'

    # speedmining

    def canstandon(self, point) -> bool:
        # point is ideally middle of a square where you can stand
        lu = Point2((round(point.x - 0.5), round(point.y - 0.5)))
        return (layout_if.layout[lu.x][lu.y] in {0,2})

    def speedmining(self):
        # set basepos_of_mimt
        hash = 0
        for bas in self.all_bases:
            hash += bas.position.x
        if hash != self.basepos_hash:
            self.basepos_hash = hash
            # per mimt the closest own base
            # self.nowhere if there is no landed base.
            self.basepos_of_mimt = {}
            for (mimpos,mimt) in self.all_minerals:
                bestsd = 99999
                bestbasepos = self.nowhere
                for base in self.all_bases:
                    basepos = base.position
                    sd = self.sdist(basepos, mimpos)
                    if sd < bestsd:
                        bestsd = sd
                        bestbasepos = basepos
                self.basepos_of_mimt[mimt] = bestbasepos
            # automatic hatchpoint is at average distance 2.91 from basepos
            # automatic patchpoint is at average distance 0.92 from closetst mineralpatchhalf
            for (mimpos,mimt) in self.all_minerals:
                basepos = self.basepos_of_mimt[mimt]
                mimleft = Point2((mimpos.x - 0.5, mimpos.y))
                mimright = Point2((mimpos.x + 0.5, mimpos.y))
                patchpointleft = mimleft.towards(basepos, 0.92)
                patchpointright = mimright.towards(basepos, 0.92)
                if self.sdist(mimleft,basepos) < self.sdist(mimright,basepos):
                    if self.canstandon(patchpointleft):
                        patchpoint = patchpointleft
                    else:
                        patchpoint = patchpointright
                else: # right
                    if self.canstandon(patchpointright):
                        patchpoint = patchpointright
                    else:
                        patchpoint = patchpointleft
                self.patchpoint_of_mimt[mimt] = patchpoint
        if self.supply_used >= 100:
            # normal mining
            # idle miners should mine. Rare.
            for miner in self.units(SCV):
                minert = miner.tag
                if minert in self.idles:
                    if minert in self.mim_of_minert:
                        mim = self.mim_of_minert[minert]
                        self.go_gather_mim(miner, mim)
        if self.supply_used < 100:
            # init phase_of_minert
            for minert in self.mim_of_minert:
                if minert not in self.phase_of_minert:
                    self.phase_of_minert[minert] = 'G'
            # log
            for miner in self.units(SCV):
                minert = miner.tag
                if minert in self.mim_of_minert:
                    mim = self.mim_of_minert[minert]
                    (mimpos, mimt) = mim
                    patchpoint = self.patchpoint_of_mimt[mimt]
                    ppdist = self.circledist(patchpoint, miner.position)
                    if minert not in self.lastppdist_of_minert:
                        self.lastppdist_of_minert[minert] = ppdist
                    speed = ppdist - self.lastppdist_of_minert[minert]
                    if minert not in self.lastspeed_of_minert:
                        self.lastspeed_of_minert[minert] = speed
                    acc = speed - self.lastspeed_of_minert[minert]
                    exclama = ''
                    if abs(acc) >= 0.06:
                        exclama = '!'
                    self.log_speedmining(
                        self.name(minert) + '   ' + str(round(100*ppdist)) + ' ' + str(round(100*speed))
                        + ' ' + str(round(100*acc)) + '   ' + self.phase_of_minert[minert] + exclama)
                    self.lastspeed_of_minert[minert] = speed
            # idle miners should mine. This is rare.
            for miner in self.units(SCV):
                minert = miner.tag
                if minert in self.idles:
                    if minert in self.mim_of_minert:
                        # move to waitpoint, start gather when other is at miningframe start_to_speed
                        thismim = self.mim_of_minert[minert]
                        (thismimpos, thismimt) = thismim
                        patchpoint = self.patchpoint_of_mimt[thismimt]
                        basepos = self.basepos_of_mimt[thismimt]
                        waitpoint = patchpoint.towards(basepos, 2)
                        wait = False
                        for otherminert in self.mim_of_minert:
                            if self.mim_of_minert[otherminert] == thismim:
                                if otherminert < minert:  # smallest first
                                    wait = True
                                    if otherminert in self.miningframe_of_minert:
                                        othertime = self.frame - self.miningframe_of_minert[otherminert]
                                        if (othertime >= self.start_to_speed) and (othertime < self.start_to_speed + 20):
                                            wait = False
                        if not self.near(miner.position, waitpoint, 1.0):
                            wait = True  # move to waitpoint
                        if wait:
                            if not self.near(miner.position, waitpoint, 1.0):
                                miner.move(waitpoint)
                        else:  # start mining
                            for mim in self.all_minerals:
                                (mimpos, mimt) = mim
                                if mimt == thismimt:
                                    self.go_gather_mim(miner, mim)
            # miningframe_of_minert
            for miner in self.units(SCV):
                minert = miner.tag
                if minert in self.mim_of_minert:
                    mim = self.mim_of_minert[minert]
                    (mimpos, mimt) = mim
                    patchpoint = self.patchpoint_of_mimt[mimt]
                    if minert not in self.miningframe_of_minert:
                        self.miningframe_of_minert[minert] = -99999
                    ppdist = self.circledist(patchpoint, miner.position)
                    # miningframe: moment the scv is 3 near the patchpoint
                    if (ppdist < 3):
                        if not miner.is_carrying_minerals:
                            if self.miningframe_of_minert[minert] + 90 < self.frame: # roundtrip > 90
                                if (ppdist > 2):
                                    self.miningframe_of_minert[minert] = self.frame
            # calibrating miningframe on ppdist
            for miner in self.units(SCV):
                minert = miner.tag
                if minert in self.mim_of_minert:
                    mim = self.mim_of_minert[minert]
                    (mimpos, mimt) = mim
                    phase = self.phase_of_minert[minert]
                    patchpoint = self.patchpoint_of_mimt[mimt]
                    ppdist = self.circledist(patchpoint, miner.position)
                    time = self.frame - self.miningframe_of_minert[minert]
                    if minert not in self.lastppdist_of_minert:
                        self.lastppdist_of_minert[minert] = ppdist
                    speed = (ppdist - self.lastppdist_of_minert[minert]) / self.chosen_game_step
                    if ppdist > 0.2:
                        if phase in {'H','I'}:
                            calctime = round(2 + (3-ppdist) / self.scv_step)
                            if calctime < time:
                                # calibrating miningframe
                                self.miningframe_of_minert[minert] = self.frame - calctime
            # speedmining
            for miner in self.units(SCV):
                minert = miner.tag
                if minert in self.mim_of_minert:
                    mim = self.mim_of_minert[minert]
                    (mimpos, mimt) = mim
                    phase = self.phase_of_minert[minert]
                    patchpoint = self.patchpoint_of_mimt[mimt]
                    ppdist = self.circledist(patchpoint, miner.position)
                    if phase in {'G','H','W','I'}:
                        if miner.is_carrying_minerals:
                            # it turns to return; patchpoint
                            phase = 'R'
                    if phase == 'R':
                        if not miner.is_carrying_minerals:
                            # it turns to gather; hatchpoint
                            phase = 'G'
                    if phase == 'G':
                        if self.near(miner.position, patchpoint, 3):
                            phase = 'I'
                            for othert in self.mim_of_minert:
                                if othert != minert:
                                    if mim == self.mim_of_minert[othert]:
                                        basepos = self.basepos_of_mimt[mimt]
                                        waitpoint = patchpoint.towards(basepos, 2)
                                        if othert in self.miningframe_of_minert:
                                            othertime = self.frame - self.miningframe_of_minert[othert]
                                            if othertime < self.start_to_speed:
                                                phase = 'W'
                                                miner.move(waitpoint)
                                        if othert in self.phase_of_minert:
                                            if self.phase_of_minert[othert] == 'I':
                                                phase = 'W'
                                                miner.move(waitpoint)
                    if phase == 'W':
                        wait = False
                        for othert in self.mim_of_minert:
                            if othert != minert:
                                if mim == self.mim_of_minert[othert]:
                                    if othert in self.miningframe_of_minert:
                                        wait = True
                                        othertime = self.frame - self.miningframe_of_minert[othert]
                                        if othertime >= self.start_to_speed:
                                            wait = False
                                    if othert in self.phase_of_minert:
                                        if self.phase_of_minert[othert] == 'I':
                                            wait = True
                        if not wait:
                            phase = 'I'
                            for mim in self.all_minerals:
                                if mim[1] == mimt:
                                    self.go_gather_mim(miner,mim)
                    if phase == 'I':
                        if self.near(miner.position, patchpoint, 1.5):
                            phase = 'H'
                            for patch in self.mineral_field:
                                if self.postag_of_patch(patch) == mimt:
                                    miner.move(patchpoint)
                                    miner(AbilityId.HARVEST_GATHER_SCV,patch,queue=True)
                    if phase == 'H':
                        # expect ppdist decreasing
                        if ppdist > self.lastppdist_of_minert[minert] + 0.2:
                            # Should be rare. When this happens, the order has shifted.
                            for patch in self.mineral_field:
                                if self.postag_of_patch(patch) == mimt:
                                    miner(AbilityId.HARVEST_GATHER_SCV, patch)
                    self.phase_of_minert[minert] = phase
                    self.lastppdist_of_minert[minert] = ppdist # do not use beyond this point



    async def scv_endgame(self):
        # volunteer to idler
        for scv in self.units(SCV):
            scvt = scv.tag
            if scvt in self.idles:
                if self.job_of_scvt[scvt] == 'volunteer':
                    self.promote(scv,'idler')
        # idler to volunteer
        if self.minerals < 999:
            for scvt in self.all_scvt:
                if self.job_of_scvt[scvt] == 'idler':
                    if len(self.all_minerals) > 0:
                        mim = random.choice(tuple(self.all_minerals))
                        tries = 0
                        while (mim in self.all_mim_to_mine) and (tries<100):
                            tries += 1
                            mim = random.choice(tuple(self.all_minerals))
                        for scv in self.units(SCV):
                            if scv.tag == scvt:
                                self.promote(scv,'volunteer')
                                self.go_gather_mim(scv,mim)

    def hop_cc(self):
        # there are in-between ccs, so expo cannot be used.
        tomove = set() # of cc
        cancelable = {AbilityId.COMMANDCENTERTRAIN_SCV}
        # tomove (cc)
        for cc in self.structures(COMMANDCENTER) + self.structures(ORBITALCOMMAND):
            if cc.tag in self.readies:
                if cc.tag not in self.speciality_of_tag:
                    if self.purpose[cc.tag] == 'scv':
                        movable = True
                        for order in cc.orders:
                            if order.ability.id not in cancelable:
                                movable = False
                        if movable:
                            # move reason: low minerals
                            patches = 0
                            for (mimpos, mimt) in self.all_minerals:
                                if self.near(mimpos,cc.position,10):
                                    patches +=1
                            if patches < 4:
                                tomove.add(cc)
                            # move reason: enemies
                            strength = 0
                            mytile = self.maptile_of_pos(cc.position)
                            for tile in self.nine[mytile]:
                                for myn in self.goodguys_of_tile[tile]:
                                    if self.near(myn.position, cc.position, 10):
                                        strength += self.ground_strength(myn)
                                for ene in self.enemies_of_tile[tile]:
                                    if self.near(ene.position,cc.position,10):
                                        strength -= self.ground_strength(ene)
                            if strength < -50: # about 3 marines
                                tomove.add(cc)
        # moveto (cc_pos)
        moveto = set() # of ccpos
        if len(tomove) > 0:
            for ccpos in self.expansion_locations:
                patches = 0
                for (mimpos, mimt) in self.all_minerals:
                    if self.near(mimpos, ccpos, 10):
                        patches += 1
                if patches >= 4:
                    strength = 0
                    mytile = self.maptile_of_pos(ccpos)
                    for tile in self.nine[mytile]:
                        for myn in self.goodguys_of_tile[tile]:
                            if self.near(myn.position, ccpos, 10):
                                strength += self.ground_strength(myn)
                        for ene in self.enemies_of_tile[tile]:
                            if self.near(ene.position, ccpos, 10):
                                strength -= self.ground_strength(ene)
                    if strength >= -50:  # about 3 marines
                        if self.check_layout(COMMANDCENTER,ccpos):
                            moveto.add(ccpos)
        # do 1 move
        if (len(tomove) > 0) and (len(moveto) > 0):
            minsd = 99999
            if len(tomove) > len(moveto):
                moveto_choice = random.choice(tuple(moveto))
                for cc in tomove:
                    sd = self.sdist(cc.position,moveto_choice)
                    if (sd < minsd):
                        tomove_choice = cc
                        minsd = sd
            else: # len(tomove) <= len(moveto)
                tomove_choice = random.choice(tuple(tomove))
                for ccpos in moveto:
                    sd = self.sdist(ccpos, tomove_choice.position)
                    if (sd < minsd):
                        moveto_choice = ccpos
                        minsd = sd
            # hop tomove_choice to moveto_choice
            cc = tomove_choice
            self.write_layout(COMMANDCENTER,moveto_choice) # guarded by goal_of_flying_struc
            for order in cc.orders:
                if order.ability.id in cancelable:
                    self.log_command('cc(AbilityId.CANCEL_BUILDINPROGRESS)')
                    cc(AbilityId.CANCEL_BUILDINPROGRESS)
                    self.log_command('cc(AbilityId.CANCEL_QUEUECANCELTOSELECTION)')  # build worker
                    cc(AbilityId.CANCEL_QUEUECANCELTOSELECTION)
            self.goal_of_flying_struct[cc.tag] = moveto_choice
            self.landings_of_flying_struct[cc.tag] = 0
            self.log_success('up base')
            # lift via purpose
            if cc.type_id == COMMANDCENTER:
                self.log_cc('Commandcenter '+str(cc.tag) +' '+ self.txt(cc.position) + ' wishes to fly by hop_cc')
                self.purpose[cc.tag] = 'wishtofly'
            elif cc.type_id == ORBITALCOMMAND:
                self.log_cc('Orbitalcommand '+str(cc.tag) +' '+ self.txt(cc.position) + ' will fly by hop_cc')
                self.purpose[cc.tag] = 'fly'
            # give a hopped cc a destiny. Is this already possible?
            if cc in self.structures(COMMANDCENTER):
                self.cc_destiny[moveto_choice] = 'pf'

    #*********************************************************************************************************************

    def manage_layout(self):
        # add existing own buildings to layout
        for struc in self.structures:
            structype = struc.type_id
            place = self.position_of_building(struc)
            tag = struc.tag
            spt = (structype, place, tag)
            if spt not in self.designs:
                if structype not in self.landable:
                    if structype != AUTOTURRET:
                        placed = False
                        for (st1,pl1,ta1) in self.designs:
                            if pl1 == place:
                                placed = True
                        self.log_fail(placed,'Wild structure '+struc.name)
                        self.designs.add(spt)
        # erase layout buildings that are in designs, but neither existing there nor thought
        # if vision, delete from enemy_structureinfo
        todel = set()
        for tp in self.enemy_structureinfo:
            (typ,pos) = tp
            if self.is_visible(pos):
                seen = False
                for ene in self.enemy_real_structures:
                    if (ene.position == pos):
                        seen = True
                if not seen:
                    todel.add(tp)
        self.enemy_structureinfo -= todel
        # if vision, delete from enemy_structureinfo_plus
        todel = set()
        for tp in self.enemy_structureinfo_plus:
            (typ,pos,finish) = tp
            if self.is_visible(pos):
                seen = False
                for ene in self.enemy_real_structures:
                    if (ene.position == pos):
                        seen = True
                if not seen:
                    todel.add(tp)
        self.enemy_structureinfo_plus -= todel
        # designs: add tag to realized plans
        newdesigns = set()
        for (structype,place,tag) in self.designs:
            if tag == self.notag:
                for astruc in self.structures(structype):
                    if self.position_of_building(astruc) == place:
                        tag = astruc.tag
            newdesigns.add((structype,place,tag))
        self.designs = newdesigns.copy()
        # designs: erase if neither tag nor plan is found
        erase = set()
        for (structype,place,tag) in self.designs:
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
                if structype == MAINCELLBLOCK:
                    seen = True
            if place in self.tankplaces:
                seen = True
            for expo in range(0,self.expos):
                if place == self.airport_of_expo[expo]:
                    seen = True
                if place == self.employment_of_expo[expo]:
                    seen = True
            if place in self.goal_of_flying_struct.values():
                seen = True
            for tp in self.enemy_structureinfo:
                (typ,pos) = tp
                if place == pos:
                    seen = True
            for (th, po, status, ow) in self.throwspots:
                if place == po:
                    seen = True
            if not seen:
                erase.add((structype,place,tag))
        for (structype,place,tag) in erase:
            self.log_success('(manage_layout clean of a '+structype.name+')')
            self.erase_layout(structype,place)

# *********************************************************************************************************************

    def get_area(self, point) -> str:
        roundpoint = (round(point.x - 0.5), round(point.y - 0.5))
        stri = 'middle'
        if roundpoint in self.hometop:
            stri = 'home'
        elif roundpoint in self.enemytop:
            stri = 'enemy'
        return stri

    def walk_duration(self, pointa, pointb) -> float:
        areaa = self.get_area(pointa)
        areab = self.get_area(pointb)
        if areaa == areab:
            walk_dist = self.circledist(pointa, pointb)
        else:
            var1 = self.circledist(pointa, self.homeramp_pos) + self.circledist(self.homeramp_pos, pointb)
            var2 = self.circledist(pointa, self.enemyramp_pos) + self.circledist(self.enemyramp_pos, pointb)
            walk_dist = min(var1, var2)
        walk_dura = walk_dist / self.walk_speed
        return walk_dura

    def flystraight(self,aa,bb) -> bool:
        # can fly straight from aa to bb, no detector in self.detection_range?
        # bb should not be aa
        dist = self.circledist(aa,bb)
        mid = Point2(((aa.x+bb.x)/2,(aa.y+bb.y)/2))
        aabbvec = ((bb.x-aa.x)/dist,(bb.y-aa.y)/dist)
        perpendic = ((aa.y-bb.y)/dist,(bb.x-aa.x)/dist)
        straight = True
        for det in self.detect:
            if self.near(det,mid,self.detection_range+dist/2):
                tooclose = False
                if self.near(det,aa,self.detection_range):
                    tooclose = True
                    self.detect_improve = bb
                if self.near(det,bb,self.detection_range):
                    tooclose = True
                    self.detect_improve = bb.towards(det,-2)
                aadet = (det.x-aa.x,det.y-aa.y)
                inprovec = aadet[0]*aabbvec[0]+aadet[1]*aabbvec[1]
                inproper = aadet[0]*perpendic[0]+aadet[1]*perpendic[1]
                if (inprovec > 0) and (inprovec < dist):
                    if abs(inproper) < self.detection_range:
                        tooclose = True
                        self.detect_improve = bb.towards(det,-2)
                straight = straight and not tooclose
        return straight

#**************************************

    async def selfhate(self):
        if self.do_selfhate:
            if len(self.units) + len(self.structures) < 10:
                if self.frame >= 22 * 60 * 5:
                    if self.selfhate_frame == 99999:
                        await self._client.chat_send('I surrender voluntary under social pressure', team_only=False)
                        self.selfhate_frame = self.frame + 7 * 22
                    elif self.frame >= self.selfhate_frame:
                        await self._client.quit()

#*********************************************************************************************************************
#   strategy system
#   a strategy is, per game_choice, a probability to choose "yes".
#   the game choices can be made at the start of the game and are unknown to the opponent.
#
#   We feed back won-or-loss of a game to the strategy.
#
    async def win_loss(self):
        if self.game_result == 'doubt':
            # win and loss conditions
            # known
            known = 0
            for tp in self.enemy_structureinfo:
                (typ, pos) = tp
                if typ not in self.win_ignore:
                    known += 1
            # actual visible
            ene_max_hea = -1
            seen = 0
            for stru in self.enemy_real_structures: # visible now
                if stru.type_id not in self.win_ignore:
                    seen += 1
                    if stru.health > ene_max_hea:
                        ene_max_hea = stru.health
            if (ene_max_hea < 456) and (seen == known):
                self.game_result = 'win'
            #
            if len(self.structures) == 1:
                my_max_hea = -1
                for stru in self.structures:
                    if stru.health > my_max_hea:
                        my_max_hea = stru.health
                if my_max_hea < 456:
                    self.game_result = 'loss'
            #
            if self.selfhate_frame < 99999:
                self.game_result = 'loss'
            # tune strategy
            if self.game_result == 'win':
                for nr in range(0,self.game_choices):
                    was = self.strategy[self.stratline][nr]
                    if self.game_choice[nr]:
                        will = was * 0.85 + 0.15
                    elif nr >= self.radio_choices:
                        will = was * 0.85
                    else:
                        will = was
                    self.strategy[self.stratline][nr] = will
            elif self.game_result == 'loss':
                for nr in range(0,self.game_choices):
                    was = self.strategy[self.stratline][nr]
                    if self.game_choice[nr]:
                        will = was * 0.85
                    elif nr >= self.radio_choices:
                        will = was * 0.85 + 0.15
                    else:
                        will = was
                    self.strategy[self.stratline][nr] = will
            if self.game_result != 'doubt':
                self.log_success('gg '+self.game_result)
                self.write_strategy()
                await self._client.chat_send('gg', team_only=False)

    def write_strategy(self):
        pl = open('data/strategy.txt','w')
        stri = '# strategy.txt'
        pl.write(stri + '\n')
        for ix in range(0,len(self.strategy)):
            oppi = self.strategy_oppi[ix]
            astrat = self.strategy[ix]
            if self.there_is_a_new_opening:
                astrat[self.radio_choices - 1] = 0.51
            stri = 'opponent '+oppi
            iix = 0
            while iix < len(astrat):
                if iix % 10 == 0:
                    pl.write(stri + '\n')
                    stri = ''
                rou = round(astrat[iix]*100000)/100000
                stri = stri+str(rou)+' '
                iix += 1
            pl.write(stri + '\n')
        pl.close()

    def line_of_oppi(self, oppi):
        line = len(self.strategy_oppi)
        for mayline in range(0,len(self.strategy_oppi)):
            if self.strategy_oppi[mayline] == oppi:
                line = mayline
        return line

    async def init_strategy(self):
        # strategy is a list of winchances to choose a strategic aspect.
        # opponent-id based init strategy.
        # for unknown opponents race-based.
        #
        # file strategy.txt must have shape:
        #      # strategy.txt
        #      opponent 23-ie6-56
        #      0.775 0.006 0.111  (about 10 on a line, last line maybe less, total self.game_choices)
        #
        # defaults
        self.strategy = []
        for oppi in {'zerg','terran','protoss','someone'}:
            self.strategy_oppi.append(oppi)
            newstrategy = []
            for i in range(0,self.game_choices):
                newstrategy.append(0.5)
            self.strategy.append(newstrategy)
        # read from disk
        pl = open('data/strategy.txt','r')
        read_strategy = pl.read().splitlines()
        pl.close()
        # overwrite read lines already in strategy
        putline = -1
        putnr = 0
        for line in range(0,len(read_strategy)):
            words = read_strategy[line].split()
            if words[0] == '#':
                pass
            elif words[0] == 'opponent':
                oppi = words[1]
                putline = self.line_of_oppi(oppi)
                putnr = 0
            elif putline < len(self.strategy):
                for aword in words:
                    self.strategy[putline][putnr] = float(aword)
                    putnr += 1
        # add read lines not yet in strategy
        putline = -1
        for line in range(0,len(read_strategy)):
            words = read_strategy[line].split()
            if words[0] == '#':
                pass
            elif words[0] == 'opponent':
                # first, finish former putline
                if putline == len(self.strategy):
                    self.strategy_oppi.append(oppi)
                    self.strategy.append(newstrategy)
                oppi = words[1]
                putline = self.line_of_oppi(oppi)
                newstrategy = []
            elif putline == len(self.strategy):
                for aword in words:
                    newstrategy.append(float(aword))
        if putline == len(self.strategy):
            self.strategy_oppi.append(oppi)
            self.strategy.append(newstrategy)
        # strategy line
        self.stratline = self.line_of_oppi(self.opponent)
        # for a new opponent, add a strategy.
        if self.stratline == len(self.strategy):
            # new opponent, so use species info copy
            speciesline = self.line_of_oppi(self.enemy_species)
            newstrategy = self.strategy[speciesline].copy()
            self.strategy_oppi.append(self.opponent)
            self.strategy.append(newstrategy)
        # radio tuning
        totalsum = 0.0
        for nr in range(0,self.radio_choices):
            totalsum = totalsum + self.strategy[self.stratline][nr]
        # radiostrategy
        radiostrategy = []
        for chance in self.strategy[self.stratline]:
            radiostrategy.append(chance / totalsum)
        # init game_choice
        self.game_choice = []
        # chance-system radio_nr (using an overwrite calculation)
        radio_nr = 0
        sum = 0.0
        for nr in range(0,self.radio_choices):
            sum += radiostrategy[nr]
            if random.random() * sum < radiostrategy[nr]:
                radio_nr = nr
        # max-system radio_nr (brutal variant)
        maxval = -1
        radio_numbers = set()
        for nr in range(0,self.radio_choices):
            cval = radiostrategy[nr]
            if cval > maxval:
                maxval = cval
                radio_numbers = {nr}
            elif cval == maxval:
                radio_numbers.add(nr)
        radio_nr = random.choice(tuple(radio_numbers))
        # TO TEST use next line
        #radio_nr = 46
        for nr in range(0,self.radio_choices):
            self.game_choice.append(nr == radio_nr)
        for nr in range(self.radio_choices,self.game_choices):
            self.game_choice.append(random.random() < self.strategy[self.stratline][nr])
        self.game_result = 'doubt'

#*********************************************************************************************************************
def main():
    # Easy/Medium/Hard/VeryHard
    all_maps = ['LightshadeAIE','OxideAIE','BlackburnAIE','JagannathaAIE','2000AtmospheresAIE','RomanticideAIE']
    map = random.choice(all_maps)
    # TO TEST use next line
    #map = 'LightshadeAIE'
    opponentspecies = random.choice([Race.Terran,Race.Zerg,Race.Protoss])
    # TO TEST use next line
    #opponentspecies = Race.Zerg
    # Easy/Medium/Hard/VeryHard
    run_game(maps.get(map), [
        Bot(Race.Terran, Chaosbot()),
        Computer(opponentspecies, Difficulty.VeryHard)
        ], realtime = False)

if __name__ == "__main__":
    main()
