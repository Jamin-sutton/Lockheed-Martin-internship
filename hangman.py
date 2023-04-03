from random import choice
from os import system
system('pip install english-words')

from english_words import english_words_lower_alpha_set

#for showing word--> replace_str_index 
def replace_str_index(index,text,replacement):
    return (f'{text[:index]}{replacement}{text[index+1:]}')

class HangMan:
  def __init__(self):
    self.words = list(english_words_lower_alpha_set)
    
    self.word = choice(self.words)
    self.guessed = []
    self.correct_guesses = []
    self.word_list = list(self.word)
    self.bad_guesses = 1
    self.current_guessed_word = ("_"*len(self.word))
    self.screen_animations = {
        1: """
        /---|
        |   
        |
        |
        |
        """,
        2: """
        /---|
        |   o
        |
        |
        |
        """,
        3: """
        /---|
        |   o
        |   |
        | 
        |
        """,
        4: """
        /---|
        |   o
        |  /|
        |
        |
        """,
        5: """
        /---|
        |   o
        |  /|\\
        |
        |
        """,
        6: """
        /---|
        |   o
        |  /|\\
        |  /
        |
        """,
        7: """
        /---|
        |   o ~ thanks
        |  /|\\
        |  / \\
        |
        """
    }
    #game loop in init function so its executed on instantiation of class
    self.split_word()
    self.word_split.sort()
    self.game_update()
    
  def split_word(self):
    self.word_split = []
    for letter in list(self.word):
            if letter in self.word_split:
                continue
            self.word_split.append(letter)
  
  def get_user_guess(self):
    user_guess = input("input letter guess: ")
    
    while len(user_guess) > 1:
      user_guess = input("input one letter guess: ")
      
    while user_guess in self.guessed:
      user_guess = input("already guessed, guess again: ")
      
      if user_guess not in self.guessed:
        break
        
    self.guessed.append(user_guess)
    return user_guess

  def check_letter(self):
    users_guess = self.get_user_guess()
    if users_guess in self.word_split:
      self.correct_guesses.append(users_guess)
      self.correct_guesses.sort()
    else:
        self.bad_guesses += 1
    
    self.guessed.append(users_guess)

    
  def update_screen(self):
    print(self.screen_animations[self.bad_guesses])
    for letter_index in range(len(self.word_list)):
                letter = self.word_list[letter_index]
                if not letter in self.correct_guesses:
                    continue
                    
                self.current_guessed_word = replace_str_index(letter_index, self.current_guessed_word, letter)

    print(self.current_guessed_word)
     
  def game_update(self):
    self.correct_guesses.sort()
    while self.word_split != self.correct_guesses and not self.bad_guesses >= 7:
        self.update_screen()
        self.check_letter()
    print(f'the word was: {self.word}')
    print(self.screen_animations[self.bad_guesses])

if __name__ == '__main__':
    HangMan()