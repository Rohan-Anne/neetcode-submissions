class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        subarrays = 0
        prefixSum = 0
        remainders = {0 : 1}
        for i in range(len(nums)):
            prefixSum += nums[i]
            currentRemainder = prefixSum % k
            if currentRemainder in remainders:
                subarrays += remainders[currentRemainder]
            else:
                remainders[currentRemainder] = 0
            remainders[currentRemainder] += 1
        return subarrays

        
        
        