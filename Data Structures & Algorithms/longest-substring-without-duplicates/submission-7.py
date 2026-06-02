class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        frequencies = dict()
        frequencies[s[0]] = 1
        longest = 1
        for i in range(1, len(s)):
            if len(frequencies.keys()) > longest:
                    longest = len(frequencies.keys())
            if s[i] in frequencies.keys():
                while s[i] in frequencies.keys():
                    frequencies.pop(next(iter(frequencies)))
            frequencies[s[i]] = 1
        
        if len(frequencies.keys()) > longest:
            return len(frequencies.keys())
        return longest 
        

                    
                

                



        
                

        
        