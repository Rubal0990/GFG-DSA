// { Driver Code Starts
// Initial Template for C++
#include <bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
// User function Template for C++

class Solution {
  public:
    int minVal(int a, int b) {
        int setbits = __builtin_popcount(b);
		int ans = 0;
		
		for (int i = 30; i >= 0; i--) {
			if ((a >> i) & 1) {
				if (setbits > 0) {
					setbits--;
					ans += (1 << i);
				}
			}
		}
		
		for (int i = 0; i <= 30; i++) {
			if (!((ans >> i) & 1)) {
				if (setbits > 0) {
					setbits--;
					ans += (1 << i);
				}
			}
		}
		return ans;
    }
};

// { Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int a, b;
        cin >> a >> b;

        Solution ob;
        cout << ob.minVal(a, b);

        cout << "\n";
    }

    return 0;
}  // } Driver Code Ends