#User function Template for python3

class Solution:
    def endPoints(self, matrix, R, C):
        d, x, y = 1, 0, 0
        if matrix[x][y]: 
            matrix[x][y], d = 0, (d+1) % 4

        while True:
            pos = [x, y]
            
            if d == 0: 
                x -= 1
            
            elif d == 1: 
                y += 1
            
            elif d == 2: 
                x += 1
            
            elif d == 3: 
                y -= 1
            
            if x < 0 or x >= R or y < 0 or y >= C:
                return pos
            
            if matrix[x][y]: 
                matrix[x][y], d = 0, (d+1) % 4



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        matrix = []
        for i in range(r):
            line = [int(x) for x in input().strip().split()]
            matrix.append(line)
        ob = Solution()
        ans = ob.endPoints(matrix,r,c)
        print('(',ans[0],', ',ans[1],')',sep ='')

# } Driver Code Ends