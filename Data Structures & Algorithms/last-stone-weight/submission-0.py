class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)
        print(stones)

        while len(stones) > 1:
            largest = heapq.heappop(stones) * -1
            secondLargest = heapq.heappop(stones) * -1
            if largest == secondLargest:
                continue
            elif largest > secondLargest:
                largest = largest - secondLargest
                heapq.heappush(stones, largest * -1)

        if len(stones) == 0:
            return 0
        else:
            return -1 * stones[0]

        