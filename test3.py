def min_heapify(heap, heapsize, root):
    left = root * 2 + 1
    right = left + 1
    flag = root
    if left < heapsize and heap[left] < heap[flag]:
        flag = left
    if right < heapsize and heap[right] < heap[flag]:
        flag = right
    if root != flag:
        heap[root], heap[flag] = heap[flag], heap[root]
        min_heapify(heap, heapsize, flag)

def build_min_heap(heap):
    heapsize = len(heap)
    for i in range((heapsize - 2) // 2, -1, -1):
        min_heapify(heap, heapsize, i)


def heapsort(heap):
    build_min_heap(heap)

    for i in range(len(heap)-1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        min_heapify(heap, i, 0)



if __name__ == '__main__':
    li = [5, 6, 8, 1, 2, 4, 9]
    # li = [5, 7, 9, 8, 2, 4, 1, 3, 6, 4, 9, 3, 1]
    # li = [5, 4, 3, 2, 1]
    # quick_sort(li, 0, len(li)-1)
    heapsort(li)
    print(li)