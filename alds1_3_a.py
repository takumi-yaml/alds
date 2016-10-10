import re

stack = []
_l = input().split(' ')

for c in _l:
    if re.match(r"(\+|\-|\/|\*)", c):
        f = stack.pop()
        z = stack.pop()
        stack.append(eval("{}{}{}".format(z, c, f)))
    else:
        stack += [c]

print(stack[0])
