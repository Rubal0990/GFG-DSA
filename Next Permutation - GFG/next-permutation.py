#User function Template for python3

class Solution:
    def nextPermutation(self, N, arr):
        mn=float("inf")
        for i in range (-2,-N-1,-1):
            if i== -N and arr[0]>arr[1]:
                arr.sort()
                break
            if arr[i]<arr[i+1]:
                k=arr[i+1:]
                for j in k:
                    if j>arr[i]:
                        mn=min(mn,j)
                ind=max(idx for idx, val in enumerate(arr) if val == mn)
                t=arr[i]
                arr[i]=arr[ind]
                arr[ind]=t
                k=arr[i+1:]
                k.sort()
                arr[:]=arr[0:i+1] + k
                break
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