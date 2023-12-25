#User function Template for python3

class Solution:
    def search(self, arr, N, X):
        
        for i, num in enumerate(arr):
            if num == X:
                return i
        
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math



    
def main():
        T=int(input())
        while(T>0):
            
            N=int(input())
            
            A=[int(x) for x in input().strip().split()]
            
            x=int(input())
            ob=Solution()
            print(ob.search(A,N,x))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends