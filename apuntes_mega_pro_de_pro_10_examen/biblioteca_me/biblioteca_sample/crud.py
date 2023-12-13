from bdd_clientes import*
 
""" 
id_lector int auto_increment, 
nombre varchar, 
apellidos varchar, 
fecha_alta date, 
fecha_baja date, 
"""
def anadir_cliente():
    try:
        nombre = input("Introduce el nombre: ")
        apellidos = input("Introduce los apellidos: ")
        fecha_alta = input("Introduce la fecha de alta (formato MM/DD/YYYY): ") #año-mes-día
        fecha_baja = input("Introduce la fecha de baja (formato MM/DD/YYYY): ")

        conexion = conexion_bdd()
        cursor = conexion.cursor()
        query = "Insert into lectores (nombre, apellidos, fecha_alta, fecha_baja) VALUES (%s, %s, %s, %s)"
        valores = (nombre, apellidos, fecha_alta, fecha_baja)
        cursor.execute(query, valores)
        conexion.commit()
        print("Se ha dado de alta con éxito el lector")
        acabarconexion(conexion)
    except mysql.connector.Error as error:
        print("Error al añadir el lector. ", error)
        return None
def ver_clientes():
    try:
        conexion = conexion_bdd()
        cursor = conexion.cursor()
        query = "select * from lectores"
        cursor.execute(query)
        registros = cursor.fetchall()
        for registro in registros:
            print(registro)
        acabarconexion(conexion)
    except mysql.connector.Error as error:
        print("Error al ver los lectores. ", error)
        return None

def eliminar_cliente():
    try:
        id_lector = int(input("Introduce el id del lector que quieres eliminar: "))
        conexion = conexion_bdd()
        cursor = conexion.cursor()
        query = "delete from lectores where id_lector = %s"
        valores = (id_lector,)
        cursor.execute(query, valores)
        conexion.commit()
        print("Se ha eliminado con éxito el lector")
        acabarconexion(conexion)
    except mysql.connector.Error as error:
        print("Error al eliminar el lector. ", error)
        return None
def buscar_cliente():
    try:
        id_lector = int(input("Introduce el id del lector: "))
        conexion = conexion_bdd()
        cursor = conexion.cursor()
        query = "select * from lectores where id_lector = %s"
        valores = (id_lector,)
        cursor.execute(query, valores)
        registros = cursor.fetchall()
        for registro in registros:
            print(registro)
        acabarconexion(conexion)
    except mysql.connector.Error as error:
        print("Error al buscar el lector. ", error)
        return None
def modificar_cliente():
    try:
        id_lector = int(input("Introduce el id del lector que quieres modificar: "))
        nombre = input("Introduce el nuevo nombre: ")
        apellidos = input("Introduce los nuevos apellidos: ")
        fecha_alta = input("Introduce la nueva fecha de alta (formato MM/DD/YYYY): ")
        fecha_baja = input("Introduce la nueva fecha de baja (formato MM/DD/YYYY): ")

        conexion = conexion_bdd()
        cursor = conexion.cursor()
        query = "UPDATE lectores SET nombre = %s, apellidos = %s, fecha_alta = %s, fecha_baja = %s WHERE id_lector = %s"
        valores = (nombre, apellidos, fecha_alta, fecha_baja, id_lector)
        cursor.execute(query, valores)
        conexion.commit()
        print("Se ha modificado con éxito el lector")
        acabarconexion(conexion)
    except mysql.connector.Error as error:
        print("Error al modificar el lector. ", error)
        return None
