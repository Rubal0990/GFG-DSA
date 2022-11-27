#User function Template for python3

class Solution:
	def findSubarray(self, a, n):
    	  c, m, l, r = 0, 0, 0, 0
    	  Start, Finish = 0, 0
        x = []
        
        for i in range(n):
            if a[i] < 0:
                l = i + 1
                r = i + 1
                c = 0
            else:
                c += a[i]
                r += 1
                if c >= m:
                   m = c
                   Start, Finish = l, r
       
        for i in range(Start, Finish):
            x.append(a[i])
        
        if not x:
            return [-1]
        else:
            return x


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

	tc=int(input())
	while tc > 0:
	    n=int(input())
	    a=list(map(int, input().strip().split()))
	    ob = Solution()
	    ans=ob.findSubarray(a, n)
	    for x in ans:
	        print(x, end=" ")
	    print()
	    tc=tc-1
# } Driver Code Ends