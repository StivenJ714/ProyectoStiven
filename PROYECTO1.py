import random

DD = 90
EE = 100
i = 3
j = 3

while DD > 0 and EE > 0:
    GO1 = input("DALE ENTER PARA VER QUIEN ATACA: ")
    go = random.randint(1,2)
    if go == 1:
        print("ATACA PC.")
        atackpc = random.randint(1,2)
        if atackpc == 1:
            EE -= 10
        elif atackpc == 2 and i > 0:
            EE -= 15
            i -= 1
    else:
        print("ATACA USUARIO")
        atackusuario = input("SELECCIONE ATAQUE: [A]LANCE, [B]SABLE: ")
        if atackusuario == "A":
            DD -= 10
        elif atackusuario == "B" and j > 0:
            DD -= 15
            j -= 1
            print(f'TE QUEDAN ',j,' SABLES')
    print("VIDA PC:", DD," VIDA USUARIO:", EE)
if DD > EE:
    print("TE GANO LA PC.")
else:
    print("EL GANADOR ES EL USUARIO.")

