# @before-stub-for-debug-begin
from python3problem35 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start


class Solution:
    # search binary tree
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while (start <= end):
            mid = (end - start) // 2 + start
            if (nums[mid] == target):
                return mid
            elif (nums[mid] > target):
                end = mid - 1
            else:
                start = mid + 1
        return start

'''     
        start = 0
        end = len(nums) - 1
        while (start <= end):
            mid = (end - start) // 2 + start
            if (nums[mid] == target):
                return mid
            elif (nums[mid] > target):
                end = mid - 1
            else:
                start = mid + 1
        return start
'''
'''
        for i in range(len(nums)):
            if (nums[i] >= target):
                return i
        return len(nums)
'''

    
# @lc code=end

