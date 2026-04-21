class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maximumLength = 0
        for num in numSet:
            length = 0
            if num - 1 not in numSet:
                length = 1
            while num + length in numSet:
                length += 1
            if length > maximumLength:
                maximumLength = length
        return maximumLength



        

        

        


        