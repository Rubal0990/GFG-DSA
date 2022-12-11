#User function Template for python3

class Solution:
    def maxIndexDiff(self, A, n): 
        if n == 1:
            return 0
        
        s = 0
        L = [A[0]]
        R = [-1] * n
        r = A[n-1]
        
        for i in range(1, n):
            L.append(min(A[i], L[i-1]))
        
        for j in range(n-1, -1, -1):
            if r < A[j]:
                r = A[j]
            
            R[j] = max(r, A[j])
        
        i, j = 0, 0
        while i < n and j < n:
            if L[i] <= R[j]:
                w = j - i
                s = max(s, w)
                j += 1
            else:
                i += 1
        
        return s


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            ob=Solution()
            print(ob.maxIndexDiff(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends