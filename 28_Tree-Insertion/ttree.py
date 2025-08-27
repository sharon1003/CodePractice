class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
        #Enter you code here.
        node = Node(val)
        if not self.root:
            self.root = node
            return
            
        queue = [self.root]
        level = 1
        num_node = 1
        while queue:
            if num_node > 2**level:
                temp_node = queue.pop(0)
            else:
                continue

            if temp_node.left is None:
                temp_node.left = node
                num_node += 1
            elif temp_node.right is None:
                temp_node.right = node
                num_node += 1          
        

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
