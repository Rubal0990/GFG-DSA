#User function Template for python3

class Solution:
    def ExcelColumn(self, N):
        if N == 1: 
            return "A"
        
        res = ""
        N -= 1
        rem = 0
        
        while N >= 0:
            rem = N % 26
            res = chr(65 + int(rem)) + res
            N /= 26
            N -= 1
        
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        ob=Solution()
        print(ob.ExcelColumn(n))

# } Driver Code Ends
