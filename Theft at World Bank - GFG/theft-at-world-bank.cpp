// { Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution{
	public:
	struct compare
	{
	    bool operator() (const pair<long double, long long> &p1, const pair<long double, long long> &p2)
	    {
	        return (p1.first/p1.second)>(p2.first/p2.second);
	    }
	};
	
	bool isPerfectSq(long long num)
	{
	    long long x = sqrt(num);
	    return (x*x==num);
	}
	
	long double maximumProfit(int n, long long capacity, vector<long long> weight, vector<long long> profit)
	{
	    vector<pair<long double, long long>> gold(n);
	    
	    for(int i=0 ; i<n ; i++)
	    {
	        gold[i] = {profit[i], weight[i]};
	    }
	    
	    sort(gold.begin(), gold.end(), compare());
	    
	    long double ans=0;
	    
	    for(int i=0 ; i<n && capacity>0 ; i++)
	    {
	        if(isPerfectSq(gold[i].second))
	        {
	            continue;
	        }
	        
	        if(capacity>=gold[i].second)
	        {
	            ans += gold[i].first;
	            capacity -= gold[i].second;
	        }
	        else
	        {
	            ans += (gold[i].first/gold[i].second)*capacity;
	            capacity=0;
	        }
	    }
	    
	    return ans;
	}
};

// { Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int n;
		long long C;
		cin >> n >> C;
		vector<long long > w(n), p(n);
		for(int i = 0; i < n; i++){
		    cin >> w[i] >> p[i];
		}
		Solution ob;
		long double ans = ob.maximumProfit(n, C, w, p);
		cout << fixed << setprecision(3) << ans << "\n";
	}  
	return 0;
}  // } Driver Code Ends