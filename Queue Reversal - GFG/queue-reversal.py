#User function Template for python3

class Solution:
    def rev(self, q):
        stack = []
        
        while q.qsize() != 0:
            x = q.get()
            stack.append(x)
        
        while len(stack) != 0:
            x = stack.pop()
            q.put(x)
        
        return q


#{ 
 # Driver Code Starts

#Initial Template for Python 3

from queue import Queue
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        q=Queue(maxsize=n)
        for j in a:
            q.put(j)
            
        ob = Solution()
        q=ob.rev(q)
        for i in range(0,n):
            print(q.get(),end=" ")
        print()
# } Driver Code Ends