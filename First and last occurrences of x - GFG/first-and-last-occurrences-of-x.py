#User function Template for python3


def find(arr, n, x):
    ans = []
    
    for i in range(n):
        if arr[i] == x:
            ans.append(i)
    
    if len(ans) == 0:
        return -1, -1
    else:
        return ans[0], ans[-1]



#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ans=find(arr,n,x)
    print(*ans)
# } Driver Code Ends