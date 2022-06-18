class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
 
# Function to insert nodes in level order
def insertLevelOrder(arr, root, i, n):
     
    # Base case for recursion
    if i < n:
        temp = newNode(arr[i])
        root = temp
 
        # insert left child
        root.left = insertLevelOrder(arr, root.left,
                                     2 * i + 1, n)
 
        # insert right child
        root.right = insertLevelOrder(arr, root.right,
                                      2 * i + 2, n)
    return root