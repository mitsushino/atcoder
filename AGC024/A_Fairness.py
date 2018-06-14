A, B, C, K = map(int, input().split())

tmp_A = B + C
tmp_B = A + C
if abs(tmp_A - tmp_B) > (10 ** 18):
    print('Unfair')
else:
    if K % 2 == 1:
        print(tmp_A - tmp_B)
    else:
        print(tmp_B - tmp_A)