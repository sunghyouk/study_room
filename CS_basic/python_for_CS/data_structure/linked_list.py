class Node:
    def __init__(self, data=None):

        """
        data : 노드는 데이터 부분과
        next : 다음 노드를 가리키는 참조 부분을 가진다.
        """
        self.__data = data
        self.__next = None

    def __del__(self):
        print("data of {} is deleted".format(self.data))

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, n):
        self.__next = n


class Linked_list:
    def __init__(self):
        # 연결 리스트의 첫번째 노드
        self.head = None

        # 연결 리스트의 마지막 노드
        self.tail = None

        # 데이터 개수
        self.d_size = 0


def empty(self):
    if self.d_size == 0:
        return True
    else:
        return False


def size(self):
    return self.d_size


def append(self, data):
    # 삽입할 노드를 만든다
    new_node = Node(data)

    # 1) 리스트가 비어있을 때
    if self.empty():
        self.head = new_node
        self.tail = new_node
        self.d_size += 1

    # 2) 데이터가 한 개 이상 있을 때
    else:
        self.tail.next = new_node
        self.tail = new_node
        self.d_size += 1


def search_target(self, target, start=0):
    """
    start로부터 target과 일치하는 첫 번째 데이터와 그 위치를 반환
    target이 존재하지 않을 때 (None, None)
    """
    if self.empty():
        return None

    # 첫 번째 노드
    pos = 0
    # 노드의 순회 코드
    cur = self.head
    # pos가 start보다 클 때만 대상 데이터와 현재 노드의 데이터를 비교
    if pos >= start and target == cur.data:
        return cur.data, pos

    while cur.next:
        pos += 1
        # 노드의 순회 코드
        cur = cur.next
        if pos >= start and target == cur.data:
            return cur.data, pos

    return None, None


def search_pos(self, pos):
    """
    search_pos(pos) -> data
    pos가 범위를 벗어나면 -> None
    """

    if pos > self.size() - 1:
        return None

    cnt = 0
    cur = self.head
    if cnt == pos:
        return cur.data

    while cnt < pos:
        cur = cur.next
        cnt += 1

    return cur.data


def remove(self, target):
    if self.empty():
        return None

    # bef(ore): cur(rent) node의 이전 노드를 가리킴
    bef = self.head
    cur = self.head

    # 1) 삭제할 노드가 첫 번째 일 때
    if target == cur.data:
        # 1-1) 데이터가 하나일 때
        if self.size() == 1:
            self.head = None
            self.tail = None
        # 1-2) 데이터가 2개 이상일 때
        else:
            self.head = self.head.next
        self.d_size -= 1
        return cur.data

    while cur.next:
        bef = cur
        cur = cur.next
        # 2) 삭제할 노드가 첫 번째가 아닐 때
        if target == cur.data:
            # 2-1) 삭제할 노드가 마지막 노드일 때
            if cur == self.tail:
                self.tail = bef
            # 2-2) 일반적인 경우
            bef.next = cur.next
            self.d_size -= 1
            return cur.data

    return None


def show_list(slist):
    if slist.empty():
        print('The list is empty')
        return

    for i in range(slist.size()):
        print(slist.search_pos(i), end=' ')
