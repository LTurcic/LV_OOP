from datetime import date
godina= 2023
mjesec= 4
dan= 18

korisnik = {}

korisnik["Ime_korisnika"] = input("Unesite ime korisnika:").capitalize()
korisnik["Prezime_korisnika"] = input("Unesite prezime korisnika:").capitalize()
korisnik["Telefon_korisnika"] =int(input ("Unesite broj telefona:"))
korisnik["Email"]= input("Unesite email adresu:").strip()

artikl = {}

artikl["Naslov"] = input ("Unesite naslov artikal:")
artikl["Opis"] =input("Unesite opis artikla:")
artikl["Cijena €"]=float(input("Unesite cijenu artikla u eurima:"))

prodaja = {}

prodaja["Datum"]=date(godina, mjesec, dan)
prodaja["Korisnik"]=korisnik
prodaja["Artikl"]=artikl

print(f"Informacije o artiklu: "
      f"\n\tNaslov: {prodaja['Artikl']['Naslov']}".expandtabs(8),
      f"\n\tOpis: {prodaja['Artikl']['Opis']}".expandtabs(8),
      f"\n\tCjena €: {prodaja['Artikl']['Cijena €']}".expandtabs(8),
      f"\nDatum isteka prodaje: "
      f"\n\tDan: {prodaja['Datum'].day}".expandtabs(8),
      f"\n\tMjesec: {prodaja['Datum'].month}".expandtabs(8),
      f"\n\tGodina: {prodaja['Datum'].year}".expandtabs(8),
      f"\nInformacije o korisniku: "
      f"\n\t{prodaja['Korisnik']['Ime_korisnika']} {prodaja['Korisnik']['Prezime_korisnika']}".expandtabs(8),
      f"\n\t{prodaja['Korisnik']['Telefon_korisnika']}".expandtabs(8),
      f"\n\t{prodaja['Korisnik']['Email']}".expandtabs(8))
