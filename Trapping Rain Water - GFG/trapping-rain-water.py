
class Solution:
    def trappingWater(self, arr,n):
        l = 0
        r = n - 1
        ans = 0
        l_max = 0
        r_max = 0
        
        while l < r:
            if arr[l] < arr[r]:
                if arr[l] >= l_max: 
                    l_max = arr[l]
                else:
                    ans += l_max - arr[l]
                l += 1
            else:
                if arr[r] >= r_max: 
                    r_max = arr[r]
                else:
                    ans += r_max - arr[r]
                r -= 1

        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends