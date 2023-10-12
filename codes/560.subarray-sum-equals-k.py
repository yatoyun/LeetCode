#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#
from collections import defaultdict

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cumulative_sum_dict = defaultdict(int)
        cumulative_sum = 0
        
        output = 0
        
        for num in nums:
            cumulative_sum += num
            
            if cumulative_sum - k in cumulative_sum_dict.keys():
                output += cumulative_sum_dict[cumulative_sum - k]
            
            if cumulative_sum - k == 0:
                output += 1
            
            cumulative_sum_dict[cumulative_sum] += 1
        
        return output
            
            
# @lc code=end

