class Kolegij:
    def __init__(self, ime, ects):
        self.__ime = ime
        self.__ects = ects

    @property
    def ime(self):
        return self.__ime

    @ime.setter
    def ime(self, ime):
        self.__ime = ime

    @property
    def ects(self):
        return self.__ects
    @ects.setter
    def ects(self, ects):
        self.__ects = ects

    def ispis(self):
        print(f"\tKolegij {self.__ime} nosi {self.__ects} ECTS bod")