"""
                Container With Most Water (LeetCode 11)

Problem Statement: You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Optimal Approach (Two Pointers):
- Use two pointers, one at the beginning and one at the end.
- Calculate the water area formed by these two lines.
- Move the pointer pointing to the shorter line inward (since the smaller line limits the height of water).
- Repeat until both pointers meet.
- Keep track of the maximum area found.

Complexity Analysis:
Time Complexity: O(n)
where n = number of vertical lines, i.e., the length of the input array height
Space Complexity: O(1)

Constraints:
n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:
Input: height = [1,1]
Output: 1
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            area = width * min(height[left], height[right])
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

"""
class Solution(object):
Defines a class Solution.

On LeetCode, you are required to implement your solution as a method inside this class.

    def maxArea(self, height):
        #:type height: List[int]
        #:rtype: int

Defines a method maxArea that takes height as input.
height is a list of integers representing the heights of vertical lines.
:rtype: int means the function will return an integer — the maximum area of water.

        left, right = 0, len(height) - 1
Initializes two pointers:

left → points to the first line (index 0).
right → points to the last line (index len(height) - 1).
These pointers will move toward each other to check all possible containers.

        max_area = 0
max_area stores the maximum water area found so far.
Initially set to 0 because we haven’t calculated any areas yet.

        while left < right:
Loop continues until the two pointers meet.
left < right ensures we always have at least two lines to form a container.

            width = right - left
Calculates the width of the container.
Distance between the two lines is right - left.

            area = width * min(height[left], height[right])
Calculates the area of water the current container can hold:

Area = width × height of shorter line
Area = width×height of shorter line
min(height[left], height[right]) ensures we don’t “overflow” the water beyond the shorter line.

            max_area = max(max_area, area)
Updates max_area if the current area is bigger than the previous maximum.
Ensures we always keep track of the largest area found.

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
Moves the pointer pointing to the smaller line inward.
Why? Because the shorter line limits the water height.
By moving it, we try to find a taller line that can potentially increase the area.
If the heights are equal, moving either pointer works — here, we move right.

        return max_area
Returns the maximum area found after checking all possibilities.
"""

