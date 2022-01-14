class Solution:
    def findExtra(self,a,b,n):
        for i in range(len(b)):
            if a[i] != b[i]:
                return i
        return n-1

#{ 
#  Driver Code Starts
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        print(Solution().findExtra(a,b,n))
# } Driver Code Ends