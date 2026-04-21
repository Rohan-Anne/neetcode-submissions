class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            if l == r:
                if nums[l] == target:
                    return l
                else:
                    return -1
            currentIndex = int((l + r) / 2)
            print(currentIndex)
            if nums[currentIndex] == target:
                return currentIndex
            elif nums[currentIndex] < target:
                l = currentIndex + 1
            else:
                r = currentIndex
        
        return -1
        