#User function Template for python3

class Solution:
    def maxSum (self, w, x, b, n):
        hash_ = {}
        
        for i in range(n):
            hash_[ord(x[i])] = i
        
        max_so_far = 0
        max_ending_here = 0
        start = end = s = 0
        
        if ord(w[0]) in hash_:
            max_so_far = b[hash_[ord(w[0])]]
        else:
            max_so_far = ord(w[0])
        
        for i in range(len(w)):
            c = ord(w[i])
            
            if c in hash_:
                max_ending_here += b[hash_[c]]
            else:
                max_ending_here += c
            
            if max_ending_here > max_so_far:
                max_so_far = max_ending_here
                start = s
                end = i
            
            if max_ending_here < 0:
                max_ending_here = 0
                s = i + 1
        
        ans = ""
        for i in range(start,end+1):
            ans += w[i]
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        w = input()
        n = int(input())
        x = input().split(' ')
        b = input().split(' ')
        for itr in range(n):
            b[itr] = int(b[itr])
       

        ob = Solution()
        print(ob.maxSum(w,x,b,n))
# } Driver Code Ends