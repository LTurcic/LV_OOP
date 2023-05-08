def unos_intervala(min, max):
    while True:
        try:
            broj = int(input(f"Unesite cijeli broj u intervalu {min}-{max}: "))

            if broj < min or broj > max:
                raise Exception(f"Unesite broj unutar interevala {min}-{max}.")

        except ValueError:
            print("Unijeli ste znak, a ne cijeli broj.")

        except Exception as e:
            print(e)

        else:
            return broj
