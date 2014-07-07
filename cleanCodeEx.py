def createFk(rootJoint):
    """
    Pass the first joint in the chain as the rootJoint.
    Creates a full chain FK set up.
    """
    cmds.select(rootJoint , hi=1)
    currentChain = cmds.ls(sl=1)
    chainLength = len(currentChain)
    current = 0
    for jnt in currentChain:
        sep = '_'
        ctrlName = [jnt, 'Fk', str(current)]
        ctrl = nsCtrl.square(name = sep.join(ctrlName), position = [0, 0, 0])
        nsUtil.getWorldSpace(obj = jnt, target = ctrl)
        padGrp = nsUtil.rigPad(child = ctrl, parent = jnt)
        cmds.parentConstraint(ctrl, jnt, mo = 1)
        if current > 0:
            cmds.parent(padGrp, temp)
            temp = ctrl
            current = current + 1
        else:
            temp = ctrl
            current = current + 1