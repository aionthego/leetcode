# leetcode
 let us simplify the leet code problems

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
