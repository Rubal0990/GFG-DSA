class Solution:
    def countTriplets(self, arr, n, sumo):
        arr.sort()
        rem = 0
        count = 0
        
        for i in range(n):
            rem = sumo - arr[i]
            l = i+1
            r = n-1
            
            while r > l:
                if arr[r] + arr[l] < rem:
                    count += r-l
                    l += 1
                else:
                    r -= 1
        
        return count


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        k=l[1]
        a=list(map(int,input().split()))
        ob = Solution()
        ans=ob.countTriplets(a,n,k)
        print(ans)
# } Driver Code Ends