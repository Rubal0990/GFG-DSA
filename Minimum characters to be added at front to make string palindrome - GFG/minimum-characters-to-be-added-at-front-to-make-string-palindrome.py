class Solution:
    def minChar(self, str):
        n = len(s)
        r = s[::-1]
        lps = [0] * (n+1)
        i, length = 0, 0
        
        while i < n:
            if r[i] == s[length]:
                length += 1
                lps[i+1] = length
                i += 1
            
            else:
                if length == 0:
                    lps[i+1] = 0
                    i += 1
                else:
                    length = lps[length-1]
        
        return n-lps[-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        s=input()
        obj=Solution()
        ans=obj.minChar(s)
        print(ans)
# } Driver Code Ends
