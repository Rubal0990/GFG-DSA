#User function Template for python3

class Solution:
    def power(self, N, R):
        ans = 1
        mod = 1000000007
        
        while R > 0:
            if R % 2 == 1:
                ans = (ans * N) % mod 
            
            N = (N * N) % mod
            R //= 2 
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        N=input()
        R=N[::-1]
        
        ob=Solution();
        ans=ob.power(int(N),int(R))
        print(ans)
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends