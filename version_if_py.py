# version_if_py.py
# reduced copy from Infy's Sharpy
from typing import Set, Dict, Any
from sc2 import UnitTypeId, AbilityId
from sc2.ids.buff_id import BuffId
from sc2.ids.upgrade_id import UpgradeId

class version_if:

    def version410():
            version_if._set_enum_mapping(
                UpgradeId,
                {
                    UpgradeId.ENHANCEDSHOCKWAVES: 296,
                    UpgradeId.MICROBIALSHROUD: 297,
                    UpgradeId.SUNDERINGIMPACT: 298,
                    UpgradeId.AMPLIFIEDSHIELDING: 299,
                    UpgradeId.PSIONICAMPLIFIERS: 300,
                    UpgradeId.SECRETEDCOATING: 301,
                },
            )
            version_if._set_enum_mapping(
                BuffId,
                {
                    BuffId.AMORPHOUSARMORCLOUD: 295,
                    BuffId.RAVENSHREDDERMISSILEARMORREDUCTIONUISUBTRUCT: 296,
                    BuffId.BATTERYOVERCHARGE: 297,
                },
            )
            version_if._set_enum_mapping(
                UnitTypeId,
                {
                    UnitTypeId.INHIBITORZONESMALL: 1968,
                    UnitTypeId.INHIBITORZONEMEDIUM: 1969,
                    UnitTypeId.INHIBITORZONELARGE: 1970,
                    UnitTypeId.ACCELERATIONZONESMALL: 1971,
                    UnitTypeId.ACCELERATIONZONEMEDIUM: 1972,
                    UnitTypeId.ACCELERATIONZONELARGE: 1973,
                    UnitTypeId.ACCELERATIONZONEFLYINGSMALL: 1974,
                    UnitTypeId.ACCELERATIONZONEFLYINGMEDIUM: 1975,
                    UnitTypeId.ACCELERATIONZONEFLYINGLARGE: 1976,
                    UnitTypeId.INHIBITORZONEFLYINGSMALL: 1977,
                    UnitTypeId.INHIBITORZONEFLYINGMEDIUM: 1978,
                    UnitTypeId.INHIBITORZONEFLYINGLARGE: 1979,
                    UnitTypeId.ASSIMILATORRICH: 1980,
                    UnitTypeId.EXTRACTORRICH: 1981,
                    UnitTypeId.REFINERYRICH: 1960,
                    UnitTypeId.MINERALFIELD450: 1982,
                    UnitTypeId.MINERALFIELDOPAQUE: 1983,
                    UnitTypeId.MINERALFIELDOPAQUE900: 1984,
                },
            )
            version_if._set_enum_mapping(
                AbilityId,
                {
                    AbilityId.BATTERYOVERCHARGE_BATTERYOVERCHARGE: 3801,
                    AbilityId.AMORPHOUSARMORCLOUD_AMORPHOUSARMORCLOUD: 3803,
                },
            )
            version_if._set_enum_mapping(
                BuffId,
                {
                    BuffId.INHIBITORZONETEMPORALFIELD: 292,
                    BuffId.RESONATINGGLAIVESPHASESHIFT: 293,
                    BuffId.AMORPHOUSARMORCLOUD: 294,
                    BuffId.RAVENSHREDDERMISSILEARMORREDUCTIONUISUBTRUCT: 295,
                    BuffId.BATTERYOVERCHARGE: 296,
                },
            )
            version_if._set_enum_mapping(
                UnitTypeId,
                {
                    UnitTypeId.ASSIMILATORRICH: 1955,
                    UnitTypeId.EXTRACTORRICH: 1956,
                    UnitTypeId.INHIBITORZONESMALL: 1957,
                    UnitTypeId.INHIBITORZONEMEDIUM: 1958,
                    UnitTypeId.INHIBITORZONELARGE: 1959,
                    UnitTypeId.REFINERYRICH: 1960,
                    UnitTypeId.MINERALFIELD450: 1961,
                },
            )
            version_if._set_enum_mapping(
                AbilityId, {AbilityId.AMORPHOUSARMORCLOUD_AMORPHOUSARMORCLOUD: 3801},
            )


    def _set_enum_mapping(enum: Any, items: Dict[Any, int]):
        for enum_key, value in items.items():
            enum_key._value_ = value
            enum._member_map_[enum_key.name] = value
            enum._value2member_map_[value] = enum_key


