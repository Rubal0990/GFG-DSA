#User function Template for python3

# arr[] : int input array of integers
# k : the quadruple sum required
class Solution:
    def fourSum(self, arr, k):
        result = []
        arr.sort()
       
        for i in range(len(arr)-3):
            if i > 0 and arr[i] == arr[i-1]:
                continue
               
            for j in range(i+1, len(arr)-2):
                if j > i+1 and arr[j] == arr[j-1]:
                    continue
                
                sum = k-arr[i]-arr[j]
                l = j+1
                r = len(arr)-1
                while l < r:
                    if arr[l]+arr[r] == sum:
                        result.append([arr[i], arr[j], arr[l], arr[r]])
                        while l < r and arr[l] == arr[l+1]:
                            l += 1
                        
                        while l < r and arr[r] == arr[r-1]:
                            r -= 1
                        
                        l += 1
                        r -= 1
                    
                    elif arr[l]+arr[r] < sum:
                        l += 1
                    
                    else:
                        r -= 1
        
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3


#Main
if __name__=='__main__':
    t = int(input())
    while t:
        t-=1
        n, k=map(int,input().split())
        # print(n, k)
        a=list(map(int,input().strip().split()))[:n]
        # print(a)
        ob=Solution()
        ans=ob.fourSum(a, k)
        # print(ans)
        for v in ans:
            for u in v:
                print(u, end=" ")
            print("$", end="")
        if(len(ans)==0):
            print(-1, end="")
        print()
        
        

# } Driver Code Ends