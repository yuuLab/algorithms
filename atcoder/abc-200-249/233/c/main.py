from sys import setrecursionlimit

setrecursionlimit(10 ** 7)

def dfs(bag_i: int, total: int):
    # bag_i番目の袋からボールを選ぶ
    
    # すべての袋から1つずつボールを選び終わった場合
    if bag_i == N:
        return 1 if total == X else 0

    # まだボールを選んでいない袋がある場合
    cnt = 0
    for ball in bags[bag_i]:
        cnt += dfs(bag_i + 1, total * ball)
    return cnt


N, X = map(int, input().split())
bags = [list(map(int, input().split()[1:])) for _ in range(N)]


print(dfs(0, 1))