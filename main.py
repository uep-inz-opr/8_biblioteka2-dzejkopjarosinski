# Liczba akcji n
# Jedna akcja to wypozycz, oddaj
# Można wypozczyć tylko jeden egzemplarz danej ksiazki 
# Można maksymalnie wypozczyć 3 egzemplaże książek 
'''
12
(" dodaj ", "Pan Tadeusz ", " Adam Mickiewicz ", 2000)
(" dodaj ", "Quo Vadis ", " Henryk Sienkiewicz ", 2010)
(" dodaj ", " Chatka Puchatka ", " Alan Alexander Milne ", 1998)
(" dodaj ", "Pan Tadeusz ", " Adam Mickiewicz ", 2000)
(" dodaj ", " Chatka Puchatka ", " Alan Alexander Milne ", 2014)
(" wypozycz ", " Bartek Perkowski ", "Pan Tadeusz ")
(" wypozycz ", " Bartek Perkowski ", "Pan Tadeusz ")
(" wypozycz ", " Jacek Malyszko ", "Quo Vadis ")
(" wypozycz ", " Bartek Perkowski ", "Quo Vadis ")
(" oddaj ", " Jacek Malyszko ", "Quo Vadis ")
(" wypozycz ", " Bartek Perkowski ", "Quo Vadis ")
(" oddaj ", " Jacek Malyszko ", "Quo Vadis ")

'''



class Book:
    def __init__(self, tytul, autor, rok):
        self.tytul = tytul
        self.autor autor
        self.rok = rok



class Egzemplarz:
    def __init__(self,rocznik,wypozczony):
        self.rocznik = rocznik
        self.wypozczony = wypozczony



class Czytelnik():
    def __init__(self,nazwisko, czytelnicy):
        self.nazwisko = nazwisko
        self.czytelnicy = czytelnicy





class Biblioteka:

        def __init__(self):
            self.ksiazki = []
            self.egzemplarze = []
            self.czytelnicy = []
            self.tytuly = []
            self.wynik = []



        def dodajKsiazke(self, ksiazka):
            self.ksiazki.append(ksiazka)
            


        def wypozycz(self,czytelnik, tytul):
            if len(czytelnik.czytelnicy) < 3:
                for wypozczona in self.ksiazki:
                    if wypozczona.tytul == tytul:
                        for ksiazka_czytelnika in czytelnik.czytelnicy:
                            if ksiazka_czytelnika.tytul == tytul:
                                return False
                        czytelnik.czytelnicy.append(wypozczona)
                        self.ksiazki.remove(wypozczona)
                        return True
            return False



        def oddaj(self, nazwisko, tytul):
            for czytelnik in self.czytelnicy:
                if czytelnik.nazwisko == nazwisko:
                    for ksiazka_czytelnika in czytelnik.czytelnicy 
                        if ksiazka_czytelnika == tytul:
                            self.ksiazki.append(ksiazka_czytelnika)
                            czytelnik.ksiazki.remove(ksiazka_czytelnika)
                            return True
            return False




biblio = Biblioteka()

n = int(input())

for i in range(0, n):
    wejscie = eval(input())
    if wejscie[0] == "dodaj":
        biblio.dodajEgzemplarz(wejscie)
    elif wejscie[0] == "wypozycz":
        biblio.wypozycz(wejscie[1],wejscie[2])
    elif wejscie[0] == "oddaj":
        biblio.oddaj(wejscie[1],wejscie[2])

biblio.pokarzWynik()
