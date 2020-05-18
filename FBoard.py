# Author: Quazi Safin
# Date: 12/05/2019
# Description: A functional game where two players compete, and one tries to move their piece to the finish
# while the other player tries to block their progress.

class FBoard:
    _board = [[],
              [],
              [],
              [],
              [],
              [],
              [],
              []]
    _gameState = None
    _xposition = (None, None)

    def __init__(self):
        '''A Function that initializes the game, a constructor '''
        #Initializes board with E for empty
        for x in range(8):
            for y in range(8):
                self._board[x].append('E')


        #Puts 'O' on row 7, columns 0, 2, 4, 6
        self._board[7][0] = 'O'
        self._board[7][2] = 'O'
        self._board[7][4] = 'O'
        self._board[7][6] = 'O'

        #Puts 'X' on row 0, column 3
        self._board[0][3] = 'X'

        #Initializes the other members
        self._xposition = (0, 3)
        self._gameState = "UNFINISHED"


    def printboard(self):
        print("============== BOARD ===============")
        for x in range(8):
            print(self._board[x])

    ''' A function that returns the value of gamestate '''
    def get_game_state(self):
        return self._gameState

    ''' A function that sets the new position of X'''
    def move_x(self, row, column):

        if row > 7 or row < 0:
            return False

        if column > 7 or column < 0:
            return False

        possiblemoves = []

        #checks game state and returns false is game is over
        if self._gameState == "O_WON" or self._gameState == "X_WON":
            return False
        #checks if the move requested is the same as the current position returns false if so
        if self._xposition[0] == row and self._xposition[1] == column:
            return False




         #checks possible moves from current positions and append to array via tuple format
        if (0 <= self._xposition[0] - 1 <= 7) and (0 <= self._xposition[1] - 1 <= 7) and  (self._board[self._xposition[0] - 1][self._xposition[1] -1] == 'E'):
            possiblemoves.append((self._xposition[0] - 1, self._xposition[1] - 1))


        if (0 <= self._xposition[0] - 1 <= 7) and (0 <= self._xposition[1] + 1 <=7) and (self._board[self._xposition[0] - 1][self._xposition[1] + 1]) == 'E':
            possiblemoves.append((self._xposition[0] - 1, self._xposition[1] + 1))


        if (0 <= self._xposition[0] + 1 <= 7) and (0 <= self._xposition[1] - 1 <= 7) and (self._board[self._xposition[0] + 1][self._xposition[1] - 1] == 'E'):
            possiblemoves.append((self._xposition[0] + 1, self._xposition[1] - 1))


        if (0 <= self._xposition[0] + 1 <= 7) and (0 <= self._xposition[1] + 1 <= 7) and (self._board[self._xposition[0] + 1][self._xposition[1] + 1]) == 'E':
            possiblemoves.append((self._xposition[0] + 1, self._xposition[1] + 1))




        for x in possiblemoves:
            if x[0] == row and x[1] == column:
                self._board[self._xposition[0]][self._xposition[1]] = 'E'
                self._board[row][column] = 'X'
                self._xposition = (row,column)
                if self._xposition[0] == 7:
                    self._gameState = "X_WON"
                return True

        return False

    ''' A funcion that sets the new position of X'''

    def force(self, row, column, character):
        self._board[row][column] = character

    def check_legal(self, row, column):
        possiblemoves = []
        # checks possible moves from current positions and append to array via tuple format
        if self._board[row - 1][column - 1] == 'E':
            possiblemoves.append((row - 1, column - 1))

        if self._board[row - 1][column + 1] == 'E':
            possiblemoves.append((row - 1, column + 1))

        if self._board[row + 1][column - 1] == 'E':
            possiblemoves.append((row - 1, column - 1))

        if self._board[row + 1][column + 1] == 'E':
            possiblemoves.append((row + 1, column + 1))

        if len(possiblemoves) == 0:
            return False

    def move_o(self, row, column, newrow, newcolumn):

        if newrow > 7 or newrow < 0:
            return False

        if newcolumn > 7 or newcolumn < 0:
            return False

        if self._board[row][column] != 'O':
            return False

        if self._board[newrow][newcolumn] != 'E':
            return False


        # checks game state and returns false is game is over
        if self._gameState == "O_WON" or self._gameState == "X_WON":
            return False

        #if the move to make is = to 1 row less and the column is 1 less or 1 greater, then it is valid
        if newrow == (row - 1) and ((newcolumn == column - 1) or (newcolumn == column + 1)):
            self._board[newrow][newcolumn] = 'O'
            self._board[row][column] = 'E'
            if self.check_legal(self._xposition[0], self._xposition[1]) == False:
                self._gameState = "O_WON"
            return True


        return False
