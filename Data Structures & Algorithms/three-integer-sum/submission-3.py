class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        triplets = []
        for i in range(len(nums) - 1):
            startIndex = i + 1
            finalIndex = len(nums) - 1
            while startIndex < finalIndex:
                currentSum = nums[startIndex] + nums[finalIndex]
                if currentSum == -1 * nums[i]:
                    triplet = sorted([nums[i], nums[startIndex], nums[finalIndex]])
                    if triplet not in triplets:
                        triplets.append(triplet)
                    finalIndex -= 1
                    startIndex += 1
                elif currentSum > -1 * nums[i]:
                    finalIndex -= 1
                else:
                    startIndex += 1
        return triplets

            

        