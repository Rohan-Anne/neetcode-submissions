class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        tripletsTuples = set()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            target = -1 * nums[i]
            start = i + 1
            end = len(nums) - 1
            while start < end:
                if nums[start] + nums[end] == target:
                    if (nums[i], nums[start], nums[end]) not in tripletsTuples:
                        tripletsTuples.add((nums[i], nums[start], nums[end])) 
                    start += 1
                elif nums[start] + nums[end] < target:
                    start += 1
                else:
                    end -= 1
        
        triplets = []
        temp = list(tripletsTuples)
        for elem in temp:
            triplets.append([elem[0], elem[1], elem[2]])
        return triplets

            
        