#-*- coding: utf-8 -*-

#archivo python de prueba

def comparar(x,y):
	if x>y return x
	elif y>x return y
	else	return "Iguales"

 if __name__ == "__main__":
	x = input("Ingrese un numero entero")
	y = input("Ingrese un numero entero")
	print (comparar(x,y))
