_input = '_input_alds1_2_d'

# _list = []
# with open(_input, 'r') as f:
#     for i, line in enumerate(f.readlines()):
#         if i == 0:
#             length = int(line)
#         else:
#             _list.append(line.rstrip())


cnt = 0
coefficients = [1]
n = 1

_list = []
length = int(input())
for i in range(length):
    try:
        _list.append(int(input()))
    except EOFError:
        continue


for i in range(1,length):
    if i < n:
        continue
    coefficients.append(i)
# 2.25にするのが肝らしい
    n = i*2.25 + 1

for c in coefficients[::-1]:
    for i in range(length):
        val = _list[i]
        j = i - c
        while j >= 0 and _list[j] > val:
            _list[j + c] = _list[j]
            j -= c
            cnt += 1
        _list[j+c] = val

print(len(coefficients))
print(*coefficients[::-1])
print(cnt)
print(*_list, sep='\n')
