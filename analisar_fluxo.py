import pandas as pd
from collections import Counter
import numpy as np

def analisar_fluxo_vetorial(transacoes):
    entropia_por_endereco = {}
    ocorrencias = Counter(transacoes['from'].tolist() + transacoes['to'].tolist())

    for endereco, count in ocorrencias.items():
        fluxos = transacoes[(transacoes['from'] == endereco) | (transacoes['to'] == endereco)]
        tempos = fluxos['timestamp'].diff().fillna(0).values
        variacao_temporal = np.std(tempos)
        entropia = np.log1p(variacao_temporal) / (np.log1p(count) + 1e-5)
        entropia_por_endereco[endereco] = entropia

    anomalias = {k: v for k, v in entropia_por_endereco.items() if v < 0.1 and ocorrencias[k] > 2}

    return {
        'entropia_por_endereco': entropia_por_endereco,
        'possiveis_carteiras_abandonadas': anomalias
    }

if __name__ == "__main__":
    df = pd.read_csv("data/transacoes_simuladas.csv")
    resultado = analisar_fluxo_vetorial(df)
    print("Carteiras possivelmente abandonadas:")
    for carteira, entropia in resultado["possiveis_carteiras_abandonadas"].items():
        print(f"{carteira} — entropia: {entropia:.4f}")
