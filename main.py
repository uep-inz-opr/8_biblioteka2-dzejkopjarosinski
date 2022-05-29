class Biblioteka():

    
    def __init__(self):
        self.books = []
        self.titles=[]
        self.readers= {}
        self.wyniki=[]
        self.copies=[]




    def addBook(self, book):
        self.books.append(book)



    def addCopy(self,copy):
        copy1 = list(copy)
        if copy1[1:3] in self.books:
            self.copies.append(copy1[1:3])
            self.titles.append(copy1[1])
            self.wyniki.append('True')
        else:
            library.addBook(copy1[1:3])
            self.copies.append(copy1[1:3])
            self.titles.append(copy1[1])
            self.wyniki.append('True')






    def counting(self):
        final_list=[]
        sort_list=[]
        for book in self.books:
            copies_counted = self.copies.count(book)
            book1 = [book[0], book[1], copies_counted]
            final_list.append(book1)
        sort_list = sorted(final_list, key=lambda x: x[0])
        for el in sort_list:
            el1 = (el[0], el[1], el[2])
            print(el1)


    def reader(self, name, title):
        if name in self.readers:
            if len(self.readers[name]) < 3 and title not in self.readers[name]:
                self.readers[name].append(title)
                self.titles.remove(title)
                self.wyniki.append('True')
            else:
                self.wyniki.append('False')
        else:
            self.readers[name]=[]
            self.readers[name].append(title)
            self.titles.remove(title)
            self.wyniki.append('True')



    def borrow(self,name,title):
        if title in self.titles:
            self.reader(name,title)
        else:
            self.wyniki.append('False')





    def oddaj(self,name,title):
        if name in self.readers:
            if title in self.readers[name]:
                self.readers[name].remove(title)
                self.titles.append(title)
                self.wyniki.append('True')
            else:
                self.wyniki.append('False')



        else:
            self.wyniki.append('False')

    def podajWynik(self):
        for wynik in self.wyniki:
            print(wynik)





biblio = Biblioteka()



n = int(input())

for i in range(0, n):
    x = eval(input())
    if x[0] == "dodaj":
        library.addCopy(x)
    elif x[0] == "wyporzycz":
        library.borrow(x[1],x[2])
    elif x[0] == "oddaj":
        library.oddaj(x[1],x[2])

biblio.podajWynik()