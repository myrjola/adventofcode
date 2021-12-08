lines = list(open("input.txt").readlines())

outputs = [line.strip().split(' | ')[1] for line in lines]

easy_digits = [digit for output in outputs for digit in output.split() if len(digit) in [2, 3, 4, 7]]

print("part 1: ", len(easy_digits))

def deduce_digits(signals):
    one = next(signal for signal in signals if len(signal) == 2)
    seven = next(signal for signal in signals if len(signal) == 3)
    four = next(signal for signal in signals if len(signal) == 4)
    eight = next(signal for signal in signals if len(signal) == 7)
    three = next(signal for signal in signals if len(signal) == 5 and len(signal.difference(seven)) == 2 and one.issubset(signal))
    nine = next(signal for signal in signals if len(signal) == 6 and seven.union(four).issubset(signal))
    six = next(signal for signal in signals if len(signal) == 6 and not one.issubset(signal))
    zero = next(signal for signal in signals if len(signal) == 6 and signal not in [nine, six])
    five = next(signal for signal in signals if len(signal) == 5 and len(nine.difference(signal)) == 1 and not one.issubset(signal))
    two = next(signal for signal in signals if signal not in [zero, one, three, four, five, six, seven, eight, nine])
    return {
        zero: '0',
        one: '1',
        two: '2',
        three: '3',
        four: '4',
        five: '5',
        six: '6',
        seven: '7',
        eight: '8',
        nine: '9'
    }

inputs = [(list(map(frozenset, signals.split())), list(map(frozenset, outputs.split()))) for line in lines for signals, outputs in [line.strip().split(' | ')]]

# for signals, outputs in inputs:
#     deduction = deduce_digits(signals)
#     print([deduction[output] for output in outputs])

print("part 2: ", sum([int(''.join([deduce_digits(signals)[output] for output in outputs])) for signals, outputs in inputs]))





