class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        memo = []
        for i in range(len(nums)):
            memo.append(-1)
        memo[len(nums) - 1] = nums[len(nums) - 1]
        memo[len(nums) - 2] = max(nums[len(nums) - 1], nums[len(nums) - 2])
        def dfs(start):
            if memo[start] == -1:
                rob = 0
                if start + 2 < len(nums):
                    if memo[start + 2] == -1:
                        memo[start + 2] = dfs(start + 2)
                    rob = memo[start + 2]
                skip = 0
                if start + 3 < len(nums):
                    if memo[start + 3] == -1:
                        memo[start + 3] = dfs(start + 3)
                    skip = memo[start + 3]
                memo[start] = max(nums[start] + rob, nums[start + 1] + skip)
            return memo[start]
    
        return dfs(0)


        