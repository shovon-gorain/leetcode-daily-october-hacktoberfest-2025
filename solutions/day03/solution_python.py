"""
Day 03 – Trapping Rain Water II

Problem Statement:
------------------
Given an m x n integer matrix heightMap representing the height of each unit cell 
in a 2D elevation map, return the volume of water it can trap after raining.

Example 1:
----------
Input:
heightMap = [[1,4,3,1,3,2],
             [3,2,1,3,2,4],
             [2,3,3,2,3,1]]

Output:
4

Example 2:
----------
Input:
heightMap = [[3,3,3,3,3],
             [3,2,2,2,3],
             [3,2,1,2,3],
             [3,2,2,2,3],
             [3,3,3,3,3]]

Output:
10

Constraints:
------------
- m == heightMap.length
- n == heightMap[i].length
- 1 <= m, n <= 200
- 0 <= heightMap[i][j] <= 2 * 10^4


Approach:
---------
This is a 2D version of the classic "Trapping Rain Water" problem.
- Water is trapped only if surrounded by higher boundaries in all directions.
- To simulate this, we use a priority queue (min-heap) to process cells in order 
  of their height, starting from the boundary.

Algorithm:
1. Push all boundary cells into the min-heap and mark them visited.
2. Repeatedly pop the lowest cell from the heap.
3. For each neighbor:
   - If it's not visited:
     - If neighbor height < current boundary height, water is trapped.
     - Update neighbor’s effective boundary height as max(neighbor, boundary).
     - Push into heap and mark visited.
4. Continue until all cells are processed.

Complexity:
-----------
- Time: O(m * n * log(m * n))  [each cell pushed/popped from heap once]
- Space: O(m * n)  [visited matrix + heap]

"""

import heapq

def trapRainWater(heightMap):
    if not heightMap or not heightMap[0]:
        return 0

    m, n = len(heightMap), len(heightMap[0])
    visited = [[False] * n for _ in range(m)]
    heap = []

    # Step 1: Add all boundary cells into min-heap
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                heapq.heappush(heap, (heightMap[i][j], i, j))
                visited[i][j] = True

    trapped_water = 0
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    # Step 2: Process heap
    while heap:
        h, x, y = heapq.heappop(heap)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                # If neighbor is lower, trap water
                if heightMap[nx][ny] < h:
                    trapped_water += h - heightMap[nx][ny]
                # Update boundary height
                heapq.heappush(heap, (max(heightMap[nx][ny], h), nx, ny))

    return trapped_water


import heapq
from typing import List

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
