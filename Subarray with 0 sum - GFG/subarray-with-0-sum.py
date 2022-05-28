#User function Template for python3

class Solution:
    def subArrayExists(self, arr, n):
        if 0 in arr:
            return True
           
        dt = {}
        tsum = 0
       
        for x in arr:
            tsum += x
            if tsum == 0 or tsum in dt:
                return True
            
            dt[tsum] = dt.get(tsum, 0) + 1
           
        return False

#{ 
#  Driver Code Starts
#Initial Template for Python 3



def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        if(Solution().subArrayExists(arr,n)):
            print("Yes")
        else:
            print("No")
        
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends