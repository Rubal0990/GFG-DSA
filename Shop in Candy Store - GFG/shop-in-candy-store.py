#User function Template for python3

class Solution:
    def candyStore(self, candies, N, K):
        
        def cost(arr):
            i, j, ret = 0, N, 0
            
            while i < j:
                ret += arr[i]
                j -= K
                i += 1
            
            return ret

        return cost(sorted(candies)), cost(sorted(candies, reverse=True))

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):

        N,K = [int(x) for x in input().split()]
        candies = [int(x) for x in input().split()]

        solObj = Solution()

        print(*solObj.candyStore(candies,N,K))
# } Driver Code Ends