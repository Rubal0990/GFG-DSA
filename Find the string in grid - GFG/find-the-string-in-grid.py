#User function Template for python3

class Solution:
    def help(self, board, w, r, c):
        x = [[-1, 0], [1, 0], [-1,0],
            [0, 1], [0, -1], [-1,-1],
            [-1,1], [1,-1], [1,1]]
        
        if board[r][c] != w[0]:
            return False
        
        for i in x:
            rs = r + i[0]
            cs = c + i[1]
            Flag = True
            
            for k in range(1,len(w)):
                if (0 <= rs < len(board)) and (0 <= cs < len(board[0])) and w[k] == board[rs][cs]:
                    rs += i[0]
                    cs += i[1]
                
                else:
                    Flag = False
                    break
            
            if Flag:
                return True
        
        return False

    def searchWord(self, board, word):
        l = []
        count = 0
        rows = len(board)
        cols = len(board[0])
        
        for i in range(rows):
            for j in range(cols):
                if self.help(board, word, i, j):
                    l.append([i, j])
        
        l.sort(key=lambda x:x[0])
        return l


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		grid = []
		for _ in range(n):
			cur  = input()
			temp = []
			for __ in cur:
				temp.append(__)
			grid.append(temp)
		word = input()
		obj = Solution()
		ans = obj.searchWord(grid, word)
		for _ in ans:
			for __ in _:
				print(__, end = " ")
			print()
		if len(ans)==0:
		    print(-1)

# } Driver Code Ends