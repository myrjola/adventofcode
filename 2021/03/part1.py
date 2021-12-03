from statistics import mode

lines = [line.strip() for line in open("input.txt", 'r').readlines()]

bit_columns = zip(*lines)

most_common_bits = [mode(bits) for bits in bit_columns]

most_common_bits_int = int(''.join(most_common_bits), 2)
least_common_bits_int = ~most_common_bits_int & 0xFFF

print(most_common_bits_int*least_common_bits_int)
