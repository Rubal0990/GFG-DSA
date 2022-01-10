#User function Template for python3

class Solution:
    def first_zero(self ,arr, high , low):
        while(high>=low):
            mid = (high+low)//2
            
            if (mid==0 or arr[mid-1]==1) and arr[mid] == 0:
                return mid
            elif arr[mid] == 1:
                low = mid+1
            else:
                high = mid-1
                
        return -1
            
        
    def countZeroes(self,arr,n):
        index_z = self.first_zero(arr,n-1,0)
        
        if index_z == -1:
            return 0
            
        return(n - index_z)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countZeroes(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends