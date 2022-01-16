
class cell:
    def __init__(self, x = 0, y = 0, dist = 0):
        self.x = x
        self.y = y
        self.dist = dist
    
def isInside(x, y, N):
    if (x >= 1 and x <= N and y >= 1 and y <= N):
        return True
    return False

class Solution:
    #Function to find out minimum steps Knight needs to reach target position.
    def minStepToReachTarget(self, KnightPos, TargetPos, N):
    		
        dx = [2, 2, -2, -2, 1, 1, -1, -1]
        dy = [1, -1, 1, -1, 2, -2, 2, -2]
        
        queue = []
    
        queue.append(cell(KnightPos[0], KnightPos[1], 0))
        
        visited = [[False for i in range(N + 1)] for j in range(N + 1)]
        
        visited[KnightPos[0]][KnightPos[1]] = True
        
        while(len(queue) > 0):
        
            t = queue[0]
            queue.pop(0)
            
            if(t.x == TargetPos[0] and t.y == TargetPos[1]):
                return t.dist
        
        
            for i in range(8):
            
                x = t.x + dx[i]
                y = t.y + dy[i]
            
                if(isInside(x, y, N) and not visited[x][y]):
                    visited[x][y] = True
                    queue.append(cell(x, y, t.dist + 1))
        

#{ 
#  Driver Code Starts

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