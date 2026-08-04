
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        
        for i, num in enumerate(nums):
            # 1. Found a duplicate within the current window!
            if num in seen:
                return True
            
            # 2. Add current number to window
            seen.add(num)
            
            # 3. Maintain window size of at most k
            if len(seen) > k:
                seen.remove(nums[i - k])
                
        return False