import random

s = "pedra"
p = "papel"
t = "tesoura"

a = False

z = None

ponto = 0

opcao = None

def verifica(n,m):
    if(n==s):
        m = not m
        print("é igual a pedra")
    if(n==p):
        m = not m
        print("é igual a papel")
    if(n==t):
        m = not m
        print("é igual a tesoura")
    return m

print("PEDRA    PAPEL    TESOURA!")

while(opcao!='n'):
    print("digite sua opção:")

    z = input()

    verifica(z,a)

    x = random.randint(0,10)

    if(x<=3):
        print(s)
    if(x>3 and x<=6):
        print(p)
    if(x>6):
        print(t)

    if(x<=3 and z==s):
        print("Empate")

    if(x<=3 and z==p):
        print("ganhou")
        ponto = ponto + 10

    if(x<=3 and z==t):
        print("perdeu")
        ponto = ponto - 5

    if(x>3 and x<=6 and z==s):
        print("perdeu")
        ponto = ponto -5

    if(x>3 and x<=6 and z==p):
        print("empate")

    if(x>3 and x<=6 and z==t):
        print("ganhou")
        ponto = ponto + 10

    if(x>6 and z==s):
        print("ganhou")
        ponto = ponto + 10

    if(x>6 and z==p):
        print("perdeu")
        ponto = ponto - 5

    if(x>6 and z==t):
        print("empate")

    print(ponto)

    print("deseja continuar? N / S")
    opcao = input()




final = input()
