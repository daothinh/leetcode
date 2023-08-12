# @before-stub-for-debug-begin
from python3problem67 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    # explain code:
    # 1. res = "" is the result string
    # 2. carry = 0 is the carry bit
    # 3. i = len(a) - 1 and j = len(b) - 1 are the index of a and b
    # 4. while i >= 0 or j >= 0 or carry: is the loop condition
    # 5. if i >= 0: carry += int(a[i]) and i -= 1 are the operation of a
    # 6. if j >= 0: carry += int(b[j]) and j -= 1 are the operation of b
    # 7. res = str(carry % 2) + res is the operation of res
    # 8. carry //= 2 is the operation of carry
    # 9. return res is the result

    def addBinary(self, a: str, b: str) -> str:
        res = ""
        i = len(a) - 1
        j = len(b) - 1
        carry = 0

        while i >= 0 or j >=0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            res = str(carry % 2) + res
            carry //= 2
            
        return res

# @lc code=end

