#User function Template for python3

class Solution:
    def find_permutation(self, S):
        if len(S)==1:
            return [S]
        
        perms = self.find_permutation(S[1:])
        
        char = S[0]
        result = []
        for perm in perms:
            for i in range(len(perm)+1):
                result.append(perm[:i]+char+perm[i:])

        result.sort()
        ans = []
        for i in result:
            if i not in ans:
                ans.append(i)
     
        return ans


#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S=input()
		ob = Solution()
		ans = ob.find_permutation(S)
		for i in ans:
			print(i,end=" ")
		print()
# } Driver Code Ends