class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        mapping = {'}': '{', ')' : '(', ']' : '['}
        stack = [s[0]]
        for i in range(1, len(s)):
            print(s[i])
            if s[i] == '{' or s[i] == '(' or s[i] == '[':
                stack.append(s[i])
            else:
                if not stack:
                    return False
                if mapping[s[i]] != stack[-1]:
                    return False
                stack.pop()

        return not stack

        