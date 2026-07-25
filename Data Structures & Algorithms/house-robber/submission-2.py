class Solution:
    def robHelper(self, nums, memo):
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        if len(nums) == 3:
            return max(nums[0] + nums[2], nums[1])
        if nums in memo:
            return memo[nums]
        if nums[2:] not in memo:
            memo[nums[2:]] = self.robHelper(nums[2:], memo)
        if nums[3:] not in memo:
            memo[nums[3:]] = self.robHelper(nums[3:], memo)
        memo[nums] = max(nums[0] + memo[nums[2:]], nums[1] + memo[nums[3:]])
        return memo[nums]

    def rob(self, nums: List[int]) -> int:
        numsTuple = tuple(nums)
        memo = {}
        return self.robHelper(numsTuple, memo)
        


        