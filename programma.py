import random
from lingowords import*

poging = 5

def get_random_woord(words):
    return random.choice(words)
  

def get_1e_letter(geselecteed_woord):
    eerste_letter = geselecteed_woord[0][0]
    return eerste_letter


print('Welkom bij lingo')
eerst_letter = get_1e_letter(words)
print(eerst_letter)

for i in range(poging):
    woord_vraag  = input('raad het woord: ')
    random_woord = get_random_woord(words)
    if woord_vraag == random_woord :
        print(random_woord)
        exit()
    elif woord_vraag in random_woord:
        print()



