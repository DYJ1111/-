def levelOrder(self, root: 'Node') -> List[List[int]]:
    """
    层次遍历，类似于BFS，使用队列辅助
    O(n), O(n)
    """
    if not root:
        return []

    res = []
    from collections import deque
    queue = deque()
    queue.append(root)

    while queue:
        cur_res = []
        for _ in range(len(queue)):  # the nodes of current level
            node = queue.popleft()
            cur_res.append(node.val)

            for child in node.children:
                queue.append(child)
        res.append(cur_res)

    return res