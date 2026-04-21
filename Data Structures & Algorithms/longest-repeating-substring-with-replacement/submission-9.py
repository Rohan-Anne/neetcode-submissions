class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        startIndex = 0
        currentIndex = 0
        maxFrequency = 0
        longestLength = 1
        characters = {}

        while currentIndex < len(s):
            characters[s[currentIndex]] = 1 + characters.get(s[currentIndex], 0)
            maxFrequency = max(maxFrequency, characters[s[currentIndex]])
            while currentIndex - startIndex + 1 - maxFrequency > k:
                characters[s[startIndex]] -= 1
                startIndex += 1
            longestLength = max(longestLength, currentIndex - startIndex + 1)
            currentIndex += 1
        return longestLength






        
        