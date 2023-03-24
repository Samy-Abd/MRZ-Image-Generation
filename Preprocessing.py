from tqdm import tqdm


#we take the data from the csv file and generate two files name and surname from it


special_ch = '?@#$%^&*()_+{}|:"<>?/.,;[]\=-`~!'

def spec_checker(line):
    for i in special_ch:
        if i in line:
            return False

def checker(line):
    # Check if the line is empty
    if line == '\n':
        return False
    # Check if there is space before the name or surname
    elif line.isspace():
        return False
    # Check if there are invalid characters
    elif spec_checker(line) == False:   
        return False
     # Check if the line is empty
    elif len(line) < 1:
        return False
    elif line == 'UNITE' or line == 'O.N.A.':
        return False
    elif line == '.':
        return False
    elif len(line) >= 30:
        return False
    else:
        return True

seperator = '|'
with open('data/nom_prenom.csv', 'r') as f_in, open('data/nom.txt', 'w') as f_nom, \
            open('data/prenom.txt', 'w') as f_prenom, open('data/nom_prenom_traite.txt', 'w') as f_traite:
    # Read the input file line by line
    for line in tqdm(f_in):
        lineb = line.split(seperator)
        if checker(lineb[0]):
            if lineb[0].startswith(' '):
                lineb[0] = lineb[0][1:]
            f_nom.write(lineb[0].replace('\n', "") + '\n')
        if len(lineb) > 1 and checker(lineb[1]):
            if lineb[1].startswith(' '):
                lineb[1] = lineb[1][1:]
            f_prenom.write(lineb[1].replace('\n', "") + '\n')
        if len(lineb) > 1:
            if len(lineb[0]) > 1 and len(lineb[1]) > 1 \
                and checker(lineb[0]) and checker(lineb[1]):
                    f_traite.write(lineb[0].replace('\n', "") + '|' + lineb[1].replace('\n', "") + '\n')







