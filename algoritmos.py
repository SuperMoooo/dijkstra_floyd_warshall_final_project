from utils import *

def dijkstra(rede : dict):
    vertice_origem = 0
    vertice_destino = 0

    vertices_na_rede : list = rede["vertices"]
    arcos_na_rede : list = rede["arcos"]

    print("Vértices: ", vertices_na_rede)

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

    # caminho final
    caminhos = [{
        "caminho": [vertice_origem],
        "custos": [0]
    }]

    # passos
    passo = 1


    # vértices escolhidos
    permanentes = [vertice_origem]
    # vértices por usar
    temporarios = [i for i in vertices_na_rede if i != vertice_origem]

    # histórico de todos os caminhos
    # cada vértice vai ter o seu historico
    historico = {}

    # melhores custos por vértice
    melhores_custos = {}
    for vertice in vertices_na_rede:
        melhores_custos[vertice] = {
            "custo": float("inf"),
            "origem": None
        }
    melhores_custos[vertice_origem] = {
        "custo": 0,
        "origem": None
    }

    while permanentes[-1] != vertice_destino:

        # guardar o vértice que estamos a testar
        vertice_key = permanentes[-1]

        # e adicionar ao histórico
        if historico.get(vertice_key) == None:
            historico[vertice_key] = [[]]
        

        if passo - 1 != 0:
            # garantir que existe a lista do lado direito do passo atual
            historico[vertice_key].append([])

            for arco in historico[permanentes[-2]][-1]:
                historico[vertice_key][-2].append({
                    "de": arco["de"],
                    "para": arco["para"],
                    "custo": arco["custo"],
                    "anterior": True
                    })

        # vai vértice a vértice dos temporários
        for vertice_temp in temporarios:
            # Adicionar ao historico de passos o passo anterior para saber o mínimo
            # para cada vértice vai ver todos os arcos
            for arco in arcos_na_rede:
                # se houver arco do vértice que estamos a testar e do vértice temp
                if arco["de"] == vertice_key and arco["para"] == vertice_temp:
                    # guardar no passo atual todos os caminhos possiveis e o seu custo
                    custo_total = arco["custo"]
                    if passo > 1:
                        custo_total = arco["custo"] + caminhos[-1]["custos"][-1]
                    historico[vertice_key][-1].append({
                        "de": vertice_key,
                        "para": vertice_temp,
                        "custo": custo_total,
                        "anterior": False
                    })
                    if custo_total < melhores_custos[vertice_temp]["custo"]:
                        melhores_custos[vertice_temp] = {
                            "custo": custo_total,
                            "origem": vertice_key
                        }

            if vertice_temp not in (arco["para"] for arco in historico[vertice_key][-1]):
                # guardar como infinito
                historico[vertice_key][-1].append({
                    "de": vertice_key,
                    "para": vertice_temp,
                    "custo": float("inf"),
                    "anterior": False
                })
      
            
        # escolher o vértice com valor mais pequeno
   
        min_vertice = vertice_custo_minimo(temporarios, melhores_custos)

        # ATUAL
        min_custo = melhores_custos[min_vertice]["custo"]
        vert_origem = melhores_custos[min_vertice]["origem"]

        


        if min_custo == float("inf"):
            raise Exception(f"Não existe caminho possível no {passo}º passo")
        permanentes.append(min_vertice)
        temporarios.remove(min_vertice)

        # guardar o novo caminho
        novo_caminho = []
        for vertice in caminhos[-1]["caminho"]:
            novo_caminho.append(vertice)
            if vertice == vert_origem:
                break
        novo_caminho.append(min_vertice)

        # guardar os novos custos
        novos_custos = []
        contador = 0
        for custo in caminhos[-1]["custos"]:
            novos_custos.append(custo)
            if custo == min_custo or contador == len(novo_caminho):
                break
            contador += 1
        novos_custos.append(min_custo)
       
        caminhos.append({
            "caminho": novo_caminho,
            "custos": novos_custos
        })

        print(f"PASSO {passo} FEITO")
        passo += 1

    return caminhos


def floyd_warshall(rede : dict):
    pass
