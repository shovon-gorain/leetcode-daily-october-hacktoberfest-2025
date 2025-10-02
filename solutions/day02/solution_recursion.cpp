#include<bits/stdc++.h>
using namespace std;

// This solution uses recursion to calculate the maximum number of bottles that can be drunk
class Solution {
public:
    static int exchange(int n, int k){
        if (n<k) return 0;
        return 1+exchange(n-k+1, k+1);
    }
    static int maxBottlesDrunk(int n, int k) {
        return n+exchange(n, k);
    }
};
