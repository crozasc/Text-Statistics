
class texto:
    def __init__(self, nombre):
        contenido = open(nombre, "r")
        lineas = 0
        palabras = 0
        palabrasNoRepetidas = 0
        caracteresConEspacio = 0
        caracteresSinEspacio = 0

    def estadisticasTexto(self):
        for i in self.contenido:
            self.contarCaracteresConEspacio(i)
            self.contarCaracteresSinEspacio(i)
            self.contarPalabras(i)

            
    def contarCaracteresConEspacio(self, i):
        if(i!=""): self.caracteresConEspacio+= 1

    def contarCaracteresSinEspacio(self, i):
        if(i!=" "): 
            self.caracteresConEspacio+= 1
        elif (i==" "):
            self.caracteresConEspacio-= 1
    
    def contarPalabras(self, i):
        if(i==" "):
            self.palabras+=1
    
    def contarLineas(self, i):
        if(i=="\n"):
            self.palabras+=1





