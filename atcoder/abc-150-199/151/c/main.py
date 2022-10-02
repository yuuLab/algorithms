N, M = map(int, input().split())
questions =  [list(map(str, input().split())) for _ in range(M)]

ac = [False for _ in range(N)]
penalties = [0 for _ in range(N)]

for i in range(M):
    number = int(questions[i][0])
    answer = questions[i][1]
    if answer == 'WA' and not ac[number-1]:
        penalties[number-1] += 1
    else:
        ac[number-1] = True

answers = 0
penalty = 0
for i in range(N):
    if ac[i]:
        answers += 1
        penalty += penalties[i]
print(answers, penalty)