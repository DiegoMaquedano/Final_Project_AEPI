from Proyecto_Final.Modelos import Fabricantes,Piezas,Ordenes
from Proyecto_Final.Funciones import show_menu,importar_fabricantes,importar_piezas,crear_pieza
from Proyecto_Final.Funciones import info_pieza,modificar_pieza,eliminar_pieza,crear_fabricante,info_fabricante
from Proyecto_Final.Funciones import modificar_fabricante,eliminar_fabricante,crear_orden_compra,info_orden,generar_informe
"""

Código del menú principal llamando a todas las funciones

"""

print("BASE DE DATOS DE FEU VERT".center(150))

# Chequear si hay datos en la base de Piezas
peticion=Piezas.select()
cuenta=0
for q in peticion:
    if q.Nombre_Pieza!=None:
        cuenta+=1

if cuenta==0:
    importar_piezas()

# Chequear si hay datos en la base de Fabricantes
peticion = Fabricantes.select()
cuenta = 0
for q in peticion:
    if q.Nombre_Fabricante != None:
        cuenta +=1

if cuenta == 0:
    importar_fabricantes()


#Bucle infinito
while True:
    show_menu()
    opcion=input(">> ")
    if opcion.upper()=="S":
        break

    elif opcion.upper()=="A":

        while True:

            print("Menú Piezas".center(150))
            print("Escoja una de las acciones a realizar con las piezas")
            print("1-Crear Pieza")
            print("2-Info Pieza")
            print("3-Modificar Pieza")
            print("4-Eliminar Pieza")
            print("S-Volver atrás")

            opcion=input(">> ")

            if opcion.upper()=="S":
                print("Volviendo al menú principal")
                break
            elif opcion.upper()=="1":
                crear_pieza()
            elif opcion.upper()=="2":
                info_pieza()
            elif opcion.upper()=="3":
                modificar_pieza()
            elif opcion.upper()=="4":
                eliminar_pieza()
            else:
                print("No has seleccionado una opcion valida")


    elif opcion.upper()=="B":

        while True:

            print("Menú Fabricantes".center(150))
            print("Escoja una de las acciones a realizar con los fabricantes")
            print("1-Crear Fabricante")
            print("2-Info Fabricante")
            print("3-Modificar Fabricante")
            print("4-Eliminar Fabricante")
            print("S-Volver atrás")

            opcion = input(">> ")

            if opcion.upper() == "S":
                print("Volviendo al menú principal")
                break
            elif opcion.upper() == "1":
                crear_fabricante()
            elif opcion.upper() == "2":
                info_fabricante()
            elif opcion.upper() == "3":
                modificar_fabricante()
            elif opcion.upper() == "4":
                eliminar_fabricante()
            else:
                print("No has seleccionado una opcion valida")


    elif opcion.upper()=="C":

        while True:

            print("Menú Ordenes".center(150))
            print("Escoja una de las acciones a realizar con las órdenes")
            print("1-Crear Orden")
            print("2-Info Orden")
            print("S-Volver atrás")

            opcion = input(">> ")

            if opcion.upper() == "S":
                print("Volviendo al menú principal")
                break
            elif opcion.upper() == "1":
                crear_orden_compra()
            elif opcion.upper() == "2":
                info_orden()
            else:
                print("No has seleccionado una opción valida")

    elif opcion.upper()=="D":
        generar_informe()


    else:
        print("No has seleccionado una opción valida")

print("Gracias por usar el sistema de Feu Vert. Vuelva pronto")
