def calcular(n1,operacao,n2):
    if operacao == '+':
        resultado = n1 + n2
    elif operacao == '-':
        resultado = n1 - n2
    elif operacao == '*':
        resultado = n1 * n2
    elif operacao == '/':
        if n2 == 0:
            return "Erro! não é possível dividir por zero."
        resultado = n1 / n2
    else:
        print("Opção inválida")
    return resultado

numero_01 = float(input("Digite um valor: "))
operacao = input("diga qual operação: ")
numero_02 = float(input("digite mais um valor: "))


print('o resultado da operação é: ', calcular(numero_01,operacao,numero_02))
