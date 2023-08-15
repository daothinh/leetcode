#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    #Add nums2 to nums1 and sort nums1
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for index in range(n):
            nums1[m + index] = nums2[index]
        nums1.sort()
        
# @lc code=end

