#User function Template for python3

class Solution:
    def solve(self, n, k, stalls):
        stalls.sort()
        lo = float('inf')
        for i in range(1, len(stalls)):
            lo = min(lo, stalls[i] - stalls[i-1])
        
        hi = stalls[-1] - stalls[0] + 1

        def ok(d, k):
            p = float('-inf')
            for stall in stalls:
                if stall-p >= d:
                    k -= 1
                    p = stall
            
            return k <= 0
        
        while lo < hi:
            mi = lo + (hi - lo) // 2
            if ok(mi, k):
                lo = mi + 1
            else:
                hi = mi
        
        return lo-1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = list(map(int, input().split()))
        stalls = list(map(int, input().split()))
        ob = Solution()
        res = ob.solve(n, k, stalls)
        print(res)

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends