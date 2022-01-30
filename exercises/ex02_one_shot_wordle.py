"""EX02 - Creating a one shot wordle"""

__author__ = "730460153"

secret_word = str("python")

guess: str = input(f"What is your {len(secret_word)}-letter guess? ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
index: int = 0
final: str = ""

while len(guess) != len(secret_word):
        input(f"That was not {len(secret_word)} letters! Try again: ")

while index < len(secret_word):
    exists: bool = False
    index_two: int = 0
    if secret_word[index] == guess[index]:
        final = final + GREEN_BOX
        exists = True
    while exists is (False) and index_two < len(secret_word):
        if secret_word[index_two] == guess[index]:
            exists = True
        else:
            index_two = index_two + 1
        if exists is True:
            final = final + YELLOW_BOX
    else:
        if exists == False:
            final = final + WHITE_BOX
    index = index + 1
print(final) 

if len(guess) == len(secret_word) and guess != secret_word:
    print("Not quite.  Play again soon!")

if guess == secret_word:
    print("Woo! You got it!")