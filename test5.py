def quick_sort(nums, left, right):
    if left >= right:
        return
    l, r = left, right
    flag = nums[left]
    while l < r:
        while l < r and nums[r] >= flag:
            r -= 1
        nums[l] = nums[r]
        while l < r and nums[l] < flag:
            l += 1
        nums[r] = nums[l]
    nums[l] = flag
    quick_sort(nums, left, l-1)
    quick_sort(nums, l+1, right)


def max_heapify(heap, heapsize, root):
    left = 2 * root + 1
    right = left + 1
    flag = root
    if left < heapsize and heap[left] > heap[flag]:
        flag = left
    if right < heapsize and heap[right] > heap[flag]:
        flag = right
    if flag != root:
        heap[flag], heap[root] = heap[root], heap[flag]
        max_heapify(heap, heapsize, flag)


def build_max_heap(heap):
    heapsize = len(heap)
    for i in range((heapsize-2)//2, -1, -1):
        max_heapify(heap, heapsize, i)


def heap_sort(heap):
    build_max_heap(heap)
    for i in range(len(heap)-1, -1, -1):
        heap[i], heap[0] = heap[0], heap[i]
        max_heapify(heap, i, 0)


li = [5, 6, 6, 8, 1, 2, 1, 4, 9]
# li = [5, 7, 9, 8, 2, 4, 1, 3, 6, 4, 9, 3, 1]
# li = [5, 4, 3, 2, 1]
# quick_sort(li, 0, len(li)-1)
heap_sort(li)
print(li)