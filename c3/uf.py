class Unionfind:
    def __init__(self, n):
        self.parents = [-1]*n

    def size(self, v):
        i = self.find(v)
        size = abs(self.parents[i])
        return size

    def connected(self, v1, v2):
        return self.find(v1) == self.find(v2)
        
    def find(self, v):
        r = v
        while(self.parents[r] >= 0):
            r = self.parents[r]
        return r

    def union(self, v1, v2):
        size1 = self.size(v1)
        size2 = self.size(v2)
        root1 = self.find(v1)
        root2 = self.find(v2)
        if (root1 != root2 or (root1 == -1 and root2 == -1)):
            if size1<=size2:
                self.parents[root1] = root2
                self.parents[root2] -= size1
            else:
                self.parents[root2] = root1
                self.parents[root1] -= size2


if __name__ == '__main__':
    uf = Unionfind(5)
    print(uf.size(3))
    print(uf.connected(2,3))
    uf.union(2,3)
    print(uf.size(3))
    print(uf.connected(2,3))