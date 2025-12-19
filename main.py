# 4 - Problema de determinacão do caminho de custo mínimo numa rede orientada
# (a) Criação de um gerador de redes com determinado número de vértices e arcos;
# (b) Implementação dos algoritmos de Dijkstra e Floyd-Warshall 
# e discussão do seu desempenho nas redes geradas.
# (c) Comparação com outros algoritmos que possam ser relevantes neste contexto.

# Nota: Não precisa ser conexo, Dijkstra só custo positivo,
# Floyd-Warshall aceita custo negativo, mas não ciclos negativos

import gerador_redes, algoritmos


if __name__ == "__main__":
    # gerar_rede(numero de vertices, numero de arcos, custo_minimo ,custo_maximo)
    rede = gerador_redes.gerar_rede(10, 20, 0, 20)
    print(rede)
    try:
        caminhos = algoritmos.dijkstra(rede)
        print(caminhos)
        print("Caminho Final: ", caminhos[-1])
    except Exception as e:
        print(e)

    # algoritmos.floyd_warshall(rede)
    pass