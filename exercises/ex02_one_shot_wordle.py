"""EX02 - Creating a one shot wordle"""

__author__ = "730460153"

from operator import truediv
import secrets


Secret_word = str("python")

guess: str = input(f"What is your {len(Secret_word)}-letter guess? ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
index: int = 0
final: str = ""
exists: bool = False
index_two: int = 0


while len(guess) != len(Secret_word):
        input(f"That was not {len(Secret_word)} letters! Try again: ")

while index < len(Secret_word):
    if Secret_word[index] == guess[index]:
        final = final + GREEN_BOX
    while exists == (not True) and index < len(Secret_word):
        if Secret_word[index_two] == guess[index]:
            exists = True
        else:
            index_two = index_two + 1
        if Secret_word[index_two] == guess[index]:
            final = final + YELLOW_BOX
            exists = True
    else:
        final = final + WHITE_BOX
    index = index + 1
print(final) 

if len(guess) == len(Secret_word) and guess != Secret_word:
    print("Not quite.  Play again soon!")

if guess == Secret_word:
    print("Woo! You got it!")