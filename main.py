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


class Biblioteka(object):

        def __init__(self):
            self.books = []
            self.copies  = []
            self.readers = []
            self.titles = []
            self.wynik=[]



        def dodajKsiazke(self, ksiazka):
            self.books.append(ksiazka)


        #Stworz pojedynczy egzemplarz i dodaj do listy egzemplarzy
        def addCopy(self, egzemplarz):
            el1 = list(egzemplarz)
            # Jeśli egzemplarz znajduje sie w liscie ksiazek
            if el1[1:3] in self.books:
                self.copies.append(el1[1:3])
                self.titles.append(el1[1])
                self.wynik.append("True")

            else:
            # Jeśli egzemplarz nie znajduje się w liście ksiazek
                self.dodajKsiazke(el1[1:3])
                self.titles.append(el1[1])
                self.copies.append(el1[1:3])
                self.wynik.append('True')



        def reader(self, name, title):
            if name in self.readers:
                if len(self.readers[name]) < 3 and title not in self.readers[name]:
                    self.readers[name].append(title)
                    self.titles.remove(title)
                    self.wynik.append('True')
                else:
                    self.wynik.append('False')
            else:
                self.readers[name]=[]
                self.readers[name].append(title)
                self.titles.remove(title)
                self.wynik.append('True')




        def borrow(self):
            if title in self.titles:
                self.reader(name,title)
            else:
                self.wynik.append('False')



        def returnBack(self,name,title):
            if name in self.readers:
                if title in self.readers[name]:
                    self.readers[name].remove(title)
                    self.titles.append(title)
                    self.wynik.append('True')
                else:
                    self.wynik.append('False')
            else:
                self.wynik.append('False')


        def calculation(self):
            final_list = []
            sort_list  = []
            for ksiazka in self.books:
                a = self.copies .count(ksiazka)
                ksiazka1 = [ksiazka[0], ksiazka[1],a]
                final_list.append(ksiazka1)
                sort_list = sorted(final_list, key=lambda x: x[0])
                for element in sort_list:
                    element1 = (element[0], element[1], element[2])
                    print(element1)


        def pokaWynik(self):
            for w in self.wynik:
             print(w)





biblio = Biblioteka()

n = int(input())

for i in range(0, n):
    wejscie = eval(input())
    if wejscie[0] == "dodaj":
        biblio.addCopy(wejscie)
    elif wejscie[0] == "borrow":
        biblio.borrow(wejscie[1],wejscie[2])
    elif wejscie[0] == "oddaj":
        biblio.returnBack(wejscie[1],wejscie[2])

biblio.pokaWynik()