class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = dict()
        for i in range(len(nums)):
            if nums[i] in numbers:
                numbers[nums[i]] += 1
            else:
                numbers[nums[i]] = 1
        numbers = sorted(numbers.items(), key = lambda item: item[1], reverse=True)
        needed = numbers[0:k]
        frequentElements = []
        for i in range(len(needed)):
            frequentElements.append(needed[i][0])
        return frequentElements
            




        

        