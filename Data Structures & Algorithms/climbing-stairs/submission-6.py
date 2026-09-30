class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        memo = []
        for i in range(n):
            memo.append(-1)
        memo[0] = 1
        memo[1] = 2
        def dfs(i):
            if memo[i] != -1:
                return memo[i]
            else:
                if memo[i - 1] == -1:
                    memo[i - 1] = dfs(i - 1)
                if memo[i - 2] == -1:
                    memo[i - 2] = dfs(i - 2)
                memo[i] = memo[i - 1] + memo[i - 2]
                return memo[i]
        return dfs(n - 1)
        