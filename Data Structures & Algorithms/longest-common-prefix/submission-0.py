class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1: return strs[0]
        prefix = strs[0]
        for i in range(1, len(strs)):
            print(prefix)
            currentPrefix = ""
            for j in range(len(strs[i])):
                if j >= len(prefix):
                    break
                if prefix[j] == strs[i][j]:
                    currentPrefix += strs[i][j]
                else:
                    break
            prefix = currentPrefix
        return prefix
        