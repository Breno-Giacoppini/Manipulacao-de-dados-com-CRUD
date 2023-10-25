import json

# Função para ler os dados de um arquivo JSON
def ler_dados(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        dados = []
    return dados

# Função para escrever os dados em um arquivo JSON
def escrever_dados(dados, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

# Função para criar um novo registro
def criar_registro(nome_arquivo):
    try:
        dados = ler_dados(nome_arquivo)
        veiculo = input("Informe o veículo: ")
        nome_cliente = input("Informe o nome do cliente: ")
        try:
            ano_carro = int(input("Informe o ano do carro: "))
        except ValueError:
            print("\nAno do carro inválido. Deve ser um número.")
            return

        while True:
            cliente = input("Cliente? (S/N): ").strip().upper()

            if cliente == "S":
                cliente = "Sim"
                break
            elif cliente == "N":
                cliente = "Não"
                break
            else:
                print("\nOpção inválida. Digite 'S' para Sim ou 'N' para Não.")

        tipo_problema = input("Informe o tipo de problema: ")
        eixos = input("Informe o número de eixos: ")
        peso = input("Informe o peso: ")
        altura = input("Informe a altura: ")
        comprimento = input("Informe o comprimento: ")

        novo_registro = {
            "Veiculo": veiculo,
            "Nome do Cliente": nome_cliente,
            "Ano do Carro": ano_carro,
            "Cliente": cliente,
            "Tipo de Problema": tipo_problema,
            "eixos": eixos,
            "peso": peso,
            "altura": altura,
            "comprimento": comprimento
        }

        dados.append({"Registro " + str(len(dados) + 1): novo_registro})
        escrever_dados(dados, nome_arquivo)
    except Exception as e:
        print(f"Ocorreu um erro ao criar o registro: {e}")
    finally:
        print("\nRegistro criado com sucesso!")

# Função para listar todos os registros no formato desejado
def listar_registros(nome_arquivo):
    try:
        dados = ler_dados(nome_arquivo)
        for idx, registro in enumerate(dados, 1):
            chave = list(registro.keys())[0]
            valores = registro[chave]
            print(f"Registro {idx}:\n")
            for campo, valor in valores.items():
                if campo == "Cliente":
                    valor = "Sim" if valor == "Sim" else "Não"
                print(f"{campo}: {valor}")
            print()
    except Exception as e:
        print(f"Ocorreu um erro ao listar os registros: {e}")
    finally:
        print(f"Há o total de {idx} de registros em nosso banco de dados!")

# Função para atualizar um registro
def atualizar_registro(nome_arquivo):
    try:
        dados = ler_dados(nome_arquivo)
        listar_registros(nome_arquivo)
        try:
            indice = int(input("Informe o número do registro que deseja atualizar: ")) - 1
            if 0 <= indice < len(dados):
                veiculo = input("Informe o veículo: ")
                nome_cliente = input("Informe o nome do cliente: ")
                try:
                    ano_carro = int(input("Informe o ano do carro: "))
                except ValueError:
                    print("\nAno do carro inválido. Deve ser um número.")
                    return
                while True:
                    cliente = input("Cliente? (S/N): ").strip().upper()

                    if cliente == "S":
                        cliente = "Sim"
                        break
                    elif cliente == "N":
                        cliente = "Não"
                        break  # Mova o break aqui para encerrar o loop corretamente
                    else:
                        print("\nOpção inválida. Digite 'S' para Sim ou 'N' para Não.")

                tipo_problema = input("Informe o tipo de problema: ")
                eixos = input("Informe o número de eixos: ")
                peso = input("Informe o peso: ")
                altura = input("Informe a altura: ")
                comprimento = input("Informe o comprimento: ")

                novo_registro = {
                    "Veiculo": veiculo,
                    "Nome do Cliente": nome_cliente,
                    "Ano do Carro": ano_carro,
                    "Cliente": cliente,
                    "Tipo de Problema": tipo_problema,
                    "eixos": eixos,
                    "peso": peso,
                    "altura": altura,
                    "comprimento": comprimento
                }

                dados[indice] = {"Registro " + str(indice + 1): novo_registro}
                escrever_dados(dados, nome_arquivo)
            else:
                print("\nÍndice inválido.")
        except Exception as e:
            print(f"Ocorreu um erro ao atualizar o registro: {e}")
    finally:
            print("\nRegistro atualizado com sucesso!")

# Função para excluir um registro
def excluir_registro(nome_arquivo):
    dados = ler_dados(nome_arquivo)
    listar_registros(nome_arquivo)
    try:
        indice = int(input("\nInforme o número do registro que deseja excluir: ")) - 1
        if 0 <= indice < len(dados):
            del dados[indice]
            escrever_dados(dados, nome_arquivo)
            print("\nRegistro excluído com sucesso!")
        else:
            print("\nÍndice inválido.")
    except ValueError:
        print("\nNúmero de registro inválido.")

# Função principal do programa
def main():
    nome_arquivo = "Banco.json" 
    while True:
        print("\nMenu Principal:\n")
        print("1. Criar Registro")
        print("2. Listar Registros")
        print("3. Atualizar Registro")
        print("4. Excluir Registro")
        print("5. Sair\n")

        try:
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                criar_registro(nome_arquivo)
            elif opcao == 2:
                listar_registros(nome_arquivo)
            elif opcao == 3:
                atualizar_registro(nome_arquivo)
            elif opcao == 4:
                excluir_registro(nome_arquivo)
            elif opcao == 5:
                break
            else:
                print("\nOpção inválida. Tente novamente.")
        except ValueError:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
