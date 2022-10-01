## Python atcoder 基本技法

#### 標準入力

```python
n = int(input())
a, b, c = map(int, input().split())

lis = list(map(int, input().split()))
se = set(input().split())

two_dimensions = [list(map(int, input().split())) for _ in range(n)]
```

#### List の展開

```python
L = [2, 2, 4, 4, 8]
print(*L)

# 2 2 4 4 8
```

#### List or Set

python で集合の中に属することを比較する場合は、set を使用した方が速度が上がる。(HashTable を使用するため)

```python
s = input().split()
t = set(input().split())
for x in s:
    print("Yes" if x in t else "No")
```
