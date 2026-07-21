class Solution:

    def helper(self, cost, memo, lastIndex):
        if lastIndex == 0:
            return 0
        if lastIndex == 1:
            return 0
        if lastIndex in memo:
            return memo[lastIndex]
        # Get minimum cost of 2 indexes before the position you are trying to reach
        if lastIndex - 1 not in memo:
            memo[lastIndex - 1] = self.helper(cost, memo, lastIndex - 1)
        if lastIndex - 2 not in memo:
            memo[lastIndex - 2] = self.helper(cost, memo, lastIndex - 2)
        # Return whichever cost is less between the 2 index choices
        memo[lastIndex] = min(memo[lastIndex - 1] + cost[lastIndex - 1], memo[lastIndex - 2] + cost[lastIndex - 2])
        print(memo)
        return memo[lastIndex]


    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        return self.helper(cost, memo, len(cost))
    

        
        