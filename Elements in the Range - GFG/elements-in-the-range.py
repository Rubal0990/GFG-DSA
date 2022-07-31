class Solution:
    def check_elements(self, arr, n, A, B):
        mask, cnt = 0, 0
        
        for e in arr:
            if B >= e >= A and (1<<e) & mask == 0:
                mask |= 1<<e 
                cnt += 1
        
        return cnt == B-A+1


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        l = list(map(int, input().split()))
        n=l[0]
        k=l[1]
        y=l[2]
        a = list(map(int,input().split()))
        ob = Solution()
        ans=ob.check_elements(a,n,k,y)
        if(ans):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends