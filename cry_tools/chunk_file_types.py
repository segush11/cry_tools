from enum import IntEnum

import construct as cs


class FileTypes(IntEnum):
    FileType_Geom = 0xFFFF0000
    FileType_Anim = 0xFFFF0001


class ChunkTypes(IntEnum):
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


FileHeader = cs.Struct(
    'signature' / cs.PaddedString(8, 'ascii'),
    'file_type' / cs.Enum(cs.Int32ul, FileTypes),
    'file_version' / cs.Hex(cs.Int32ul),
    'file_offset' / cs.Int32ul
)


ChunkHeader = cs.Struct(
    'chunk_type' / cs.Enum(cs.Int32ul, ChunkTypes),
    'chunk_version' / cs.Hex(cs.Int32ul),
    'file_offset' / cs.Int32ul,
    'chunk_id' / cs.Int32ul,
)


ChunkHeaders = cs.Struct(
    'num_chunks' / cs.Int32ul,
    'chunk_list' / cs.Array(cs.this.num_chunks, ChunkHeader)
)


RangeEntity = cs.Struct(
    'name' / cs.Bytes(32),
    'start' / cs.Int32sl,
    'end' / cs.Int32sl,
)


TimingChunk0x918 = cs.Struct(
    'chunk_header' / ChunkHeader,
    'seconds_per_tick' / cs.Float32l,
    'ticks_per_frame' / cs.Int32sl,
    'global_range' / RangeEntity
)
