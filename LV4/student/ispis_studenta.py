from ispit import ispis_ispita

def ispis_studenta(student):
    print(f"Student {student['ime']} {student['prezime']} je prijavio:")
    ispis_ispita(student['ispit'])