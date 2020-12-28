# Entry point

import SudokuGridModule

sudokuGrid = SudokuGridModule.SudokuGrid()
print(sudokuGrid.grid)

sudokuGrid.Write(3, 6, 2)
sudokuGrid.Print()