import json


def processar_faturamento(arquivo):
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

    print(f"Menor valor de faturamento: {menor_valor:.2f}")
    print(f"Maior valor de faturamento: {maior_valor:.2f}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_media}")


if __name__ == "__main__":
    processar_faturamento('faturamento.json')
