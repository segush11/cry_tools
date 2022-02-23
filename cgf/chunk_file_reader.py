from cgf.base_structures import FileHeader, ChunkTable
from cgf.chunk_file import ChunkFile


class ChunkFileReader:
    def read(self, file_name):
        stream = open(file_name, 'rb')

        header = FileHeader.read_from(stream)

        stream.seek(header.file_offset)

        chunk_table = ChunkTable.read_from(stream)

        chunk_file = ChunkFile()
        chunk_file.header = header
        chunk_file.chunk_table = chunk_table

        return chunk_file
