class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        dict1 = {}
        for k in range(len(s1)):
            if s1[k] in dict1:
                dict1[s1[k]] += 1
            else:
                dict1[s1[k]] = 0
        for i in range(len(s2)):
            lastIndex = i + len(s1)
            substring = s2[i:lastIndex]
            dict2 = {}
            for j in range(len(substring)):
                if substring[j] in dict2:
                    dict2[substring[j]] += 1
                else:
                    dict2[substring[j]] = 0
            if dict1 == dict2:
                return True 
        return False
        