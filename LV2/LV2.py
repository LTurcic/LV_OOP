from datetime import date

kolegij = {}

kolegij['Ime_kolegija'] = input('Unesite ime kolegija: ').upper()
kolegij['Broj_ECTS'] = int(input('Unesite ECTS bodove za kolegij: '))

print('Kolegij', kolegij['Ime_kolegija'], 'nosi', kolegij['Broj_ECTS'], 'ECTS bodova')

ispit = {}

ispit['Kolegij'] = kolegij
dan = int(input('Unesite dan ispita: '))
mjesec = int(input('Unesite mjesec ispita: '))
godina = int(input('Unesite godinu ispita: '))
ispit['Datum_ispita'] = date(godina, mjesec, dan)
print('Kolegij', ispit['Kolegij']['Ime_kolegija'], 'nosi', ispit['Kolegij']['Broj_ECTS'], 'ECTS bodova')
print('Datum ispita je:', ispit['Datum_ispita'])

student = {}

student['Ispit'] = ispit
ime_studenta = input('Unesite ime studenta: ').capitalize()
prezime_studenta = input('Unesite prezime studenta: ').capitalize()
student['Podaci'] = ime_studenta + ' ' + prezime_studenta
print('Student', student['Podaci'], '\nje prijavio ispit iz kolegija',
       student['Ispit']['Kolegij']['Ime_kolegija'], '\nkoji će se održati:', student['Ispit']['Datum_ispita'])