def ispis_ispita(ispit):
 print(f"Ispit iz kolegija {ispit['kolegij']['ime']} koji nosi {ispit['kolegij']['ects']} ECTS bodova.",
       f"Ispit će se održati {ispit['datum']}.")

def ispis_svih_ispita(ispiti):
    print('Ispis svih ispita: ')
    for ispit in ispiti:
        ispis_ispita(ispit)



def get_ispit(redni_broj, ispit):
    return f"{redni_broj}. {ispit['kolegij']['ime']}"