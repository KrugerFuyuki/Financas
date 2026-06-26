import json
import os

lancamentos_json = 'lancamentos.json'

def carregar_lancamentos():
    if os.path.exists(lancamentos_json):
        with open(lancamentos_json, "r", encoding="utf-8") as f:
            return json.load(f)

    return {"lançamentos": []}

def salvar_lancamentos(dados):
    with open(lancamentos_json, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

lancamentos_salvos = carregar_lancamentos()

receitas = {}

while True:
    try:
        print("\nAs opções que podem ser utilizadas são:")

        print("1 - Registrar (receita ou dispesa nova)")
        print("2 - Ver extrato")
        print("3 - Relatório de saldo")
        print("4 - Gerar um relatório.txt")
        print("5 - Encerrar operação")

        opcao = input("escolha a operação que deseja prosseguir com:")

        if opcao == "1":

        elif opcao == "2":

        elif opcao == "3":

        elif opcao == "4":

        elif opcao == "5":
            print("Agradecemos pelo uso do nosso sistema, até!!")
            break

        else:
            print("Opção inválida! Por favor, escolha um número de 1 a 5.")

    except Exception as e:
        print(f"\nUm erro inesperado aconteceu")