# @before-stub-for-debug-begin
from python3problem70 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    # 
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        else:
            a = 2
            b = 3
            for i in range(4, n + 1):
                c = a + b
                a = b
                b = c
            return c
        
# @lc code=end
