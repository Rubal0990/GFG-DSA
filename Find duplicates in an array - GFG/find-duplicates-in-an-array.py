class Solution:
    def duplicates(self, arr, n): 
    	res = {}
        lst = []
        
        for i in arr:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1
                
                
        for key, value in res.items():
            if value > 1:
                lst.append(key)
                
        if len(lst) == 0:
            return [-1]
        else:
            lst.sort()  
            return lst
    	    

#{ 
#  Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends