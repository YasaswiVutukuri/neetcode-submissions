from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp = defaultdict(list)
        for word in strs:
            keys = "".join(sorted(word))
            grp[keys].append(word)
        return list(grp.values())
