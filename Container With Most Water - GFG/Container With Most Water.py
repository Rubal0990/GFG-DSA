#User function Template for python3

def maxArea(A, le):
    maxArea, f, e = 0, 0, le-1 
    
    while f < e:
        ar = min(A[f], A[e]) * (e - f)
        maxArea = max(ar, maxArea)
        
        if A[f] < A[e]:
            f += 1
        else: 
            e -= 1
    
    return maxArea


#{ 
 # Driver Code Starts
#Initial Template for Python 3



for _ in range(0,int(input())):
    
    n = int(input())
    l = list(map(int,input().split()))
    
    print(maxArea(l,n))
    
    
# } Driver Code Ends