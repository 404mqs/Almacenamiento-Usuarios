#Importes

from time import sleep
from prettytable import PrettyTable
from datetime import date


#Funciones

def separador(value):
    return print(f"\n" * value)

def calcular_edad(año, mes, dia):
    today = date.today()
    return(today.year - año - ((today.month, today.day) < (mes, dia)))

#Iniciando Listas

nombres = []
fechas = []
edades = []
apellidos = []
iniciales = []
estado_civil = []

#Bucle - Agregar Personas

agregando = True

while agregando:

    #Pidiendo Nombre

    nombre = input("[?] Ingrese Nombre: ")
    while len(nombre)-1 < 2:
        print("[!] ERROR. El nombre debe tener mas de dos caracteres. ")
        nombre = input("[?] Ingresar Nombre ")

    ###############################

    #Pidiendo Apellido

    apellido = input("[?] Ingresar Apellido: ")
    while len(apellido)-1 < 2:
        print("[!] ERROR. El apellido debe tener mas de dos caracteres. ")
        apellido = input("[?] Ingresar Apellido: ")

    ###############################

    #Pidiendo Edad

    año = int(input("[?] Ingrese su año de nacimiento: "))
    while año > date.today().year:
        print("[!] ERROR. El año maximo a usar es 2021. Intente nuevamente.")
        año = int(input("[?] Ingrese su año de nacimiento: "))
    
    mes = int(input("[?] Ingrese su mes de nacimiento: "))
    while mes > 12 or mes < 1:
        print("[!] ERROR. Seleccione un mes entre 1 y 12. Intente nuevamente.")
        mes = int(input("[?] Ingrese su mes de nacimiento: "))

    dia = int(input("[?] Ingrese su dia de nacimiento: "))
    while dia > 31 or dia < 1:
        print("[!] ERROR. Seleccione un dia entre 1 y 31. Intente nuevamente.")
        dia = int(input("[?] Ingrese su dia de nacimiento: "))


    nacimiento = f"{año}-{mes}-{dia}"

    edad = calcular_edad(año, mes, dia)

    ###############################
    
    separador(1)
    estadocivil = int(input("[?] Ingrese su estado civil:\n[+] 1: Soltero/a \n[+] 2: Casado/a \n[+] 3: Divorciado/a \n[+] 4: Viudo/a\n[?] Seleccion: "))
    
    while estadocivil > 4 or estadocivil < 1:
        separador(1)
        print("[-] No se entendio su eleccion. Seleccione un numero")
        estadocivil = int(input("[?] Ingrese su estado civil:\n[+] 1: Soltero/a \n[+] 2: Casado/a \n[+] 3: Divorciado/a \n[+] 4: Viudo/a\n[?] Seleccion: "))

    if estadocivil == 1:
        estado_civil.append("SOLTERO/A")     
    if estadocivil == 2:
        estado_civil.append("CASADO/A")
    if estadocivil == 3:
        estado_civil.append("DIVORCIADO/A")
    if estadocivil == 4:
        estado_civil.append("VIUDO/A")


    ###############################
    #Agregando Nombres

    if len(nombre)-1 > 2:      
        nombres.append(nombre.upper())

    #Agregando Apellidos

    if len(apellido)-1 > 2:
        apellidos.append(apellido.upper())

    #Agregando Edades

    fechas.append(nacimiento)
    edades.append(edad)

    #Lista para recolectar Iniciales

    aux = []
    name_list = nombre.split()
    for i in name_list:
        aux.append(i[0].upper())
    
    surname_list = apellido.split()
    for i in surname_list:
        aux.append(i[0].upper())

    iniciales.append(aux)
    agregando = False

    separador(1)
    seleccion = int(input(f"[?] Quiere agregar mas personas a la tabla? \n[+] 1: Si \n[+] 2: No \n[?] Seleccion: "))
    separador(1)

    while seleccion > 2 or seleccion < 1:
        separador(1)
        print("[-] No se entendio su eleccion. Seleccione un numero")
        seleccion = int(input(f"[?] Quiere agregar mas personas a la tabla? \n[+] 1: Si \n[+] 2: No \n[?] Seleccion: "))
        
    if seleccion == 1:
        agregando = True

    elif seleccion == 2:
        print("[!] Procesando Informacion...")
        sleep(2)
    
#Tabla de Informacion

table = PrettyTable(["NOMBRE", "APELLIDO", "FECHA DE NACIMIENTO", "EDAD", "ESTADO CIVIL", "INICIALES"])

#Agregando Informacion Recolectada
    
for i in range(len(nombres)):
    table.add_row([nombres[i], apellidos[i], fechas[i], edades[i], estado_civil[i], '.'.join(iniciales[i])])

separador(20)
print(table)
input("")



