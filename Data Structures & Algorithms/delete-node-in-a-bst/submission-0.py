# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
     # def findMax(root):
        #     curr = root
        #     while curr and curr.right:
        #         curr = curr.right
        #     return curr.val
        
        def findMin(root):
            curr = root
            while curr and curr.left:
                curr = curr.left
            return curr.val
        
        if not root:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                # max_val = findMax(root.left)
                # root.val = max_val
                # root.left = self.deleteNode(root.left, max_val)

                min_val = findMin(root.right)
                root.val = min_val
                root.right = self.deleteNode(root.right, min_val)
        return root
        