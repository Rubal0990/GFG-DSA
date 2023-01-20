#User function Template for python3

class Solution():
    def maxWeightCell(self, N, Edge):
        arr = [0] * N
        
        for x in range(N):
            if Edge[x] != -1:
                arr[Edge[x]] += x
        
        return arr.index(max(arr))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        Edge = [int(i) for i in input().split()]
        obj = Solution()
        ans=obj.maxWeightCell(N, Edge);
        print(ans)

# } Driver Code Ends