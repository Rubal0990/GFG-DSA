#User function Template for python3


class Solution:
    def chooseandswap (self, A):
        s = list(set(A))
        s.sort()
       
        for smallestchar in s:
            smallestpos = A.index(smallestchar)
            found = False
            for ch in A:
                if ch > smallestchar:
                    found = True
                    break
            
            if not found:
                continue
            
            biggerpos = A.index(ch)
            if biggerpos < smallestpos:
                A = A.replace(ch, '#')
                A = A.replace(smallestchar, ch)
                A = A.replace('#', smallestchar)
                return A
           
        return A




#{ 
#  Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        A = input()
        ans = ob.chooseandswap(A)
        print(ans)


# } Driver Code Ends