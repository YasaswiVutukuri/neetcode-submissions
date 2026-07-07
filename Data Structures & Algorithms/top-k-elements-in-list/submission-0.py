from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Automatically creates a frequency map
        counts = Counter(nums) 
        
        # Step 2 & 3: most_common(k) returns the top k elements as (element, frequency) tuples
        # We use a list comprehension to just grab the elements
        return [item[0] for item in counts.most_common(k)]