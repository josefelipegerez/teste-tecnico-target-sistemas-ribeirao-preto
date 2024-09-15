# questao_1.py
def pertence_fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num or a == num

# Definindo o número a ser verificado
numero = int(input("Informe um número: "))

# Verificando se o número pertence à sequência de Fibonacci
if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
