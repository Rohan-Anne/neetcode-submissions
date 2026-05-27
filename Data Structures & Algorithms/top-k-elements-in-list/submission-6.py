import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = dict()
        for i in range(len(nums)):
            if nums[i] in frequencies.keys():
                frequencies[nums[i]] += 1
            else:
                frequencies[nums[i]] = 1
        elements = []
        for key in frequencies.keys():
            heapq.heappush(elements, (frequencies[key], key))
            if len(elements) > k:
                heapq.heappop(elements)
       
        
        kFrequent = []
        for i in range(len(elements)):
            kFrequent.append(elements[i][-1])
        return kFrequent
            

        