# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 13:04:14 2019

@author: MM


Program finds the smallest monthly payment to the cent such that we can pay off
 the debt (from credit card) within a year.
 
 balance - the outstanding balance on the credit card
 annualInterestRate - annual interest rate as a decimal
 
 Monthly interest rate = (Annual interest rate) / 12.0
 Monthly payment lower bound = Balance / 12
 Monthly payment upper bound = (Balance x (1 + Monthly interest rate)^12) / 12.0
"""

balance = input("input the outstanding balance on the credit card")
annualInterestRate = input("input annual interest rate as a decimal")

monPayment = 0
remBalance = balance
monInterestRate = annualInterestRate/12.0

lowPayBound = balance/12
upPayBound = (balance * (1+monInterestRate)**12)/12.0
 
while 0 < remBalance or remBalance< -0.2:
    remBalance = balance
    monPayment = round((lowPayBound + upPayBound)/2 , 2)
    
    for month in range(12):
        monBalance = remBalance - monPayment
        remBalance = monBalance + (monInterestRate*monBalance)
        
    if remBalance > 0:
        lowPayBound = monPayment
    elif remBalance <-0.2:
        upPayBound = monPayment
    
print("Lowest Payment:", monPayment)