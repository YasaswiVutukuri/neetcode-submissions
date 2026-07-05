class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Base case: a list of 0 or 1 elements is already sorted
        if len(nums) <= 1:
            return nums
        
        # Step 1: Split into two halves
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        
        # Step 2: Recursively sort each half
        left = self.sortArray(left)
        right = self.sortArray(right)
        
        # Step 3: Merge the two sorted halves
        return self.merge(left, right)
    
    def merge(self, left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result