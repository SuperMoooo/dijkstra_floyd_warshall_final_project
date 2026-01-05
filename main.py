# 4 - Problema de determinacão do caminho de custo mínimo numa rede orientada
# (a) Criação de um gerador de redes com determinado número de vértices e arcos;
# (b) Implementação dos algoritmos de Dijkstra e Floyd-Warshall 
# e discussão do seu desempenho nas redes geradas.
# (c) Comparação com outros algoritmos que possam ser relevantes neste contexto.

# Nota: Não precisa ser conexo, Dijkstra só custo positivo,
# Floyd-Warshall aceita custo negativo, mas não ciclos negativos

import gerador_redes, algoritmos
import time

if __name__ == "__main__":
    # gerar_rede(numero de vertices, numero de arcos, custo_minimo ,custo_maximo)
    rede = gerador_redes.gerar_rede(10, 20, 0, 20)
    print(rede)

    vertice_origem = 0
    vertice_destino = 0

    vertices_na_rede : list = rede["vertices"]
    arcos_na_rede : list = rede["arcos"]

     # loop enquanto o utilizador não escolher um vértice que exista na rede
    while vertice_origem not in vertices_na_rede:
        if vertice_origem != 0:
            print("Erro! O vértice de origem escolhido não é válido.")

        vertice_origem = int(input("Digite o vértice de ORIGEM: "))

    # ´´ e verifica se o vértice de destion é diferente do da origem
    while vertice_destino not in vertices_na_rede or vertice_destino == vertice_origem:
        if vertice_destino != 0:
            print("Erro! O vértice de destino escolhido não é válido.")

        vertice_destino = int(input("Digite o vértice de DESTINO: "))

        
    print(":::::::::::::::::::// DIJKSTRA //:::::::::::::::::::")
    try:
        inicio_tempo = time.time()
        caminhos = algoritmos.dijkstra(rede, vertice_origem, vertice_destino, vertices_na_rede, arcos_na_rede)
        fim_tempo = time.time()
        print("Caminhos: ",caminhos)
        print("----------------------------------------------------")
        print("Caminho custo mínimo: ", caminhos[-1])
        print("Tempo de execução: ", fim_tempo - inicio_tempo)
        print("----------------------------------------------------")
    except Exception as e:
            print(e)
    try:
        print(":::::::::::::::::::// FLOYD WARSHALL //:::::::::::::::::::")
        
        inicio_tempo = time.time()
        pesos = algoritmos.floyd_warshall(vertice_origem, vertice_destino, vertices_na_rede, arcos_na_rede)
        fim_tempo = time.time()

        caminho = [vertice_origem]
        x = vertice_origem - 1
        y = vertice_destino - 1
        while caminho[-1] != vertice_destino:
            caminho.append(pesos[x][y])
            x = pesos[x][y] - 1
        
        print("----------------------------------------------------")
        print("Caminho custo mínimo: ", caminho)
        print("Tempo de execução: ", fim_tempo - inicio_tempo)
        print("----------------------------------------------------")
        print("::::::::::::::::::://:::::::::::::::::::")
    except Exception as e:
            print(e)