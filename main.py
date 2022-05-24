##Secret Santa
##Please do exactly as I told you
##If you run into any dificulties with using this program, just whatsapp me
import random
santa = ('Dart','Cyberblader','Juan','Sanj', 'Cotton', 'Rhea', 'Tamago')
people =  ('Dart','Cyberblader','Juan','Sanj', 'Cotton', 'Rhea', 'Tamago')
santa = list (santa)
people = list (people)
while len(santa) > 0:
    x = random.randint(0,len(santa)-1)
    y = random.randint(0, len(people)-1)

    if santa[x] != people[y]:
        giver = santa[x]
        receiver = people[y]
        print (giver, 'has', receiver)
        del santa[x]
        del people[y]
        