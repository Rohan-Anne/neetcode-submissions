class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        i = 0
        while i < length:
            nums.append(nums[i])
            i += 1
        return nums

        