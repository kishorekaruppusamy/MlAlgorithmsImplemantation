from TreeBuilder import *


class TreeTraverser:
    @staticmethod
    def preOrderTraversal(root: Node):
        if root is None:
            return

        print(root.data)
        TreeTraverser.preOrderTraversal(root.left)
        TreeTraverser.preOrderTraversal(root.right)

    @staticmethod
    def inOrderTraversal(root: Node):
        if root is None:
            return

        TreeTraverser.inOrderTraversal(root.left)
        print(root.data)
        TreeTraverser.inOrderTraversal(root.right)

    @staticmethod
    def postOrderTraversal(root: Node):
        if root is None:
            return

        TreeTraverser.postOrderTraversal(root.left)
        TreeTraverser.postOrderTraversal(root.right)
        print(root.data)


if __name__ == "__main__":
    values = [50, 20, 60, 19, 30, 55, 70]

    treebuilder = TreeBuilder(values)

    tree_root = treebuilder.createBST()

    TreeTraverser.inOrderTraversal(tree_root)

