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
