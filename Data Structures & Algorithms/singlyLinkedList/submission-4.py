class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        cur = self.head
        i = 0
        while cur:
            if i == index:
                return cur.value
            cur = cur.next
            i+=1
        return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node       

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
    def remove(self, index: int) -> bool:
        cur = self.head
        pre = self.head
        i = 0
        while cur:
            if i == index:
                print("Item detected")
                pre.next = cur.next
                # cur.next = None
                if cur == self.tail:
                    print("current Item is tail")
                    self.tail = pre
                if cur == self.head:
                    print("current Item is head")
                    self.head = pre.next
                cur.next = None
                return True
            pre = cur
            cur = cur.next
            i+=1
        return False

    def getValues(self) -> List[int]:
        arr =[]
        cur = self.head
        while cur:
            arr.append(cur.value)
            cur = cur.next
        return arr

