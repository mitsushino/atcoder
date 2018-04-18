import sys


def plus_or_minus(opr1, opr2, op):
    if op == '+':
        return opr1 + opr2
    else:
        return opr1 - opr2


A, B, C, D = map(int, list(input()))

op = ['+', '-']

for i in range(2):
    for j in range(2):
        for k in range(2):
            o2 = plus_or_minus(A, B, op[i])
            o3 = plus_or_minus(o2, C, op[j])
            o4 = plus_or_minus(o3, D, op[k])
            if o4 == 7:
                print('{}{}{}{}{}{}{}=7'.format(A, op[i], B, op[j], C, op[k], D))
                sys.exit()