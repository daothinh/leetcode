# @before-stub-for-debug-begin
from python3problem66 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            #reverse digits -> add one -> reverse digits
            digits = digits[::-1]
            for i in range(0, len(digits)):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    return digits[::-1]
            digits.append(1)
            return digits[::-1]
            
# @lc code=end

