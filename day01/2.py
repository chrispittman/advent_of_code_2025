f = open('data', 'r')
data = [line.rstrip() for line in f.readlines()]
data = [(line[0], int(line[1:])) for line in data]

ptr = 50
num_zeros = 0
for (direction, amt) in data:
    for i in range(amt):
        if direction == 'L':
            ptr -= 1
        if direction == 'R':
            ptr += 1
        if ptr % 100 == 0:
            num_zeros += 1

print(num_zeros)