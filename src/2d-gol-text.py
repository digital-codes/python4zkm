"""Fundamental processing of game of live"""
# we use numpy for 2d arrays
import numpy as np

# function definition: this is the core part
def step(a,d):
    """Compute the result array"""
    # create a new empty array
    b = np.empty((d,d))
    # set list of neighbour indices: up,down,left,right
    nd = ((-1,0),(1,0),(0,-1),(0,1))
    # loop over elements
    for i in range(d):
        for j in range(d):
            sum = 0
            # loop over neighbours: this is the very core
            for dd in nd:
                    si = i + dd[0]
                    sj = j + dd[1]
                    # ignore boundary pixels
                    # if not (si < 0 or si >=d or sj < 0 or sj >= d):
                    #     sum += a[si,sj]
                    # alternatively, we can wrap at the boundaries
                    si = d-1 if si < 0 else 0 if si == d else si
                    sj = d-1 if sj < 0 else 0 if sj == d else sj
                    sum += a[si,sj]
            # !!!!!!! important !!!!!!!!!
            # !!! evaluate sum
            b[i,j] = 1 if sum == 2 else 0
            # !!!!!!! important !!!!!!!!!
    return b


# main loop
def main():
    """Initialisation and main loop"""
    # set dimension
    d = 8 # dimension

    # create the initial matrix
    a = np.zeros((d,d))
    #print(a)

    # initialize matrix with random values
    for i in range(d):
        for ii in range(d):
            a[i,ii] = np.random.randint(0,2)
    print(a)

    iters = 0
    while True: # endless loop. We will break on certain conditions
        aa = a.copy() # save old value
        a = step(a,d).copy() # compute new values
        # maybe print the first 10 iterations
        if iters < 10:
            print("\n",a)
            
        # check stady state
        if np.array_equal(aa,a):
            if np.sum(a) > 0:
                print("Zombie after ",iters," iterations")
            else:
                print("Dead after ",iters," iterations")
            break
        # check iterations
        if iters == 1000:
            print("Still alive after ",iters," iterations")
            break
        iters += 1

    print("Done")
    print(a)


# call main
if __name__ == "__main__":
    main()
