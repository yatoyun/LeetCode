#
# @lc app=leetcode id=2485 lang=python3
#
# [2485] Find the Pivot Integer
#

# @lc code=start
class Solution:
    def pivotInteger(self, n: int) -> int:
        sum_1toN = n * (n+1) / 2
        left_num = 0
        pivot_integer = -1
        
        if n == 1:
            return 1
        
        for i in range(n,0,-1):
            if left_num >= sum_1toN / 2:
                pivot_integer = i + 1
                break
            
            left_num += i
        
        if left_num != pivot_integer*(pivot_integer+1) / 2:
            pivot_integer = -1
        
        return pivot_integer
        

# @lc code=end

