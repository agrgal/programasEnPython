# Juego de las tres en raya

# Datos clave: el tablero, los jugadores implicados, y el estado del juego: quien va, si se ha ganado, etc.
# Los movimientos hechos por los jugadores, los contadores usados.

"""
• Game the class that will hold the board, players and the core game playing logic,
• Board this is a class that represents the current state of the TicTacToe board or
grid within the game,
• Human Player this class represents the human player involved in the game,
• Computer Player this class represents the computer playing the game,
• Move this class represents a particular move made by a player,
• Counter which can be used to represent the counters to play with; this will be
either X or Y.
"""
from abc import ABCMeta, abstractmethod  # para crear clases abstractas (Player)
import random


class Counter:
    """Clase ficha: representa una ficha que se usa en el tablero """

    def __init__(self, label):
        self.label = label

    def __str__(self):
        return self.label


class Move:
    """ Represents a move made by a player """

    def __init__(self, counter, x, y):
        self.x = x
        self.y = y
        self.counter = counter


class Player(metaclass=ABCMeta):
    """ Abstract class representing a Player and their counter """

    def __init__(self, board):
        self.board = board
        self._counter = None

    @property
    def counter(self):
        """Representa la ficha de un jugador, que puede ser una X o una O"""
        return self._counter

    @counter.setter
    def counter(self, valor):
        self._counter = valor

    @abstractmethod
    def get_move(self): pass

    def __str__(self):
        return self.__class__.__name__ + '[' + str(self.counter) + ']'


class HumanPlayer(Player):
    """ Represents a Human Player and their behaviour """

    def __init__(self, board):
        super().__init__(board)

    @staticmethod
    def _get_user_input(prompt):
        invalid_input = True
        user_input_int = 0
        while invalid_input:
            print(prompt)
            user_input = input()
            if not user_input.isdigit():
                print('Input must be a number')
            else:
                user_input_int = int(user_input)
                if user_input_int < 1 or user_input_int > 3:
                    print('input must be a number in the range 1 to 3')
                else:
                    invalid_input = False
        return user_input_int - 1

    def get_move(self):
        """ Allow the human player to enter their move """
        row = self._get_user_input("Por favor, mete la fila: ")
        column = self._get_user_input("Por favor, mete la columna: ")
        while True:
            if self.board.is_empty_cell():
                Move(self.counter, row, column)
            else:
                print('That position is not free')
                print('Please try again')


class ComputerPlayer(Player):
    """ Implements algorithms for playing game """

    def __init__(self, board):
        super().__init__(board)

    def randomly_select_cell(self):
        """ Use a simplistic random selection approach to find a cell to fill. """
        while True:
            # Randomly select the cell
            row = random.randint(0, 2)
            column = random.randint(0, 2)
            # Check to see if the cell is empty
            if self.board.is_empty_cell(row, column):
                return Move(self.counter, row, column)

    def get_move(self):
        """ Provide a very simple algorithm for selecting a move"""
        if self.board.is_empty_cell(1, 1):
            # Choose the center
            return Move(self.counter, 1, 1)
        elif self.board.is_empty_cell(0, 0):
            # Choose the top left
            return Move(self.counter, 0, 0)
        elif self.board.is_empty_cell(2, 2):
            # Choose the bottom right
            return Move(self.counter, 2, 2)
        elif self.board.is_empty_cell(0, 2):
            # Choose the top right
            return Move(self.counter, 0, 2)
        elif self.board.is_empty_cell(2, 0):
            # Choose the bottom right
            return Move(self.counter, 2, 0)
        else:
            return self.randomly_select_cell()


class Board:
    """ The ticTacToe board"""

    def __init__(self):
        # Set up the 3 by 3 grid of cells
        self.cells = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.separator = '\n' + ('-' * 11) + '\n'

    def __str__(self):
        """ Imprime el tablero  """
        row1 = ' ' + str(self.cells[0][0]) + ' | ' + str(self.cells[0][1]) + ' | ' + str(self.cells[0][2])
        row2 = ' ' + str(self.cells[1][0]) + ' | ' + str(self.cells[1][1]) + ' | ' + str(self.cells[1][2])
        row3 = ' ' + str(self.cells[2][0]) + ' | ' + str(self.cells[2][1]) + ' | ' + str(self.cells[2][2])
        return row1 + self.separator + row2 + self.separator + row3

    def add_move(self, move):
        """ A move to the board """
        row = self.cells[move.x]  # Selecciona una de las listas
        row[move.y] = move.counter  # Dentro de esa lista, pone una ficha

    def is_empty_cell(self, row, column):
        """ Comprueba si una celda esta vacía o no """
        return self.cells[row][column] == ''

    def cell_contains(self, ficha, row, column):
        """ Comprueba si en una celda determinada, hay una ficha determinada """
        return self.cells[row][column] == ficha

    def is_full(self):
        """ Comprueba si el tablero está lleno """
        for row in range(0, 3):
            for column in range(0, 3):
                if self.is_empty_cell(row, column):
                    return False
        return True

    def check_for_winner(self, player):
        """ Comprueba si un jugador ha ganado o no  """
        c = player.counter
        return (  # across the top
                (self.cell_contains(c, 0, 0) and self.cell_contains(c, 0, 1) and self.cell_contains(c, 0, 2)) or
                # across the middle
                (self.cell_contains(c, 1, 0) and self.cell_contains(c, 1, 1) and self.cell_contains(c, 1, 2)) or
                # across the bottom
                (self.cell_contains(c, 2, 0) and self.cell_contains(c, 2, 1) and self.cell_contains(c, 2, 2)) or
                # down the left side
                (self.cell_contains(c, 0, 0) and self.cell_contains(c, 1, 0) and self.cell_contains(c, 2, 0)) or
                # down the middle
                (self.cell_contains(c, 0, 1) and self.cell_contains(c, 1, 1) and self.cell_contains(c, 2, 1)) or
                # down the right side
                (self.cell_contains(c, 0, 2) and self.cell_contains(c, 1, 2) and self.cell_contains(c, 2, 2)) or
                # diagonal
                (self.cell_contains(c, 0, 0) and self.cell_contains(c, 1, 1) and self.cell_contains(c, 2, 2)) or
                # other diagonal
                (self.cell_contains(c, 0, 2) and self.cell_contains(c, 1, 1) and self.cell_contains(c, 2, 0))
        )  # fin del return


class Game:
    """ Contiene la lógica del juego """

    def __init__(self):
        self.board = Board()  # inicializa un tablero
        self.human = HumanPlayer(self.board)  # inicializa un humano
        self.computer = ComputerPlayer(self.board)  # inicializa la computadora
        self.next_player = None
        self.winner = None

    def select_player_counter(self):
        """ Que el jugador seleccione su ficha """
        counter = ''
        while not (counter == 'X' or counter == 'O'):
            print('¿Quieres ser X o O?')
            counter = input().upper()
            if counter != 'X' and counter != 'O':
                print('Debe ser X o O')
            if counter == 'X':
                self.human.counter = X
                self.computer.counter = O
            else:
                self.human.counter = O
                self.computer.counter = X

    def select_player_to_go_first(self):
        """ Selecciona aleatoriamente quién va primero, el humano o el ordenador."""
        if random.randint(0, 1) == 0:
            self.next_player = self.human
        else:
            self.next_player = self.computer


# ==================
# programa principal
# ==================

X = Counter("X")  # Constante que representa la clase X
O = Counter("O")  # Constante que representa la clase O
