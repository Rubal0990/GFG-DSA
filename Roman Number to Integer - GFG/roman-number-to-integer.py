#User function Template for python3

class Solution:
    def romanToDecimal(self, S): 
        h_map = {
            "I": 1, "V": 5, 
            "X": 10, "L": 50,
            "C": 100, "D": 500,
            "M": 1000
        }
        
        sum1 = h_map[S[-1]]
        
        for i in range(len(S)-2, -1, -1):
            if h_map[S[i]] >= h_map[S[i+1]]:
                sum1 += h_map[S[i]]
            else:
                sum1 -= h_map[S[i]]
        
        return sum1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        ob = Solution()
        S = input()
        print(ob.romanToDecimal(S))
# } Driver Code Ends