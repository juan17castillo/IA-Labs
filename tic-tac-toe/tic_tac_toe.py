import re

from random import randint

_PLAYER = "player"
_MACHINE = "machine"

_PLAYER_SYMBOL = "x"
_MACHINE_SYMBOL = "o"

class TicTacToeGame():
  def __init__(self):
    self.board = [None] * 9
    self.turn = _PLAYER
    self.is_game_over = False
    self.winner = None

  def is_over(self): # TODO: Finish this function by adding checks for a winning game (rows, columns, diagonals)
    counter = self.board.count(None) == 0
    if(counter):
      self.winner = None
      self.is_game_over = True
      return False
    else:
      cell = self.board
      if(cell[0] == cell[4] == cell[8] and cell[0] is not None):
        self.is_game_over = True
        if(cell[0] == _PLAYER_SYMBOL):
          self.winner = _PLAYER
        else:
          self.winner = _MACHINE

        return False
        #evaluate diagonal from right to left
      if(cell[2] == cell[4] == cell[6] and cell[2] is not None):
        self.is_game_over = True
        #evaluate which player is the diagonal by a ramdom cell of the diagonal
        if(cell[4] == _PLAYER_SYMBOL):
          self.winner = _PLAYER
        else:
          self.winner = _MACHINE
        
        return False
      playerSc = 0
      machineSc = 0

      #range to end the game in favor of the player or the machine depending on the case
      for i in range(9):
        if(playerSc==3):
          self.is_game_over = True
          self.winner = _PLAYER
          
          return False
        elif(machineSc == 3):
          self.is_game_over = True
          self.winner = _MACHINE
          return False

        if(i%3==0):
          playerSc, machineSc = 0, 0
        
        if(cell[i] is not None):
          if(cell[i] == _PLAYER_SYMBOL):
            playerSc+=1
          else:
            machineSc+=1

        if(i<3 and cell[i] == cell[i+3] == cell[i+6] and cell[i] is not None):
          self.is_game_over = True
          if(cell[i] == _PLAYER_SYMBOL):
            self.winner = _PLAYER
            return False
          
          else:
            self.winner = _MACHINE
            return False

            #There is a problem when both diagonals are performed

    return True

  def play(self):
    if self.turn == _PLAYER:
      self.player_turn()
      self.turn = _MACHINE
    else:
      self.machine_turn()
      self.turn = _PLAYER

  def player_choose_cell(self):
    print("Input empty cell bewtween 0 and 8")

    player_cell = input().strip()
    match = re.search("\d", player_cell)

    if not match:
      print("Input is not a number, please try again")

      return self.player_choose_cell()

    player_cell = int(player_cell)

    if not -1 < player_cell < 9:
      print("Index out of limits")

      return self.player_choose_cell()

    if self.board[player_cell] is not None:
      print("Cell is already taken, try again")

      return self.player_choose_cell()


    return player_cell

  def player_turn(self):
    chosen_cell = self.player_choose_cell()

    self.board[chosen_cell] = _PLAYER_SYMBOL

  def machine_turn(self): # TODO: Finish this function by making the machine choose a random cell (use random module)
    position = randint(0,8)
    #Takes a random position while it is not occupied
    while(self.board[position] is not None):
        position = randint(0,8)
    self.board[position] = _MACHINE_SYMBOL

  def format_board(self):
    row0 = "|".join(list(map(lambda c: " " if c is None else c, self.board[0:3])))
    row1 = "|".join(list(map(lambda c: " " if c is None else c, self.board[3:6])))
    row2 = "|".join(list(map(lambda c: " " if c is None else c, self.board[6:9])))

    return "\n".join([row0, row1, row2])

  def print(self):
    print("Player turn:" if self.turn == _MACHINE else "Machine turn:")
    print(self.format_board())
    print()

  def print_result(self): # TODO: Finish this function in order to print the result based on the *winner*
    print("The winner is: {0}!".format(self.winner) if self.winner is not None else "It's a Draw!")
