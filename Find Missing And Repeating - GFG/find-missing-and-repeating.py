#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        arr.sort()
        repeat = 0
        
        for i in range(n-1):
            if arr[i] == arr[i+1]:
                repeat = arr[i]
                
        arr2 = set([i for i in range(1, n+1)])
        arr = set(arr)
        missing = arr2.difference(arr)
        miss = 0
        
        for i in missing:
            miss = i
        
        return repeat, miss

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends