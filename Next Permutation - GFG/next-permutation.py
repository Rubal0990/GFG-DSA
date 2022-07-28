#User function Template for python3

class Solution:
    def swap(self, arr, ind1, ind2):
        arr[ind1], arr[ind2] = arr[ind2], arr[ind1]
        
    def reverse(self, arr, beg, end):
        while beg < end:
            self.swap(arr, beg, end)
            beg += 1
            end -= 1
    
    def nextPermutation(self, N, arr):
        if N == 1:
            return arr
        
        if N == 2:
            return self.swap(arr, 0, 1)
            
        dec = N - 2
        while dec>=0 and arr[dec]>=arr[dec+1]:
            dec -= 1
        
        self.reverse(arr, dec+1, N-1)
        if dec == -1:
            return arr
        
        next_num = dec + 1
        while next_num<N and arr[next_num]<=arr[dec]:
            next_num += 1
        
        self.swap(arr, next_num, dec)
        return arr

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        ans = ob.nextPermutation(N, arr)
        for i in range(N):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends
