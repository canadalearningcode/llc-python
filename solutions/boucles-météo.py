conditions_météo = ['pluie', 'neige', 'nuages','soleil','brouillard']
for type_de_météo in conditions_météo:
    if type_de_météo == 'pluie':
        print(type_de_météo + ' : Apporter un parapluie')
    elif type_de_météo == 'neige':
        print(type_de_météo + ' : Porter un pantalon de neige')
    else:
        print(type_de_météo + ' : Qui sait? ')
