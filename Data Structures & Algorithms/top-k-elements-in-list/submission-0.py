class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFrequencies = {}
        for num in nums:
            if num not in numFrequencies:
                numFrequencies[num] = 1
            else:
                numFrequencies[num] += 1
        numFrequencies = dict(sorted(numFrequencies.items(), key=lambda item: item[1], reverse=True))
        elements = list(numFrequencies.keys())
        return elements[0:k]
        
        