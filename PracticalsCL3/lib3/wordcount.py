from collections import defaultdict
import re

# Simulated Mapper
def mapper(text):
    mapped = []
    for line in text:
        words = re.findall(r'\w+', line.lower())
        for word in words:
            mapped.append((word, 1))
    return mapped

# Simulated Shuffle and Sort
def shuffle_sort(mapped_data):
    shuffled = defaultdict(list)
    for word, count in mapped_data:
        shuffled[word].append(count)
    return shuffled

# Simulated Reducer
def reducer(shuffled_data):
    reduced = {}
    for word, counts in shuffled_data.items():
        reduced[word] = sum(counts)
    return reduced

# Input Text File
with open(r"D:\PracticalsCL3\lib3\input.txt", 'r') as file:
    lines = file.readlines()

# MapReduce Pipeline
mapped = mapper(lines)
shuffled = shuffle_sort(mapped)
reduced = reducer(shuffled)

# Output Result
print("Word Count:")
for word, count in reduced.items():
    print(f"{word}: {count}")