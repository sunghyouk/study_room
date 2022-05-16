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

    def __remove_recursion(self, cur, target):
        # 대상 데이터가 트리 안에 없을 때
        if cur is None:
            return None, None

        # 대상 데이터가 노드 데이터보다 작으면 -> 왼쪽 자식에서 대상 데이터를 가진 노드를 지운다.
        elif target < cur.data:
            cur.right, rem_node = self.__remove_recursion(cur.left, target)
        # 대상 데이터가 노드 데이터보다 크면 -> 오른쪽 자식에서 대상 데이터를 가진 노드를 지운다.
        elif target > cur.data:
            cur.right, rem_node = self.__remove_recursion(cur.right, target)

        # target == cur.data
        else:
            # 1. 리프 노드일 때
            if not cur.left and not cur.right:
                rem_node = cur
                cur = None
            # 2-1. 자식 노드가 왼쪽에 하나 있을 때
            elif not cur.right:
                rem_node = cur
                cur = cur.left
            # 2-2. 자식 노드가 오른쪽에 하나 있을 때
            elif not cur.left:
                rem_node = cur
                cur = cur.right
            # 3. 자식 노드가 두 개일 때
            else:
                # 4. 대체 노드를 찾는다.
                replace = cur.left
                while replace.right:
                    replace = replace.right
                # 5. 삭제 노드와 대체 노드의 값을 교환
                cur.data, replace.data = replace.data, cur.data
                # 6. 대체 노드를 삭제하면서 삭제된 노드를 반환
                cur.left, rem_node = self.__remove_recursion(cur.left, replace.data)
        return cur, rem_node

    def remove(self, target):
        self.root, removed_node = self.__remove_recursion(self.root, target)
        removed_node.left = removed_node.right = None

        return removed_node
