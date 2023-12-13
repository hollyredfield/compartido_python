import mysql.connector
class Conexion:
    def __init__(self):
        self.conexion = None
    def conexion_bdd(self):
        try:
            self.conexion = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "biblioteca",
            )
            print("¡Conexión realizada con éxito!")
            
        except mysql.connector.Error as error:
            print("Error al conectarse a la base de datos. ", error)
    def cerrar_conexion_bdd(self):
        if self.conexion:
            self.conexion.close()
            print("Conexión cerrada con éxito")


