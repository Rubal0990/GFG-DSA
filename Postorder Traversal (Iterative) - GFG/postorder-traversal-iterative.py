#User function Template for python3

'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    from collections import deque
    
    def postOrder(self,node):
        parent = {}
        temp = node
        q = deque()
        q.append(temp)
        parent[temp] = -1
        
        while(q):
            size = len(q)
            
            while(size):
                ele = q.popleft()
                if ele.left:
                    parent[ele.left] = ele
                    q.append(ele.left)
        
                if ele.right:
                    parent[ele.right] = ele
                    q.append(ele.right)
        
                size-=1
        
        ans = []
        while(True):
            
            if node.left == None and node.right == None and parent[node] == -1:
                ans.append(node.data)
                break
            
            while(node.left):
                node = node.left
            
            if node.left == None and node.right == None:
                ans.append(node.data)
            
                if parent[node].left and  node.data == parent[node].left.data:
                    parent[node].left = None
            
                else:
                    parent[node].right = None
                node = parent[node]
            
            if node.right:
                node = node.right
            
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3

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
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        ob = Solution()
        res = ob.postOrder(root)
        for i in range (len(res)):
            print (res[i], end = " ")
        print()
        
        


# } Driver Code Ends