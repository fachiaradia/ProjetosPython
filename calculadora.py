#Título
print("******CALCULADORA PYTHON******")

#Variáveis
soma = int("1")
subtra = int("2")
multipli = int("3")
divisao = int("4")


#Opções
print("Escolha uma das operações desejadas:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

#Seleção da operação pelo usuário
operacao = int(input("Digite operação desejada (1/2/3/4): "))

#Input dos valores pelo usuário
priNum = int(input("Digite primeiro número: "))
segNum = int(input("Digite segundo número: "))

if operacao == soma:
    print("Resultado é: ",priNum+segNum)
elif operacao == subtra:
    print("Resultado é: ",priNum-segNum)
elif operacao == multipli:
    print("Resultado é: ",priNum*segNum)
else:
    print("Resultado é: ",priNum/segNum)

