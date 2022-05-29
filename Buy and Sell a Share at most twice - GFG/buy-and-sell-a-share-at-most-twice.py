
from typing import List


class Solution:
    def maxProfit(self, n : int, price : List[int]) -> int:
        profit = [0] * n
        
        max_profit = price[n-1]
        min_profit = price[0]
        
        for i in range(n-2, 0, -1):
            if price[i] > max_profit:
                max_profit = price[i]
            
            profit[i] = max(profit[i+1], max_profit - price[i])
        
        for i in range(1, n):
            if price[i] < min_profit:
                min_profit = price[i]
            
            profit[i] = max(profit[i-1], profit[i] + (price[i] - min_profit))
            
        
        result = profit[n-1]
        return result


#{ 
#  Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        price=IntArray().Input(n)
        
        obj = Solution()
        res = obj.maxProfit(n, price)
        
        print(res)
        

# } Driver Code Ends