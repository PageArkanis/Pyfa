type = "passive"
def handler(fit, src, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.group.name == "Structure Doomsday Weapon",
                                     "lightningWeaponTargetAmount", src.getModifiedItemAttr("structureRigDoomsdayTargetAmountBonus"),
                                     stackingPenalties=True)