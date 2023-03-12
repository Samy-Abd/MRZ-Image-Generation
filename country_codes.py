

seperator = '|'
with open('data/nom_prenom.csv', 'r') as f_country:
    for line in f_country:
        if line.startswith('#'):
            continue
        