/*
Problem Statement: Trapping Rain Water II (LeetCode 407)
Given a 2D elevation map (m x n) where each cell represents height, 
calculate how much water can be trapped after raining.

Optimal Approach:
- Treat the problem like filling water from the lowest boundary.
- Use a min-heap to always process the lowest boundary cell first.
- Start with all boundary cells in the heap and mark them visited.
- For each cell taken from the heap, look at its 4 neighbors:
    - If neighbor is lower, water is trapped there.
    - Push neighbor into heap with updated height = max(current boundary, neighbor height)

Constraints:
m == heightMap.length
n == heightMap[i].length
1 <= m, n <= 200
0 <= heightMap[i][j] <= 2 * 104
*/

/**
 * @param {number[][]} heightMap
 * @return {number}
 */
var trapRainWater = function(heightMap) {
    const m = heightMap.length;
    const n = heightMap[0].length;
    
    if (m <= 2 || n <= 2) return 0;

    const visited = Array.from({ length: m }, () => Array(n).fill(false));
    const heap = [];

    const push = (cell) => {
        heap.push(cell);
        let i = heap.length - 1;
        while (i > 0) {
            const parent = Math.floor((i - 1) / 2);
            if (heap[parent][0] <= heap[i][0]) break;
            [heap[parent], heap[i]] = [heap[i], heap[parent]];
            i = parent;
        }
    };

    const pop = () => {
        if (heap.length === 1) return heap.pop();
        const top = heap[0];
        heap[0] = heap.pop();
        let i = 0;
        while (true) {
            let smallest = i;
            const left = 2 * i + 1;
            const right = 2 * i + 2;
            if (left < heap.length && heap[left][0] < heap[smallest][0]) smallest = left;
            if (right < heap.length && heap[right][0] < heap[smallest][0]) smallest = right;
            if (smallest === i) break;
            [heap[i], heap[smallest]] = [heap[smallest], heap[i]];
            i = smallest;
        }
        return top;
    };

    for (let i = 0; i < m; i++) {
        push([heightMap[i][0], i, 0]);
        push([heightMap[i][n - 1], i, n - 1]);
        visited[i][0] = true;
        visited[i][n - 1] = true;
    }
    for (let j = 1; j < n - 1; j++) {
        push([heightMap[0][j], 0, j]);
        push([heightMap[m - 1][j], m - 1, j]);
        visited[0][j] = true;
        visited[m - 1][j] = true;
    }

    const dirs = [[1,0], [-1,0], [0,1], [0,-1]];
    let water = 0;

    while (heap.length > 0) {
        const [h, r, c] = pop();
        for (const [dr, dc] of dirs) {
            const nr = r + dr, nc = c + dc;
            if (nr >= 0 && nr < m && nc >= 0 && nc < n && !visited[nr][nc]) {
                visited[nr][nc] = true;
                water += Math.max(0, h - heightMap[nr][nc]);
                push([Math.max(h, heightMap[nr][nc]), nr, nc]);
            }
        }
    }

    return water;
};

// Sample Input Test Case:
const heightMap = [
    [1, 4, 3, 1, 3, 2],
    [3, 2, 1, 3, 2, 4],
    [2, 3, 3, 2, 3, 1]
];

console.log(trapRainWater(heightMap)); // Output: 4


/*
Examples
1. Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
Output: 4
Explanation: After the rain, water is trapped between the blocks.
We have two small ponds 1 and 3 units trapped.
The total volume of water trapped is 4.

2. Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
Output: 10
*/

/*
Complexity Analysis:

Time Complexity: O(m * n * log(m * n))
- m = number of rows, n = number of columns
- Each cell is processed once, each heap operation takes log(m * n)

Space Complexity: O(m * n)
- Visited matrix + heap can store up to m*n elements
*/


