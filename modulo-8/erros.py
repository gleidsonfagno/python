from functools import reduce

def processar_faturas(nome_arquivo: str):

  faturas = []

  with open(file=nome_arquivo, mode='r', encoding='utf8') as arquivo:
    linha = arquivo.readline()
    linha = arquivo.readline()
    while linha:
      try:
        fatura = float(linha.strip().split(sep=',')[-3])
      except ValueError as exc:
        raise ValueError(f'Falha ao processar as faturas devido ao seguinte erro: "{exc}"')
      else:
        faturas.append(fatura)
      linha = arquivo.readline()

  total_a_pagar = reduce(lambda x, y: x + y, faturas)
  total_a_pagar = round(total_a_pagar, 2)

  return total_a_pagar