class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def insertLevelOrder(arr, i, n, root):
    if i < n:
        temp = Node(arr[i])
        root = temp
        root.left = insertLevelOrder(arr, 2 * i + 1, n, root.left)
        root.right = insertLevelOrder(arr, 2 * i + 2, n, root.right)
    return root

story = [1,2,2,NULL,3,NULL,3]
n = len(story)
root = None
tree = insertLevelOrder(story, root, 0, n)

def check_symmetric(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    elif((tree1 is None) != (tree2 is None)) or tree1.data != tree2.data:
        return False
    else:
        return check_symmetric(tree1.left, tree2.right) and check_symmetric(tree1.right, tree2.left)

def is_symmetric(tree):
    if tree is None:
        return True
    return check_symmetric(tree.left, tree.right)

# root = [1,2,2,None,3,None,3]
root2 = [1,2,2,None,3,None,3]
n1 = len(root2)
root = None
tree2 = insertLevelOrder(root2, root, 0, n1)
print(is_symmetric(tree))
# print(is_symmetric(root2))