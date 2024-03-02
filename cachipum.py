import random
import sys

usuario = sys.argv[1]

opciones = ["piedra","papel","tijera"]

npc = random.choice(opciones)

print(f"tu jugaste {usuario}")
print(f"computador jugó {npc}")

if usuario in opciones:
    if usuario == npc:
        print ("EMPATE")
    elif((usuario == "piedra" and npc == "tijera") or
         (usuario == "papel" and npc == "piedra") or
         (usuario == "tijera" and npc == "papel")):
        print("GANASTE")
    else:
        print("PERDISTE")
else:
    print("Argumento inválido: Debe ser piedra, papel o tijera.")