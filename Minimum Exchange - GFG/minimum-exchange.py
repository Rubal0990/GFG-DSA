#User function Template for python3

class Solution:
	def MinimumExchange(self, matrix):
		n = len(matrix[0])
        m = len(matrix)
        tA = 0
        
        for i in range(m):
            for j in range(n):
                if (i+j)%2 == 0:
                    if matrix[i][j] == 'B':
                        tA += 1
                
                else:
                    if matrix[i][j] == 'A':
                        tA += 1
        
        return min(tA, m*n-tA)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		matrix = []
		for _ in range(n):
			cur  = input()
			temp = []
			for __ in cur:
				temp.append(__)
			matrix.append(temp)
		obj = Solution()
		ans = obj.MinimumExchange(matrix)
		print(ans)

# } Driver Code Ends