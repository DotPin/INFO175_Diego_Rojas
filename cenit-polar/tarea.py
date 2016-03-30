#!/usr/bin/python
# -*- coding: utf-8 -*-


#Tarea de codificación con interfaz gráfica llamada Cenit-Polar, en la que solicita palabra por medio de un TextBox
#despues escoge mediante CheckButton opcion a codificar y realiza el trabajo dependiendo de lo que quiere.

from Tkinter import *
import string

class apl(Tk):
  
    def __init__(self,parent):
      Tk.__init__(self,parent)
      self.parent = parent
      self.iniciar()
#DR     
    def iniciar(self):
      self.title("Encriptador")
      
      titulo = Label(self, text="Ingrese la Frase a Encriptar")
      titulo.place(x = 20, y = 50)
      
      def encriptacion():
	acu = StringVar()
	si = IntVar()
	print("Presionado")
	if int(v.get()) == 1:
	  acu = str(txt.get())
	  cenit(acu)
	  print("pasa1")
	elif int(v.get()) == 2:
	  acu = str(txt.get())
	  si = int(txt2.get())
	  print("frase: ",acu)
	  print("salto de cenit: ",si)
	  cesar(acu,si)
	  print("pasa2")
	print("FInaliza")
      
      resultado = StringVar()
      resultado = (" Texto resultante ")
#IO      
      def cenit(frase): 			#metodo de encriptación cenit-polar
	tx = "cenit"
	tx2 = "polar"
	frase = frase.lower()
	final=''
	print("Frase de parámetro cenit: ",frase)
	for texto in frase:
	  if texto == "c": final+=tx2[0]
	  elif texto == "e": final+=tx2[1]
	  elif texto == "n": final+=tx2[2]
	  elif texto == "i": final+=tx2[3]
	  elif texto == "t": final+=tx2[4]
	  elif texto == "p": final+=tx[0]
	  elif texto == "o": final+=tx[1]
	  elif texto == "l": final+=tx[2]
	  elif texto == "a": final+=tx[3]
	  elif texto == "r": final+=tx[4]
	  else: final += texto
	rst2.config(text=final)
#EJ
      def cesar(frase, jump):	#método encriptación cesar con parámetro word = palabra enviada, jump = numero de saltos
	try: 
	  if jump < 0 :
	    tkMessageBox.showwarning("Importante","Debe ingresar numeros mayores que 0")
	  else:
	    print("Frase de parámetro cesar: ",frase)
	    r = string.ascii_lowercase
	    palabra = ""
	    for char in frase:
	      if char != " ":
		i = (r.index(char.lower()) + jump) % len(r)
		palabra += r[i]
	      else:
		palabra += char
	    rst2.config(text=palabra)
	except(NameError,ValueError): 
	  tkMessageBox.showerror("Importante","Ingrese valores numericos")
      
      txt = StringVar()
      entrada = Entry(self, textvariable = txt, bg = "white")
      entrada.place(x = 15 , y = 80, width = 470, height = 200)
      
      
      opcion = Label(self, text="Seleccione el tipo de encriptación:")
      opcion.place(x=20, y=310)
#GA      
      def validador():			#activador y desactivador de eventos botones y cuadros de texto
	c1.config(state=DISABLED)
	c2.config(state=DISABLED)
	entrada.config(state=DISABLED)
	print("Valor del Radiobutton: ", str(v.get()))
	if int(v.get()) == 2:
	  entrada2.config(state=NORMAL)
      
      v = IntVar()
      c1 = Radiobutton(self, text="Cenit-Polar", variable=v, value=1,command=validador)
      c1.place(x = 25, y = 330)
      
      c2 = Radiobutton(self, text="Cesar", variable=v, value=2,command=validador)
      c2.place(x = 250, y = 330)
      
      
      enc = Label(self, text="Seleccione el salto para la encriptacion cesar:")
      enc.place(x = 20 , y = 370)
      
      txt2 = IntVar()		# texto debe ir como parámetro en método cesar
      entrada2 = Entry(self, textvariable = txt2, bg = "white",state=DISABLED)
      entrada2.place(x = 310 , y = 367, width = 25, height = 25)
      
      
      rst = Label(self, text="Resultado:")
      rst.place( x = 20 , y = 390) 
      
      
      rst2 = Label(self, text=resultado, bg = "white")  #Label resultante a modificar con variable rst2
      rst2.place(x = 20 , y = 410, width = 470, height = 200)
      
      bencriptar = Button(self, text="Encriptar", command=encriptacion)			#comando que realiza acción de encriptación
      bencriptar.place(x = 350, y = 625, width=120 , height= 50)
#OS      
      def salir():
	self.quit()
      
      bcerrar = Button(self, text="Cerrar", command = salir )
      bcerrar.place(x = 20, y = 650, width= 120, height=25)
    
      

if __name__ == "__main__":
  tp = apl(None)
  tp.geometry("500x700")
  tp.resizable(False,False)
  tp.mainloop()
  
  
  
#Trabajo Realizado por Hackerter
#Diego Rojas Asenjo
  
  
  
  
  
  
  
  