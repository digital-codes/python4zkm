""" Demonstrate fundamental programming elements
by creating a checker board, 8 by 8 fields,
field size is configurable, same width and height

This is basically the same as in the previous example, but instead
of printing the segment immediately we create a data structure
based upon lists ([]) and append the segment to the line

"""

# function to make one linear segment of a pattern
def segment(width, color):
    """ put <width> items of color in a row"""
    # initialize a new list
    segment = []
    # add items with a FOR LOOP
    for i in range(width):
        segment.append(color)
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
    # create the empty board
    board = []
    # create an empty line to start with
    line = []
    while row < fields*fieldWidth and column < fields*fieldWidth:
        # append the segment to the line
        line.append(segment(fieldWidth,color))
        # invert color
        color = 1 if color == 0 else 0
        # increment column
        column = column + fieldWidth if column < fieldWidth*(fields-1) else 0
        # if column == 0 then previous line is complete.
        # add line to board, increment row and start a new line
        if column == 0:
            board.append(line)
            row = row + 1
            line = []
        # invert color again if new row and end of field
        if column == 0 and row % fieldWidth == 0 :
            color = 1 if color == 0 else 0


    print("Checker board")
    for b in board:
        print(b)


# call the main function
if __name__ == "__main__":
    main()
