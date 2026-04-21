class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequencyS = {}
        frequencyT = {}
        for char in s:
            if char not in frequencyS:
                frequencyS[char] = 0
            else:
                frequencyS[char] += 1
        for char in t:
            if char not in frequencyT:
                frequencyT[char] = 0
            else:
                frequencyT[char] += 1
        
        return frequencyS == frequencyT
            
            

        



        