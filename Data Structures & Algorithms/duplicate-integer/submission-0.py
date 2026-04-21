class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = set([])
        for i in range(len(nums)):
            numSet.add(nums[i])
        if len(numSet) == len(nums):
            return False
        return True
        