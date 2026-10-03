class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixSum = 0
        remainders = {0: -1}
        for i in range(len(nums)):
            prefixSum += nums[i]
            remainder = prefixSum % k
            if remainder in remainders:
                if i - remainders[remainder] > 1:
                    print(remainders)
                    return True
            else:
                remainders[remainder] = i
        return False

        
        

        

        