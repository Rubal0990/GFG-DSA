// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
//User function template for C++

class Solution{
  public:
    long long findRank(string str) {
       string s = str;
        int n = str.size(), k = 0;
        long long int fact[n+1] = {0}, ans = 0;
        fact[0] = 1;
        for(int i=1; i<=n; i++){
            fact[i] = fact[i-1]*i;
        }
        while(n){
            sort(s.begin(), s.end());
            int idx = 0;
            for(int i=0; s[i]!='\0'; i++){
                //cout << s[i] << " " << str[k] << " ";
                if(s[i] == str[k]){
                    idx = i;
                    s.erase(s.begin()+idx);
                    break;
                }
            }
            //cout << n << " " << idx << " " << ans << " " << s << "\n";
            ans += idx*fact[n-1];
            n--;
            k++;
        }
        return ans+1;
    }
};

// { Driver Code Starts.
int main(){
    int T;
    cin>>T;
    while(T--){
        string s;
        cin>>s;
        Solution obj;
        long long ans = obj.findRank(s);
        cout<<ans<<endl;
    }
}  // } Driver Code Ends