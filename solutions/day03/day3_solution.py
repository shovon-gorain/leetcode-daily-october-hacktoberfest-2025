from heapq import heappush, heappop

class Solution:
    def trapRainWater(self, heightMap):
        # Edge case: if heightMap is empty or has no columns
        if not heightMap or not heightMap[0]:
            return 0

        ROWS, COLS = len(heightMap), len(heightMap[0])

        # Min-heap to store the boundary cells (height, row, col)
        # Start with all boundary cells since water can only be trapped inside
        min_heap = []
        for r in range(ROWS):
            for c in range(COLS):
                if r in (0, ROWS - 1) or c in (0, COLS - 1):
                    heappush(min_heap, (heightMap[r][c], r, c))
                    heightMap[r][c] = -1  # mark as visited

        # Result to store trapped water
        res = 0
        # Keep track of the maximum boundary height seen so far
        max_h = -1
        # Directions for exploring neighbors (up, down, left, right)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Process cells from the smallest boundary upwards
        while min_heap:
            h, r, c = heappop(min_heap)
            # Update maximum boundary height
            max_h = max(max_h, h)
            # Water trapped at this cell = max_h - current height
            res += max_h - h

            # Visit neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and heightMap[nr][nc] != -1:
                    # Push neighbor into heap
                    heappush(min_heap, (heightMap[nr][nc], nr, nc))
                    # Mark visited
                    heightMap[nr][nc] = -1  

        return res
