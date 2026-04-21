class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        startIndex = 0
        finalIndex = len(numbers) - 1
        while startIndex < finalIndex:
            sum = numbers[startIndex] + numbers[finalIndex]
            if sum == target:
                return [startIndex + 1, finalIndex + 1]
            elif sum > target:
                finalIndex = finalIndex - 1
            elif sum < target:
                startIndex = startIndex + 1
        
        return None
        

         