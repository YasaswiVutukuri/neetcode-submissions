class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = {}
        result = []

        # LOOP 1: build the count dictionary completely first
        for num in nums:
            if num in count:
                count[num] = count[num] + 1
            else:
                count[num] = 1

        # LOOP 2: only after counting is done, check which numbers qualify
        for num in count:
            if count[num] > n/3:
                result.append(num)

        return result