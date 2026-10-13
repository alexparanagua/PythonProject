def obter_cidade_por_cep(cep: str, consulta_cep) -> str:
    """
    consulta_cep: função/callable que recebe um CEP e devolve um dict
    Ex.: {"cidade": "Votorantim", "uf": "SP"}
    """
    dados = consulta_cep(cep)
    return dados["cidade"]