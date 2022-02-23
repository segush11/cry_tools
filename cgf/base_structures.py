from struct import unpack, calcsize

from cgf.base_types import FilesType, ChunkTypes


class FileHeader:
    def __init__(self, signature, file_type, file_offset, version):
        self.signature = signature
        self.file_type = file_type
        self.file_offset = file_offset
        self.version = version

    @staticmethod
    def read_from(stream):
        signature, = unpack('<7sx', stream.read(calcsize('<7sx')))
        file_type, version, file_offset = unpack('<III', stream.read(calcsize('<III')))

        return FileHeader(signature[:-1].decode('ascii'), FilesType(file_type), file_offset, version)


class ChunkHeader:
    def __init__(self, chunk_type, chunk_version, file_offset, chunk_id):
        self.chunk_type = chunk_type
        self.chunk_version = chunk_version
        self.chunk_id = chunk_id
        self.file_offset = file_offset

    @staticmethod
    def read_from(stream):
        chunk_type, chunk_version, file_offset, chunk_id = unpack('<IIII', stream.read(calcsize('<IIII')))

        return ChunkHeader(ChunkTypes(chunk_type), chunk_version, file_offset, chunk_id)


class ChunkTable:
    def __init__(self, num_chunks, chunk_headers):
        self.num_chunks = num_chunks
        self.chunk_headers = chunk_headers

    @staticmethod
    def read_from(stream):
        num_chunks, = unpack('<I', stream.read(calcsize('<I')))
        chunk_headers = [ChunkHeader.read_from(stream) for _ in range(num_chunks)]

        return ChunkTable(num_chunks, chunk_headers)


class RangeEntity:
    def __init__(self, name, range):
        self.name = name
        self.range = range

    @staticmethod
    def read_from(stream):
        name, = unpack('<32s', stream.read(calcsize('<32s')))
        start, end = unpack('<ii', stream.read(calcsize('<ii')))

        return RangeEntity(name, [start, end])