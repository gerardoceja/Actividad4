import math
def main():
     #escribe tu código abajo de esta línea
   import math

a = float(input("Ingrese la longitud del lado A: "))
b = float(input("Ingrese la longitud del lado B: "))
c = float(input("Ingrese la longitud del lado C: "))

s = (a + b + c) / 2

ar= math.sqrt(s*(s-a)*(s-b)*(s-c))

print("Area del triangulo: ",ar)



if __name__ == '__main__':
    main()
