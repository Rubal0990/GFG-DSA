#User function Template for python3

class Solution:
    def largestNum(self,n,s):
        if n * 9 < s:
            return -1
            
        if s <= 9:
            return str(s) + (n-1) * '0'
        
        nines = s // 9
        rest = s % 9
        
        return nines * '9' + (nines < n) * str(rest) + (n-nines-1) * '0'
    
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,s = map(int,input().strip().split())
        ob = Solution()
        print(ob.largestNum(n,s))
# } Driver Code Ends