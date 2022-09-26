#User function Template for python3

class Solution:
    def countBitsFlip(self, a, b):
        xor = a ^ b
        count = 0
        
        while xor != 0:
            if xor&1 == 1:
                count += 1
            xor >>= 1
        
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math



def main():
    
    T=int(input())
    
    while(T>0):
        
        
        ab=[int(x) for x in input().strip().split()]
        a=ab[0]
        b=ab[1]
        ob=Solution()
        print(ob.countBitsFlip(a,b))
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends