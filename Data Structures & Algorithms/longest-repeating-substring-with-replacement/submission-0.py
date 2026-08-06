class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}  # "note vals in dict"
        l = 0
        max_len = 0
        max_freq = 0  # keeps track of the most repeated character count
        
        for r in range(len(s)):
            # 1. Add current character s[r] to dict count
            counts[s[r]] = counts.get(s[r], 0) + 1
            
            # 2. Update highest frequency character in window
            max_freq = max(max_freq, counts[s[r]])
            
            # 3. If minority characters > k, shrink window from left
            while (r - l + 1) - max_freq > k:
                counts[s[l]] -= 1
                l += 1
            
            # 4. Track max window size
            max_len = max(max_len, r - l + 1)
            
        return max_len