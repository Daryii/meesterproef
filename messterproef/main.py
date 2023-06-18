import random
from lingowords import*
import sys
from termcolor import colored

def get_random_woord(words):
    return random.choice(words)

def get_1e_letter(geselecteed_woord):
    eerste_letter = geselecteed_woord[0][0]
    return eerste_letter

print('Welkom bij lingo')
print("Type een 5 letter woord en click enter!\n")

eerst_letter = get_1e_letter(words)
print(eerst_letter)
woord = get_random_woord(words)
opnieuw_spelen = ""

while opnieuw_spelen != "q":
    for poging in range(1,6):
        raad = input("").lower()

        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')

        for i in range(min(len(raad),5)):
            if raad[i] == woord[i]:
                print(colored(raad[i], 'green'), end="")
            elif raad[i] in woord:
                print(colored(raad[i], 'yellow'), end="")
            else:
                print(raad[i], end="")

            if raad == woord:
                print(colored(f"Gefeliciteerd! Je hebt de woord in {i} geraden ",'red'))
                break
    opnieuw_spelen = input("Wil je opnieuw spelen? Typ (q) om af te sluiten.")
