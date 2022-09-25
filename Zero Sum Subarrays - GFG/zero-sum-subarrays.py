#User function Template for python3

class Solution:
    def findSubArrays(self, arr, n):
        count = 0
        dict1 = {0:1}
        total = 0
        
        for i in range(n):
            total += arr[i]
            
            if total in dict1.keys():
                dict1[total] += 1
                count += dict1[total] - 1
            else:
                dict1[total] = 1
        
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
        
if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        A = [int(x) for x in input().strip().split(' ')]
        ob = Solution()
        print(ob.findSubArrays(A,N))
        
                
                
# } Driver Code Ends