from pywinauto.application import Application
from pywinauto import Desktop
from pywinauto.keyboard import send_keys
from time import sleep

# 1. Inicia o Bloco de Notas e aguarda abrir
app = Application(backend="win32").start('notepad.exe Teste.txt')
sleep(1)

# 2. VERIFICAÇÃO OBJETIVA: Procura qualquer diálogo de aviso ativo na tela
desktop = Desktop(backend="uia")

# Buscamos por janelas flutuantes ativas que pertençam ao Bloco de Notas
# No Win11, ela se identifica pelo control_type "Window" ou "Dialog" e herda o foco
dialogo_aberto = desktop.window(active_only=True, control_type="Window")

# Se o título da janela ativa for o aviso ou contiver o ID do Bloco de Notas, confirmamos
# Caso o arquivo já exista, a janela ativa será o próprio editor de texto, não o pop-up
if dialogo_aberto.exists() and "ContentDialog" in str(dialogo_aberto.element_info.automation_id):
    print("⚠️ Tela de confirmação detectada! Criando novo arquivo...")
    send_keys('{ENTER}')
    send_keys('{ENTER}')
    sleep(1) # Aguarda o diálogo sumir
else:
    print("✅ O arquivo já existe ou a tela não apareceu. Pulando confirmação.")

sleep(2)
# 3. DIGITAR O TEXTO
# Como o cursor já nasce piscando dentro do campo de texto, basta enviar as teclas diretamente
texto_para_escrever = "Olá!{VK_SPACE}Este{VK_SPACE}texto{VK_SPACE}foi{VK_SPACE}escrito{VK_SPACE}via{VK_SPACE}Python{VK_SPACE}no{VK_SPACE}Windows{VK_SPACE}11."
send_keys(texto_para_escrever)
sleep(0.5)
# 4. SALVAR O ARQUIVO (Atalho: Ctrl + S)
# O '^' representa a tecla CTRL no pywinauto
send_keys('^s')

# 5. FECHAR O BLOCO DE NOTAS (Atalho: Alt + F4)
# O '%' representa a tecla ALT no pywinauto
send_keys('%{F4}')

print("Processo concluído com sucesso!")
