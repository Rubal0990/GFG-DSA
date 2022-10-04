#User function Template for python3

class Solution:
    def check(self, st, M, a, b):
        if M[a][b] == 1:
            st.append(b)
        elif M[b][a] == 1:
            st.append(a)
    
    def celebrity(self, M, n):
        st = []
        
        for i in range(n):
            st.append(i)
        
        while len(st) != 1:
            a = st[-1]
            st.pop()
            b = st[-1]
            st.pop()
            self.check(st, M, a, b)
        
        for i in range(n):
            cel = st[-1]
            if M[cel][i] != 0 and i != cel:
                return -1
        
        for j in range(n):
            cel = st[-1]
            if M[j][cel] != 1 and cel != j:
                return -1
        
        return st[-1]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        k = 0
        m = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(a[k])
                k+=1
            m.append(row)
        ob = Solution()
        print(ob.celebrity(m,n))
# } Driver Code Ends