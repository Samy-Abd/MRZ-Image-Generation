from tqdm import tqdm
import random
import itertools
from Preprocessing import checker

nom = []
prenom = []
with open('data/prenom.txt', 'r') as f_nom:
    for line in tqdm(f_nom):
        nom.append(line.replace('\n', ""))
with open('data/nom.txt', 'r') as f_prenom:
    for line in tqdm(f_prenom):
        prenom.append(line.replace('\n', ""))

random.shuffle(nom)
random.shuffle(prenom)

print(len(nom), len(prenom))
random_nom= random.sample(nom, 1000)
random_prenom= random.sample(prenom, 1000)
combinations = list(itertools.product(random_nom, random_prenom))
nom_prenom = random.sample(combinations, 150000)
with open('data/sample.txt', 'a+') as f_sample:
    for i in nom_prenom:
        if not checker(i[0]) or not checker(i[1]):
            continue
        f_sample.write(i[0] + '|' + i[1] + '\n')
    
