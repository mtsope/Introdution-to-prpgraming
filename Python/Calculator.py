
print ("********************** Calculadora simples *****************")
num1 = input("First number?")
print ("Number 1 {}.".format(num1))

num2 = input("Second number?")
print ("Number 2{}".format(num2))


print ("Adicao - {} + {} = {}".format(num1, num2, num1 + num2))
print ("Subtracao - {} - {} = {}".format(num1, num2, num1 - num2))
print ("ultiplicacao - {} * {} = {}".format(num1, num2, num1 * num2))
print ("Divisao - {} / {} = {}".format(num1, num2, num1 / num2))




import math

print ("********************** Hipotenusa *****************")
slideA = input("Wahat is the length of A")
slideB = input("Wahat is the length of B")
slideC = (slideA * slideB) + (slideB + slideA)
slideC + math.sqrt(slideC)
print ("The length os slideC is {}".format(slideC))