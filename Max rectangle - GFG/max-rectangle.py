#User function Template for python3
from collections import deque

class Solution:
    def maxHist(self, row):
        result = []
        top_val = 0
        max_area = 0
        area = 0
        i = 0
        
        while i < len(row):
            if (len(result) == 0) or (row[result[-1]] <= row[i]):
                result.append(i)
                i += 1
            else:
                top_val = row[result.pop()]
                area = top_val * i
                if (len(result)):
                    area = top_val * (i - result[-1] - 1)
                    
                max_area = max(area, max_area)
 
        while (len(result)):
            top_val = row[result.pop()]
            area = top_val * i
            if (len(result)):
                area = top_val * (i - result[-1] - 1)
 
            max_area = max(area, max_area)
 
        return max_area
       
        
    def maxArea(self, A, n, m):
        result = self.maxHist(A[0])
        for i in range(1, len(A)):
 
            for j in range(len(A[i])):
                if (A[i][j]):
                    A[i][j] += A[i - 1][j]
 
            result = max(result, self.maxHist(A[i]))
 
        return result
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3



# Driver Code 
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        R,C = map(int, input().strip().split())
        A = []
        for i in range(R):
            line = [int(x) for x in input().strip().split()]
            A.append(line)
        print(Solution().maxArea(A, R, C)) 
	
# This code is contributed 
# by SHUBHAMSINGH10 

# } Driver Code Ends