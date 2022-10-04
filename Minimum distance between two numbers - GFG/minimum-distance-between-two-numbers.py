class Solution:
    def minDist(self, arr, n, x, y):
        if x not in arr or y not in arr:
            return -1
        
        md = 99999
        px = arr.index(x)
        py = arr.index(y)
        md = abs(py-px)
        
        for i in range(min(px, py)+1, n):
            if x == arr[i]:
                px = i
            elif y == arr[i]:
                py = i
            
            md = min(abs(py-px), md)
        
        return md
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        x,y = list(map(int, input().strip().split()))
        print(Solution().minDist(arr, n, x, y))



# } Driver Code Ends