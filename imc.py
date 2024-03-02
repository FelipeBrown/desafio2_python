w = float(input("Ingresa tu peso en kilogramos: "))
h = float(input("ingresa tu altura en metros: "))
    
imc = w / (h**2)
print (f"tu imc es: {imc}")

if imc < 18.5:
    print("Bajo Peso")
elif 18.5 <= imc < 25:
    print("Peso Adecuado")
elif 25 <= imc < 30:
    print("Sobrepeso")
elif 30 <= imc < 35:
    print("Obesidad grado 1")
elif 35 <= imc < 40:
    print("Obesidad grado 2")
else:
    print("Obesidad grado 3")