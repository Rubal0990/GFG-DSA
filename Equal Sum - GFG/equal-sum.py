#User function Template for python3
class Solution:
	def equilibrium(self,arr, n): 
    	left = 0
        sum = 0
        right = 0
        
        for i in range(n):
            sum += arr[i]
            
        for i in range(n):
            left += arr[i]
          
            if left == right:
                return "YES"
            
            right = sum - left
        
        return "NO"

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

	
	tc=int(input())
	while tc > 0:
	    n=int(input())
	    a=list(map(int , input().strip().split()))
	    ob = Solution()
	    ans=ob.equilibrium(a, n)
	    print(ans)
	    tc=tc-1
# } Driver Code Ends