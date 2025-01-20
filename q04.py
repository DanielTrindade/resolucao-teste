def calcular_percentuais(faturamento):
    valor_total = sum(faturamento.values())
    percentuais = {}
    for estado, valor in faturamento.items():
        percentual = (valor / valor_total) * 100
        percentuais[estado] = percentual
    
    return percentuais, valor_total

def main():
    faturamento = {
        'SP': 67836.43,
        'RJ': 36678.66,
        'MG': 29229.88,
        'ES': 27165.48,
        'Outros': 19849.53
    }
    
    percentuais, total = calcular_percentuais(faturamento)
    
  
    print('\nFaturamento por Estado:')
    print('-' * 50)
    print(f'Valor total de faturamento: R$ {total:.2f}\n')
    print('Percentual de representação por estado:')
    
    # Ordena os estados por percentual de participação (decrescente)
    estados_ordenados = sorted(percentuais.items(), key=lambda x: x[1], reverse=True)
    
    for estado, percentual in estados_ordenados:
        valor = faturamento[estado]
        print(f'{estado}: R$ {valor:.2f} ({percentual:.2f}%)')

if __name__ == "__main__":
    main()