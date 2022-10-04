#User function template for Python

class Solution:
	def reverseInGroups(self, arr, n, k):
        def helper(arr):
            return arr[::-1]
        
        num = N//K + 1
        l = 0
        r = K
        while num > 0:
            num -= 1
            arr[l:r] = helper(arr[l:r])
            l = r
            if num == 1:
                r += N%K    
            else:
                r += K
        
        return arr


#{ 
 # Driver Code Starts
#Initial template for Python

import math
def main():
    T=int(input())
    while(T>0):
        nk=[int(x) for x in input().strip().split()]
        N=nk[0]
        K=nk[1]
        arr=[int(x) for x in input().strip().split()]
        
        ob = Solution()
        ob.reverseInGroups(arr,N,K)
        for i in arr:
            print(i,end=" ")
        print()
        T-=1

if __name__=="__main__":
    main()




# } Driver Code Ends