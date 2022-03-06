#User function Template for python3

class Solution:
    def computeBeforeMatrix(self, N, M, after):
        for i in range(N-1,-1,-1):
            for  j in range(M-1,-1,-1):
               
                if(i):
                    after[i][j]-=after[i-1][j]
                if(j):
                    after[i][j]-=after[i][j-1]
               
                if(i and j):
                    after[i][j]+=after[i-1][j-1]
           
        return after


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N, M =[int(i) for i in input().split()]
        after= []
        for j in range (N):
            after.append([int(i) for i in input().split()])
        ob = Solution()
        before=ob.computeBeforeMatrix(N,M,after)
        for i in range(len(before)): 
            for j in range(len(before[i])):
                print(before[i][j],end=' ')
            print()
        
        
        T -= 1
# } Driver Code Ends