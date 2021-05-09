from Proyecto_Final.Modelos import Piezas,Fabricantes,Ordenes
from peewee import *
from datetime import datetime
import json

"""

Definición de todas las funciones a emplear en el menú

"""

######################## MOSTRAR MENÚ ###############################
def show_menu():
    print("Bienvenido al sistema de consulta de piezas y pedidos Feu vert".center(150))
    print("Elija una de las opciones disponibles: ")
    print("A-Menú Piezas")
    print("B-Menú Fabricantes")
    print("C-Menú Ordenes")
    print("D-Generar Informe")
    print("S- Salir")

######################## IMPORTAR CSV PIEZAS ###############################
import csv
from datetime import datetime
def importar_piezas():
    with open("piezas.csv") as csvFile:
        CSVdata = csv.reader(csvFile, delimiter=',')
        next(CSVdata)
        for row in CSVdata:
            nombre_pieza = row[0].upper()
            id_pieza=row[1].upper()
            fecha_pieza = datetime.strptime(row[2].upper(),'%d/%m/%Y %H:%M:%S')
            fabricante_pieza = row[3].upper()
            loc_fabri_pieza = row[4].upper()
            precio_pieza = row[5].upper()

            pieza=Piezas.create(Nombre_Pieza=nombre_pieza,
                                Numero_Registro_Pieza=id_pieza,
                                Fecha_Fabri_Pieza=fecha_pieza,
                                Fabri_Pieza=fabricante_pieza,
                                Localidad_Fabri_Pieza=loc_fabri_pieza,
                                Precio_Pieza=precio_pieza)
            pieza.save()
        print("Carga de piezas completada")

######################## IMPORTAR CSV FABRICANTES ###############################
import csv
from datetime import datetime
def importar_fabricantes():
    with open("fabricantes.csv") as csvFile:
        CSVdata = csv.reader(csvFile, delimiter=',')
        next(CSVdata)
        for row in CSVdata:
            nombre_fabricante = row[0].upper()
            id_fabricante=row[1].upper()
            loc_fabricante = row[2].upper()
            cif_fabricante = row[3].upper()

            fabricante=Fabricantes.create(Nombre_Fabricante=nombre_fabricante,
                                Numero_Registro_Fabricante=id_fabricante,
                                Localizacion_Fabricante=loc_fabricante,
                                CIF_Fabricante=cif_fabricante)
            fabricante.save()
        print("Carga de fabricantes completada")



######################## CREAR PIEZA ###############################
def crear_pieza():
    print("Menú de crear piezas. Si desea volver atrás, escriba 'S' en cualquier momento")
    nombre=input("Introduzca el nombre de la pieza: ").upper()
    if nombre=="S":
        print("Volviendo al menú anterior")
        return
    while not nombre:
        nombre = input("Introduzca el nombre de la pieza: ").upper()
        if nombre=="S":
            print("Volviendo al menú anterior")
            return
    while True:
        try:
            registro=input("Introduzca el nùmero de registro de la pieza: ").upper()
            if registro=="S":
                print("Volviendo al menú anterior")
                return
            while not registro:
                registro = input("Introduzca el número de registro de la pieza: ")
                if registro == "S":
                    print("Volviendo al menú anterior")
                    return
            resultado=Piezas.get(Piezas.Numero_Registro_Pieza==registro)
            print("Esta pieza ya está dada de alta. Intente de nuevo")
        except:
            break

    while True:
        fecha = input("Introduza la fecha de la compra en formato dd/mm/yyyy: ").upper()
        if fecha=="S":
            print("Volviendo al menú anterior")
            return
        try:
            fecha_transformada=datetime.strptime(fecha,"%d/%m/%Y")
            break
        except ValueError:
            print("El formato de fecha debe ser dd/mm/yy, intente de nuevo")

    while True:
        fabricante = input("Introduzca el nombre del fabricante de la pieza: ").upper()
        if fabricante=="S":
            print("Volviendo al menú anterior")
            return
        try:
            fabricantes=Fabricantes.get(Fabricantes.Nombre_Fabricante==fabricante)
            break
        except DoesNotExist:
            print("El fabricante introducido no existe en la base de datos. Intente de nuevo")

    localidad=input("Introduzca la localidad donde se fabricó la pieza: ").upper()
    if localidad=="S":
        print("Volviendo al menú anterior")
        return
    while not localidad:
        localidad = input("Introduzca el nombre de la pieza: ")

    while True:
        precio = input("Introduzca el precio de la pieza en formato XX.XX: ").upper()
        if precio=="S":
            print("Volviendo al menú anterior")
            return
        try:
            precio_transformado=float(precio)
            break
        except ValueError:
            print("El precio está en formato incorrecto. Intentar de nuevo")

    while True:
        ventas = input("Introduzca el número de piezas vendidas: ").upper()
        if ventas=="S":
            print("Volviendo al menú anterior")
            return
        try:
            ventas_transformadas=int(ventas)
            break
        except ValueError:
            print("Las ventas deben introducirse como número. Intentar de nuevo")

    pieza=Piezas.create(Nombre_Pieza=nombre, Numero_Registro_Pieza=registro,
                        Fecha_Fabri_Pieza=fecha_transformada, Fabri_Pieza=fabricante,
                        Localidad_Fabri_Pieza=localidad,Precio_Pieza=precio_transformado,
                        Piezas_Vendidas=ventas_transformadas)
    pieza.save()
    print("Se ha creado la pieza correctamente")



######################## INFO PIEZA ###############################
def info_pieza():
    print("Menú de consulta de piezas. Escriba 'S' para volver atrás")
    while True:
        try:
            seleccion=input("Introduzca el numero de registro: ").upper()
            if seleccion=="S":
                print("Volviendo al menú anterior")
                return
            pieza=Piezas.get(Piezas.Numero_Registro_Pieza==seleccion)
            print(f"Nombre: {pieza.Nombre_Pieza} Registro: {pieza.Numero_Registro_Pieza}\n"
                  f"Fecha: {pieza.Fecha_Fabri_Pieza}, Fabricante: {pieza.Fabri_Pieza_id}\n"
                  f"Localidad: {pieza.Localidad_Fabri_Pieza},Precio: {pieza.Precio_Pieza},Vendidas: {pieza.Piezas_Vendidas}")
            break
        except:
            print("El número introducido no es correcto, vuelva a intentarlo")



######################## MODIFICAR PIEZA ###############################
def modificar_pieza():
    print("Menú de modificar piezas. Escriba 'S' en cualquier momento para volver atrás")
    while True:
        try:
            registro=input("Introduzca el número de registro de la pieza a modificar: ").upper()
            if registro=="S":
                print("Volviendo al menú anterior")
                return
            resultado=Piezas.get(Piezas.Numero_Registro_Pieza==registro)
            break
        except:
            print("El número introducido no es correcto, pruebe con otro")

    nombre = input("Introduzca el nombre modificado de la pieza: ").upper()
    if nombre=="S":
        print("Volviendo al menú anterior")
        return
    while not nombre:
        nombre = input("Introduzca el nombre modificado de la pieza: ").upper()
        if nombre=="S":
            print("Volviendo al menú anterior")
            return
    while True:
        fecha = input("Introduza la fecha de la compra modificada en formato dd/mm/yy: ").upper()
        if fecha=="S":
            print("Volviendo al menú anterior")
            return
        try:
            fecha_transformada=datetime.strptime(fecha,"%d/%m/%Y")
            break
        except ValueError:
            print("El formato de fecha debe ser dd/mm/yy, intente de nuevo")

    while True:
        fabricante = input("Introduzca el nombre modificado del fabricante de la pieza: ").upper()
        if fabricante=="S":
            print("Volviendo a menú anterior")
            return
        try:
            fabricantes=Fabricantes.get(Fabricantes.Nombre_Fabricante==fabricante)
            break
        except DoesNotExist:
            print("El fabricante introducido no existe en la base de datos. Intente de nuevo")

    localidad=input("Introduzca la localidad modificada donde se fabricó la pieza: ").upper()
    if localidad=="S":
        print("Volviendo al menú anterior")
        return

    while True:
        precio = input("Introduzca el precio modificado de la pieza en formato XX.XX: ").upper()
        if precio=="S":
            print("Volviendo al menú anterior")
            return
        try:
            precio_transformado=float(precio)
            break
        except ValueError:
            print("El precio está en formato incorrecto. Intentar de nuevo")

    while True:
        ventas = input("Introduzca el número de piezas vendidas modificado: ").upper()
        if ventas=="S":
            print("Volviendo al menú anterior")
            return
        try:
            ventas_transformadas=int(ventas)
            break
        except ValueError:
            print("Las ventas deben introducirse como número. Intentar de nuevo")

    resultado.Nombre_Pieza=nombre
    resultado.Fecha_Fabri_Pieza=fecha_transformada
    resultado.Fabri_Pieza=fabricante
    resultado.Localidad_Fabri_Pieza=localidad
    resultado.Precio_Pieza=precio_transformado
    resultado.Piezas_Vendidas=ventas_transformadas

    resultado.save()
    print("Se ha modificado la pieza")



######################## ELIMINAR PIEZA ###############################
def eliminar_pieza():
    print("Menú de borrar piezas. Escriba 'S' en cualquier momento para volver atrás")
    while True:
        try:
            registro=input("Introduzca el número de registro de la pieza que desea borrar: ").upper()
            if registro=="S":
                print("Volviendo al menú anterior")
                return
            resultado=Piezas.get(Piezas.Numero_Registro_Pieza==registro)
            break
        except:
            print("El numero introducido no es correcto, pruebe con otro")
    resultado.delete_instance()
    print("La pieza se ha borrado correctamente")


######################## CREAR FABRICANTE ###############################
def crear_fabricante():
    print("Menú de crear fabricante. Escriba 'S' en cualquier momento para volver atrás")
    while True:
        try:
            nombre_fabri=input("Introduzca el nombre del nuevo fabricante: ").upper()
            if nombre_fabri=="S":
                print("Volviendo al menú anterior")
                return
            while not nombre_fabri:
                nombre_fabri = input("Introduzca el nombre del nuevo fabricante: ").upper()
                if nombre_fabri == "S":
                    print("Volviendo al menú anterior")
                    return
            resultado=Fabricantes.get(Fabricantes.Nombre_Fabricante==nombre_fabri)
            print("Este fabricante ya está dado de alta. Intente de nuevo")
        except:
            break

    while True:
        try:
            registro_fabri=input("Introduzca el numero de registro del nuevo fabricante: ").upper()
            if registro_fabri=="S":
                print("Volviendo al menú anterior")
                return
            while not registro_fabri:
                registro_fabri = input("Introduzca el numero de registro del nuevo fabricante: ").upper()
                if registro_fabri == "S":
                    print("Volviendo al menú anterior")
                    return
            resultado=Fabricantes.get(Fabricantes.Numero_Registro_Fabricante==registro_fabri)
            print("Este fabricante ya está dado de alta. Intente de nuevo")
        except:
            break

    localidad=input("Introduzca la localidad del nuevo fabricante: ").upper()
    if localidad=="S":
        print("Volviendo al menú anterior")
        return

    while True:
        try:
            cif_fabri=input("Introduzca el CIF del nuevo fabricante: ").upper()
            if cif_fabri=="S":
                print("Volviendo al menú anterior")
                return
            while not cif_fabri:
                cif_fabri = input("Introduzca el CIF del nuevo fabricante: ").upper()
                if cif_fabri == "S":
                    print("Volviendo al menú anterior")
                    return
            resultado=Fabricantes.get(Fabricantes.CIF_Fabricante==cif_fabri)
            print("Este fabricante ya está dado de alta. Intente de nuevo")
        except:
            break

    fabricante=Fabricantes.create(Nombre_Fabricante=nombre_fabri, Numero_Registro_Fabricante=registro_fabri,
                        Localizacion_Fabricante=localidad, CIF_Fabricante=cif_fabri)

    fabricante.save()
    print("Se ha creado el nuevo fabricante")



######################## INFO FABRICANTE ###############################
def info_fabricante():
    print("Menú de consulta de fabricantes. Escriba 'S' en cualqueir momento para volver atrás")
    while True:
        try:
            seleccion=input("Introduzca el numero de registro del fabricante: ").upper()
            if seleccion=="S":
                print("Volviendo al menú anterior")
                return
            fabricante=Fabricantes.get(Fabricantes.Numero_Registro_Fabricante==seleccion)
            print(f"Nombre: {fabricante.Nombre_Fabricante} Registro: {fabricante.Numero_Registro_Fabricante}\n"
                  f"Localidad: {fabricante.Localizacion_Fabricante},CIF: {fabricante.CIF_Fabricante}")
            break
        except:
            print("El número introducido no es correcto, vuelva a intentarlo")


######################## MODIFICAR FABRICANTE ###############################
def modificar_fabricante():
    print("Menú de modificar fabricantes. Escriba 'S' en cualquier momento para volver atrás")
    while True:
        try:
            registro=input("Introduzca el número de registro del fabricante a modificar: ").upper()
            if registro=="S":
                print("Volviendo al menú anterior")
                return
            resultado=Fabricantes.get(Fabricantes.Numero_Registro_Fabricante==registro)
            break
        except:
            print("El numero introducido no es correcto, pruebe con otro")

    localidad=input("Introduzca la localidad modificada del fabricante: ").upper()
    if localidad == "S":
        print("Volviendo al menú anterior")
        return

    resultado.Localizacion_Fabricante=localidad

    resultado.save()
    print("Se ha modificado el fabricante")


######################## ELIMINAR FABRICANTE ###############################
def eliminar_fabricante():
    print("Menú de borrar fabricantes. Escriba 'S' para volver al atrás")
    while True:
        try:
            registro=input("Introduzca el número de registro del fabricante que desea borrar: ").upper()
            if registro == "S":
                print("Volviendo al menú anterior")
                return
            resultado=Fabricantes.get(Fabricantes.Numero_Registro_Fabricante==registro)
            break
        except:
            print("El numero introducido no es correcto, pruebe con otro")
    resultado.delete_instance()
    print("El fabricante se ha borrado correctamente")



####################### CREAR ORDEN COMPRA ###############################
def crear_orden_compra():
    print("Menú de crear orden de compra")
    piezas=[]
    while True:
        try:
            numero_registro_pieza=input("Introduzca el numero de registro de la pieza a incluir. Pulse S para finalizar: ").upper()
            if numero_registro_pieza=="S":
                break
            else:
                resultado = Piezas.get(Piezas.Numero_Registro_Pieza == numero_registro_pieza)
                piezas.append(numero_registro_pieza)
        except:
            print("El número de registro indicado no existe. Intente de nuevo")

    if piezas==[]:
        print("No ha introducido elementos en la orden. Saliendo del menú")
    else:
        while True:
            try:
                id_compra=input("Introduzca el id de la compra. Escriba 'S' para salir: ").upper()
                if id_compra=="S":
                    print("Volviendo al menú anterior")
                    return
                while not id_compra:
                    id_compra=input("Introduzca el id de la compra: ")
                    if id_compra == "S":
                        print("Volviendo al menú anterior")
                        return
                resultado=Ordenes.get(Ordenes.ID_Compra_Orden==id_compra)
                print("Esta orden de compra ya existe. Intente de nuevo")
            except:
                break

        while True:
            try:
                fecha_compra=input("Introduzca la fecha de la compra en formato dd/mm/yyyy. Escriba 'S' para salir: ").upper()
                if fecha_compra=="S":
                    print("Volviendo al menú anterior")
                    return
                fecha_transformada=datetime.strptime(fecha_compra,"%d/%m/%Y")
                break
            except ValueError:
                print("El formato de fecha debe ser dd/mm/yy, intente de nuevo")

        vendedor=input("Introduzca su nombre. Escriba 'S' para salir: ").upper()
        if vendedor == "S":
            print("Volviendo al menú anterior")
            return
        while not vendedor:
            vendedor = input("Introduzca el id de la compra: ")
            if vendedor == "S":
                print("Volviendo al menú anterior")
                return
        piezas_pedido=tuple(piezas)

        for i in piezas_pedido:
            total=0
            pieza=Piezas.get(Piezas.Numero_Registro_Pieza==i)
            pieza.Piezas_Vendidas+=1
            pieza.save()
            precio_pieza=pieza.Precio_Pieza
            total+=precio_pieza

        orden=Ordenes.create(ID_Compra_Orden=id_compra, Fecha_Compra_Orden=fecha_compra,
                             Vendedor_Orden=vendedor, Piezas_Compra_Orden=piezas_pedido,
                             Precio_Orden=total)

        orden.save()
        print("Se ha creado la nueva orden de compra")



######################## INFO ORDEN ###############################
def info_orden():
    print("Menú de consulta de órdenes. Escriba 'S' para salir")
    while True:
        try:
            seleccion=input("Introduzca el ID de la orden a consultar: ").upper()
            if seleccion=="S":
                print("Volviendo al menú anterior")
                return
            orden=Ordenes.get(Ordenes.ID_Compra_Orden==seleccion)
            print(f"ID Orden: {orden.ID_Compra_Orden}\nFecha: {orden.Fecha_Compra_Orden}\n"
                  f"Vendedor: {orden.Vendedor_Orden}\nPiezas Orden: {orden.Piezas_Compra_Orden}\n"
                  f"Precio Orden: {orden.Precio_Orden}")
            break
        except:
            print("El número introducido no es correcto, vuelva a intentarlo")


######################## GENERAR INFORME ###############################
def generar_informe():
    print("Generando resultado de ventas...")
    #Total de piezas vendidas
    piezas_vendidas=Piezas.select(fn.SUM(Piezas.Piezas_Vendidas)).scalar()

    #Ingresos totales
    ingresos_totales=Ordenes.select(fn.SUM(Ordenes.Precio_Orden)).scalar()

    #Fabricante más vendido
    max_piezas=Piezas.select(fn.MAX(Piezas.Piezas_Vendidas))
    fabri_mas_vendido_select=Piezas.select(Piezas.Fabri_Pieza_id).where(Piezas.Piezas_Vendidas==max_piezas)
    for q in fabri_mas_vendido_select:
        resultado=q.Fabri_Pieza_id
    fabri_mas_vendido=resultado

    #Fabricante menos vendido
    min_piezas=Piezas.select(fn.MIN(Piezas.Piezas_Vendidas))
    fabri_menos_vendido_select = Piezas.select(Piezas.Fabri_Pieza_id).where(Piezas.Piezas_Vendidas == min_piezas)
    for q in fabri_menos_vendido_select:
        resultado=q.Fabri_Pieza_id
    fabri_menos_vendido=resultado

    #Fabricante más caro
    qry = Piezas.select(Piezas.Fabri_Pieza_id, fn.SUM(Piezas.Precio_Pieza)).group_by(Piezas.Fabri_Pieza_id)
    maxi = 0
    for q in qry:
        if q.Precio_Pieza > maxi:
            maxi = q.Precio_Pieza
            fabri = q.Fabri_Pieza_id
    fabri_mas_caro=fabri

    #Época de mayor producción
    qry2 = Piezas.select(Piezas.Fecha_Fabri_Pieza, fn.COUNT(Piezas.Numero_Registro_Pieza)).group_by(Piezas.Fecha_Fabri_Pieza)
    spring = range(80, 172)
    summer = range(172, 264)
    fall = range(264, 355)
    primavera = 0
    otono = 0
    verano = 0
    invierno = 0
    for q in qry2:
        doy = q.Fecha_Fabri_Pieza.timetuple().tm_yday
        if doy in spring:
            primavera += 1
        elif doy in summer:
            verano += 1
        elif doy in fall:
            otono += 1
        else:
            invierno += 1
    diccionario = {"primavera": primavera, "verano": verano, "otono": otono, "invierno": invierno}
    epoca_mas_produccion=max(diccionario, key=diccionario.get)

    #Época de mayores ventas
    qry2 = Piezas.select(Piezas.Fecha_Fabri_Pieza, fn.SUM(Piezas.Piezas_Vendidas)).group_by(Piezas.Fecha_Fabri_Pieza)
    spring = range(80, 172)
    summer = range(172, 264)
    fall = range(264, 355)
    primavera = 0
    otono = 0
    verano = 0
    invierno = 0
    for q in qry2:
        doy = q.Fecha_Fabri_Pieza.timetuple().tm_yday
        if doy in spring:
            primavera += q.Piezas_Vendidas
        elif doy in summer:
            verano += q.Piezas_Vendidas
        elif doy in fall:
            otono += q.Piezas_Vendidas
        else:
            invierno += q.Piezas_Vendidas
    diccionario = {"primavera": primavera, "verano": verano, "otono": otono, "invierno": invierno}
    epoca_mas_ventas=max(diccionario, key=diccionario.get)

    #Listado de localizaciones
    qry3 = Piezas.select(Piezas.Localidad_Fabri_Pieza).distinct()
    localizaciones = []
    for q in qry3.order_by(Piezas.Localidad_Fabri_Pieza):
        localizaciones.append(q.Localidad_Fabri_Pieza)
    listado_localizaciones = localizaciones

    #Listado de fabricantes
    qry4 = Fabricantes.select(Fabricantes.Nombre_Fabricante)
    fabricantes = []
    for q in qry4.order_by(Fabricantes.Numero_Registro_Fabricante):
        fabricantes.append(q.Nombre_Fabricante)
    listado_fabricantes = fabricantes

    #Empleado del mes
    qry5 = Ordenes.select(Ordenes.Vendedor_Orden, fn.SUM(Ordenes.Precio_Orden)).group_by(Ordenes.Vendedor_Orden)
    total = 0
    for q in qry5:
        if q.Precio_Orden > total:
            empleado_mes = q.Vendedor_Orden
    empleado_del_mes = empleado_mes

    resultado_json={
        "Total de piezas vendidas":piezas_vendidas,
        "Ingresos totales":ingresos_totales,
        "Fabricante más vendido":fabri_mas_vendido,
        "Fabricante menos vendido":fabri_menos_vendido,
        "Fabricante más caro":fabri_mas_caro,
        "Época de mayor producción":epoca_mas_produccion,
        "Época de mayores ventas":epoca_mas_ventas,
        "Localizaciones de fabricación piezas":listado_localizaciones,
        "Listado de fabricantes":listado_fabricantes,
        "Empleado del mes":empleado_del_mes
    }

    fichero = open("informe_ventas.json", "w")
    json.dump(resultado_json, fichero)
    fichero.close()
    print("Informe generado correctamente")
