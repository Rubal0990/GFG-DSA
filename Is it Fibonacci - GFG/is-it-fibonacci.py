#User function Template for python3

class Solution():
    def solve(self, N, K, GeekNum):
        n = len(GeekNum)-1
        
        if N == n + 1:
            return GeekNum[-1]
        
        if N < n + 1:
            return GeekNum[N - 1]
        
        i = n - (K-1)
        j = n
        s = sum(GeekNum[i: j+1])
        
        while n + 1 < N:
            GeekNum.append(s)
            n += 1
            s -= GeekNum[i]
            i += 1
            j += 1
            s += GeekNum[j]
        
        return GeekNum[-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        N,K=map(int,input().split())
        GeekNum = [int(i) for i in input().split()]
        print(Solution().solve(N, K, GeekNum))
        
    
# } Driver Code Ends