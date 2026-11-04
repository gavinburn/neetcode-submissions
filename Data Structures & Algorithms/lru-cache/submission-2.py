class Node:

    def __init__(self, key, value, prev, nextNode):
        self.key = key
        self.value = value
        self.prev = prev
        self.nextNode = nextNode


class LRUCache:

    def __init__(self, capacity: int):

        self.cache = {}

        self.head = Node("dummy", "value", None, None)
        self.capacity = capacity
        self.nodes = 0
        self.tail = None

        

        

    def get(self, key: int) -> int:
        # print(self.cache)
        if key in self.cache:
            value = self.cache[key].value
            self.remove(key)
            self.add(key, value)
            # print(self.cache)
            return self.cache[key].value
        else:
            return -1        

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            self.cache[key].key = key
            self.cache[key].value = value
            self.remove(key)
            self.add(key,value)
            return

        self.add(key, value)

        # print(str(key) + " " + str(self.nodes))

        if self.nodes > self.capacity:
            # print("reached")
            self.removeFromFront()


    def remove(self, key):
        self.nodes -=1

        if self.cache[key].prev is not None and self.cache[key].nextNode is not None:
            self.cache[key].prev.nextNode = self.cache[key].nextNode
            self.cache[key].nextNode.prev = self.cache[key].prev
            self.cache.pop(key)

        elif self.cache[key].prev is None and self.cache[key].nextNode is not None:
            self.head = self.head.nextNode
            self.cache[key].nextNode.prev = None
            self.cache.pop(key)

        elif self.cache[key].nextNode is None and self.cache[key].prev is not None:
            self.tail = self.tail.prev 
            self.cache[key].prev.nextNode = None
            self.cache.pop(key)

        else: 
            self.head = Node("dummy", "value", None, None)
            self.tail = None

    def add(self, key, value):
        self.nodes +=1

        if self.head.key == "dummy":
            self.head.key = key
            self.head.value = value
            self.tail = self.head
            self.cache[key] = self.head
            return
        
        newNode = Node(key, value, self.tail, None)
        self.tail.nextNode = newNode
        self.tail = newNode
        self.cache[key] = newNode


    def removeFromFront(self):
        # print(self.head.key)
        self.cache.pop(self.head.key)
        self.nodes -=1 
        self.head.nextNode.prev = None
        self.head = self.head.nextNode
        # print(self.head.key)

        



        
