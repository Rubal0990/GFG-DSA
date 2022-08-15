#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''

class Solution:
    def NumberOFTurns(self, root, first, second):
        def _get_path(nd, tgt, path):
            if not nd: return False
            path.append(nd)
            if nd.data == tgt: return True
            if _get_path(nd.left, tgt, path): return True
            if _get_path(nd.right, tgt, path): return True
            path.pop()
            return False
        
        def _count_turn(p):
            ans = 0
            for i in range(lca+1, len(p)-1):
                if p[i-1].left == p[i] and p[i].right == p[i+1] or p[i-1].right == p[i] and p[i].left == p[i+1]:
                    ans += 1
            return ans
        
        p1, p2 = [], []
        _get_path(root, first, p1)
        _get_path(root, second, p2)
        minL = min(len(p1), len(p2))
        lca = next( (i for i in range(minL-1) if p1[i+1] != p2[i+1]), minL-1 )
        ans = 1 if lca != minL-1 else 0
        ans += _count_turn(p1) + _count_turn(p2)
        return ans


#{ 
 # Driver Code Starts
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
        n1,n2=list(map(int, input().strip().split())) 
        ob = Solution()
        turn = ob.NumberOFTurns(root,n1,n2)
        if turn!=0:
            print(turn)
        else:
            print(-1)
# } Driver Code Ends