# Geek and knots
## Medium 
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">M hooks are present in a straight line on wall A and N hooks are present in a straight line on wall B. Each hook on wall A is connected to each hooks on wall B by ropes. K ropes must be used to make the desired giant knot. How many such knots can Geek make ?<br>
<strong>Note:</strong> 2 knots are considered to be the same if they involve the same hooks.&nbsp;</span></p>

<p><br>
<span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
M = 3, N = 2, K = 2
<strong>Output:</strong> 3
<strong>Explaination: </strong>
hooks on Wall A are A1 A2 A3.
hooks on wall B are B1 B2. </span>

<span style="font-size:18px">Joining 
 A1  A2  A3
 |       |
 B1      B2</span>

<span style="font-size:18px">is same as joining 
 A1  A2  A3
 |       |
 B2      B1 
because the two groups involve the same hooks. 
But the groups (A1-B1, A3-B2), (A1-B1, A2-B2), 
(A2-B1, A3-B2) are all different.  </span></pre>

<p><br>
<span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
M = 2, N = 2, K = 2
<strong>Output:</strong> 1
<strong>Explaination: </strong>Any one of (A1-B1, A2-B2) 
and (A1-B2, A2-B1) can be used.</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:</strong><br>
You do not need to read input or print anything. Your task is to complete the function <strong>knots()</strong> which takes M, N and K as input parametes and returns the number of possible knots. Return the answer modulo 10<sup>9</sup>+7.</span></p>

<p><br>
<span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(max(N2, M2))<br>
<strong>Expected Auxiliary Space: </strong>O(max(N2, M2))</span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ N, M, K ≤ 1000<br>
1 ≤ K ≤ min(N, M)&nbsp;</span></p>
</div>