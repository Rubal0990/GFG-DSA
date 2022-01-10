#User function Template for python3

class Solution:  
    
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        if n == 0:
            return 0
        if n == 1:
            return a[0]
        if n == 2:
            return max(a[0], a[1])
            
        sum_of_loot = n * [0]
        sum_of_loot[0] = a[0]
        sum_of_loot[1] = max(a[0], a[1])
        for i in range(2, n):
            sum_of_loot[i] = max(a[i] + sum_of_loot[i-2], sum_of_loot[i-1])
        
        return sum_of_loot[n-1]
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.FindMaxSum(a,n))
# } Driver Code Ends