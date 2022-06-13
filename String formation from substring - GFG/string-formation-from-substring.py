#User function Template for python3
class Solution:
	def isRepeat(self, s):
		le = len(s)
        
        for i in range(le//2):
            rep = le // (i + 1)
            if s[:i+1]*rep == s:
                return 1
        
        return 0

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		
		ob = Solution()	
		answer = ob.isRepeat(s)
		
		print(answer)


# } Driver Code Ends