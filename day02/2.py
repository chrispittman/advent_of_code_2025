f = open('data', 'r')
data = f.readlines()[0].split(',')
data = [pair.split('-') for pair in data]

# partition a string into substrings of a given length
def partition_str(s, size):
    for i in range(0, len(s), size):
        yield s[i:i + size]

result = 0
for (min_range, max_range) in data:
    for test_num in range(int(min_range), int(max_range)+1):
        test_str = str(test_num)
        is_invalid_id = False
        for substr_length in range( (len(test_str)//2) ):
            partitions = list(partition_str(test_str, substr_length+1))
            all_identical = len(set(partitions)) == 1
            if all_identical:
                is_invalid_id = True
                break
        if is_invalid_id:
            result += test_num

print(result)