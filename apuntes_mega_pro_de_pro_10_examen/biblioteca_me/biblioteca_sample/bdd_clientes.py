import mysql.connector
def conexion_bdd():
    try:
        return mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "biblioteca"
        )   
        
    except mysql.connector.Error as z:
        print("Error al conectar a la base de datos: ", z)
        return None 
def acabarconexion(conexion_bdd):   
    try:
        if conexion_bdd:
            conexion_bdd.close()
            print("Conexión cerrada")
    except mysql.connector.Error as z:
        print("Error al tratar de cerar la conexión con la base de datos: ", z)
conexion = conexion_bdd()
acabarconexion(conexion)