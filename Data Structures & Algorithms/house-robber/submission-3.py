class Solution:
    def rob(self, nums: List[int]) -> int:
        # Base Cases
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        # Memoization
        memo = []
        for i in range(len(nums)):
            memo.append(-1)
        memo[len(nums) - 1] = nums[len(nums) - 1]
        memo[len(nums) - 2] = max(nums[len(nums) - 1], nums[len(nums) - 2])
        # 1D DP
        def dfs(start):
            if memo[start] == -1:
                # Calculate what happens if you rob current house and skip adjacent house
                rob = 0
                if start + 2 < len(nums):
                    if memo[start + 2] == -1:
                        memo[start + 2] = dfs(start + 2)
                    rob = memo[start + 2]
                # Calculate what happens if you rob adjacent house and skip the current house as well as the house after the adjacent house
                skip = 0
                if start + 3 < len(nums):
                    if memo[start + 3] == -1:
                        memo[start + 3] = dfs(start + 3)
                    skip = memo[start + 3]
                print("Rob Current House:")
                print(nums[start] + rob)
                print("Skip Current House and Rob Adjacent:")
                print(nums[start + 1] + skip)
                print("Current Start Index: " + str(start))
                memo[start] = max(nums[start] + rob, nums[start + 1] + skip)
            return memo[start]
        
        value = dfs(0)
        print(memo)
        return value


        