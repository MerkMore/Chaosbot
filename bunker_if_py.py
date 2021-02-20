# bunker_if_py.py
# author: MerkMore
# version: 19 feb 2021
# Burny style
#
# use:   from bunker_if_py import bunker_if
#
from typing import List,Set,Dict
#
import sc2
from sc2.ids.ability_id import AbilityId
from sc2.ids.unit_typeid import UnitTypeId
from sc2.ids.upgrade_id import UpgradeId
from sc2.position import Point2
# from sc2.constants import *
from sc2.ids.unit_typeid import SCV
from sc2.ids.unit_typeid import MARINE
from sc2.ids.unit_typeid import BUNKER


class bunker_if:
    #
    # SHARED
    #   do in the begin of on_step:
    #   bunker_if.init_step(self)
    units = None
    structures = None
    get_available_abilities = None
    #
    # EXTERNAL
    #   to be maintained by the wishes of the user
    #   dead things will disappear from these sets.
    hiding_spot = None
    bunkertags = set()
    door = {}
    scvtags = set()
    marinetags = set()
    do_log = False
    #
    # INTERNAL
    #   do not use outside this interface
    notag = -1
    bunkertags_inited = set()
    marinetags_inited = set()
    scvtags_inited = set()
    visible_marinetags = set()
    bunk_ammar = {}
    goalbunkertag = {}
    loadpast = {}
    astate = {}

    def log(stri):
        if bunker_if.do_log:
            print('bunker_if: '+stri)

    def init_step(self):
        bunker_if.units = self.units
        bunker_if.structures = self.structures
        bunker_if.get_available_abilities = self.get_available_abilities

    def step():
        # Distribute marines over the bunkers.
        # to be called on_step
        #
        # EXTERNAL:
        # bunkertags: some bunkers, ready or being built
        # door: a spot outside a bunker
        # scvtags: some scv job cheeser, to do cold repair.
        # marinetags: some marines.
        # hiding_spot: gathering place for superfluous marines and scvs
        # do_log: boolean controlling print
        #
        # INTERNAL
        # scvtags_inited: the scvtags in scvtags that did init
        # bunkertags_inited: the bunkertags in bunkertags that did init
        # marinetags_inited: the marinetags in marinetags that did init
        # visible_marinetags: marinetags outside bunkers
        # bunk_ammar[bu.tag]: ideal amount of marines in bunker bu
        # goalbunkertag[man.tag]: for bunk_marine man the bunker it belongs to.
        #                      for scvtags man the bunker it will repair
        #     assumed is that a bunk_marine man inside a bunker has that correct bunker in goalbunkertag
        # loadpast[man.tag]: for bunk_marine man, how long ago it got a load command (max load_frames)
        # astate[man.tag]: for marinetags and scvtags a state indication
        #                  astate 'working'       has goalbunkertag, is repairing or entering or in his bunker
        #                  astate 'walking'       has goalbunkertag, is moving or waiting until bunker ready
        #                  astate 'returning'     no goalbunkertag, is moving to hiding_spot
        #                  astate 'resting'       no goalbunkertag.
        #
        load_frames = 20
        load_dist = 6
        # old_goalbunkertag
        # store old version of goalbunkertag, so goalbunkertag can be corrected without other code in that part
        old_goalbunkertag = bunker_if.goalbunkertag.copy()
        # lost scvtags
        lost = set()
        for mant in bunker_if.scvtags:
            if mant not in (scv.tag for scv in bunker_if.units(SCV)):
                lost.add(mant)
        bunker_if.scvtags -= lost
        # lost marines
        lost = set()
        for mant in bunker_if.visible_marinetags: # history
            if (bunker_if.loadpast[mant] == load_frames) and (mant not in (mar.tag for mar in bunker_if.units(MARINE))):
                lost.add(mant)
        bunker_if.marinetags -= lost
        # recalc visible_marinetags, they ar invisible inside a bunker
        bunker_if.visible_marinetags = set()
        for mant in bunker_if.marinetags:
            if mant in (mar.tag for mar in bunker_if.units(MARINE)):
                bunker_if.visible_marinetags.add(mant)
        # init scvtags
        for mant in bunker_if.scvtags:
            if mant not in bunker_if.scvtags_inited:
                bunker_if.scvtags_inited.add(mant)
                bunker_if.astate[mant] = 'returning'
                for man in bunker_if.units(SCV):
                    if man.tag == mant:
                        man.move(bunker_if.hiding_spot)
        # init marines
        for mant in bunker_if.marinetags:
            if mant not in bunker_if.marinetags_inited:
                bunker_if.marinetags_inited.add(mant)
                bunker_if.loadpast[mant] = 0
                bunker_if.astate[mant] = 'returning'
                # returning marine will be commanded to walk later
        # init bunkers
        for bunt in bunker_if.bunkertags:
            if bunt not in bunker_if.bunkertags_inited:
                bunker_if.bunkertags_inited.add(bunt)
                bunker_if.bunk_ammar[bunt] = 0
                for bun in bunker_if.structures(BUNKER):
                    if bun.tag == bunt:
                        bunker_if.log('bun(AbilityId.RALLY_BUILDING,bunker_if.door[bunt])')
                        bun(AbilityId.RALLY_BUILDING,bunker_if.door[bunt])
        # loadpast
        for mant in bunker_if.marinetags:
            if bunker_if.loadpast[mant] < load_frames:
                bunker_if.loadpast[mant] += 1
        # lost bunker
        lost = set()
        for bunt in bunker_if.bunkertags:
            if bunt not in (bun.tag for bun in bunker_if.structures(BUNKER)):
                lost.add(bunt)
        bunker_if.bunkertags -= lost
        for mant in bunker_if.visible_marinetags:
            if mant in bunker_if.goalbunkertag:
                bunt = bunker_if.goalbunkertag[mant]
                if bunt not in bunker_if.bunkertags:
                    del bunker_if.goalbunkertag[mant]
        # minmarperbunker
        bunkers = len(bunker_if.bunkertags)
        marines = len(bunker_if.marinetags)
        minmarperbunker = 0
        marover = 0
        if bunkers > 0:
            minmarperbunker = marines // bunkers
            marover = marines % bunkers
        # correct bunk_ammar[bu], the wished amount of marines per bunker
        marextra = 0
        for bunt in bunker_if.bunkertags:
            if bunker_if.bunk_ammar[bunt] < minmarperbunker:
                bunker_if.bunk_ammar[bunt] = minmarperbunker
            elif bunker_if.bunk_ammar[bunt] == minmarperbunker + 1:
                marextra += 1
            elif bunker_if.bunk_ammar[bunt] > minmarperbunker + 1:
                bunker_if.bunk_ammar[bunt] = minmarperbunker + 1
                marextra += 1
        if marextra < marover:
            for bunt in bunker_if.bunkertags:
                if marextra < marover:
                    if bunker_if.bunk_ammar[bunt] == minmarperbunker:
                        bunker_if.bunk_ammar[bunt] += 1
                        marextra += 1
        if marextra > marover:
            for bunt in bunker_if.bunkertags:
                if marextra > marover:
                    if (bunker_if.bunk_ammar[bunt] == minmarperbunker + 1):
                        for bun in bunker_if.structures(BUNKER):
                            if bun.tag == bunt:
                                if (len(bun.passengers) <= minmarperbunker):
                                    bunker_if.bunk_ammar[bunt] -= 1
                                    marextra -= 1
        if marextra > marover:
            for bunt in bunker_if.bunkertags:
                if marextra > marover:
                    if (bunker_if.bunk_ammar[bunt] == minmarperbunker + 1):
                        bunker_if.bunk_ammar[bunt] -= 1
                        marextra -= 1
        # max 4 or 6
        if minmarperbunker >= 4:
            for bunt in bunker_if.bunkertags:
                bunker_if.bunk_ammar[bunt] = min(bunker_if.bunk_ammar[bunt],4)
        #
        # bunk_cvs
        for mant in bunker_if.scvtags:
            if bunker_if.astate[mant] == 'working':
                bunt = bunker_if.goalbunkertag[mant]
                if bunt in bunker_if.bunkertags:
                    for bun in bunker_if.structures(BUNKER):
                        if bun.tag == bunt:
                            if bun.health == bun.health_max:
                                bunker_if.astate[mant] = 'returning'
                else:
                    del bunker_if.goalbunkertag[mant]
                    bunker_if.astate[mant] = 'returning'
            if bunker_if.astate[mant] == 'walking':
                bunt = bunker_if.goalbunkertag[mant]
                if bunt in bunker_if.bunkertags:
                    for bun in bunker_if.structures(BUNKER):
                        if bun.tag == bunt:
                            for man in bunker_if.units(SCV):
                                if man.tag == mant:
                                    if bunker_if.near(man.position, bun.position, load_dist):
                                        man.repair(bun)
                                        bunker_if.astate[mant] = 'working'
                else: # bunker gone
                    del bunker_if.goalbunkertag[mant]
                    bunker_if.astate[mant] = 'returning'
            if bunker_if.astate[mant] in ['resting','returning']:
                for bunt in bunker_if.bunkertags:
                    if bunker_if.astate[mant] in ['resting','returning']:
                        for bun in bunker_if.structures(BUNKER):
                            if bun.tag == bunt:
                                if bun.health < bun.health_max:
                                    bunker_if.goalbunkertag[mant] = bunt
                                    for man in bunker_if.units(SCV):
                                        if man.tag == mant:
                                            if bunker_if.near(man.position, bun.position, load_dist):
                                                man.repair(bun)
                                                bunker_if.astate[mant] = 'working'
                                            else:
                                                man.move(bunker_if.door[bunt])
                                                bunker_if.astate[mant] = 'walking'
            if bunker_if.astate[mant] == 'returning':
                for man in bunker_if.units(SCV):
                    if man.tag == mant:
                        man.move(bunker_if.hiding_spot)
                        bunker_if.astate[mant] = 'resting'
        # unload
        for bunt in bunker_if.bunkertags:
            for bun in bunker_if.structures(BUNKER):
                if bun.tag == bunt:
                    if len(bun.passengers) > bunker_if.bunk_ammar[bunt]:
                        bunker_if.log('bun(AbilityId.UNLOADALL_BUNKER)')
                        bun(AbilityId.UNLOADALL_BUNKER)
        # dedication
        dedicated = {}
        for bunt in bunker_if.bunkertags:
            dedicated[bunt] = 0
            for mant in bunker_if.marinetags:
                if mant in bunker_if.goalbunkertag:
                    if bunker_if.goalbunkertag[mant] == bunt:
                        dedicated[bunt] += 1
        # stop visible overdedication
        changed = True
        while changed:
            changed = False
            furthest = 0
            for mant in bunker_if.visible_marinetags:
                if mant in bunker_if.goalbunkertag:
                    bunt = bunker_if.goalbunkertag[mant]
                    if dedicated[bunt] > bunker_if.bunk_ammar[bunt]:
                        for bun in bunker_if.structures(BUNKER):
                            if bun.tag == bunt:
                                for man in bunker_if.units(MARINE):
                                    if man.tag == mant:
                                        sd = bunker_if.sdist(man.position,bun.position)
                                        if sd > furthest:
                                            furthest = sd
                                            furthestmant = mant
            if furthest > 0:
                mant = furthestmant
                bunt = bunker_if.goalbunkertag[mant]
                del bunker_if.goalbunkertag[mant]
                dedicated[bunt] -= 1
                changed = True
        # stop underdedication
        for bunt in bunker_if.bunkertags:
            if dedicated[bunt] < bunker_if.bunk_ammar[bunt]:
                changed = True
                while changed:
                    changed = False
                    if dedicated[bunt] < bunker_if.bunk_ammar[bunt]:
                        closest = 99999
                        for mant in bunker_if.visible_marinetags:
                            if mant not in bunker_if.goalbunkertag:
                                for bun in bunker_if.structures(BUNKER):
                                    if bun.tag == bunt:
                                        for man in bunker_if.units(MARINE):
                                            if man.tag == mant:
                                                sd = bunker_if.sdist(man.position, bun.position)
                                                if sd < closest:
                                                    closest = sd
                                                    closestmant = mant
                        if closest < 99999:
                            mant = closestmant
                            bunker_if.goalbunkertag[mant] = bunt
                            dedicated[bunt] += 1
                            changed = True
        # now, move marines
        # assignment changes
        for mant in bunker_if.visible_marinetags:
            oldgoal = bunker_if.notag # use tags to compare
            if mant in old_goalbunkertag:
                oldgoal = old_goalbunkertag[mant]
            newgoal = bunker_if.notag
            if mant in bunker_if.goalbunkertag:
                newgoal = bunker_if.goalbunkertag[mant]
            # end old assignment
            if (oldgoal != bunker_if.notag): # was walking or working
                if (oldgoal != newgoal): # not there
                    bunker_if.astate[mant] = 'returning'
                    # if marine ends in returning state, it will be given a walk command
            # start new assignment
            if (newgoal != bunker_if.notag): # start walking or working
                if (oldgoal != newgoal): # not there
                    bunt = bunker_if.goalbunkertag[mant]
                    for man in bunker_if.units(MARINE):
                        if man.tag == mant:
                            bunker_if.astate[mant] = 'walking'
                            man.move(bunker_if.door[bunt])
        # astate changes by end task
        for mant in bunker_if.visible_marinetags:
            if bunker_if.astate[mant] == 'working':
                if bunker_if.loadpast[mant] == load_frames:
                    # loadcommand was long ago, but he is visible; he must be ejected
                    del bunker_if.goalbunkertag[mant]
                    bunker_if.astate[mant] = 'returning'
                    # returning marine will be commanded to walk later
            if bunker_if.astate[mant] == 'walking':
                bunt = bunker_if.goalbunkertag[mant]
                for bun in bunker_if.structures(BUNKER):
                    if bun.tag == bunt:
                        for man in bunker_if.units(MARINE):
                            if man.tag == mant:
                                if bunker_if.near(man.position, bun.position, load_dist):
                                    if bun in bunker_if.structures(BUNKER).ready: # finished building
                                        bunker_if.log('bun(AbilityId.LOAD_BUNKER,man)')
                                        bun(AbilityId.LOAD_BUNKER, man)
                                        bunker_if.loadpast[mant] = 0
                                        bunker_if.astate[mant] = 'working'
            if bunker_if.astate[mant] == 'returning':
                for man in bunker_if.units(MARINE):
                    if man.tag == mant:
                        man.attack(bunker_if.hiding_spot)
                        bunker_if.astate[mant] = 'resting'
        # log
        if len(bunker_if.bunkertags) > 0:
            bunker_if.log('bunkers '+str(len(bunker_if.bunkertags))+'  marines '+str(len(bunker_if.marinetags))
                            +'  scvs '+str(len(bunker_if.scvtags)))
            astate_count = {}
            for mant in bunker_if.visible_marinetags:
                astate_count[bunker_if.astate[mant]] = 0
            for mant in bunker_if.visible_marinetags:
                astate_count[bunker_if.astate[mant]] += 1
            for st in astate_count:
                bunker_if.log(st+' '+str(astate_count[st]))
            inbunker = 0
            for bun in bunker_if.structures(BUNKER):
                if bun.tag in bunker_if.bunkertags:
                    inbunker += len(bun.passengers)
            bunker_if.log('in bunker '+str(inbunker))

    async def salvage(bun):
        # to be called repeatedly until a bunker is gone
        if bun in bunker_if.structures(BUNKER).ready:
            # chosen is to set the passengers free
            for man in bun.passengers:
                if man.tag in bunker_if.marinetags:
                    bunker_if.marinetags.remove(man.tag)
            # no bunker_if.bunkertags.remove(bun.tag), this happens after it is gone
            if len(bun.passengers) == 0:
                if AbilityId.EFFECT_SALVAGE in (await bunker_if.get_available_abilities([bun]))[0]:
                    bunker_if.log('bun(AbilityId.SALVAGE_BUNKER)')
                    bun(AbilityId.EFFECT_SALVAGE)
            if len(bun.passengers) > 0:
                bunker_if.log('bun(AbilityId.UNLOADALL_BUNKER)')
                bun(AbilityId.UNLOADALL_BUNKER)

    # INTERNAL
    def sdist(p, q):
        return (p.x - q.x) * (p.x - q.x) + (p.y - q.y) * (p.y - q.y)

    def near(p,q,supdist) -> bool:
#       works for integers as well as for floats
        return (bunker_if.sdist(p,q) < supdist*supdist)



