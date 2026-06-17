import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        heapq.heapify(self.heap)
        self.k = k
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        largest = None
        value = len(self.heap) + 1 - self.k
        removed = []
        for i in range(value):
            removed.append(heapq.heappop(self.heap))
        for i in range(len(removed)):
            heapq.heappush(self.heap, removed[i])
        return removed[-1]
