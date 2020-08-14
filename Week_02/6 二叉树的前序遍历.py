def preorderTraversal(self, root: TreeNode) -> List[int]:
    res = []
    # def recursion(root):
    #     if not root:
    #         return

    #     res.append(root.val)
    #     recursion(root.left)
    #     recursion(root.right)

    #     return
    # recursion(root)
    # return res
    
    """
    迭代法： 使用 stack 代替递归，前序遍历的迭代法可参考层次遍历
    O(n), O(n)
    """
    from collections import deque
    stack = deque()
    if not root:
        return []

    stack.append(root)

    while stack:
        node = stack.pop()
        res.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res