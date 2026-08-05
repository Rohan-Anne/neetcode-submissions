class CacheNode:
    def __init__(self, key, value, prev, next):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next 

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        tempNode = CacheNode(None, None, None, None)
        self.least = tempNode
        self.most = tempNode
        self.initialized = False
    
    def traversal(self):
        if self.least is None:
            return
        traversal = self.least
        array = [traversal.key]
        while traversal.next:
            traversal = traversal.next
            array.append(traversal.key)
        print(array)


    def get(self, key: int) -> int:
        print("Start of get call for key " + str(key))
        print(self.cache)
        self.traversal()
        if not self.initialized:
            return -1
        else:
            if key not in self.cache:
                return -1
            else:
                node = self.cache[key]
                if len(self.cache) == 1:
                    return node.value
                if node == self.least:
                    self.least = self.least.next
                if node != self.most:
                    # Disconnect node
                    if node.next:
                        node.next.prev = node.prev
                    if node.prev:
                        node.prev.next = node.next
                    # Attach node to the end of the list
                    node.prev = self.most
                    node.next = None
                    # Update MRU node
                    self.most.next = node
                    self.most = self.most.next
                return node.value
        

    def put(self, key: int, value: int) -> None:
        print("Start of put call for key " + str(key) + " and value " + str(value))
        print(self.cache)
        self.traversal()
        # Insert element
        if not self.initialized:
            firstNode = CacheNode(key, value, None, None)
            self.least = firstNode
            self.most = firstNode
            self.cache[key] = firstNode
            self.initialized = True
        else:
            if key in self.cache:
                if len(self.cache) == 1:
                    self.least.value = value
                else:
                    node = self.cache[key]
                    node.value = value
                    # If node is LRU move pointer forward 
                    if node == self.least:
                        self.least = self.least.next
                    if node != self.most:
                        # Disconnect node
                        if node.next:
                            node.next.prev = node.prev
                        if node.prev:
                            node.prev.next = node.next
                        # Move node to end of list
                        node.prev = self.most
                        node.next = None
                        # Make node MRU
                        self.most.next = node
                        self.most = self.most.next
            else:
                node = CacheNode(key, value, self.most, None)
                self.most.next = node
                self.most = self.most.next
                self.cache[key] = node
        # Check capacity
        if len(self.cache) > self.capacity:
            key = self.least.key
            self.cache.pop(key)
            self.least = self.least.next
        
        


                    


                


        
