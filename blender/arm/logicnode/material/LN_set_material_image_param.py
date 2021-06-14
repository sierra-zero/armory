from arm.logicnode.arm_nodes import *

class SetMaterialImageParamNode(ArmLogicTreeNode):
    """Set an image value material parameter to the specified object. 
    
    @seeNode Get Scene Root
    
    @input Object: Object whose material parameter should change. Use `Get Scene Root` node to set paramter globally.
    
    @input Per Object: 
        - `Enabled`: Set material parameter specific to this object. Global parameter will be ignored.
        - `Disabled`: Set parameter globally, including this object.

    @input Material: Material whose parameter to be set.

    @input Node: Name of the parameter.

    @input Image: Name of the image.
    """
    bl_idname = 'LNSetMaterialImageParamNode'
    bl_label = 'Set Material Image Param'
    arm_section = 'params'
    arm_version = 2

    def init(self, context):
        super(SetMaterialImageParamNode, self).init(context)
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('ArmNodeSocketObject', 'Object')
        self.add_input('NodeSocketBool', 'Per Object')
        self.add_input('NodeSocketShader', 'Material')
        self.add_input('NodeSocketString', 'Node')
        self.add_input('NodeSocketString', 'Image')

        self.add_output('ArmNodeSocketAction', 'Out')

    def get_replacement_node(self, node_tree: bpy.types.NodeTree):
        if self.arm_version not in (0, 1):
            raise LookupError()
            
        return NodeReplacement(
            'LNSetMaterialImageParamNode', self.arm_version, 'LNSetMaterialImageParamNode', 2,
            in_socket_mapping={0:0, 1:3, 2:4, 3:5}, out_socket_mapping={0:0}
        )
