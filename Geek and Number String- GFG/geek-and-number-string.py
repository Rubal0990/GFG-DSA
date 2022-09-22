#User function Template for python3

class Solution:
    def checker(self, a, b):
        if (a==1 and b==2) or (a==2 and b==1):
            return True
        elif (a==3 and b==4) or (a==4 and b==3):
            return True
        elif (a==5 and b==6) or (a==6 and b==5):
            return True
        elif (a==7 and b==8) or (a==8 and b==7):
            return True
        elif (a==0 and b==9) or (a==9 and b==0):
            return True
        
        return False
   
    def minLength(self, s, n): 
        stack = []
        
        for i in range(len(s)):
            x = int(s[i]) - 0
            
            if stack == []:
                stack.append(x)
            elif stack != [] and self.checker(stack[-1], x):
                stack.pop()
            elif stack != [] and not self.checker(stack[-1], x):
                stack.append(x)
        
        return len(stack)
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        ob = Solution()
        print(ob.minLength(s,n))
# } Driver Code Ends