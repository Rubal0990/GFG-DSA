#User function Template for python3
from collections import defaultdict, Counter

class Solution:
    def findSubString(self, str):
        n = len(Counter(str))
        d = defaultdict(int)
        left = 0
        ans = float('inf')
        
        for i, e in enumerate(str):
            d[e] += 1
            while len(d) == n:
                ans = min(ans, i - left + 1)
                left_most = str[left]
                left += 1
                d[left_most] -= 1
                if d[left_most] == 0:
                    del d[left_most]
        
        return ans
    
    
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
    	str = input()
    	ob=Solution()
    	print(ob.findSubString(str))
    	
    	T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends