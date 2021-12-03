from statistics import mode

lines = [line.strip() for line in open("test-input.txt", 'r').readlines()]

bit_columns = zip(*lines)

most_common_bits = [mode(bits) for bits in bit_columns]


