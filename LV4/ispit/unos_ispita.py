from datetime import date
from kolegij import get_kolegij


def unos_ispita(kolegiji, redni_broj):
    ispit = {}

    print('Popis kolegija: ')
    for i, kolegij in enumerate(kolegiji, start=1):
        print(get_kolegij(i, kolegij))

    odabrani_kolegij = int(input('Odaberite kolegij: '))

    ispit['kolegij'] = kolegiji[odabrani_kolegij - 1]

    dan = int(input(f'Unesite dan {redni_broj}. ispita: '))
    mjesec = int(input(f'Unesite mjesec {redni_broj}. ispita: '))
    godina = int(input(f'Unesite godinu {redni_broj}. ispita: '))

    ispit['datum'] = date(godina, mjesec, dan)

    return ispit
