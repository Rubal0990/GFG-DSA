#User function Template for python3

class Solution:
    def checkCompressed(self, S, T):
        i, j, N, M = 0, 0, len(S), len(T)
        while i < N and j < M:
            if not T[j].isdigit():
                if T[j] != S[i]: 
                    return 0
                
                i, j = i + 1, j + 1
            
            else:
                k = j + 1
                while k < M and T[k].isdigit(): 
                    k += 1
                
                i += int(T[j:k])
                j = k
        
        return 1 if i==N and j==M else 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S = input()
        T = input()
        
        ob = Solution()
        print(ob.checkCompressed(S,T))
# } Driver Code Ends