class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_s = dict()
        for char in s:
            news = count_s.get(char,0)+1
            count_s[char] = news
        count_t = dict()
        for char in t:
            newt = count_t.get(char,0)+1
            count_t[char] = newt
        if count_s == count_t:
            return True
        else:
            return False