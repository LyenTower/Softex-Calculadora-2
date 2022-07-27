operacao = "1" 
while operacao != 0:
    num_1= float(input('Escolha o primeiro número:'))
    num_2= float(input('Escolha o segundo número:'))
    operacao = int(input("Escolha qual operação você deseja: \n 1-Adição \n 2-Subtração \n 3-Multiplicação \n 4- Divisão \n 0-Sair \n"))
    
    if operacao == 0:
        print("Você saiu da calculadora")
        break
    if operacao == 1:
        resultado = num_1 + num_2
    elif operacao == 2:
        resultado = num_1 - num_2
    elif operacao == 3:
        resultado = num_1 * num_2
    elif operacao == 4:
        resultado = num_1 / num_2
    elif operacao != 1 or 2 or 3 or 4 or 0:
        resultado = "Operação não existe"
    
    print(f'A sua conta tem como resultado:{resultado}')