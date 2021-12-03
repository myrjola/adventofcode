from statistics import multimode
import collections

lines = [line.strip() for line in open("input.txt", 'r').readlines()]

filtered_lines = lines
bit_columns = list(zip(*filtered_lines))

for i in range(len(bit_columns)):
    column = bit_columns[i]
    most_common_bit = max(multimode(column))
    filtered_lines = [line for line in filtered_lines if line[i] == most_common_bit]
    bit_columns = list(zip(*filtered_lines))
    if (len(filtered_lines) == 1):
        break

oxygen_generator_rating = int(''.join(filtered_lines[0]), 2)

filtered_lines = lines
bit_columns = list(zip(*filtered_lines))

for i in range(len(bit_columns)):
    column = bit_columns[i]
    stats = collections.Counter(column).most_common()
    least_common = stats[-1][0]
    if (stats[0][0] == [1][0]):
        least_common = '0'

    filtered_lines = [line for line in filtered_lines if line[i] == least_common]
    if (len(filtered_lines) == 1):
        break

co2_scrubber_rating = int(''.join(filtered_lines[0]), 2)

print(oxygen_generator_rating*co2_scrubber_rating)
