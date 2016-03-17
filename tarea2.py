#!/usr/bin/python
# -*- coding: utf-8 -*-

#Programa donde toma un texto ingresado y separado por comas
#donde se espera que el texto sea separado por las comas en otro arreglo
#y ordenado por abecedario

def ordenamiento(txt):
  txt2 = txt.split(",")
  txt2.sort()
  return txt2


if __name__ == "__main__":
  algo =  raw_input("Ingrese palabras saparado por comas: ")
  print "Palabras ordenadas por abecedario: ",ordenamiento(algo)
  
#Creado por hackerter  
#Máquina EVA01

