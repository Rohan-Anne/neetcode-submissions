import copy
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        pickedNumbers = []
        for i in range(len(nums)):
            pickedNumbers.append(False)
        def traversal(perm, nums, pick):
            if len(perm) >= len(nums):
                print(perm)
                permutations.append(perm.copy())
                return
            for i in range(len(nums)):
                if not pick[i]:
                    perm.append(nums[i])
                    pick[i] = True
                    traversal(perm, nums, pick)
                    perm.pop()
                    pick[i] = False
        traversal([], nums, pickedNumbers)
        return permutations
        
        
                    



        traversal(0, pickedNumbers)




        