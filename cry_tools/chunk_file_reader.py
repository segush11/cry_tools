from cry_tools.chunk_file_types import *


class ChunkFileReader:
    def read(self, file_name: str):
        with open(file_name, 'rb') as input_file:
            signature, file_type, file_version, file_offset = unpack_struct(FileHeaderStruct, input_file)

            file_header = FileHeader(
                signature=signature[:-1].decode('ascii'),
                file_type=FileTypes(file_type),
                file_version=file_version,
                file_offset=file_offset
            )

            input_file.seek(file_header.file_offset)

            chunks_count, = unpack_values('<I', input_file)
            chunk_headers = []

            for chunk_index in range(chunks_count):
                chunk_type, chunk_version, file_offset, chunk_id = unpack_struct(ChunkHeaderStruct, input_file)
                chunk_header = ChunkHeader(
                    chunk_id=chunk_id,
                    chunk_type=ChunkTypes(chunk_type),
                    chunk_version=chunk_version,
                    file_offset=file_offset
                )

                chunk_headers.append(chunk_header)

            chunk_list = []

            for chunk_header in chunk_headers:
                match chunk_header.chunk_type:
                    case ChunkTypes.ChunkType_Timing:
                        match chunk_header.chunk_version:
                            case 0x918:
                                input_file.seek(chunk_header.file_offset)
                                chunk_item = TimingChunk0918.make_from_file(input_file)
                                chunk_list.append(chunk_item)
