#User function Template for python3

class Solution:
    def findAndReplace(self, S, Q, index, sources, targets):
        ret = []
        i, n = 0, len(S)
        
        while i < n:
            if index and index[0] == i:
                if S[i:].startswith(sources[0]):
                    i += len(sources[0])
                    ret.append(targets[0])
                else:
                    ret.append(S[i])
                    i += 1
                    
                index = index[1:]
                sources = sources[1:]
                targets = targets[1:]
            else:
                ret.append(S[i])
                i += 1
        
        ans = ""
        for i in ret:
            ans += str(i)
            
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S=input()
        Q=int(input())
        index=list(map(int,input().split()))
        sources=list(map(str,input().split()))
        targets=list(map(str,input().split()))
        
        ob = Solution()
        print(ob.findAndReplace(S,Q,index,sources,targets))
# } Driver Code Ends