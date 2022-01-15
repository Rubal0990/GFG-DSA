#User function Template for python3
class Solution:
	def balancedNumber(self, N):
		str1 = str(N)
		n = len(str1)
        l, r = 0, 0
        
        mid = int(n/2)
        
        for x in range(mid):
            l += int(str1[x])
        
        for y in range(mid+1, n):
            r += int(str1[y])
            
        if l != r:
            return False
        else:
            return True
		    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		N = input ()
		ob = Solution()
		if ob.balancedNumber(N):
			print (1)
		else:
			print (0) 
# } Driver Code Ends