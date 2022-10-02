from collections import deque

N = int(input())
a = list(map(int, input().split()))

# [n, m]=[ボールの整数, 個数]の形で管理する。
q = deque([])
# 現在のボールの総個数
ans = 0

for i in range(N):
    num = a[i]
    # キューが空なら新規で追加
    if len(q) == 0:
        q.append([num, 1])
        ans += 1
        print(ans)
        continue
    
    # 一つ前のボールを取り出す
    pre_num, count = q.pop()
    if num == pre_num:
        if count + 1 < num:
            q.append([num, count+1])
            ans += 1
        else:
            # 一定個数連続したら削除し、キューにも戻さない。
            ans -= count
    else:
        # 取り出したボールを戻し、新しいボールも加える。
        q.append([pre_num, count])
        q.append([num, 1])
        ans += 1
    print(ans)

    