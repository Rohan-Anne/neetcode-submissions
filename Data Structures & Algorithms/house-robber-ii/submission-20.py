class Solution:

    def robHelper(self, nums, memo, isFullList):
        # Base Cases
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        if len(nums) == 3:
            if isFullList:
                return max(nums[0], nums[1], nums[2])
            else:
                return max(nums[0] + nums[2], nums[1])
        # Return if result already calculated
        if nums in memo:
            return memo[nums]
        # Otherwise utilize 1D DP
        if isFullList:
            # Choice 1: Choose first house and forfeit second house and last house
            if nums[2:len(nums) - 1] not in memo:
                memo[nums[2:len(nums) - 1]] = self.robHelper(nums[2:len(nums) - 1], memo, False)
            # Choice 2: Choose last house and forfeit first house and second to last hosue
            if nums[1:len(nums) - 2] not in memo:
                memo[nums[1:len(nums) - 2]] = self.robHelper(nums[1:len(nums) - 2], memo, False)
            # Choice 3: Choose second house and forfeit first house
            if nums[3:] not in memo:
                memo[nums[3:]] = self.robHelper(nums[3:], memo, False)
            # Choice 4: Choose second to last house and forfeit last house
            if nums[0:len(nums) - 3] not in memo:
                memo[nums[0:len(nums) - 3]] = self.robHelper(nums[0:len(nums) - 3], memo, False)
            print(memo)
            return max(nums[0] + memo[nums[2:len(nums) - 1]], nums[-1] + memo[nums[1:len(nums) - 2]], nums[1] + memo[nums[3:]], nums[len(nums) - 2] + memo[nums[0:len(nums) - 3]])
        else:  
            # Choice 1: Choose first house and forfeit house after
            if nums[2:] not in memo:
                memo[nums[2:]] = self.robHelper(nums[2:], memo, False)
            # Choice 2: Choose second house and forfeit house before and after
            if nums[3:] not in memo:
                memo[nums[3:]] = self.robHelper(nums[3:], memo, False)
            return max(nums[0] + memo[nums[2:]], nums[1] + memo[nums[3:]])
    def rob(self, nums: List[int]) -> int:
        memo = {}
        nums = tuple(nums)
        return self.robHelper(nums, memo, True)
        