#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
import os

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return os.path.commonprefix(strs)
# @lc code=end

