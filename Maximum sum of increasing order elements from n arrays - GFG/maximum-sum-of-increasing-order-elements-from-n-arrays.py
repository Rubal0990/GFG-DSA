#User function Template for python3

def maximumSum (n, m, arr) : 
    a = []
    temp = max(arr[n-1])
    sum1 = temp
    
    for i in range(n-1,0,-1):
        for item in arr[i-1]:
            if item < temp:
                a.append(item)
                
        if(len(a)==0):
            return 0
            
        temp = max(a)
        sum1 += temp
        a = []
        
    return sum1


#{ 
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n, m = map(int , input().split())
    arr = []
    for i in range(0, n):
        ll = list(map(int, input().strip().split()))
        arr.append(ll)
    ans = maximumSum(n, m, arr)
    print(ans)




# } Driver Code Ends
