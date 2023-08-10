# @before-stub-for-debug-begin
from python3problem28 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        if len(needle) > len(haystack):
            return -1
        for i in range(0, len(haystack) - len(needle) + 1, 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
        
# @lc code=end


#leetcode = 8
#leeto = 5
# 3
