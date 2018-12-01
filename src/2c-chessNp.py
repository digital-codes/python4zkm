""" Demonstrate fundamental programming elements
by creating a checker board, 8 by 8 fields, 
field size is configurable, same width and height
"""

# numpy is a helper library
import numpy as np

# function to make one linear segment of a pattern
def segment(width, color):
    """ put <width> items of color in a row starting at position row,col (= y,x)"""
    # initialize a new list as a numpy array
    segment = np.empty(width) # 
    # add items with a FOR LOOP
    for i in range(width):
        segment[i] = color
    # return the list
    return segment

# the main function 
def main():
    """create a checker board pattern using a function"""

    # constants
    fields = 8
    fieldWidth = 2
    
    # variables
    row = 0
    column = 0
    # set color to 0
    color = 0
    # create the board matrix
    board = np.empty((fields*fieldWidth,fields*fieldWidth))
    while row < fields*fieldWidth and column < fields*fieldWidth:
        # append the segment
        board[row,column:column+fieldWidth] = segment(fieldWidth,color)
        # invert color
        color = 1 if color == 0 else 0
        # increment column
        column = column + fieldWidth if column < fieldWidth*(fields-1) else 0
        # increment row if column = 0
        row = row + 1 if column == 0 else row
        # invert color again if new row and end of field
        if column == 0 and row % fieldWidth == 0 :
            color = 1 if color == 0 else 0
        

    print("Checker board")
    print(board)
    

# call the main function
if __name__ == "__main__":
    main()
    

    
