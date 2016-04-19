def fibonacci(x):
	if((x==1 or x==2)):
		return 1
	else:
		return(fibonacci(x-1)+fibonacci(x-2))

x = int(input("Ingrese el numero mayor a 0 para comenzar la serie fibonacci: "))
print fibonacci(x)
