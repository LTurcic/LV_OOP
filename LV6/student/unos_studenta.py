from ispit import get_ispit
from utilities import unos_intervala
from .Student import Student


def unos_studenta(ispiti, redni_broj):
    ime = input(f"Unesite ime {redni_broj}. studenta: ").capitalize()
    prezime = input(f"Unesite prezime {redni_broj}. studenta: ").capitalize()

    for i, ispit in enumerate(ispiti, start=1):
        print(get_ispit(i, ispit))

    print('Za odabir ispita')
    odabrani_ispit = unos_intervala(1, len(ispiti))
    ispit = ispiti[odabrani_ispit - 1]
    return Student(ime, prezime, ispit)