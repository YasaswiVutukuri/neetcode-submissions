class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        need = {}
        window = {}

        # Frequency of s1
        for ch in s1:
            need[ch] = need.get(ch, 0) + 1

        # First window
        for i in range(len(s1)):
            ch = s2[i]
            window[ch] = window.get(ch, 0) + 1

        if need == window:
            return True

        left = 0

        # Slide the window
        for right in range(len(s1), len(s2)):
            # Add new character
            window[s2[right]] = window.get(s2[right], 0) + 1

            # Remove left character
            window[s2[left]] -= 1
            if window[s2[left]] == 0:
                del window[s2[left]]

            left += 1

            if need == window:
                return True

        return False