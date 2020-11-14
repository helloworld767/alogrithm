def sym(left, right):
    if not left and not right:
        return True
    if not left or not right:
        return False
    if left.val == right.val:
        return sym(left.left, right.right) and sym(left.right, right.left)
    else:
        return False

sym(root, root)
