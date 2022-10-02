N = int(input())
A = list(map(int, input().split()))

# Ai - Ajが200の倍数であるということは、Aiを200で割ったあまりとAjを200で割った余りが一致すると言える。
N = int(input())
A = list(map(int, input().split()))

B = [a % 200 for a in A]
count_dict = {}
for b in B:
    if b in count_dict:
        count_dict[b] += 1
    else:
        count_dict[b] = 1
ans = 0
for val in count_dict.values():
    ans += (val * (val-1))//2
print(ans)