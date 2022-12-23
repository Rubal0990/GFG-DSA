#User function Template for python3
from math import sqrt

class Solution:
	def threeDivisors(self, query, q):
	    m = int(sqrt(max(query)))
	    prime = [True] * (m + 1)
	    prime[0], prime[1] = False, False
	    
	    for i in range(2, len(prime)):
	        if not prime[i]:
	            continue
	        
	        for j in range(i*i, len(prime), i):
	            prime[j] = False
	    
	    prime = [i for i, e in enumerate(prime) if e]
	    
	    ans = [0] * q
	    for i in range(q):
	        for k in prime:
	            if k*k > query[i]:
	                break
	            
	            ans[i] += 1
	    
	    return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		q = int(input())
		query = []
		for _ in range(q):
			query.append(int(input()))
		
		ob = Solution()
		ans = ob.threeDivisors(query,q)
		for a in ans:
			print(a)

# } Driver Code Ends