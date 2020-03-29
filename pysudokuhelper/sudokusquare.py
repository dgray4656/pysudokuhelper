class SudokuSquare():
    """
    This is a class that represents a single square in a sudoku puzzle.

    Attributes:
        value (int): The numeric value (between 1 and 9) assiged to the square.
        possible_values (list): A list containing values (between 1 and 9) that could be the value of the square.
        xpos (int): Column number (between 1 and 9) on the puzzle where the square is located.
        ypos (int): Row number (between -1 and -9) on the puzzle where the square is located.
        cellindex (int): Index value (between 0 and 80) that identifies the square on the puzzle board.

    Notes:
        * When the .value attribute is 'None', the .possible_values attribute will contain at least one possible value for the square.
        * When the .value attribute is set to a number between 1 and 9, the .possible_values attribute will be an empty list.
    """



    def __init__(self, initvalue=None, initx=None, inity=None):
        """
        The constructor for SudokuSquare class.

        Parameters:
            initvalue (int): Numeric value (between 1 and 9) assigned to the square at creation.  (Default is 'None').
            initx (int): Numeric value (between 1 and 9) reflecting the x-position of the square in a puzzle.  (Default is 'None').
            inity (int): Numeric value (between -1 and -9) reflectin the y-position of the square in a puzzle.  (Default is 'None').

        Notes:
            * the .cellindex attribute is set automaticaly based on values of .xpos and .ypos attributes.
        """
        if initvalue:
            self.value=initvalue
            self.possible_values=[]
            self.xpos=initx
            self.ypos=inity
        else:
            self.value=None
            self.possible_values=[1,2,3,4,5,6,7,8,9]
            self.xpos=initx
            self.ypos=inity
        self.cellindex=(((-inity - 1)*9)-1) + initx

    def setvalue(self, inputval):
        """
        The function to set the value of the SudokuSquare.

        Parameters: 
            inputval (int): The numeric value to store in the square's .value attribute.  If the inputval is not between 1 and 9 (inclusive), the function does nothing.

        Returns: Nothing.
        """
        if inputval>0 and inputval<10:
            self.value=inputval
            self.possible_values=[]

    def clearvalue(self):
        """
        The function to set the value of the SudokuSquare back to 'None'.

        Parameters: None.
        Returns: Nothing.
        """
        self.value=None
        self.possible_values=[1,2,3,4,5,6,7,8,9]

    def clearpossible(self, valtoclear):
        """
        The function to eliminate a value from the list referenced by the .possible_values attribute.

        Parameters: 
            valtoclear (int): the numeric value to remove from the list in .possible_values.  If the valtoclear is not included in .possible_values, the function does nothing.

        Returns: Nothing.
        """
        if valtoclear in self.possible_values:
            self.possible_values.remove(valtoclear)

    def getstate(self):
        """
        The function to return the .value property if it is not 'None', otherwise return the .possible_values property.

        Parameters: None.
        Returns: a string containing either the .valueproperty or a set of .possible_values enclosed in square brackets
        """
        if self.value is None:
            s="["
            for x  in self.possible_values:
                s+=str(x)
            s+="]"
            return s
        else:
            return str(self.value)

