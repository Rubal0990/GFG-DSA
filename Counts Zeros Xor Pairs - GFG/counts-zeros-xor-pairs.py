#User function Template for python3
from collections import Counter

def calculate (arr, n) : 
    z = Counter(arr)
    ans = 0
    
    for i in arr:
        if z[i]>1:
            ans += z[i] - 1
            z[i] -= 1
            
    return ans



#{ 
#  Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    res = calculate(arr, n)
    print(res)


# } Driver Code Ends