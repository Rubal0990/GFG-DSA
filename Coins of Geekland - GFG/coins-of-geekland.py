#User function Template for python3

class Solution:
    def Maximum_Sum(self, mat, N, K):
        
        # Prefix Matrix
        for i in range(N):
            for j in range(N):
                if i-1 >= 0:
                    mat[i][j] += mat[i-1][j]
                if j-1 >= 0:
                    mat[i][j] += mat[i][j-1]
                if i-1 >= 0 and j-1 >= 0:
                    mat[i][j] -= mat[i-1][j-1]
        
        ans = 0
        for i in range(N):
            for j in range(N):
                local_sum = mat[i][j]
                if i-K >= 0:
                    local_sum -= mat[i-K][j]
                if j-K >= 0:
                    local_sum -= mat[i][j-K]
                if i-K >= 0 and j-K >= 0:
                    local_sum += mat[i-K][j-K]
                
                ans = max(ans, local_sum)
                
        return ans
                

#{ 
#  Driver Code Starts
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        matrix=[]
        for _ in range(n):
            matrix.append( [ int(x) for x in input().strip().split() ] )
        k=int(input())
        obj = Solution()
        print(obj.Maximum_Sum(matrix,n,k))
# } Driver Code Ends