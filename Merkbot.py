# Merkbot.py containing Chaosbot
# author: MerkMore
# version 21 june 2020
# Burny style
import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer
from sc2.constants import *
from sc2.position import Point2
import random
from math import sqrt as sqrt



class Chaosbot(sc2.BotAI):
#   CHANGE VALUE AD LIB SECTION:
    do_log_success = True
    do_log_population = False
    do_log_gasminer = False
    do_log_resource = False
    do_log_limbo = False
    do_log_buildposition = False
    do_log_wish = True
#   CHANGE THE REST WITH CARE
#   make iteration available
    itera = -1
    routine = 'start'
#   constants
    all_structures = []
#      (as far as this program knows) 
    liftable = []
    techtree = []
    anything = []
    shipyard = None
#   gamestate values
    inrepair = []
    bestbctag = -1
#   traveller scvs have a goal
    goal_of_scvt = {}
    ambition_pf = []
    no_lab = []
    towt_of_tnkt = {}
#   The boundary for a bc to jump away
    fear = 250
#   scv management:
#   The tag of existing own scvs, in this iteration
    all_scvt = []
#   The tag of existing refineries where we want to mine from, in this iteration
    all_gast = []
#   The tag of existing minerals where we want to mine from, in this iteration
    all_mimt = []
#   job_of_scvt dictionary 
    all_job = ('gasminer','miner','traveller','escorter','builder','shiprepairer','arearepairer','idler','fighter')
    job_of_scvt = {}
    count_of_job = {}
#   arearepairers have a cottage
    cottage_of_scvt = {}
#   gas harvesting assignments
    gast_of_scvt = {}
    count_of_gast = {}
#   mineral harvesting assignments
    mimt_of_scvt = {}
    count_of_mimt = {}
#   traveller and builder have a structure to build
    structure_of_scvt = {}
#   When promoted, fire if idle, but not when not moved yet.
    promotionsite_of_scvt = {}
#   wish for rush
    rushing = True
    endwish = {}
    wish = {}
    wish_now = []
    log_wish_history = ''
#   money handling with reservations
    reserved_minerals = 0
    reserved_vespene = 0
#   stored tips
    tips = []
    tips_used = []
#   the supplydepot used as a gate:
    updown = -1
#   army coodination
    attack_phase = 'harrass'
    tried_coordinated_attack = False
#   is_repairing
    busy_arearepairer = []
#   squareroots of integers from 0 to 200*200
    stored_root = []
#   for missing scvs (fallen or in gaslimbo), the iteration is stored
    itera_of_missing_scvt = {}
#   the preferred landing place of a flying structure
    home_of_flying_struct = {}




    async def on_step(self, iteration: int):
#       make iteration available for logging
        self.itera = iteration
#       init stuff
        if len(self.techtree) == 0:
            await self.my_init()
#       
#       main iteree:
#       
        await self.gamestate_validate()
        self.log_resource()
        await self.build_worker(100-self.minerals//100)
        if self.rushing:
            for thing in self.wish_now:
                await self.build_thing(thing,True)
        for thing in self.anything:
            await self.build_thing(thing,False)
#       rest
        await self.siege_tank()
        if self.townhalls.ready.amount >= 4:
            await self.do_upgrades()
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
#       list of most structures
        self.most_struct(SUPPLYDEPOT)
        self.most_struct(BARRACKS)
        self.most_struct(REFINERY)
        self.most_struct(BARRACKSTECHLAB)
        self.most_struct(FACTORY)
        self.most_struct(FACTORYTECHLAB)
        self.most_struct(STARPORT)
        self.most_struct(STARPORTTECHLAB)
        self.most_struct(FUSIONCORE)
        self.most_struct(COMMANDCENTER)
        self.most_struct(PLANETARYFORTRESS)
        self.most_struct(ENGINEERINGBAY)
        self.most_struct(ARMORY)
#       liftable
        self.liftable = [BARRACKS,FACTORY,STARPORT,COMMANDCENTER]
        self.landable = [BARRACKSFLYING,FACTORYFLYING,STARPORTFLYING,COMMANDCENTERFLYING]
#       Some preconditions.
#       Each element is a unit, upgrade, or structure. First can not be produced without second. 
#       First is structure
        self.tech(BARRACKS,SUPPLYDEPOT)
        self.tech(BARRACKSTECHLAB,BARRACKS)
        self.tech(BARRACKSTECHLAB,REFINERY)
        self.tech(FACTORY,BARRACKS)
        self.tech(FACTORYTECHLAB,FACTORY)
        self.tech(FACTORYTECHLAB,REFINERY)
        self.tech(STARPORT,FACTORY)
        self.tech(STARPORTTECHLAB,STARPORT)
        self.tech(STARPORTTECHLAB,REFINERY)
        self.tech(PLANETARYFORTRESS,COMMANDCENTER)
        self.tech(PLANETARYFORTRESS,ENGINEERINGBAY)
        self.tech(PLANETARYFORTRESS,REFINERY)
        self.tech(MISSILETURRET,ENGINEERINGBAY)
        self.tech(FUSIONCORE,STARPORT)
        self.tech(ARMORY,FACTORY)
#       First is unit
        self.tech(BATTLECRUISER,STARPORTTECHLAB)
        self.tech(BATTLECRUISER,FUSIONCORE)
        self.tech(MARINE,BARRACKS)
        self.tech(SIEGETANK,FACTORYTECHLAB)
        self.tech(MARAUDER,BARRACKSTECHLAB)
        self.tech(RAVEN,STARPORTTECHLAB)
        self.tech(VIKINGFIGHTER,STARPORT)
#       First is upgrade
        self.tech(PUNISHERGRENADES,BARRACKSTECHLAB)
        self.tech(TERRANSHIPWEAPONSLEVEL1,ARMORY)
        self.tech(TERRANSHIPWEAPONSLEVEL2,ARMORY)
        self.tech(TERRANSHIPWEAPONSLEVEL3,ARMORY)
        self.tech(TERRANSHIPWEAPONSLEVEL2,TERRANSHIPWEAPONSLEVEL1)
        self.tech(TERRANSHIPWEAPONSLEVEL3,TERRANSHIPWEAPONSLEVEL2)
        self.tech(TERRANVEHICLEANDSHIPARMORSLEVEL1,ARMORY)
        self.tech(TERRANVEHICLEANDSHIPARMORSLEVEL2,ARMORY)
        self.tech(TERRANVEHICLEANDSHIPARMORSLEVEL3,ARMORY)
        self.tech(TERRANVEHICLEANDSHIPARMORSLEVEL2,TERRANVEHICLEANDSHIPARMORSLEVEL1)
        self.tech(TERRANVEHICLEANDSHIPARMORSLEVEL3,TERRANVEHICLEANDSHIPARMORSLEVEL2)
        self.tech(TERRANBUILDINGARMOR,ENGINEERINGBAY)
        self.tech(TERRANINFANTRYWEAPONSLEVEL1,ENGINEERINGBAY)
        self.tech(TERRANINFANTRYWEAPONSLEVEL2,ENGINEERINGBAY)
        self.tech(TERRANINFANTRYWEAPONSLEVEL3,ENGINEERINGBAY)
        self.tech(TERRANINFANTRYWEAPONSLEVEL2,TERRANINFANTRYWEAPONSLEVEL1)
        self.tech(TERRANINFANTRYWEAPONSLEVEL3,TERRANINFANTRYWEAPONSLEVEL2)
        self.compute_anything()
#       shipyard
        self.shipyard = self.start_location.position.towards(self.game_info.map_center,4)
        self.fix_count_of_job()
#       priority system
        await self.rush(BATTLECRUISER,2)
        await self.rush(MARINE,7)
        await self.rush(COMMANDCENTER,3)
        await self.rush(REFINERY,4)
#       use stored placement tips
        mapplace = 'map: '+self.game_info.map_name+' '+str(self.start_location.position.x)+' '+str(self.start_location.position.y)
        self.log_success(mapplace)
        pl = open('placement.txt','r')
        alltips = pl.read().splitlines()
        pl.close()
        self.tips = []
        cop = False
        for nr in range(0,len(alltips)):
            if alltips[nr] == mapplace:
                cop = True
            elif alltips[nr] == '#####':
                cop = False
            if cop:
                self.tips.append(alltips[nr])
#       feedback the tips
        for nr in range(0,len(self.tips)):
            ti = self.tips[nr]
            print(ti) 



#   logging
    def log_fail(self,bol,str):
        if not bol:
            print(f' On {self.itera} fail {self.routine} '+str) 

    def log_success(self,str):
        if self.do_log_success:
            print(f' On {self.itera} doing {self.routine} '+str) 

    def log_buildposition(self,building,place):
        if self.do_log_buildposition:
            x = round(place.x)
            y = round(place.y)
            print(f' On {self.itera} buildposition '+building.name+' '+str(x)+' '+str(y))

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
                        print('gasminer without assignment '+str(scvt)) 
            for scvt in self.gast_of_scvt:
                if scvt not in self.all_scvt:
                    print('assignment but not existing?! scv '+str(scvt))
                if scvt not in self.job_of_scvt:
                    print('assignment but scv without job?! '+str(scvt))
                if scvt in self.job_of_scvt:
                    job = self.job_of_scvt[scvt]
                    if job != 'gasminer':
                        print(job+' with gasminer assignment '+str(scvt))

    def log_population(self):
        if self.do_log_population:
            lin = ''
            for jo in self.count_of_job:
                co = self.count_of_job[jo]
                lin = lin + jo[0]+jo[1]+jo[2]+' '+str(co)+'   '
            print(f' On {self.itera} population: '+lin)

    def log_limbo(self,str):
        if self.do_log_limbo:
            print(f' On {self.itera} limbo: '+str) 

    def log_wish(self,str):
        if self.do_log_wish:
            if str != self.log_wish_history:
                self.log_wish_history = str
                print(f' On {self.itera} wish: '+str) 

    def log_resource(self):
        if self.do_log_resource:
            print(f' On {self.itera} minerals '+str(self.minerals)+'   gas '+str(self.vespene)\
            +'   reserved '+str(self.reserved_minerals)+'   reserved gas '+str(self.reserved_vespene))





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
    def most_struct(self,barra):
        self.routine = 'most_struct'
        self.log_fail((type(barra) == UnitTypeId),'')
        self.all_structures.append(barra)

    def tech(self,facto,barra):
        self.routine = 'tech'
        self.log_fail((type(facto) in [UpgradeId,UnitTypeId]),'first arg')
        self.log_fail((type(barra) in [UpgradeId,UnitTypeId]),'second arg')
        self.techtree.append( (facto,barra) )

    def check_techtree(self,facto) -> bool:
        cando = True
        for pair in self.techtree:
            if pair[0] == facto:
                cando = cando and self.we_have_a(pair[1])
        return cando

    def compute_anything(self):
        self.anything = []
        for pair in self.techtree:
            something = pair[0]
            if something not in self.anything:
                self.anything.append(something)
            something = pair[1]
            if something not in self.anything:
                self.anything.append(something)
        
    def we_have_a(self,barra) -> bool:
        if type(barra) == UpgradeId:
            have = (self.already_pending_upgrade(barra) > 0.99)
        if type(barra) == UnitTypeId:
#           a structure or a unit
            if barra in self.all_structures:
                have = (len(self.structures(barra).ready) > 0)
            else:
                have = (len(self.units(barra).ready) > 0)
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
            if barra in self.all_structures:
                have = len(self.structures(barra))
            else:
                have = len(self.units(barra))
        return have



#   money handling with reservations
    def can_pay(self,thing,urgent) -> bool:
        if urgent:
            cost = self.calculate_cost(thing)
            return (self.minerals >= cost.minerals) and (self.vespene >= cost.vespene)
        else:
            cost = self.calculate_cost(thing)
            return (self.minerals >= self.reserved_minerals+cost.minerals) and (self.vespene >= self.reserved_vespene+cost.vespene)



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


    def miner_vacatures(self) -> bool:
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
#                   accept idler if 1.4 times as far
                    if self.job_of_scvt[scvt] == 'idler':
                        sd = sd/2
                    if sd < best_sdist:
                        best_sdist = sd
                        best_scvt = scvt
        scvt = best_scvt
        return scvt        

    def get_near_scvt_idler(self,point) -> int:
#       suggestion: call    if self.count_of_job('idler') > 0;
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
        self.log_fail(self.job_of_scvt[scvt] == 'idler','HEU1')
        return scvt        

    def get_near_gast_free(self,point) -> int:
#       supposes done:   fix_count_of_gast
#       suggestion: call   if self.gasminer_vacatures() > 0:
        best_sdist = 80000
        best_gast = None
        for gas in self.structures(REFINERY).ready:
            gast = gas.tag
            if gast in self.all_gast:
                if self.count_of_gast[gast] < 3:
                    sd = self.sdist(gas.position,point)
                    if sd < best_sdist:
                        best_sdist = sd
                        best_gast = gast
        gast = best_gast
        self.log_fail(gast in self.all_gast,'HEU2')
        return gast        

    def get_near_mimt_free(self,point) -> int:
#       supposes done:   fix_count_of_mimt
#       suggestion: call   if self.miner_vacatures() > 0:
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
        self.log_fail(mimt in self.all_mimt,'HEU3')
        return mimt        



    async def gamestate_validate(self):
        self.routine = 'gamestate_validate'
#       
#   in the jump lost battlecruisers
        count = 0
        for bc in self.units(BATTLECRUISER).ready:
            if (bc.tag in self.inrepair):
                count = count+1
        if len(self.inrepair) > count:
            self.fear = min(500,self.fear+40)
#   inrepair contains tags of living, unhealthy battlecruisers
        new_inrepair = []
        for bc in self.units(BATTLECRUISER).ready:
            if (bc.tag in self.inrepair) and (bc.health<525):
                new_inrepair.append(bc.tag)
        self.inrepair = new_inrepair
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
#   ambition_pf contains tags of living commandcenters
        new_ambition_pf = []
        for cc in self.structures(COMMANDCENTER).ready:
            if cc.tag in self.ambition_pf:
                new_ambition_pf.append(cc.tag)
        self.ambition_pf = new_ambition_pf
#       
#   rushing depends on endwish
#       only once per game toggle to True
        if self.rushing:
            rr = True
            for thing in self.endwish:
                rr = rr and (self.we_started_amount(thing) >= self.endwish[thing])
            if rr: 
                self.rushing = False
                self.log_success('rush reached!')
#   
#   wish_now is the reachable part of wish
            self.wish_now = []
            lin = ''
            for thing in self.wish:
                if self.check_techtree(thing):
                    if self.we_started_amount(thing) < self.wish[thing]:
                        self.wish_now.append(thing)
                        lin = lin+' '+thing.name
                
            if len(self.wish_now)>0:
                self.log_wish(lin)
#    
#   save money to the cost of all wish_now
            self.reserved_minerals = 0
            self.reserved_vespene = 0
            for thing in self.wish_now:
                cost = self.calculate_cost(thing)
                self.reserved_minerals = self.reserved_minerals + cost.minerals
                self.reserved_vespene = self.reserved_vespene + cost.vespene
#   
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
#                       self.log_limbo('a '+job+' in limbo '+str(scvt))
                        new_all_scvt.append(scvt)
                        if scvt in self.itera_of_missing_scvt:
                            time_lost = self.itera - self.itera_of_missing_scvt[scvt]
                        else:
                            time_lost = 0
                            self.itera_of_missing_scvt[scvt] = self.itera
                        if time_lost < 20:
                            new_all_scvt.append(scvt)
                        else:
                            self.log_limbo('give up hope '+str(scvt))
                if (job == 'builder'):
                    if (self.structure_of_scvt[scvt] == REFINERY):
                        if scvt not in new_all_scvt:
#                           self.log_limbo('DEBUG a '+job+' in limbo '+str(scvt))
                            new_all_scvt.append(scvt)
                            if scvt in self.itera_of_missing_scvt:
                                time_lost = self.itera - self.itera_of_missing_scvt[scvt]
                            else:
                                time_lost = 0
                                self.itera_of_missing_scvt[scvt] = self.itera
                            if time_lost < 20:
                                new_all_scvt.append(scvt)
                            else:
                                self.log_limbo('give up hope '+str(scvt))
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
#   The tag of existing refineries where we want to mine from, in this iteration
        self.all_gast = []
        for gas in self.structures(REFINERY).ready:
            gast = gas.tag
            if gas.vespene_contents > 0:
#               for tow in self.townhalls.ready:   does not work when going from cc to pf
                for tow in self.townhalls:
                    if tow.build_progress > 0.75:
                        towt = tow.tag
                        if not tow.is_flying:
                            if self.near(gas.position,tow.position,10):
                                self.all_gast.append(gast)
#   The tag of existing minerals where we want to mine from, in this iteration
        self.all_mimt = []
        for mim in self.mineral_field:
            mimt = mim.tag
            if mim.mineral_contents > 0:
#               for tow in self.townhalls.ready:   does not work when going from cc to pf
                for tow in self.townhalls:
                    if tow.build_progress > 0.75:
                        towt = tow.tag
                        if not tow.is_flying:
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
#   goal_of_scvt contains the tag of living traveller scvs
        new_goal_of_scvt = {}
        for scvt in self.all_scvt:
            if self.job_of_scvt[scvt] == 'traveller':
                new_goal_of_scvt[scvt] = self.goal_of_scvt[scvt]
        self.goal_of_scvt = new_goal_of_scvt
#   structure_of_scvt contains the tag of living builders and travellers
        new_structure_of_scvt = {}
        for scvt in self.all_scvt:
            if self.job_of_scvt[scvt] in ('builder','traveller'):
                new_structure_of_scvt[scvt] = self.structure_of_scvt[scvt]
        self.structure_of_scvt = new_structure_of_scvt



#   actions
    async def build_worker(self,amount):
        self.routine = 'build_worker'
        todo = amount - (self.units(SCV).amount + self.already_pending(SCV))
        todo = min(todo,self.supply_left)
        if self.count_of_job['idler'] < 11:
            for cc in self.townhalls.ready:
                if (cc.is_idle) and (cc.tag not in self.ambition_pf):
#                   always urgent
                    if self.can_pay(SCV,True):
                        if todo > 0:
                            todo = todo-1
                            self.log_success('')
                            cc.train(SCV)



    async def build_army(self,ship,hangar,amount,urgent):
        self.routine = 'build_army'
        todo = amount - (self.units(ship).ready.amount + self.already_pending(ship))
        if ship == SIEGETANK:
            todo = todo - self.units(SIEGETANKSIEGED).ready.amount
        todo = min(todo,(self.supply_left//6))
        if self.check_techtree(ship):
            for sp in self.structures(hangar).ready:
                if sp.is_idle:
                    if self.can_pay(ship,urgent):
                        if todo>0:
                            todo = todo-1
                            self.log_success(ship.name)
                            sp.train(ship)



    async def build_building(self,building,amount,urgent):
        self.routine = 'build_building'
        todo = amount - (self.structures(building).ready.amount + self.already_pending(building))
        if building == SUPPLYDEPOT:
            todo = todo - self.structures(SUPPLYDEPOTLOWERED).ready.amount
        if todo > 0:
            if self.check_techtree(building):
                if self.can_pay(building,urgent):
#                   get a random place
                    if len(self.townhalls.ready) > 0:
                        cc = self.townhalls.ready.random
                        dist = 12
                        if building == STARPORT:
                            dist = 6
                        if building == MISSILETURRET:
                            dist = random.randrange(-10,10) 
                        fixplace = cc.position.towards(self.game_info.map_center, dist)
                        place = await self.find_placement(building,fixplace,20,True,2)
                    else:
                        place = await self.find_placement(building,self.start_location.position,20,True,2)
#                   get place from tips
                    found = False
                    for nr in range(0,len(self.tips)):
                        if (nr not in self.tips_used) and (not found):
                            ti = self.tips[nr]
                            woord = ti.split()
                            if woord[0] == 'position':
                                if woord[1] == building.name:
                                    place = Point2((float(woord[2]),float(woord[3]))) 
                                    self.tips_used.append(nr)
                                    self.log_success('using a placement tip');
                                    found = True 
#                   dismantling Burny bot_ai build
#                   the suggested self.do is said to be outdated
                    scvt = self.get_near_scvt_to_goodjob(place)
                    for scv in self.units(SCV):
                        if scv.tag == scvt:
#                           best to stop the scv from mining, for if the build does not start, it remains in old function
                            if scv.is_collecting:
                               scv(STOP)
                            self.job_of_scvt[scvt] = 'builder'
                            self.promotionsite_of_scvt[scvt] = scv.position
                            self.structure_of_scvt[scvt] = building
                            self.log_success('planning '+building.name+' '+str(scvt))
                            if scv.build(building,place):
                                self.log_success('ordered  '+building.name+' '+str(scvt))
                            self.log_buildposition(building,place)



    async def build_refinery(self,amount,urgent):
        self.routine = 'build_refinery'
        todo = amount - (self.structures(REFINERY).amount + self.already_pending(REFINERY))
        for cc in self.townhalls.ready:
            vgs: Units = self.vespene_geyser.closer_than(20, cc)
            for vg in vgs:
                if not self.gas_buildings.closer_than(1, vg):
                    if self.can_pay(REFINERY,urgent):
                        if todo>0:
                            todo = todo-1
#                           dismantling Burny bot_ai build
                            place = vg.position
                            scvt = self.get_near_scvt_to_goodjob(place)
                            for scv in self.units(SCV):
                                if scv.tag == scvt:
                                    self.job_of_scvt[scvt] = 'builder'
                                    self.promotionsite_of_scvt[scvt] = scv.position
                                    self.structure_of_scvt[scvt] = REFINERY
                                    self.log_success('planning '+str(scvt))
                                    if scv.build_gas(vg):
                                        self.log_success('ordered  '+str(scvt))



    async def build_commandcenter(self,amount,urgent):
        self.routine = 'build_commandcenter'
        if self.can_pay(COMMANDCENTER,urgent):
            for scvt in self.goal_of_scvt:
#               only a traveller has a goal
                goal = self.goal_of_scvt[scvt]
                for scv in self.units(SCV):
                    if scv.tag == scvt:
                        if self.near(scv.position,goal,3):
                            self.job_of_scvt[scvt] = 'builder'
                            self.promotionsite_of_scvt[scvt] = scv.position
                            self.log_success('traveller became builder '+str(scvt))
                            self.log_success('planning '+str(scvt))
                            if scv.build(COMMANDCENTER, goal):
                                self.log_success('ordering  '+str(scvt))
#                           the scvt keeps its structure_of_scvt
        todo = amount - (self.townhalls.ready.amount + self.already_pending(COMMANDCENTER) + self.already_pending(PLANETARYFORTRESS))
        plans = len(self.goal_of_scvt)
        if todo>plans:
            if self.minerals > 250*plans+250: 
#               add 1 ccplan
                goal = random.choice(self.expansion_locations_list)
                if (not self.near(goal,self.enemy_start_locations[0].position,50)) \
                and (goal not in [tow.position for tow in self.townhalls]) \
                and (goal not in [self.goal_of_scvt[scvt] for scvt in self.goal_of_scvt]):
                    scvt = self.get_near_scvt_to_goodjob(goal)
                    for scv in self.units(SCV):
                        if scv.tag == scvt:
                            job = self.job_of_scvt[scvt]
                            self.job_of_scvt[scvt] = 'escorter'
                            self.promotionsite_of_scvt[scvt] = scv.position
                            self.log_success(job+' became escorter '+str(scvt))
                            scv.attack(goal)
                    if len(self.units(MARINE).ready) > 0:
                        mar = random.choice(self.units(MARINE).ready)
                        mar.attack(goal)
                    if len(self.units(MARAUDER).ready) > 0:
                        mar = random.choice(self.units(MARAUDER).ready)
                        mar.attack(goal)
                    scvt = self.get_near_scvt_to_goodjob(goal)
                    self.goal_of_scvt[scvt] = goal
                    self.structure_of_scvt[scvt] = COMMANDCENTER
                    for scv in self.units(SCV):
                        if scv.tag == scvt:
                            job = self.job_of_scvt[scvt]
                            self.job_of_scvt[scvt] = 'traveller'
                            self.promotionsite_of_scvt[scvt] = scv.position
                            self.log_success(job+' became traveller '+str(scvt))
                            scv(MOVE_MOVE, goal)



    async def build_techlab(self, thing, onthing, urgent):
        self.routine = 'build_techlab'
        for ba in self.structures(onthing).ready.idle:
            if not ba.has_add_on:
                if ba.tag not in self.no_lab:
                    if self.can_pay(thing,urgent):
                        self.log_success('on '+onthing.name)
                        ba.build(thing)
                        self.no_lab.append(ba.tag)
 


    async def attack(self):
        self.routine = 'attack'
        if self.attack_phase == 'harrass':
            tp = self.mineral_field.random.position
        elif self.attack_phase == 'gather':
            tp = self.game_info.map_center
        elif self.attack_phase == 'coordinated':
            tp = self.enemy_start_locations[0].position
        sent = 0
        for srt in [BATTLECRUISER,MARINE,MARAUDER,VIKINGFIGHTER]:
            for ar in self.units(srt).ready.idle:
                if not (ar.tag in self.inrepair):
                    if (self.attack_phase == 'gather') and (self.near(ar.position,self.game_info.map_center,10)):
                        pass
                    else:
                        sent = sent + 1
                        ar.attack(tp)
        if sent > 0:
            self.log_success(' with '+str(sent))
#       
#       attack_phase changes
        if self.attack_phase == 'harrass':
            if not self.tried_coordinated_attack:
                if self.supply_used > 190:
                    self.attack_phase = 'gather'
                    self.log_success('gathering the army for a coordinated attack')
        elif self.attack_phase == 'gather':
            reached = 0
            total = 0
            for srt in [BATTLECRUISER,MARINE,MARAUDER,VIKINGFIGHTER]:
                for ar in self.units(srt).ready:
                    total = total+1
                    if self.near(ar.position,self.game_info.map_center,10):
                        if ar in self.units(srt).ready.idle:
                            reached = reached+1
            if reached*5 > total*4:
                self.attack_phase = 'coordinated'
                self.log_success('starting a coordinated attack')
        elif self.attack_phase == 'coordinated':
            self.attack_phase = 'harrass'
            self.tried_coordinated_attack = True
#       
#       ravens should attack the best battlecruiser
        for rv in self.units(RAVEN).ready.idle:
            for bc in self.units(BATTLECRUISER).ready:
                if bc.tag == self.bestbctag:
                    rv.attack(bc)
                    self.log_success('raven will follow a bc')
#       fighter scvs
        if self.count_of_job['fighter'] > 0:
            for scv in self.units(SCV).idle:
                scvt = scv.tag
                if scvt in self.all_scvt:
                    if self.job_of_scvt[scvt] == 'fighter':
                        place = self.mineral_field.random.position
                        scv.attack(place)



    async def to_pf(self,urgent):
        self.routine = 'to_pf'
        if self.check_techtree(PLANETARYFORTRESS):
            for cc in self.structures(COMMANDCENTER).ready:
                if cc.tag not in self.ambition_pf: 
                    self.ambition_pf.append(cc.tag)
            todo = 1
            if self.can_pay(PLANETARYFORTRESS,urgent):
                for cc in self.structures(COMMANDCENTER).ready:
                    if cc.tag in self.ambition_pf: 
                        if cc.is_idle:
                            if todo > 0:
                                todo = todo-1
                                self.log_success('')
                                cc.train(PLANETARYFORTRESS)



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
                to_raise = False
                for ene in self.enemy_units:
                    if self.near(ene.position,sd.position,5):
                        to_raise = True
                if to_raise:
                    sd(MORPH_SUPPLYDEPOT_RAISE)
                    self.log_success('raising')
        for sd in self.structures(SUPPLYDEPOT).ready:
            if sd.tag == self.updown:
                to_lower = True
                for ene in self.enemy_units:
                    if self.near(ene.position,sd.position,5):
                        to_lower = False
                if to_lower:
                    sd(MORPH_SUPPLYDEPOT_LOWER)
                    self.log_success('lowering')



    async def siege_tank(self):
#       siege tank at a random own base
        for tnk in self.units(SIEGETANK).ready.idle:
            tnkt = tnk.tag
            if tnkt in self.towt_of_tnkt:
                towt = self.towt_of_tnkt[tnkt]
                for tow in self.townhalls.ready:
                    if tow.tag == towt:
                        if self.near(tnk.position,tow.position,10):
                            tnk(SIEGEMODE_SIEGEMODE)
                        else:
                            tnk.attack(tow.position)
            else:
                if self.townhalls.ready.amount == 0:
                    tnk(SIEGEMODE_SIEGEMODE)
                else:
                    tow = self.townhalls.ready.random
                    towt = tow.tag
                    self.towt_of_tnkt[tnkt] = towt
                    tnk.attack(tow.position)



    async def do_upgrades(self):
        self.routine = 'do_upgrades'
        todo = 1
#       bug on TERRANVEHICLEANDSHIPARMORSLEVEL1,TERRANVEHICLEANDSHIPARMORSLEVEL2,TERRANVEHICLEANDSHIPARMORSLEVEL3
        upg = random.choice([TERRANSHIPWEAPONSLEVEL1,TERRANSHIPWEAPONSLEVEL2,TERRANSHIPWEAPONSLEVEL3])
        self.log_fail((type(upg) == UpgradeId),'BOE')
        if self.already_pending_upgrade(upg) == 0:
            if self.check_techtree(upg):
                for ar in self.structures(ARMORY).ready.idle:
                    if self.can_pay(upg,False):
                        if todo>0:
                            todo = todo-1
                            self.log_success(upg.name)
                            ar.research(upg)
        todo = 1
        upg = random.choice([TERRANBUILDINGARMOR,TERRANINFANTRYWEAPONSLEVEL1,\
        TERRANINFANTRYWEAPONSLEVEL2,TERRANINFANTRYWEAPONSLEVEL3])
        self.log_fail((type(upg) == UpgradeId),'BOE')
        if self.already_pending_upgrade(upg) == 0:
            if self.check_techtree(upg):
                for eb in self.structures(ENGINEERINGBAY).ready.idle:
                    if self.can_pay(upg,False):
                        if todo>0:
                            todo = todo-1
                            self.log_success(upg.name)
                            eb.research(upg)
        todo = 1
#       bug on COMBATSHIELD
        upg = random.choice([PUNISHERGRENADES])
        self.log_fail((type(upg) == UpgradeId),'BOE')
        if self.already_pending_upgrade(upg) == 0:
            if self.check_techtree(upg):
                for tl in self.structures(BARRACKSTECHLAB).ready.idle:
                    if self.can_pay(upg,False):
                        if todo>0:
                            todo = todo-1
                            self.log_success(upg.name)
                            tl.research(upg)
#       Patch over bug in Burny/Starcraft code:
        for ar in self.structures(ARMORY).ready.idle:
            ar(AbilityId.ARMORYRESEARCH_TERRANVEHICLEANDSHIPPLATINGLEVEL1)
            ar(AbilityId.ARMORYRESEARCH_TERRANVEHICLEANDSHIPPLATINGLEVEL2)
            ar(AbilityId.ARMORYRESEARCH_TERRANVEHICLEANDSHIPPLATINGLEVEL3)



    async def battle_jump_home(self):
        self.routine = 'battle_jump_home'
        for bc in self.units(BATTLECRUISER).ready:
            if (bc.health <= self.fear) and (bc.tag not in self.inrepair):
#               jump bc home for repair
                self.log_success('')
                bc(EFFECT_TACTICALJUMP,self.shipyard)
                self.inrepair.append(bc.tag)
                self.fear = max(150,self.fear-10)



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
                            self.log_success('finished '+str(scvt))
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
                            self.log_success(' '+s.name+' '+str(scvt))
                            scv.repair(s)
                            self.busy_arearepairer.append(scvt)
                        elif scv.is_idle:
                            if self.near(scv.position,self.cottage_of_scvt[scvt],5):
#                               dream or mine unadministrated
                                self.fix_count_of_mimt()
                                if self.miner_vacatures() > 0:
                                    mimt = self.get_near_mimt_free(scv.position)
                                    for mim in self.mineral_field:
                                        if mim.tag == mimt:
                                            if self.near(mim.position,scv.position,12):
                                                scv.gather(mim)
                                                self.log_success('arearepairer bored '+str(scvt))
                            else:
                                self.log_success('going home '+str(scvt))
                                scv(MOVE_MOVE,self.cottage_of_scvt[scvt])



    async def manage_workers(self):
        self.routine = 'manage_workers'
#       
#       jobhaters 
        for scv in self.units(SCV).idle:
            scvt = scv.tag
            if scvt in self.all_scvt:
                job = self.job_of_scvt[scvt]
                if job in ('gasminer','miner','escorter','builder'):
                    if scv.position != self.promotionsite_of_scvt[scvt]:
                        self.log_success('fired slacking '+job+' '+str(scvt))
                        self.job_of_scvt[scvt] = 'idler'
#       builders start to mine after building a geyser
        for scv in self.units(SCV):
            scvt = scv.tag
            if scvt in self.all_scvt:
                job = self.job_of_scvt[scvt]
                if job == 'builder':
                    if scv.is_collecting:
                        if self.gasminer_vacatures() > 0:
                            if scv.position != self.promotionsite_of_scvt[scvt]:
                                self.log_success('jobswich mining builder '+str(scvt))
                                self.job_of_scvt[scvt] = 'gasminer'
                                gast = self.get_near_gast_free(scv.position)
                                self.gast_of_scvt[scvt] = gast
                                self.count_of_gast[gast] = self.count_of_gast[gast]+1
#       
        self.fix_count_of_job()
#
#       arearepairers
        wishr = min(len(self.all_scvt)//6,self.townhalls.ready.amount)
        if self.count_of_job['arearepairer'] > wishr:
#           get one that is far from each townhall
            best_dist = 0
            best_scvt = None
            for scv in self.units(SCV).ready:
                scvt = scv.tag
                if scvt in self.all_scvt:
                    if self.job_of_scvt[scvt] == 'arearepairer':
                        clos_dist = 80000
                        for tow in self.townhalls.ready:
                            sd = self.sdist(self.cottage_of_scvt[scvt],tow.position)
                            clos_dist = min(clos_dist,sd)
                        if clos_dist > best_dist:
                            best_dist = clos_dist
                            best_scvt = scvt
            scvt = best_scvt
            self.log_success('fired arearepairer '+str(scvt))
            self.job_of_scvt[scvt] = 'idler'
            scv(STOP)
        if self.count_of_job['arearepairer'] < wishr:
#           get a townhall that is far from each cottage
            worst_towpos = None
            worst_dist = 0
            for tow in self.townhalls.ready:
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
                    self.log_success('promoted '+job+' to arearepairer '+str(scvt))
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
                    self.log_success('promoted '+job+' to shiprepairer '+str(scvt))
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
                        self.log_success('fired shiprepairer '+str(scvt))
                        self.job_of_scvt[scvt] = 'idler'
#       whip them
        for scv in self.units(SCV).idle:
            scvt = scv.tag
            if scvt in self.all_scvt:
                if (self.job_of_scvt[scvt] == 'shiprepairer'):
                    if not self.near(scv.position,self.shipyard,15):
                        scv(MOVE_MOVE,self.shipyard)
                    elif len(self.inrepair) > 0:
                        for bc in self.units(BATTLECRUISER).ready:
                            bct = bc.tag
                            if bct == self.inrepair[0]:
                                scv.repair(bc)
#       keep the bc in the shipyard
        if len(self.inrepair) > 0:
            for bc in self.units(BATTLECRUISER).ready:
                bct = bc.tag
                if bct == self.inrepair[0]:
                     if self.near(bc.position,self.shipyard,15) and not self.near(bc.position,self.shipyard,5):
                         bc(MOVE_MOVE,self.shipyard)



    async def manage_gas(self):
        self.routine = 'manage_gas'
        self.log_gasminer()
        self.fix_count_of_job()
        for scvt in self.all_scvt:
            if self.job_of_scvt[scvt] == 'gasminer':
                if scvt not in self.gast_of_scvt:
                    self.log_success('gasminer retired '+str(scvt))
                    self.job_of_scvt[scvt] = 'idler'
        vacatures = self.gasminer_vacatures()
        if vacatures > 0:
#           new gas-mineral connections
            if vacatures < self.count_of_job['idler']:
                for gas in self.structures(REFINERY).ready:
                    gast = gas.tag
                    if gast in self.all_gast:
                        if self.count_of_gast[gast] < 3:
                            scvt = self.get_near_scvt_idler(gas.position)
                            for scv in self.units(SCV):
                                if scv.tag == scvt:
                                    self.job_of_scvt[scvt] = 'gasminer'
                                    self.promotionsite_of_scvt[scvt] = scv.position
                                    scv.gather(gas)
                                    self.log_success('new gasminer group '+str(scvt))
                                    self.gast_of_scvt[scvt] = gast
                                    self.count_of_gast[gast] = self.count_of_gast[gast]+1
            else:
                for scv in self.units(SCV):
                    scvt = scv.tag
                    if self.job_of_scvt[scvt] == 'idler':
                        gast = self.get_near_gast_free(scv.position)
                        for gas in self.structures(REFINERY).ready:
                            if gas.tag == gast:
                                self.job_of_scvt[scvt] = 'gasminer'
                                self.promotionsite_of_scvt[scvt] = scv.position
                                scv.gather(gas)
                                self.log_success('new gasminer '+str(scvt))
                                self.gast_of_scvt[scvt] = gast
                                self.count_of_gast[gast] = self.count_of_gast[gast]+1
        self.log_gasminer()



    async def manage_minerals(self):
        self.routine = 'manage_minerals'
        self.fix_count_of_job()
        for scvt in self.all_scvt:
            if self.job_of_scvt[scvt] == 'miner':
                if scvt not in self.mimt_of_scvt:
                    self.log_success('miner retired '+str(scvt))
                    self.job_of_scvt[scvt] = 'idler'
        vacatures = self.miner_vacatures()
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
                                    self.job_of_scvt[scvt] = 'miner'
                                    self.promotionsite_of_scvt[scvt] = scv.position
                                    scv.gather(mim)
                                    self.log_success('new miner group '+str(scvt))
                                    self.mimt_of_scvt[scvt] = mimt
                                    self.count_of_mimt[mimt] = self.count_of_mimt[mimt]+1
            else:
                for scv in self.units(SCV):
                    scvt = scv.tag
                    if self.job_of_scvt[scvt] == 'idler':
                        mimt = self.get_near_mimt_free(scv.position)
                        for mim in self.mineral_field:
                            if mim.tag == mimt:
                                self.job_of_scvt[scvt] = 'miner'
                                self.promotionsite_of_scvt[scvt] = scv.position
                                scv.gather(mim)
                                self.log_success('new miner '+str(scvt))
                                self.mimt_of_scvt[scvt] = mimt
                                self.count_of_mimt[mimt] = self.count_of_mimt[mimt]+1



    async def manage_rest(self):
        self.routine = 'manage_rest'
        self.fix_count_of_job()
#       
#       max idle workers
        todo = self.count_of_job['idler'] - 22
        for scv in self.units(SCV):
            scvt = scv.tag
            if scvt in self.all_scvt:
                if self.job_of_scvt[scvt] == 'idler':
                    if todo > 0:
                        todo = todo-1
                        self.log_success('suiciding idler '+str(scvt))
                        self.job_of_scvt[scvt] = 'fighter'
                        self.promotionsite_of_scvt[scvt] = scv.position
                        scv.attack(self.enemy_start_locations[0].position)
#       job-swap for late game
        if (self.count_of_job['idler'] == 0) and (self.itera % 9 == 0):
            if self.minerals > self.vespene + 1000:
                todo = 1
                for scvt in self.all_scvt:
                    if (self.job_of_scvt[scvt] == 'miner'):
                        if todo > 0:
                            todo = todo-1
                            self.log_success('floating minerals fire '+str(scvt))
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
                            self.log_success('floating gas fire '+str(scvt))
                            self.job_of_scvt[scvt] = 'idler'
                            for scv in self.units(SCV):
                                if scvt == scv.tag:
                                    scv(STOP) 
            


#   rush
    async def rush(self,thing,amount):
        self.routine = 'rush'
        self.endwish[thing] = amount
        if thing in self.wish:
            self.wish[thing] = max(self.wish[thing],amount)
        else:
            self.wish[thing] = amount
        self.log_wish('wishing '+thing.name+' '+str(amount))
        stable = False
        while not stable:
            stable = True
#           to change a dict while using it:
#           method 1:   old_wish = self.wish.copy()
#           method 2:   walk and merge
            morewish = {}
            for th in self.wish:
                for pair in self.techtree:
                    if pair[0] == th:
                        if pair[1] not in self.wish:
                            morewish[pair[1]] = 1
                            stable = False
            for th in morewish:
                self.wish[th] = morewish[th]
        for th in self.wish:
            self.log_wish('so wishing '+th.name+' '+str(self.wish[th]))
         

            
#   Build specific unit or structure
    async def build_thing(self,thing,urgent):
        bases = self.townhalls.ready.amount
        battlecruisers = self.units(BATTLECRUISER).ready.amount
        later = min(2,battlecruisers+1)
        if thing == ENGINEERINGBAY:
            await self.build_building(ENGINEERINGBAY,later,urgent)
        if thing == BARRACKS:
            await self.build_building(BARRACKS,later,urgent)
        if thing == FACTORY:
            await self.build_building(FACTORY,later,urgent)
        if thing == FUSIONCORE:
            await self.build_building(FUSIONCORE,later,urgent)
        if thing == ARMORY:
            await self.build_building(ARMORY,min(2,battlecruisers),urgent)
        if thing == RAVEN:
            await self.build_army(RAVEN,STARPORT,min(1,battlecruisers-1),urgent)
        if thing == VIKINGFIGHTER:
            await self.build_army(VIKINGFIGHTER,STARPORT,1,urgent)
        if thing == PLANETARYFORTRESS:
            await self.to_pf(urgent)
        if thing == REFINERY:
            await self.build_refinery(2*bases,urgent)
        if thing == SUPPLYDEPOT:
            await self.build_building(SUPPLYDEPOT,3*bases-1,urgent)
        if thing == MISSILETURRET:
            await self.build_building(MISSILETURRET,3*bases-2,urgent)
        if thing == COMMANDCENTER:
            await self.build_commandcenter(5+(self.minerals-500)//500,urgent)
        if thing == MARINE:
            await self.build_army(MARINE,BARRACKS,10-battlecruisers,urgent)
        if thing == MARAUDER:
            await self.build_army(MARAUDER,BARRACKS,5-battlecruisers,urgent)
        if thing == SIEGETANK:
            await self.build_army(SIEGETANK,FACTORY,bases//2,urgent)
        if thing == BATTLECRUISER:
            await self.build_army(BATTLECRUISER,STARPORT,32,urgent)
        if thing == STARPORT:
            await self.build_building(STARPORT,bases,urgent)
        if thing == BARRACKSTECHLAB:
            await self.build_techlab(thing,BARRACKS,urgent)
        if thing == FACTORYTECHLAB:
            await self.build_techlab(thing,FACTORY,urgent)
        if thing == STARPORTTECHLAB:
            await self.build_techlab(thing,STARPORT,urgent)

#       Easy/Medium/Hard/VeryHard
run_game(maps.get('ThunderbirdLE'), [
    Bot(Race.Terran, Chaosbot()),
    Computer(Race.Terran, Difficulty.VeryHard)
    ], realtime=True)
