#User function Template for python3


class Solution:
    def carpetBox(self, A, B, C, D):
        
        def helper(a, b):
            res = 0
            
            while a > b:
                a //= 2
                res += 1
            
            return res
        
        return min(helper(A, C) + helper(B, D), helper(A, D) + helper(B, C))



#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():
        T=int(input())
        while(T>0):
            A,B,C,D = map(int, input().split())
            
            obj = Solution()
            print(obj.carpetBox(A,B,C,D))
            
            T-=1


if __name__ == "__main__":
    main()


# } Driver Code Ends