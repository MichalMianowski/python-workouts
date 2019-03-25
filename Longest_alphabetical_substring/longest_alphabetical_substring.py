# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 12:58:37 2019

@author: MM

program print out the longest substring in of given string s, 
in which the letters occur in alphabetical order
"""

s = input("give me some string")
posAns = s[0]   #possible answer
ans = s[0]
i = 0

for i in range(len(s)-1):
    
    if s[i] <= s[i+1]:
        posAns += s[i+1]
    else:
        if len(posAns) > len(ans):
            ans = posAns
        posAns = s[i+1]
if len(posAns) > len(ans):
            ans = posAns

print("Longest substring in alphabetical order is:", ans)