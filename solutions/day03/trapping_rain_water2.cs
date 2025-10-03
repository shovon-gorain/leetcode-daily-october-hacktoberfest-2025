using System;
using System.Collections.Generic;

public class Solution
{
    public int TrapRainWater(int[][] heightMap)
    {
        if (heightMap == null || heightMap.Length == 0 || heightMap[0].Length == 0)
        {
            return 0;
        }

        int rows = heightMap.Length;
        int cols = heightMap[0].Length;

        // Min-priority queue to store cells (height, row, col)
        // We want to process cells with lower heights first to simulate water flow
        var pq = new SortedSet<(int height, int r, int c)>();

        bool[,] visited = new bool[rows, cols];

        // Add all boundary cells to the priority queue
        // These are the "sources" from which water can potentially flow out
        for (int r = 0; r < rows; r++)
        {
            for (int c = 0; c < cols; c++)
            {
                if (r == 0 || r == rows - 1 || c == 0 || c == cols - 1)
                {
                    pq.Add((heightMap[r][c], r, c));
                    visited[r, c] = true;
                }
            }
        }

        int trappedWater = 0;
        int[] dr = { -1, 1, 0, 0 }; // Row offsets for neighbors
        int[] dc = { 0, 0, -1, 1 }; // Column offsets for neighbors

        while (pq.Count > 0)
        {
            // Get the cell with the smallest height from the priority queue
            var current = pq.Min;
            pq.Remove(current);

            int currentHeight = current.height;
            int r = current.r;
            int c = current.c;

            // Explore neighbors
            for (int i = 0; i < 4; i++)
            {
                int nr = r + dr[i];
                int nc = c + dc[i];

                // Check if the neighbor is within bounds and not visited
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && !visited[nr, nc])
                {
                    visited[nr, nc] = true;

                    // If the neighbor's height is less than the current "wall" height,
                    // water can be trapped there. The amount trapped is the difference.
                    if (heightMap[nr][nc] < currentHeight)
                    {
                        trappedWater += currentHeight - heightMap[nr][nc];
                        // The effective height of this neighbor becomes the currentHeight
                        // because water will rise to that level.
                        pq.Add((currentHeight, nr, nc));
                    }
                    else
                    {
                        // If the neighbor's height is greater or equal, it becomes a new "wall"
                        // for subsequent calculations.
                        pq.Add((heightMap[nr][nc], nr, nc));
                    }
                }
            }
        }

        return trappedWater;
    }
}
