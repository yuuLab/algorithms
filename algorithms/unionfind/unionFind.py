
class UnionFind:
    
    def __init__(self, n: int):
        # ノード数 n
        self.n = n
        # ノード数で初期化
        # rankは木の高さを表す
        self.parents = []
        self.rank = []
        for i in range(n):
            self.parents.append(i)
            self.rank.append(0)


    def find(self, x: int) -> int:
        """
        データxが属するグループ(木の根)を再帰で取得する。
        parents[x] == x であるとき、xは木の根である。
        """
        if self.parents[x] == x:
            return x

        # 効率化のため辺の圧縮を行い、木の根まで再帰。
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
         
         
    def unite(self, x: int, y: int):
        x = self.find(x)
        y = self.find(y)
        # 同グループ
        if x == y:
            return
        
        # 効率化のためランクが小さいものから大きいものへ結合する
        if self.rank[x] < self.rank[y]:
            self.parents[x] =y
        else:
            self.parents[y] = x
            # 高さが同じ場合、結合された方の高さを加算
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
        
        
    def is_same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
    
    
    def size(self, x: int) -> int:
        return -self.parents[self.find(x)]