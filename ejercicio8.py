#!/usr/bin/python
# -*- coding: utf-8 -*-

#escribir una funcion que se llame encrypt en python que reciba como entrada una palabra y a cada caracter (solo letras) lo modifique por la letra que esta en N posiciones de distancia en el abecedario. Se debe poder especificar el numero de N de posiciones que se desea correr cada caracter (parametro de la funcion). puede omitir la ñ, extienda la funcion para que soporte frases, usar modulo string de python, string.ascii_lowercase.

import string

def encrypt(palabra, saltos):
  abcd = string.ascii_lowercase
  palabra_encriptada = ""
  for char in palabra:
    if char != " ":
      index = (abcd.index(char.lower()) + saltos) % len(abcd)
      palabra_encriptada += abcd[index]
    else:
      palabra_encriptada += char
  return palabra_encriptada




if __name__ == "__main__":
  palabra = raw_input("Ingrese la palabra que desea encriptar: ")
  saltos = input("Inrgese el numero de saltos: ")
  print("Palabra encriptada",encrypt(palabra,saltos))