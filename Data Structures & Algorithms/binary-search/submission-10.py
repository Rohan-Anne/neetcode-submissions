class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = int((l + r) / 2)
            print("Middle index: " + str(m))
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m

        if nums[l] == target:
            return l
            
        return -1
        