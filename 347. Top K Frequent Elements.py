import collections
nums = [5,1,-1,-8,-7,8,-5,0,1,10,8,0,-4,3,-1,-1,4,-5,4,-3,0,2,2,2,4,-2,-4,8,-7,-7,2,-8,0,-8,10,8,-8,-2,-9,4,-7,6,6,-1,4,2,8,-3,5,-9,-3,6,-8,-5,5,10,2,-5,-1,-5,1,-3,7,0,8,-2,-3,-1,-5,4,7,-9,0,2,10,4,4,-4,-1,-1,6,-8,-9,-1,9,-9,3,5,1,6,-1,-2,4,2,4,-6,4,4,5,-5]
k = 7

def min_heapify(heap, heapsize, root):
    left = root * 2 + 1
    right = left + 1
    flag = root
    if left < heapsize and dic[heap[left]] < dic[heap[flag]]:
        flag = left
    if right < heapsize and dic[heap[right]] < dic[heap[flag]]:
        flag = right
    if flag != root:
        heap[flag], heap[root] = heap[root], heap[flag]
        min_heapify(heap, heapsize, flag)


def build_min_heap(heap):
    heapsize = len(heap)
    for i in range(len((heap) - 2) // 2, -1, -1):
        min_heapify(heap, heapsize, i)


heap = collections.deque()
dic = collections.Counter(nums)
for key in dic:
    if len(heap) == k and dic[key] > dic[heap[0]]:
        heap[0] = key
        min_heapify(heap, k, 0)
    elif len(heap) < k:
        heap.appendleft(key)
        min_heapify(heap, len(heap), 0)
        print([dic[i] for i in heap])
print(dic)



