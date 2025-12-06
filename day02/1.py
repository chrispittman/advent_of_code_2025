f = open('data', 'r')
data = f.readlines()[0].split(',')
data = [pair.split('-') for pair in data]

result = 0
for (min_range, max_range) in data:
    for test_num in range(int(min_range), int(max_range)+1):
        test_str = str(test_num)
        midpoint = len(test_str)//2
        if test_str[0:midpoint] == test_str[midpoint:]:
            result += test_num

print(result)