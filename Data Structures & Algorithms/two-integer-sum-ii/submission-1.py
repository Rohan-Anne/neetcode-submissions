class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        startIndex = 0
        finalIndex = len(numbers) - 1
        while startIndex < finalIndex:
            currentSum = numbers[startIndex] + numbers[finalIndex]
            if currentSum == target:
                return [startIndex + 1, finalIndex + 1]
            elif currentSum > target:
                finalIndex -= 1
            else:
                startIndex += 1
        