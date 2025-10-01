#include <bits/stdc++.h>
using namespace std;

int main() {
    // Input: example array
    vector<int> nums = {1, 2, 2, 3, 3, 3};

    // Logic: count frequencies
    map<int, int> freq;
    for (int x : nums) freq[x]++;

    // Output
    for (auto p : freq) {
        cout << p.first << " -> " << p.second << endl;
    }

    return 0;
}

