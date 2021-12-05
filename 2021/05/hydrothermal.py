import numpy as np

lines = [line.strip() for line in open("input.txt", 'r').readlines()]

vents = [line.split(' -> ') for line in lines]
coordinates = [np.array([endpoints.split(',') for endpoints in vent]).astype(int) for vent in vents]

vectors = [np.subtract(end, start) for start, end in coordinates]

board = np.zeros((1000,1000), dtype=np.int64)

for (start, end), vector in zip(coordinates, vectors):
    # filter diagonal vectors
    if 0 not in vector:
        continue

    # This logic was flawed but worked for part 1 😅
    length = int(np.linalg.norm(vector))
    unit = vector / length

    vent_cloud_points = [start + (unit * i) for i in range(length + 1)]

    for x, y in vent_cloud_points:
        board[int(y)][int(x)] += 1

# print("\n".join(["".join(map(str,line)) for line in board]))

print("Part 1: ", len(np.where(board >= 2)[0]))

board = np.zeros((1000,1000), dtype=np.int64)

for (start, end), vector in zip(coordinates, vectors):
    unit = np.nan_to_num(vector / abs(vector))
    length = round(np.linalg.norm(vector) / np.linalg.norm(unit))

    vent_cloud_points = [start + (unit * i) for i in range(length + 1)]

    for x, y in vent_cloud_points:
        board[int(y)][int(x)] += 1

# print("\n".join(["".join(map(str,line)) for line in board]))

print("Part 2: ", len(np.where(board >= 2)[0]))
