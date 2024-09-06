from questao1 import calcular_soma
from questao2 import fibonacci
from questao4 import calcular_percentual_faturamento


def main():
    # Questão 1
    print(f"Resultado da Questão 1: {calcular_soma()}")

    # Questão 2
    numero = int(input("Informe um número para verificar na sequência de Fibonacci: "))
    if fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")

 # Questão 4
    faturamento = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }
    percentuais = calcular_percentual_faturamento(faturamento)
    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}%")


if __name__ == "__main__":
    main()
