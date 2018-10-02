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

#####################################
# you can type the instructions directly in the python shell
# where you see the output.
# make sure you type only in the line with the leading ">>>"
#####################################

#define and print a variable
# integer number
a = 3
print("Variable a is: ",a,", type is ",type(a))

# A float number:
# A float (rationale Zahl) can have digits after
# the decimal point while an integer doesn't (ganze zahl)

aa = 3.14159
print("Variable aa is: ",aa,", type is ",type(aa))

# text (string)
b = "zkm"
print("Variable b is: ",b,", type is ",type(b))

# a list (vector, array) of numbers
# a list of elements enclosed in [ ]
c = [4,3,2,1]
print("Variable c is: ",c,", type is ",type(c))

# individual elements of a list
# can be address with an index
# all indices start from 0, by default
print("First element of variable c is: ",c[0],", type is ",type(c[0]))
print("Second element of variable c is: ",c[1],", type is ",type(c[1]))

# we can use another variable as index
d = 3
print("Element ",d," of variable c is: ",c[d],", type is ",type(c[d]))

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
    print("Element is : ",cc)
# Again, we have the ":" and the indentation
# This time, we don't have an explicit index
# but we don't need to check the index range any more
# less errors!

######################################
# input options
# let's see how can we enter the data into the program

print("Example demonstating keyboard input\n")

a1 = input("Raw input, text or number\n")
print("type: ",type(a1),", value: ",a1)

a2 = eval(input("Evaluated input, text, number, list or dict. Text enclosed in \"\"\n"))
print("type: ",type(a2),", value: ",a2)

a3,b1 = eval(input("Evaluated input, 2 entries as before, separated by ,\n"))
print("A - type: ",type(a3),", value: ",a3)
print("B - type: ",type(b1),", value: ",b1)

a4 = eval(input("Evaluated input, 2 entries as before, separated by ,\n"))

if "tuple" in str(type(a4)) or "list" in str(type(a4)):
    for aa in a4:
        print("type: ",type(aa),", value: ",aa)
else:   
    print("type: ",type(a4),", value: ",a4)


################################################
# back to operation ...
print("Let's go back to the data ....\n")

# Now, let's take the list and convert it into a numpy array
# All functions imported from the numpy module
# have to be prefixed with np.
# So here we use the function array()
# with c as the parameter
print("When working with larger amounts of data \
we need additional functions, e.g. for operations \
on multiple items at the same time.\n\
Numpy (numerical python) is a library which \
provides a lot of such functions.\n\
However, we need to get the numbers into numpy types\n\
For example, we can turn a list into an numpy array")

nc = np.array(c)
print("Variable nc (numpy) is: ",nc)
# This looks quite the same so far

# but we can also change the data type, to float, for example
nf = np.array(c,"float")
print("Variable nf (numpy) is: ",nf)

# there are a few more differences to lists, e.g on multiplication
print("Multiply the list by 2 give a list with twice as many items: \n",2*c)
print("Multiply the array by 2 multiplies the elements: ",2*nc)
print("With numpy arrays we have to use the append function to get longer arrays")
print(np.append(nc,nc))
print("We can also repeat each item in an array with np.repeat")
print(np.repeat(nc,2))

# we can also turn the text into a numpy array
print("We can also convert strings into numeric arrays")
nt = np.fromstring(b,"uint8")
print("Variable nt from ",b," as unisgned integer array (uint) is: ",nt)

