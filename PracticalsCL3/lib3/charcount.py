from collections import defaultdict

# Simulated Mapper
def mapper(text):
    mapped = []
    for line in text:
        for char in line:
            if char != ' ' and char !='.' and char != '\n':
                mapped.append((char, 1))
    return mapped

# Simulated Shuffle and Sort
def shuffle_sort(mapped_data):
    shuffled = defaultdict(list)
    for char, count in mapped_data:
        shuffled[char].append(count)
    return shuffled

# Simulated Reducer
def reducer(shuffled_data):
    reduced = {}
    for char, counts in shuffled_data.items():
        reduced[char] = sum(counts)
    return reduced

# Input Text File
with open(r"D:\PracticalsCL3\lib3\input.txt", 'r') as file:
    lines = file.readlines()

# MapReduce Pipeline
mapped = mapper(lines)
shuffled = shuffle_sort(mapped)
reduced = reducer(shuffled)

# Output Result
print("Character Count:")
for char, count in reduced.items():
    print(f"{char}: {count}")