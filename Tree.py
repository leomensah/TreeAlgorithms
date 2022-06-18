class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

class Tree:
    def createNode(self, data):
        return Node(data)

    def insert(self, node, data):
        if node is None:
            return self.createNode(data)
        if data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)
        return node

    def traverse_Inorder(self, root):
        if root is not None:
            self.traverse_Inorder(root.left)
            print(root.data)
            self.traverse_Inorder(root.right)

    def preOrderTraverser(self, root):
        if root is not None:
            print(root.data)
            self.preOrderTraverser(root.left)
            self.preOrderTraverser(root.right)

    def postOrderTraverser(self, root):
        if root is not None:
            self.postOrderTraverser(root.left)
            self.postOrderTraverser(root.right)
            print(root.data)

tree = Tree()
node1 = tree.createNode(1)
node2 = tree.createNode(2)
node3 = tree.createNode(3)
node4 = tree.createNode(4)
node5 = tree.createNode(5)
node2.left = node4
node2.right = node5
node1.left = node2
node1.right = node3
print(node1.data)

print("Inorder ----> ")
tree.traverse_Inorder(node1)