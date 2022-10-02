# グラフとみなし、閉路があれば並べることはできない。また、同じ数字が3回出現した場合も並べることは不可。
# UnionFindで解く

class UnionFind:
    
    def __init__(self, n: int):
        # ノード数
        self.n = n
        # ノード数で初期化
        # rankは木の高さを表す
        self.parent = []
        self.rank = []
        for i in range(n):
            self.parent.append(i)
            self.rank.append(0)
            
    def find(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
         
    def unite(self, x: int, y: int):
        x = self.find(x)
        y = self.find(y)
        # 同グループ
        if x == y:
            return
        
        # 効率化のためランクが小さいものから大きいものへ結合する
        if self.rank[x] < self.rank[y]:
            self.parent[x] =y
        else:
            self.parent[y] = x
            # 高さが同じ場合、結合された方の高さを加算
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
        
    def is_same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
    
    def size(self, x: int) -> int:
        return -self.parent[self.root(x)]
    
    
def judge():
    N, M = map(int, input().split())
    uf = UnionFind(N)
    C = [0] * N  
    for _ in range(M):
        a, b = map(int, input().split())
        a, b = a - 1, b - 1
        if uf.is_same(a, b): 
            return False
        uf.unite(a, b)
        C[a] += 1
        C[b] += 1
        
        if C[a] >= 3 or C[b] >= 3:
            return False

    return True

print("Yes" if judge() else "No")