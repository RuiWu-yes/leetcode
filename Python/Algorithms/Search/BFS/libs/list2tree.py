import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

# The binary tree can be created by list.
class ListCreateTree():
    def __init__(self, nodestyle=0):
        self.nodestyle = nodestyle

    def lct(self, root, list, i):  # 用列表递归创建二叉树，
        # 它其实创建过程也是从根开始a开始，创左子树b，再创b的左子树，如果b的左子树为空，返回none。
        # 再接着创建b的右子树，
        if i < len(list):
            if list[i] == None:
                return None  # 这里的return很重要
            else:
                if self.nodestyle == 0:
                    root = TreeNode(list[i])
                else:
                    root = Node(list[i])
                # 往左递推
                root.left = self.lct(root.left, list, 2*i+1)  # 从根开始一直到最左，直至为空，
                # 往右回溯
                root.right = self.lct(root.right, list, 2*i+2)  # 再返回上一个根，回溯右，
                # 再返回根'
                return root  # 这里的return很重要
        return root