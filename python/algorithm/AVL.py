class TreeNode(object): #트리를 짜기 위해 기본적인 노드설정과 height 추가
    def __init__(self, val=None, left=None, right=None, height=0):
        self.val=val
        self.left=left
        self.right=right
        self.height=height
        
class AVL_Tree:
    def insert(self, n, val):
        if not n: #처음 insert하는 값은 이전에 아무것도 없기에 insert함과 동시에 TreeNode구성
            return TreeNode(val)
        elif val < n.val: #이전에 있던 노드 즉, root보다 작으면 left노드로 insert
            n.left=self.insert(n.left, val)
        elif val > n.val: #이전에 있던 노드 즉, root보다 크면 right노드로 insert
            n.right=self.insert(n.right, val)
        
        n.height = 1 + max(self.getHeight(n.left), self.getHeight(n.right)) #height를 구하는 방식
        
        return self.balance(n)
    
    def balance(self, n):
        if self.checkBalance(n) > 1: #left노드의 height가 right노드의 height보다 2 이상 클 경우
            if self.checkBalance(n.left) < 0: #left노드의 right노드의 height가 더 큰 경우 => LR
                n.left = self.left_Rotate(n.left)
            n = self.right_Rotate(n) # LL
            
        elif self.checkBalance(n) < -1: #right노드의 height가 left노드의 height보다 2 이상 클 경우
            if self.checkBalance(n.right) > 0: #right노드의 left노드의 height가 더 큰 경우 => RL
                n.right = self.right_Rotate(n.right)
            n = self.right_Rotate(n) # RR
        return n # rotation이 다 된 subtree반환
        
        
    def left_Rotate(self, n):
        y = n.right
        n.right = y.left
        y.left = n
        
        n.height = 1 + max(self.getHeight(n.left), self.getHeight(n.right)) # height 변경
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        
        return y
    
    def right_Rotate(self, n):
        y = n.left 
        n.left = y.right
        y.right = n
        
        n.height = 1 + max(self.getHeight(n.left), self.getHeight(n.right)) # height 변경
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        
        return y
        
    def getHeight(self, n):
        if not n: # 아무것도 없으면 height = -1
            return -1
        return n.height
    
    def checkBalance(self, n):
        if not n:
            return 0
        return self.getHeight(n.left) - self.getHeight(n.right)
    
    def preOrder(self, n):
        if not n:
            return
        
        print(n.val, end=" ")
        self.preOrder(n.left)
        self.preOrder(n.right)

AVL = AVL_Tree()
n = None

n = AVL.insert(n, 41)
n = AVL.insert(n, 20)
n = AVL.insert(n, 65)
n = AVL.insert(n, 11)
n = AVL.insert(n, 29)
n = AVL.insert(n, 50)
n = AVL.insert(n, 26)

AVL.preOrder(n)
print()

n = AVL.insert(n, 23)
AVL.preOrder(n)
print()

n = AVL.insert(n, 55)
AVL.preOrder(n)
print()

n = AVL.insert(n, 30)
AVL.preOrder(n)
print()