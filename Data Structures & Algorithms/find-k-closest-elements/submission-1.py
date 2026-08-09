class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        l = 0
        r = len(arr) - 1
        
        # Shrink window until size is k
        while r - l + 1 > k:
            # Drop whichever side is farther from x
            if abs(arr[l] - x) > abs(arr[r] - x):
                l += 1   # Left is farther (e.g., 1 vs 10), drop left
            else:
                r -= 1   # Right is farther or equal, drop right
                
        return arr[l : r + 1]