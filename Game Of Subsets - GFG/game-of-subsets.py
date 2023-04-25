from typing import List
from operator import mul
from functools import reduce

class Solution:
    def goodSubsets(self, n : int, arr : List[int]) -> int:
        MOD = 10**9 + 7
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        A = [0] * 31
        for v in arr:
            A[v] += 1
        K1 = pow(2, A[1], MOD)
        
        # process primes
        tmp = K1
        for pv in primes:
            tmp = (tmp * (A[pv]+1)) % MOD
        ans = (tmp - K1) % MOD
        
        # process valid composites numbers
        def exc(*ex):
            return [v for v in primes if v not in ex and A[v] > 0]
        
        mp = { 
            (6,): exc(2, 3),
            (10,): exc(2, 5),
            (14,): exc(2, 7), 
            (15,): exc(3, 5), 
            (15,14): exc(2, 3, 5, 7),
            (21,): exc(3, 7), 
            (21,10): exc(2, 3, 5, 7),
            (22,): exc(2, 11), 
            (22,15): exc(2, 3, 5, 11), 
            (22,21): exc(2, 3, 7, 11),
            (26,): exc(2, 13), 
            (26,15): exc(2, 3, 5, 13), 
            (26,21): exc(2, 3, 7, 13), 
            (30,): exc(2, 3, 5)
        }
        
        for cvs, targets in mp.items():
            prod_comp = reduce(mul, (A[v] for v in cvs))
            if prod_comp == 0:
                continue
            
            MUL = (K1 * prod_comp) % MOD
            su = 0
            
            for mask in range(2**len(targets)):
                tmp, i = 1, 0
                while mask:
                    if mask & 1:
                        tmp = (tmp * A[targets[i]]) % MOD
                    
                    i += 1
                    mask >>= 1
                
                su = (su + tmp) % MOD
            
            ans = (ans + MUL * su) % MOD
        
        return ans


#{ 
 # Driver Code Starts
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
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.goodSubsets(n, arr)
        
        print(res)
        

# } Driver Code Ends