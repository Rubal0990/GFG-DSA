#User function Template for python3

class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        count = 0
        i = 0
        j = 0
        prod = 1
        
        while j < len(a):
            prod *= a[j]
            
            while i <= j and prod >= k:
                prod /= a[i]
                i += 1
            
            count += j - i + 1
            j += 1
        
        return count


#{ 
 # Driver Code Starts

#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]
        
        print(Solution().countSubArrayProductLessThanK(arr, n, k))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends