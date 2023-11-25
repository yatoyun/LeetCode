#
# @lc app=leetcode id=1323 lang=python3
#
# [1323] Maximum 69 Number
#

# @lc code=start
class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        num = num.replace('6', '9', 1)
        
        return int(num)
# @lc code=end

