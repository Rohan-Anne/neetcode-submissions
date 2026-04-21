class Solution:
    def isValid(self, s: str) -> bool:
        keyValuePairs = {'(' : ')', '{' : '}', '[' : ']'}
        stack = []

        for char in s:
            if char in keyValuePairs:  # opening bracket
                stack.append(char)
            else:  # closing bracket
                if not stack:
                    return False
                if keyValuePairs[stack[-1]] != char:
                    return False
                stack.pop()

        return not stack


        