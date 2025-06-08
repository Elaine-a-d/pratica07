
import csv

def escrever_dados_csv(nome_arquivo='pessoas.csv'):
    """
    Cria um arquivo CSV e escreve informações de pessoas (Nome, Idade, Cidade).

    Args:
        nome_arquivo (str): O nome do arquivo CSV a ser criado/escrito.
    """
    # 1. Definir os dados das pessoas
    dados_pessoas = [
        {"Nome": "Alice", "Idade": 30, "Cidade": "São Paulo"},
        {"Nome": "Bruno", "Idade": 25, "Cidade": "Rio de Janeiro"},
        {"Nome": "Carla", "Idade": 22, "Cidade": "Belo Horizonte"},
        {"Nome": "Daniel", "Idade": 40, "Cidade": "Curitiba"},
        {"Nome": "Elaine", "Idade": 28, "Cidade": "Brasília"}
    ]

    # 2. Definir os cabeçalhos das colunas
    # As chaves dos dicionários em dados_pessoas devem corresponder a esses cabeçalhos
    cabecalhos = ["Nome", "Idade", "Cidade"]

    print(f"Tentando criar/escrever no arquivo: {nome_arquivo}")

    try:
        # 3. Abrir o arquivo CSV para escrita
        # 'w' para escrita, newline='' é importante para evitar linhas em branco extras
        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
            # 4. Criar um csv.DictWriter
            # fieldnames especifica a ordem dos cabeçalhos e mapeia as chaves do dicionário
            writer = csv.DictWriter(arquivo_csv, fieldnames=cabecalhos)

            # 5. Escrever o cabeçalho no arquivo
            writer.writeheader()
            print("Cabeçalhos escritos com sucesso.")

            # 6. Escrever as linhas de dados
            for pessoa in dados_pessoas:
                writer.writerow(pessoa)
                print(f"Dados escritos para: {pessoa['Nome']}")

        print(f"\nDados de pessoas escritos com sucesso em '{nome_arquivo}'")

    except IOError as e:
        print(f"Erro de I/O ao escrever no arquivo '{nome_arquivo}': {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# --- Execução principal ---
if __name__ == "__main__":
    escrever_dados_csv()
    