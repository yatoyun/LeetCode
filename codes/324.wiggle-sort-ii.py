#
# @lc app=leetcode id=324 lang=python3
#
# [324] Wiggle Sort II
#

# @lc code=start
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        min_nums = nums[:len(nums)//2 + bool(len(nums)%2)]
        big_nums = nums[len(nums)//2 + bool(len(nums)%2):]
        print(min_nums, big_nums)
        for i in range(len(nums)//2):
            nums[2*i] = min_nums[-(i+1)]
            nums[2*i+1] = big_nums[-(i+1)]
        
        if len(nums) % 2 != 0:
            nums[-1] = min_nums[0]
        
        
# @lc code=end

