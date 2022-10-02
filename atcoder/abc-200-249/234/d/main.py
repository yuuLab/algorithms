import heapq

N, K = map(int, input().split())
P = list(map(int, input().split()))

que = P[:K]
heapq.heapify(que)
print(min(que))
for i in range(K, N):
    p = P[i]
    minima = heapq.heappop(que)
    # 最小値を取り出し、次の値と比較し、大きい方を優先度付きキューに戻す
    minima = max(p, minima)
    heapq.heappush(que, minima)
    # 最小値をキューから再び取り出す
    ans = heapq.heappop(que)
    print(ans)
    # キューに戻す
    heapq.heappush(que, ans)