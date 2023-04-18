#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''

class Solution:
    def check(self, node, mini, maxi):
        if node is None:
            return True
        
        if node.data < mini or node.data > maxi:
           return False
        
        return (self.check(node.left, mini, node.data - 1) and
            self.check(node.right, node.data+1, maxi))
    
    def solve(self, root, ans, target, k):
        maxi = 4294967296
        mini = -4294967296
        if root == None:
            return (0, 0)
        
        left, l = self.solve(root.left, ans, target, k)
        right, r = self.solve(root.right, ans, target, k)
        if left + right + root.data == target and self.check(root, mini, maxi) == True:
            if self.s > l + r + 1:
                self.s = l + 1 + r
        
        return (left + right + root.data, l + r + 1)   
    
    def minSubtreeSumBST(self, target, root):
        self.s = 10000
        ans, s = self.solve(root, 0, target, 0)
        
        if self.s == 10000:
            return -1
        
        return self.s


#{ 
 # Driver Code Starts.

#Initial Template for Python 3
from collections import defaultdict
from collections import deque
from sys import stdin, stdout
from math import inf
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
    test_cases = int(input())
    for _ in range (test_cases):
        target = int(input())
        N = input()
        root = buildTree(N)
        res = Solution().minSubtreeSumBST(target, root)
        print(res)
# } Driver Code Ends