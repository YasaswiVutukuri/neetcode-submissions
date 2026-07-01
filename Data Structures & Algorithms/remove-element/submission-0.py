class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        strt = 0
        for num in nums:
            if num != val:
                nums[strt] = num
                strt += 1
                
        return strt