import random
from lingowords import words
from termcolor import colored

def get_random_woord(words):
    return random.choice(words)

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

        correcte_woord = list('-' * 5)
        nieuw_woord = list(woord)
        raad_woord = list(raad)

        for i in range(5):
            if raad_woord[i] == nieuw_woord[i]:
                correcte_woord[i] = colored(raad_woord[i], 'green')

                nieuw_woord[i] = ' '
                raad_woord[i] = ' '

        for i in range(5):
            if raad_woord[i] in nieuw_woord and raad_woord[i] != ' ':
                p = nieuw_woord.index(raad_woord[i])
                correcte_woord[i] = colored(raad_woord[i], 'yellow')
                nieuw_woord[p] = ' '
        
        
        print(''.join(correcte_woord))

        if raad_woord == woord:
            print(colored(f"Gefeliciteerd! Je hebt het woord geraden in poging {poging} !", 'red'))
            break

        if poging == 5:
            print(colored(f"Helaas, je hebt het woord niet geraden. Het woord was '{woord}'.", 'red'))

    opnieuw_spelen = input("Wil je opnieuw spelen? Typ 'q' om af te sluiten of druk op Enter om opnieuw te spelen!.\n")
    if opnieuw_spelen.lower() == 'q':
        break
