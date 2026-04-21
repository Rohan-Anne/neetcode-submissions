class Solution:
    def isPalindrome(self, s: str) -> bool:
        startIndex = 0
        finalIndex = len(s) - 1
        while startIndex < finalIndex:
            while startIndex < finalIndex and not s[startIndex].isalnum():
                startIndex += 1
            while startIndex < finalIndex and not s[finalIndex].isalnum():
                finalIndex -= 1
            if s[startIndex].lower() != s[finalIndex].lower():
                return False
            startIndex += 1
            finalIndex -= 1
        return True
        