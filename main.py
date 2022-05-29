class Biblioteka(object):

    # Initialize lists to contain data
    def __init__(self):
        self.books = []
        self.titles=[]
        self.readers= {} #Will be adding value to the key
        self.wyniki=[]
        self.copies=[]



    def addBook(self, book):
        self.books.append(book)


    def addCopy(self,copy):
        copy1 = list(copy)
        # If a given copy is in the list of books, append it to lists of copies and titles then return True 
        if copy1[1:3] in self.books:
            self.copies.append(copy1[1:3])
            self.titles.append(copy1[1])
            self.wyniki.append('True')
        else:
         # Else add te book to the liblary and also return True (Object needed as class parameter)   
            biblio.addBook(copy1[1:3])
            self.copies.append(copy1[1:3])
            self.titles.append(copy1[1])
            self.wyniki.append('True')



    def reader(self, name, title):
        if name in self.readers:
            if len(self.readers[name]) < 3 and title not in self.readers[name]:

                # Append value to the key
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


    # Perform remove and append on the reader and the list he is in

    def borrow(self,name,title):
        if title in self.titles:
            self.reader(name,title)
        else:
            self.wyniki.append('False')





    def return_back(self,name,title):
        if name in self.readers:
            if title in self.readers[name]:
                self.readers[name].remove(title)
                self.titles.append(title)
                self.wyniki.append('True')
            else:
                self.wyniki.append('False')



        else:
            self.wyniki.append('False')

    # Return the Trues and Falses 
    def podajWynik(self):
        for wynik in self.wyniki:
            print(wynik)




# Create an instance of the class
biblio = Biblioteka()



n = int(input())

#logic for input 
for i in range(0, n):
    x = eval(input())
    if x[0] == "dodaj":
        biblio.addCopy(x)
    elif x[0] == "wypozycz":
        biblio.borrow(x[1],x[2])
    elif x[0] == "oddaj":
        biblio.return_back(x[1],x[2])

biblio.podajWynik()