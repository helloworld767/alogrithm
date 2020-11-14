class Solution:
    """
    @param: k: An integer
    """

    def __init__(self, k):
        # do intialization if necessary
        self.heap = []
        self.maxheapsize = k

    def min_heapify(self, heapsize, root):
        left = root * 2 + 1
        right = left + 1
        flag = root
        if left < heapsize and self.heap[flag] > self.heap[left]:
            flag = left
        if right < heapsize and self.heap[flag] > self.heap[right]:
            flag = right
        if flag != root:
            self.heap[root], self.heap[flag] = self.heap[flag], self.heap[root]
            self.min_heapify(heapsize, flag)

    def build_min_heap(self):
        heapsize = len(self.heap)
        for i in range((len(self.heap) - 2) // 2, -1, -1):
            self.min_heapify(heapsize, i)

    def heap_sort(self):
        heapsize = len(self.heap)
        for i in range(heapsize - 1, -1, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            self.min_heapify(i, 0)

    """
    @param: num: Number to be added
    @return: nothing
    """

    def add(self, num):
        # write your code here
        if len(self.heap) < self.maxheapsize:
            self.heap.append(num)
            self.build_min_heap()
        elif self.heap[0] < num:
            self.heap[0] = num
            self.build_min_heap()
        print(self.heap)

    """
    @return: Top k element
    """

    def topk(self):
        # write your code here
        t = self.heap.copy()
        self.heap_sort()
        k = self.heap.copy()
        self.heap = t
        return k


k = Solution(3)
k.add(num=3)
k.add(num=10)
print(k.topk())
k.add(num=1000)
k.add(num=-99)
print(k.topk())
k.add(num=4)
print(k.topk())
k.add(num=100)
print(k.topk())