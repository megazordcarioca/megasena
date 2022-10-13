from random import shuffle
import pandas as pd
import json, numpy, requests, csv, emoji

filePath = "./src/lotofacil.csv"


def webScrapping():
    print("Sincronizando dados...Isso pode demorar um pouco")
    data = {}
    request = requests.get(
        "https://loteriascaixa-api.herokuapp.com/api/lotofacil"
    )  # Pega os resultados por meio de um método GET
    print("Dados coletados!")
    data = json.loads(
        request.content
    )  # Itera em cima dos response e extrai os resultdados
    print("Criando a planilha e escrevendo dados")

    with open(filePath, "w") as f:  # Escreve os resultados em um csv novo ou sobrescreve
        es = csv.DictWriter(f, fieldnames=data[0].keys())
        es.writeheader()
        es.writerows(data)

    print("Dados adquiridos com sucesso! Segura minha cerveja, eu assumo daqui. Pode beber se quiser")


def dataMining():
    df = pd.read_csv(filePath)
    filtred_data = df.filter(items=["dezenas"])
    print(filtred_data)


def lotofacil():
    x = [[i] for i in range(1, 25)]
    shuffle(x)
    print(x[0:14])


def main():
    print(webScrapping())
    print(dataMining())


print(main())
