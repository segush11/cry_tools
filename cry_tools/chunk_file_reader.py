from cry_tools.chunk_file_types import *


class ChunkFileReader:
    def read(self, file_name: str):
        with open(file_name, 'rb') as stream:
            file_header = FileHeader.parse_stream(stream)

            stream.seek(file_header.file_offset)

            chunk_headers = ChunkHeaders.parse_stream(stream)

            chunk_list = []

            for chunk_header in chunk_headers.chunk_list:
                match chunk_header.chunk_type:
                    case ChunkTypes.ChunkType_Timing.name:
                        match chunk_header.chunk_version:
                            case 0x918:
                                stream.seek(chunk_header.file_offset)

                                timing_chunk = TimingChunk0x918.parse_stream(stream)
                                chunk_list.append(timing_chunk)
