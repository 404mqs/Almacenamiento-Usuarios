from time import sleep
from prettytable import PrettyTable

def separador(value):
    print(f"\n" * value)

nombres = []
edades = []
apellidos = []

agregando = True

while agregando:

    nombre = input("[?] Ingrese Nombre: ")
    while len(nombre)-1 < 2:
        print("[!] ERROR. El nombre debe tener mas de dos caracteres. ")
        nombre = input("[?] Ingresar Nombre ")

    ###############################

    apellido = input("[?] Ingresar Apellido: ")
    while len(apellido)-1 < 2:
        print("[!] ERROR. El apellido debe tener mas de dos caracteres. ")
        apellido = input("[?] Ingresar Apellido: ")

    ###############################

    edad = int(input("[?] Ingrese Edad: "))
    while edad <= 0:
        print("[!] ERROR. La EDAD debe ser a partir de 0.")
        edad = int(input("[?] Ingrese Edad: "))

    ###############################
    
    if len(nombre)-1 > 2:      
        nombres.append(nombre)

    if len(apellido)-1 > 2:
        apellidos.append(apellido)

    if edad >= 0:
        edades.append(edad)

    agregando = False

    separador(1)
    seleccion = int(input(f"[?] Quiere agregar mas personas a la tabla? \n[+] 1: Si \n[+] 2: No \n"))
    
    while seleccion > 2 or seleccion < 1:
        separador(1)
        print("[-] No se entendio su eleccion. Seleccione un numero")
        seleccion = int(input(f"[?] Quiere agregar mas personas a la tabla? \n[+] 1: Si \n[+] 2: No \n"))
        
    if seleccion == 1:
        agregando = True

    elif seleccion == 2:
        print("[!] Procesando Informacion...")
        sleep(2)
    
    while seleccion > 2 or seleccion < 1:
        separador(1)
        print("[-] No se entendio su eleccion. Seleccione un numero")
        seleccion = int(input(f"[?] Quiere agregar mas personas a la tabla? \n [+] 1: Si \n [+] 2: No \n"))

    table = PrettyTable(["Nombre", "Apellido", "Edad"])

for i in range(len(nombres)):

    table.add_row([nombres[i], apellidos[i], edades[i]])

separador(20)
print(table)
input("")



