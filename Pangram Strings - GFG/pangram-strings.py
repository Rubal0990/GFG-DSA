#User function Template for python3
class Solution:
	def isPanagram(self, S):
	    k = set()
        S = S.lower()
        
        for i in S:
            if i.isalpha():
                k.add(i)
        
        return 1 if len(k) == 26 else 0

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.isPanagram(S)
		print(answer)

# } Driver Code Ends