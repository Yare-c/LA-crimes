import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

with open('crimes.csv') as f:
    reader = csv.reader(f)
    x = list(reader)
    titles = x[0]
    x.pop(0)

def place():
    global places, places_times, places_dict
    places = []
    places_dict = []
    for mure in x:
        if mure[15] not in places:
            places.append(mure[15])
            places_dict.append({'name': mure[15], 'number': 0})

    for d in x:
        if d[15] in places:
            indx = places.index(d[15])
            places_dict[indx]['number'] = places_dict[indx]['number'] + 1
    places_times = []
    for d2 in places_dict:
        places_times.append(d2['number'])

place()
def weapon():
    global weapons, weapon_times, weapons_dict
    weapons = []
    weapons_dict = []
    for mure in x:
        if mure[17] not in weapons:
            weapons.append(mure[17])
            weapons_dict.append({'name': mure[17], 'number': 0})

    for d in x:
        if d[17] in weapons:
            indx = weapons.index(d[17])
            weapons_dict[indx]['number'] = weapons_dict[indx]['number'] + 1
    weapon_times = []
    for d2 in weapons_dict:
        weapon_times.append(d2['number'])


weapon()

train_data = {
    'coordinats': [],
    'sex': [],
    'age': []
}
def age_sex():
    global gens, gens_data, sex
    age = []
    sex = []
    for add in x:
        train_data['coordinats'].append([add[26], add[27]])
        # take away the trash data
        if add[12] == '' or add[12] == "X": 
            pass
        else:
            train_data['sex'].append(add[12])
            train_data['age'].append(add[11])
        age.append(add[11])
        sex.append(add[12])
    gens = ['M', 'F', 'X']
    genders = [{'gender': 'M', 'number': 0}, {'gender': 'F', 'number': 0}, {'gender': 'X', 'number': 0}]
    for aq in sex:
        if aq in gens:
            indx = gens.index(aq)
            genders[indx]['number'] = genders[indx]['number'] + 1
    gens_data = []
    for getting in genders:
        gens_data.append(getting['number'])

    # age for everyone
    age_int = [int(t) for t in age]
    age_median = sum(age_int) / len(age_int)

    # age for sexes
    men_age = []
    female_age = []
    x_age = []
    for who in x:
        if who[12] == "M":
            men_age.append(who[11])
        if who[12] == "F":
            female_age.append(who[11])
        if who[12] == "X":
            x_age.append(who[11])

    # to integers
    men_age_int = [int(men_int) for men_int in men_age]
    female_age_int = [int(female_int) for female_int in female_age]
    x_age_int = [int(x_int) for x_int in x_age]

    # median
    men_age_median = sum(men_age_int) / len(men_age_int)
    female_age_median = sum(female_age_int) / len(female_age_int)
    x_age_median = sum(x_age_int) / len(x_age_int)
age_sex()

def crime():
    global name_crime, much_times, crimes
    crime_pure = []
    crime = []
    crimes = []
    for po in x:
        crime_pure.append(po[9])
        if po[9] not in crime:
            crime.append(po[9])
            crimes.append({'name': po[9], 'number': 0})
    for aq2 in crime_pure:
        if aq2 in crime:
            indx = crime.index(aq2)
            crimes[indx]['number'] = crimes[indx]['number'] + 1
    much_times = []
    name_crime = []
    for number in crimes:
        name_crime.append(number['name'])
        much_times.append(number['number'])
crime()

def sort_data_crimes():
    global power, power2, top_5
    power =[]
    power2 = []
    high_data = []
    top_5 = ["Vehicle St.", "Assault", "Theft", "Burglary Veh.", "Vandalism"]
    for high in crimes:
        high_data.append(high['number'])
    
    high_data.sort()
    for appen in range(1, 6):
        power.append(high_data[len(high_data)-appen])

    for finder in power:
        for finder2 in crimes:
            if finder == finder2['number']:
                power2.append(finder2['name'])
    


def sort_data_weapon():
    global power, power2
    power =[]
    power2 = []
    high_data = []
    for high in weapons_dict:
        high_data.append(high['number'])
    
    high_data.sort()
    for appen in range(1, 6):
        power.append(high_data[len(high_data)-appen])

    for finder in power:
        for finder2 in weapons_dict:
            if finder == finder2['number']:
                power2.append(finder2['name'])
    print(power)
    power2[0] = '*'
    power2[1] = 'Arm'
    power2[2] = 'Unknown'
    power2[3] = 'Verbal Th.'
    power2[4] = 'Hand Gun'
    


def sort_data_place():
    global power, power2
    power =[]
    power2 = []
    high_data = []
    for high in places_dict:
        high_data.append(high['number'])
    
    high_data.sort()
    for appen in range(1, 6):
        power.append(high_data[len(high_data)-appen])

    for finder in power:
        for finder2 in places_dict:
            if finder == finder2['number']:
                power2.append(finder2['name'])
    
    print(power2)
    power2[1] = 'Fam. Dwelling'
    power2[2] = 'Multi Dwelling'
    power2[3] = 'Parking'
    power2[4] = 'Other'
sort_data_place()

def plotting():
    plt.style.use('ggplot')
    plt.title('Los-Angeles 2020-2022')
    plt.suptitle('Weapons')
    plt.xlabel('Name of weapon')
    plt.ylabel('Number of weapon')
    #plt.xticks(rotation='vertical')
    plt.bar(power2, power)
    plt.show()
plotting()
def coords():
    global finale, another_data, crimes_data
    finale = []
    another_data = []
    crimes_data = []
    c = 0
    for get in x:
        crimes_data.append(get[9])
        another_data.append(f'Age:{get[11]}, Sex: {get[12]}, Crime: {get[9]}')
        finale.append([get[26], get[27]])
        if c == 0:
            break
        else:
            c = c + 1
coords()


    