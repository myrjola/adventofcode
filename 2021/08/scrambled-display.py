lines = list(open("input.txt").readlines())

signals, four_digits = lines[0].strip().split('|')

output = [line.strip().split('|')[1] for line in lines]

easy_digits = [digit for digits in output for digit in digits.split() if len(digit) in [2, 3, 4, 7]]

print("part 1: ", len(easy_digits))
