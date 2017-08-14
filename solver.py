# A Sudoku solver. Probably not a great one.


class Square:
    def __init__(self, value):
        self.value = value             # single character, _ if empty
        self.original = False          # bool denoting if square is part of starting map
        self.solved = False            # bool denoting if square has been solved
        self.possible = [True] * 9     # if self.possible[i] == true, then i+1 is a possible value. All false if solved
        self.possible_count = 9        # Represents how many Trues in possible
        if self.value != '_':
            self.solved = True
            self.original = True
            for i in range(0, 9):
                if i != int(self.value) - 1:
                    self.possible[i] = False
                    self.possible_count = 1


class Board:
    def __init__(self):
        self.squares = {}      # map of squares such that squares[(i, j)] will contain the Square for location (i, j)
        self.unsolved = set()  # set which contains all locations that still aren't solved for
        for i in range(0, 9):
            for j in range(0, 9):
                self.unsolved.add((i, j))

    def read_in(self):
        f = open('test.txt', 'r')
        for i in range(0, 9):
            for j in range(0, 9):
                value = f.read(1)
                self.squares[(i, j)] = Square(value)
                self.unsolved.remove((i, j))
            f.read(1)  # Deals with newline

    # Returns a copy of the calling board
    def copy(self):
        copy = Board()
        for square in self.squares:
            copy.squares[square] = Square(self.squares[square].value)
        for square in self.unsolved:
            copy.unsolved.add(square)
        return copy

    def to_string(self):
        string = ''
        for i in range(0, 3):
            for I in range(0, 3):
                for j in range(0, 3):
                    for J in range(0, 3):
                        string += self.squares[(3*i+I, 3*j+J)].value
                    string += '  '
                string += '\n'
            string += '\n'
        return string


# Before: Find all squares with only one possible solution and update them
# After: All squares in the same sector, row, or column as the passed in value get their possible and possible_count
def update_effected_squares(board, value, i, j):
    # def same_square(i, j):
    #     for x in range((i//3)*3, (i//3)*3+3):
    #             for y in range((j//3)*3, (j//3)*3+3):
    #                     print('(' + str(x) + ', ' + str(y) + ')')
    effected_coords = set()
    for x in range(0, 9):
        effected_coords.add((i, x))
        effected_coords.add((x, j))
    for x in range((i//3)*3, (i//3)*3+3):
        for y in range((j//3)*3, (j//3)*3+3):
            effected_coords.add((x, y))
    for coord in effected_coords:
        if board.squares[coord].possible[value-1]:  # if the square located at coord has value as possible
            board.squares[coord].possible[value-1] = False
            board.squares[coord].possible_count -= 1
            if board.squares[coord].possible_count == 1:
                board.squares[coord].value = board.squares.possible.index(True) + 1
                board.squares[coord].possible[board.squares[coord].value - 1] = False
                board.squares[coord].possible_count = 0
                update_effected_squares(board, board.squares[coord].value, coord[0], coord[1])


def solver(board):
    print 'yo'


def main():
    board = Board()
    board.read_in()
    print(board.to_string())


if __name__ == '__main__':
    main()
