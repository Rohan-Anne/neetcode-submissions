class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charS = dict()
        charT = dict()
        for i in range(len(s)):
            if s[i] in charS:
                charS[s[i]] += 1
            else:
                charS[s[i]] = 1
        for i in range(len(t)):
            if t[i] in charT:
                charT[t[i]] += 1
            else:
                charT[t[i]] = 1
        return charS == charT
        


        