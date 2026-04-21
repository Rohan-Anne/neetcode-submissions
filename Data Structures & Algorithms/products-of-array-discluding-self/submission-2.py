class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        prefixSum = 1
        suffixSum = 1
        output = []
        for i in range(len(nums)):
            prefixSum *= nums[i]
            prefix.append(prefixSum)
            suffixSum *= nums[len(nums)-i-1]
            suffix.append(suffixSum)
        
        suffix = suffix[::-1]

        for i in range(len(nums)):
            if i == 0:
                output.append(suffix[1])
            elif i == len(nums) - 1:
                output.append(prefix[len(nums) - 2])
            else:
                output.append(prefix[i - 1] * suffix[i + 1])
        
        return output

        
        
        






        

        

        