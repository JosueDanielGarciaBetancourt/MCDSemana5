from Logica.NumeroNatural import NumeroNatural

if __name__ == '__main__':

    objNumero = NumeroNatural()

    print("\n--Primer número--")
    num1 = objNumero.validarTipo()
    divisoresNum1 = objNumero.obtener_divisores(num1)

    print("\n--Segundo número--")
    num2 = objNumero.validarTipo()
    divisoresNum2 = objNumero.obtener_divisores(num2)

    print("\n--Máximo Común Divisor--")
    mcd = objNumero.calcular_mcd(divisoresNum1, divisoresNum2)
    print(mcd)





