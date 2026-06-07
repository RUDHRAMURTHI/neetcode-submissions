class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        new_node = TreeNode(key, val)
        if self.root is None:
            self.root = new_node
            return
        else:
            curr = self.root
            while True:
                if curr.key > key:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = new_node
                        return
                elif curr.key < key:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = new_node
                        return
                else:
                    curr.val = val
                    return

    def get(self, key: int) -> int:
        curr = self.root
        while curr:
            if curr.key > key:
                curr = curr.left
            elif curr.key < key:
                curr = curr.right
            else:
                return curr.val
        return -1


    def getMin(self) -> int:
        curr = self.root
        if not curr: return -1
        while curr and curr.left:
            curr = curr.left
        return curr.val

    def getMax(self) -> int:
        curr = self.root
        if not curr: return -1
        while curr and curr.right:
            curr = curr.right
        return curr.val

    def findMin(self, node):
        curr = node
        while curr and curr.left:
            curr = curr.left
        return curr

    def removeHelper(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self.removeHelper(root.left, key)
        elif key > root.key:
            root.right = self.removeHelper(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                min_node = self.findMin(root.right)
                root.key = min_node.key
                root.val = min_node.val
                root.right = self.removeHelper(root.right, min_node.key)
                
        return root

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    def getInorderKeys(self) -> List[int]:
        self.res =[]
        self.inorderTraversal(self.root)
        return self.res

    def inorderTraversal(self, root):
        if root is None:
            return
        self.inorderTraversal(root.left)
        self.res.append(root.key)
        self.inorderTraversal(root.right)