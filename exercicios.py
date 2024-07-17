#1
#n1 = int(input())
#n2 = int(input())
#print("1-Soma, 2-Subtração, 3-Multiplicação, 4-Divisão")
#op = int(input())

#if op == 1:
#    r = n1+n2
#    print("resultado da soma: ", r)
#elif op == 2:
#    r = n1-n2
#    print("resultado da soma: ", r)
#elif op == 3:
#    r = n1*n2
#    print("resultado da soma: ", r)
#elif op == 4:
#    if n2 == 0 and n1 == 0:
#        print("Não tem divisão com zero")
#   else:
#        r = n1/n2
#        print("resultado da soma: ", r)
#else:
#    print("Operação inválida")

#print("TABUADA")
#n1 =int(input())
#for i in range(1,11):
   # r = n1*i
   # print(n1,"X",i,"=",r)

#3
#n =int(input())
#fatorial = 1

#for i in range(1, n + 1):
#    fatorial *= i

#print(fatorial)

#4
#n1 =int(input())
#n2 =int(input())
#n3 =int(input())

#maior = max(n1,n2,n3)
#print("O maior nº é ", maior)

#5
#string = input()
#string_invertida = ''.join(reversed(string))
#print(string_invertida)

#6
#texto = input()
#vogais = "aeiou"
#numero_de_vogais = sum(letra in vogais for letra in texto.lower())
#print("Número de vogais:", numero_de_vogais)


#7
#N = int(input("Digite o número até o qual você deseja imprimir números primos: "))

#for num in range(2, N + 1):
#    for i in range(2, num):
#        if (num % i) == 0:
#            break
#    else:
#        print(num)

#8
#N = int(input("Digite o número de termos da sequência de Fibonacci que você deseja: "))

#a, b = 0, 1
#for i in range(N):            
#    print(a)
#    a, b = b, a + b

#9
#texto = input("Digite a string que você deseja verificar: ")

#texto = texto.replace(' ', '').lower()
#if texto == ''.join(reversed(texto)):
#    print("A string é um palíndromo.")
#else:
#    print("A string não é um palíndromo.")

#10
print("Escolha a conversão desejada:")
print("1. Celsius para Fahrenheit")
print("2. Fahrenheit para Celsius")
opcao = int(input("Digite sua opção (1 ou 2): "))

temperatura = float(input("Digite a temperatura a ser convertida: "))

if opcao == 1:
    resultado = temperatura * 9/5 + 32
    print(f"A temperatura em Fahrenheit é {resultado}°F.")
elif opcao == 2:
    resultado = (temperatura - 32) * 5/9
    print(f"A temperatura em Celsius é {resultado}°C.")
else:
    print("Opção inválida.")





