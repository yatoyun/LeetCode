#
# @lc app=leetcode id=600 lang=python3
#
# [600] Non-negative Integers without Consecutive Ones
#

# @lc code=start
class Solution:
    def findIntegers(self, n: int) -> int:
        fib = [1, 2]
        
        for i in range(2, 32):
            fib.append(fib[i - 1] + fib[i - 2])
        
        last_bit = 0
        ans = 0
        
        for i in range(31, -1, -1):
            if n & (1 << i):
                ans += fib[i]
                
                if last_bit:
                    ans -= 1
                    break
                
                last_bit = 1
            else:
                last_bit = 0
        
        return ans + 1
        
        
        
        
# @lc code=end

