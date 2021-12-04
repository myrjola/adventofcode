lines = [line.strip() for line in open("input.txt", 'r').readlines()]

rows = [line.strip().split() for line in lines[1:] if len(line.strip()) > 0]

rows_per_column = 5
board_rows = [rows[i:i+rows_per_column] for i in range(0, len(rows), rows_per_column)]
# add columns to the boards
boards = [(*zip(*rs), *rs) for rs in board_rows]

def find_bingo(bingo_numbers, bingo_boards):
    for i in range(len(bingo_numbers)):
        for board in bingo_boards:
            for line in board:
                if all(element in bingo_numbers[:i] for element in line):
                    return bingo_numbers[:i], board

used_numbers, winning_board = find_bingo(lines[0].split(','), boards)

board_numbers = set([x for line in winning_board for x in line])
unmarked_numbers = board_numbers.difference(used_numbers)

print(int(used_numbers[-1]) * sum([int(x) for x in unmarked_numbers]))
