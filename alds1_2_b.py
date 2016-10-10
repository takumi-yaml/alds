_input = '_input_alds1_2_b'

with open(_input, 'r') as f:
    for i, line in enumerate(f.readlines()):
        if i == 0:
            length = int(line)
        else:
            eles = [int(l) for l in line.split()]

length = int(input())
eles = [int(l) for l in input().split()]
times = 0

for i in range(length-1):
    _min = i
    for j in range(i, length):
        if eles[j] < eles[_min]:
            _min = j
    if i != _min:
        eles[i], eles[_min] = eles[_min], eles[i]
        times += 1

print(*eles)
print(times)
