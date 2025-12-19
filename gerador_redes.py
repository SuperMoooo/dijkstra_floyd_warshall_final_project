import random
def gerar_rede(n_vertices : int, n_arcos : int, custo_min : int, custo_max : int):
    rede = []

    # armazenar todos os vértices
    vertices = [i for i in range(1, n_vertices + 1)]

    arcos = []

    # armazenar todos os arcos
    for _ in range(n_arcos + 1):
        de = random.choice(vertices)
        para = random.choice(vertices)
        
        # Enquanto for arco para si mesmo, encontra novos vértices
        while de == para:
            de = random.choice(vertices)
            para = random.choice(vertices)

        arcos.append({
            "de": de,
            "para": para,
            "custo": random.randint(custo_min, custo_max)
        })
    
    rede = {
        "vertices": vertices,
        "n_vertices": n_vertices,
        "arcos": arcos,
        "n_arcos": n_arcos
    }


    return rede
