# LaunchLab UniFAP - Desenvolvimento ADS
# Código de projeção de focos epidemiológicos

def calcular_projecao_focos(focos_atuais, taxa_reproducao, periodos):
    print("--- MONITORAMENTO DE ENDEMIAS UniFAP ---")

    # Crescimento linear
    focos_projetados = focos_atuais + (taxa_reproducao * periodos)

    return focos_projetados


if __name__ == "__main__":
    print(f"Total Projetado: {calcular_projecao_focos(10, 1.5, 4)}")