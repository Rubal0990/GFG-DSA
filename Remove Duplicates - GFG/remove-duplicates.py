#User function Template for python3
class Solution:
	def removeDups(self, S):
        p = ""
        
        for char in S:
            if char not in p:
                p = p+char
            
        return p

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		
		ob = Solution()	
		answer = ob.removeDups(s)
		
		print(answer)


# } Driver Code Ends