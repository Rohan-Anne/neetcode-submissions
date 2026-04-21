class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = [[strs[0]]]
        for i in range(1, len(strs)):
            anagramWithOthers = False
            for j in range(len(anagrams)):
                if self.checkAnagram(anagrams[j][0], strs[i]):
                    anagrams[j].append(strs[i])
                    anagramWithOthers = True
            if not anagramWithOthers:
                    anagrams.append([strs[i]])
        return anagrams


    def checkAnagram(self, str1, str2):
        dict1 = {}
        dict2 = {} 
        for i in range(len(str1)):
            if str1[i] not in dict1:
                dict1[str1[i]] = 0
            else:
                dict1[str1[i]] += 1
        
        for i in range(len(str2)):
            if str2[i] not in dict2:
                dict2[str2[i]] = 0
            else:
                dict2[str2[i]] += 1
        return dict1 == dict2
        



        