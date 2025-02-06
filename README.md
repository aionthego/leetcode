# leetcode
 let us simplify the leet code problems

 ## 4. Median of two sorted arrays
 Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

 It is implemented by merging two arrays
 ```
 merge the first array; iterate the second array
 if nums2[index] greater than the last elelment of merged
     then append
 else iterate through merged
     find the correct location for the insert

 after the merge, find the median
 if odd, the median is the middle number
 if even, find the middle two numbers and get the average of them
 ```

 ## 28. Find the Index of the First Occurrence in a String
 Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 It is implemented by simplifying the Knuth–Morris–Pratt algorithm.
 ```
 move forward with haystack
 if haystack[index] matches with the first character of the needle
     then check for the full needle match
        if you find the needle
            then store the key index
        else
            go back in the haystack; no need to start from zero
 else move forward with haystack

 if you reach the end, process the result
 ```
