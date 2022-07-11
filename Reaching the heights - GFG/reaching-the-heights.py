#User function Template for python3

def reaching_height (n, arr) : 
    res = []
    arr.sort()
    l, r = 0, n - 1
    
    while l < r:
        res.append(arr[r])
        res.append(arr[l])
        l += 1
        r -= 1
    
    if n % 2:
        res.append(arr[l])
    
    if n >= 2:
        if res[0] <= res[1]:
            return [-1]
    
    return res
    


#{ 
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ans = reaching_height(n, arr)
    if(len(ans) == 1 and ans[0] == -1):
        print("Not Possible")
    else:
        print(*ans)
# } Driver Code Ends