class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = []
        for i in range(len(cost) + 1):
            memo.append(-1)
        memo[0] = 0
        memo[1] = 0
        memo[2] = min(cost[0], cost[1])
        def dfs(i):
            if memo[i] == -1:
                if memo[i - 1] == -1:
                    memo[i - 1] = dfs(i - 1)
                if memo[i - 2] == -1:
                    memo[i - 2] = dfs(i - 2)
                memo[i] = min(memo[i - 1] + cost[i - 1], memo[i - 2] + cost[i - 2])
            return memo[i]
        return dfs(len(cost))
            
        
        