import json

print("**************************************************")
print("*                   Bienvenido                   *")
print("**************************************************")


print("Cual es tu ROL en CAMPUSLANDS")
print("\n1. Coordinador\t 2. Trainer")
print(" ")
Rol = int(input("------>"))

if Rol == 1:
    print("Bienvenido al coordinador") 
    print(" ")
elif Rol == 2:
    print("Bienvenido al Trainer")
    print(" ")