# @before-stub-for-debug-begin
from python3problem58 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    # split String -> LIST and return length the last word
    def lengthOfLastWord(self, s: str) -> int:
        s.strip()
        if s == "":
            return 0
        s = s.split(" ")
        for i in range(len(s) -1, -1, -1):
            if s[i] != "":
                return len(s[i])
        return 0
# @lc code=end

