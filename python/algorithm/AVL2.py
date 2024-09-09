class Node(object):
    def __init__(self, x=None):
        self.val=x
        self.left=None
        self.right=None
        self.height=0

class AVL_Tree(object):
    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key<root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
            
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        
        balance = self.getBalance(root)
        
        if balance>1 and key<root.left.val:
            return self.rightRotate(root)
        
        if balance<-1 and key>root.right.val:
            return self.leftRotate(root)
        
        if balance>1 and key>root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        
        if balance<-1 and key<root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        
        return root
            
        
    def leftRotate(self, z):
        y=z.right
        T2=y.left
        
        y.left=z
        z.right=T2
        
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.left))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y        
    
    def rightRotate(self, z):
        y=z.left
        T3=y.right
        
        y.right=z
        z.left=T3
        
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.left))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y   
        
    def getHeight(self, root):
        if not root:
            return -1
        
        return root.height
        
    def getBalance(self, root):
        if not root:
            return 0
        
        return self.getHeight(root.left) - self.getHeight(root.right)
    
    def preOrder(self, root):
        if not root:
            return
        
        print("{0} ".format(root.val), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)
        
AVL = AVL_Tree()
root = None

root = AVL.insert(root, 41)
root = AVL.insert(root, 20)
root = AVL.insert(root, 65)
root = AVL.insert(root, 11)
root = AVL.insert(root, 29)
root = AVL.insert(root, 50)
root = AVL.insert(root, 26)

AVL.preOrder(root)
print()

root = AVL.insert(root, 23)
AVL.preOrder(root)
print()

root = AVL.insert(root, 55)
AVL.preOrder(root)
print()

root = AVL.insert(root, 30)
AVL.preOrder(root)
print()



