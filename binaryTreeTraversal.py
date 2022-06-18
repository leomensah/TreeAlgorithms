from collections import deque
# from unittest import result

def levelOrderTraversal(root):
    queue = deque()

    root = queue.append(root)
    results = []
    while root:
        l = len(root)
        level = []
        for i in range(l):
            node = root.popleft()
            if node:
                level.append(node.value)
                root.append(node.left)
                root.append(node.right)
        results.append(level)
    return results
