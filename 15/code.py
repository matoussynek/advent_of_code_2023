def hash(string):
    current_value = 0
    for c in string:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value

strings = open('./input.txt').read().split(',')

tot = 0
for string in strings:
    tot += hash(string)

print(f'Star1 total: {tot}')

boxes = [[] for _ in range(256)]
focal_lengths = {}

for string in strings:
    if '-' in string:
        label = string[:-1]
        box_index = hash(label)
        if label in boxes[box_index]:
            boxes[box_index].remove(label)
    else:
        label, length = string.split("=")
        length = int(length)
        
        index = hash(label)
        if label not in boxes[index]:
            boxes[index].append(label)
            
        focal_lengths[label] = length

tot2 = 0
for i, box in enumerate(boxes, 1):
    for j, label in enumerate(box, 1):
        tot2 += i * j * focal_lengths[label]

print(f'Star2 total: {tot2}')