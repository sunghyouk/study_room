# 이진 트리 기반 - 이진 탐색 트리 만들기

from binary_tree import TreeNode


class BST:
    # 이진 트리와 같음
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def preorder_traverse(self, cur, f):
        if not cur:
            return

        f(cur.data)
        self.preorder_traverse(cur.left, f)
        self.preorder_traverse(cur.right, f)

    # insert() implementation
    def insert(self, data):
        new_node = TreeNode()
        new_node.data = data

        cur = self.root

        if cur is None:
            self.root = new_node
            return

        while True:
            parent = cur
            if data < cur.data:
                cur = cur.left
                if not cur:
                    parent.left = new_node
                    return
            else:
                cur = cur.right
                if not cur:
                    parent.right = new_node
                    return

    # search() implementation
    def search(self, target):
        cur = self.root

        while cur:
            if target == cur.data:
                return cur
            elif target < cur.data:
                cur = cur.left
            elif target > cur.data:
                cur = cur.right

        return cur

# TODO: def __remove_recursion

    def remove(self, target):
        self.root, removed_node = self.__remove_recursion(self.root, target)
        removed_node.left = removed_node.right = None

        return removed_node
