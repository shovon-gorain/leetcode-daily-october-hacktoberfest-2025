class Solution {
    public int trapRainWater(int[][] heightMap) {
          if (heightMap == null || heightMap.length == 0 || heightMap[0].length == 0) {
            return 0;
        }
        
        int m = heightMap.length;
        int n = heightMap[0].length;
        boolean[][] visited = new boolean[m][n];
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[2]));
        
       
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 || i == m - 1 || j == 0 || j == n - 1) {
                    pq.offer(new int[]{i, j, heightMap[i][j]});
                    visited[i][j] = true;
                }
            }
        }
        
        int ans = 0;
        int[][] direc = {{1,0}, {-1,0}, {0,1}, {0,-1}};
        
        while (!pq.isEmpty()) {
            int[] cell = pq.poll();
            int row = cell[0], col = cell[1], height = cell[2];
            
            for (int[] dir : direc) {
                int r = row + dir[0];
                int c = col + dir[1];
                
                if (r >= 0 && r < m && c >= 0 && c < n && !visited[r][c]) {
                    visited[r][c] = true;
                    
                    ans += Math.max(0, height - heightMap[r][c]);
                    
                    pq.offer(new int[]{r, c, Math.max(heightMap[r][c], height)});
                }
            }
        }
        return ans;
    }
}


