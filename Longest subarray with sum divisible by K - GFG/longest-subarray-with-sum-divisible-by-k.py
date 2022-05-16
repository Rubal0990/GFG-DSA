#User function Template for python3
class Solution:
	def longSubarrWthSumDivByK (self, arr,  n, k) : 
		dict_ = {}
		sumAll = 0
		max_ = 0
		
		for i in range(n):
		    sumAll += arr[i]
		    temp = ((sumAll%k)+k)%k
		    
		    if temp == 0:
		        max_ = i + 1
		    elif temp in dict_.keys():
		        if(max_ <(i - dict_[temp])):
		            max_ = i - dict_[temp]
		    else:
		        dict_[temp] = i
		        
		return max_



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	for _ in range(0,int(input())):
		n, K = map(int ,input().split())
		arr = list(map(int,input().strip().split()))
		ob = Solution()
		res = ob.longSubarrWthSumDivByK(arr, n, K)
		print(res)




# } Driver Code Ends