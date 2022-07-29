//{ Driver Code Starts
//Initial template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function template for C++

class Solution{   
public:
    bool isPrime(int num) {
        if(num <= 1) return false;
        if (num <= 3)  return true; 
        
        int range = sqrt(num);
        if (num % 2 == 0 || num % 3 == 0) 
            return false; 
        
        for (int i = 5; i <= range; i += 6) 
            if (num % i == 0 || num % (i + 2) == 0) 
                return false; 
        
        return true;
    }

    int firingEmployees(vector<int> &arr, int n){
        unordered_map<int,vector<int>> mp;
        int geek = 0;
        for(int i=0; i<n; i++)
        {
            if(arr[i] != 0)
            mp[arr[i]].push_back(i+1);
            else
            geek = i + 1;
            
        }
        
        queue<int> q;
        for(auto it:mp[geek])
        q.push(it);
        
        int seniors = 0;
        int cnt = 0;
        while(!q.empty())
        {
             seniors++;
            int sz=q.size();
            for(int i=0;i<sz;i++)
            {
                int ind=q.front();
                q.pop();
                if(isPrime(ind+seniors))
                cnt++;
                
                  for(auto it:mp[ind])
                 q.push(it);
            }
        }
        
        return cnt;          
    }
};

//{ Driver Code Starts.

int main()
{
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        vector<int>arr(n,0);
        
        for(int i=0; i<n; i++)
            cin >> arr[i];

        Solution obj;
        cout << obj.firingEmployees(arr, n) << endl;
    }
    return 0;
}
// } Driver Code Ends