def ispis_kolegija(kolegij):
    print(f"\tKolegij {kolegij['ime']} nosi {kolegij['ects']} ECTS bodova")

    return kolegij

def ispis_svih_kolegija(kolegiji):
    print('Popis svih kolegija: ')
    for kolegij in kolegiji:
        ispis_kolegija(kolegij)


def get_kolegij(redni_broj, kolegij):
    return f"{redni_broj}. {kolegij['ime']}"