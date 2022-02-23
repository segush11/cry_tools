from enum import Enum
from struct import Struct
from collections import namedtuple
from dataclasses import dataclass

from cry_tools.chunk_file_utils import *


class FileTypes(Enum):
    FileType_Geom = 0xFFFF0000
    FileType_Anim = 0xFFFF0001


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


FileHeaderStruct = Struct('<7sx I I I')
FileHeader = namedtuple('FileHeader', [
    'signature',
    'file_type',
    'file_version',
    'file_offset'
])


ChunkHeaderStruct = Struct('<I I I I')
ChunkHeader = namedtuple('ChunkHeader', [
    'chunk_type',
    'chunk_version',
    'file_offset',
    'chunk_id',
])


RangeEntityStruct = Struct('<32s i i')
RangeEntity = namedtuple('RangeEntity', [
    'name',
    'start',
    'end'
])


@dataclass
class TimingChunk0918:
    chunk_header: ChunkHeader
    seconds_per_tick: float
    seconds_per_frame: float
    ticks_per_frame: int
    global_range: RangeEntity

    @staticmethod
    def make_from_file(input_file):
        chunk_type, chunk_version, file_offset, chunk_id = unpack_struct(ChunkHeaderStruct, input_file)
        chunk_header = ChunkHeader(
            chunk_id=chunk_id,
            chunk_type=ChunkTypes(chunk_type),
            chunk_version=chunk_version,
            file_offset=file_offset
        )

        seconds_per_tick, = unpack_values('<f', input_file)
        ticks_per_frame, = unpack_values('<i', input_file)
        seconds_per_frame = seconds_per_tick * ticks_per_frame
        global_range = RangeEntity._make(unpack_struct(RangeEntityStruct, input_file))

        return TimingChunk0918(
            chunk_header=chunk_header,
            seconds_per_tick=seconds_per_tick,
            seconds_per_frame=seconds_per_frame,
            ticks_per_frame=ticks_per_frame,
            global_range=global_range
        )
