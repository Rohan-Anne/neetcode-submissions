class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumDict = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in sumDict:
                return [sumDict[difference], i]
            sumDict[nums[i]] = i

        
        






        