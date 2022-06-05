#User function template for Python
import math

class Solution:	
	def buzzTime(self, N, M, L, H, A):
		def ok(h):
		    s = 0
		    for a0, acc in zip(H, A):
		        speed = a0 + acc * h
		        if speed > L:
		            s += speed
		    
		    return s >= M
		  
		lo, hi = 0, math.ceil(M // max(A)) + math.ceil(L / max(A))
		
		while lo < hi:
		    mi = lo + (hi - lo) // 2
		    if ok(mi):
		        hi = mi
		    else:
		        lo = mi + 1
		        
		return lo

#{ 
#  Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, M, L = [int(x) for x in input().split()]
        H = [0 for x in range(N)]
        A = [0 for x in range(N)]
        for i in range(N):
            H[i], A[i] = [int(y) for y in input().split()]
        ob = Solution()
        print(ob.buzzTime(N, M, L, H, A))

# } Driver Code Ends