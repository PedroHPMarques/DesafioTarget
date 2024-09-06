def calcular_percentual_faturamento(faturamento):
    total = sum(faturamento.values())
    percentuais = {estado: (valor / total) * 100 for estado, valor in faturamento.items()}
    return percentuais
