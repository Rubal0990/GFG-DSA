#User function Template for python3

class Solution:
	def characterReplacement(self, s, k):
		lookup = {}
		maxCount = 0
		i = 0
		j = 0
		res = 0
		
		for j in range(len(s)):
		    lookup[s[j]] = 1 + lookup.get(s[j], 0)
		    maxCount = max(maxCount, lookup[s[j]])
		    
		    while (j-i+1)-maxCount > k:
		        lookup[s[i]] -= 1
		        i += 1
		    
		    res = max(res, j-i+1)
	    return res  


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		k = int(input())
		ob = Solution()
		ans = ob.characterReplacement(s, k)
		print(ans)

# } Driver Code Ends