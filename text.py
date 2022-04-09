"""This is the text module.
This module contains the text class and its methods."""
from dataclasses import dataclass

@dataclass
class text:
    """Class for keeping track of a book and it's statistics"""
    def __init__(self, name):
        self.name = name
        self.lines = 0
        self.words = 0
        self.unicWords = set([])
        self.charactersWithSpace = 1
        self.charactersWithoutSpace = 1
        
    def statisticsText(self):
        """Calls the fuctions to count the statistics of the text and print them"""
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
        """Count the characters counting spaces
        i -- Line of text"""
        for j in i:
            if(j!=""): self.charactersWithSpace+= 1
        self.charactersWithSpace=self.charactersWithSpace-1

    def countCharactersWithoutSpace(self, i):
        """Count the characters witouth counting spaces
        i -- Line of text"""
        for j in i:
            if(j!=" "): 
                self.charactersWithoutSpace+= 1
        self.charactersWithoutSpace=self.charactersWithoutSpace-1
    
    def countWords(self, i):
        """Count the words
        i -- Line of text"""
        for j in i:
            if(j==" "):self.words+=1
        self.words=self.words+1
    
    def countLines(self, i):
        """Count the lines
        i -- Line of text"""
        self.lines+=1

    def countUnicWords(self, i):
        """Count the unics words
        i -- Line of text"""
        aux=i.split()
        aux=set(aux)
        self.unicWords.update(aux)

    def printStatistics(self):
        """Print all the statistics variables"""
        print("Lines:",self.lines)
        print("Words:",self.words)
        print("Unic Words:", len(self.unicWords))
        print("Characters counting spaces:",self.charactersWithSpace)
        print("Characters without counting spaces:",self.charactersWithoutSpace)

    def searchWord(self, word):
        """Search for a word and count the times it's repeated
        word -- the word to search
        timesRepeated -- the number of times the word is repeated"""
        timesRepeated = 0
        content=open(self.name,"r", encoding="utf-8")
        for i in content:
            aux=i.replace(";"," ").replace(","," ").replace("-"," ").replace("|"," ").replace("/"," ").split()
            for j in aux:
                if(j==word): timesRepeated+=1
        if(timesRepeated==0):print("The word \"", word, "\" is not repeated")
        else:print("The word \"", word, "\" is repeated", timesRepeated, "times")

    def reemplazarPalabra(self, word, replace):
        """Replace a selected word of the book
        word -- the word to replaced
        replace -- the replace word"""
        initialContent=open(self.name,"r", encoding="utf-8")
        initialContent=initialContent.read()
        initialContent=initialContent.replace(word,replace)
        finalContent=open(self.name,"w", encoding="utf-8")
        finalContent.write(initialContent)
