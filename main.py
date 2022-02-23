import sys

from cry_tools.chunk_file_reader import ChunkFileReader


_, file_name = sys.argv

reader = ChunkFileReader()
reader.read(file_name)
