#User function Template for python3
from collections import Counter
import numpy as np

class Solution:
    def minValue(self, s, k):
        dict1 = Counter(s)

        for i in range(k):
            max_key = max(dict1, key=dict1.get)
            dict1[max_key] -= 1

        arr = np.array(list(dict1.values()))
        
        return np.sum(arr**2)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        k = int(input())
        
        ob = Solution()
        print(ob.minValue(s, k))
# } Driver Code Ends