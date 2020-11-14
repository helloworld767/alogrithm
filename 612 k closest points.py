points = [[-1,-1],[1,1],[100,100]]
origin = [0,0]
k = 2
# points = [[point.x, point.y] for point in points]
points.sort()


def comp(point1, point2, origin):
    d1 = (point1[0] - origin[0]) ** 2 + (point1[1] - origin[1]) ** 2
    d2 = (point2[0] - origin[0]) ** 2 + (point2[1] - origin[1]) ** 2
    if d1 == d2:
        return point1 < point2
    return d1 < d2


def max_heapify(heap, heapsize, root, origin):
    left = 2 * root + 1
    right = left + 1
    flag = root
    if left < heapsize and comp(heap[flag], heap[left], origin):
        flag = left
    if right < heapsize and comp(heap[flag], heap[right], origin):
        flag = right
    if root != flag:
        heap[flag], heap[root] = heap[root], heap[flag]
        max_heapify(heap, heapsize, flag, origin)


def build_max_heap(heap, origin):
    heapsize = len(heap)
    for i in range((len(heap) - 2) // 2, -1, -1):
        max_heapify(heap, heapsize, i, origin)


def heap_sort(heap):
    for i in range(len(heap) - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        max_heapify(heap, i, 0, origin)


heap = points[:k]
build_max_heap(heap, origin)
for i in range(k, len(points)):
    if comp(points[i], heap[0], origin):
        heap[0] = points[i]
        max_heapify(heap, len(heap), 0, origin)
heap_sort(heap)
print(heap)