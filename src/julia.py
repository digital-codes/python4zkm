import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors
#%matplotlib inline  # only for ipython
from numba import jit


##### this is used to show the image
def julia_image(N,z):
    dpi = 96
    width = 1 + 2*N//dpi 
    height = 1+ N//dpi
    
    fig, ax = plt.subplots(figsize=(width, height),dpi=72)

    # named colormaps:
    # gnuplot2 (default)
    # viridis
    # gray
    # magma
    # plasma
    # inferno
    # hot
    # nipy_spectral (good for original data, -.835, -2321)
    
    ax.imshow(z,cmap="nipy_spectral",origin='lower')
    #ax.imshow(z,cmap="viridis",origin='lower')
    plt.show()


# this computes the julia set
# try the different predefined parameter sets
# and/or vary the initial condition values as you like
@jit
def julia_numba(N):
    T = np.empty((N, 2*N), dtype=np.uint8)
    # rabbit: z2 −0.123 + 0.745i
    # basilika:  z2 −1
    # also:
    # c = 0.37 + 0.16i
    # c = −0.50−0.56i
    # c = −0.25

    # initial conditions    
    creal = .37 # -0.123 # -0.835
    cimag = .16 # .745 # - 0.2321
    h = 2.0/N
    # the main loop
    for J in range(N):
        for I in range(2*N):
            zimag = -1.0 + J*h
            zreal = -2.0 + I*h
            T[J,I] = 0
            zreal2 = zreal*zreal
            zimag2 = zimag*zimag
            while (zimag2 + zreal2 <= 4) and (T[J,I] < 255):
                zimag = 2* zreal*zimag + cimag
                zreal = zreal2 - zimag2 + creal
                zreal2 = zreal*zreal
                zimag2 = zimag*zimag 
                T[J,I] += 1
                
    julia_set = T
    return T

# main part 
N = 1000 # set size of image area
julia_set = julia_numba(N) # computer
# you can zoom into some areas with the lens tool
print(" you can zoom into some areas with the lens tool")
julia_image(N,julia_set) # display 

