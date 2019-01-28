from tkinter import*

raiz=Tk()
mFrame=Frame(raiz,width=1200,height=600)
mFrame.pack()

Operaciones=""
BorrarPantalla=False
Resultado=0 #ahise va guardar todo uwu
#cuadro de texto
numeroPantalla=StringVar()
cuadroN=Entry(mFrame,textvariable=numeroPantalla)#se asocia conla pantalla
cuadroN.grid(row=1,column=1,padx=10,pady=10,columnspan=5)#columnspan para que salgan bien los botones ya que ocupa las 4 espacios
cuadroN.config(background="black",justify="center", fg="pink")
#teclado funciones

def numeroPulsado(num):
    global Operaciones
    global BorrarPantalla

    if BorrarPantalla != False:
        numeroPantalla.set(num)
        BorrarPantalla = False#BOrrar la pantalla

    else:

        numeroPantalla.set(numeroPantalla.get() + num)


def borrar(num):
    global Operaciones
    global BorrarPantalla
    global Resultado
    Resultado =int(num)
    Operaciones="borrar"
    BorrarPantalla = True
    numeroPantalla.set(Resultado)
    #borar=true


def Sumar(num):
    global Operaciones
    global Resultado
    global BorrarPantalla

    Resultado+=int(num)#para que lo tome como numerp
    Operaciones="sumar"
    BorrarPantalla=True
    numeroPantalla.set(Resultado)#PARA QUE MUESTRE EN LA PANTALLA EL RESULTADO


num1=0

contador_resta=0
def Restar(num):
    global Operaciones
    global Resultado
    global BorrarPantalla
    global num1
    global contador_resta

    if contador_resta == 0:

        num1 = int(num)

        Resultado= num1

    else:

        if contador_resta == 1:

            Resultado = num1 - int(num)

        else:

            resultado = int(Resultado) - int(num)

        numeroPantalla.set(Resultado)

        resultado = numeroPantalla.get()

    contador_resta = contador_resta + 1

    Operaciones = "resta"

    BorrarPantalla= True

contador_multi=0

def Multi(num):
    global Operaciones
    global Resultado
    global BorrarPantalla
    global num1
    global contador_multi
    if contador_multi == 0:
        num1 = int(num)

        Resultado = num1

    else:

        if contador_multi == 1:

            Resultado = num1 * int(num)

        else:

            Resultado = int(Resultado) * int(num)

        numeroPantalla.set(Resultado)

        Resultado = numeroPantalla.get()

    contador_multi = contador_multi + 1

    Operaciones = "multiplicacion"

    BorrarPantalla = True

contador_divi=0

def Divi(num):
    global Operaciones
    global Resultado
    global BorrarPantalla
    global num1
    global contador_divi
    if contador_divi == 0:
        num1 = int(num)

        resultado = num1

    else:

        if contador_multi == 1:

            Resultado = num1 / int(num)

        else:

            Resultado = int(Resultado) / int(num)

        numeroPantalla.set(Resultado)

        Resultado = numeroPantalla.get()

    contador_divi = contador_divi + 1

    Operaciones = "division"

    BorrarPantalla = True


#el resultado :
def ELRESULTADO():
    global Resultado
    global Operaciones
    global contador_divi
    global contador_multi
    global contador_resta


    if Operaciones=="sumar":
       numeroPantalla.set(Resultado+int(numeroPantalla.get()))#COGE LO QUE YA LLEVA SUMAO Y LE DA EL RESULTADO COMPLETO
       Resultado=0#PARA QUE AL FINAL SE QUEDE EN CERO LA VARIABLE

    elif Operaciones=="restar":
        numeroPantalla.set( int(Resultado)-int(numeroPantalla.get()))  # COGE LO QUE YA LLEVA SUMAO Y LE DA EL RESULTADO COMPLETO
        Resultado = 0  # PARA QUE AL FINAL SE QUEDE EN CERO LA VARIABLE
        contador_resta=0

    elif Operaciones == "mltiplicacion":
        numeroPantalla.set( int(Resultado)*int(numeroPantalla.get()))  # COGE LO QUE YA LLEVA SUMAO Y LE DA EL RESULTADO COMPLETO
        Resultado = 0  # PARA QUE AL FINAL SE QUEDE EN CERO LA VARIABLE
        contador_multi = 0
    elif Operaciones == "division":
        numeroPantalla.set( int(Resultado)/int(numeroPantalla.get()))  # COGE LO QUE YA LLEVA SUMAO Y LE DA EL RESULTADO COMPLETO
        Resultado = 0  # PARA QUE AL FINAL SE QUEDE EN CERO LA VARIABLE
        contador_divi = 0
    elif Operaciones=="borrar":
        numeroPantalla.set("")
        Resultado=0

    #fila1

B7=Button(mFrame,text="7",width=3,command=lambda:numeroPulsado("7"))
B7.grid(row=2,column=1)
B8=Button(mFrame,text="8",width=3,command=lambda:numeroPulsado("8"))
B8.grid(row=2,column=2)
B9=Button(mFrame,text="9",width=3,command=lambda:numeroPulsado("9"))
B9.grid(row=2,column=3)
BD=Button(mFrame,text="/",width=3, command=lambda:Divi(numeroPantalla.get()))
BD.grid(row=2,column=4)
BB=Button(mFrame,text="C",width=3, command=lambda:borrar(numeroPantalla.get()))
BB.grid(row=2,column=5)

#fila 2


B4=Button(mFrame,text="4",width=3,command=lambda:numeroPulsado("4"))#lambda pra que no aparezca error
B4.grid(row=3,column=1)
B5=Button(mFrame,text="5",width=3,command=lambda:numeroPulsado("5"))
B5.grid(row=3,column=2)
B6=Button(mFrame,text="6",width=3,command=lambda:numeroPulsado("6"))
B6.grid(row=3,column=3)
BM=Button(mFrame,text="X",width=3, command=lambda:Multi(numeroPantalla.get()))
BM.grid(row=3,column=4)


#FILA3

B1=Button(mFrame,text="1",width=3,command=lambda :numeroPulsado("1"))
B1.grid(row=4,column=1)
B2=Button(mFrame,text="2",width=3,command=lambda :numeroPulsado("2"))
B2.grid(row=4,column=2)
B3=Button(mFrame,text="3",width=3,command=lambda :numeroPulsado("3"))
B3.grid(row=4,column=3)
BR=Button(mFrame,text="-",width=3 , command=lambda: Restar(numeroPantalla.get()))
BR.grid(row=4,column=4)

#FILA4

B0=Button(mFrame,text="0",width=3,command=lambda :numeroPulsado("0"))
B0.grid(row=5,column=1)
BP=Button(mFrame,text=".",width=3,command=lambda :numeroPulsado("."))
BP.grid(row=5,column=2)
BI=Button(mFrame,text="=",width=3,command=lambda:ELRESULTADO())
BI.grid(row=5,column=3)
BS=Button(mFrame,text="+",width=3, command=lambda: Sumar(numeroPantalla.get()) )#get para pasar el numero en pantalla
BS.grid(row=5,column=4)












raiz.mainloop()