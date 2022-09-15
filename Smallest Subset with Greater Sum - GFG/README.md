# Smallest Subset with Greater Sum
## Easy 
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">You are given an array <strong>Arr</strong> of size <strong>N</strong> containing&nbsp;non-negative integers. Your task is to choose&nbsp;the <strong>minimum</strong> number of elements such that their sum should be greater than the sum of the rest of the elements of the array.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong></span>
<span style="font-size:18px">N = 4&nbsp;</span>
<span style="font-size:18px">Arr[] = {2, 17, 7, 3}</span>
<strong><span style="font-size:18px">Output:</span></strong>
<span style="font-size:18px">1</span>
<strong><span style="font-size:18px">Explanation:</span></strong>
<span style="font-size:18px">If we only select element 17, the sum of the 
rest of the elements will be (2+3+7)=12.
So the answer will be 1.</span>

<strong><span style="font-size:18px">Example 2:</span></strong></pre>

<pre><strong><span style="font-size:18px">Input:</span></strong>
<span style="font-size:18px">N = 4</span>
<span style="font-size:18px">Arr = {20, 12, 18, 4}</span>
<strong><span style="font-size:18px">Output:</span></strong>
<span style="font-size:18px">2</span>
<strong><span style="font-size:18px">Explanation:
</span></strong><span style="font-size:18px">If we select 12 and 18 from the array, 
the sum will be (12+18) = 30 and the sum of 
the rest of the elements will be (20+4) = 24. 
So, the answer will be 2. We can also 
select 20 and 18 as well.</span>

</pre>

<p><strong><span style="font-size:18px">Your Task:</span></strong></p>

<p><span style="font-size:18px">You don't need to read input or print anything. Your task is to complete the function <strong>minSubset()</strong>&nbsp;which takes the array&nbsp;<strong>Arr[]</strong>&nbsp;and its size <strong>N&nbsp;</strong>as inputs and returns the minimum number of elements to be selected.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong>&nbsp;O(N log N)<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(1)</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= N&nbsp;&lt;= 10<sup>5</sup><br>
1 &lt;= Arr[i] &lt;= 10<sup>9</sup><br>
Array may contain duplicate elements.&nbsp;</span></p>
</div>