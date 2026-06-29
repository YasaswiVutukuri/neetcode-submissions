class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 1. Get the shortest word length
        shrt_len = min(len(word) for word in strs)
        
        # 2. Loop through the index numbers
        for index in range(shrt_len):
            char = strs[0][index]
            
            # 3. Look at every word in the list
            for word in strs:
                if word[index] != char:
                    return strs[0][:index]
                    
        # 4. If no mismatch, return the full prefix length
        return strs[0][:shrt_len]