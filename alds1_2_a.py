
_input = '_input_alds1_2_a'

with open(_input, 'r') as f:
    for i, line in enumerate(f.readlines()):
        if i == 0:
            length = int(line)
        else:
            eles = [int(l) for l in line.split()]

length = int(input())
eles = [int(l) for l in input().split()]

times = 0
for i in range(length):
    flag = 1
    while flag > 0:
        flag = 0
        for j in range(length-1, i, -1):
            if eles[j] < eles[j - 1]:
                _temp = eles[j]
                eles[j] = eles[j-1]
                eles[j-1] = _temp
                flag = 1
                times += 1

print(*eles)
print(times)
