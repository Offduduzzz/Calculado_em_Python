#   Calculadora em python
#   while, if, ...
#   variáveis
saida = ''


#   recolhendo informações do usuário
num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')
print('-='*30)
#   checagem
while saida != 'sim':
    try:
        num1_float = float(num1)
        num2_float = float(num2)
        #   escolha da operação
        print('Qual operação você deseja fazer? ')
        print('-='*30)
        print('[1] ADIÇÃO \n[2] SUBTRAÇÃO \n[3] MULTIPLICAÇÃO \n[4] DIVISÃO')
        #   input da operação escolhida
        print('-='*30)
        operacao_escolhida = input('Digite o número que indique a operação: ')
        print('-='*30)
        try:
            operacao_escolhida_int = int(operacao_escolhida)
        #   calculo dos números fornecido pelo usuário
            if operacao_escolhida_int == 1:
                calculo = (num1_float + num2_float)
                print(f'A soma é {calculo}.')
            elif operacao_escolhida_int == 2:
                calculo = (num1_float - num2_float)
                print(f'A subtraçaõ é {calculo}.')
            elif operacao_escolhida_int == 3:
                calculo = (num1_float * num2_float)
                print(f'A multiplicação é {calculo}.')
            elif operacao_escolhida_int == 4:
                calculo = (num1_float / num2_float)
                print(f'A divisão é {calculo}.') 
            print('-='*30)
            saida = input('DESEJA SAIR DO PROGRAMA? ').lower()
        except ValueError:
            print('ERROR!!\n(OBS.: Você não digitou um número que indique a operação desejada.)')
    except ValueError:
        print('ERROR!!\n(OBS.: Você não digitou um número.)')
print('VOCÊ ENCERROU O PROGRAMA!')