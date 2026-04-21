class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        for i in range(len(s2)):
            lastIndex = i + len(s1)
            currentSubstring = s2[i:lastIndex]
            if sorted(currentSubstring) == sorted(s1):
                return True 
        return False
        