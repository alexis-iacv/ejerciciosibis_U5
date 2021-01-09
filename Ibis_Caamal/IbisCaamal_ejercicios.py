#Operadores de Asingnacion

c = 2

c += 5  # suma de asignacion
c -= 2  # resta en asignacion
c *= 3  # multiplicacion en asignacion
c /= 3  # division en asignacion
c **=2  # potencia en asignacion
c %= 2  # modulo en asignacion
print ("Resultado de asignaciones ")
print(c)

a= "-IBIS-"

a *= 3

print(a)

#FACTORIAL

num= int(input("Digite numero para calcular el factorial: "))
fac = 1

for i in range(num):
    fac *= num
    num -= 1
print ("Resultado del Factorial")   
print(fac)

#Expreciones boleanas
num1 = 10
num2 = 10

com = num1 != num2
comp = num1 == num2
print("Primera comparacion Boleana ; ")
print (com)
print("Segunda comparacion Boleana ; ")
print (comp)

#Formulas Tipo C
import math
def discriminante(a,b,c):
    discrim=pow(b,2)-(4*a*c)
    return discrim

def raices(a,b,disc):
    raiz1=(-b+math.sqrt(disc))/(2*a)
    raiz2=(-b-math.sqrt(disc))/(2*a)
    return raiz1,raiz2

print ("Calculo de Raices")
a=float(input("a: "))
b=float(input("b: "))
c=float(input("c: "))
disc=discriminante(a,b,c)
if disc<0:
    print("No hay raices positivas")
else:
    print("Las raices positivas son: ")
    print raices(a,b,disc)



    

