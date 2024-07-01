"""
File: matrixDisplay.py
Last Modified: 7/1/1014

Logic for outputting the location on the matrix display
"""

import RPi.GPIO as IO

class Matrix():
    def __init__(self):
        """
        Defines set up information for pin numbers
        """
        # Define all our output pins from the matrix display to the RPi
        IO.setup(12, IO.OUT)
        IO.setup(22, IO.OUT)
        IO.setup(27, IO.OUT)
        IO.setup(25, IO.OUT)
        IO.setup(17, IO.OUT)
        IO.setup(24, IO.OUT)
        IO.setup(23, IO.OUT)
        IO.setup(18, IO.OUT)
        IO.setup(21, IO.OUT)
        IO.setup(20, IO.OUT)
        IO.setup(26, IO.OUT)
        IO.setup(16, IO.OUT)
        IO.setup(19, IO.OUT)
        IO.setup(13, IO.OUT)
        IO.setup(6, IO.OUT)
        IO.setup(5, IO.OUT)

        # A row/colum matrix, where each index defines a row/column gpio pin
        self.col_mat = [12, 22, 27, 25, 17, 24, 23, 18]
        self.row_mat = [21, 20, 26, 16, 19, 13, 6, 5]


    def reset(self):
        """
        Unlight the matrix, and set all values to 0
        """
        for col in self.col_mat:
            IO.output(col, 0)
        for row in self.row_mat:
            IO.output(row, 0)

    
    def __row(self, r):
        """
        Light a given row of the matrix, from 0 to 7, where 0 is the "top" row (closest to pins 9-16)
        
        r - The row to light
        """
        if r >= len(self.row_mat) or r < 0:
            print("Error: Row size")
            return
        
        IO.output(self.row_mat[r], 1)
            
    
    def __col(self, c):
        """
        Unlight all the cells in a column except the specified one, where the cells are numbered from 0 to 7, with the "left" pin as 0 (closest to pins 1 and 16)
        
        c - The cell to light
        """
        if c >= len(self.col_mat) or c < 0:
            print("Error: Col size")
            return
        
        for i in range(len(self.col_mat)):
            if c != i:
                IO.output(self.col_mat[i], 1)
                
    
    def light(self, c, r):
        """
        Light the specified matrix location
        
        c - The column number to light
        r - The row number to light
        """
        self.reset()
        self.__row(r)
        self.__col(c)

    
    


