from texto import*

def menu2(option):
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
    ans=True
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


menu()
