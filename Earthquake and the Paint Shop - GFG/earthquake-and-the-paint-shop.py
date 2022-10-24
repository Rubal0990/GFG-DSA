#User function Template for python3

class alphanumeric:
    def __init__(self, name, count):
        self.name = name
        self.count = count

class Solution:
    def sortedStrings(self, N, A):
        m = {}
        
        for e in A:
            if e not in m:
                m[e] = 0
            
            m[e] += 1
        
        b = set(A)
        c = list(b)
        c.sort()
        
        return [alphanumeric(x, m[x]) for x in c]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        a=[]
        for i in range(N):
            x=input()
            a.append(x)
        ob=Solution()
        ans=ob.sortedStrings(N,a)
        for i in ans:
            print(i.name,end=" ")
            print(i.count)
# } Driver Code Ends