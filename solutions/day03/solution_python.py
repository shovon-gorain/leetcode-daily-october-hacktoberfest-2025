import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = []

        # Step 1: push all boundary cells into heap
        for i in range(m):
            for j in [0, n - 1]:
                heapq.heappush(heap, (heightMap[i][j], i, j))
                visited[i][j] = True
        for j in range(n):
            for i in [0, m - 1]:
                if not visited[i][j]:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True

        trapped_water = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # Step 2: BFS with min-heap
        while heap:
            height, x, y = heapq.heappop(heap)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    # if neighbor is lower, water is trapped
                    trapped_water += max(0, height - heightMap[nx][ny])
                    # push the effective height into heap
                    heapq.heappush(heap, (max(heightMap[nx][ny], height), nx, ny))

        return trapped_water
