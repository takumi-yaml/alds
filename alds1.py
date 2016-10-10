from _collections import deque

_temp = []

size = int(input().rstrip())
for i in range(size):
    try:
        _temp.append(int(input()))
    except EOFError:
        continue

# with open('_input_alds1', 'r') as f:
#     for i, l in enumerate(f.readlines()):
#         if i == 0:
#             larry = l
#         else:
#             line = l.rstrip()
#             _temp.append(int(l))
# f.close()

my_max = -20000000000000
my_min = _temp.pop(0)


for val in _temp:
    my_max = max(my_max, (val - my_min))
    my_min = min(my_min, val)

print(my_max)


# 1. 最大差分maxを、shiftして残りの配列中で一番大きい数字との差分と比較
# 2. 最初の配列中から低い半分の数だけ、それ以降の大きいとの差分を出しそれをmaxと比較
