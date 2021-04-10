# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 297 二叉树的序列化与反序列化
# @Content : 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，
#            同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。
#            请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一
#            个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
# @Att     : 说明: 不要使用类的成员 / 全局 / 静态变量来存储状态，你的序列化和反序列化算法应该是无状态的。


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    # 方法一：前序遍历
    def serialize_preorder(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        SEP, NULL = ',', '#'
        string = ''
        def traverse(root):
            nonlocal string
            if not root:
                string += (NULL + SEP)
                return
            # 前序遍历位置
            string += (str(root.val) + SEP)  # 根
            traverse(root.left)              # 左
            traverse(root.right)             # 右
        traverse(root)
        return string

    def deserialize_preorder(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        SEP, NULL = ',', '#'
        datas = data.split(SEP)
        def deser(datas):
            if not datas: return
            # 前序遍历位置
            first = datas.pop(0)  # 列表最左侧就是根节点
            if first == NULL: return
            root = TreeNode(int(first))
            # 先构造左子树，后构造右子树
            root.left = deser(datas)   # 先左
            root.right = deser(datas)  # 后右
            return root
        return deser(datas)


    # 方法二：后序遍历
    def serialize_postorder(self, root):
        SEP, NULL = ',', '#'
        string = ''
        def traverse(root):
            nonlocal string
            if not root:
                string += (NULL + SEP)
                return
            # 前序遍历位置
            traverse(root.left)              # 左
            traverse(root.right)             # 右
            string += (str(root.val) + SEP)  # 根
        traverse(root)
        return string

    def deserialize_postorder(self, data):
        SEP, NULL = ',', '#'
        datas = data.split(SEP)
        def deser(datas):
            if not datas: return
            # 从后往前取出元素
            last = datas.pop()
            if last == NULL: return
            root = TreeNode(int(last))
            # 先构造右子树，后构造左子树
            root.right = deser(datas)  # 先右
            root.left = deser(datas)   # 后左
            return root
        # datas = ['#', '#', '2', '#', '#', '4', '#', '#', '5', '3', '1', '']
        # 由于从后往前取元素，datas最后一个元素是''，显然需要去除
        return deser(datas[0:len(datas)-1])


    # 方法三：中序遍历(无法实现)
    # 中序遍历无法实现反序列化deserialize
    # 要想实现反序列方法，首先要构造root节点。
    #    前序遍历得到的datas列表中，第一个元素是root节点的值；
    #    后序遍历得到的datas[0:len(datas)-1]列表中，最后一个元素是root节点的值
    #    中序遍历root的值夹在两棵子树的中间，也就是在datas列表的中间，我们不知道确切的索引位置，所以无法找到root节点，也就无法反序列化


    # 方法四：层序遍历
    def serialize_levelorder(self, root):
        SEP, NULL = ',', '#'
        string = ''
        def traverse(root):
            nonlocal string
            if not root: return
            queue = [root]
            while queue:
                cur = queue.pop(0)
                # 层序遍历代码位置
                if cur == None:
                    string += (NULL + SEP)
                    continue
                string += (str(cur.val) + SEP)
                queue.append(cur.left)
                queue.append(cur.right)
        traverse(root)
        return string

    def deserialize_levelorder(self, data):
        SEP, NULL = ',', '#'
        if not data: return
        datas = iter(data.split(SEP))      # iter函数：生成迭代器(迭代器的好处是保存当前元素和生成下一个元素的方法，这样可以节约空间)
        root = TreeNode(int(next(datas)))  # next函数：返回迭代器的下一个元素
        queue = [root]
        while queue:
            # 队列中存的都是父节点
            parent = queue.pop(0)
            # 父节点对应的左侧子节点的值
            left = next(datas)
            if left != NULL:
                parent.left = TreeNode(int(left))
                queue.append(parent.left)
            else:
                parent.left = None
            # 父节点对应的右侧子节点的值
            right = next(datas)
            if right != NULL:
                parent.right = TreeNode(int(right))
                queue.append(parent.right)
            else:
                parent.right = None
        return root


if __name__ == '__main__':
    # Your Codec object will be instantiated and called as such:
    # ser = Codec()
    # deser = Codec()
    # ans = deser.deserialize(ser.serialize(root))

    from libs.list2tree import ListCreateTree
    from libs.tree import BinaryTree
    # 你可以将以下二叉树：
    #     1
    #    / \
    #   2   3
    #      / \
    #     4   5
    # 序列化为 "[1,2,3,null,null,4,5]"
    list = [1, 2, 3, None, None, 4, 5]
    Tree = ListCreateTree()
    root = Tree.lct(None, list, 0)

    ser = Codec()
    deser = Codec()

    str_preorder = ser.serialize_preorder(root)
    str_postorder = ser.serialize_postorder(root)
    str_levelorder = ser.serialize_levelorder(root)

    res_preorder = deser.deserialize_preorder(str_preorder)
    res_postorder = deser.deserialize_postorder(str_postorder)
    res_levelorder = deser.deserialize_levelorder(str_levelorder)

    result_preorder = BinaryTree().inorder(res_preorder)
    result_postorder = BinaryTree().inorder(res_postorder)
    result_levelorder = BinaryTree().inorder(res_levelorder)

    print('前序遍历法:', '序列化-->', str_preorder, '反序列化-->', result_preorder)
    print('后序遍历法:', '序列化-->', str_postorder, '反序列化-->', result_postorder)
    print('层序遍历法:', '序列化-->', str_levelorder, '反序列化-->', result_levelorder)