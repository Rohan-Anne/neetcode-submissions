class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = dict()
        for i in range(len(nums)):
            numbers[nums[i]] = i
        
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in numbers.keys() and numbers[difference] != i:
                return [i, numbers[difference]]
        