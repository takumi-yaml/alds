# length = input()
# eles = int(input().split(' '))


# with open('_input_alds1_1_a', 'r') as f:
#     for i, l in enumerate(f.readlines()):
#         if i == 0:
#             length = int(l.rstrip())
#         else:
#             line = l.rstrip().split(' ')
#             eles = [int(l) for l in line]
# f.close()


length = int(input())
eles = [int(i) for i in input().split()]

for i in range(length):
    val = eles[i]
    j = i - 1
    while j >= 0 and eles[j] > val:
        eles[j+1] = eles[j]
        j -= 1
    eles[j+1] = val
    print(*eles)
