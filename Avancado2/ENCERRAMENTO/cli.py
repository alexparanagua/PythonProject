import json
import urllib.request
import urllib.error
from datetime import datetime

# URL base da sua API FastAPI
API_URL = "http://127.0.0.1:8000/tarefas"
# Token que definimos na sua validação do FastAPI
TOKEN = "meutoken"


def enviar_requisicao(url, metodo="GET", dados=None):
    """Função utilitária para fazer chamadas HTTP na API usando urllib"""
    req = urllib.request.Request(url, method=metodo)
    req.add_header("Authorization", f"Bearer {TOKEN}")
    req.add_header("Content-Type", "application/json")

    corpo_requisicao = None
    if dados:
        corpo_requisicao = json.dumps(dados).encode("utf-8")

    try:
        with urllib.request.urlopen(req, data=corpo_requisicao) as response:
            # CORREÇÃO: Verifica se o status retornado é 200 ou 201
            if 200 <= response.status <= 299:
                return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        erro_msg = e.read().decode("utf-8")
        print(f"\n[Erro {e.code}]: {erro_msg}")
    except urllib.error.URLError:
        print("\n[Erro]: Não foi possível conectar à API. O Uvicorn está rodando?")
    return None


def menu_listar():
    print("\n--- LISTAR TAREFAS ---")
    pagina = input("Deseja paginação? Digite o número da página (ou Enter para tudo): ")
    if pagina == '':
        pagina='1'
        tamanho='10'
    url = API_URL
    if pagina.strip():
        if tamanho!='10':
            tamanho = input("Quantidade por página (padrão 10): ") or "10"
        url = f"{API_URL}?pagina={pagina}&tamanho={tamanho}"

    resultado = enviar_requisicao(url, "GET")
    if resultado:
        print(f"\n{'ID':<5} | {'TÍTULO':<20} | {'CONCLUÍDA':<10} | {'CRIADA EM'}")
        print("-" * 60)
        for t in resultado:
            status = "Sim" if t.get("concluida") else "Não"
            print(f"{t.get('id'):<5} | {t.get('titulo'):<20} | {status:<10} | {t.get('criada')}")


def menu_buscar_por_id():
    print("\n--- BUSCAR TAREFA POR ID ---")
    tarefa_id = input("Digite o ID da tarefa: ")
    if not tarefa_id.strip(): return

    resultado = enviar_requisicao(f"{API_URL}/{tarefa_id}", "GET")
    if resultado:
        print(f"\nID: {resultado.get('id')}")
        print(f"Título: {resultado.get('titulo')}")
        print(f"Descrição: {resultado.get('descricao')}")
        print(f"Concluída: {'Sim' if resultado.get('concluida') else 'Não'}")
        print(f"Criada em: {resultado.get('criada')}")


def menu_inserir():
    print("\n--- CADASTRAR NOVA TAREFA ---")
    titulo = input("Título: ")
    descricao = input("Descrição: ")
    data_iso = datetime.now().isoformat(timespec='seconds')

    # Monta em lote (Lista) conforme sua rota @app.post espera
    nova_tarefa = [{
        "id": None,
        "titulo": titulo,
        "descricao": descricao,
        "concluida": False,
        "criada": data_iso
    }]

    resultado = enviar_requisicao(API_URL, "POST", dados=nova_tarefa)
    if resultado:
        print(f"\nSucesso: {resultado.get('mensagem')}")


def menu_atualizar():
    print("\n--- ATUALIZAR TAREFA ---")
    tarefa_id = input("ID da tarefa que deseja alterar: ")
    if not tarefa_id.strip(): return

    print("Insira os novos dados:")
    titulo = input("Novo Título: ")
    descricao = input("Nova Descrição: ")
    concluida_input = input("Concluída? (s/n): ").lower()
    concluida = True if concluida_input == 's' else False
    data_iso = datetime.now().isoformat(timespec='seconds')

    tarefa_editada = [{
        "id": int(tarefa_id),
        "titulo": titulo,
        "descricao": descricao,
        "concluida": concluida,
        "criada": data_iso
    }]

    resultado = enviar_requisicao(API_URL, "PUT", dados=tarefa_editada)
    if resultado:
        print(f"\nSucesso: {resultado.get('mensagem')}")


def menu_excluir():
    print("\n--- EXCLUIR TAREFA ---")
    tarefa_id = input("ID da tarefa que deseja deletar: ")
    if not tarefa_id.strip(): return

    # Sua rota @app.delete espera receber o objeto para ler o obj.id
    tarefa_deletar = [{"id": int(tarefa_id), "titulo": "", "descricao": "", "criada": ""}]

    resultado = enviar_requisicao(API_URL, "DELETE", dados=tarefa_deletar)
    if resultado:
        print(f"\nSucesso: {resultado.get('mensagem')}")


def principal():
    while True:
        print("\n==============================")
        print("    SISTEMA DE TAREFAS CLI")
        print("==============================")
        print("[1] Listar Tarefas (Tudo / Paginado)")
        print("[2] Buscar Tarefa por ID")
        print("[3] Inserir Nova Tarefa")
        print("[4] Atualizar Tarefa")
        print("[5] Excluir Tarefa")
        print("[0] Sair")
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            menu_listar()
        elif opcao == "2":
            menu_buscar_por_id()
        elif opcao == "3":
            menu_inserir()
        elif opcao == "4":
            menu_atualizar()
        elif opcao == "5":
            menu_excluir()
        elif opcao == "0":
            print("\nEncerrando aplicação CLI. Até logo!")
            break
        else:
            print("\nOpção inválida! Tente novamente.")


if __name__ == "__main__":
    principal()
