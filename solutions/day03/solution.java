class Solution {
    private int[][] directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    
    public int trapRainWater(int[][] heightMap) {
        if (heightMap == null || heightMap.length == 0) return 0;
        
        int rows = heightMap.length;
        int cols = heightMap[0].length;
        
        PriorityQueue<int[]> minHeap = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        boolean[][] visited = new boolean[rows][cols];
        
        for (int row = 0; row < rows; row++) {
            minHeap.offer(new int[]{heightMap[row][0], row, 0});
            minHeap.offer(new int[]{heightMap[row][cols - 1], row, cols - 1});
            visited[row][0] = visited[row][cols - 1] = true;
        }
        
        for (int col = 1; col < cols - 1; col++) {
            minHeap.offer(new int[]{heightMap[0][col], 0, col});
            minHeap.offer(new int[]{heightMap[rows - 1][col], rows - 1, col});
            visited[0][col] = visited[rows - 1][col] = true;
        }
        
        int totalWater = 0;
        
        while (!minHeap.isEmpty()) {
            int[] cell = minHeap.poll();
            int height = cell[0], row = cell[1], col = cell[2];
            
            for (int[] dir : directions) {
                int newRow = row + dir[0];
                int newCol = col + dir[1];
                
                if (newRow >= 0 && newRow < rows && 
                    newCol >= 0 && newCol < cols && 
                    !visited[newRow][newCol]) {
                    
                    totalWater += Math.max(0, height - heightMap[newRow][newCol]);
                    minHeap.offer(new int[]{Math.max(height, heightMap[newRow][newCol]), newRow, newCol});
                    visited[newRow][newCol] = true;
                }
            }
        }
        
        return totalWater;
    }
}