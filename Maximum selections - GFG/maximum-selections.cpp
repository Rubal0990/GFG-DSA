// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
// ranges[i][0] is the start of ith range
// ranges[i][1] is the end of ith range

class Solution{
public:
    static bool sortbysec(const vector<int> &a, const vector<int> &b)
    {
        return (a[1] < b[1]);
    }

    int max_non_overlapping(vector< vector<int> >& ranges)
    {
        sort(ranges.begin(),ranges.end(),sortbysec);
        
        int f1 = 0, f2 = 0, count = 0;
        while(f2 < ranges.size()){
            if(ranges[f2][0] >= ranges[f1][1]){
                f1 = f2;
                count++;
            }    
            f2++;
        }
        
        return count+1;
    }
};

// { Driver Code Starts.

int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		int n;
		cin>>n;

		vector< vector<int> > v(n,vector<int>(2));
		for(int i=0; i<n; i++)
			cin>> v[i][0] >> v[i][1];
			
        Solution ob;
		cout<< ob.max_non_overlapping(v) << endl;
	}
	return 1;
}

  // } Driver Code Ends