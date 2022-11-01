#User function Template for python3
from bisect import bisect

class Solution:
    def median(self, matrix, R, C):
    	low = 1
        high = 2001
        
        while low < high:
            mid = (low+high) // 2
            count = 0
            
            for row in range(R):
                count += bisect(matrix[row], mid)
            
            if count <= (R*C)//2:
                low = mid + 1
            else:
                high = mid
        
        return low


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        r,c = map(int,input().strip().split())
        matrix = [[0 for j in range(c)] for i in range(r)]
        for i in range(r):
            t=[int(el) for el in input().split()]
            for j in range(c):
                matrix[i][j]=t[j]
        ans = ob.median(matrix, r, c);
        print(ans)
# } Driver Code Ends