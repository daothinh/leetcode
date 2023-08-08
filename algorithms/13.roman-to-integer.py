# @before-stub-for-debug-begin
from python3problem13 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start


class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        res = 0
        for i in range(len(s)):
            # compare current and next
            # if current < nextnum, then subtract
            # else add
            if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
                res -= m[s[i]]
            else:
                res += m[s[i]]
        return res

# @lc code=end

# XI = 10 + 1
# IX = 10 - 1

