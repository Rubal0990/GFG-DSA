//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++
int m = 1e9+7;
class Solution {
  public:
    int countPaths(int n, vector<vector<int>>& roads) {
        vector<pair<int, int>> adj[n];
        int u, v, wt;
        vector<int> temp;
        for(int i=0; i<roads.size(); i++)
        {
            temp = roads[i];
            u = temp[0];
            v = temp[1];
            wt = temp[2];
            if(u==v) continue;
            adj[u].push_back({v, wt});
            adj[v].push_back({u, wt});
        }
        
        vector<int> dist(n,1e8), cnt(n,0);
        dist[0] = 0;
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int> > > pq;
        pq.push({0, 0});
        
        while(!pq.empty())
        {
            int node = pq.top().second;
            int wt = pq.top().first;
            pq.pop();
            vector<pair<int,int>> temp = adj[node];
            for(int i=0; i<temp.size(); i++)
            {
                int child = temp[i].first;
                int x = wt + temp[i].second;
                int y = dist[child];
                if(x < y)
                {
                    dist[child] = x;
                    pq.push({x, child});
                    cnt[child] = 1;
                }
                else if(x==y)
                {
                    int z = cnt[child];
                    z = (z%m + 1)%m;
                    cnt[child] = z;
                    pq.push({x, child});// y am i pushing again though they are equal… just dry run it uh will understand
                }
            }
        }
        return cnt[n-1] % m;
    }
};

//{ Driver Code Starts.

int main() {
    int T;
    cin >> T;
    while (T--) {
        int n, m;
        cin >> n >> m;
        int u, v;

        vector<vector<int>> adj;

        for (int i = 0; i < m; ++i) {
            vector<int> temp;
            for (int j = 0; j < 3; ++j) {
                int x;
                cin >> x;
                temp.push_back(x);
            }
            adj.push_back(temp);
        }

        Solution obj;
        cout << obj.countPaths(n, adj) << "\n";
    }

    return 0;
}
// } Driver Code Ends