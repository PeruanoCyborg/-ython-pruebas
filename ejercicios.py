nombre = input("¿Cuál es tu nombre?")
edad = input("¿Cuántos años tienes?")

edad_el_proximo_ano = int(edad) + 1

print("Hola", nombre, "¡en un año tendrás", edad_el_proximo_ano, " años!")



word = input("Ingresa una palabra: ")
vocales = ["a", "e", "i", "o", "u"]
count =0
for leter in word:
    if leter in vocales:
        count += 1
print("numero de vocales:", count)   


x = 5
x = x + 2
x *= 3
print(x)
