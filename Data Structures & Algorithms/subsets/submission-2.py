class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        currentSubset = []
        def traversal(i):
            print(currentSubset)
            if i >= len(nums):
                subsets.append(currentSubset.copy())
                return
            currentSubset.append(nums[i])
            traversal(i + 1)
            currentSubset.remove(nums[i])
            traversal(i + 1)
        traversal(0)
        return subsets

        
        
        