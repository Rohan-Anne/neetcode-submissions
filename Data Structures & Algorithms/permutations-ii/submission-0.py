class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        pickedNumbers = []
        for i in range(len(nums)):
            pickedNumbers.append(False)
        permutations = []
        def traversal(perm, nums, pick):
            if len(perm) >= len(nums):
                permutations.append(perm.copy())
                return
            seen = set()
            for i in range(len(nums)):
                if not pick[i] and nums[i] not in seen:
                    seen.add(nums[i])
                    pick[i] = True
                    perm.append(nums[i])
                    traversal(perm, nums, pick)
                    pick[i] = False
                    perm.pop()
        traversal([], nums, pickedNumbers)
        return permutations


                


        