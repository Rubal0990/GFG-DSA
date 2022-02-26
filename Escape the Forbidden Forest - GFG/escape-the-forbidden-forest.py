import numpy as np

class Solution:
    def build_bridges(self, str1, str2):
        m = len(str1)
        n = len(str2)
        matrix = np.zeros([m+1, n+1], dtype=int)
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if str1[i-1] == str2[j-1]:
                    matrix[i][j] = matrix[i-1][j-1] + 1
                else:
                    matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
       
        return matrix[m][n]


#{ 
#  Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        obj = Solution()
        str1, str2 = input().split()
        print(obj.build_bridges(str1, str2))

# } Driver Code Ends