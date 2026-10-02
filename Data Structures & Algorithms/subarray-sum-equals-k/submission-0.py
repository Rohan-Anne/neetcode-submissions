class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarrays = 0
        prefix = []
        prefixSum = 0
        for i in range(len(nums)):
            prefixSum += nums[i]
            prefix.append(prefixSum)
        seen = dict()
        print(prefix)
        for i in range(len(prefix)):
            if prefix[i] == k:
                subarrays += 1
            if prefix[i] - k in seen.keys():
                subarrays += seen[prefix[i] - k]

            if prefix[i] not in seen:
                seen[prefix[i]] = 1
            else:
                seen[prefix[i]] += 1
        return subarrays
                
        
        
        
            
        