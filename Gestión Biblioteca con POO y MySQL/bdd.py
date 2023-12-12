import mysql.connector
from mysqlx import Error


class ConexionBiblioteca:

    def conectar(self):
        try:
            conexion = mysql.connector.connect(
                host='localhost',
                user='root',
                password='DAM1', #La contraseña cambia de mi casa a la que tengo en clase
                database='biblioteca'
            )
            return conexion
        
        except mysql.connector.Error as err:
            print(f"Error en conexión: {err}")
            return None
        
    def cierra_conexion(self, conexion):
        if conexion:
            conexion.close()
            print("Conexión cerrada.")