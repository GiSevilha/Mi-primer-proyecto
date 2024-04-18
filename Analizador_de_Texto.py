print("Introduzca el texto o frase que quieras:")
texto = str(input("")).lower().strip()
letras = []

print()
print("CANTIDAD DE LETRAS")
letra1 = letras.append(input("Letra 1: ").lower())
letra2 = letras.append(input("Letra 2: ").lower())
letra3 = letras.append(input("Letra 3: ").lower())

print()
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"A letra '{letras[0]}' aparece {cantidad_letras1} vezes no texto.")
print(f"A letra '{letras[1]}' aparece {cantidad_letras2} vezes no texto.")
print(f"A letra '{letras[2]}' aparece {cantidad_letras3} vezes no texto.")

print()
print("CANTIDAD DE PALABRAS")
palabras = texto.split()
print(f"El texto contiene {len(palabras)} palabras en total.")

print()
print("LETRAS DE INICIO Y FIN")
print(f"La primera letra que aparece en el texto es la {texto[0].upper()}")
print(f"La última letra que aparece en el texto es la {texto[-1].upper()}")

print()
print("TEXTO INVERTIDO")
palabras.reverse()
texto_invertido = " ".join(palabras)
print(f"O texto invertido ficaria assim: {texto_invertido}")

print()
print("¿LA PALABRA PYTHON APARECE O NO EN EL TEXTO?")
comprobar_palabra = "python" in palabras
if comprobar_palabra == True:
    print(f"La palabra Python aparece en el texto.")
else:
    print(f"La palabra Python no aparece en el texto.")