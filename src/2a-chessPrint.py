""" Demonstrate fundamental programming elements
by creating a checker board, N by N fields,
field size is configurable, same width and height

The following programming constructs are demonstrated:

Comment
    # The "#" starts a comment until the end of the line
    # We can write whatever we want

Variable
    Normally, we have to remember values sometime in order to perform
    operations on or with them later on. A variable is an object which
    has a name and a value, like so:
    var1 = "some text"
    or
    var2 = 123
    or
    var3 = True
    We can change the value of variables any time

Constant
    A constant is basically a variable were the value cannot be changed
    (immutable). We don't have this here but we use some variables in this
    style

Operation
    We have a large number of operator available to do math, logic and other
    things like:
        a = 5 + 3
        b = a * 4
        c = a % 3  # The is the modulo operation (reminder)
        d = 5 == 6  # d is False. The double "=" means "has equal value"

Block
    Every language has it's own syntax to form group of statements. Python
    uses indentation. All statements in sequence with the same indent level
    are in the same block, like so:
    if a == 4 then:
        thing1a()   # call function thing1a in the IF branch
        thing1b()   # same identation => same block => do also thing1b
    else:           # same indent as the "if", previous block terminated
        thing2()    # new block, do thing2 in the ELSE branch
    thing3()        # not indented, previous block terminated. Thing3 is
                    # outside the IF-ELSE block

Branch
    We test a condition and do one thing when it is true and another thing
    when it is false using IF ... ELSE ... statements like:
    if a == 4:
        do thing 1
    else:
        do thing 2

Iteration (loop)
    We can repeat sections of the code several times in different ways, for
    example for a (fixed) number of times using a
    FOR LOOP like so:
        for i in range(10):
            statements ...
    of while a condition is true like so:
    while a < b:
        statements ...

Function
    we use functions to execute code which is (re)used several times
    we can provide parameters to the functions, so the same code can
    actually perform (slightly) different depending on the parameters
    Function can return "objects" (we don't know what exactly that is yet,
    but in Python more or less everything is an object)
    Functions have to be declared before we can use them like so:
    def <name>([paramters]):
        ... function code ...
        [return]

"""

########################################################################
# this is our first function declaration
# We have to decalre the function before we use it
# function to make one linear segment of a pattern
def segment(width, color):
    """ print <width> items of a color """
    # add items with a FOR LOOP
    for i in range(width):
        #print(color,end="") # simple verion
        print("{0:2d}".format(color),end="") # this looks better

########################################################################
# our second function is the main function
def main():
    """create a checker board pattern using a function"""

    # constants (actually just variables we do not change any more)
    fields = 4
    fieldWidth = 4

    # variables
    row = 0
    column = 0
    # set color to 0
    color = 0
    # we iterate until we are done ...
    while row < fields*fieldWidth and column < fields*fieldWidth:
        # print segment
        segment(fieldWidth, color)
        # invert color after every segment
        color = 1 if color == 0 else 0
        # increment column. go back to 0 after 8 fields
        column = column + fieldWidth if column < fieldWidth*(fields-1) else 0
        # new line and increment row if column = 0
        if column == 0:
            print("") # prints a new line
            # next row
            row = row + 1
        # invert color again if new row and end of field
        if column == 0 and row % fieldWidth == 0 :
            color = 1 if color == 0 else 0


########################################################################
# call the main function
if __name__ == "__main__":
    main()
