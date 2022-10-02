N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

for i in range(P, Q + 1):
    text = ''
    for j in range(R, S + 1):
        # 黒になる場合を考える。
        if (i - j - A + B == 0) or (i - A - B + j == 0):
            text += '#'
        else:
            text += '.'
    print(text)