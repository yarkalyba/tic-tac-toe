import copy


class Board:
    '''Class to represent the board'''
    CROSS = '✗'
    ZERO = 'o'

    def __init__(self):
        self.board = 3 * [[None, None, None],
                          [None, None, None],
                          [None, None, None]]
        self.last_position = None
        self.last_symbol = None
        self.have_winner = False
        self.draw = False
        self.play = True

    def winner(self):
        '''Method to check if where is a winner'''
        for row in range(3):
            set_rows = set()
            set_cols = set()
            for col in range(3):
                set_cols.add(self.board[col][row])
                set_rows.add(self.board[row][col])
            if len(set_rows) == 1 and set_rows.pop() != None:
                # checks rows
                self.have_winner = True
                self.play = False
                return self.board[row][0]

            if len(set_cols) == 1 and set_cols.pop() != None:
                # checks columns
                self.have_winner = True
                self.play = False
                return self.board[0][row]

        set_diagonal = set()
        set_diagonal1 = set()
        # checks diagonals
        for i in range(3):
            set_diagonal.add(self.board[i][i])
            set_diagonal1.add(self.board[2 - i][i])
        if len(set_diagonal) == 1 and set_diagonal.pop() != None:
            self.have_winner = True
            self.play = False
            return self.board[1][1]
        if len(set_diagonal1) == 1 and set_diagonal1.pop() != None:
            self.have_winner = True
            self.play = False
            return self.board[1][1]

    def check_status(self):
        '''Method to check if the is a winner or we have to play'''
        self.winner()
        nones = 0
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == None:
                    nones += 1
        if nones == 0 and self.have_winner == False:
            self.draw = True
            self.play = False
        if self.have_winner:
            self.play = False

        if nones != 0 and self.have_winner == False:
            self.play = True

    def is_free(self, row, col):
        """
        Method to check if the position is free
        :param row: index of row
        :param col: index of column
        :return: True if free
        """
        return self.board[row][col] == None

    def fill(self, index, value):
        """
        Method to fill the position with value
        :param index: tuple of indexes
        :param value: symbol of player
        :return: board with new symbol
        """
        row = index[0]
        col = index[1]
        if self.board[row][col] is None:
            new_board = copy.deepcopy(self)
            new_board.board[row][col] = value
            return new_board
        else:
            print("You can't choose this position(ಠ_ಠ)")

    def free(self):
        """
        Method to make list of free positions
        :param row: index of row
        :param col: index of column
        :return: list of free positions
        """
        lst_free = []
        for row in range(3):
            for col in range(3):
                if self.is_free(row, col):
                    lst_free.append((row, col))
        return lst_free

    def make_children(self, symbol):
        """
        Method to return list of children with one more symbol
        :param symbol: symbol pf player
        :return: list of children
        """
        lst = self.free()
        children = []
        for i in lst:
            child = self.fill(i, symbol)
            children.append(child)
        return children

    def user_move(self, symbol):
        """Method to add user's move to the board"""
        positions = {'1': (0, 0), '2': (0, 1), '3': (0, 2), '4': (1, 0),
                     '5': (1, 1), '6': (1, 2), '7': (2, 0), '8': (2, 1),
                     '9': (2, 2)}
        Board.print_positions()
        print(self)
        while True:
            user_choice = input('Your choice: ')
            if user_choice in positions.keys():
                break
            else:
                print('You should enter number of the position!')
        board = self.fill(positions[user_choice], symbol)
        return board

    @staticmethod
    def print_positions():
        print('Available positions:\n 1 2 3\n 4 5 6\n 7 8 9')

    def __str__(self):
        str = ''
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == None:
                    str += ' ⬜'
                elif self.board[row][col] == Board.CROSS:
                    str += ' ✗'
                else:
                    str += ' o'
            str += '\n'
        return str
