class Solution:
    def decodingHelper(self, s, memo):
        if len(s) == 0:
            return 0
        if len(s) == 1:
            if int(s[0]) > 0:
                return 1
            else:
                return 0
        count = 0
        if int(s[0]) > 0:
            if s[1:] not in memo:
                memo[s[1:]] = self.decodingHelper(s[1:], memo)
            count += memo[s[1:]]
        if int(s[0]) > 0 and int(s[0:2]) <= 26:
            if s[2:] not in memo:
                memo[s[2:]] = self.decodingHelper(s[2:], memo)
            count += memo[s[2:]]
            if s[2:] == '':
                count += 1
        return count


            


    def numDecodings(self, s: str) -> int:
        # Can get character by adding 64 to integer value
        # ASCII value will have at most 2 digits
        # Single digit values are guaranteed to be decodable
        # Double digit values cannot 
        memo = {}
        return self.decodingHelper(s, memo)
        