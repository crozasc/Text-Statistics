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
        print("Las Estadisticas del libro son las siguientes")
        for i in contenido:
            self.contarCaracteresConEspacio(i)
            self.contarCaracteresSinEspacio(i)
            self.contarPalabras(i)
            self.contarLineas(i)
            self.contarPalabrasUnicas(i)
            
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
        print("Lineas:",self.lineas)
        print("Palabras:",self.palabras)
        print("Palabras únicas:", len(self.palabrasUnicas))
        print("Caracteres contando espacios:",self.caracteresConEspacio)
        print("Caracteres sin contar espacios:",self.caracteresSinEspacio)

    def buscarPalabra(self, palabra):
        vecesRepetida = 0
        contenido=open(self.nombre,"r", encoding="utf-8")
        for i in contenido:
            aux=i.split()
            for j in aux:
                if(j==palabra): vecesRepetida+=1
        print("La palabra \"", palabra, "\" esta repetida", vecesRepetida, "veces")

    def reemplazarPalabra(self, palabra, reemplazo):
        contenidoInicial=open(self.nombre,"r", encoding="utf-8")
        contenidoInicial=contenidoInicial.read()
        contenidoInicial=contenidoInicial.replace(palabra,reemplazo)
        contenidoFinal=open(self.nombre,"w", encoding="utf-8")
        contenidoFinal.write(contenidoInicial)
