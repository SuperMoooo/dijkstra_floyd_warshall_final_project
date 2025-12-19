def vertice_custo_minimo(temporarios, melhores_custos):
    min_vertice = min(
        temporarios,
        key=lambda vertice: melhores_custos[vertice]["custo"]
    )
    return min_vertice

