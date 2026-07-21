class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        left = 0
        right = 0
        
        # Keep going while AT LEAST ONE string still has characters left
        while left < len(word1) or right < len(word2):
            
            # Step 1: If word1 still has characters, grab one!
            if left < len(word1):
                result += word1[left]
                left += 1
                
            # Step 2: If word2 still has characters, grab one!
            if right < len(word2):
                result += word2[right]
                right += 1
                
        return result