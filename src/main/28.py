class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        moveforward = True                  # keep the while loop running
        index = 0                           # initialize the index
        length = len(haystack)              # length; to check the index 
        found_index = list()                # place holder for the found items. list in case of multiple needles

        while moveforward:
            char = haystack[index]
            if char == needle[0]:           # check for match of the first character of the needle
                goback = index+1            # in case, no match, then don't need to start over from zero index
                full_needle = True
                key = index
                for n in needle:
                    if index < length:
                        char = haystack[index]
                        if char == n:       # check for all needle characters
                            index += 1
                        else:
                            index = goback
                            full_needle = False
                            break
                    else:
                        full_needle = False

                if full_needle:
                    found_index.append(key) # when full needle is found store the key index   
            else:        
                index += 1                  # continue the hay stack
                                            # end of the while loop
            if index >= length:
                moveforward = False

                                            # process the result
        result = -1
        if found_index:
            result = found_index[0]
        return result


testcases = list()
#add haystack and needle
testcases.append(["sadbutsad", "sad"])
testcases.append(["leetcode", "leeto"])
testcases.append(["aaa", "aa"])
testcases.append(["aa", "aaa"])
testcases.append(["mississippi", "issip"])
solution = Solution()
for i, testcase in enumerate(testcases):
    haystack = testcase[0]
    needle = testcase[1]
    result = Solution.strStr(solution, haystack, needle)
    print(i+1, haystack, needle, result)
        