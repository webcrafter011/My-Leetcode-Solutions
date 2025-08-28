class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key → Node

        # Dummy head & tail to avoid edge cases
        self.head = Node(0, 0)   # left = MRU
        self.tail = Node(0, 0)   # right = LRU
        self.head.next = self.tail
        self.tail.prev = self.head

    # helper: remove a node from DLL
    def _remove(self, node: Node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    # helper: insert node right after head (MRU position)
    def _insert(self, node: Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        # move node to MRU position
        self._remove(node)
        self._insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # remove old node
            self._remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self._insert(node)

        if len(self.cache) > self.capacity:
            # evict LRU (node before tail)
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
