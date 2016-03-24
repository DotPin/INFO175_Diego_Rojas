#!/usr/bin/python
# -*- coding: utf-8 -*-

#escribir una funcion que reciba una variable entera size y retorne en una lista 
#de todos los numeros que estan entre 1 y size que sean multiplos de 3 y 7

def multiplos(size):
    pl = []
    for a in range(1,size):
      if (size % a == 0 and size % 3 == 0):
	pl.append(a)
    return pl

if __name__ == "__main__":
  size = input("Ingrese un numero entero mayor a 1: ")
  while size <= 1:
    print("Error el numero ingresado es bajo")
    size = input("Ingrese nuevamente un numero entero mayor a 1: ")
  print("Lista de multiplos de su numero-> ",multiplos(size))
      
