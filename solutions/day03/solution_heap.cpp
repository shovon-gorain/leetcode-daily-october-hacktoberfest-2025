// Day 3: Trapping Rain Water II (LeetCode Hard)
// Heap-based C++ Solution using Priority Queue with custom comparator

#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    struct Compare {
        bool operator()(const pair<int,pair<int,int>>& a,
                        const pair<int,pair<int,int>>& b) const {
            return a.first > b.first; 
        }
    };
    int trapRainWater(vector<vector<int>>& height) {
        int m = height.size();
        int n = height[0].size();
        int water = 0;
        vector<vector<bool>>vis(m, vector<bool>(n,false));
        priority_queue<pair<int,pair<int,int>>,vector<pair<int,pair<int,int>>>,Compare>pq;
        for(int i =0;i<m;i++){
            pq.push({height[i][0],{i,0}});
            vis[i][0] = true;
            pq.push({height[i][n-1],{i,n-1}});
            vis[i][n-1] = true;
        }
        for(int j = 1;j<n-1;j++){
            pq.push({height[0][j],{0,j}});
            vis[0][j] = true;
            pq.push({height[m-1][j],{m-1,j}});
            vis[m-1][j] = true;
        }
        int rows[] = {0,1,0,-1};
        int cols[] = {1,0,-1,0};
        while(!pq.empty()){
            auto topp = pq.top();
            pq.pop();
            int cell = topp.first;
            int row = topp.second.first;
            int col = topp.second.second;
            for(int i =0;i<4;i++){
                int r = row + rows[i];
                int c = col + cols[i];
                if(r<m && c<n && r>=0 && c>=0 && vis[r][c] == false){
                    if(height[r][c]<cell){
                        water += cell - height[r][c];
                    }
                    pq.push({max(height[r][c],cell),{r,c}});
                    vis[r][c] = true;
                }
            }
        }
        return water;

    }
};