class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        prefix.append(0) # For the first number there are no elements before to make product of
        suffix = []
        output = []

        # Create prefix array
        prefix_product = 1
        for i in range(len(nums) - 1):
            prefix_product *= nums[i]
            prefix.append(prefix_product)

        # Create suffix array
        reversed_nums = nums[::-1]
        suffix_product = 1
        for i in range(len(reversed_nums) - 1):
            suffix_product *= reversed_nums[i]
            suffix.append(suffix_product)
        suffix = suffix[::-1]
        suffix.append(0) # For the last number there are no elements after to make products from

        # Use prefix and suffix arrays to get output array
        for i in range(len(prefix)):
            if i == 0 or i == len(prefix) - 1:
                output.append(prefix[i] + suffix[i])
            else:
                output.append(prefix[i] * suffix[i])

        
        

        print("Prefix Array: " + str(prefix))
        print("Suffix Array: " + str(suffix))
        print("Output Array: " + str(output))

        return output
        
        