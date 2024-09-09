class Node(object):
    def __init__(self, key=None):
        self.val = key
        self.left = None
        self.right = None

class BST(object):
    def insert(self, root, key):
        if not root:
            return Node(key)
    
        if root.val < key:
            root.right = self.insert(root.right, key)
        else:
            root.left = self.insert(root.left, key)
        return root

    def search(self, root, key):
        if root is None or root.val == key:
            return root
        if root.val < key:
            return self.search(root.right, key)
        return self.search(root.left, key)
    
    def findmin(self, root):
        if root is None:
            return root
        if root.left is None:
            return root.val
        return self.findmin(root.left)
    
    def preOrder(self, root):
        if not root:
            return
        
        print(root.val, end=" ")
        self.preOrder(root.left)
        self.preOrder(root.right)
    
    def inOrder(self, root):
        if not root:
            return
        
        self.inOrder(root.left)
        print(root.val, end=" ")
        self.inOrder(root.right)
    
    def postOrder(self, root):
        if not root:
            return
        
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.val, end=" ")
        
    
b = BST()
root = None

root = b.insert(root, 20)
root = b.insert(root, 41)
root = b.insert(root, 65)
root = b.insert(root, 11)
root = b.insert(root, 29)
root = b.insert(root, 26)
root = b.insert(root, 50)
b.inOrder(root)

print(b.search(root, 11))