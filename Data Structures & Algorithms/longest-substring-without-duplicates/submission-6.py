class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        maximumLength = -1
        l = 0
        r = 0
        characters = set()
        for i in range(len(s)):
            while s[i] in characters:
                characters.remove(s[l])
                l += 1
            if r - l + 1 > maximumLength:
                maximumLength = r - l + 1
            characters.add(s[i])
            r += 1
        return maximumLength
            

        