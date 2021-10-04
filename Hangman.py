# Hangman is a game where only some of the letters from a random words are displayed and you have to guess it before you run out of lives.

import random
word_list = ["BANANA","PINEAPPLE","RASPBERRY"]
choice = random.choice(word_list)
length = len(choice)
display = []
length2 = len(display)
end = 0
count = 0
life = 5

for letter in choice:
    display += "_"

print("Guess the word with",length,"letters!")
print(display)

while life != 0 or length != count:
    guess = input("Enter your guess : ").upper()
    for position in range(length):
        letter2 = choice[position]
        if guess == letter2:
            display[position] = letter2
            count += 1
        elif letter2 != choice[position]:
            life -=1
            print("Wrong guess!\nLife remaining :",life)
            break
    print(display)
