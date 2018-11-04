
# coding: utf-8

# In[40]:


"""Fundamental processing of game of live"""
# we use numpy for 2d arraays
import numpy as np
# set dimension
d = 8 # dimension
a = np.zeros((d,d))
print(a)


# In[41]:


for i in range(d):
    for ii in range(d):
        a[i,ii] = np.random.randint(0,2)
print(a)


# In[42]:


def step(a):
    """Compute the result array"""
    # create a new empty array
    b = np.empty((d,d))
    # set list of neighbour indices: up,down,left,right
    nd = ((-1,0),(1,0),(0,-1),(0,1))
    # loop over elements
    for i in range(d):
        for j in range(d):
            sum = 0
            # loop over neighbours
            for dd in nd:
                    si = i + dd[0]
                    sj = j + dd[1]
                    # check boundaries
                    if not (si < 0 or si >=d or sj < 0 or sj >= d):
                        sum += a[si,sj]
            # !!! evaluate sum             
            b[i,j] = 1 if sum == 2 else 0
    return b


# In[43]:


iters = 0
while np.sum(a) > 0:
    aa = a.copy() # save old value
    a = step(a).copy() # compute new values
    print(a)
    # check stady state
    if np.array_equal(aa,a):
        print("Steady state")
        break
    # check iterations
    if iters == 100:
        print("Exit after ",iters," iterations")
        break
    iters += 1

print("Done")

