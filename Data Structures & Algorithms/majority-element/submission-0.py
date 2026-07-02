class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        val = sorted(nums)
        maj = len(nums) // 2
        
        return val[maj] 