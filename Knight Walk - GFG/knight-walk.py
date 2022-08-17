class Solution:
	def minStepToReachTarget(self, S, Target, N):
		S = [S[0]-1, S[1]-1]
        Target = [Target[0]-1, Target[1]-1]
        dx = [-1, -2, -2, -1, 1, 2, 2, 1]
        dy = [-2, -1, 1, 2, 2, 1, -1, -2]
        
        visited = [[0 for i in range(N)] for j in range(N)]
        queue = [(0, S[0], S[1])]
        visited[S[0]][S[1]] = 1
        
        while queue:
            d, r, c = queue.pop(0)
            if r==Target[0] and c==Target[1]:
                return d
            
            for i in range(8):
                x, y = r+dx[i], c+dy[i]
                
                if x>=0 and y>=0 and x<N and y<N and visited[x][y]==0:
                    visited[x][y] = 1
                    queue.append((d+1, x, y))


#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		KnightPos = list(map(int, input().split()))
		TargetPos = list(map(int, input().split()))
		obj = Solution()
		ans = obj.minStepToReachTarget(KnightPos, TargetPos, N)
		print(ans)

# } Driver Code Ends