import random

class TicTacToe:
    def __init__(self):
        self.player_piece = ''
        self.computer_piece = ''
        self.piece_list = ["" for i in range(9)]
        self.user_move = 0
        self.computer_move = 0
        self.computer_in_row = 0
        self.player_in_row = 0
        self.play_again = True
        self.win_list =  [[0, 4, 8], [2, 4, 6],
           [0, 3, 6], [1, 4, 7], [2, 5, 8],
           [0, 1, 2], [3, 4, 5], [6, 7, 8]]
       #win list is the possible win combinatiosn in a 2D list^
       
      
        """
        moves is a dictionary with the keys as move position and a number as the corresponding board space
        """
      
        self.moves = {
            'top left':0, 'top middle':1, 'top right':2,
            'middle left':3, 'middle':4, 'middle right':5,
            'bottom left':6, 'bottom middle':7, 'bottom right':8
        }
        self.key_list = self.moves.keys()
        self.start_game()

  #draws board based on piece_list
  #thats why the piece list is important
    def draw_board(self):
      print(f'{self.piece_list[0]} | {self.piece_list[1]} | {self.piece_list[2]}\n'
          '========\n'
              f'{self.piece_list[3]} | {self.piece_list[4]} | {self.piece_list[5]}\n'
          '========\n'
              f'{self.piece_list[6]} | {self.piece_list[7]} | {self.piece_list[8]}\n')
    
    def what_piece_computer(self):
        if self.player_piece == 'x':
            self.computer_piece = 'o'
            return
       
        self.computer_piece = 'x'

    """
    user_pice_type lets the user choose between x's or o's
    uses while loop to make sure user input is valid
    """
    def user_piece_type(self):
        self.player_piece = input("Would you like to be X's or O's: ")
        while True:
            if self.player_piece.lower() == "x" or self.player_piece.lower() == "o":
                return self.player_piece.lower()
            print("Please input valid answer!")
            self.player_piece = input("Would you like to be X's or O's: ")

        """
        uses two funcs to assign the user piece what they want
        then the what_piece_computer func assigns the comput the opposite piece as the user
        """
    def assign_pieces(self):
        self.player_piece = self.user_piece_type()
        self.what_piece_computer()

#reset_game resets the piece_list 
    def reset_game(self):
        for i in range(9):
            self.piece_list[i] = ""

    """
                game_going checks if the game has been won and if the board is full
                """
    def game_going(self):
      if self.check_if_won(self.player_piece):
        return False
      elif self.check_if_won(self.computer_piece):
        return False
      elif "" in self.piece_list:
         return True
              
      return False

  
    def is_valid(self, user_input):
        if not user_input in self.key_list:
          return False
          
        elif self.piece_list[self.moves[user_input]] == self.computer_piece:
          return False
          
        return True
            

    def ask_move(self):
      user_input = input("Pick a move: ")
      
      while not self.is_valid(user_input):
        
        print("enter valid move!")
        user_input = input("Pick a valid move: ")
      self.user_move = self.moves[user_input]

    #asks player if they wish to play again
    def ask_play_again(self):
        user_input = input("would you like to play again y/n: ")
        if user_input == "n":
          print("YOU ARE PLAYING AGAIN\n")
          self.play_again = True
        elif user_input == "STUD":
          print("iight G")
          self.play_again = False

  #this func loops through win list and checks if player has won
  # needs to work with computer moves as well
    
    def check_if_won(self, player_piece): 
      for win_combo in self.win_list:
        count = 0
        for slot in win_combo:
          if player_piece in self.piece_list[slot]:
             count += 1 
          if count == 3:
            return True
            
        """
      this func sets the computer piece and makes sure it is on an empyt slot
      """
    def computer_pick_move(self): 
      self.computer_move = random.randint(0, 8)
      #while self.game_going(): 
      while self.piece_list[self.computer_move] == self.player_piece: 
          self.computer_move = random.randint(0, 8) 
          
      self.piece_list[self.computer_move] = self.computer_piece
  
    def start_game(self):
        print("Valid moves are: ")
        for move in self.key_list:
          print("-" + move)

        while self.play_again:
          self.reset_game()
          self.assign_pieces()
          self.draw_board()
          
        #^above code initializes game
        #below code is the game loop
          
          while self.game_going():  
              self.ask_move()
              self.piece_list[self.user_move] = self.player_piece
            
              self.computer_pick_move()
              self.draw_board()

          if self.check_if_won(self.player_piece):
            print('congrats you won\n')
            self.ask_play_again()
            
          elif self.check_if_won(self.computer_piece):
            print("You lost\n")
            
          
if __name__ == '__main__':
  TicTacToe()