#User function Template for python3

class Solution:
    def endPoints(self, matrix, m, n):
        hmap = {}
        hmap["up"] = "right"
        hmap["right"] = "down"
        hmap["down"] = "left"
        hmap["left"] = "up"
        pos = [0,0]
        d = "right"
        
        while(True):
            if matrix[pos[0]][pos[1]] == 1:
                d = hmap[d]
                
            if d == "right":
                if pos[1] + 1 >= len(matrix[0]):
                    return pos
                else:
                    matrix[pos[0]][pos[1]] = 0
                    pos[1] += 1
                    
            elif d == "up":
                if pos[0] - 1 < 0:
                    return pos
                else:
                    matrix[pos[0]][pos[1]] = 0
                    pos[0] -= 1
                    
            elif d == "left":
                if pos[1] - 1 < 0:
                    return pos
                else:
                    matrix[pos[0]][pos[1]] = 0
                    pos[1] -= 1
            
            else:
                if pos[0] + 1 >= len(matrix):
                    return pos
                else:
                    matrix[pos[0]][pos[1]] = 0
                    pos[0] += 1


#{ 
#  Driver Code Starts
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