
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        heap = []
        for j in range(n):
            heap.append((matrix[0][j], 0, j))
        heapq.heapify(heap)
        i = 0
        while i < k - 1:
            cur = heapq.heappop(heap)
            x, y = cur[1], cur[2]
            if x + 1 < m:
                heapq.heappush(heap, (matrix[x + 1][y], x + 1, y))
            i += 1
        return heap[0][0]
        