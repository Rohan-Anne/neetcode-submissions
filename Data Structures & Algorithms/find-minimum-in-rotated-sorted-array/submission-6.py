class Solution:
    def findMin(self, nums: List[int]) -> int:
        smallest = nums[0]
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] < nums[right]:
                smallest = min(smallest, nums[left])
                return smallest
            mid = int((left + right) / 2)
            print("Left: " + str(left))
            print("Right: " + str(right))
            print("Mid: " + str(mid))
            smallest = min(smallest, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        return smallest

        