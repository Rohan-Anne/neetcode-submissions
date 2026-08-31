class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        solution = []
        subset = []
        def traversal(i):
            if i >= len(nums):
                solution.append(subset.copy())
                return 
            subset.append(nums[i])
            traversal(i + 1)
            subset.pop()
            traversal(i + 1)
        traversal(0)
        return solution
        
            
            
        