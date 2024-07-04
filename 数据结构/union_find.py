class UnionFind:
    def __init__(self):
        self.parent = {}
        self.size = {}

    def find(self, x):
        """
        查找元素 x 的根节点，并应用路径压缩优化。
        路径压缩是通过递归地将x的所有祖先节点直接连接到根节点，从而使得树的高度尽可能低。
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 路径压缩
        return self.parent[x]

    def union(self, x, y):
        """
        合并元素 x 和 y 所在的集合。
        按秩合并（这里的“秩”是树的大小）通过始终将较小的树连接到较大的树上，从而保持树的高度尽可能低。
        """
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.size[rootX] < self.size[rootY]:
                self.parent[rootX] = rootY
                self.size[rootY] += self.size[rootX]
            else:
                self.parent[rootY] = rootX
                self.size[rootX] += self.size[rootY]

    def add(self, x):
        """
        添加新元素 x，初始化其父节点为它自身，大小为 1。
        """
        if x not in self.parent:
            self.parent[x] = x
            self.size[x] = 1