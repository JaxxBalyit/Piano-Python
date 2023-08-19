"""
Piano en Python
Autores:
    Chávez Zepeda José Emmanuel
    Rendón Lira Oswaldo
    Gutiérrez D'esesarte Ángel Miguel

Este código nos sirve para mostrar la implementación de lo aprendido
en la UDA de POOE, implementando un proyecto final de nuestra propia
elección e interés, utilizando clases e interfaces gráficas en Python
"""

import tkinter as tk
import tkinter.font as tkFont
import pygame


class Tecla:
    __nota = None
    __frec = None
    __tipo = None
    __boton = None

    # Métodos Getters
    def getFrec(self):
        return self.__frec

    def getNota(self):
        return self.__nota

    def getTipo(self):
        return self.__tipo

    # Métodos Setters
    def setFrec(self, Frec):
        self.__frec = Frec

    def setNota(self, Nota):
        self.__nota = Nota

    def setTipo(self, Tipo):
        self.__tipo = Tipo

    def printNota(self, Nota, L):
        L.config(text=Nota)

    def crearTeclaButton(self, root, Nota, Comando, Fuente, Tipo, x, y, w, h):
        self.__boton = tk.Button(root, text=Nota, command=Comando, fg=Fuente, bg=Tipo).place(
            relx=x, rely=y, relwidth=w, relheight=h)


root = tk.Tk()
root.title("PIANO")
root.config(bg="black")
pygame.init()

fontStyle = tkFont.Font(size=20)
fontStyle2 = tkFont.Font(size=15)

l1 = tk.Label(root, text="YAMAHA", font=fontStyle)
l1.place(relx=.42, rely=.10)
l1.config(fg="gold", bg="black")

l3 = tk.Label(root, text="La tecla que usted esta tocando es:")
l3.place(relx=.10, rely=.10)
l3.config(fg="gold", bg="black")
l4 = tk.Label(root, text="Music", font=fontStyle2)
l4.place(relx=.185, rely=.15)

frecArray = [261, 293, 329, 349, 392, 440,
             493, 522, 553, 586, 621, 658, 697, 738]
frecSusArray = [277, 311, 369, 415, 466, 505, 537, 564, 602, 637]
noteArray = ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si',
             'Do1', 'Re1', 'Mi1', 'Fa1', 'Sol1', 'La1', 'Si1']
noteSusArray = ['Do#', 'Re#', 'Fa#', 'Sol#',
                'La#', 'Do#1', 'Re#1', 'Fa#1', 'Sol#1', 'La#1']

# Creacion de teclas blancas
tb1 = Tecla()
tb2 = Tecla()
tb3 = Tecla()
tb4 = Tecla()
tb5 = Tecla()
tb6 = Tecla()
tb7 = Tecla()
tb8 = Tecla()
tb9 = Tecla()
tb10 = Tecla()
tb11 = Tecla()
tb12 = Tecla()
tb13 = Tecla()
tb14 = Tecla()


# Creacion de teclas negras
tn1 = Tecla()
tn2 = Tecla()
tn3 = Tecla()
tn4 = Tecla()
tn5 = Tecla()
tn6 = Tecla()
tn7 = Tecla()
tn8 = Tecla()
tn9 = Tecla()
tn10 = Tecla()

# Asignación de frecuencia, nota y tipo a la teclas blancas
tecBlancas = [tb1, tb2, tb3, tb4, tb5, tb6,
              tb7, tb8, tb9, tb10, tb11, tb12, tb13, tb14]
change = 0

for tb in tecBlancas:
    tb.setFrec(frecArray[change])
    tb.setNota(noteArray[change])
    tb.setTipo("white")
    change = change + 1

# Asignación de frecuencia, nota y tipo a la teclas negras
xArray = [.06, .12, .18, .24, .30, .36, .42, .48, .54, .60, .66, .72, .78, .84]
tecNegras = [tn1, tn2, tn3, tn4, tn5, tn6, tn7, tn8, tn9, tn10]
change = 0

for tb in tecNegras:
    tb.setFrec(frecSusArray[change])
    tb.setNota(noteSusArray[change])
    tb.setTipo("black")
    change = change + 1
yArray = [.09, .15, .27, .33, .39, .51, .57, .69, .75, 0.81]


# FUNCION PARA TECLAS BLANCAS
def printTb1():
    l4.config(text=tb1.getNota())
    sound = pygame.mixer.Sound(r".\DO.wav")
    sound.play()


def printTb2():
    l4.config(text=tb2.getNota())
    sound = pygame.mixer.Sound(r".\RE.wav")
    sound.play()


def printTb3():
    l4.config(text=tb3.getNota())
    sound = pygame.mixer.Sound(r".\MI.wav")
    sound.play()


def printTb4():
    l4.config(text=tb4.getNota())
    sound = pygame.mixer.Sound(r".\FA.wav")
    sound.play()


def printTb5():
    l4.config(text=tb5.getNota())
    sound = pygame.mixer.Sound(r".\SOL.wav")
    sound.play()


def printTb6():
    l4.config(text=tb6.getNota())
    sound = pygame.mixer.Sound(r".\LA.wav")
    sound.play()


def printTb7():
    l4.config(text=tb7.getNota())
    sound = pygame.mixer.Sound(r".\SI.wav")
    sound.play()


def printTb8():
    l4.config(text=tb8.getNota())
    sound = pygame.mixer.Sound(r".\DO1.wav")
    sound.play()


def printTb9():
    l4.config(text=tb9.getNota())
    sound = pygame.mixer.Sound(r".\RE1.wav")
    sound.play()


def printTb10():
    l4.config(text=tb10.getNota())
    sound = pygame.mixer.Sound(r".\MI1.wav")
    sound.play()


def printTb11():
    l4.config(text=tb11.getNota())
    sound = pygame.mixer.Sound(r".\FA1.wav")
    sound.play()


def printTb12():
    l4.config(text=tb12.getNota())
    sound = pygame.mixer.Sound(r".\SOL1.wav")
    sound.play()


def printTb13():
    l4.config(text=tb13.getNota())
    sound = pygame.mixer.Sound(r".\LA1.wav")
    sound.play()


def printTb14():
    l4.config(text=tb14.getNota())
    sound = pygame.mixer.Sound(r".\SI1.wav")
    sound.play()


# FUNCION PARA TECLAS NEGRAS
def printTn1():
    l4.config(text=tn1.getNota())
    sound = pygame.mixer.Sound(r".\DO#.wav")
    sound.play()


def printTn2():
    l4.config(text=tn2.getNota())
    sound = pygame.mixer.Sound(r".\RE#.wav")
    sound.play()


def printTn3():
    l4.config(text=tn3.getNota())
    sound = pygame.mixer.Sound(r".\FA#.wav")
    sound.play()


def printTn4():
    l4.config(text=tn4.getNota())
    sound = pygame.mixer.Sound(r".\SOL#.wav")
    sound.play()


def printTn5():
    l4.config(text=tn5.getNota())
    sound = pygame.mixer.Sound(r".\LA#.wav")
    sound.play()


def printTn6():
    l4.config(text=tn6.getNota())
    sound = pygame.mixer.Sound(r".\DO#1.wav")
    sound.play()


def printTn7():
    l4.config(text=tn7.getNota())
    sound = pygame.mixer.Sound(r".\RE#1.wav")
    sound.play()


def printTn8():
    l4.config(text=tn8.getNota())
    sound = pygame.mixer.Sound(r".\FA#1.wav")
    sound.play()


def printTn9():
    l4.config(text=tn9.getNota())
    sound = pygame.mixer.Sound(r".\SOL#1.wav")
    sound.play()


def printTn10():
    l4.config(text=tn10.getNota())
    sound = pygame.mixer.Sound(r".\LA#1.wav")
    sound.play()


# Creacion de botones de teclas negras
tb1.crearTeclaButton(root, tb1.getNota(), printTb1, "black",
                     tb1.getTipo(), xArray[0], .35, .10, .50)
tb2.crearTeclaButton(root, tb2.getNota(), printTb2, "black",
                     tb2.getTipo(), xArray[1], .35, .10, .50)
tb3.crearTeclaButton(root, tb3.getNota(), printTb3, "black",
                     tb3.getTipo(), xArray[2], .35, .10, .50)
tb4.crearTeclaButton(root, tb4.getNota(), printTb4, "black",
                     tb4.getTipo(), xArray[3], .35, .10, .50)
tb5.crearTeclaButton(root, tb5.getNota(), printTb5, "black",
                     tb5.getTipo(), xArray[4], .35, .10, .50)
tb6.crearTeclaButton(root, tb6.getNota(), printTb6, "black",
                     tb6.getTipo(), xArray[5], .35, .10, .50)
tb7.crearTeclaButton(root, tb7.getNota(), printTb7, "black",
                     tb7.getTipo(), xArray[6], .35, .10, .50)
tb8.crearTeclaButton(root, tb8.getNota(), printTb8, "black",
                     tb1.getTipo(), xArray[7], .35, .10, .50)
tb9.crearTeclaButton(root, tb9.getNota(), printTb9, "black",
                     tb2.getTipo(), xArray[8], .35, .10, .50)
tb10.crearTeclaButton(root, tb10.getNota(), printTb10,
                      "black", tb3.getTipo(), xArray[9], .35, .10, .50)
tb11.crearTeclaButton(root, tb11.getNota(), printTb11,
                      "black", tb4.getTipo(), xArray[10], .35, .10, .50)
tb12.crearTeclaButton(root, tb12.getNota(), printTb12,
                      "black", tb5.getTipo(), xArray[11], .35, .10, .50)
tb13.crearTeclaButton(root, tb13.getNota(), printTb13,
                      "black", tb6.getTipo(), xArray[12], .35, .10, .50)
tb14.crearTeclaButton(root, tb14.getNota(), printTb14,
                      "black", tb7.getTipo(), xArray[13], .35, .10, .50)

# Creacion botones de teclas negras
tn1.crearTeclaButton(root, tn1.getNota(), printTn1, "white",
                     tn1.getTipo(), yArray[0], .35, .05, .25)
tn2.crearTeclaButton(root, tn2.getNota(), printTn2, "white",
                     tn2.getTipo(), yArray[1], .35, .05, .25)
tn3.crearTeclaButton(root, tn3.getNota(), printTn3, "white",
                     tn3.getTipo(), yArray[2], .35, .05, .25)
tn4.crearTeclaButton(root, tn4.getNota(), printTn4, "white",
                     tn4.getTipo(), yArray[3], .35, .05, .25)
tn5.crearTeclaButton(root, tn5.getNota(), printTn5, "white",
                     tn5.getTipo(), yArray[4], .35, .05, .25)
tn6.crearTeclaButton(root, tn6.getNota(), printTn6, "white",
                     tn6.getTipo(), yArray[5], .35, .05, .25)
tn7.crearTeclaButton(root, tn7.getNota(), printTn7, "white",
                     tn7.getTipo(), yArray[6], .35, .05, .25)
tn8.crearTeclaButton(root, tn8.getNota(), printTn8, "white",
                     tn8.getTipo(), yArray[7], .35, .05, .25)
tn9.crearTeclaButton(root, tn9.getNota(), printTn9, "white",
                     tn9.getTipo(), yArray[8], .35, .05, .25)
tn10.crearTeclaButton(root, tn10.getNota(), printTn10,
                      "white", tn10.getTipo(), yArray[9], .35, .05, .25)

root.geometry("1200x750")
root.mainloop()
