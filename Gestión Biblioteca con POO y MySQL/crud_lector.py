from bdd import ConexionBiblioteca
from mysqlx import Error

class Lector:

    def __init__(self, nombre, apellidos, fecha_alta, fecha_baja):

        self.conexion = ConexionBiblioteca() #Inicializo una instancia de la clase ConexionBiblioteca para gestionar la conexión a la base de datos
        
        self.nombre = nombre # Asigno los valores iniciales a los atributos de la instancia
        self.apellidos = apellidos
        self.fecha_alta = fecha_alta
        self.fecha_baja = fecha_baja
        
    #Setters y Getters
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def get_nombre(self):
        return self.nombre

    def set_apellidos(self, apellidos):
        self.apellidos = apellidos
    
    def get_apellidos(self):
        return self.apellidos
    
    def set_fecha_alta(self, fecha_alta):
        self.fecha_alta = fecha_alta
    
    def get_fecha_alta(self):
        return self.fecha_alta
    
    def set_fecha_baja(self, fecha_baja):
        self.fecha_baja = fecha_baja
    
    def get_fecha_baja(self):
        return self.fecha_baja
    
    def alta_lector(self, nombre, apellidos, fecha_alta):
        try:
            
            conexion = self.conexion.conectar() # Esta parte establece la conexión a la base de datos
            cursor = conexion.cursor()
            
            query = "INSERT INTO lectores (nombre, apellidos, fecha_alta) VALUES (%s, %s, %s)" # Esta define la consulta SQL para insertar un nuevo lector
            valores = (nombre, apellidos, fecha_alta)
            
            cursor.execute(query, valores) # Esta ejecuta la consulta y realiza la inserción
            conexion.commit()
            
            print('Alta de lector realizada con éxito') # Si sale bien imprime el texto
            
            self.conexion.cierra_conexion(conexion) # Finalmente esta cierra la conexión a la base de datos
    
        except Error as error:
            print(f"Error en alta de lector: {error}") # En caso de error imprime esto
            
            return None # Este return None significa que, si ocurre algún error durante el proceso de alta de un lector en la base de datos (por ejemplo, problemas de conexión, consulta SQL incorrecta, etc.), 
                        # la función retornará None para indicar que la operación no fue exitosa. 
                        # En este caso, el código que llamó a la función puede interpretar que hubo un problema y mostrar un mensaje de error.
        
    def borrar_lector(self, id_lector):
        try:
            # Comprueba si el lector tiene préstamos pendientes antes de borrarlo
            if self.tiene_prestamos_pendientes(id_lector): # Llama al método tiene_prestamos_pendientes para verificar si el lector tiene préstamos pendientes. Este método retorna True si hay préstamos pendientes y False si no los hay.
                print("No se puede borrar el lector porque tiene préstamos pendientes.")
                return None

            conexion = self.conexion.conectar()
            cursor = conexion.cursor()
            query = "DELETE FROM lectores WHERE id_lector = %s"
            valores = (id_lector,)
            cursor.execute(query, valores)
            conexion.commit()
            print("Usuario eliminado con éxito.")
            self.conexion.cierra_conexion(conexion)

        except Error as error:
            print(f"Error en borrar lector: {error}")   
            return None
        
    def tiene_prestamos_pendientes(self, id_lector):
        try:
            conexion = self.conexion.conectar()
            cursor = conexion.cursor()
            query = "SELECT COUNT(*) FROM prestamos WHERE lector = %s AND fecha_devolucion IS NULL"
            valores = (id_lector,)
            cursor.execute(query, valores)
            interruptor = cursor.fetchone()[0] # El comando fetchone()[0] se utiliza en Python para recuperar el primer elemento de la primera fila 
                                                # de un conjunto de resultados después de ejecutar una consulta SQL. Dado que la consulta es un COUNT(*), 
                                                # obtendrás un único valor que representa la cantidad de préstamos pendientes. [0] accede a ese valor.
            self.conexion.cierra_conexion(conexion)
            return interruptor > 0
            # Este método se utiliza en objetos cursor de bases de datos después de ejecutar una consulta. 
            # Devuelve la siguiente fila del conjunto de resultados como una tupla. Si no hay más filas, devuelve None.
            # Usa [0] para acceder al primer elemento de la tupla, ya que estamos interesados en obtener un valor específico de la fila.
            
        except Error as error:
            print(f"Error en verificar préstamos pendientes: {error}")
            return True # En caso de error, imprime el mensaje de error y devuelve True (asumiendo que hay préstamos pendientes)

            
    