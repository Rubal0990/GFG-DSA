#User function Template for python3

class Solution:
    def findMaxAverage(self, arr, n, k):
        summ = 0
        left = 0
     
        for i in range(k):
            summ += arr[i]
     
        maxsum = summ
        j = k
     
        while j < n:
            summ = summ + arr[j] - arr[j-k]
            if summ > maxsum :
                maxsum = summ
                left = j - k + 1
            j += 1
     
        return left

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxAverage(arr, n, k)
        for i in range(ans, ans+k):
            print(arr[i], end=" ")
        print()
        tc -= 1
# } Driver Code Ends