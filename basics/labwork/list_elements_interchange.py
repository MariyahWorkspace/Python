# -*- coding: utf-8 -*-
"""list_elements_interchange.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nv3-wmb0eBj6c3FQBmA04x5UrbppIyGo
"""

#program to interchange first and last elements in a list
list = ["Anna", "Shein", "Kali", "Stella"]
print("The original list is:",list)

#logic to reverse first element(from start index 0) and last element (first element from end)
list[0], list[-1] = list[-1], list[0]
print("The list after interchanging first and last elements:", list)