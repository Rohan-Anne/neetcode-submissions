class Solution:
    def climbStairsHelper(self, n, memo):
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n in memo:
            return memo[n]
        memo[n] = self.climbStairsHelper(n - 1, memo) + self.climbStairsHelper(n - 2, memo)
        return memo[n]

    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.climbStairsHelper(n, memo)
        
    
    
        