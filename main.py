import random
from hangman_art import *
from hangman_words import *
soln=[]
print(logo)
chosen_word = random.choice(word_list)
for letters in chosen_word:
  soln.append("_")
c=len(stages)-1
while '_' in soln and c!=0:
  guess=input("guess a letter ").lower()
  if guess in chosen_word:
    for i in range(0,len(chosen_word)):
      if chosen_word[i] == guess:
        soln[i]=guess
  else:    
      print("wrong answer, you lost a life")
      print(stages[c])
      c-=1
  print(f"{' '.join(soln)}")
if c==0:
  print(stages[0])
  print("you lose")
  print(f"The correct answer was {chosen_word}")
else:
  print("you won")
