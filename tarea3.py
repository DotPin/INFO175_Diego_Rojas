#!/usr/bin/python
# -*- coding: utf-8 -*-

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