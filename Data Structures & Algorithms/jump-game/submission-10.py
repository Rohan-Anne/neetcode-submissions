class Solution:

    def orHelper(self, nums, start, end):
        if start == end:
            return self.canJumpHelper(nums, start)
        return self.canJumpHelper(nums, start) or self.orHelper(nums, start + 1, end)
    
    def canJumpHelper(self, nums, startIndex):
        jumpHeight = nums[startIndex]
        if startIndex >= len(nums) - 1:
            return True
        if startIndex + jumpHeight >= len(nums) - 1:
            return True
        if jumpHeight == 0:
            return False
        return self.orHelper(nums, startIndex + 1, startIndex + jumpHeight)
    
    def canJump(self, nums: List[int]) -> bool:
        return self.canJumpHelper(nums, 0)

        