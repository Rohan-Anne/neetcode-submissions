class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            print("Left: " + str(l))
            print("Right: " + str(r))
            m = int((l + r) / 2)
            if nums[m] == target:
                return m
            # Scenario 1: l and m are in the same branch
            if nums[m] >= nums[l] and nums[m] >= nums[r]:
                # Check if target exists between l and m
                if nums[l] == target:
                    return l 
                if nums[l] < target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # Scenario 2: r and m are in the same branch
            if nums[r] >= nums[m] and nums[l] >= nums[m]:
                # Check if target exists between m and r
                if nums[r] == target:
                    return r
                if nums[m] < target < nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            
            # Scenario 3: l and r are part of the same sorted branch
            if nums[l] <= nums[m] <= nums[r]:
                # See where target falls within sorted branch
                if target > nums[m]:
                    l = m + 1
                elif target < nums[m]:
                    r = m - 1

        # Final check or return -1           
        if nums[l] == target:
            return l
        else:
            return -1

        