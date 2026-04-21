class Solution:
    def isValid(self, s: str) -> bool:
        if s[0] in [')', '}', ']']:
            return False
        stack = []
        keys = {'{' : '}', '[' : ']', '(' : ')'}
        for i in range(len(s)):
            # Check first if it is an opening bracket
            if s[i] in ['(', '{', '[']:
                stack.append(s[i])
            else:
                if stack and s[i] == keys[stack[-1]]:
                    stack.pop()
                else:
                    return False
        
        return not stack
            
                
        
        