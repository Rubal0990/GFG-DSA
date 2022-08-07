#User function Template for python3
from collections import deque

class Solution:
	def FirstNonRepeating(self, A):
		q = deque()
		ans = ""
		mp = {}
		
		for i in range(len(A)):
		    if A[i] in mp:
		        mp[A[i]] += 1
		        while q and (q[0]==A[i] or mp[q[0]]>1):
		            q.popleft()
	        else:
	            mp[A[i]] = 1
	            q.append(A[i])
	        
	        if not q:
	            ans += '#'
	        else:
	            ans += q[0]
		            
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		A = input()
		ob = Solution()
		ans = ob.FirstNonRepeating(A)
		print(ans)

# } Driver Code Ends