import sys

from cgf.chunk_file_reader import ChunkFileReader

_, file_name = sys.argv

chunk_file_reader = ChunkFileReader()
chunk_file = chunk_file_reader.read(file_name)
