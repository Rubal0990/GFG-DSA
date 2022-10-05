//{ Driver Code Starts
// Initial Template for C++
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++
class Solution {
  public:
    string lexicographicallySmallest(string S, int k) {
        
        string ans="";
        int l=S.length();
        
        if(l&(l-1)) k+=k;
        else k/=2;
        
        if(k>=l) return "-1";
        
        stack<char>st;
        
        for(int i=0;i<l;i++){
            
            while(!st.empty() && k>0 && st.top()>S[i]) {
                st.pop();
                k--;
            }
            st.push(S[i]);
        }
        
        if(k>0) while(k--) st.pop();
        
        while(!st.empty()){
            ans=st.top()+ans;
            st.pop();
        }
        return ans;
    }
};


//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        string S;
        int k;
        cin >> S >> k;
        Solution ob;
        cout << ob.lexicographicallySmallest(S, k) << endl;
    }
    return 0;
}

// } Driver Code Ends