korisnik = {
    'ime': 'Ivan',
    'prezime': 'Ivic',
    'godine': 24
}
for value in korisnik:
    print(value, end=' ')
    print()
for key, value in korisnik.items():
    print(f'{key} {value}', end=' ')
    print()
for key in korisnik.keys():
    print(f'{key}', end=' ')
    print()
for value in korisnik.values():
    print(f'{value}', end=' ')
    print()