from typing import Optional

from ._module import Module


class Bone(Module):
    FRONT = 0
    BONE_LENGTH_BOUNDS = (0.02, 0.1)

    def __init__(self, rotation: float, bone_length_output: float):
        self._bone_length = \
            ((bone_length_output + 1) / 2) * (Bone.BONE_LENGTH_BOUNDS[1]-Bone.BONE_LENGTH_BOUNDS[0]) + Bone.BONE_LENGTH_BOUNDS[0]
        super().__init__(Module.Type.BONE, 1, rotation)

    @property
    def bone_length(self):
        return self._bone_length

    @property
    def front(self) -> Optional[Module]:
        return self.children[self.FRONT]

    @front.setter
    def front(self, module: Module) -> None:
        self.children[self.FRONT] = module