class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarrays = 0
        prefixSum = 0
        prefixSums = {0: 1}
        for i in range(len(nums)):
            prefixSum += nums[i]
            if prefixSum - k in prefixSums:
                subarrays += prefixSums[prefixSum - k]
            if prefixSum not in prefixSums:
                prefixSums[prefixSum] = 0
            prefixSums[prefixSum] += 1
        return subarrays


                
        
        
        
            
        