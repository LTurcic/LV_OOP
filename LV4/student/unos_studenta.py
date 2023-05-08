from ispit import get_ispit


def unos_studenta(ispiti, redni_broj):
    student = {}
    student['ime'] = input(f"Unesite ime {redni_broj}. studenta: ").capitalize()
    student['prezime'] = input(f"Unesite prezime {redni_broj}. studenta: ").capitalize()

    for j, ispit in enumerate(ispiti, start=1):
        print(get_ispit(j, ispit))

    odabrani_ispit = int(input("Unesite ispit: "))
    student['ispit'] = ispiti[odabrani_ispit - 1]

    return ispiti