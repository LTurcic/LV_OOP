from ispit import ispis_ispita


def ispis_studenta(student):
    print(f"Student {student['ime']} {student['prezime']} je prijavio:")
    ispis_ispita(student['ispit'])


def ispis_svih_studenata(studenti):
    print('Popis svih studenata: ')
    for student in studenti:
        student.ispis()