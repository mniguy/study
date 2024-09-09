from tkinter.messagebox import NO


class Node:
    def __init__(self, x=None, left=None, right=None):
        self.val=x
        self.left=left
        self.right=right
        
def balancedBST(arr):
    if not arr:
        return None
        
    mid = len(arr)//2 
        
    root = Node(arr[mid])
        
    root.left = balancedBST(arr[:mid]) #mid를 기준으로 왼쪽과 오른쪽으로 나눠서 각각 함수를 다시 돌려줌
    root.right = balancedBST(arr[mid+1:]) 
        
    return root #recursion을 할 수 없을때까지 계속해서 root값을 return

def preOrder(node):
    if not node:
        return
    
    print(node.val, end=" ")
    preOrder(node.left)
    preOrder(node.right)

arr=[1,2,3,4,5,6,7]
root = balancedBST(arr)
preOrder(root)