#User function Template for python3

class Solution:
	def FindWays(self, maze):
        RYTE, DOWN = 1, 2
		n = len(maze)
		
	    def wtf(p): 
	        return(p % 1000000007)
		
        def cons(): 
            return [[0]*n for _ in range(n)]
        
        adv = cons()
        adv[0][0] = maze[0][0]
        pts = cons()
        pts[0][0] = 1
        
        for j in range(1, n):
            if maze[0][j-1] == DOWN: 
                break
            adv[0][j] = adv[0][j-1] + maze[0][j]
            pts[0][j] = 1
            
        for i in range(1, n):
            if maze[i-1][0] == RYTE: 
                break
            adv[i][0] = adv[i-1][0] + maze[i][0]
            pts[i][0] = 1
            
        for i in range(1, n):
            for j in range(1, n):
                if maze[i-1][j] != RYTE and pts[i-1][j]:
                    adv[i][j] = adv[i-1][j] + maze[i][j]
                    pts[i][j] = pts[i-1][j]
                if maze[i][j-1] != DOWN and pts[i][j-1]:
                    adv[i][j] = max(adv[i][j], adv[i][j-1] + maze[i][j])
                    pts[i][j] += pts[i][j-1]
                    
        if not pts[-1][-1]: 
            return 0, 0
        
        return wtf( pts[-1][-1]), adv[-1][-1]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		matrix = []
		for _ in range(n):
			cur = list(map(int, input().split()))
			matrix.append(cur)
		obj = Solution()
		ans = obj.FindWays(matrix)
		for _ in ans:
			print(_, end = " ")
		print()

# } Driver Code Ends