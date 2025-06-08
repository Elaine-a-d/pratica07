
import json
import os # Importar para verificar o caminho do arquivo

def manipular_arquivo_json(nome_arquivo='pessoa.json'):
    """
    Escreve dados de uma pessoa em um arquivo JSON e depois os lê de volta.
    """
    # 1. Definir os dados da pessoa como um dicionário Python
    dados_pessoa = {
        "nome": "João Silva",
        "idade": 35,
        "cidade": "Florianópolis"
    }

    print(f"--- Escrevendo dados no arquivo JSON: {nome_arquivo} ---")
    try:
        # 2. Escrever os dados em JSON
        # 'w' para escrita, encoding='utf-8' para caracteres especiais
        # indent=4 para formatar o JSON com identação de 4 espaços, tornando-o legível
        with open(nome_arquivo, mode='w', encoding='utf-8') as arquivo_json_escrita:
            json.dump(dados_pessoa, arquivo_json_escrita, indent=4)
        print(f"Dados da pessoa escritos com sucesso em '{nome_arquivo}'.")

    except IOError as e:
        print(f"Erro de I/O ao escrever no arquivo '{nome_arquivo}': {e}")
        return # Encerrar a função se a escrita falhar
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao escrever: {e}")
        return # Encerrar a função se a escrita falhar

    print(f"\n--- Lendo dados do arquivo JSON: {nome_arquivo} ---")
    try:
        # 3. Ler os dados do JSON
        # 'r' para leitura
        with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo_json_leitura:
            dados_lidos = json.load(arquivo_json_leitura)
        print(f"Dados lidos com sucesso de '{nome_arquivo}'.")

        # 4. Exibir os dados lidos
        print("\nInformações da Pessoa Lida:")
        print(f"Nome: {dados_lidos.get('nome', 'N/A')}")
        print(f"Idade: {dados_lidos.get('idade', 'N/A')}")
        print(f"Cidade: {dados_lidos.get('cidade', 'N/A')}")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado. Certifique-se de que ele foi criado.")
    except json.JSONDecodeError as e:
        print(f"Erro: O arquivo '{nome_arquivo}' não contém um JSON válido: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao ler: {e}")

# --- Execução principal ---
if __name__ == "__main__":
    # Caminho do arquivo JSON
    # Você pode definir um caminho absoluto se quiser, mas relativo é mais flexível
    arquivo_json_nome = "pessoa.json"
    
    # Para verificar se o script está rodando na pasta certa
    print(f"Diretório de trabalho atual: {os.getcwd()}")
    
    manipular_arquivo_json(arquivo_json_nome)