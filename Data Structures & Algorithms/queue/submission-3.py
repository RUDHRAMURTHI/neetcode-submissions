class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head

    def isEmpty(self) -> bool:
        if self.head == self.tail:
            return True
        else:
            return False

    def append(self, value: int) -> None:
        new_node = Node(value)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = self.tail.next

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        new_node.next = self.head.next
        if self.head.next:
            self.head.next.prev = new_node
        else:
            self.tail = new_node
        new_node.prev = self.head
        self.head.next = new_node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        else:
            cur = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            cur.prev = None
            return cur.value
        
    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        else:
            cur = self.head.next
            self.head.next = self.head.next.next
            if self.head.next:
                self.head.next.prev = self.head
            else:
                self.tail = self.head
            cur.next = None
            cur.prev = None
            return cur.value
    # def getlist(self) -> list:
    #     res = []
    #     cur = self.head.next
    #     while cur:
    #         res.append(cur.value)
    #         cur = cur.next
    #     return res
            