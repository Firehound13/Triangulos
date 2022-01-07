lado1 = float(input("Qual o primeiro lado?"))
lado2 = float(input("Qual o segundo lado?"))
lado3 = float(input("Qual o terceiro lado?"))

if lado1 + lado2 >= lado3:
    print("Forma um triângulo")
elif lado1 + lado3 >= lado2:
    print("Forma um triângulo")
elif lado2 + lado3 >= lado1:
    print("Forma um triângulo")

if lado1 == lado2 == lado3:
    print("Triângulo Equilátero")
elif lado1 == lado2 != lado3:
    print("Triângulo Isósceles")
elif lado1 != lado2 != lado3:
    print("Triângulo Escaleno")
