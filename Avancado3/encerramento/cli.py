from prompts import obter_prompt_sistema
from memory import carregar_historico, salvar_historico
from ai_client import chat_completions, GroqAPIError
from utils import limitar_historico


def main():
    tema = input("Escolha o tema (motivacional/estudos/filmes) [estudos]: ").strip().lower() or "estudos"
    system_prompt = obter_prompt_sistema(tema)

    historico = carregar_historico()
    mensagens = [{"role": "system", "content": system_prompt}] + historico

    print("\n🤖 Assistente iniciado. Digite 'sair' para encerrar.\n")

    while True:
        user_text = input("Você: ").strip()
        if user_text.lower() in ("sair", "exit", "quit"):
            break

        mensagens.append({"role": "user", "content": user_text})
        mensagens = limitar_historico(mensagens, max_itens=14)

        try:
            resposta = chat_completions(mensagens)
        except GroqAPIError as e:
            print("❌ " + str(e))
            continue

        print("\nAssistente:", resposta, "\n")
        mensagens.append({"role": "assistant", "content": resposta})

        salvar_historico([m for m in mensagens if m["role"] != "system"])

    print("👋 Até mais! Bons estudos!")


if __name__ == "__main__":
    main()