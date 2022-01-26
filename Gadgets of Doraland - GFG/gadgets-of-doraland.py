#User function Template for python3
from collections import Counter

class Solution:
    def TopK(self, array, k):
        counter = Counter(array)
        counter = sorted(counter.items(), reverse=True, key=lambda x : x[1])
        i = 1
        # print(counter)
        while i < len(counter) :
            start = i-1
            while i< len(counter) and counter[i][1] == counter[i-1][1]:
                i+=1
            end = i
            counter[start:end] = sorted(counter[start:end], reverse=True)
            i+=1
            
        # print(counter)    
        res= []
        for i in range(k):
            res.append(counter[i][0])
        return res


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        array = [int(x) for x in input().strip().split()]
        k = int(input())
        obj = Solution()
        res = obj.TopK(array, k)
        for each in res:
            print(each, end=' ')
        print()

# } Driver Code Ends