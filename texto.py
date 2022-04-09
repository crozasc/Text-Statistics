class text:
    def __init__(self, name):
        self.name = name
        self.lines = 0
        self.words = 0
        self.unicWords = set([])
        self.charactersWithSpace = 1
        self.charactersWithoutSpace = 1
        
    def statisticsText(self):
        content=open(self.name,"r", encoding="utf-8")
        print("The statistics of the book are")
        for i in content:
            self.countCharactersWithSpace(i)
            self.countCharactersWithoutSpace(i)
            self.countWords(i)
            self.countLines(i)
            self.countUnicWords(i)
        self.printStatistics()
            
    def countCharactersWithSpace(self, i):
        for j in i:
            if(j!=""): self.charactersWithSpace+= 1
        self.charactersWithSpace=self.charactersWithSpace-1

    def countCharactersWithoutSpace(self, i):
        for j in i:
            if(j!=" "): 
                self.charactersWithoutSpace+= 1
        self.charactersWithoutSpace=self.charactersWithoutSpace-1
    
    def countWords(self, i):
        for j in i:
            if(j==" "):self.words+=1
        self.words=self.words+1
    
    def countLines(self, i):
        self.lines+=1

    def countUnicWords(self, i):
        aux=i.split()
        aux=set(aux)
        self.unicWords.update(aux)

    def printStatistics(self):
        print("Lines:",self.lines)
        print("Words:",self.words)
        print("Unic Words:", len(self.unicWords))
        print("Characters counting spaces:",self.charactersWithSpace)
        print("Characters without counting spaces:",self.charactersWithoutSpace)

    def searchWord(self, word):
        timesRepeated = 0
        content=open(self.name,"r", encoding="utf-8")
        for i in content:
            aux=i.replace(";"," ").replace(","," ").replace("-"," ").replace("|"," ").replace("/"," ").split()
            for j in aux:
                if(j==word): timesRepeated+=1
        if(timesRepeated==0):print("The word \"", word, "\" is not repeated")
        else:print("The word \"", word, "\" is repeated", timesRepeated, "times")

    def reemplazarPalabra(self, word, reemplazo):
        initialContent=open(self.name,"r", encoding="utf-8")
        initialContent=initialContent.read()
        initialContent=initialContent.replace(word,reemplazo)
        finalContent=open(self.name,"w", encoding="utf-8")
        finalContent.write(initialContent)

def menu2(option):
    ans=True
    if option=="1":book="Libros_txt_utf-8\El_Arbol_De_La_Colina.txt"
    elif option=="2":book="Libros_txt_utf-8\El_Caos_Reptante.txt"
    elif option=="3":book="Libros_txt_utf-8\En_El_Mar_Remoto.txt"
    elif option=="4":book="Libros_txt_utf-8\Lazarillo_de_Tormes.txt"
    elif option=="5":book="Libros_txt_utf-8\Para_Leer_Al_Atardecer.txt" 
    elif option=="6":book="Libros_txt_utf-8\\Una_corta_historia_del_eBook.txt"
    elif option=="7":
        try:
            book=input("Enter the name of the book in Libros_txt_utf-8: ")
            book='Libros_txt_utf-8\\' + book
            open(book,"r", encoding="utf-8")
        except: 
            print("Invalid book")
            ans=False    
    t=text(book)
    while ans:
        print ("""
        Select option
        1.Statistics
        2.Find repeated word
        3.Find word and replace
        4.Go back
        """)
        ans=input("What would you like to do? ")
        if ans=="1":t.statisticsText()
        elif ans=="2":t.searchWord(input("Enter your word: "))
        elif ans=="3":t.reemplazarPalabra(input("Enter the searched word: "),input("Enter the replace word: "))
        elif ans=="4":ans=False
        elif ans !="":
            print("\n Not Valid Choice Try again")


def menu():
    ans=True
    while ans:
        print ("""
        Select book
        1.El Arbol De La Colina
        2.El Caos Reptante
        3.En El Mar Remoto
        4.Lazarillo de Tormes
        5.Para Leer Al Atardecer
        6.Una_corta_historia_del_eBook
        7.Another book added to Libros_txt_utf-8
        8.Leave
        """)
        ans=input("What would you like to do?: ")
        if ans=="1":menu2(ans) 
        elif ans=="2":menu2(ans) 
        elif ans=="3":menu2(ans) 
        elif ans=="4":menu2(ans) 
        elif ans=="5":menu2(ans) 
        elif ans=="6":menu2(ans)
        elif ans=="7":menu2(ans)
        elif ans=="8":ans=False
        elif ans !="":
            print("\n Not Valid Choice Try again")
