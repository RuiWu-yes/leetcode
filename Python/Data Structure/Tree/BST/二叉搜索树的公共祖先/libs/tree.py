class TreeNode:
    def __init__(self, x=-1):
        self.val = x
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self):
        self.root = TreeNode()

    def add(self, val):
        node = TreeNode(val)
        if self.isEmpty(): self.root = node
        else:
            tree_node = self.root
            queue = []
            queue.append(self.root)
            while queue:
                tree_node = queue.pop(0)
                if tree_node.left == None:
                    tree_node.left = node
                    return
                elif tree_node.right == None:
                    tree_node.right = node
                    return
                else:
                    queue.append(tree_node.lchild)
                    queue.append(tree_node.rchild)

    def inorder(self, root):
        res = []
        deque = [root]
        while deque:
            node = deque.pop(0)
            res.append(node.val)
            if node.left:
                deque.append(node.left)
            if node.right:
                deque.append(node.right)
        return res

    def isEmpty(self):
        return True if self.root.val == -1 else False