class Solution:

    def encode(self, strs: List[str]) -> str:
        finalString = ""
        for i in range(len(strs)):
            finalString += str(len(strs[i])) + "#" + strs[i]
        return finalString

    def decode(self, s: str) -> List[str]:
        i = 0;
        finalStrings = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            start = j + 1
            end = start + length
            currentString = s[start:end]
            finalStrings.append(currentString)
            i = start + length
        return finalStrings




            
            
            
            
            
                



