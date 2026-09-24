import math

def calcular_expansao_exponencial(vetor, taxa_crescimento, periodos):
    """
    Calcula a projeção de expansão exponencial de vetores de contágio/endemia.
    
    :param vetor: lista de valores iniciais de focos/casos por região
    :param taxa_crescimento: taxa de reprodução/crescimento (ex: 0.15 para 15%)
    :param periodos: número de intervalos de tempo (dias/semanas)
    :return: lista com a projeção expandida para cada ponto do vetor
    """
    if not isinstance(vetor, list) or not vetor:
        raise ValueError("O vetor inicial deve ser uma lista não vazia.")
    if taxa_crescimento < 0 or periodos < 0:
        raise ValueError("Taxa e períodos devem ser valores não negativos.")

    resultado = []
    for foco in vetor:
        # Fórmula de crescimento exponencial: V_final = V_inicial * (1 + r)^t
        valor_projetado = foco * math.pow((1 + taxa_crescimento), periodos)
        resultado.append(round(valor_projetado, 2))
        
    return resultado

if __name__ == "__main__":
    focos_iniciais = [10, 25, 50, 100]
    taxa = 0.08  # 8% de crescimento
    tempo = 5     # 5 períodos
    
    projeçao = calcular_expansao_exponencial(focos_iniciais, taxa, tempo)
    print(f"Vetor Original: {focos_iniciais}")
    print(f"Projeção Exponencial ({tempo} períodos): {projeçao}")
