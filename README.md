# pySudokuHelper

This package can help users solve Sudoku puzzles of different difficulties.  It has been built using the 'Sudoku' game distributed with Debian 10.  pySudokuHelper can:

- identify candidate values for all squares based on initial state of a given puzzle
- identify which squares have a single candidate value, and set the value for those squares
- identify which values have a single valid destination square for each row, column, and block, and set the value for those squares
- identify 'naked twins' in each row, column, or block, and eliminate the values from all other open cells in the same row, column, or block.

This package should be able to automatically solve 'Easy,' 'Medium,' and 'Hard' puzzles in Debian 10.  'Very Hard' puzzles cannot be solved automatically yet.

This is an educational project undertaken to:
* gain experience with Python programming
* gain experience with git
* explore python package creation and distribution
