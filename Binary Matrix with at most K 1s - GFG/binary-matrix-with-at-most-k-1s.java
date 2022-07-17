//{ Driver Code Starts
import java.io.*;
import java.util.*;

class GFG {
    public static void main(String args[]) throws IOException {
        BufferedReader read =
            new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while (t-- > 0) {
            String S[] = read.readLine().split(" ");
            int R = Integer.parseInt(S[0]);
            int C = Integer.parseInt(S[1]);
            
            ArrayList<ArrayList<Integer>> M = new ArrayList<>();
            
            for(int i=0; i<R; i++)
            {
                ArrayList<Integer> temp = new ArrayList<>();
                String S1[] = read.readLine().split(" ");
                for(int j=0; j<C; j++)
                {
                    temp.add(Integer.parseInt(S1[j]));
                }
                M.add(temp);
            }
            
            String S2[] = read.readLine().split(" ");
            int K = Integer.parseInt(S2[0]);
            int Q = Integer.parseInt(S2[1]);
            
            int[] q_i = new int[Q];
            int[] q_j = new int[Q];
            
            String S3[] = read.readLine().split(" ");
            String S4[] = read.readLine().split(" ");
            
            for(int i=0; i<Q; i++)
            {
                q_i[i] = Integer.parseInt(S3[i]);
                q_j[i] = Integer.parseInt(S4[i]);
            }
            
            Solution ob = new Solution();
            ArrayList<Integer> res = ob.largestSquare(M,R,C,K,Q,q_i,q_j);
            
            for(int i=0; i<Q; i++)
                System.out.print(res.get(i) + " ");
            System.out.println();
        }
    }
}
// } Driver Code Ends


//User function Template for Java

class Solution {
    static ArrayList<Integer> largestSquare(ArrayList<ArrayList<Integer>> M, int R, int C, int K, int Q, int[] q_i, int[] q_j) {
        ArrayList<Integer> res = new ArrayList<>();
        int[][] dp = new int[R+1][C+1];
        for(int i=1;i<=R;i++){
            for(int j=1;j<=C;j++){
                dp[i][j] = M.get(i-1).get(j-1)+dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1];
            }
        }
        for(int q=0;q<Q;q++){
            int i=q_i[q];
            int j=q_j[q];
            int d = Math.min(Math.min(i,j),Math.min(R-i-1,C-j-1));
            int ans=0;
            int l=0;
            int h=d;
            while(l<=h){
                int m = (l+h)/2;
                int x1=i-m;
                int y1=j-m;
                int x2=i+m;
                int y2=j+m;
                int count = dp[x2+1][y2+1]-dp[x1][y2+1]-dp[x2+1][y1]+dp[x1][y1];
                if(count<=K){
                    ans = 2*m+1;
                    l=m+1;
                }
                else{
                    h=m-1;
                }
            }
            res.add(ans);
        }
        return res;
    }
};