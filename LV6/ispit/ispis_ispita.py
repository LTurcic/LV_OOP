

def ispis_svih_ispita(ispiti):
    print('Ispis svih ispita: ')
    for ispit in ispiti:
        ispit.ispis()



def get_ispit(redni_broj, ispit):
    return f"{redni_broj}. {ispit.kolegij.ime}"