class Solution:

    def robHelper(self, nums, memo, firstValue):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        if nums in memo:
            print(memo)
            return memo[nums]
        if firstValue:
            # Choice 1: Moving along with the first house
            if nums[2:len(nums) - 1] not in memo:
                memo[nums[2:len(nums) - 1]] = self.robHelper(nums[2:len(nums) - 1], memo, False)
            # Choice 2: Moving along with the final house
            if nums[1:len(nums) - 2] not in memo:
                memo[nums[1:len(nums) - 2]] = self.robHelper(nums[1:len(nums) - 2], memo, False)
            # Choice 3: Not moving along with either house
            if nums[1:len(nums) - 1] not in memo:
                memo[nums[1:len(nums) - 1]] = self.robHelper(nums[1:len(nums) - 1], memo, False)
            memo[nums] = max(nums[0] + memo[nums[2:len(nums) - 1]], nums[-1] + memo[nums[1:len(nums) - 2]], memo[nums[1:len(nums) - 1]])
            print("Choice 1: " + str(nums[0] + memo[nums[2:len(nums) - 1]]))
            print("Choice 2: " + str(nums[-1] + memo[nums[1:len(nums) - 2]]))
            print("Choice 3: " + str(memo[nums[1:len(nums) - 1]]))
        else:
            # Just like straight line robbing houses problem
            if nums[2:] not in memo:
                memo[nums[2:]] = self.robHelper(nums[2:], memo, False)
            if nums[3:] not in memo:
                memo[nums[3:]] = self.robHelper(nums[3:], memo, False)
            memo[nums] = max(nums[0] + memo[nums[2:]], nums[1] + memo[nums[3:]])
        return memo[nums]

        

    def rob(self, nums: List[int]) -> int:
        nums = tuple(nums)
        memo = {}
        return self.robHelper(nums, memo, True)
        