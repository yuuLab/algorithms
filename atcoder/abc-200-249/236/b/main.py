N = int(input())
cards = list(map(int, input().split()))

cards.sort()
ans = -1
answer = list()
for i in range(0, N*4-1, 4):
    if cards[i-1] != cards[i-2] and i != 0:
        ans = cards[i-2]
        print(cards[i-2])
        break
if ans == -1:
    print(cards[-1])