#User function Template for python3

class Solution:
    def BalancedString(self, N):
        chars = 'abcdefghijklmnopqrstuvwxyz'
        is_even = 1 if sum(int(c) for c in str(N)) % 2 == 0 else -1
 
        res = chars*(N//26)
        N %= 26
        if N%2 == 0:
            res += chars[:N//2] + chars[::-1][:N//2][::-1]
        else:
           res += chars[:(N+is_even)//2] + chars[::-1][:(N-is_even)//2][::-1]
           
        return res
    
    
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        
        ob=Solution()
        print(ob.BalancedString(N))
# } Driver Code Ends