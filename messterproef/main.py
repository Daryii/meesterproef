import random
from lingowords import words
from termcolor import colored

def get_random_woord(words):
    return 'tegel'

def get_1e_letter(geselecteed_woord):
    eerste_letter = geselecteed_woord[0]
    return eerste_letter

while True:
    print('Welkom bij Lingo!')
    print("Type een 5-letterwoord en druk op Enter!\n")

    woord = get_random_woord(words)
    eerste_letter = get_1e_letter(woord)
    print(eerste_letter)

    opnieuw_spelen = ""

    for poging in range(50):
        while True:
            raad = input(f"Poging {poging}: ").lower()
            if len(raad) == 5:
                break
            else:
                print("Het woord moet precies 5 letters lang zijn!")

        correcte_letters = ""
        
        for i in range(5):
            if raad[i] == woord[i]:
                
                correcte_letters += colored(raad[i], 'green')
            else:
                correcte_letters += '-'
        copy_woord = correcte_letters
        for x in range(5):
            if copy_woord in woord and copy_woord != woord[x]:
                correcte_letters += colored(raad[x], 'yellow')
                
                

        print(correcte_letters)

        if raad == woord:
            print(colored(f"Gefeliciteerd! Je hebt het woord geraden in poging {poging} of druk op Enter!", 'red'))
            break

        if poging == 5:
            print(colored(f"Helaas, je hebt het woord niet geraden. Het woord was '{woord}'.", 'red'))

    opnieuw_spelen = input("Wil je opnieuw spelen? Typ 'q' om af te sluiten.\n")
    if opnieuw_spelen.lower() == 'q':
        break
