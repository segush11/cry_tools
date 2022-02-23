import sys

from cry_tools.chunk_file_reader import ChunkFileReader


reader = ChunkFileReader()
reader.read(sys.argv[1])
