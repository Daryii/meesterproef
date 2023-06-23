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


    for poging in range(1,6):
        while True:
            raad = input(f"Poging {poging}: ").lower()
            if len(raad) == 5:
                break
            else:
                print("Het woord moet precies 5 letters lang zijn!")

        correcte_woord =list(woord)
        nieuw_woord = list(woord)

        for i in range(5):
            if raad[i] == nieuw_woord[i]:
                correcte_woord[i] = colored(raad[i], 'green')
                nieuw_woord[i] = ' '
            elif raad[i] in nieuw_woord and raad[i] != nieuw_woord[i]:  
                correcte_woord[i] = colored(raad[i], 'yellow')
                nieuw_woord[i] = ' '
            else:
                correcte_woord[i] = '-'
                
            

        
        print(''.join(correcte_woord))

        if raad == woord:
            print(colored(f"Gefeliciteerd! Je hebt het woord geraden in poging {poging} !", 'red'))
            break

        if poging == 5:
            print(colored(f"Helaas, je hebt het woord niet geraden. Het woord was '{woord}'.", 'red'))

    opnieuw_spelen = input("Wil je opnieuw spelen? Typ 'q' om af te sluiten of druk op Enter om opnieuw te spelen!.\n")
    if opnieuw_spelen.lower() == 'q':
        break
