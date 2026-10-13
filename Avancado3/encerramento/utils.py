def limitar_historico(mensagens, max_itens=12):
    if len(mensagens) <= max_itens:
        return mensagens
    return mensagens[-max_itens:]