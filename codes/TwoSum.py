from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # remove the number more than target
        nums.sort()
        New_List = []
        for x in nums:
            if x > target:
                break
            New_List.append(x)

        output = []
        for i in range(len(New_List) - 1):
            try:
                list = New_List[i + 1 :]
                x = list.index(target - New_List[i])
                output[0] = i
                output[1] = x
                break
            except:
                pass

        return output


main = Solution()
Solution.twoSum(main, [2, 7, 11, 15], 9)
