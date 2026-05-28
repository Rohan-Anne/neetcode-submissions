class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in range(len(strs)):
            encoded += str(len(strs[i]))
            encoded += "#"
            encoded += strs[i]
        print(encoded)
        return encoded 

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        currentString = ""
        while i < len(s):
            if s[i] != "#":
                currentString += s[i]
            else:
                strs.append(s[i + 1: i + 1 + int(currentString)])
                i += int(currentString)
                currentString = ""
            i += 1
        return strs

            

            

            

