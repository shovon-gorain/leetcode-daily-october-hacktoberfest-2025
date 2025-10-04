"""
Day 04 – Container With Most Water

Problem Statement:
------------------
You are given an integer array height of length n. There are n vertical lines drawn such that 
the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container 
contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
----------
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The maximum area is formed between lines at indices 1 and 8, 
giving area = min(8,7) * (8-1) = 49.

Example 2:
----------
Input: height = [1,1]
Output: 1

Constraints:
------------
- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4


Approach:
---------
This is a classic two-pointer problem.
- The water contained depends on the shorter of the two lines.
- To maximize area, we try widest possible container (left=0, right=n-1).
- At each step:
  - Compute area = min(height[left], height[right]) * (right - left).
  - Update max_area if larger.
  - Move the pointer with the smaller height inward, 
    since only this can potentially increase area.

Algorithm:
1. Initialize two pointers: left=0, right=n-1.
2. While left < right:
   - Compute area.
   - Update max_area.
   - Move pointer at smaller height inward.
3. Return max_area.

Complexity:
-----------
- Time: O(n) [each pointer moves at most n steps]
- Space: O(1) [only variables used]

"""

class Solution:
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            width = right - left
            current_area = min(height[left], height[right]) * width
            max_area = max(max_area, current_area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area


# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxArea([1,8,6,2,5,4,8,3,7]))  # Expected: 49
    print(sol.maxArea([1,1]))                # Expected: 1
