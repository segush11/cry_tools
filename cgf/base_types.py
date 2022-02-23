from enum import Enum


class FilesType(Enum):
    FileType_Geom = 0xFFFF0000
    FileType_Anim = 0xFFFF0001

    def __str__(self):
        return self.name


class ChunkTypes(Enum):
    ChunkType_ANY = 0
    ChunkType_Mesh = 0xCCCC0000
    ChunkType_Helper = 0xCCCC0001
    ChunkType_VertAnim = 0xCCCC0002
    ChunkType_BoneAnim = 0xCCCC0003
    ChunkType_GeomNameList = 0xCCCC0004
    ChunkType_BoneNameList = 0xCCCC0005
    ChunkType_MtlList = 0xCCCC0006
    ChunkType_MRM = 0xCCCC0007
    ChunkType_SceneProps = 0xCCCC0008
    ChunkType_Light = 0xCCCC0009
    ChunkType_PatchMesh = 0xCCCC000A
    ChunkType_Node = 0xCCCC000B
    ChunkType_Mtl = 0xCCCC000C
    ChunkType_Controller = 0xCCCC000D
    ChunkType_Timing = 0xCCCC000E
    ChunkType_BoneMesh = 0xCCCC000F
    ChunkType_BoneLightBinding = 0xCCCC0010
    ChunkType_MeshMorphTarget = 0xCCCC0011
    ChunkType_BoneInitialPos = 0xCCCC0012
    ChunkType_SourceInfo = 0xCCCC0013

    def __str__(self):
        return self.name
