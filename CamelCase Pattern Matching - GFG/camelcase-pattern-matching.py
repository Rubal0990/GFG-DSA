#User function Template for python3

class Solution:
    def CamelCase(self,N,Dictionary,Pattern):
        li = []
        
        for i in Dictionary:
            x = ''
            
            for j in i:
                if j.isupper(): 
                    x += j
            
            if Pattern == x[:len(Pattern)]: 
                li.append(i)
        
        return li if len(li) != 0 else [-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        Dictionary=list(map(str,input().split()))
        Pattern=input()
        ob=Solution()
        ans=ob.CamelCase(N,Dictionary,Pattern)
        ans.sort()
        for i in ans:
            print(i,end=" ")
        print()    
# } Driver Code Ends