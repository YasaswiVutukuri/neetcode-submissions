class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index,num in enumerate(nums):
            val = target - num
            if val in seen:
                return [seen[val],index]
            else:
                seen[num] = index