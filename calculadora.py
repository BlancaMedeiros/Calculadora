def calcular():
    if operacao == '+':
        resultado = n1 + n2
    elif operacao == '-':
        resultado = n1 - n2
    elif operacao == '*':
        resultado = n1 * n2
    elif operacao == '/':
        if n2 == 0:
            print("Erro: não é possível dividir por zero!")
            return
        resultado = n1 / n2
    else:
        print("Opção inválida")
    return resultado

n1 = float(input("Digite um valor: "))
operacao = input("diga qual operação: ")
n2 = float(input("digite mais um valor: "))
print('o resultado da operação é: ', calcular())
