from random import choice
from os import system
system('pip install english-words')
from english_words import english_words_lower_alpha_set

class Wordle:
    def __init__(self):
      self.word_list = list(english_words_lower_alpha_set)
      self.word = choice(self.word_list)
      #ensures word is only 5 letters
      while len(self.word) != 5:
        self.word = choice(self.word_list)
      self.word_split = list(self.word)
      self.guessed_word = ""
      self.num_guesses = -1
      self.guess_dict = {
        0: ["" for i in range(5)],
        1: ["" for i in range(5)],
        2: ["" for i in range(5)],
        3: ["" for i in range(5)],
        4: ["" for i in range(5)],
        5: ["" for i in range(5)]
      }
      
      while self.guessed_word != self.word:
        self.draw_board()
        self.update_guess_list()
        if self.guessed_word == self.word:
          self.draw_board()
          print(f"you won, the word was {self.word}")
        elif self.num_guesses >= 6:
          print(f"you lost, the word was {self.word}")
          break
    

    def get_user_guess(self):
      """gets user guess and sets it to guessed word"""
      user_guess = input("enter 5 letter word: ")
      while len(user_guess) != 5:
        #now if word is not 5 letters or word is not in word list then computer prompts enter again
        user_guess = input("Not valid, enter 5 letter word: ")
        
      self.guessed_word = user_guess.lower()
      self.num_guesses += 1

    def draw_board(self):
      """dg stands for dictionary guess --> I was lazy
      this func will draw the board based on the guess dictionary """
      dg = self.guess_dict
      for i in range(6):
        print(f'{dg[i][0]} | {dg[i][1]} | {dg[i][2]} | {dg[i][3]} | {dg[i][4]}')
        print('===============')

    def update_guess_list(self):
      """gets user guess then updates the current list in the dictionary based on the number of guesses"""
      self.get_user_guess()
      guess_split = list(self.guessed_word)
      for index in range(len(guess_split)):
        letter = guess_split[index]
        if guess_split[index] in self.word_split:
         if guess_split[index] == self.word_split[index]:
           letter = f"\33[92m{letter}\033[m"#green
         else: 
           letter = f"\33[93m{letter}\033[m"#yellow
        self.guess_dict[self.num_guesses][index] = letter
        
      
if __name__ == "__main__":
  Wordle()

#underline/colors in console!!!

# print("\33[93mhello\033[m") #yellow : right letter wrong spot 
# print("\33[92mhello\033[m") #green : right spot and right letter


   
    
    
  

  