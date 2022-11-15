#User function Template for python3

class Solution:
    def longestPerfectPiece(self, arr, N):
        ans = 1
        i = 0
        
        while i < N:
            j = i + 1
            while j < N and abs(arr[j] - arr[i]) <= 1:
                j += 1
            
            ans = max(ans, j - i);
            i = j
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.longestPerfectPiece(arr,N))
# } Driver Code Ends