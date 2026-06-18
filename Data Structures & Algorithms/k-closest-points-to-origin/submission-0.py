import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        tuples = []
        closest = []
        for i in range(len(points)):
            current = (-(points[i][0]**2 + points[i][1]**2), points[i])
            print(current)
            heapq.heappush(tuples, current)
            while len(tuples) > k:
                farthest = heapq.heappop(tuples)
        
        for i in range(len(tuples)):
            closest.append(tuples[i][1])
        
        
        return closest
                 
        