''' MAKE SURE YOU DO PIP INSTALL NUMPY IN YOUR TERMINAL'''
import numpy as np


POSITION_ERROR = (-1, -1)
INITIAL_RED_GENERAL_POSITION = (9, 4)
INITIAL_BLACK_GENERAL_POSITION = (0, 4)
ROWS = 10
COLS = 9

# Class that has all functionalities of a single piece
class XiangqiPiece:

    def __init__(self, piece_type, player, x, y):
        self.__type = piece_type
        self.__player = player
        self.__x = x
        self.__y = y

    def __str__(self):
        return self.__type

    def get_type(self):
        return self.__type

    def get_player(self):
        return self.__player

    def move_to(self, x, y):
        self.__x = x
        self.__y = y

    def is_in_black_territory(self, x, y):
        return x <= 4 and x >= 0

    def is_in_red_territory(self, x, y):
        return x >= 5 and x <= 9

    def is_in_black_palace(self, x, y):
        return x <= 2 and x >= 0 and y >= 3 and y <= 5

    def is_in_red_palace(self, x, y):
        return x <= 9 and x >= 7 and y >= 3 and y <= 5

    def is_valid_move(self, x, y, board):
        if self.__type == 'Cha':
            return self.is_valid_move_cha(x, y) and not self.is_blocked_cha(x, y, board)

        elif self.__type == 'Hor':
            return self.is_valid_move_hor(x, y) and not self.is_blocked_hor(x, y, board)

        elif self.__type == 'Elp':
            return self.is_valid_move_elp(x, y) and not self.is_blocked_elp(x, y, board)

        elif self.__type == 'Adv':
            return self.is_valid_move_adv(x, y) and not self.is_blocked_adv(x, y, board)

        elif self.__type == 'Gen':
            return self.is_valid_move_gen(x, y) and not self.is_blocked_gen(x, y, board)

        elif self.__type == 'Can':
            return self.is_valid_move_can(x, y) and not self.is_blocked_can(x, y, board)

        elif self.__type == 'Sol':
            return self.is_valid_move_sol(x, y) and not self.is_blocked_sol(x, y, board)

        else:
            return False

    def is_valid_move_cha(self, x, y):
        return (abs(x - self.__x) > 0 and self.__y == y) or (abs(y - self.__y) > 0 and self.__x == x)

    def is_valid_move_hor(self, x, y):
        return (abs(x - self.__x) == 2 and abs(y - self.__y) == 1) or (
                    abs(x - self.__x) == 1 and abs(y - self.__y) == 2)

    def is_valid_move_elp(self, x, y):
        if self.__player == 'black':
            if self.is_in_red_territory(x, y):
                return False
            return abs(x - self.__x) == abs(y - self.__y)
        else:
            if self.is_in_black_territory(x, y):
                return False
            return abs(x - self.__x) == abs(y - self.__y)

    def is_valid_move_adv(self, x, y):
        if (self.__player == 'black'):
            if (not self.is_in_black_palace(x, y)):
                return False
            return abs(x - self.__x) == abs(y - self.__y) and abs(x - self.__x) == 1
        else:
            if (not self.is_in_red_palace(x, y)):
                return False
            return abs(x - self.__x) == abs(y - self.__y) and abs(x - self.__x) == 1

    def is_valid_move_gen(self, x, y):
        if (self.__player == 'black'):
            if (not self.is_in_black_palace(x, y)):
                return False
            return ((abs(y - self.__y) == 1 and self.__x == x) or (abs(x - self.__x) == 1 and self.__y == y))
        else:
            if (not self.is_in_red_palace(x, y)):
                return False
            return ((abs(y - self.__y) == 1 and self.__x == x) or (abs(x - self.__x) == 1 and self.__y == y))

    def is_valid_move_can(self, x, y):
        return (abs(x - self.__x) > 0 and self.__y == y) or (abs(y - self.__y) > 0 and self.__x == x)

    def is_valid_move_sol(self, x, y):
        if (self.__player == 'black'):
            if (self.is_in_red_territory(self.__x, self.__y)):
                return ((abs(y - self.__y) == 1 and self.__x == x) or (x - self.__x == 1 and self.__y == y))
            else:
                return (x - self.__x == 1 and self.__y == y)
        else:
            if (self.is_in_black_territory(self.__x, self.__y)):
                return ((abs(y - self.__y) == 1 and self.__x == x) or (x - self.__x == -1 and self.__y == y))
            else:
                return (x - self.__x == -1 and self.__y == y)
        return False

    def is_blocked_cha(self, x, y, board):
        move_posible = board[x][y] is None or board[x][y].get_player() != self.__player
        moves_horizontally = np.sign(x - self.__x) != 0
        if moves_horizontally:
            x_sign = np.sign(x - self.__x)
            acum = x_sign
            distance = abs(x - self.__x)
            for i in range(1, distance):
                if board[self.__x + acum][self.__y] is not None:
                    return True
                acum += x_sign
        else:
            y_sign = np.sign(y - self.__y)
            acum = y_sign
            distance = abs(y - self.__y)
            for i in range(1, distance):
                if board[self.__x][self.__y + acum] is not None:
                    return True
                acum += y_sign

        return not move_posible

    def is_blocked_hor(self, x, y, board):
        if y - self.__y == 2:
            move_posible = board[x][y] is None or board[x][y].get_player() != self.__player
            return board[self.__x][self.__y + 1] is not None or not move_posible
        if y - self.__y == -2:
            move_posible = board[x][y] is None or board[x][y].get_player() != self.__player
            return board[self.__x][self.__y - 1] is not None or not move_posible
        if x - self.__x == 2:
            move_posible = board[x][y] is None or board[x][y].get_player() != self.__player
            return board[self.__x + 1][self.__y] is not None or not move_posible
        if x - self.__x == -2:
            move_posible = board[x][y] is None or board[x][y].get_player() != self.__player
            return board[self.__x - 1][self.__y] is not None or not move_posible

    def is_blocked_elp(self, x, y, board):
        move_posible = board[x][y] is None or board[x][y].get_player() != self.__player
        x_sign = np.sign(x - self.__x)
        y_sign = np.sign(y - self.__y)
        acum_x = x_sign
        acum_y = y_sign
        distance = abs(x - self.__x)
        for i in range(1, distance):
            if board[self.__x + x_sign][self.__y + y_sign] is not None:
                return True
            acum_x += x_sign
            acum_y += y_sign
        return not move_posible

    def is_blocked_adv(self, x, y, board):
        if board[x][y] is None:
            return False
        return board[x][y].get_player() == self.__player

    def is_blocked_gen(self, x, y, board):
        if board[x][y] is None:
            return False
        return board[x][y].get_player() == self.__player

    def is_blocked_can(self, x, y, board):
        middle_pieces_acumulator = 0
        empty_target_location = board[x][y] is None
        moves_horizontally = np.sign(x - self.__x) != 0
        if moves_horizontally:
            x_sign = np.sign(x - self.__x)
            acum = x_sign
            distance = abs(x - self.__x)
            for i in range(1, distance):
                if board[self.__x + acum][self.__y] is not None:
                    middle_pieces_acumulator += 1
                acum += x_sign
        else:
            y_sign = np.sign(y - self.__y)
            acum = y_sign
            distance = abs(y - self.__y)
            for i in range(1, distance):
                if board[self.__x][self.__y + acum] is not None:
                    middle_pieces_acumulator += 1
                acum += y_sign

        if middle_pieces_acumulator == 0 and empty_target_location:
            return False

        if middle_pieces_acumulator != 1:
            return True

        if not empty_target_location:
            return not board[x][y].get_player() != self.__player
        return True

    def is_blocked_sol(self, x, y, board):
        if board[x][y] is None:
            return False
        return board[x][y].get_player() == self.__player


# Class that validates moves and checks.
class XiangqiCheckHelper:

    def __init__(self, board):
        self.__board = board
        self.__black_general_pos = (0, 4)
        self.__red_general_pos = (9, 4)
        self.__posible_moves_red = -1
        self.__posible_moves_black = -1
        self.__test_move_tmp = None

    def update(self, board, player, red_general_pos, black_general_pos):
        self.__board = board
        self.__red_general_pos = red_general_pos
        self.__black_general_pos = black_general_pos
        if player == 'red':
            self.__posible_moves_red = self._get_posible_moves('red')
        else:
            self.__posible_moves_black = self._get_posible_moves('black')

    def has_moves_left(self, player):
        if player == 'red':
            return self.__posible_moves_red > 0
        else:
            return self.__posible_moves_black > 0

    def is_stalemate(self, player):
        if player == 'red' and self.__posible_moves_red == 0:
            return not self._is_red_in_check()
        elif player == 'black' and self.__posible_moves_black == 0:
            return not self._is_black_in_check()
        else:
            return False

    def is_in_check(self, player):
        if player == 'red':
            return self._is_red_in_check()
        elif player == 'black':
            return self._is_black_in_check()
        return False

    def _is_red_in_check(self):
        for x in range(ROWS):
            for y in range(COLS):
                if self.__board[x][y] is not None:
                    (gen_x, gen_y) = self.__red_general_pos
                    if self.__board[x][y].get_player() == 'black' and \
                            self.__board[x][y].is_valid_move(gen_x, gen_y, self.__board):
                        return True
        return False

    def _is_black_in_check(self):
        for x in range(ROWS):
            for y in range(COLS):
                if self.__board[x][y] is not None:
                    (gen_x, gen_y) = self.__black_general_pos
                    if self.__board[x][y].get_player() == 'red' and \
                            self.__board[x][y].is_valid_move(gen_x, gen_y, self.__board):
                        return True
        return False

    def _get_posible_moves(self, player):
        posible_moves = 0
        for x in range(ROWS):
            for y in range(COLS):
                if self.__board[x][y] is not None and self.__board[x][y].get_player() == player:
                    for i in range(ROWS):
                        for j in range(COLS):
                            if self.__board[x][y].is_valid_move(i, j, self.__board) and \
                                    not self.general_left_in_check(x, y, i, j) and \
                                    not self.are_generals_seeing_eachother(x, y, i, j) and \
                                    not self.still_in_check(x, y, i, j):
                                posible_moves += 1
        return posible_moves

    def still_in_check(self, x1, y1, x2, y2):
        player = self.__board[x1, y1].get_player()
        if self.is_in_check(player):
            self._test_move(x1, y1, x2, y2)
            still_in_check = self.is_in_check(player)
            self._undo_test_move(x1, y1, x2, y2)
            return still_in_check
        return False

    def general_left_in_check(self, x1, y1, x2, y2):
        player = self.__board[x1, y1].get_player()
        self._test_move(x1, y1, x2, y2)
        ret = self.is_in_check(player)
        self._undo_test_move(x1, y1, x2, y2)
        return ret

    def are_generals_seeing_eachother(self, x1, y1, x2, y2):
        self._test_move(x1, y1, x2, y2)
        (red_gen_x, red_gen_y) = self.__red_general_pos
        (black_gen_x, black_gen_y) = self.__black_general_pos
        if red_gen_y != black_gen_y:
            self._undo_test_move(x1, y1, x2, y2)
            return False
        else:
            for i in range(black_gen_x + 1, red_gen_x - 1):
                if self.__board[black_gen_x + i][red_gen_y] is not None:
                    self._undo_test_move(x1, y1, x2, y2)
                    return False
        self._undo_test_move(x1, y1, x2, y2)
        return True

    def _test_move(self, x1, y1, x2, y2):
        if (self.__board[x1, y1].get_type() == 'Gen'):
            self._move_general(self.__board[x1, y1].get_player(), x2, y2)
        self.__test_move_tmp = self.__board[x2][y2]
        self.__board[x2, y2] = self.__board[x1, y1]
        self.__board[x1, y1] = None

    def _undo_test_move(self, x1, y1, x2, y2):
        self.__board[x1, y1] = self.__board[x2, y2]
        self.__board[x2, y2] = self.__test_move_tmp
        if (self.__board[x1, y1].get_type() == 'Gen'):
            self._move_general(self.__board[x1, y1].get_player(), x1, y1)

    def _move_general(self, player, x, y):
        if (player == 'black'):
            self.__black_general_pos = (x, y)
        else:
            self.__red_general_pos = (x, y)





# Main class for the game. Performs moves and does some validation.
class XiangqiGame:

    def __init__(self):
        self.__board = np.full([ROWS, COLS], None, dtype=object)
        self.__black_won = False
        self.__red_won = False
        self.__stalemate = False
        self.__black_general_pos = INITIAL_BLACK_GENERAL_POSITION
        self.__red_general_pos = INITIAL_RED_GENERAL_POSITION
        self.__current_player = 'red'
        self.__check_helper = XiangqiCheckHelper(self.__board)
        self._init_pieces()

    def _init_pieces(self):
        # Black
        self.__board[0, 0] = XiangqiPiece('Cha', 'black', 0, 0)
        self.__board[0, 1] = XiangqiPiece('Hor', 'black', 0, 1)
        self.__board[0, 2] = XiangqiPiece('Elp', 'black', 0, 2)
        self.__board[0, 3] = XiangqiPiece('Adv', 'black', 0, 3)
        self.__board[0, 4] = XiangqiPiece('Gen', 'black', 0, 4)
        self.__board[0, 5] = XiangqiPiece('Adv', 'black', 0, 5)
        self.__board[0, 6] = XiangqiPiece('Elp', 'black', 0, 6)
        self.__board[0, 7] = XiangqiPiece('Hor', 'black', 0, 7)
        self.__board[0, 8] = XiangqiPiece('Cha', 'black', 0, 8)

        self.__board[2, 1] = XiangqiPiece('Can', 'black', 2, 1)
        self.__board[2, 7] = XiangqiPiece('Can', 'black', 2, 7)

        self.__board[3, 0] = XiangqiPiece('Sol', 'black', 3, 0)
        self.__board[3, 2] = XiangqiPiece('Sol', 'black', 3, 2)
        self.__board[3, 4] = XiangqiPiece('Sol', 'black', 3, 4)
        self.__board[3, 6] = XiangqiPiece('Sol', 'black', 3, 6)
        self.__board[3, 8] = XiangqiPiece('Sol', 'black', 3, 8)

        # Red
        self.__board[9, 0] = XiangqiPiece('Cha', 'red', 9, 0)
        self.__board[9, 1] = XiangqiPiece('Hor', 'red', 9, 1)
        self.__board[9, 2] = XiangqiPiece('Elp', 'red', 9, 2)
        self.__board[9, 3] = XiangqiPiece('Adv', 'red', 9, 3)
        self.__board[9, 4] = XiangqiPiece('Gen', 'red', 9, 4)
        self.__board[9, 5] = XiangqiPiece('Adv', 'red', 9, 5)
        self.__board[9, 6] = XiangqiPiece('Elp', 'red', 9, 6)
        self.__board[9, 7] = XiangqiPiece('Hor', 'red', 9, 7)
        self.__board[9, 8] = XiangqiPiece('Cha', 'red', 9, 8)

        self.__board[7, 1] = XiangqiPiece('Can', 'red', 7, 1)
        self.__board[7, 7] = XiangqiPiece('Can', 'red', 7, 7)

        self.__board[6, 0] = XiangqiPiece('Sol', 'red', 6, 0)
        self.__board[6, 2] = XiangqiPiece('Sol', 'red', 6, 2)
        self.__board[6, 4] = XiangqiPiece('Sol', 'red', 6, 4)
        self.__board[6, 6] = XiangqiPiece('Sol', 'red', 6, 6)
        self.__board[6, 8] = XiangqiPiece('Sol', 'red', 6, 8)

    def make_move(self, pos1, pos2):
        (x1, y1) = self._algebraic_to_table_pos(pos1)
        (x2, y2) = self._algebraic_to_table_pos(pos2)

        if ((x1, y1) == POSITION_ERROR or (x2, y2) == POSITION_ERROR):
            print('Wrong algebraic position.')
            return False

        if self.__board[x1][y1] == None:
            print('The requested position is vacant.')
            return False

        if self.__red_won:
            print('Red already won. Unable to move.')
            return False

        elif self.__black_won:
            print('Black already won. Unable to move.')
            return False

        elif self.__stalemate:
            print('Stalemate. Unable to move.')
            return False

        else:
            if self._is_valid_move(x1, y1, x2, y2):
                self.__board[x1, y1].move_to(x2, y2)
                if (self.__board[x1, y1].get_type() == 'Gen'):
                    self._move_general(self.__board[x1, y1].get_player(), x2, y2)
                self.__board[x2, y2] = self.__board[x1, y1]
                self.__board[x1, y1] = None

                if self.__current_player == 'red':
                    self.__current_player = 'black'
                    self.__check_helper.update(self.__board, self.__current_player, self.__red_general_pos,
                                               self.__black_general_pos)
                    if not self.__check_helper.has_moves_left('black'):
                        if self.__check_helper.is_stalemate('black'):
                            print('Stalemate!')
                            self.__stalemate = True
                        else:
                            print('Red won!')
                            self.__red_won = True
                else:
                    self.__current_player = 'red'
                    self.__check_helper.update(self.__board, self.__current_player, self.__red_general_pos,
                                               self.__black_general_pos)
                    if not self.__check_helper.has_moves_left('red'):
                        if self.__check_helper.is_stalemate('red'):
                            print('Stalemate!')
                            self.__stalemate = True
                        else:
                            print('Black won!')
                            self.__black_won = True

                return True
            else:
                print('The requested movement is not legal')
                return False

    def _move_general(self, player, x, y):
        if (player == 'black'):
            self.__black_general_pos = (x, y)
        else:
            self.__red_general_pos = (x, y)

    def _is_valid_move(self, x1, y1, x2, y2):
        # First, check who should play
        if self.__board[x1][y1].get_player() != self.__current_player:
            print('Not your turn!')
            return False

        # Check if the piece can move in the desired way.
        if not self.__board[x1][y1].is_valid_move(x2, y2, self.__board):
            print('This piece cannot move like that.')
            return False

        # If already in check, the move should impede it.
        if self.__check_helper.still_in_check(x1, y1, x2, y2):
            print('Your general would still be in check')
            return False

        # Assert the general is not left in check
        if self.__check_helper.general_left_in_check(x1, y1, x2, y2):
            print('You would leave your general in check!')
            return False

        # Assert the generals are not seeing eachother
        if self.__check_helper.are_generals_seeing_eachother(x1, y1, x2, y2):
            print('Generals would be seeing each other!')
            return False

        return True

    def is_in_check(self, player):
        return self.__check_helper.is_in_check(player)

    def get_game_state(self):
        if self.__red_won:
            return 'RED_WON'

        elif self.__black_won:
            return 'BLACK_WON'

        return 'UNFINISHED'

    def restart(self):
        self.__board = np.full([ROWS, COLS], None, dtype=object)
        self.__black_won = False
        self.__red_won = False
        self.__stalemate = False
        self.__black_general_pos = INITIAL_BLACK_GENERAL_POSITION
        self.__red_general_pos = INITIAL_RED_GENERAL_POSITION
        self.__current_player = 'red'
        self.__check_helper = XiangqiCheckHelper(self.__board)
        self._init_pieces()

    def __str__(self):
        retStr = ''
        for x in range(ROWS):
            for y in range(COLS):
                if self.__board[x][y] is not None:
                    retStr += str(self.__board[x][y])
                else:
                    retStr += '   '
                retStr += ' '
            retStr += '\n'
        return retStr

    # Example: a1 = [9, 0]
    #		  b9 = [1, 1]
    def _algebraic_to_table_pos(self, algebraic):
        letter = algebraic[0]
        if (letter < 'a' or letter > 'i'):
            return POSITION_ERROR

        number = 0
        if (algebraic[-1] < '0' or algebraic[-1] > '9'):
            return POSITION_ERROR

        if (algebraic[-1] == '0'):
            # It's a 10
            number = 10
        else:
            number = int(algebraic[-1])

        x = 10 - number
        y = ord(letter) - 97
        return (x, y)

game = XiangqiGame()
print(game)

while True:
	fromIn = input()
	toIn = input()
	game.make_move(fromIn, toIn)
	print(game)