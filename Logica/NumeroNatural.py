class NumeroNegativoError(Exception):
    pass

class NumeroNatural():
    def validarTipo(self):
        while True:
            try:
                self.numeroNatural = int(input("Ingrese un número natural: "))
                if self.numeroNatural < 0:
                    raise NumeroNegativoError
                break
            except ValueError as err:
                print("Oops!  Ingrese un número natural.  Intente otra vez...")
            except NumeroNegativoError as err:
                print("Oops!  Ingrese un número entero y positivo.  Intente otra vez...")

        return self.numeroNatural

    def obtener_divisores(self, numero):
        divisores = []
        for divisor in range(1, numero + 1):
            if numero % divisor == 0:
                print(divisor, "es divisor")
                divisores.append(divisor)
        return divisores

    def calcular_mcd(self, divisores_num1, divisores_num2):
        # Encuentra la intersección de los divisores
        interseccion = set(divisores_num1).intersection(set(divisores_num2))

        # El máximo elemento en la intersección es el MCD
        mcd = max(interseccion)
        return mcd

