#User function Template for python3

class Solution:
    def leastWeightCapacity(self, arr, N, D):
        def helper(capacity):
            prev = 0
            ans = 0
            for num in arr:
                prev += num
                if prev > capacity:
                    ans += 1
                    prev = num
                    
            return ans + 1 if prev > 0 else ans
            
        start = max(arr) - 1
        end = sum(arr)
        
        while end - start > 1:
            m = (end + start) //2
            if helper(m) <= D:
                end = m
            else:
                start = m
                
                
        return end

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        D=int(input())
        
        ob = Solution()
        print(ob.leastWeightCapacity(arr,N,D))
# } Driver Code Ends