#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int x, y, height;
} Cell;

typedef struct {
    Cell *data;
    int size, capacity;
} MinHeap;

// ---------- Min-Heap functions ----------
MinHeap* createHeap(int capacity) {
    MinHeap *heap = (MinHeap*)malloc(sizeof(MinHeap));
    heap->data = (Cell*)malloc(sizeof(Cell) * capacity);
    heap->size = 0;
    heap->capacity = capacity;
    return heap;
}

void swap(Cell *a, Cell *b) {
    Cell tmp = *a;
    *a = *b;
    *b = tmp;
}

void heapifyUp(MinHeap *heap, int idx) {
    while (idx > 0) {
        int parent = (idx - 1) / 2;
        if (heap->data[parent].height > heap->data[idx].height) {
            swap(&heap->data[parent], &heap->data[idx]);
            idx = parent;
        } else break;
    }
}

void heapifyDown(MinHeap *heap, int idx) {
    int left, right, smallest;
    while (1) {
        left = 2 * idx + 1;
        right = 2 * idx + 2;
        smallest = idx;
        if (left < heap->size && heap->data[left].height < heap->data[smallest].height)
            smallest = left;
        if (right < heap->size && heap->data[right].height < heap->data[smallest].height)
            smallest = right;
        if (smallest != idx) {
            swap(&heap->data[smallest], &heap->data[idx]);
            idx = smallest;
        } else break;
    }
}

void push(MinHeap *heap, Cell c) {
    heap->data[heap->size] = c;
    heapifyUp(heap, heap->size);
    heap->size++;
}

Cell pop(MinHeap *heap) {
    Cell top = heap->data[0];
    heap->size--;
    heap->data[0] = heap->data[heap->size];
    heapifyDown(heap, 0);
    return top;
}

// ---------- Main function ----------
int trapRainWater(int** heightMap, int heightMapSize, int* heightMapColSize) {
    if (heightMapSize == 0 || heightMapColSize[0] == 0) return 0;

    int m = heightMapSize, n = heightMapColSize[0];
    int visited[m][n];
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            visited[i][j] = 0;

    MinHeap *heap = createHeap(m * n);

    // Add boundary cells to heap
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (i == 0 || i == m - 1 || j == 0 || j == n - 1) {
                push(heap, (Cell){i, j, heightMap[i][j]});
                visited[i][j] = 1;
            }
        }
    }

    int dirs[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
    int trapped = 0;

    while (heap->size > 0) {
        Cell cell = pop(heap);
        for (int d = 0; d < 4; d++) {
            int nx = cell.x + dirs[d][0];
            int ny = cell.y + dirs[d][1];
            if (nx >= 0 && nx < m && ny >= 0 && ny < n && !visited[nx][ny]) {
                visited[nx][ny] = 1;
                trapped += (cell.height > heightMap[nx][ny]) ? (cell.height - heightMap[nx][ny]) : 0;
                // push neighbor with updated height
                int newHeight = (heightMap[nx][ny] > cell.height) ? heightMap[nx][ny] : cell.height;
                push(heap, (Cell){nx, ny, newHeight});
            }
        }
    }

    free(heap->data);
    free(heap);
    return trapped;
}