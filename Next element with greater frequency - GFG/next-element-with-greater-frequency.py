from collections import Counter

class Solution:
    def print_next_greater_freq(self,arr,n):
        stack = []
        res = []
        d = Counter(arr)
        
        for i in range(len(arr)-1, -1, -1):
            while(stack and d[stack[-1]] <= d[arr[i]]):
                stack.pop()
            if len(stack) == 0:
                res.append(-1)
            if len(stack) > 0:
                res.append(stack[-1])
            stack.append(arr[i])
        
        res[:] = res[::-1]
        return res


#{ 
#  Driver Code Starts
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        obj=Solution()
        ans=obj.print_next_greater_freq(arr,n)
        for i in ans:
            print(i,end=" ")
        print()


# } Driver Code Ends