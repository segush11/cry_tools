from cgf.base_structures import ChunkHeader, RangeEntity

from struct import unpack, calcsize


class TimingChunk0918:
    def __init__(self, header, seconds_per_tick, ticks_per_frame, global_range):
        self.header = header
        self.seconds_per_tick = seconds_per_tick
        self.ticks_per_frame = ticks_per_frame
        self.seconds_per_frame = seconds_per_tick * ticks_per_frame
        self.global_range = global_range

    @staticmethod
    def read_from(stream):
        header = ChunkHeader.read_from(stream)
        seconds_per_tick, = unpack('<f', stream.read(calcsize('<f')))
        ticks_per_frame, = unpack('<i', stream.read(calcsize('<i')))
        global_range = RangeEntity.read_from(stream)

        return TimingChunk0918(header, seconds_per_tick, ticks_per_frame, global_range)
