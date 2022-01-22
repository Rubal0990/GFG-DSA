#User function Template for python3
class Solution:
	def countSubstr(self, S):
		res = 0
        
        for i in range(len(S)):
            if S[i] == '1':
                res += 1
        
        # Return count of possible pairs of 1's
        return res*(res - 1) // 2

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