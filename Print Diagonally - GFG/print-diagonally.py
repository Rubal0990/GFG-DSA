#User function Template for python3

def downwardDigonal(N, A): 
    lst = []
    
    for i in range(N):
        for j in range(i+1):
            lst.append(A[j][i-j])
    
    for i in range(1, N):
        for j in range(N-i):
            lst.append(A[i+j][n-1-j])
    
    return lst
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        matrix =[]
        for i in range(n):
            row = list(map(int, input().strip().split()))
            matrix.append(row)
        ans = downwardDigonal(n,matrix)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends