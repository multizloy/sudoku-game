import random
import math
import copy

class Sudoku:
    def __init__(self, N, E):
        self.N = N
        self.E = E
        # compute square root of N
        self.SRN = int(math.sqrt(N))
        self.table = [[0 for x in range(N)] for y in range(N)]
        self.answerable_table = None
        self._generate_table()

    def _generate_table(self):
        # fill the subgroups diagonally table/matrices
        """
        Generate a Sudoku table with N cells, with E empty cells.

        The table is filled in two steps:

        1. The subgroups are filled diagonally.
        2. The remaining empty cells are filled in a random manner.

        The table is then modified to remove E random digits, leaving the
        resulting Sudoku puzzle.
        """
        self.fill_diagonal()
        # fill remaining empty subgroups
        self.fill_remaining(0, self.SRN)
        # Remove random Key digits to make game
        self.remove_digits()
        
    def fill_diagonal(self):
        """
        Fill the diagonal subgroups of the table.

        :return: None
        """
        for x in range(0, self.N, self.SRN):
            self.fill_cell(x, x)
    
    def not_in_subgroup(self, rowstart, colstart, num):
        """
        Check if a number already exists in a subgroup.

        :param rowstart: The top-left row of the subgroup
        :param colstart: The top-left column of the subgroup
        :param num: The number to check for
        :return: True if not in subgroup, False if it is
        """
        for x in range(self.SRN):
            for y in range(self.SRN):
                if self.table[rowstart + x][colstart + y] == num:
                    return False
        return True
    
    def fill_cell(self, row, col):
        
        """
        Fill a subgroup with a random number that is not already in the subgroup.
        
        :param row: The top-left row of the subgroup
        :param col: The top-left column of the subgroup
        :return: None
        """
        num = 0
        for x in range(self.SRN):
            for y in range(self.SRN):
                while True:
                    num = self.random_generator(self.N)
                    if self.not_in_subgroup(row, col, num):
                        break
                self.table[row + x][col + y] = num
    def random_generator(self, num):
        """
        Return a random integer between 1 and num (inclusive).
        
        :param num: The maximum number
        :return: A random integer
        """
        return math.floor(random.random() * num + 1)

    def safe_position(self, row, col, num):
        
        """
        Check if a given number is safe to place in a given row and column.
        
        :param row: The row to check
        :param col: The column to check
        :param num: The number to check
        :return: True if the number is safe to place, False otherwise
        """
        return (self.not_in_row(row, num) and self.not_in_col(col, num) and self.not_in_subgroup(row - row % self.SRN, col - col % self.SRN, num))
    
    def not_in_row(self, row, num):
        """
        Check if a given number already exists in a given row.
        
        :param row: The row to check
        :param num: The number to check
        :return: True if not in row, False if it is
        """
        for col in range(self.N):
            if self.table[row][col] == num:
                return False
        return True
    
    def not_in_col(self, col, num):
        """
        Check if a given number already exists in a given column.
        
        :param col: The column to check
        :param num: The number to check
        :return: True if not in column, False if it is
        """
        for row in range(self.N):
            if self.table[row][col] == num:
                return False
        return True
    
    def fill_remaining(self, row, col):
        # check if we have reached the end of the matrix
        """
        Recursively fill the Sudoku table with a valid value in each cell.
        
        :param row: The current row
        :param col: The current column
        :return: True if the table is fully filled, False otherwise
        """
        if row == self.N - 1 and col == self.N:
            return True
        # move to the next row if we have reached the end of the current row
        if col == self.N:
            row += 1
            col = 0
        # skip cells that are already filled
        if self.table[row][col] != 0:
            return self.fill_remaining(row, col + 1)
        # try filling the current cell with a valid value
        for num in range(1, self.N + 1):
            if self.safe_position(row, col, num):
                self.table[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.table[row][col] = 0
        # no valid value was found, so backtrack
        return False
    
    def remove_digits(self):
        """
        Removes a certain amount of numbers from the Sudoku table to create a puzzle
        sheet. The numbers are chosen randomly, and the table is modified in-place.
        
        :return: None
        """
        count = self.E
        # replicates the table so we can have a filled and pre-filled copy
        self.answerable_table = copy.deepcopy(self.table)
        # removing random numbers to create the puzzle sheet
        while (count != 0):
            row = self.random_generator(self.N) - 1
            col = self.random_generator(self.N) - 1
            if (self.answerable_table[row][col] != 0):
                count -= 1
                self.answerable_table[row][col] = 0
                
    def puzzle_table(self):
        """
        Returns the puzzle table, which is a copy of the original table but with some numbers removed.
        
        :return: The puzzle table
        """
        return self.answerable_table

    def puzzle_answers(self):
        """
        Returns the answer table, which is a copy of the original table with all the numbers filled in.
        
        :return: The answer table
        """
        return self.table

    def print_sudoku(self):
        """
        Prints the Sudoku table and the puzzle table to the console.

        The first table is the answer table, with all the numbers filled in.
        The second table is the puzzle table, which is a copy of the original table
        but with some numbers removed.
        """
        for row in range(self.N):
            for col in range(self.N):
                print(self.table[row][col], end=" ")
            print()
        print("")
        for row in range(self.N):
            for col in range(self.N):
                print(self.answerable_table[row][col], end=" ")
            print()

if __name__ == "__main__":
    N = 9
    E = (N * N) // 2
    sudoku = Sudoku(N, E)
    sudoku.print_sudoku()