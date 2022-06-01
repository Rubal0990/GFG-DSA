#User function Template for python3

class Solution:
    def shiftPile(self, N, n):
        arr = []
        self.solve('1', '2', '3', N, arr)
        return arr[n-1]
        
    def solve(self, src, temp, dest, N, arr):
        if N == 0:
            return
        
        self.solve(src, dest, temp, N-1, arr)
        arr.append([src, dest])
        
        self.solve(temp, src, dest, N-1, arr)
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, n = [int(x) for x in input().split()]
        
        ob = Solution()
        ans = ob.shiftPile(N, n)
        print(ans[0]+" "+ans[1])
# } Driver Code Ends