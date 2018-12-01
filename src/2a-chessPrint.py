""" Demonstrate fundamental programming elements
by creating a checker board, 8 by 8 fields, 
field size is configurable, same width and height
"""

# function to make one linear segment of a pattern
def segment(width, color):
    """ print <width> items of a color """
    # add items with a FOR LOOP
    for i in range(width):
        # print(color,end="") # simple verion
        print("{0:2d}".format(color),end="") # this looks better

# the main function 
def main():
    """create a checker board pattern using a function"""

    # constants
    fields = 8
    fieldWidth = 4
    
    # variables
    row = 0
    column = 0
    # set color to 0
    color = 0
    while row < fields*fieldWidth and column < fields*fieldWidth:
        # print segment
        segment(fieldWidth,color)
        # invert color
        color = 1 if color == 0 else 0
        # increment column
        column = column + fieldWidth if column < fieldWidth*(fields-1) else 0
        # new line and increment row if column = 0
        if column == 0:
            print("") # prints a new line
            # reset line
            row = row + 1
        # invert color again if new row and end of field
        if column == 0 and row % fieldWidth == 0 :
            color = 1 if color == 0 else 0
        

# call the main function
if __name__ == "__main__":
    main()
    

    
