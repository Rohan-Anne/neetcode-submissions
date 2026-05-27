class Solution:

    def makeDictString(self, text: str):
        stringDict = dict()
        for i in range(len(text)):
            if text[i] in stringDict.keys():
                stringDict[text[i]] += 1
            else:
                stringDict[text[i]] = 1
        return stringDict


    def isAnagram(self, s: str, t: str) -> bool:
        dictS, dictT = self.makeDictString(s), self.makeDictString(t)
        return dictS == dictT
        
        
        



        