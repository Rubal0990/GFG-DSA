#User function Template for python3

class Solution():
    def solve(self, N, A):
        if A[N-1] < 9:
            return N
        
        else:
            for i in range(N-1, -1, -1):
                if A[i] < 9:
                    return i + 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(int(input())):
    n = int(input())
    array=[int(i) for i in input().split()]
    obj = Solution()
    print(obj.solve(n, array))
# } Driver Code Ends
