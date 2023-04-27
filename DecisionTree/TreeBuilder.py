def getNode(data):
    node = Node(data)
    node.data = data
    node.left = None
    node.right = None
    return node


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class TreeBuilder:
    def __init__(self, values):
        self.values = values

    def binarySearchTree(self, root, data) -> Node:
        if root is None:
            return getNode(data)

        if data <= root.data:
            root.left = self.binarySearchTree(root.left, data)
        else:
            root.right = self.binarySearchTree(root.right, data)

        return root

    def createBST(self):
        length = len(self.values)
        if length == 0:
            return None
        root = None

        for itr in range(0, length):
            root = self.binarySearchTree(root, self.values[itr])

        return root
