class union_find(object):
    def __init__(self, size):
        self.f = [-1] * size
    
    def get_father(self, x):
        if self.f[x] == x:
            return x
        self.f[x] = self.get_father(self.f[x])
        return self.f[x]

    def merge(self, x, y):
        if self.f[x] == -1:
            return False
        if self.f[y] == -1:
            return False
        x = self.get_father(x)
        y = self.get_father(y)
        if x == y:
            return False
        else:
            self.f[x] = y
            return True

class Solution(object):
    def numIslands2(self, m, n, positions):
        count = 0
        result = []
        uf = union_find(m * n)
        for position in positions:
            i, j = position[0], position[1]
            cur = i * n + j
            uf.f[cur] = cur
            count += 1
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for d in directions:
                x, y = i + d[0], j + d[1]
                if 0 <= x < m and  0 <= y < n and uf.merge(cur, x * n + y):
                    count -= 1
            result.append(count)
        return result

        