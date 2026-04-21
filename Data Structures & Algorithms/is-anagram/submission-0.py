class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequencyS = {}
        frequencyT = {}
        for char in s:
            if char in frequencyS:
                frequencyS[char] += 1
            else:
                frequencyS[char] = 0
        for char in t:
            if char in frequencyT:
                frequencyT[char] += 1
            else:
                frequencyT[char] = 0
        
        return frequencyS == frequencyT
            

        



        