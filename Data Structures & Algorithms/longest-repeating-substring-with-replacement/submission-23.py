class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= 1:
            return len(s)
        l = 0
        maxFrequency = 1
        frequencies = dict()
        frequencies[s[0]] = 1
        longest = 1
        for r in range(1, len(s)):
            # Update frequencies
            if s[r] in frequencies.keys():
                frequencies[s[r]] += 1
            else:
                frequencies[s[r]] = 1

            # Choose the most frequent character
            if frequencies[s[r]] > maxFrequency:
                maxFrequency = frequencies[s[r]]
            
            while (r - l + 1) - maxFrequency > k:
                frequencies[s[l]] -= 1
                l += 1
            
            if (r - l + 1) > longest:
                longest = r - l + 1


            print("Left: " + str(l))
            print("Right: " + str(r))
            print(frequencies)

        return longest


            

        
        
        