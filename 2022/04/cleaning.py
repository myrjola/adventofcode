lines = open('input.txt').read().split('\n')[:-1]

elf_pairs = [line.split(',') for line in lines]


def cleaning_sections(elf):
    start, end = map(int, elf.split('-'))
    return set(range(start, end + 1))

def is_full_overlap(cleaning_sections1, cleaning_sections2):
    return cleaning_sections1.issubset(cleaning_sections2) or cleaning_sections2.issubset(cleaning_sections1)

def is_any_overlap(cleaning_sections1, cleaning_sections2):
    return len(cleaning_sections1.intersection(cleaning_sections2)) > 0

full_overlap = 0
any_overlap = 0
for elf_pair in elf_pairs:
    elf1_cleaning_sections, elf2_cleaning_sections = map(cleaning_sections, elf_pair)

    if is_full_overlap(elf1_cleaning_sections, elf2_cleaning_sections):
        full_overlap += 1

    if is_any_overlap(elf1_cleaning_sections, elf2_cleaning_sections):
        any_overlap += 1

print('part 1:', full_overlap)
print('part 2:', any_overlap)








