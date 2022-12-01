#User function Template for python3
class Solution:
    def rearrange(self, arr, n): 
        a = sorted(arr)
        i = 0
        j = n - 1
        
        for x in range(0, n, 2):
            arr[x] = a[j]
            if x + 1 <= n - 1:
                arr[x+1] = a[i]
                j -= 1
                i += 1
        
        return arr

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math




def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            ob.rearrange(arr,n)
            
            for i in arr:
                print(i,end=" ")
            
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
