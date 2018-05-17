import sys

A, B = map(int, input().split())
S = input()

if '-' in S[:A]:
    print('No')
    sys.exit()

if S[A] != '-':
    print('No')
    sys.exit()

if '-' in S[A + 1:]:
    print('No')
    sys.exit()

print('Yes')