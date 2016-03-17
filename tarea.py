#-*- coding: utf-8 -*-

#archivo python que compara 2 numeros si son mayor, menor e iguales

def comparar(x,y):
	if x>y:
	  s1 = 'Mayor '+str(x)
	  s2 = 'Menor '+str(y)
	  print ("!")
	elif y>x:
	  s1 = 'Mayor '+ str(y)
	  s2 = 'Menor '+ str(x)
	  print ("#")
	else:	
	  return "Iguales"
	return (s1+' Y '+s2)
	

if __name__ == "__main__":
	x = input("Ingrese primer numero entero: ")
	y = input("Ingrese segundo numero entero: ")
	print ("Resultado "+ comparar(x,y))
