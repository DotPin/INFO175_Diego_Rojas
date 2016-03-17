#!/usr/bin/python
# -*- coding: utf-8 -*-

def ordenamiento(txt):
  txt2 = txt.split(",")
  txt2.sort()
  return txt2


if __name__ == "__main__":
  algo =  raw_input("Ingrese palabras saparado por comas: ")
  print "Palabras ordenadas por abecedario: ",ordenamiento(algo)
  