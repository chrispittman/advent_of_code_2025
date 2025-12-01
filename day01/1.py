f = open('data', 'r')
data = [line.rstrip() for line in f.readlines()]
data = [(line[0], int(line[1:])) for line in data]

ptr = 50
num_zeros = 0
for (direction, amt) in data:
    if direction == 'L':
        ptr -= amt
    if direction == 'R':
        ptr += amt
    if ptr % 100 == 0:
        num_zeros += 1

print(num_zeros)