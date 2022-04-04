class texto:
    def __init__(self, nombre):
        self.contenido = open(nombre, "r")
        self.lineas = 0
        self.palabras = 0
        self.palabrasUnicas = 0
        self.caracteresConEspacio = 1
        self.caracteresSinEspacio = 1
        

    def estadisticasTexto(self):
        for i in self.contenido:
            self.contarCaracteresConEspacio(i)
            self.contarCaracteresSinEspacio(i)
            self.contarPalabras(i)
            self.contarLineas(i)

            
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
