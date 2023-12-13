#
# @lc app=leetcode id=2233 lang=python3
#
# [2233] Maximum Product After K Increments
#

# @lc code=start
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        nums_dict = {}
        min_v = float('inf')
        mod = pow(10, 9) + 7
        
        for v in nums:
            nums_dict[v] = nums_dict.get(v, 0) + 1
            min_v = min(min_v, v)
        
        ans = 0
        while k > 0:
            if k > nums_dict[min_v]:
                nums_dict[min_v + 1] = nums_dict.get(min_v + 1, 0) + nums_dict[min_v]
                k -= nums_dict[min_v]
                del nums_dict[min_v]
                min_v += 1
            
            else:
                nums_dict[min_v+1] = nums_dict.get(min_v + 1, 0)  + k
                nums_dict[min_v] -= k
                k = 0
        
        ans = 1
        for v, num in nums_dict.items():
            ans = (ans * pow(v, num)) % mod 
        
        return ans
# @lc code=end

