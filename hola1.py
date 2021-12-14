LetrasLista=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Letrasrara=['m','f','x','r','p','q','d','c','h','2','a','n','t','6','b','w','3','k','9','l','i','5','$','e','g','v']

condicion = 0



while condicion < 1:

    entrada=input("Ingresar palabra.\n")
    valor_letras = entrada.lower()

    Lista_letras =[]

    for x in valor_letras:
        primeraletra=x
        Lista_letras.append(primeraletra)

    Total_letras = len(Lista_letras)


    ListaResuelta=[]
    contador =0
    for var in range(0,Total_letras):
        contador=contador+1
        valorletra = Lista_letras[contador-1]
        #print("--------------------------------------------------------------------")
        valorbuscado = Letrasrara.index(str( valorletra))
        resultado=LetrasLista[valorbuscado]
        ListaResuelta.append(resultado)
        listanueva=''.join(map(str,ListaResuelta))
    print("--------------------------->",listanueva)




    
    
        


