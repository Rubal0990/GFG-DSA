'''
# node class:

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''
class Solution:
    def sum_at_distK(self,root, target, k):
        def build_path(node, parent, path):
            if not node:
                return None
            
            path[node] = parent
            if node.data == target:
                return node

            return build_path(node.left, node, path) or build_path(node.right, node, path)
        
        def travese(n, k, visited):
            if not n or n in visited or k < 0:
                return
            
            nonlocal s
            visited.add(n)
            s += n.data
            
            travese(n.left, k-1, visited)
            travese(n.right, k-1, visited)
        
        path = {}
        start = build_path(root, None, path)
        visited = set()
        s = 0
        while start and k >= 0:
            travese(start, k, visited)
            start = path[start]
            k -= 1
        
        return s



#{ 
#  Driver Code Starts
#driver code:
from collections import deque

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input()
        root=buildTree(line)
        line=input().strip().split()
        target=int(line[0])
        k=int(line[1])
        obj=Solution()
        print(obj.sum_at_distK(root,target,k))


# } Driver Code Ends