# def
#AS FUNÇÕES SÃO REUTILIZÁVEIS
# o 'print' não armazena o valor, enquanto que o 'return' armazena, e é o ideal para os casos de funções! 

#SOMA
def soma(a, b):
    return a + b

soma (10, 5)

resultado = soma (10, 5) #Quando eu chamo uma função eu não preciso identá-la, porque não há hierarquia entre funções!
print (resultado)


def soma2(a, b):
    print (a + b)
    
soma2 (10, 10)

soma

def soma3 (f, g):
    return (f + g)
resultado3 = soma3(5, 5)
print (resultado3)

#SUBTRAÇÃO
def subtração(c, d):
    return c - d


resultado2 = subtração (8, 5)
print (resultado2)

#MULTIPLICAÇÃO 

def mult (x, z):
    return (x * z)
result = mult (10, 2)
print (result)

#DIVISÃO 

def div (c, v):
    return (c / v)
res = div (50, 10)
print(res)

#DIVISÃO INTEIRA

def divIn (s, d):
    return (s //d)
Rdiv = divIn (15, 2)
print (Rdiv)