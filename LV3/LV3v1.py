from datetime import date

kolegiji = []

broj_kolegija = int(input('Unesite broj kolegija: '))

for i in range (1, broj_kolegija+1):
    kolegij = {}
    kolegij['Ime']=input(f"Unesite ime {i}. kolegija: ")
    kolegij['ECTS']=input(f"Unesite broj ECTS-a {i}. kolegija: ")
    kolegiji.append(kolegij)

print("Popis svih koelgija: ")

for kolegij in kolegiji:
    print(f"\tKolegij {kolegij['Ime']} nosi {kolegij['ECTS']} ECTS bodova.".expandtabs(8))

ispiti = []

broj_ispita = int(input('Unesite broj ispita: '))

print('Popis kolegija: ')

for i in range (1, broj_ispita+1):
    ispit = {}

    for j, kolegij in enumerate(kolegiji, start=1):
        print(f"\t{j}. {kolegij['Ime']}")

    kolegij = int(input('Odaberite kolegij: '))

    ispit['kolegij']=kolegiji[kolegij-1]

    dan = int(input(f'Unesite dan {i}. ispita: '))
    mjesec  = int(input(f'Unesite mjesec {i}. ispita: '))
    godina = int(input(f'Unesite godinu {i}. ispita: '))

    ispit['Dan ispita'] = date(godina, mjesec, dan)

    ispiti.append(ispit)

for ispit in ispiti:
    print(f"Ispit iz kolegija {ispit['kolegij']['Ime']} koji nosi {ispit['kolegij']['ECTS']} ECTS bodova će se održati {ispit['Dan ispita']}")