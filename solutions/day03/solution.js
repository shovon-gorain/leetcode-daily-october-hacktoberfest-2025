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

class MinHeap {
    constructor() {
        this.heap = [];
    }

    push(cell) {
        this.heap.push(cell);
        this.bubbleUp(this.heap.length - 1);
    }

    pop() {
        if (this.heap.length === 1) return this.heap.pop();
        const top = this.heap[0];
        this.heap[0] = this.heap.pop();
        this.bubbleDown(0);
        return top;
    }

    bubbleUp(index) {
        while (index > 0) {
            const parent = Math.floor((index - 1) / 2);
            if (this.heap[parent][0] <= this.heap[index][0]) break;
            [this.heap[parent], this.heap[index]] = [this.heap[index], this.heap[parent]];
            index = parent;
        }
    }

    bubbleDown(index) {
        const n = this.heap.length;
        while (true) {
            let smallest = index;
            const left = 2 * index + 1;
            const right = 2 * index + 2;

            if (left < n && this.heap[left][0] < this.heap[smallest][0]) smallest = left;
            if (right < n && this.heap[right][0] < this.heap[smallest][0]) smallest = right;
            if (smallest === index) break;

            [this.heap[smallest], this.heap[index]] = [this.heap[index], this.heap[smallest]];
            index = smallest;
        }
    }

    size() {
        return this.heap.length;
    }
}

function trapRainWater(heightMap) {
    const rows = heightMap.length;
    const cols = heightMap[0].length;

    if (rows <= 2 || cols <= 2) return 0;

    const visited = Array.from({ length: rows }, () => Array(cols).fill(false));
    const minHeap = new MinHeap();

    for (let row = 0; row < rows; row++) {
        minHeap.push([heightMap[row][0], row, 0]);
        minHeap.push([heightMap[row][cols - 1], row, cols - 1]);
        visited[row][0] = true;
        visited[row][cols - 1] = true;
    }
    for (let col = 1; col < cols - 1; col++) {
        minHeap.push([heightMap[0][col], 0, col]);
        minHeap.push([heightMap[rows - 1][col], rows - 1, col]);
        visited[0][col] = true;
        visited[rows - 1][col] = true;
    }

    const directions = [
        [1, 0],   
        [-1, 0], 
        [0, 1],   
        [0, -1]   
    ];

    let waterTrapped = 0;

    while (minHeap.size() > 0) {
        const [currentHeight, row, col] = minHeap.pop();

        for (const [dRow, dCol] of directions) {
            const neighborRow = row + dRow;
            const neighborCol = col + dCol;

            if (
                neighborRow >= 0 && neighborRow < rows &&
                neighborCol >= 0 && neighborCol < cols &&
                !visited[neighborRow][neighborCol]
            ) {
                visited[neighborRow][neighborCol] = true;
                waterTrapped += Math.max(0, currentHeight - heightMap[neighborRow][neighborCol]);                minHeap.push([
                    Math.max(currentHeight, heightMap[neighborRow][neighborCol]),
                    neighborRow,
                    neighborCol ])
            }
        }
    }
    return waterTrapped;
}

// Sample Input Case
const heightMap = [
    [1, 4, 3, 1, 3, 2],
    [3, 2, 1, 3, 2, 4],
    [2, 3, 3, 2, 3, 1]
];

console.log("Total water trapped:", trapRainWater(heightMap)); // Output: 4

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


