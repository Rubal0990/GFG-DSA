#User function Template for python3

def LargButMinFreq(arr, n):
    s = {}
    for i in range(n):
        s[arr[i]] = 1 + s.get(arr[i], 0)
    
    m = 0
    mi = float("inf")
    for x in s:
        if s[x] <= mi:
            mi = s[x]
    
    for x in s:
        if s[x] == mi and x > m:
            m = x
    
    return m


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
#Iterating over test cases
for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(LargButMinFreq(arr, n))
# } Driver Code Ends