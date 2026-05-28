class Solution:
    def isPalindrome(self, s: str) -> bool:
        convertedString = ""
        for i in range(len(s)):
            if ord("A") <= ord(s[i]) <= ord("Z") or ord("a") <= ord(s[i]) <= ord("z") or ord("0") <= ord(s[i]) <= ord("9"):
                convertedString += s[i].lower()

        start = 0
        end = len(convertedString) - 1

        while start < end:
            if convertedString[start] != convertedString[end]:
                return False
            start += 1
            end -= 1
        return True
        