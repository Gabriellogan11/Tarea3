def sumar(a, b):
    return a + b

if __name__ == "__main__":
    num1 = input("Introduce un numero:" )
    num2 = input("Introduce un numero")
    resultado = sumar(num1, num2)
    print(f"La suma de {num1} y {num2} es {resultado}")