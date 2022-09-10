#User function Template for python3

class Solution:
    def inside(self , grid , i , j ) : 
        if i in range(len(grid)) and j in range(len(grid[0])) :
            return True
        return False
        
    def dfs(self,grid ,  i , j , val , index , full_string ,  max_index  , visited ):
        if not self.inside(grid,  i , j ) or visited[i][j] == True or grid[i][j] != val :
            return 0
        
        if grid[i][j] == val :
            index += 1 
            if index>= max_index : 
                return 1
            if index < max_index :
                val = full_string[index]
                visited[i][j] = True
                left    = self.dfs(grid , i , j-1 , val , index , full_string , max_index , visited )
                top     = self.dfs(grid , i-1 , j , val , index , full_string , max_index , visited )
                right   = self.dfs(grid , i , j+1 , val , index , full_string , max_index , visited )
                bottom  = self.dfs(grid , i+1 , j , val , index , full_string , max_index , visited )
                visited[i][j] = False
                return left + top + right + bottom
                      
                      
    def findOccurrence(self,mat,target):
        ans = 0 
        grid = mat
        visited = [ [ False for _ in range(len(grid[0]))] for _ in range(len(grid)) ]
        for i in range(len(grid)): 
            for j in range(len(grid[0])) :
                if grid[i][j] == target[0] : 
                    val = target[0]
                    max_index = len(target)
                    index = 0 
                    full_string = target
                    ans += self.dfs(grid , i , j , val , index  ,full_string  , max_index , visited ) 
        return ans 


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        R=int(line[0])
        C=int(line[1])
        mat=[]
        for _ in range(R):
            mat.append( [x for x in input().strip().split()] )
        target=input()
        obj = Solution()
        print(obj.findOccurrence(mat,target))
# } Driver Code Ends