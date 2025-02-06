#ingresar dato a convertir
temperatura = input("Ingrese temperatura a convertir: \n")
escala = input("Qué escala es: Celcius (C) o Fahrenheit (F): \n")
escala_capital = escala.capitalize()
if escala_capital == "C":
    temperatura_a_convertir=int(temperatura)
    print(f"La temperatura en Grados Farenheit es:{((temperatura_a_convertir)*(9/5))+32}")
elif escala_capital == "F":
    temperatura_a_convertir=int(temperatura)
    print(f"La temperatura en Grados Celcius es:{(temperatura_a_convertir-32)*(5/9)}")
else:
    print("Ingrese la escala correcta: C ó F")
