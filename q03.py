import json

def analisar_faturamento(dados):
    # Filtra dias sem faturamento
    dias_validos = [dia for dia in dados if dia['valor'] > 0]
    
    if not dias_validos:
        return {
            'menor_valor': 0,
            'maior_valor': 0,
            'dias_acima_media': 0,
            'media_mensal': 0
        }
    
    # Extrai apenas os valores para cálculos
    valores = [dia['valor'] for dia in dias_validos]
    
    # Calcula o menor e maior valor
    menor_valor = min(valores)
    maior_valor = max(valores)
    
    # Calcula a média mensal (ignorando dias sem faturamento)
    media_mensal = sum(valores) / len(valores)
    
    # Conta dias acima da média
    dias_acima_media = len([dia for dia in dias_validos if dia['valor'] > media_mensal])
    
    return {
        'menor_valor': menor_valor,
        'maior_valor': maior_valor,
        'dias_acima_media': dias_acima_media,
        'media_mensal': media_mensal
    }

def main():
  with open('teste.json', 'r') as file: #mudar o nome do arquivo para o que você quiser
    dados = json.load(file)
  resultado = analisar_faturamento(dados)
  print("Resultados da análise de faturamento:")
  print(f"Menor valor de faturamento: R$ {resultado['menor_valor']:.2f}")
  print(f"Maior valor de faturamento: R$ {resultado['maior_valor']:.2f}")
  print(f"Número de dias acima da média: {resultado['dias_acima_media']}")
  print(f"Média mensal (excluindo dias sem faturamento): R$ {resultado['media_mensal']:.2f}")

if __name__ == '__main__':
  main()