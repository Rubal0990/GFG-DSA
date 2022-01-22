#User function Template for python3
class Solution:
	def countSubstr(self, S):
		count = 0
		res = 1
        n = len(S)
        
        for i in range(n):
            if S[i] == '1':
                count += 1
            res = int(count*(count-1)/2)
        
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		s = input ()
		ob = Solution()
		print (ob.countSubstr (s))

	# Contributed By: Pranay Bansal
# } Driver Code Ends