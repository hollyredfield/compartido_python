import mysql.connector
class Conectar:
    def __init__(self):
        self.conexion = None

    def conexion_bdd(self):
        try:    
            self.conexion = mysql.connector.connect(
                host='localhost',
                user='root',
                password='', #yo tengo que ponerlo en blanco porque al poner la contraseña curso que tenemos todos, salta un error, no me digas por qué.
                database='biblioteca'
            )
            print("Conexión exitosa.")

        except mysql.connector.Error as e:
            print("Error al conectar a la base de datos: ", e)

    def close_connection(self):
        if self.conexion:
            self.conexion.close()
            print("Conexión cerrada.")
    
        

 

    