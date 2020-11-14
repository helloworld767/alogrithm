def max_heapify(heap, heapsize, root):
    left = root * 2 + 1
    right = left + 1
    flag = root
    if left < heapsize and heap[left] > heap[flag]:
        flag = left
    if right < heapsize and heap[right] > heap[flag]:
        flag = right
    if root != flag:
        heap[root], heap[flag] = heap[flag], heap[root]
        max_heapify(heap, heapsize, flag)


def build_max_heap(heap):
    heapsize = len(heap)
    for i in range((len(heap) - 2) // 2, -1, -1):
        max_heapify(heap, heapsize, i)


def heap_sort(heap):
    for i in range(len(heap) - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        max_heapify(heap, i, 0)


tinput, k = [4,5,1,6,2,7,3,8],4
h = tinput[:k]
build_max_heap(h)
print(h)
for i in range(k, len(tinput)):
    if tinput[i] < h[0]:
        h[0] = tinput[i]
        max_heapify(h, k, 0)

print(h)
