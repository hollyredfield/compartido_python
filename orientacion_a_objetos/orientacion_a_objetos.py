class Libro:
    """
    Clase que representa un libro.

    Atributos:
    - titulo (str): El título del libro.
    - autor (str): El autor del libro.
    - paginas (int): El número de páginas del libro.
    """

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def abrir(self):
        print(f"Abriendo el libro {self.titulo}.")

    def leer(self):
        print(f"Leyendo {self.paginas} páginas de {self.titulo}.")

mi_libro = Libro("Cien Años de Soledad", "Gabriel García Márquez", 417)
mi_libro.abrir()
mi_libro.leer()

class Persona:
    """
    Clase que representa a una persona.
    """

    especie = 'Homo sapiens'  # Atributo de clase

    def __init__(self, nombre, edad):
        self.nombre = nombre    # Atributo de instancia
        self.edad = edad        # Atributo de instancia

    def presentarse(self):
        """
        Método que imprime un mensaje de presentación de la persona.
        """
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

empleado1 = Persona("Pepe", 24)
empleado2 = Persona("Juan",32)
empleado1.presentarse()
empleado2.presentarse()

class CuentaBancaria:
    """
    Clase que representa una cuenta bancaria.

    Atributos:
    - titular (str): El titular de la cuenta bancaria.
    - saldo (float): El saldo actual de la cuenta bancaria.

    Métodos:
    - __init__(titular, saldo_inicial): Constructor de la clase.
    - depositar(cantidad): Realiza un depósito en la cuenta bancaria.
    - ver_saldo(): Devuelve el saldo actual de la cuenta bancaria.
    """

    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.__saldo = saldo_inicial  # Saldo es un atributo privado

    def depositar(self, cantidad):
        """
        Realiza un depósito en la cuenta bancaria.

        Parámetros:
        - cantidad (float): La cantidad a depositar.

        Resultado:
        - None
        """
        if cantidad > 0:
            self.__saldo += cantidad
            print("Depósito realizado.")
        else:
            print("Cantidad inválida.")

    def ver_saldo(self):
        """
        Devuelve el saldo actual de la cuenta bancaria.

        Resultado:
        - float: El saldo actual de la cuenta bancaria.
        """
        return self.__saldo

class CuentaAhorro(CuentaBancaria):
    """
    Clase que representa una cuenta de ahorro en un banco.

    Atributos:
    - titular (str): El titular de la cuenta.
    - saldo_inicial (float): El saldo inicial de la cuenta.
    - tasa_interes (float): La tasa de interés aplicada a la cuenta.

    Métodos:
    - __init__(titular, saldo_inicial, tasa_interes): Constructor de la clase.
    - acumular_interes(): Acumula el interés en la cuenta.
    """
    def __init__(self, titular, saldo_inicial, tasa_interes):
        super().__init__(titular, saldo_inicial)
        self.tasa_interes = tasa_interes

    def acumular_interes(self):
        """
        Acumula el interés en la cuenta.

        Calcula el incremento del saldo de la cuenta basado en la tasa de interés
        y lo deposita en la cuenta.
        """
        incremento = self.ver_saldo() * self.tasa_interes
        self.depositar(incremento)
