class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1 or k == 0: return False
        seen = set()
        start = 0
        end = 1
        seen.add(nums[0])
        while end < len(nums):
            if nums[end] in seen:
                return True
            seen.add(nums[end])
            end += 1
            if end - start > k:
                seen.remove(nums[start])
                start += 1
        return False
        