def dfs(node, target):
    if not node.left and not node.right:
        return node.val
    if node.val > target:
        return dfs(node.left, target)
    elif node.val == target:
        return node.val
    else:
        if not node.right:
            return node.val
        elif node.right.val <= target:
            return dfs(node.right, target)
        elif node.right.val > target:
            return node.val