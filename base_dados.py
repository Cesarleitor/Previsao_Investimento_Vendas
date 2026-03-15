import pandas as pd

dados = {

    'investimentos': [1000, 2000, 4000, 5000, 8000, 10000, 15000, 20000, 25000, 30000, 35000, 40000,45000, 50000],
    'vendas': [20,38,80,101,164,201,300,410,499,602,703,820,900,996]
}

df = pd.DataFrame(dados)

print(df)

df.to_csv("dados_investimento.csv", index=False)