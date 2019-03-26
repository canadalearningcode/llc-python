import csv
sightings_in_mb = []
ufo_data_file = open('../exercises/ufo-data.csv', 'r')

ufo_data_dictionary_reader = csv.DictReader(ufo_data_file)
for sighting in ufo_data_dictionary_reader:
    if sighting['Province'] == 'MB' and sighting['Location'] == 'Gimli':
        sightings_in_mb.append(sighting)

print(len(sightings_in_mb))
ufo_data_file.close()
