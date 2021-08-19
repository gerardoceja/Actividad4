import math
def main():
    #escribe tu código abajo de esta línea
    import math

r = float(input("Ingrese el radio de la esfera: "))

a = 4 * math.pi * r**2
v= (4 * math.pi * r**3) / 3

print("Area de la esfera: ",a)
print("Volumen de la esfera: ",v)



if __name__ == '__main__':
    main()
