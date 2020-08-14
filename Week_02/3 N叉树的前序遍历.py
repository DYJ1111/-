def preorder(self, root: 'Node') -> List[int]:
    res = []

    # def recursion(root):
    #     if not root:
    #         return
    #     res.append(root.val)
    #     for child in root.children:
    #         recursion(child)
    # recursion(root)
    # return res
    """
    迭代法：参考二叉树前序遍历的迭代法
    O(N), O(N)
    """
    if not root:
        return res
    from collections import deque
    stack = deque()
    stack.append(root)
    while stack:
        node = stack.pop()
        res.append(node.val)

        for child in node.children[::-1]:
            stack.append(child)

    return res