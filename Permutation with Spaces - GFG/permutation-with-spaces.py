#User function Template for python3

class Solution:
    def permutation (self, S):
        n = len(S)
        ans = []
        
        def helper(ind, out):
            if ind == n:
                ans.append(out)
                return
            
            inp = " " + S[ind]
            inp1 = S[ind]
            helper(ind+1, out+inp)
            helper(ind+1, out+inp1)
        helper(1, S[0])
        
        return ans



#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        S = input()
        ans = ob.permutation(S);
        write = "";
        for i in ans:
            write += "(" + i + ")"
        print(write)


# } Driver Code Ends