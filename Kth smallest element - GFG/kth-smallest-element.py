#User function Template for python3

class Solution:
    def kthSmallest(self,arr, l, r, k):
        if k < 1 or k > len(arr):
            return None
        
        return self.quick_select(arr, 0, len(arr) - 1, k - 1)
    
    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    def quick_select(self, arr, low, high, k):
        if low == high:
            return arr[low]
        
        pivot_index = self.partition(arr, low, high)
        
        if k == pivot_index:
            return arr[k]
        elif k < pivot_index:
            return self.quick_select(arr, low, pivot_index - 1, k)
        else:
            return self.quick_select(arr, pivot_index + 1, high, k)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    import random 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        k=int(input())
        ob=Solution()
        print(ob.kthSmallest(arr, 0, n-1, k))
        
# } Driver Code Ends