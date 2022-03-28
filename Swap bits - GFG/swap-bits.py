#User function Template for python3

class Solution:
    def swapBits(self, X, P1, P2, N):
        for i in range(N):
            # Store the bits to be swapped in two variables.
            temp1 = (X >> P1) & 1
            temp2 = (X >> P2) & 1
            
            # Make both bits 0.
            X = X & (~(1 << P1))
            X = X & (~(1 << P2))
            
            # Insert the bits in the opposite locations.
            X = X | (temp1 << P2)
            X = X | (temp2 << P1)
            
            # Increment p1 and p2.
            P1 += 1
            P2 += 1
        
        return X



#{ 
#  Driver Code Starts

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        obj = Solution()
        X, P1, P2, N = map(int, input().split())
        print(obj.swapBits(X, P1, P2, N))
        

# } Driver Code Ends