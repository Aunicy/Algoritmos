def Invertidora(numero):
    acumulado = 0
    while numero>0:
        acumulado = acumulado * 10 + (numero%10)
        numero = numero // 10

    return acumulado

valor = -1
while valor<=0:
    valor = int(input("Digite un valor: "))

    if valor <= 0:
        print("Sólo positivos.")

invertido = Invertidora(valor)

print(invertido)