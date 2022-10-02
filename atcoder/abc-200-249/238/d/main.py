# x + y = (x XOR y) + 2(x AND y)であることを利用して、連立方程式で解く。
# また、(x AND y) AND (x XOR y) = 0であることも利用する。

T = int(input())
for i in range(T):
    a, s = map(int, input().split())
    if (v := s - 2 * a) >= 0 and v & a == 0:
        print('Yes')
    else:
        print('No')