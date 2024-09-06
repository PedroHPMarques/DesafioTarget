from questao1 import calcular_soma
from questao2 import fibonacci
from questao4 import calcular_percentual_faturamento
from questao5 import inverter_string
import json


def executar_questao1():
    print("\n===== Questão 1: Soma de Números =====")
    print(f"Resultado da Questão 1: {calcular_soma()}")


def executar_questao2():
    print("\n===== Questão 2: Verificar Fibonacci =====")
    try:
        numero = int(input("Informe um número para verificar na sequência de Fibonacci: "))
        if fibonacci(numero):
            print(f"O número {numero} pertence à sequência de Fibonacci.")
        else:
            print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
    except ValueError:
        print("Por favor, insira um número inteiro válido.")


def processar_faturamento(arquivo):
    print("\n===== Questão 3: Processar Faturamento =====")
    with open(arquivo, 'r') as file:
        dados = json.load(file)

    valores = [item['valor'] for item in dados if item['valor'] > 0]

    if not valores:
        print("Não há faturamento para processar.")
        return

    menor_valor = min(valores)
    maior_valor = max(valores)
    media_mensal = sum(valores) / len(valores)
    dias_acima_media = sum(1 for valor in valores if valor > media_mensal)

    print(f"Menor valor de faturamento: {menor_valor: .2f}")
    print(f"Maior valor de faturamento: {maior_valor: .2f}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_media}")


def executar_questao4():
    print("\n===== Questão 4: Percentual de Faturamento por Estado =====")
    faturamento = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }
    percentuais = calcular_percentual_faturamento(faturamento)
    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual: .2f}%")


def executar_questao5():
    print("\n===== Questão 5: Inversão de String =====")
    string = input("Informe uma string para inverter: ")
    print(f"String invertida: {inverter_string(string)}")


def main():
    executar_questao1()
    executar_questao2()
    processar_faturamento('faturamento.json')
    executar_questao4()
    executar_questao5()


if __name__ == "__main__":
    main()
