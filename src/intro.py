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

###########################################
# so far, we've dealt with individual items and lists and their np eqivalent, arrays
# a single list turns into an array with a single dimentsion
# we can also have more dimensions, for example two
# a 2D array is widley know as a table

# lets create an 2 d array with 3 rows and 4 columns, with type integer
n2d = np.empty((3,4),dtype=np.int16)

print("The array has 3 rows and 4 columns, but empty() \ndoes not set any data, so the values are random\n",n2d)

# we can extract specific cells with 2 indices and/or ranges

print("item 2 and 3 of the second row can be accessed like so:\n, n2d[1,1:3]\n",n2d[1,1:3])
print("Remember, the last index value is not included")

# the dimensionality of an array are called a "shape"
print("shape of n2d:", n2d.shape)

# a simple example for of a table is a weekly schedule like the following
wd = np.zeros((4,7),dtype=np.uint8) # this time, we use a 0 initialized 2d array
# columns go from Monday to Sunday
# rows are daily activities like sleep, eat, work, fun
# we put some numbers ....
wd[0,:] = [8,8,8,8,8,8,8] # 8 hours of sleep (sigh)
wd[1,:] = [2,2,2,2,2,3,3] # 
wd[2,:] = [8,8,8,8,8,0,0] # so much work ...
wd[3,:] = [6,6,6,6,6,15,15] # so much fun

print("Our week schedule looks like so:\n", wd)

###########################################
# to show is graphically, we use the standard plotting library
# matplotlib with the local name plt
import matplotlib.pyplot as plt

# create a plotting figure with 2 areas, vertically spaced
# this is the first one
axs = plt.subplot(2,1,1)

collabel=("MO","TU","WE","TH","FR","SA","SU") # this is a list but with round bracket
# we can access values like with [] but we cannot change them. This is called a tuple
rowlabel=("Sleep","Eat","Work","Fun")
axs.axis('tight')
axs.axis('off')
rcols = ["white"] * len(wd)
cecols = [["gray"] * len(wd[0])]*len(wd)
clcols = ["green"] * len(wd[0])

tbl = axs.table(cellText=wd,rowLabels=rowlabel,\
                      colLabels=collabel,loc='center',\
                      cellColours=cecols,\
                      colColours=clcols,rowColours=rcols)
tbl.auto_set_font_size(False)
tbl.set_fontsize(14)
tbl.scale(1.2, 1.4)
l, b, w, h = axs.get_position().bounds
axs.set_position([l + .1*w, b, w*.8, h])
axs.set_title("Weekly schedule")

# this is the second one
tplot = plt.subplot(2,1,2)
tplot.axis('off')
tplot.clear()
tplot.axis('off')
txt = """
the meaning of the table is very clear.
however, if we remove the row and columns labels
the context is completely lost and we have no idea
what these number should tell us ...
"""

tplot.annotate(txt,\
    xy=(1, 1), xytext=(.96,.94), xycoords="data", \
    textcoords="axes fraction",ha="right", va="top", size=14)

# show the figure
plt.show()






