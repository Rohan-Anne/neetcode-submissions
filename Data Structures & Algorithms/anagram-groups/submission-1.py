class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramKeys = []
        anagramGroups = [[strs[0]]]
        firstDict = {}
        for char in strs[0]:
            if char not in firstDict:
                firstDict[char] = 0
            else:
                firstDict[char] += 1
        anagramKeys.append(firstDict)

        for i in range(1, len(strs)):
            wordDict = {}
            for char in strs[i]:
                if char not in wordDict:
                    wordDict[char] = 0
                else:
                    wordDict[char] += 1
            if wordDict in anagramKeys:
                anagramIndex = anagramKeys.index(wordDict)
                anagramGroups[anagramIndex].append(strs[i])
            else:
                anagramKeys.append(wordDict)
                anagramGroups.append([strs[i]])

        return anagramGroups




            



        