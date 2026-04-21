class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        currentTriplets = set()
        for i in range(len(nums)):
            currentList = list(nums)
            currentList.pop(i)
            print(currentList)
            startIndex = 0
            finalIndex = len(currentList) - 1
            while startIndex < finalIndex:
                if currentList[startIndex] + currentList[finalIndex] == -1 * nums[i]:
                    currentTuple = tuple(sorted([currentList[startIndex], currentList[finalIndex], nums[i]]))
                    if not (currentTuple in currentTriplets):
                        currentTriplets.add(currentTuple)
                        triplets.append([currentList[startIndex], currentList[finalIndex], nums[i]])
                    startIndex += 1
                elif currentList[startIndex] + currentList[finalIndex] + nums[i] > 0:
                    finalIndex -= 1
                else:
                    startIndex += 1
        return triplets

                    



                
            
        