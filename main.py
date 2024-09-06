from questao1 import calcular_soma
from questao2 import fibonacci


def main():
    # Questão 1
    print(f"Resultado da Questão 1: {calcular_soma()}")

    numero = int(input("Informe um número para verificar na sequência de Fibonacci: "))
    if fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")


if __name__ == "__main__":
    main()
