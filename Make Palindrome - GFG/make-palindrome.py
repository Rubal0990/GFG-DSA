from typing import List


class Solution:
    def makePalindrome(self, n : int, arr : List[str]) -> bool:
        reversedArr = {}
        for i in range(n):
            s = arr[i][::-1]
            a = reversedArr.get(s,0)
            reversedArr[s] = a + 1
        
        for i in range(n):
            if reversedArr.get(arr[i]) is None:
                return False
            else:
                if reversedArr.get(arr[i]) == 1:
                    del reversedArr[arr[i]]
                else:
                    reversedArr[arr[i]] -= 1
        
        return True


#{ 
 # Driver Code Starts
class StringArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=input().strip().split()#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        arr=StringArray().Input(n)
        
        obj = Solution()
        res = obj.makePalindrome(n, arr)
        
        result_val = "YES" if res else "NO"
        print(result_val)

# } Driver Code Ends