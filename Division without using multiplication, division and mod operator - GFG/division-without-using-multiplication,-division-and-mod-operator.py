#User function Template for python3

class Solution:
    def divide(self, a, b):
        if (a < 0) ^ (b < 0):
            sign = -1
        else:
            sign = 1
     
        a = abs(a)
        b = abs(b)
        
        quotient = 0
        temp = 0

        for i in range(31, -1, -1):
            if (temp + (b << i) <= a):
                temp += b << i
                quotient |= 1 << i

        if sign == -1:
          quotient = -quotient
        
        return quotient


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        inp = list(map(int,input().split())) 
        
        a=inp[0]
        b=inp[1]
        
        ob=Solution()
        
        print(ob.divide(a,b))
        
# } Driver Code Ends