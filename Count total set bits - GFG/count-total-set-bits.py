#User function Template for python3

class Solution:
    def countSetBits(self, n):
        n += 1
        powerOf2 = 2
        cnt = n // 2
        
        while powerOf2 <= n:
            totalPairs = n // powerOf2
            cnt += (totalPairs // 2) * powerOf2;
            
            if totalPairs & 1:
                cnt += (n % powerOf2)
            else:
                cnt += 0
            
            powerOf2 <<= 1
    
        return cnt


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        ob=Solution()
        print(ob.countSetBits(int(input())))
# } Driver Code Ends