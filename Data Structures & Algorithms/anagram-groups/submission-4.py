class Solution:

    def makeStringDict(self, text: str):
        stringDict = defaultdict(str)
        for i in range(len(text)):
            if text[i] in stringDict.keys():
                stringDict[text[i]] += 1
            else:
                stringDict[text[i]] = 1
        return stringDict

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        sublists = [[self.makeStringDict(strs[0]), strs[0]]]
        for i in range(1, len(strs)):
            textDict = self.makeStringDict(strs[i])
            existedAlready = False
            for j in range(len(sublists)):
                if textDict == sublists[j][0]:
                    sublists[j].append(strs[i])
                    existedAlready = True

            if not existedAlready:
                sublists.append([textDict, strs[i]])
        
        for i in range(len(sublists)):
            sublists[i] = sublists[i][1:]
            
        return sublists

      

        