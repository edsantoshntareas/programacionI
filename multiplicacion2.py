for indice in range (32,36):
	print("Tabla del ", indice)
	for elemento in range(1,11):
		resultado = indice * elemento
		print("{2} x {0} = {1}".format(elemento,resultado,indice))
	print()

print()
print("Otros Valores")
print()

tablas= [21, 34, 54, 65, 76]
for indice in tablas:
	print("Tabla del ", indice)
	for elemento in range(1,11):
		resultado = indice * elemento
		print("{2} x {0} = {1}".format(elemento,resultado,indice))
	print()