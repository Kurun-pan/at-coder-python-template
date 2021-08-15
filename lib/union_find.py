class UnionFind():
    def __init__(self, n):
        self.n = n
        self.roots = [-1] * (n + 1)

    def find_root(self, x):
        if self.roots[x] < 0:
            return x
        self.roots[x] = self.find_root(self.roots[x])
        return self.roots[x]

    def unite(self, x, y):
        x = self.find_root(x)
        y = self.find_root(y)
        if x == y:
            return

        # 小さいグループを大きいグループに統合する
        if self.roots[x] < self.roots[y]:
            x, y = y, x
        self.roots[x] += self.roots[y]
        self.roots[y] = x

    def is_same_group(self, x, y):
        return self.find_root(x) == self.find_root(y)

    def size(self, x):
        return -self.roots[self.find_root(x)]
 