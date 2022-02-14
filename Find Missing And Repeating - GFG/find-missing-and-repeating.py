#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        arr.sort()
        ans = []
        s = 0
        
        for i in arr:
            s += i
        
        su = (n * (n + 1)) // 2
        
        for i in range(n-1):
            if arr[i] == arr[i+1]:
                hold = arr[i]
                break
        
        bach = su - s
        p = hold + bach
        
        ans.append(hold)
        ans.append(p)
        
        return(ans)

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