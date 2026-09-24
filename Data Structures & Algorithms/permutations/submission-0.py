class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Base Cases
        if len(nums) == 1:
            return [[nums[0]]]
        if len(nums) == 2:
            return [[nums[0], nums[1]], [nums[1], nums[0]]]
        permutations = []
        for i in range(len(nums)):
            # Combine all numbers before and after current element into a list
            before = []
            after = []
            if i > 0:
                before = nums[0:i]
            if i < len(nums) - 1:
                after = nums[i + 1:len(nums)]
            # Get all the permutations of a list of numbers that doesn't include this number, and then add the current number to the beginning of all permutations
            currentPermutations = self.permute(before + after)
            for j in range(len(currentPermutations)):
                currentPermutations[j] = [nums[i]] + currentPermutations[j]
                # Add final permutation to list
                permutations.append(currentPermutations[j])
        return permutations
        
        