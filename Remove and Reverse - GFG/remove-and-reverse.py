#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
from collections import Counter

class Solution:
    def removeReverse(self, S): 
        C, N = Counter(S), len(S)
        res = [[], []]
        pos, off, dir = [0, N-1], (1, -1), 0
        
        while pos[0] < pos[1]:
            ch = S[ pos[dir] ]
            pos[dir] += off[dir]
            
            if C[ch] > 1:
                C[ch] -= 1
                dir = 1 - dir
            else:
                res[dir].append(ch)
        
        res[1-dir].append(S[pos[1-dir]])
        res[1-dir].reverse()
        ans = (res[0] + res[1]) if dir == 0 else (res[1] + res[0])
        return ''.join(ans)
    

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        ans = ob.removeReverse(S)
        print(ans)


# } Driver Code Ends