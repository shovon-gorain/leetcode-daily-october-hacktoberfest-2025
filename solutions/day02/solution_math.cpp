#include<bits/stdc++.h>
using namespace std;

//This solution uses a mathematical approach to calculate the maximum number of bottles that can be drunk, which
//can be derived from solving the recurrence relation used in the recursive solution.

class Solution {
public:
    int maxBottlesDrunk(int n, int k) {
        return n+((-2*k+3+sqrt(4*k*k+8*n-12*k+1))/2);
    }
};
