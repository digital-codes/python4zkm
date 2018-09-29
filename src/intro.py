# python is an interpreted language
# we use version 3: python3

# The character "#" indicates a comment,
# up to the end of the line 

# First, we import an external module
# which has functionality written
# by someone else ...
# The module name is numpy
# we use it here with the local name np
# It is used for various mathematical operations
import numpy as np

#define and print a variable
# integer number
a = 3
print("Variable a is: ",a)

# A float number:
# A float (rationale Zahl) can have digits after
# the decimal point while an integer doesn't (ganze zahl)

aa = 3.14159
print("Variable aa is: ",aa)

# text (string)
b = "zkm"
print("Variable b is: ",b)

# a list (vector, array) of numbers
# a list of elements enclosed in [ ]
c = [4,3,2,1]
print("Variable c is: ",c)

# individual elements of a list
# can be address with an index
# all indices start from 0, by default
print("First element of variable c is: ",c[0])
print("Second element of variable c is: ",c[1])

# we can use another variable as index
d = 3
print("Element ",d," of variable c is: ",c[d])

# if we use an invalid index, python will be unhappy
#print("Element 5 of variable c is: ",c[5])
# it's better to comment this code out by placing a "#"
# at the start of the line


# we can iterate of all elements in a list in different ways
# with a for loop:
for i in range(0,4):
    print("Element ",i,": ",c[i])
# Please note three things here:
#   1) the range 0,4 seems to covers 5 elements,
#   but the last one is NOT included
#   2) the line with the condition (control statement) ends with ":"
#   3) the following line is indented
# This holds in general for all control structures in python

# Alternatively, we can use the "in" operator
for cc in c:
    print("(next) element is : ",cc)
# Again, we have the ":" and the indentation
# This time, we don't have an explicit index
# but we don't need to check the index range any more
# less errors!

# Now, let's take the list and convert it into a numpy array
# All functions imported from the numpy module
# have to be prefixed with np.
# So here we use the function array()
# with c as the parameter
nc = np.array(c)
print("Variable nc (numpy) is: ",nc)
# This looks quite the same so far

# but we can also change the data type, to float, for example
nf = np.array(c,"float")
print("Variable nf (numpy) is: ",nf)

# there are a few more differences, e.g on multiplication
print("Multiply the basic list by 2 gives a list with twice as many items: \n",2*c)
print("Multiply the numpy array by 2 multiplies the elements: ",2*nc)

# we can also turn the text into a numpy array
nt = np.fromstring(b,"uint8")
print("Variable nt from text variable b(\"",b,"\") as unisgned integer array (uint) is: ",nt)

#####################################
# you can type more instructions directly in the python shell
# where you see the output.
# make sure you type only in the line with the leading ">>>"

print("\nDo some tests ...\n")

# we can now go on to the next example ...
print("We can now go on to the next example ...")

