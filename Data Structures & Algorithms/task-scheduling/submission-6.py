import heapq
class Solution:
    def leastInterval(self, tasks, n):
        # Count frequency of tasks
        counts = dict()
        for i in range(len(tasks)):
            if tasks[i] in counts.keys():
                counts[tasks[i]] += 1
            else:
                counts[tasks[i]] = 1

        # Create heap of task frequencies
        heap = []
        for key in counts.keys():
            heap.append(-1 * counts[key])
        heapq.heapify(heap)

        
        # Create queue to manage tasks on cooldown
        queue = []
        
        # Find shortest interval
        shortestInterval = 0
        
        while heap or queue:
            shortestInterval += 1
            # If there are elements in heap, pop most frequent and add to queue
            if heap:
                mostFrequent = heapq.heappop(heap) + 1
                if mostFrequent < 0:
                    queue.append((mostFrequent, shortestInterval + n))

            if len(queue) > 0 and shortestInterval >= queue[0][1]:
                 heapq.heappush(heap, queue.pop(0)[0])
            
            print("Heap: " + str(heap))
            print("Queue: " + str(queue))
            print("Interval: " + str(shortestInterval))

        return shortestInterval


        


        