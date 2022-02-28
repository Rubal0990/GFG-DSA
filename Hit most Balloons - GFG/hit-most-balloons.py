#User function Template for python3

class Solution: 
    def mostBalloons(self, N, arr):
        ans = 1
        
        for i in range(N):
            count = dict()
            same_pos = 0
            
            for j in range(N):
                x_diff = arr[j][0] - arr[i][0]
                y_diff = arr[j][1] - arr[i][1]
                
                if x_diff == 0 and y_diff == 0:
                    same_pos += 1
                else:
                    slope = float("inf") if y_diff == 0 else x_diff / y_diff
                    count[slope] = count.get(slope, 0) + 1
                
            ans = max(ans, max(count.values()) + same_pos)
            
        return ans
                    
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N = int(input()) 
        arr=[[] for j in range(N)]
        for j in range(2): 
            inp = [int(i) for i in input().split()] 
            for i in range(N): 
                arr[i].append(inp[i])
        ob = Solution()
        print(ob.mostBalloons(N, arr))
        
        T -= 1
# } Driver Code Ends