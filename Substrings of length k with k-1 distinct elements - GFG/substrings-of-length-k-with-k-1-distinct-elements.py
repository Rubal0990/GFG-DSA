#User function Template for python3
from collections import defaultdict

class Solution:
    def countOfSubstrings(self, S, K):
        hashmap = defaultdict(int)
        res = 0
        for c in range(K):
            hashmap[S[c]] += 1
        
        for i in range(K, len(S)):
            if len(hashmap) == K-1:
                res += 1
            
            hashmap[S[i-K]] -= 1
            if hashmap[S[i-K]] == 0:
                del(hashmap[S[i-K]])
            
            hashmap[S[i]] += 1
        
        if len(hashmap) == K-1:
                res += 1
        
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S=input()
        K=int(input())
        
        ob = Solution()
        print(ob.countOfSubstrings(S,K))
# } Driver Code Ends
