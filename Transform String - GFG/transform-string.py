#Back-end complete function Template for Python 3

class Solution:
    def transform(self, A, B): 
        if A == B:
            return 0
            
        listA = list(A)
        listB = list(B)
        lenA = len(listA)
        lenB = len(listB)
        count1 = 0
        count2 = 0
        newDict2 = {}
        newDict1 = {}
        temp1 = temp2 = lenA-1
        count = 0
        
        if lenA != lenB:
            return -1
            
        while temp1 >= 0:
            if listA[temp1] == listB[temp2]:
                temp2 -= 1
            else:
                if listA[temp1] in newDict1:
                    newDict1[listA[temp1]] += 1
                else:
                    newDict1[listA[temp1]] = 1
                count += 1
            temp1 -= 1
            
        for i in range(count):
            if listB[i] in newDict2:
                newDict2[listB[i]] += 1
            else:
                newDict2[listB[i]] = 1
                
        try:
            for i in newDict1:
                if (i in newDict2) and (newDict1[i] == newDict2[i]):
                    continue
                else:
                    return -1
        except:
            return -1
            
        return count

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        line = input().strip().split()
        A = line[0]
        B = line[1]
        ob = Solution()
        print(ob.transform(A,B))
# } Driver Code Ends