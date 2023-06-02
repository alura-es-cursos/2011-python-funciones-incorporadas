import horca
import adivinanza

print("****************************************")
print("***********Juegos de Python*************")
print("****************************************")
print("(1) Horca (2) Adivinanza")
juego = int(input("Selecciona el juego que deseas: "))

if juego == 1:
  print("Juego de la horca")
  horca.jugar()
elif juego == 2:
  print("Juego de adivinar el número")
  adivinanza.jugar()
