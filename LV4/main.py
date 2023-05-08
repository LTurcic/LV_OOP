#from kolegij import unos_kolegija
#from ispit import unos_ispita
#from student import unos_studenta, ispis_studenta

from kolegij import unos_kolegija
from ispit import unos_ispita
from student import unos_studenta, ispis_studenta

kolegiji = []
ispiti = []
studenti = []


broj_kolegija = int(input('Unesite broj kolegija: '))
for i in range(1, broj_kolegija+1):
    kolegiji.append(unos_kolegija(i))

broj_ispita = int(input('Unesite broj ispita: '))
for i in range(1, broj_ispita+1):
    ispiti.append(unos_ispita(kolegiji, i))

broj_studenata = int(input('Unesite broj studenata: '))
for i in range(1, broj_studenata+1):
    studenti.append(unos_studenta(ispiti, i))

print('Popis svih studenata: ')
for student in studenti:
    ispis_studenta(student)