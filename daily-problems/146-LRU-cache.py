'''
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
'''


class DLL:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = DLL(-1)
        self.tail = DLL(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.lookup = {}
        self.position = {}

    def oldUpdate(self, node):
        # Update the orig
        node.prev.next = node.next
        node.next.prev = node.prev

    def newUpdate(self, node):
        # Update the new position
        self.head.next.prev = node
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.lookup:
            return -1
        node = self.position[key]
        self.oldUpdate(node)
        self.newUpdate(node)
        return self.lookup[key]

    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            node = self.position[key]
            self.lookup[key] = value
            self.oldUpdate(node)
            self.newUpdate(node)
        else:
            newNode = DLL(key)
            self.position[key] = newNode
            self.lookup[key] = value
            if len(self.lookup) > self.capacity:
                leastUsed = self.tail.prev
                k = leastUsed.val
                self.oldUpdate(leastUsed)
                self.newUpdate(newNode)
                del self.position[k]
                del self.lookup[k]
            else:
                self.newUpdate(newNode)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
