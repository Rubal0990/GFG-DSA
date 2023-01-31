#User function Template for python3

class Solution:
    def minRepeats(self, a, b):
        temp = a
        ctr = 0
        ans = False
        
        if a == b:
            return 1
        
        for i in range(len(b) // len(a) + 2):
            if b in temp:
                ans = True
                break
            
            temp += a
            ctr += 1
        
        if ctr != 0 and ans == True:
            return ctr + 1
        else:
            return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A=input()
        B=input()
        
        ob = Solution()
        print(ob.minRepeats(A,B))
# } Driver Code Ends