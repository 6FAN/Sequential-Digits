#!/usr/bin/env python
# coding: utf-8

# * An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
# * Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

# **Example 1**
# 
# * **Input** : low = 100, high = 300
# * **OutPut**: [123, 234]

# **Example 2**
# 
# * **Input** : low = 1000, high = 13000
# * **Output**: [1234,2345,3456,4567,5678,6789,12345]

# In[4]:


class Solution:
    def sequetialDigits(self, low, high):
        # 1: Initialization
        s =  "123456789"
        res = []
        
        # 2: Iterating through Digits
        for i in range(len(s)):
            for j in range(i + 1, len(s) +1):
                
                # 3: Extracting Substrings and Converting to Integer
                curr = int(s[i:j])
                
                # 4: Checking Conditions and Adding to Result
                if low <= curr <= high:
                    res.append(curr)
         
        
        # 5: Sorting and Returning the Result
        res.sort()
        return res

    
low = int(input('Enter a Num :'))
high = int(input('Enter a Num : '))


obj = Solution()
obj.sequetialDigits(low, high)


# # Step by step algorithm

# **1: Initialization**
# * s is a string representing all the possible digits from 1 to 9 in sequence.
# * res is an empty list that will store the sequential digits within the range [low, high].

# **2: Iterating through Digits**
# 
# * The outer loop iterates over each starting index i of the digits.
# * The inner loop iterates over each ending index j of the digits, starting from i + 1.
# 

# **3: Extracting Substrings and Converting to Integer**
# 
# * s[i:j] extracts a substring from index i to index j, inclusive.
# * int() converts the substring into an integer.

# **4: Checking Conditions and Adding to Result**
# 
# * If the generated number num falls within the specified range [low, high], it's added to the result list res.

# **5: Sorting and Returning the Result**
# 
# * The result list res is sorted in ascending order and returned.

# # Explanection

# * In this program they are given low value it is 100 and high value it's 300.
# * We are taking a range 100 to 300, in that we get 123 and 234.
# * we are not taking a value 345 becuse it's a **greater Than 300** so skip.
