'''
高橋氏が青木氏より多く票を獲得するためには、高橋氏の得る票数を増やし、青木氏の得る票数を減らすことが重要です。 そこで、
X = (高橋氏の得る票数) − (青木氏の得る票数) と定義する
  ・i番目の街で演説をするとXは、2A+Bだけ増加する
  ・X > 0 になると高橋氏の勝利
'''

N = int(input())
X = 0
x = []
for i in range(N):
    A, B = map(int, input().split())
    X -= A
    x.append(A + A + B)
x.sort()
ans = 0
while X <= 0:
    X += x.pop()
    ans += 1
print(ans)
