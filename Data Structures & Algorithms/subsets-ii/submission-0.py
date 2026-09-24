class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        seenSet = set()
        currentSubset = []
        def traversal(i, seen):
            if i >= len(nums):
                subsets.append(currentSubset.copy())
                return
            if nums[i] in seen:
                # Skip over current element
                traversal(i + 1, seen.copy())
            else:
                currentSubset.append(nums[i])
                traversal(i + 1, seen.copy())
                currentSubset.remove(nums[i])
                seen.add(nums[i])
                traversal(i + 1, seen.copy())
        traversal(0, seenSet)
        return subsets

        