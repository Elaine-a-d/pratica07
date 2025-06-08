
import re
import statistics

def analisar_log_treinamento(nome_arquivo='log_treinamento.txt'):
    """
    Lê um arquivo de log de treinamento de ML, extrai os tempos de execução
    e calcula a média e o desvio padrão desses tempos.
    """
    tempos_execucao = []
    # Expressão regular para encontrar "Tempo de execução: XX.YY segundos"
    # Captura o número que pode ser inteiro ou decimal.
    padrao_tempo = re.compile(r"Tempo de execução: (\d+\.?\d*) segundos")

    print(f"Tentando abrir o arquivo: {nome_arquivo}") # LINHA DE DEBUG

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            for numero_linha, linha in enumerate(arquivo, 1):
                print(f"Lendo linha {numero_linha}: '{linha.strip()}'") # LINHA DE DEBUG: mostra o conteúdo da linha
                match = padrao_tempo.search(linha)
                if match:
                    try:
                        tempo_str = match.group(1)
                        print(f"  -> Match encontrado na linha {numero_linha}: '{tempo_str}'") # LINHA DE DEBUG
                        tempo_float = float(tempo_str)
                        tempos_execucao.append(tempo_float)
                    except ValueError:
                        print(f"Aviso: Não foi possível converter '{tempo_str}' para float na linha {numero_linha}.")
                else:
                    print(f"  -> Nenhum match encontrado na linha {numero_linha}.") # LINHA DE DEBUG
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return None, None
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
        return None, None

    print(f"Tempos de execução coletados (final): {tempos_execucao}") # LINHA DE DEBUG

    if not tempos_execucao:
        print("Nenhum tempo de execução válido foi encontrado no log.")
        return None, None
    elif len(tempos_execucao) == 1:
        print("Apenas um tempo de execução encontrado. O desvio padrão será 0.")
        media = tempos_execucao[0]
        desvio_padrao = 0.0
    else:
        media = statistics.mean(tempos_execucao)
        desvio_padrao = statistics.stdev(tempos_execucao)

    return media, desvio_padrao

# --- Execução principal ---
if __name__ == "__main__":
    media_tempo, desvio_padrao_tempo = analisar_log_treinamento()

    if media_tempo is not None:
        print(f"\n--- Resultados da Análise ---")
        print(f"Média do tempo de execução: {media_tempo:.2f} segundos")
        print(f"Desvio padrão do tempo de execução: {desvio_padrao_tempo:.2f} segundos")