#!/usr/bin/python
# -*- coding: utf-8 -*-


#Ingresa una palabra por cada enter que presione infinitamente, hasta que registra un blanco
#mostrando la palabra compuesta por cada ingreso en orden


def interlinea():
  bol = True
  a = []
  while bol:
    b = raw_input("Ingrese cada palabra con un enter, y termine el programa registrando un blanco: ")
    if b == "":
      bol = False
    else:
      a.append(b)
  return a


if __name__ == "__main__":
  print ("Palabra obtenida: ",interlinea())


#Creado por hackerter
#Máquina EVA01
