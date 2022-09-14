#User function Template for python3

class Solution:
    def numberOfSubsequences(ob, N, A):
        r = []
        m=10**9 + 7
        
        for i in A:
            if i == 1:
                r.append(i)
            
            elif i == 2:
                r.append(i)
            
            elif i & (i-1) ==0:
                r.append(i)
            
        return ((2**len(r))-1) % m


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N=int(input())
        A=list(map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.numberOfSubsequences(N,A))
# } Driver Code Ends