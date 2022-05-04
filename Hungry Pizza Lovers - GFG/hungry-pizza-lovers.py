#User function Template for python3

class Solution:
    def permute(self, arr, n):
        ans = []
        
        for i in range(n):
            su = sum(arr[i])
            ans.append([su, i])
        
        ans.sort()
        rans = []
        
        for i in range(n):
            catch = ans[i][1]
            rans.append(catch + 1)
        
        return rans


#{ 
#  Driver Code Starts
#Initial Template for Python 3

    
for _ in range(0,int(input())):
    n = int(input())
    arr = []
    for _ in range(0, n):
        ll = list(map(int, input().strip().split()))
        arr.append(ll)
    obj=Solution()
    ans = obj.permute(arr, n)
    for i in ans:
        print(i)
    



# } Driver Code Ends