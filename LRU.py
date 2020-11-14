class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    """
    @param: capacity: An integer
    """

    def __init__(self, capacity):
        # do intialization if necessary
        self.capacity = capacity
        self.cache = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    """
    @param: key: An integer
    @return: An integer
    """

    def get(self, key):
        # write your code here
        if key in self.cache:
            self.remove(self.cache[key])
            self.add_to_front(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """

    def set(self, key, value):
        # write your code here
        self.cache[key] = Node(key, value)
        self.add_to_front(self.cache[key])
        if len(self.cache) > self.capacity:
            node = self.tail.prev
            self.remove(node)
            del self.cache[node.key]

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_to_front(self, node):
        nextnode = self.head.next
        node.next = nextnode
        self.head.next = node
        nextnode.prev = node
        node.prev = self.head

LRUCache(2)
set(2, 1)
set(1, 1)
get(2)
set(4, 1)
get(1)
get(2)