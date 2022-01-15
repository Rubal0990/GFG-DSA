#User function Template for python3
class Solution:
    ##Complete this function
    #Function to rearrange  the array elements alternately.
    def rearrange(self,arr, n): 
        temp = n*[None]
        s, l = 0, n-1
        flag = True
    
        for i in range(n):
            if flag is True:
                temp[i] = arr[l]
                l -= 1
            else:
                temp[i] = arr[s]
                s += 1
    
            flag = bool(1-flag)
    
        for i in range(n):
            arr[i] = temp[i]
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