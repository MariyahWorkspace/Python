# -*- coding: utf-8 -*-
"""Anudip3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1w3lJaAxJNmWkmEo70zM_Ru6F4tON3sc-
"""

#calculate area of rectangle

#user input
a = int(input("Enter the length of rectangle: "))
b = int(input("Enter the breadth of the rectangle: "))

#logic block
area = a*b

#output function
print("The area of rectangle is: ", area)

#calc simple interest

#user input
principal = int(input("Enter the amount: "))
rate = 7.5 #given
time = float(input("Enter the time period: "))

#logic block
simple_int = (principal*rate*time)/100

#output
print("The simple interest is:", simple_int, "for a period of", time, "years.")

#validate age using if...else

#user input
a = int(input("Enter the age: "))

#logic block
if a<=18:
  print("Invalid age! You are not eligible for the program.")
else:
  print("Congratulations! You are eligible for the program, hurray!")