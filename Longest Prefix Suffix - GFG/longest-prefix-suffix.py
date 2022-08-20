#User function Template for python3

class Solution:
	def lps(self, s):
        lps = [0] * len(s)
    	prevLPS, i = 0, 1
    	
    	while i < len(s):
    	    if s[prevLPS] == s[i]:
    	        lps[i] = prevLPS + 1
    	        prevLPS += 1
    	        i += 1
    	    
    	    elif prevLPS == 0:
    	        lps[i] = 0
    	        i += 1
    		        
    	    else:
    	        prevLPS = lps[prevLPS-1]

        return lps[-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()

		ob = Solution()
		answer = ob.lps(s)
		print(answer)

# } Driver Code Ends