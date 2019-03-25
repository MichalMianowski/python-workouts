# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 22:56:54 2019

@author: MM

simple guessing your number
"""

guessed = 0
low = 0
high = 100
ans = (low + high)/2

print("Please think of a number between 0 and 100!")

while guessed == 0:    
    print("Is your secret number",ans,"?")
    x = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    
    if x == 'h':
        high = ans
    elif x == 'l':
        low = ans
    elif x == 'c':
        print("Game over. Your secret number was:", ans)
        guessed = 1
    else:
        print("Sorry, I did not understand your input.")

    if (x == 'h' or x == 'l'):
        ans = int((low + high)/2)
    
    