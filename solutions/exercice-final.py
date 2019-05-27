import csv
signalements_au_MB = []
fichier_données_ovni = open('../exercices/données-ovni.csv', 'r')

lecteur_dictionnaire_données_ovni = csv.DictReader(données-ovni)
for signalement in lecteur_dictionnaire_données_ovni:
    if signalement['Province'] == 'MB' and signalement['Lieu'] == 'Gimli':
        signalements_au_MB.append(signalement)

print(len(signalements_au_MB))
fichier_données_ovni.close()
