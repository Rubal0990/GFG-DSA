#User function Template for python3
import math

class Solution:
    def isPrime(self, N):
        if N < 2:
            return False
		    
        max_div = math.floor(math.sqrt(N))
        for i in range(2, max_div+1):
            if N%i == 0:
                return False
        
        return True
	
	def NthTerm(self, N):
		x, y = N, N
		
		while x > 1:
            if self.isPrime(x):
                break
            x -= 1
        
        while True:
            if self.isPrime(y):
                break
            y += 1
        
        if not self.isPrime(x):
            return y - N
        
        return min(abs(N-x), abs(N-y))
	        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.NthTerm(N)
		print(ans)

# } Driver Code Ends