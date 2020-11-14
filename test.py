# def merge(nums):
#     if len(nums) < 2:
#         return
#     mid = len(nums) // 2
#     l = nums[:mid]
#     r = nums[mid:]
#     merge(l)
#     merge(r)
#     nums.clear()
#     mergesort(l, r, nums)
#
#
# def mergesort(l, r, nums):
#     left, right = 0, 0
#     while left < len(l) and right < len(r):
#         if l[left] < r[right]:
#             nums.append(l[left])
#             left += 1
#         else:
#             nums.append(r[right])
#             right += 1
#     if left < len(l):
#         nums.extend(l[left:])
#     elif right < len(r):
#         nums.extend(r[right:])


def quick_sort(nums, left, right):
    if left >= right:
        return
    flag = nums[left]
    l, r = left, right
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
    left = root * 2 + 1
    right = left + 1
    flag = root
    if left < heapsize and heap[left] > heap[flag]:
        flag = left
    if right < heapsize and heap[right] > heap[flag]:
        flag = right
    if flag != root:
        heap[root], heap[flag] = heap[flag], heap[root]
        max_heapify(heap, heapsize, flag)


def build_max_heap(heap):
    heapsize = len(heap)
    for i in range((heapsize - 2) // 2, -1, -1):
        max_heapify(heap, heapsize, i)


def heapsort(heap):
    build_max_heap(heap)
    # print(heap)
    for i in range(len(heap)-1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        # print(heap)
        max_heapify(heap, i, 0)


if __name__ == "__main__":
    # li = [5, 6, 8, 1, 2, 4, 9]
    li = [5, 7, 9, 8, 2, 4, 1, 3, 6, 4, 9, 3, 1]
    # li = [1]
    # li = [5, 4, 3, 2, 1]
    # quick_sort(li, 0, len(li)-1)
    heapsort(li)
    print(li)
