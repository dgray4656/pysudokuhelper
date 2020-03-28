
import sudokusquare

class GameBoard():
    """
    This is a class that represents a 9x9 Sudoku puzzle, consisting of 81 individual SudokuSquares.

    Attributes: 
        cells (list): A list of 81 SudokuSquares.
        rows (dictionary): A dictionary with 9 keys corresponding to the integers between 1-9.  The value of each key is a list with references to the SudokuSquares in that row of the puzzle.
        columns (dictionary): A dictionary with 9 keys corresponding to the integers between 1-9.  The value of each key is a list with references to the SudokuSquares in that column of the puzzle. 
        blocks (dictionary): A dictionary with 9 keys corresponding to the integers between 1-9.  The value of each key is a list with references to the SudokuSquares in that block of the puzzle.
    """

    def __init__(self):
        """
        The constructor for GameBoard class.

        Parameters:
            * None

        Notes:
            * The SudokuSquares referenced in .cells are created starting with the top left square (index=0), then moving horizontally until the top row is filled (index=8).  Then the second row is built, startin with the left square and moving to the right.  This pattern is followed until all rows have been filled.  The bottom right square will be created last (index=80).
            * The columns in a gameboard are numbered 1 to 9 moving from left to right. The .xpos attribute of cells in the first column (.column[1]) will be 1, and so on.
            * the rows in a gameboard are numbered -1 to -9 moving from top to bottom.  The .ypos attribute of cells in the top row (.rows[1]) will be -1, and so on.  Consider the gameboard to exist in the bottom right quadrant of a cartesian coordinate grid.
            * the blocks in a gameboard represent the 3x3 blocks that make up the 9x9 gameboard.  The squares in .blocks[1] are in the top left of the gameboard; the squares in .blocks[3] are in the top right of the gameboard, and the squares in .blocks[9] are in the bottom right of the gameboard.     
        """
        self.cells=[]
        x1range=range(1,10)
        y1range=range(-1,-10,-1)
        for y in y1range:
            for x in x1range:
                self.cells.append(sudokusquare.SudokuSquare(initx=x,inity=y))

        self.rows={1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
        self.columns={1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
        self.blocks={1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}

        for x in self.cells:
            if x.ypos == -1:
                self.rows[1].append(x)
            if x.ypos == -2:
                self.rows[2].append(x)
            if x.ypos == -3:
                self.rows[3].append(x)
            if x.ypos == -4:
                self.rows[4].append(x)
            if x.ypos == -5:
                self.rows[5].append(x)
            if x.ypos == -6:
                self.rows[6].append(x)
            if x.ypos == -7:
                self.rows[7].append(x)
            if x.ypos == -8:
                self.rows[8].append(x)
            if x.ypos == -9:
                self.rows[9].append(x)
            if x.xpos == 1:
                self.columns[1].append(x)
            if x.xpos == 2:
                self.columns[2].append(x)
            if x.xpos == 3:
                self.columns[3].append(x)
            if x.xpos == 4:
                self.columns[4].append(x)
            if x.xpos == 5:
                self.columns[5].append(x)
            if x.xpos == 6:
                self.columns[6].append(x)
            if x.xpos == 7:
                self.columns[7].append(x)
            if x.xpos == 8:
                self.columns[8].append(x)
            if x.xpos == 9:
                self.columns[9].append(x)
            if x.xpos in [1,2,3]:
                if x.ypos in [-1,-2,-3]:
                    self.blocks[1].append(x)
                if x.ypos in [-4,-5,-6]:
                    self.blocks[4].append(x)
                if x.ypos in [-7,-8,-9]:
                    self.blocks[7].append(x)
            if x.xpos in [4,5,6]:
                if x.ypos in [-1,-2,-3]:
                    self.blocks[2].append(x)
                if x.ypos in [-4,-5,-6]:
                    self.blocks[5].append(x)
                if x.ypos in [-7,-8,-9]:
                    self.blocks[8].append(x)
            if x.xpos in [7,8,9]:
                if x.ypos in [-1,-2,-3]:
                    self.blocks[3].append(x)
                if x.ypos in [-4,-5,-6]:
                    self.blocks[6].append(x)
                if x.ypos in [-7,-8,-9]:
                    self.blocks[9].append(x)

    def _updateallpossiblevalues(self):
        dummylist=[]
        for x in self.rows:
            for y in self.rows[x]:
                if y.value is not None:
                    dummylist.append(y.value)
            for y in self.rows[x]:
                if y.value is None:
                    for z in dummylist:
                        y.clearpossible(z)
            dummylist=[]

        for x in self.columns:
            for y in self.columns[x]:
                if y.value is not None:
                    dummylist.append(y.value)
            for y in self.columns[x]:
                if y.value is None:
                    for z in dummylist:
                        y.clearpossible(z)
            dummylist=[]

        for x in self.blocks:
            for y in self.blocks[x]:
                if y.value is not None:
                    dummylist.append(y.value)
            for y in self.blocks[x]:
                if y.value is None:
                    for z in dummylist:
                        y.clearpossible(z)
            dummylist=[]

    def _processnakedtwins(self,dictoflists):
        for x in dictoflists:
            twooptions=[]
            tempdict={}
            for sq in dictoflists[x]:
                if sq.value is None:
                    if len(sq.possible_values)==2:
                        twooptions.append(sq.possible_values)
            if len(twooptions):
                for pair in twooptions:
                    cellindexes=[]
                    for sq in dictoflists[x]:
                        if sq.possible_values == pair:
                            cellindexes.append(sq.cellindex)
                    temptuple=tuple(pair)
                    tempdict.update({temptuple : cellindexes})
            for pair in tempdict:
                if len(tempdict[pair])==2:
                    for sq in dictoflists[x]:
                        if sq.value is None:
                            if sq.cellindex not in tempdict[pair]:
                                for val in pair:
                                    sq.clearpossible(val)
            self._updateallpossiblevalues()

    def _setonlypossiblevalues(self,dictoflists):
        for k in dictoflists:
            availablevalues=[1,2,3,4,5,6,7,8,9]
            tempdict={}
            for sq in dictoflists[k]:
                if sq.value is not None:
                    availablevalues.remove(sq.value)
            for val in availablevalues:
                tempcellindexes=[]
                for sq in dictoflists[k]:
                    if val in sq.possible_values:
                        tempcellindexes.append(sq.cellindex)
                        tempdict.update({val:tempcellindexes})
            for k in tempdict:
                if len(tempdict[k])==1:
                    self.cells[tempdict[k][0]].setvalue(k)
        self._updateallpossiblevalues()

    def setcellvalue(self, cellindex, cellvalue):
        """
        The function to set the .value property of a specific SudokuSquare within the game board.  Also makes necessary changes to the .possible_values property of all other SudokuSquares within the game board.

        Parameters: 
            * cellindex (int): index value between 0-80 to identify the member of .cells list to be updated.
            * callvalue (int): integer between 1-9 to be set to the .value property of the cell identified by cellindex.

        Returns: None.
        """
        self.cells[cellindex].setvalue(cellvalue)
        self._updateallpossiblevalues()

    def setcellvalues(self, lindexvalues):
        """
        The function to populate values of multiple SudokuSquares within a game board.

        Parameters:
            * lindexvalues (list): a list containing a set of 2-element lists.  item[0] within each member list is used as the index of the SudokuSquare to be set, and item[1] within that member list provides the value to be set.

        Returns: None.
        """
        for x in lindexvalues:
            self.cells[x[0]].setvalue(x[1])
        self._updateallpossiblevalues()

    def displaycells(self):
        """
        The function to display the current details of each SudokuSquare in the .cells property of the game board.  If the SudokuSquare has a value set, the output is .cellindex, .xpos, .ypos, .value.  Otherwise, the output is .cellindex, .xpos, .ypos, .possible_values.

        Parameters: None.
        Returns: None.
        """
        for x in self.cells:
            if x.value is not None:
                print(x.cellindex," |",x.xpos,x.ypos,x.value)
            else:
                print(x.cellindex," |",x.xpos,x.ypos,x.possible_values)

    def countcellsforautoset(self):
        """
        The function to count how many SudokuSquares in a game board with a value set to 'None' have only a single member of .possible_values.

        Parameters: None.
        Returns:
            * integer representing the number of SudokuSquares within the game board with a value of 'None' and a single element in the .possible_values list.
        """
        counter = 0
        for x in self.cells:
            if x.value is None:
                if len(x.possible_values)==1:
                    counter += 1
        return counter

    def autosetcellvalues(self):
        """
        The function to identify every SudokuSquare within the game board with .value set to 'None' and a single value in the .possible_values list, and to set .value to the value in .possible_values.  Also goes through all cells in the game board and updates their .possible_values lists.

        Parameters: None.
        Returns: None. 
        """
        for x in self.cells:
            if x.value is None:
                if len(x.possible_values)==1:
                    x.setvalue(x.possible_values[0])
                    self._updateallpossiblevalues()

    def updatecellvalues(self):
        """
        The function to set the value of SudokuSquares with a value of 'None' and only 1 value in .possible_values until there are no more SudokuSquares with a value of 'None' and only 1 value in .possible_values remaining.

        Parameters: None.
        Returns: None.
        """
        while self.countcellsforautoset():
            self.autosetcellvalues()

    def processnakedtwins(self):
        """
        The function to search for pairs of SudokuSquares within each row, column, or block that have the exact same (2) .possible_values (aka 'naked twins').  If found, remove these (2) .possible_values from each other SudokuSquare within the same row, column, or block.

        Parameters: None.
        Returns: None.
        """
        self._processnakedtwins(self.rows)
        self._processnakedtwins(self.columns)
        self._processnakedtwins(self.blocks)

    def setcellswhenonlypossiblevalue(self):
        """
        The function to identify when a given value can only be placed in a single SudokuSquare within a given row, colum, or block, and to assign that value to the .value field of that SudokuSquare.

        Parameters: None.
        Returns: None.
        """
        self._setonlypossiblevalues(self.rows)
        self._setonlypossiblevalues(self.columns)
        self._setonlypossiblevalues(self.blocks)

    def clearcellpossbasedonblockposs(self):
        """
        The function to search each block for cases where a given possible_value can only be assigned to SudokuSquares within a given row or column.  In this situation, remove that possible_value from the .possible_values list of each SudokuSquare within that row or column that does NOT fall within the block.

        Parameters: None.
        Returns: None.
        """
        for x in self.blocks:
            availablevalues=[1,2,3,4,5,6,7,8,9]
            tempdict={}
            for sq in self.blocks[x]:
                if sq.value is not None:
                    availablevalues.remove(sq.value)
            for val in availablevalues:
                tempcellindexes=[]
                for sq in self.blocks[x]:
                    if val in sq.possible_values:
                        tempcellindexes.append(sq.cellindex)
                        tempdict.update({val:tempcellindexes})
            for k in tempdict:
                setofx=set()
                setofy=set()
                for ci in tempdict[k]:
                    setofx.add(self.cells[ci].xpos)
                    setofy.add(self.cells[ci].ypos)
                if len(setofx)==1:
                    for sq in self.columns[list(setofx)[0]]:
                        if sq.cellindex not in tempdict[k]:
                            self.cells[sq.cellindex].clearpossible(k)                
                if len(setofy)==1:
                    for sq in self.rows[(list(setofy)[0])*-1]:
                        if sq.cellindex not in tempdict[k]:
                            self.cells[sq.cellindex].clearpossible(k)         

    def countsolvedcells(self):
        """
        The function to return the number of SudokuSquares within the game board that have the .value property set to a numeric value, and not set to None.

        Parameters: None.
        Returns: None.
        """
        counter = 0
        for x in self.cells:
            if x.value is not None:
                counter+=1
        return counter

    def gdisplay(self):
        """
        The function to display the current status of the game board, displaying the value of each SudokuSquare in a 9x9 grid.

        Parameters: None.
        Returns: None.
        """
        ss="+"
        for x in range(1,10):
            ss+="-"*8 + "+"

        bss="+"
        for x in range(1,10):
            bss+="="*8 + "+"

        print(bss)
        for y in self.rows:
            print(f"| {str(self.rows[y][0].value):^6} | {str(self.rows[y][1].value):^6} | {str(self.rows[y][2].value):^6} | {str(self.rows[y][3].value):^6} | {str(self.rows[y][4].value):^6} | {str(self.rows[y][5].value):^6} | {str(self.rows[y][6].value):^6} | {str(self.rows[y][7].value):^6} | {str(self.rows[y][8].value):^6} |")
            if not y % 3:
                print(bss)
            else:
                print(ss)


