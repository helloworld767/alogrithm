class SegmentTreeNode:
    def __init__(self, low, high):
        self.low, self.high, self.cnt = low, high, 0
        self.left, self.right = None, None


def build(left, right):
    root = SegmentTreeNode(cum[left], cum[right])
    if left == right:
        return root
    mid = left + (right - left) // 2
    root.left = build(left, mid)
    root.right = build(mid + 1, right)
    return root


def update(root, val):
    if not root:
        return
    if root.low <= val <= root.high:
        root.cnt += 1
        update(root.left, val)
        update(root.right, val)


def query(root, lower, upper):
    if lower <= root.low and root.high <= upper:
        return root.cnt
    if upper < root.low or root.high < lower:
        return 0
    return query(root.left, lower, upper) + query(root.right, lower, upper)


nums = [-2,5,-1]
lower = -2
upper = 2
cumsum = [0]
for i in range(len(nums)):
    cumsum.append(cumsum[-1] + nums[i])
cum = sorted(list(set(cumsum)))
root = build(0, len(cum) - 1)
res = 0
for csum in cumsum:
    res += query(root, csum - upper, csum - lower)
    print(res)
    update(root, csum)

print(res)