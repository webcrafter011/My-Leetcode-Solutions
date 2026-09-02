class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def insert_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
        self.size -= 1
    
    def remove_tail(self):
        if self.size == 0:
            return None
        node = self.tail.prev
        self.remove(node)
        return node


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.cache = {}        # key -> Node
        self.freq_map = {}     # freq -> DoublyLinkedList

    def _update(self, node):
        """Helper: move node to the next freq list"""
        freq = node.freq
        self.freq_map[freq].remove(node)
        if self.freq_map[freq].size == 0:
            del self.freq_map[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        
        node.freq += 1
        self.freq_map.setdefault(node.freq, DoublyLinkedList()).insert_head(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._update(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._update(node)
        else:
            if self.size == self.capacity:
                # evict LFU node
                lfu_list = self.freq_map[self.min_freq]
                evict = lfu_list.remove_tail()
                del self.cache[evict.key]
                self.size -= 1
            
            # new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.freq_map.setdefault(1, DoublyLinkedList()).insert_head(new_node)
            self.min_freq = 1
            self.size += 1
