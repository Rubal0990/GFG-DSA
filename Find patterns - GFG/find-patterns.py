#User function Template for python3
class Solution:
    def numberOfSubsequences (self, S, W):
        mp = {}
        N = len(S)
        ans = 0 
        check = len(W)

        for i in range(N):
            k = 0
            
            for j in range(i, N):
                if k == check:
                    break
                
                if S[j] == W[k]:
                    if j in mp:
                        continue
                    
                    else:
                        mp[j] = 1 
                        k += 1
            
            if k == check:
                ans += 1
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())
        W=str(input())

        ob = Solution()
        print(ob.numberOfSubsequences(S,W))

# } Driver Code Ends