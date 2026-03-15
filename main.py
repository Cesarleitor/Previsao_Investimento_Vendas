import pandas as pd
import matplotlib.pyplot as plt
import  sklearn as sk

data = pd.read_csv("dados_investimento.csv")

df = pd.DataFrame(data)

x = df[["investimentos"]]
y = df[["vendas"]]

x_train, x_test, y_train, y_test = sk.model_selection.train_test_split(x, y, test_size=0.2, random_state=42)

model = sk.linear_model.LinearRegression()
model.fit(x_train, y_train)

pred = model.predict(x_test)

def prev(invest):
    novo_dado = pd.DataFrame({"investimentos": [invest]})
    r = round(model.predict(novo_dado)[0][0])
    print(f"Número de vendas estimado: {r}.")

print("[!] Previsão de Renda [!]")
print("Ao realizar um investimento em marketing, gostaria de saber qual seria a estimativa para o número de vendas retornado")
print("O modelo de previsão já está funcionando! Gostaria de ver o resultado?\n")

while True:
    print("[1] Visualizar gráfico de previsão")
    print("[2] realizar teste de previsão")
    print("[3] Sair dp programa")
    opt = int(input("Digite a opção desejada: "))
    if opt == 1:
        plt.figure(figsize=(10, 6))
        plt.scatter(x_test, y_test, color='blue', label='Valores Reais')
        plt.plot(x_test,pred, color='red', label='Previsão', linewidth=2)
        plt.title("Previsão de renda com base em Vendas")
        plt.xlabel("Investimento ($)")
        plt.ylabel("Número de Vendas")
        plt.legend()
        plt.grid()
        plt.show()
    elif opt == 2:
        invest = float(input("Digite o valor do investimento: "))
        prev(invest)
    elif opt == 3:
        break
    else:
        print("Opção Inválida, Tente novamente!")

