class texto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lineas = 0
        self.palabras = 0
        self.palabrasUnicas = set([])
        self.caracteresConEspacio = 1
        self.caracteresSinEspacio = 1
        
    def estadisticasTexto(self):
        contenido=open(self.nombre,"r", encoding="utf-8")
        print("The statistics of the book are")
        for i in contenido:
            self.contarCaracteresConEspacio(i)
            self.contarCaracteresSinEspacio(i)
            self.contarPalabras(i)
            self.contarLineas(i)
            self.contarPalabrasUnicas(i)
        self.printDetalles()
            
    def contarCaracteresConEspacio(self, i):
        for j in i:
            if(j!=""): self.caracteresConEspacio+= 1
        self.caracteresConEspacio=self.caracteresConEspacio-1

    def contarCaracteresSinEspacio(self, i):
        for j in i:
            if(j!=" "): 
                self.caracteresSinEspacio+= 1
        self.caracteresSinEspacio=self.caracteresSinEspacio-1
    
    def contarPalabras(self, i):
        for j in i:
            if(j==" "):self.palabras+=1
        self.palabras=self.palabras+1
    
    def contarLineas(self, i):
        self.lineas+=1

    def contarPalabrasUnicas(self, i):
        aux=i.split()
        aux=set(aux)
        self.palabrasUnicas.update(aux)

    def printDetalles(self):
        print("Lines:",self.lineas)
        print("Words:",self.palabras)
        print("Unic Words:", len(self.palabrasUnicas))
        print("Characters counting spaces:",self.caracteresConEspacio)
        print("Characters without counting spaces:",self.caracteresSinEspacio)

    def buscarPalabra(self, palabra):
        vecesRepetida = 0
        contenido=open(self.nombre,"r", encoding="utf-8")
        for i in contenido:
            aux=i.replace(";"," ").replace(","," ").replace("-"," ").replace("|"," ").replace("/"," ").split()
            for j in aux:
                if(j==palabra): vecesRepetida+=1
        if(vecesRepetida==0):print("The word \"", palabra, "\" is not repeated")
        else:print("The word \"", palabra, "\" is repeated", vecesRepetida, "times")

    def reemplazarPalabra(self, palabra, reemplazo):
        contenidoInicial=open(self.nombre,"r", encoding="utf-8")
        contenidoInicial=contenidoInicial.read()
        contenidoInicial=contenidoInicial.replace(palabra,reemplazo)
        contenidoFinal=open(self.nombre,"w", encoding="utf-8")
        contenidoFinal.write(contenidoInicial)

def menu2(option):
    ans=True
    if option=="1":libro="Libros_txt_utf-8\El_Arbol_De_La_Colina.txt"
    elif option=="2":libro="Libros_txt_utf-8\El_Caos_Reptante.txt"
    elif option=="3":libro="Libros_txt_utf-8\En_El_Mar_Remoto.txt"
    elif option=="4":libro="Libros_txt_utf-8\Lazarillo_de_Tormes.txt"
    elif option=="5":libro="Libros_txt_utf-8\Para_Leer_Al_Atardecer.txt" 
    elif option=="6":libro="Libros_txt_utf-8\\Una_corta_historia_del_eBook.txt"
    elif option=="7":
        try:
            libro=input("Enter the name of the book in Libros_txt_utf-8: ")
            libro='Libros_txt_utf-8\\' + libro
            open(libro,"r", encoding="utf-8")
        except: 
            print("Invalid book")
            ans=False    
    t=texto(libro)
    while ans:
        print ("""
        Select option
        1.Statistics
        2.Find repeated word
        3.Find word and replace
        4.Go back
        """)
        ans=input("What would you like to do? ")
        if ans=="1":t.estadisticasTexto()
        elif ans=="2":t.buscarPalabra(input("Enter your word: "))
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
