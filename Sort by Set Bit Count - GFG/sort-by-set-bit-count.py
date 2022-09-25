#User function Template for python3

class Solution:
    def sortBySetBitCount(self, arr, n):
        dic = {}
        for i in range(n):
            num = bin(arr[i]).count('1')
            dic[i] = num
        
        dic = sorted(dic.items(), key=lambda item:item[1], reverse=True)
        li = []
        for i in dic:
            li.append(arr[i[0]])
        
        arr[::] = li[::]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.sortBySetBitCount(arr, n)
        print(*arr)

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends
