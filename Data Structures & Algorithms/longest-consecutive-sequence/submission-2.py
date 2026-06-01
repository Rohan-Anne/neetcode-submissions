class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numSet = set(nums)
        longest = 1
        for i in range(len(nums)):
            currentLength = 1
            currentNum = nums[i]
            while currentNum + 1 in numSet:
                currentNum += 1
                currentLength += 1
            if currentLength > longest:
                longest = currentLength
        return longest
            
        
        