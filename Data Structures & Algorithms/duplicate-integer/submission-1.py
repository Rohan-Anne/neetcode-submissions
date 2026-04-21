class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = set()
        for i in range(len(nums)):
            if nums[i] not in duplicates:
                duplicates.add(nums[i])
        return len(duplicates) != len(nums)
        