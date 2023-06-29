#User function Template for python3

class Solution:
    def maxSubArraySum(self, arr, N):
        sumc = 0
        ans = arr[0]
        
        for i in range(0, N):
            sumc += arr[i]
            ans = max(ans, sumc)
            if sumc < 0:
                sumc = 0
                
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends