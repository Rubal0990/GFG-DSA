#User function Template for python3

def max_sum(a,n):
    curmax = 0
    arrsum = 0
    
    for i in range(n) :
        curmax += i*a[i]
        arrsum += a[i]
    maxvalue = curmax
    
    for j in range(n-1) :
        curmax -= (arrsum - (n*arr[j]))
        if curmax > maxvalue :
            maxvalue = curmax
            
    return maxvalue

#{ 
#  Driver Code Starts
#Initial Template for Python 3


    
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(max_sum(arr,n))
# } Driver Code Ends
