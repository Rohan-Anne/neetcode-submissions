class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [[strs[0]]]
        mappings = dict()
        sublists = []

        # organize frequencies
        for string in strs:
            frequencies = []
            for i in range(26):
                frequencies.append(0)
            for char in string:
                frequencies[ord(char) - ord('a')] += 1
            frequencies = tuple(frequencies)
            if frequencies in mappings.keys():
                mappings[frequencies].append(string)
            else:
                mappings[frequencies] = [string]
        # generate sublists
        for key in mappings.keys():
            sublists.append(mappings[key])
        
        return sublists
        


                

        