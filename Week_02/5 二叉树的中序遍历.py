def inorderTraversal(self, root: TreeNode) -> List[int]:
    res = []

    # def recursion(root):
    #     if not root:
    #         return

    #     recursion(root.left)
    #     res.append(root.val)
    #     recursion(root.right)

    #     return

    # recursion(root)
    # return res
    
    """
    迭代： 先将所有的left node加入到stack中，再取出加入res，之后将right加入到stack中
    """
    from collections import deque
    stack = deque()
    if not root:
        return []

    node = root

    while stack or node:
        while node:
            stack.append(node)
            node = node.left

        node = stack.pop()
        res.append(node.val)
        node = node.right

    return res