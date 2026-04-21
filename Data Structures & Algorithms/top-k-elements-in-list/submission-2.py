class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create buckets
        buckets = []
        for i in range(len(nums)):
            buckets.append([])
        
        frequencies = dict()
        # Collect frequencies
        for i in range(len(nums)):
            if nums[i] in frequencies:
                frequencies[nums[i]] += 1
            else:
                frequencies[nums[i]] = 1
        # Sort into buckets
        for key in frequencies.keys():
            buckets[frequencies[key] - 1].append(key)
        # Collect number from buckets
        orderedNums = []
        for i in range(len(buckets)):
            if len(buckets[i]) != 0:
                for j in range(len(buckets[i])):
                    orderedNums.append(buckets[i][j])
        return orderedNums[len(frequencies.keys()) - k:]

        
        
        
        
        


        

            




        

        