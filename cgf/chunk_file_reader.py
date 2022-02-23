from cgf.base_structures import FileHeader, ChunkTable
from cgf.base_types import ChunkTypes
from cgf.chunk_file import ChunkFile
from cgf.chunk_types import *


class ChunkFileReader:
    def read(self, file_name):
        stream = open(file_name, 'rb')

        header = FileHeader.read_from(stream)

        stream.seek(header.file_offset)

        chunk_table = ChunkTable.read_from(stream)

        chunks = []

        for chunk_header in chunk_table.chunk_headers:
            match chunk_header.chunk_type:
                case ChunkTypes.ChunkType_Timing:
                    match chunk_header.chunk_version:
                        case 0x918:
                            stream.seek(chunk_header.file_offset)

                            chunk = TimingChunk0918.read_from(stream)
                            chunks.append(chunk)

        chunk_file = ChunkFile()
        chunk_file.header = header
        chunk_file.chunk_table = chunk_table

        return chunk_file
