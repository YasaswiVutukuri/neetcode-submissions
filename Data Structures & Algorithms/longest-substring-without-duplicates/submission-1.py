class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l = 0
        max_len = 0
        
        for r in range(len(s)):
            # Fix 1 & 2: Use 'while' and check the character 's[r]'
            while s[r] in window:
                window.remove(s[l])
                l += 1  # Don't forget to move 'l' forward!
                
            window.add(s[r])
            max_len = max(max_len, len(window))
            
        return max_len