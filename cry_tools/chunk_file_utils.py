import struct


def unpack_struct(input_struct, input_file):
    data_buffer = input_file.read(input_struct.size)
    unpacked_values = input_struct.unpack(data_buffer)

    return unpacked_values


def unpack_values(fmt, input_file):
    data_buffer = input_file.read(struct.calcsize(fmt))
    unpacked_values = struct.unpack(fmt, data_buffer)

    return unpacked_values
