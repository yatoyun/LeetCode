#
# @lc app=leetcode id=1856 lang=python3
#
# [1856] Maximum Subarray Min-Product
#

# @lc code=start
class Solution:
    # monotomic stack + prefix sum
    def maxSumMinProduct(self, nums: List[int]) -> int:
        mod = pow(10, 9) + 7
        
        stack = [-1]
        nums.append(0)
        ps = [0]
        output = 0
        
        for i in range(len(nums)):
            while nums[stack[-1]] > nums[i]:
                min_v = nums[stack.pop()]
                output = max(output, (ps[-1] - ps[stack[-1]+1]) * min_v)
            stack.append(i)
            ps.append(ps[-1]+nums[i])
        
        return output % mod
# @lc code=end

