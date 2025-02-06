class Solution:
    '''
        Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
    '''
    
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:  
        median = 0                          # place holder for the median 
        merged_array = []                   # merging both input array
        if len(nums1) > 0:
            for num in nums1:
                merged_array.append(num)    # copy first input
        if len(nums2) > 0:
            if len(merged_array) > 0:
                for num2 in nums2:          # iterate through the second array
                    m = merged_array[len(merged_array) - 1] # get the last element from the merged
                    if m <= num2:
                        merged_array.append(num2)           # if the number greater then append
                    else:                                   # if the number smaller then iterate
                        for i,m in enumerate(merged_array):
                            if num2 < m:
                                merged_array.insert(i, num2)
                                break
            else:
                merged_array = nums2

        if len(merged_array) > 0:           # merged in a sorted way is completed
            msize = len(merged_array)
            rem = msize % 2
            divisor = msize //2
            if rem == 0:                    # even array
                median = (merged_array[divisor-1] + merged_array[divisor])/2
            else:
                median = merged_array[divisor]
        return median


testcases = list()
#merge two array with sorted; find the middle numbers; calculate the mean
testcases.append([[1,3], [2]])
testcases.append([[1,2], [3,4]])
testcases.append([[], [1]])
testcases.append([[1], []])
testcases.append([[2,2,4,4], [2,2,4,4]]) # 3.0
testcases.append([[2,2,4,4], [2,2,2,4,4]]) # 2.0
solution = Solution()
for i, testcase in enumerate(testcases):
    first_array = testcase[0]
    second_array = testcase[1]
    result = Solution.findMedianSortedArrays(solution, first_array, second_array)
    print(i+1, result)
        